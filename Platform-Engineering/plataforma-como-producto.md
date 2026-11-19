---
tipo: concepto
resumen: >-
  Tratar la plataforma como producto es diseñarla y hacerla evolucionar según las necesidades de
  sus usuarios internos, con dueño, contrato y feedback para cada capacidad, en vez de atender
  pedidos por tickets.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "CNCF TAG App Delivery, Platforms White Paper: https://tag-app-delivery.cncf.io/whitepapers/platforms/"
  - "Matthew Skelton y Manuel Pais, Team Topologies (IT Revolution, 2019), cap. 5: https://teamtopologies.com/book"
aliases: [Platform as a product, Plataforma = producto]
parte_de: []
requiere: []
relacionado: []
---

# Plataforma como producto

Tratar la plataforma como producto es diseñarla y hacerla evolucionar según las necesidades de
sus usuarios internos, con dueño, contrato y feedback para cada capacidad, en vez de atender
pedidos por tickets.

## Por qué importa

Una plataforma construida como proyecto de infraestructura ofrece lo que su equipo cree útil, y
los desarrolladores la esquivan si no les sirve. Según el white paper de plataformas de la CNCF,
una plataforma existe para servir a sus usuarios y se diseña y evoluciona según sus requisitos,
como cualquier otro producto de software.

## Cómo funciona

Tratarla como producto implica:

- **usuarios**: los desarrolladores de los equipos de producto, a quienes se investiga con
  entrevistas, hackathons, issues y encuestas (CNCF);
- **contrato**: cada capacidad tiene una interfaz documentada y versionada que sus usuarios pueden
  esperar que se mantenga;
- **dueño**: cada capacidad tiene un responsable de su evolución. Una forma de fijarlo es una
  tabla que asigna a cada capacidad un responsable, un suplente, un referente de cumplimiento y
  un canal de feedback;
- **adopción opcional**: según la CNCF, los equipos usan solo las partes que les sirven; si nadie
  usa una capacidad, eso es información de producto;
- **métricas**: la satisfacción de los usuarios (por ejemplo, Net Promoter Score) y las métricas
  de entrega como la frecuencia de despliegue y el tiempo de restauración.

## Ejemplo

El equipo de plataforma encuesta a los desarrolladores cada trimestre y descubre que crear un
entorno de pruebas lleva dos días. Prioriza esa capacidad por encima de migrar el clúster, aunque
la migración le resultaba más interesante.

## No confundir con

Una mesa de ayuda. Un equipo que atiende tickets responde pedidos de a uno; un equipo de producto
busca qué necesitan muchos equipos y lo resuelve una vez, como servicio.

## Relaciones

- Base de: [Platform team](platform-team.md) — es la forma de trabajo que define a ese equipo.
- Base de: [Internal Developer Platform](internal-developer-platform.md) — la plataforma que se construye con este enfoque.
