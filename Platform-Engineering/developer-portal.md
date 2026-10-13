---
tipo: concepto
resumen: >-
  Un developer portal es la interfaz web que reúne el catálogo de software, la documentación y las
  acciones self-service de la plataforma; presenta las capacidades de la plataforma, pero no las
  implementa.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Backstage, What is Backstage?: https://backstage.io/docs/overview/what-is-backstage"
  - "Ajay Chankramath, Nic Cheneweth, Bryan Oliver y Sean Alvarez, Effective Platform Engineering (Manning), sección 3.3.3: https://livebook.manning.com/book/effective-platform-engineering/chapter-3/v-1/"
  - "CNCF TAG App Delivery, Platforms White Paper: https://tag-app-delivery.cncf.io/whitepapers/platforms/"
aliases: [Portal de desarrolladores, Portal interno, Internal developer portal]
parte_de: [internal-developer-platform]
requiere: []
relacionado: [plataforma-api-first, golden-path]
---

# Developer portal

Un developer portal es la interfaz web que reúne el catálogo de software, la documentación y las
acciones self-service de la plataforma; presenta las capacidades de la plataforma, pero no las
implementa.

## Por qué importa

Cuando la documentación, los dueños de cada servicio y las formas de pedir recursos están
repartidos en wikis, chats y repositorios, buscarlos es carga cognitiva extrínseca. Según
Effective Platform Engineering, una fuente central de documentación, recursos y feedback es una de
las técnicas para reducirla, y un portal como Backstage le da estructura si se implementa bien.

## Cómo funciona

Para la CNCF, el portal es una de las interfaces de la plataforma, junto con la CLI y la API: la
web para observar y pedir capacidades. Backstage, creado en Spotify y hoy proyecto en incubación
de la CNCF, se define como "un framework open source para construir developer portals" y tiene
tres piezas centrales:

- **catálogo de software**: todos los servicios, librerías, pipelines de datos y modelos, con su
  dueño;
- **plantillas de software**: para crear proyectos nuevos según las prácticas de la organización,
  que es donde viven los [[golden-path|golden paths]];
- **TechDocs**: documentación escrita como código, junto al repositorio.

El portal no tiene lógica de negocio propia: consume las APIs de la plataforma
([[plataforma-api-first]]). Como inferencia: si el portal crea recursos por su cuenta, la CLI y
la automatización no pueden hacer lo mismo y las reglas quedan duplicadas.

## Ejemplo

Una desarrolladora nueva abre el portal, busca "pagos" en el catálogo, ve qué equipo es dueño del
servicio, lee su documentación y, desde el mismo portal, crea un servicio nuevo con la plantilla
de API en Java.

## No confundir con

La [[internal-developer-platform]] entera. El portal es una ventana a la plataforma; quitarlo no
debería impedir pedir un recurso por la CLI o la API.

## Relaciones

- Parte de: [[internal-developer-platform]] — una de sus interfaces.
- Relacionado: [[plataforma-api-first]] — el portal es una presentación de esas APIs.
- Relacionado: [[golden-path]] — las plantillas que el portal ofrece.
