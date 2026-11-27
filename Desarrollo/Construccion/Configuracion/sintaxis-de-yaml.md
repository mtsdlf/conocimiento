---
resumen: >-
  La sintaxis de YAML 1.2 en tablas: bloques multilínea, anchors y alias, tags, booleanos y
  nulos, comillas, múltiples documentos y errores comunes.
estado: borrador
estabilidad: estable
revisado:
creado: 2026-10-03
fuentes:
  - "YAML Ain't Markup Language (YAML) version 1.2.2 (2021): https://yaml.org/spec/1.2.2/"
  - "YAML 1.1, Boolean Language-Independent Type: https://yaml.org/type/bool.html"
  - "YAML 1.1, Merge Key Language-Independent Type: https://yaml.org/type/merge.html"
  - "Archivo/Desarrollo/yaml-referencia.md (original en inglés, texto generado con IA; menciona una YAML 1.3 que no existe y trata `yes` y `on` como booleanos de 1.2)"
aliases: [Chuleta de YAML, YAML cheat sheet, Sintaxis YAML]
---

# Sintaxis de YAML

La sintaxis de YAML 1.2 en tablas: bloques multilínea, anchors y alias, tags, booleanos y
nulos, comillas, múltiples documentos y errores comunes.

Detalla la sintaxis del concepto [YAML](yaml.md). La especificación vigente es [YAML 1.2.2](https://yaml.org/spec/1.2.2/), de 2021; no existe una
versión 1.3. Muchos parsers siguen YAML 1.1 (PyYAML, SnakeYAML 1.x) y por eso se incluyen las
diferencias que importan.

## La sintaxis, por construcción

**Estructura y comentarios**

| Concepto | Forma |
|---|---|
| Mapeo | `clave: valor` (las claves de un mapeo son únicas) |
| Secuencia | `- valor`, o `[a, b]` en flujo |
| Anidamiento | indentación con espacios; los tabs no valen |
| Comentario | `# hasta el fin de la línea`, precedido de un espacio si va después de un valor |
| Inicio y fin de documento | `---` y `...` |
| Directivas | `%YAML 1.2` (versión), `%TAG` (prefijo de tags), antes del primer `---` |

**Bloques multilínea**: `|` (literal) conserva los saltos de línea; `>` (plegado) los
convierte en espacios, salvo las líneas vacías. El indicador de *chomping* decide los saltos
finales:

| Indicador | Saltos de línea finales |
|---|---|
| `\|` o `>` (clip) | deja uno solo |
| `\|-` o `>-` (strip) | los quita todos |
| `\|+` o `>+` (keep) | los conserva todos |

**Escalares y tipos**

| Tipo | YAML 1.2 (esquema core) | Solo en YAML 1.1 |
|---|---|---|
| Booleano | `true`, `false` (también `True`, `TRUE`) | `yes`, `no`, `on`, `off`, `y`, `n` |
| Nulo | `null`, `Null`, `NULL`, `~`, valor vacío | — |
| Entero | `15`, `0o17` (octal), `0xF` | `017` como octal |

El "problema de Noruega": en un parser YAML 1.1, `pais: NO` se lee como `false`. Para que un
valor sea texto, se pone entre comillas.

**Comillas**: con comillas simples no hay secuencias de escape (`'C:\dir'`, y `''` para una
comilla); con dobles sí (`"línea1\nlínea2"`). Sin comillas, el valor no puede empezar con un
indicador (por ejemplo `[`, `{`, `&`, `*`, `!`, `|`, `>`, `%`, `@`) ni contener `: ` o ` #`.

**Anchors, alias y merge key**

| Forma | Qué hace |
|---|---|
| `&nombre` | marca un nodo para reutilizarlo |
| `*nombre` | repite el nodo marcado |
| `<<: *nombre` | copia las claves de un mapeo en otro |

La merge key `<<` está definida en el repositorio de tipos de YAML 1.1 y no forma parte de la
especificación 1.2; la mayoría de los parsers la aceptan igual.

**Tags**: `!!str 1.2` fuerza texto, `!!int "42"` fuerza entero; `!Local` es un tag propio de la
aplicación (lo usan, por ejemplo, las funciones `!Ref` de CloudFormation).

**Errores comunes** (mensajes de PyYAML; otros parsers dicen lo mismo con otras palabras)

| Mensaje | Causa habitual | Arreglo |
|---|---|---|
| *mapping values are not allowed here* | un `: ` dentro de un valor sin comillas, o indentación corrida | comillas, o alinear |
| *found character that cannot start any token* | un tab, o un carácter reservado (`@`, `` ` ``) al inicio del valor | espacios; comillas |
| *duplicated key* / *duplicate key* | la misma clave dos veces en un mapeo | dejar una |
| *bad indentation of a sequence entry* | un `-` fuera de columna | alinear bajo la clave padre |

**Buenas prácticas**: indentar con dos espacios, poner entre comillas todo texto que pueda
parecer otro tipo (versiones como `"1.10"`, códigos de país, `"on"`), y usar anchors solo para
bloques que de verdad se repiten.

## Ver también

- [Proteger un cliente HTTP con Resilience4j en Spring Boot](../../../Arquitectura/Sistemas-distribuidos/resilience4j-en-spring-boot.md) (Arquitectura) — un `application.yml` real.
