"""Arma la navegación del sitio desde la base, sin una segunda lista que mantener.

- Las áreas y su orden salen de los `## ` de `conocimiento.md`, y cada tema, del primer enlace de
  cada viñeta bajo un área.
- Dentro de un tema, el orden es: su entrada (`<Carpeta>/<carpeta>.md`), las notas sueltas y después
  cada vertical (subcarpeta) con la misma regla.
- `conocimiento.md` es la portada del sitio.
"""
import pathlib
import re

RAIZ = "conocimiento.md"
AREA = re.compile(r"^##\s+(.+?)\s*$")
TEMA = re.compile(r"^-\s+\[([^\]]+)\]\(([^)#\s]+\.md)\)")
H1 = re.compile(r"^#\s+(.+?)\s*$", re.M)


def _titulo(md: pathlib.Path, defecto: str) -> str:
    m = H1.search(md.read_text(encoding="utf-8")) if md.exists() else None
    return m.group(1) if m else defecto


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


def on_files(files, config):
    docs = pathlib.Path(config["docs_dir"])
    incluidos = {f.src_uri for f in files.documentation_pages()}
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
    config["nav"] = nav

    portada = files.get_file_from_path(RAIZ)
    if portada is not None:
        portada.dest_uri = "index.html"
    return files
