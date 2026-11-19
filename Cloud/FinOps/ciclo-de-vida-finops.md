---
tipo: concepto
resumen: >-
  La práctica de FinOps avanza en tres fases que se repiten (Inform, Optimize y Operate) y madura
  cada capacidad por separado en tres niveles: Crawl, Walk y Run.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "FinOps Foundation, FinOps Phases: https://www.finops.org/framework/phases/"
  - "FinOps Foundation, FinOps Maturity Model: https://www.finops.org/framework/maturity-model/"
  - "FinOps Foundation, FinOps Framework: https://www.finops.org/framework/"
aliases: [fases de FinOps, Inform Optimize Operate, Crawl Walk Run, madurez FinOps]
parte_de: [que-es-finops]
requiere: [que-es-finops]
relacionado: []
---

# Ciclo de vida de FinOps

La práctica de FinOps avanza en tres fases que se repiten (Inform, Optimize y Operate) y madura
cada capacidad por separado en tres niveles: Crawl, Walk y Run.

## Por qué importa

Las fases dicen qué hacer primero: no se optimiza lo que no se ve. El modelo de madurez evita
querer automatizar todo de entrada: se arranca chico y se crece donde el valor lo justifica.

## Cómo funciona

**Las fases**, según la FinOps Foundation:

| Fase | Qué se hace | Capacidades que la alimentan |
|---|---|---|
| **Inform** | Mirar los datos de costo, uso y eficiencia para saber dónde se está | Ingesta de datos, asignación, reportes, pronóstico, economía unitaria |
| **Optimize** | Buscar oportunidades de mejorar la eficiencia y el valor con lo que mostró Inform | Optimización de uso, optimización de tarifas, ubicación de cargas |
| **Operate** | Aplicar los cambios que salieron de Optimize | Gobernanza, automatización, educación |

El ciclo no es una secuencia única: la Foundation dice que los equipos lo recorren rápido y
vuelven a Inform y Optimize de forma continua. Una misma organización puede estar en Operate para
el cómputo y en Inform para el almacenamiento.

**La madurez** se mide por capacidad, no para toda la organización:

- **Crawl**: pocos reportes y herramientas, indicadores básicos y un plan para lo más fácil de
  ahorrar.
- **Walk**: la capacidad se entiende y se sigue en la organización; automatización o procesos
  cubren la mayor parte.
- **Run**: todos los equipos la entienden y la siguen; automatizar es la forma preferida.

El modelo oficial tiene esos tres niveles y nada más.

## Ejemplo

Un equipo empieza en Crawl en asignación: etiqueta a mano los recursos de producción y publica un
reporte mensual (Inform). Encuentra discos sin usar (Optimize) y los borra con un script (Operate).
Cuando una política obliga las etiquetas al crear recursos, la asignación pasa a Walk.

## No confundir con

Las fases de un pipeline de CI/CD. Inform, Optimize y Operate no son pasos de un despliegue sino
un ciclo de gestión que puede durar semanas por vuelta.

## Relaciones

- Parte de y requiere: [FinOps](que-es-finops.md) — las fases organizan los principios en trabajo concreto.
- Usa: [Showback y chargeback](showback-y-chargeback.md) y [Costo unitario](costo-unitario.md) — dos capacidades centrales de la fase Inform.
