"""Arma el sitio desde la base, sin una segunda lista que mantener ni tocar las notas.

- Navegación: las áreas y su orden salen de los `## ` de `conocimiento.md`, y cada tema, del primer
  enlace de cada viñeta bajo un área. Dentro de un tema van su entrada (`<Carpeta>/<carpeta>.md`),
  las notas sueltas y después cada vertical (subcarpeta) con la misma regla. La entrada de cada
  carpeta es la portada de su sección: se abre al tocar el nombre de la sección.
- Portada: `conocimiento.md`, con cada área como una grilla de tarjetas.
- Cada nota suma, bajo el título, su estado y sus otros nombres (`aliases`, que así también
  encuentra la búsqueda), y al final sus `fuentes` y las notas que la enlazan.
"""
import datetime
import html
import pathlib
import posixpath
import re

RAIZ = "conocimiento.md"
AREA = re.compile(r"^##\s+(.+?)\s*$")
TEMA = re.compile(r"^-\s+\[([^\]]+)\]\(([^)#\s]+\.md)\)")
H1 = re.compile(r"^#\s+(.+?)\s*$", re.M)
FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)
ENLACE = re.compile(r"\]\(([^)\s#]+\.md)(?:#[^)]*)?\)")
URL = re.compile(r"https?://[^\s)>\]]+")
FUENTE = re.compile(r"^(?P<texto>.+?)\s*[:,]?\s*(?P<url>https?://\S+?)\s*(?P<resto>\(.*\))?$")
MESES = "ene feb mar abr may jun jul ago sep oct nov dic".split()

_titulos: dict[str, str] = {}
_entrantes: dict[str, set[str]] = {}


def _titulo(md: pathlib.Path, defecto: str) -> str:
    m = H1.search(md.read_text(encoding="utf-8")) if md.exists() else None
    return m.group(1) if m else defecto


def _es_entrada(src: str) -> bool:
    carpeta, nombre = posixpath.split(src)
    return bool(carpeta) and nombre == f"{posixpath.basename(carpeta).lower()}.md"


def _seccion(carpeta: pathlib.Path, docs: pathlib.Path, incluidos: set[str]) -> list:
    entrada = carpeta / f"{carpeta.name.lower()}.md"
    items: list = []
    if entrada.exists():
        items.append(entrada.relative_to(docs).as_posix())
    for md in sorted(carpeta.glob("*.md")):
        rel = md.relative_to(docs).as_posix()
        if md != entrada and rel in incluidos:
            items.append(rel)
    for sub in sorted(p for p in carpeta.iterdir() if p.is_dir() and not p.name.startswith(".")):
        hijos = _seccion(sub, docs, incluidos)
        if hijos:
            items.append({_titulo(sub / f"{sub.name.lower()}.md", sub.name.replace("-", " ")): hijos})
    return items


def _nav(docs: pathlib.Path, incluidos: set[str]) -> list:
    nav: list = [{"Inicio": RAIZ}]
    area = None
    for linea in (docs / RAIZ).read_text(encoding="utf-8").splitlines():
        if m := AREA.match(linea):
            area = {m.group(1): []}
            nav.append(area)
        elif area is not None and (m := TEMA.match(linea)):
            carpeta = (docs / m.group(2)).parent
            if carpeta != docs:
                next(iter(area.values())).append({m.group(1): _seccion(carpeta, docs, incluidos)})
    nav.append({"Convenciones": "CONVENCIONES.md"})
    return nav


def _grafo(docs: pathlib.Path, incluidos: set[str]) -> None:
    """Quién enlaza a quién, para la sección «Enlazan acá»."""
    _titulos.clear()
    _entrantes.clear()
    for src in incluidos:
        texto = (docs / src).read_text(encoding="utf-8")
        m = H1.search(texto)
        _titulos[src] = m.group(1) if m else posixpath.basename(src)
        for destino in ENLACE.findall(FRONTMATTER.sub("", texto)):
            if "://" in destino:
                continue
            objetivo = posixpath.normpath(posixpath.join(posixpath.dirname(src), destino))
            if objetivo in incluidos and objetivo != src:
                _entrantes.setdefault(objetivo, set()).add(src)


def on_files(files, config):
    docs = pathlib.Path(config["docs_dir"])
    incluidos = {f.src_uri for f in files.documentation_pages()}
    config["nav"] = _nav(docs, incluidos)
    _grafo(docs, incluidos)

    for f in files.documentation_pages():
        if f.src_uri == RAIZ:
            f.dest_uri = "index.html"
        elif _es_entrada(f.src_uri):
            # La entrada de la carpeta hace de índice de su sección (`navigation.indexes`).
            f.name = "index"
            f.dest_uri = posixpath.join(posixpath.dirname(f.src_uri), "index.html")
        else:
            continue
        f.__dict__.pop("url", None)
    return files


def _fecha(valor) -> str:
    if isinstance(valor, (datetime.date, datetime.datetime)):
        return f"{valor.day} {MESES[valor.month - 1]} {valor.year}"
    return str(valor)


def _cabecera(meta: dict) -> str:
    partes = []
    estado = meta.get("estado")
    if estado:
        partes.append(f'<span class="nota-estado nota-estado--{html.escape(str(estado))}">{html.escape(str(estado).capitalize())}</span>')
    if meta.get("revisado"):
        partes.append(f"Revisada el {_fecha(meta['revisado'])}")
    elif meta.get("creado"):
        partes.append(f"Creada el {_fecha(meta['creado'])}")
    linea = " · ".join(partes)
    alias = [str(a) for a in (meta.get("aliases") or [])]
    if alias:
        linea += f'<span class="nota-alias">También: {html.escape(", ".join(alias))}</span>'
    return f'<p class="nota-meta">{linea}</p>' if linea else ""


def _fuente(texto: str) -> str:
    """«Autor, título: URL» se muestra como el título enlazado; lo demás, tal cual."""
    texto = texto.replace("<", "&lt;").replace("[", "\\[").replace("]", "\\]")
    m = FUENTE.match(texto)
    if m and m.group("texto"):
        resto = f" {m.group('resto')}" if m.group("resto") else ""
        return f"[{m.group('texto')}]({m.group('url')}){resto}"
    return URL.sub(lambda u: f"<{u.group(0)}>", texto)


def _pie(page) -> str:
    bloques = []
    fuentes = [str(f) for f in (page.meta.get("fuentes") or [])]
    if fuentes:
        items = "\n".join("- " + _fuente(f) for f in fuentes)
        bloques.append(f'<div class="nota-pie" markdown>\n\n## Fuentes {{ .nota-pie__titulo }}\n\n{items}\n\n</div>')
    src = page.file.src_uri
    entrantes = sorted(_entrantes.get(src, ()), key=lambda s: _titulos.get(s, s).lower())
    if entrantes:
        base = posixpath.dirname(src)
        items = "\n".join(
            f"- [{_titulos.get(s, s)}]({posixpath.relpath(s, base or '.')})" for s in entrantes
        )
        bloques.append(f'<div class="nota-pie" markdown>\n\n## Enlazan acá {{ .nota-pie__titulo }}\n\n{items}\n\n</div>')
    return "\n\n" + "\n\n".join(bloques) if bloques else ""


def _portada(markdown: str) -> str:
    """Cada lista de temas bajo un área pasa a ser una grilla de tarjetas."""
    salida: list[str] = []
    tarjetas: list[str] = []

    def cerrar():
        if tarjetas:
            salida.append('<div class="grid cards temas" markdown>\n')
            salida.extend(tarjetas)
            salida.append("\n</div>\n")
            tarjetas.clear()

    en_area = False
    actual: list[str] | None = None
    for linea in markdown.splitlines():
        if AREA.match(linea):
            if actual is not None:
                tarjetas.append(_tarjeta(actual))
                actual = None
            cerrar()
            en_area = True
            salida.append(linea)
        elif en_area and TEMA.match(linea):
            if actual is not None:
                tarjetas.append(_tarjeta(actual))
            actual = [linea]
        elif en_area and actual is not None and linea.startswith("  "):
            actual.append(linea.strip())
        else:
            if actual is not None:
                tarjetas.append(_tarjeta(actual))
                actual = None
            if linea.strip():
                cerrar()
            salida.append(linea)
    if actual is not None:
        tarjetas.append(_tarjeta(actual))
    cerrar()
    return "\n".join(salida)


def _tarjeta(lineas: list[str]) -> str:
    texto = " ".join(lineas)
    m = TEMA.match(texto)
    resto = texto[m.end():].lstrip(" —-").strip()
    if resto:
        resto = resto[0].upper() + resto[1:]
    return f"- [**{m.group(1)}**]({m.group(2)})\n\n    {resto}\n"


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri == RAIZ:
        page.meta["hide"] = ["navigation", "toc"]
        return _portada(markdown)
    cabecera = _cabecera(page.meta)
    if cabecera:
        markdown = H1.sub(lambda m: f"{m.group(0)}\n\n{cabecera}\n", markdown, count=1)
    return markdown + _pie(page)
