---
resumen: >-
  Cultura y medición es la parte de DevOps que mira cómo trabaja la organización: por dónde pasa un
  cambio hasta producción, cómo se aprende de un incidente y con qué números se sabe si la entrega
  mejora.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Cultura y medición

Cultura y medición es la parte de DevOps que mira cómo trabaja la organización: por dónde pasa un
cambio hasta producción, cómo se aprende de un incidente y con qué números se sabe si la entrega
mejora.

Dentro de [DevOps](../devops.md), acá caen las dimensiones Culture, Lean, Measurement y Sharing de
[CALMS](../Fundamentos/calms.md); la automatización vive en
[Integración y entrega](../Integracion-y-entrega/integracion-y-entrega.md). Mide el resultado de
todas las otras partes: los despliegues que salen de [Despliegue](../Despliegue/despliegue.md) son
lo que cuentan las métricas DORA.

## El resultado y la causa

Las métricas DORA dan el resultado: tres de throughput y dos de inestabilidad, medidas juntas
porque medir velocidad sola empuja a desplegar sin cuidado y medir estabilidad sola empuja a no
desplegar. El flujo de valor explica la causa: mapeado etapa por etapa, muestra que la mayor parte
del tiempo no es trabajo sino espera entre tramos. Ninguno de los dos sirve para comparar equipos
entre sí; DORA propone las métricas para que cada equipo mejore contra sí mismo.

## Aprender de un incidente sin culpar

Si se señala a quien "hizo lo incorrecto", la gente deja de reportar problemas, y el mismo
incidente se repite. El postmortem sin culpa supone que cada persona actuó con buena intención y
con la información que tenía, y busca por qué el sistema permitió el error. Es la práctica central
de Culture y Sharing.

## Qué hay adentro de cultura y medición

- [Flujo de valor](flujo-de-valor.md) — el recorrido de un cambio de la idea a producción, cómo se mapea y cómo se acelera.
- [Métricas DORA](metricas-dora.md) — los cinco indicadores de desempeño de entrega, con sus nombres actuales.
- [Postmortem sin culpa](postmortem-sin-culpa.md) — cómo analizar un incidente para mejorar el sistema y no castigar personas.
