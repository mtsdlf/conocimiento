---
resumen: >-
  La retención unbounded es el porcentaje de una cohorte que vuelve a hacer el evento de
  retorno en el período N o en cualquier período posterior; mide si el usuario sigue "vivo",
  no con qué frecuencia vuelve.
estado: borrador
estabilidad: semi
creado: 2026-10-03
fuentes:
  - https://amplitude.com/docs/analytics/charts/retention-analysis/retention-analysis-interpret
  - https://docs.mixpanel.com/docs/reports/retention
  - https://posthog.com/docs/product-analytics/retention
aliases: [unbounded retention, rolling retention, retención on or after, retención acumulada]
---

# Retención unbounded

La retención unbounded es el porcentaje de una cohorte que vuelve a hacer el evento de
retorno en el período N o en cualquier período posterior; mide si el usuario sigue "vivo",
no con qué frecuencia vuelve.

## Qué cuenta la retención unbounded

Es una de las dos formas de contar el retorno en la
[tasa de retención por cohorte](tasa-de-retencion-por-cohorte.md).

- **Fórmula**: usuarios de la cohorte que hicieron el evento de retorno en el día *N* o después ÷
  tamaño de la cohorte.
- **Unidad y grano**: % por cohorte y por día (o semana, o mes) *N*.
- **Incluye**: a quien volvió en *N* o en cualquier momento posterior, hasta hoy.
- **Excluye**: a quien solo volvió antes de *N*.

## Si el usuario sigue vivo

La retención unbounded baja o se mantiene a medida que crece *N*, y para la misma *N* queda
por encima de la [retención de N días](retencion-de-n-dias.md). Conviene en productos de uso irregular. Su
complemento también se lee: 1 menos la retención unbounded en *N* es la proporción que no volvió
nunca desde *N*.

## Un número que se sigue moviendo y nombres que cambian

- Cambia con el tiempo: un usuario que vuelve hoy sube la retención de días ya pasados, así que
  el número de una cohorte reciente sigue moviéndose.
- Los nombres varían: Amplitude la llama "unbounded" u "on or after", PostHog "rolling" o
  "cumulative", y en GA4 "rolling" y "cumulative" significan otra cosa, porque miran hacia atrás.

## Cómo se llama en cada herramienta

Es la opción por defecto en Mixpanel; en Amplitude y PostHog se elige. Los nombres exactos están
en [Cohortes en herramientas de analítica](cohortes-en-herramientas-de-analitica.md).

## Al responder con una retención unbounded

- **Preguntas que responde**: "¿cuántos de los que llegaron en marzo seguían usando el producto
  después del mes 3?".
- **Instrucciones**: se aclara siempre que es unbounded, y no se compara con una retención de N
  días como la D7.
