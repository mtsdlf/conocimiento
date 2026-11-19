---
tipo: mapa
resumen: >-
  Herramientas y prácticas de quien escribe software: control de versiones, formatos y
  configuración, generación de proyectos y especificación y prueba de funcionalidades.
estado: borrador
estabilidad: semi
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
parte_de: [conocimiento]
---

# Desarrollo

Herramientas y prácticas de quien escribe software: control de versiones, formatos y
configuración, generación de proyectos y especificación y prueba de funcionalidades.

Los patrones entre servicios (capas de APIs, circuit breaker, saga, idempotencia, multi-tenancy)
están en el Mapa de [Arquitectura](../Arquitectura/arquitectura.md). Cómo se integra y se entrega el código está en
[DevOps](../DevOps/devops.md).

## Sub-Mapas

- [Git](Git/git.md) — el Mapa de las notas sobre Git: cómo funciona por dentro, cómo integrar cambios,
  cómo recuperar trabajo y cómo usarlo en repositorios grandes; la entrada para cualquier duda de
  Git.

## Formatos y configuración

- [YAML](yaml.md) — qué es YAML y en qué se diferencia de JSON; leerla antes de la ficha.
- [Sintaxis de YAML](sintaxis-de-yaml.md) — la ficha de consulta: multilínea, anchors, tags, booleanos y errores comunes.
- [Configuración externalizada en Spring Boot](configuracion-externalizada-spring-boot.md) — qué va en `application.properties` y qué se
  inyecta desde el entorno; leerla antes de agregar una URL o un secreto a un servicio.
- [Levantar un entorno local con Docker Compose](levantar-un-entorno-local-con-docker-compose.md) — pasos para correr la app con sus
  dependencias y un `.env` propio.

## Generar proyectos

- [Arquetipo de Maven](arquetipo-de-maven.md) — qué es una plantilla de proyecto de Maven y cómo se parametriza;
  leerla antes de armar una plantilla para servicios nuevos.
- [Derivar nombres en un arquetipo de Maven](derivar-nombres-en-un-arquetipo-de-maven.md) — pasos para generar nombres de clase a partir del
  `artifactId`.

## Especificar y probar

- [Historia de usuario](historia-de-usuario.md) — cómo se describe una funcionalidad y sus criterios de aceptación;
  leerla antes de escribir el backlog de una funcionalidad.
- [Diseñar casos de prueba de una API](disenar-casos-de-prueba-de-api.md) — pasos para armar la suite de casos de una API REST.

## Originales archivados

El backlog y la suite de pruebas del MVP de e-commerce, y la referencia de YAML en inglés, están
sin cambios en `Archivo/Desarrollo/`. Los manuales de Git que dieron origen al sub-Tema están en
`Archivo/Desarrollo/git/` y en `Archivo/DevOps/git/` (estos últimos llegaron con el Tema DevOps).
