---
tipo: metrica
resumen: >-
  La retención unbounded es el porcentaje de una cohorte que vuelve a hacer el evento de
  retorno en el período N o en cualquier período posterior; mide si el usuario sigue "vivo",
  no con qué frecuencia vuelve.
estado: borrador
estabilidad: semi
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - https://amplitude.com/docs/analytics/charts/retention-analysis/retention-analysis-interpret
  - https://docs.mixpanel.com/docs/reports/retention
  - https://posthog.com/docs/product-analytics/retention
aliases: [unbounded retention, rolling retention, retención on or after, retención acumulada]
parte_de: [tasa-de-retencion-por-cohorte]
requiere: [tasa-de-retencion-por-cohorte]
relacionado: [retencion-de-n-dias]
---

# Retención unbounded

La retención unbounded es el porcentaje de una cohorte que vuelve a hacer el evento de
retorno en el período N o en cualquier período posterior; mide si el usuario sigue "vivo",
no con qué frecuencia vuelve.

## Definición

- **Fórmula**: usuarios de la cohorte que hicieron el evento de retorno en el día *N* o después ÷
  tamaño de la cohorte.
- **Unidad y grano**: % por cohorte y por día (o semana, o mes) *N*.
- **Incluye**: a quien volvió en *N* o en cualquier momento posterior, hasta hoy.
- **Excluye**: a quien solo volvió antes de *N*.

## Cómo leerla

La retención unbounded baja o se mantiene a medida que crece *N*, y para la misma *N* queda
por encima de la [[retencion-de-n-dias|retención de N días]]. Conviene en productos de uso irregular. Su
complemento también se lee: 1 menos la retención unbounded en *N* es la proporción que no volvió
nunca desde *N*.

## Limitaciones

- Cambia con el tiempo: un usuario que vuelve hoy sube la retención de días ya pasados, así que
  el número de una cohorte reciente sigue moviéndose.
- Los nombres varían: Amplitude la llama "unbounded" u "on or after", PostHog "rolling" o
  "cumulative", y en GA4 "rolling" y "cumulative" significan otra cosa, porque miran hacia atrás.

## Dónde se calcula

Es la opción por defecto en Mixpanel; en Amplitude y PostHog se elige. Los nombres exactos están
en [[cohortes-en-herramientas-de-analitica]].

## Contexto para agentes

- **Preguntas que responde**: "¿cuántos de los que llegaron en marzo seguían usando el producto
  después del mes 3?".
- **Instrucciones**: se aclara siempre que es unbounded, y no se compara con una retención de N
  días como la D7.

## Relaciones

- Parte de: [[tasa-de-retencion-por-cohorte]] — es una de sus dos formas de contar el retorno.
- Requiere: [[tasa-de-retencion-por-cohorte]] — da por sabidos la fórmula y el denominador.
- Relacionado: [[retencion-de-n-dias]] — la forma exacta por período; da números más bajos.
