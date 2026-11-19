---
tipo: ficha
resumen: >-
  Enlaces comentados a la documentación oficial de cohortes y retención en GA4, Amplitude,
  Mixpanel y PostHog, con la equivalencia de nombres entre herramientas.
estado: borrador
estabilidad: volatil
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - https://support.google.com/analytics/answer/9670133?hl=en
  - https://amplitude.com/docs/analytics/charts/retention-analysis/retention-analysis-interpret
  - https://amplitude.com/docs/analytics/charts/retention-analysis/retention-analysis-calculation
  - https://amplitude.com/docs/analytics/charts/retention-analysis/retention-analysis-time
  - https://docs.mixpanel.com/docs/reports/retention
  - https://docs.mixpanel.com/docs/users/cohorts
  - https://posthog.com/docs/product-analytics/retention
aliases: [GA4 cohort exploration, Amplitude retention, Mixpanel retention, PostHog retention]
parte_de: []
requiere: []
relacionado: []
---

# Cohortes en herramientas de analítica

Enlaces comentados a la documentación oficial de cohortes y retención en GA4, Amplitude,
Mixpanel y PostHog, con la equivalencia de nombres entre herramientas.

## Fuente

- [GA4: exploración de cohortes](https://support.google.com/analytics/answer/9670133?hl=en):
  criterio de inclusión (entrada), criterio de retorno, granularidad diaria, semanal (domingo a
  sábado) o mensual, y tres cálculos: estándar, rolling y cumulative.
- Amplitude:
  [interpretar la retención](https://amplitude.com/docs/analytics/charts/retention-analysis/retention-analysis-interpret),
  [cómo la calcula](https://amplitude.com/docs/analytics/charts/retention-analysis/retention-analysis-calculation) y
  [cómo cuenta los días](https://amplitude.com/docs/analytics/charts/retention-analysis/retention-analysis-time).
  Ofrece "Return On", "Return On or After" y rangos a medida, y explica qué hace con los períodos
  incompletos.
- Mixpanel: [reporte de retención](https://docs.mixpanel.com/docs/reports/retention) y
  [cohorts](https://docs.mixpanel.com/docs/users/cohorts). Cuenta "On or After" por defecto, y
  llama "cohort" a cualquier grupo de usuarios guardado.
- [PostHog: retención](https://posthog.com/docs/product-analytics/retention): cuenta "On" por
  defecto, con retorno por primera vez o recurrente.

## Valores

Equivalencias copiadas el 2026-10-03. Si una herramienta cambia de nombre, manda su
documentación.

| Concepto | GA4 | Amplitude | Mixpanel | PostHog |
|---|---|---|---|---|
| [Retención de N días](retencion-de-n-dias.md) | Estándar | Return On (N-day) | On | On (por defecto) |
| [Retención unbounded](retencion-unbounded.md) | — | Return On or After | On or After (por defecto) | On or after |
| Volver en todos los períodos hasta N | Rolling | — | — | — |
| Volver en algún período hasta N | Cumulative | — | — | — |

"Rolling" y "cumulative" significan cosas distintas según la herramienta. En GA4 miran hacia
atrás: "rolling" pide volver en todos los períodos hasta N, y "cumulative", en alguno. En
PostHog, "rolling" o "cumulative" es volver en N o después. El detalle de "hasta N" en GA4 sale
de un resumen de búsqueda, no de la página, y falta verificarlo.

## Relaciones

- Detalla: [Tasa de retención por cohorte](tasa-de-retencion-por-cohorte.md) — dónde se calcula en cada herramienta.
- Detalla: [Retención de N días](retencion-de-n-dias.md) y [Retención unbounded](retencion-unbounded.md) — cómo se llama cada variante en
  cada herramienta.
