---
tipo: concepto
resumen: >-
  Las métricas DORA son los cinco indicadores de desempeño de entrega de software que publica
  DORA (DevOps Research and Assessment, el programa de investigación de Google Cloud): tres de
  throughput y dos de inestabilidad.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "DORA, DORA's software delivery performance metrics: https://dora.dev/guides/dora-metrics/"
  - "Google Cloud, Using the Four Keys to measure your DevOps performance (2020): https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance"
  - "DORA, A history of DORA's software delivery metrics: https://dora.dev/insights/dora-metrics-history/"
  - "Archivo/DevOps/devops-referencia.md (original, texto generado con IA)"
  - "Archivo/DevOps/git-collaboration-governance.md (original, texto generado con IA)"
aliases: [DORA metrics, Métricas de DORA, Four keys]
parte_de: []
requiere: []
relacionado: [calms, flujo-de-valor]
---

# Métricas DORA

Las métricas DORA son los cinco indicadores de desempeño de entrega de software que publica
DORA (DevOps Research and Assessment, el programa de investigación de Google Cloud): tres de
throughput y dos de inestabilidad.

## Por qué importa

Medir velocidad sola empuja a desplegar sin cuidado; medir estabilidad sola empuja a no
desplegar. DORA mide las dos juntas, y su investigación encuentra que los equipos con mejor
desempeño mejoran en ambas a la vez. Es la forma habitual de medir la dimensión Measurement de
[[calms]].

## Cómo funciona

| Grupo | Métrica | Qué mide |
|---|---|---|
| Throughput | **Change lead time** | Tiempo desde el commit hasta el despliegue en producción. |
| Throughput | **Deployment frequency** | Cantidad de despliegues en un período, o tiempo entre despliegues. |
| Throughput | **Failed deployment recovery time** | Tiempo para recuperarse de un despliegue que falló y exigió intervención inmediata. |
| Inestabilidad | **Change fail rate** | Proporción de despliegues que exigen intervención inmediata. |
| Inestabilidad | **Deployment rework rate** | Proporción de despliegues no planificados, hechos a causa de un incidente en producción. |

Los nombres cambiaron. En el informe de 2023, DORA reemplazó el MTTR (mean time to recover) por
el tiempo de recuperación de un despliegue fallido, porque el MTTR mezclaba fallas causadas por
un cambio con fallas externas, como la caída de un datacenter. En 2024 sumó la tasa de
retrabajo como quinta métrica. Las listas de "cuatro métricas DORA" con MTTR son anteriores a
esos cambios.

"Intervención inmediata" es tener que corregir un despliegue apenas sale: un rollback, un
hotfix o un parche fuera de lo planificado.

## Ejemplo

Un equipo despliega una vez por semana, con lead time de 6 días y 1 de cada 4 despliegues con
rollback. El [[flujo-de-valor]] muestra que 5 de esos 6 días son esperas de aprobación: achicar
esa espera mejora el lead time sin tocar el pipeline.

## No confundir con

Un SLO. Las métricas DORA miden el proceso de entrega; un SLO fija un objetivo de confiabilidad
del servicio (por ejemplo, el 99 % de las peticiones en menos de 200 ms), medido sobre un SLI,
que es el indicador en sí (la latencia). Eso es parte de la [[observabilidad]]. Tampoco son una
meta para comparar equipos entre sí: DORA las propone para que cada equipo mejore contra sí
mismo.

## Relaciones

- Relacionado: [[calms]] — DORA mide la dimensión Measurement.
- Relacionado: [[flujo-de-valor]] — explica dónde se va el lead time que DORA mide.
- Ver también: [[observabilidad]] — donde se definen SLI y SLO.
- Ver también: [[developer-experience]] — mide al desarrollador; DORA mide la entrega.
