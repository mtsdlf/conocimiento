---
tipo: concepto
resumen: >-
  YAML es un formato de serialización de datos legible por personas, que arma la estructura con
  escalares, secuencias y mapeos anidados por indentación; desde la versión 1.2, todo JSON válido
  es YAML válido.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "YAML Ain't Markup Language (YAML) version 1.2.2 (2021): https://yaml.org/spec/1.2.2/"
  - "Archivo/Desarrollo/yaml-referencia.md (original en inglés, texto generado con IA)"
aliases: [YAML Ain't Markup Language, .yml, .yaml]
parte_de: []
requiere: []
relacionado: [configuracion-externalizada-spring-boot]
---

# YAML

YAML es un formato de serialización de datos legible por personas, que arma la estructura con
escalares, secuencias y mapeos anidados por indentación; desde la versión 1.2, todo JSON válido
es YAML válido.

## Por qué importa

YAML es el formato de los manifiestos de Kubernetes, los workflows de GitHub Actions, los
playbooks de Ansible y el `application.yml` de Spring Boot. Un error de indentación no siempre
falla: puede cambiar la estructura en silencio y mover una clave a otro nivel. Entender el modelo
evita esos errores.

## Cómo funciona

Todo documento YAML se arma con tres estructuras:

| Estructura | Qué es | Ejemplo en bloque | Ejemplo en flujo |
|---|---|---|---|
| **Escalar** | un valor: texto, número, booleano o nulo | `puerto: 8080` | — |
| **Secuencia** | una lista ordenada | `- web` en cada línea | `[web, db]` |
| **Mapeo** | pares clave–valor con claves únicas | `nombre: app` en cada línea | `{nombre: app}` |

En el **estilo de bloque**, la indentación con espacios define el anidamiento; los tabs no valen
para indentar. El **estilo de flujo** usa llaves, corchetes y comas, como JSON. Los dos se pueden
mezclar en un mismo archivo.

El tipo de un escalar sin comillas lo decide el **esquema** del parser: `42` es entero y `true`
es booleano. Con comillas es texto, salvo que un tag explícito diga otra cosa. La versión vigente de la especificación es la 1.2.2,
de 2021; no hay una 1.3. Muchos parsers todavía siguen YAML 1.1, que interpreta `no`, `yes`, `on`
y `off` como booleanos; los detalles están en [Sintaxis de YAML](sintaxis-de-yaml.md).

Un archivo puede tener varios documentos separados por `---`, como los manifiestos de Kubernetes
que definen un Deployment y un Service juntos.

## Ejemplo

```yaml
servicio:
  nombre: catalogo
  puertos: [8080, 8081]
  base:
    host: db
    ssl: true
```

El mismo dato en JSON es `{"servicio": {"nombre": "catalogo", "puertos": [8080, 8081], "base":
{"host": "db", "ssl": true}}}`, y un parser YAML 1.2 lo lee igual.

## No confundir con

JSON. JSON no admite comentarios, anchors ni varios documentos por archivo, y sus tipos no
dependen de un esquema. YAML suma todo eso a costa de reglas de indentación y de tipado que JSON
no tiene.

## Relaciones

- Detallada en: [Sintaxis de YAML](sintaxis-de-yaml.md) — la ficha con la sintaxis completa y los errores comunes.
- Relacionado: [Configuración externalizada en Spring Boot](configuracion-externalizada-spring-boot.md) — `application.yml` es una de las fuentes de configuración de Spring Boot.
