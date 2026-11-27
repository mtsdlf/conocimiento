---
resumen: >-
  Configuración es la parte del desarrollo que separa del código lo que cambia entre entornos o
  es secreto: el formato en que se escribe, dónde vive cada valor y cómo llega a la app.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Configuración

Configuración es la parte del desarrollo que separa del código lo que cambia entre entornos o
es secreto: el formato en que se escribe, dónde vive cada valor y cómo llega a la app.

Dentro de [Construcción](../construccion.md), en [Desarrollo](../../desarrollo.md), recibe de la [plantilla de proyecto](../plantilla-de-proyecto.md)
los archivos base y decide qué queda fuera de [Git](../Git/git.md): un secreto en un archivo versionado
queda en el historial para siempre, aunque después se borre. Dónde viven los secretos fuera del
código está en [Gestión de secretos](../../../DevOps/DevSecOps/gestion-de-secretos.md).

## El mismo artefacto en todos los entornos

La configuración vive en el entorno, separada del código, para que el mismo artefacto corra en
todos lados. En Spring Boot, el archivo de propiedades guarda solo valores por defecto no
sensibles, y las contraseñas, las API keys y las URLs de servicios externos se inyectan como
variables de entorno o argumentos. En local llegan desde un `.env` que nunca se versiona; en el
clúster, desde un Secret.

## YAML, el formato de la configuración

YAML arma la estructura con escalares, secuencias y mapeos anidados por indentación. Un error de
indentación no siempre falla: puede mover una clave a otro nivel en silencio. Muchos parsers
siguen YAML 1.1, que lee `no`, `yes`, `on` y `off` como booleanos.

## Las cuatro notas de configuración

- [YAML](yaml.md) — qué es YAML y en qué se diferencia de JSON; leerla antes de la ficha.
- [Sintaxis de YAML](sintaxis-de-yaml.md) — la ficha de consulta: multilínea, anchors, tags, booleanos y errores comunes.
- [Configuración externalizada en Spring Boot](configuracion-externalizada-spring-boot.md) — qué va en `application.properties` y qué se
  inyecta desde el entorno; leerla antes de agregar una URL o un secreto a un servicio.
- [Levantar un entorno local con Docker Compose](levantar-un-entorno-local-con-docker-compose.md) — pasos para correr la app con sus
  dependencias y un `.env` propio.
