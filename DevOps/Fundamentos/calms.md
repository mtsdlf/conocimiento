---
resumen: >-
  CALMS (Culture, Automation, Lean, Measurement, Sharing) es el marco de cinco dimensiones para
  describir y evaluar cuánto adoptó DevOps una organización.
estado: borrador
estabilidad: estable
fuentes:
  - "John Willis, What DevOps Means to Me, Chef blog (2010): https://www.chef.io/blog/what-devops-means-to-me"
  - "Ian Buchanan, CALMS Framework, Atlassian: https://www.atlassian.com/devops/frameworks/calms-framework"
  - "Archivo/DevOps/devops-referencia.md (original, texto generado con IA)"
aliases: [CAMS, Marco CALMS]
creado: 2026-10-03
revisado:
---

# CALMS

CALMS (Culture, Automation, Lean, Measurement, Sharing) es el marco de cinco dimensiones para
describir y evaluar cuánto adoptó DevOps una organización.

## Por qué no alcanza con comprar herramientas

Una adopción de DevOps que solo compra herramientas suele fallar: automatiza el mismo proceso
con los mismos silos. CALMS obliga a mirar las cinco dimensiones juntas y sirve tanto para
planificar una adopción como para auditar cómo avanza.

## Las cinco dimensiones

John Willis describió CAMS en 2010 como los cuatro pilares de DevOps: cultura, automatización,
medición y compartir. Según Atlassian, Jez Humble sumó la L de Lean y acuñó la sigla CALMS.

| Dimensión | Qué mira |
|---|---|
| **Culture** | Colaboración entre desarrollo, operaciones, QA y seguridad; responsabilidad compartida. |
| **Automation** | Integración y entrega continuas, infraestructura como código, pruebas automáticas. |
| **Lean** | Lotes chicos, límite al trabajo en curso y eliminación de esperas en el [Flujo de valor](../Cultura-y-medicion/flujo-de-valor.md). |
| **Measurement** | Datos sobre la entrega y la operación, como las [Métricas DORA](../Cultura-y-medicion/metricas-dora.md). |
| **Sharing** | Conocimiento abierto, documentación y aprendizaje después de cada incidente. |

Willis pone la cultura primero: sin ella, "todo intento de automatización será infructuoso". La
dimensión Sharing cierra el ciclo, y su práctica más visible es el [Postmortem sin culpa](../Cultura-y-medicion/postmortem-sin-culpa.md).

Para evaluar, se suele ubicar a cada equipo en un nivel de madurez por dimensión (por ejemplo:
inicial, gestionado, definido, medido y optimizado). Esos niveles son una escala de apoyo y no
salen de una fuente única; sirven para priorizar dónde invertir, no para comparar equipos entre
sí.

## Un equipo con pipelines rápidos y aprobaciones lentas

Un equipo tiene pipelines automáticos (Automation alta), pero cada despliegue espera tres días
la aprobación de un comité (Lean baja) y nadie mide cuánto tarda un cambio (Measurement baja).
CALMS muestra que el cuello de botella no es la herramienta sino el proceso.

## CALMS no es un modelo de equipos

Un modelo de equipos. CALMS describe prácticas, no cómo organizar a las personas; eso lo cubre
[Team Topologies](../../Platform-Engineering/Organizacion-de-equipos/team-topologies.md). Crear un "equipo DevOps" aparte no cumple ninguna dimensión: es el
[Anti-patrón del equipo DevOps](../../Platform-Engineering/Colaboracion-Dev-Ops/anti-patron-equipo-devops.md).
