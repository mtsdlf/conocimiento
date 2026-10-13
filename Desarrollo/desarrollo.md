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
están en el Mapa de [[arquitectura]]. Cómo se integra y se entrega el código está en
[[devops]].

## Sub-Mapas

- [[git]] — el Mapa de las notas sobre Git: cómo funciona por dentro, cómo integrar cambios,
  cómo recuperar trabajo y cómo usarlo en repositorios grandes; la entrada para cualquier duda de
  Git.

## Formatos y configuración

- [[yaml]] — qué es YAML y en qué se diferencia de JSON; leerla antes de la ficha.
- [[sintaxis-de-yaml]] — la ficha de consulta: multilínea, anchors, tags, booleanos y errores comunes.
- [[configuracion-externalizada-spring-boot]] — qué va en `application.properties` y qué se
  inyecta desde el entorno; leerla antes de agregar una URL o un secreto a un servicio.
- [[levantar-un-entorno-local-con-docker-compose]] — pasos para correr la app con sus
  dependencias y un `.env` propio.

## Generar proyectos

- [[arquetipo-de-maven]] — qué es una plantilla de proyecto de Maven y cómo se parametriza;
  leerla antes de armar una plantilla para servicios nuevos.
- [[derivar-nombres-en-un-arquetipo-de-maven]] — pasos para generar nombres de clase a partir del
  `artifactId`.

## Especificar y probar

- [[historia-de-usuario]] — cómo se describe una funcionalidad y sus criterios de aceptación;
  leerla antes de escribir el backlog de una funcionalidad.
- [[disenar-casos-de-prueba-de-api]] — pasos para armar la suite de casos de una API REST.

## Originales archivados

El backlog y la suite de pruebas del MVP de e-commerce, y la referencia de YAML en inglés, están
sin cambios en `Archivo/Desarrollo/`. Los manuales de Git que dieron origen al sub-Tema están en
`Archivo/Desarrollo/git/` y en `Archivo/DevOps/git/` (estos últimos llegaron con el Tema DevOps).
