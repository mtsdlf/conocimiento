#!/usr/bin/env python3
"""Revisa los enlaces a secciones (`nota.md#ancla`, `#ancla`) contra los títulos de la nota destino.

Los ids son los de GitHub, que el sitio también genera (`sitio/mkdocs.yml`, `toc.slugify`, y
`nav.py` para los repetidos): el título en minúsculas, con tildes y eñes, sin la puntuación salvo
`-` y `_`, los espacios a guiones, y `-1`, `-2`... a los títulos repetidos en la misma nota.

    python3 sitio/anclas.py            # lista las anclas rotas; sale con 1 si hay alguna
    python3 sitio/anclas.py --arreglar # reescribe las que coinciden con un título al quitar
                                       # tildes y puntuación, y lista las que no coinciden con nada

Solo biblioteca estándar. Deja afuera `.investigacion/`, `Archivo/` y las carpetas ocultas.
"""
import html
import pathlib
import re
import sys
import unicodedata
from urllib.parse import unquote

RAIZ = pathlib.Path(__file__).resolve().parent.parent
EXCLUIDAS = {"Archivo", "sitio"}

FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)
CERCO = re.compile(r"^\s*(```|~~~)")
TITULO = re.compile(r"^(#{1,6})[ \t]+(.+?)(?:[ \t]+#+)?[ \t]*$")
ENLACE = re.compile(r"(\]\()([^)\s#]*)#([^)\s]+)(\))")
CODIGO = re.compile(r"(`+).*?\1")
IMAGEN_O_ENLACE = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
ETIQUETA = re.compile(r"</?[^>]*>")
GUION_BAJO = re.compile(r"(?<!\w)_+|_+(?!\w)")
# Lo que GitHub (github-slugger) saca: todo lo que no sea letra, número, marca, `-`, `_` o espacio.
NO_VA = re.compile(r"[^\w\- ]")


def slug(texto: str) -> str:
    """El id que GitHub le da a un título (sin contar repetidos)."""
    texto = unicodedata.normalize("NFC", texto).lower()
    return NO_VA.sub("", texto).replace(" ", "-")


def texto_del_titulo(crudo: str) -> str:
    """El texto que se ve del título: sin enlaces, código, etiquetas ni marcas de énfasis."""
    crudo = CODIGO.sub(lambda m: m.group(0).strip("`").strip(), crudo)
    crudo = IMAGEN_O_ENLACE.sub(r"\1", crudo)
    crudo = ETIQUETA.sub("", crudo)
    crudo = GUION_BAJO.sub("", crudo)
    return html.unescape(crudo).strip()


def normal(ancla: str) -> str:
    """Para comparar sin tildes, mayúsculas ni puntuación."""
    ancla = unicodedata.normalize("NFKD", unquote(ancla).lower())
    return "".join(c for c in ancla if c.isalnum() and not unicodedata.combining(c))


def lineas_fuera_de_codigo(texto: str):
    """(número de línea, línea) de lo que no está en un bloque de código."""
    dentro = None
    for i, linea in enumerate(texto.split("\n")):
        m = CERCO.match(linea)
        if m:
            if dentro is None:
                dentro = m.group(1)
            elif m.group(1) == dentro:
                dentro = None
            continue
        if dentro is None:
            yield i, linea


def ids(nota: pathlib.Path) -> list[str]:
    """Los ids de los títulos de una nota, con `-1`, `-2`... para los repetidos, como GitHub."""
    texto = nota.read_text(encoding="utf-8")
    m = FRONTMATTER.match(texto)
    cuerpo = texto[m.end():] if m else texto
    usados: dict[str, int] = {}
    salida = []
    for _, linea in lineas_fuera_de_codigo(cuerpo):
        t = TITULO.match(linea)
        if not t:
            continue
        base = slug(texto_del_titulo(t.group(2)))
        nuevo = base
        while nuevo in usados:
            usados[base] += 1
            nuevo = f"{base}-{usados[base]}"
        usados[nuevo] = 0
        salida.append(nuevo)
    return salida


def notas(raiz: pathlib.Path):
    for md in sorted(raiz.rglob("*.md")):
        partes = md.relative_to(raiz).parts
        if any(p.startswith(".") or p in EXCLUIDAS for p in partes[:-1]):
            continue
        yield md


def revisar(raiz: pathlib.Path, arreglar: bool) -> tuple[int, list[str]]:
    cache: dict[pathlib.Path, list[str]] = {}
    corregidos = 0
    rotos: list[str] = []
    for nota in notas(raiz):
        texto = nota.read_text(encoding="utf-8")
        lineas = texto.split("\n")
        cambio = False
        for i, linea in lineas_fuera_de_codigo(texto):
            if "#" not in linea:
                continue
            sin_codigo = CODIGO.sub(lambda m: "\0" * len(m.group(0)), linea)

            def reemplazar(m: re.Match) -> str:
                nonlocal corregidos, cambio
                if sin_codigo[m.start()] == "\0":
                    return m.group(0)
                ruta, ancla = m.group(2), m.group(3)
                if "://" in ruta or ruta.startswith("mailto:") or (ruta and not ruta.endswith(".md")):
                    return m.group(0)
                destino = (nota.parent / unquote(ruta)).resolve() if ruta else nota
                lugar = f"{nota.relative_to(raiz)}:{i + 1}: {ruta}#{ancla}"
                if not destino.is_file():
                    rotos.append(f"{lugar} (no existe la nota)")
                    return m.group(0)
                if destino not in cache:
                    cache[destino] = ids(destino)
                validos = cache[destino]
                if unquote(ancla) in validos:
                    return m.group(0)
                candidatos = [v for v in validos if normal(v) == normal(ancla)]
                if len(candidatos) == 1:
                    if arreglar:
                        corregidos += 1
                        cambio = True
                        print(f"corregido  {lugar} -> #{candidatos[0]}")
                        return f"{m.group(1)}{ruta}#{candidatos[0]}{m.group(4)}"
                    rotos.append(f"{lugar} (se arregla: #{candidatos[0]})")
                else:
                    rotos.append(f"{lugar} (no hay un título que coincida)")
                return m.group(0)

            nueva = ENLACE.sub(reemplazar, linea)
            if nueva != linea:
                lineas[i] = nueva
        if cambio:
            nota.write_text("\n".join(lineas), encoding="utf-8")
    return corregidos, rotos


def main() -> int:
    arreglar = "--arreglar" in sys.argv[1:]
    corregidos, rotos = revisar(RAIZ, arreglar)
    for r in rotos:
        print(f"roto       {r}")
    if arreglar:
        print(f"\n{corregidos} anclas corregidas, {len(rotos)} sin resolver")
    else:
        print(f"\n{len(rotos)} anclas rotas")
    return 1 if rotos else 0


if __name__ == "__main__":
    sys.exit(main())
