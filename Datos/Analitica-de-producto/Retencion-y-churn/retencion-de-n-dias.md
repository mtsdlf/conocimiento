---
resumen: >-
  La retención de N días es el porcentaje de una cohorte que vuelve a hacer el evento de
  retorno exactamente en el día (o semana, o mes) N desde su entrada.
estado: borrador
estabilidad: semi
creado: 2026-10-03
fuentes:
  - https://amplitude.com/docs/analytics/charts/retention-analysis/retention-analysis-interpret
  - https://amplitude.com/docs/analytics/charts/retention-analysis/retention-analysis-calculation
  - https://amplitude.com/docs/analytics/charts/retention-analysis/retention-analysis-time
  - https://posthog.com/docs/product-analytics/retention
aliases: [N-day retention, retención clásica, return on, retención D1 D7 D30]
---

# Retención de N días

La retención de N días es el porcentaje de una cohorte que vuelve a hacer el evento de
retorno exactamente en el día (o semana, o mes) N desde su entrada.

## Qué cuenta la retención de N días

Es una de las dos formas de contar el retorno en la
[tasa de retención por cohorte](tasa-de-retencion-por-cohorte.md).

- **Fórmula**: usuarios de la cohorte que hicieron el evento de retorno en el día *N* exacto ÷
  tamaño de la cohorte.
- **Unidad y grano**: % por cohorte y por día *N* (o semana, o mes). Las más citadas son D1, D7 y
  D30: los días 1, 7 y 30 después de la entrada.
- **Incluye**: solo a quien volvió en ese período exacto.
- **Excluye**: a quien volvió antes o después, pero no en ese período.

## Para productos de uso frecuente

Mide la frecuencia de uso, así que conviene en productos que se usan todos los días o todas las
semanas. La curva puede subir de un período al siguiente, porque cada período se mide por
separado.

## Dónde da números engañosos

- En productos de uso esporádico (viajes, impuestos) da números cercanos a cero aunque el
  cliente siga ahí. En esos casos conviene la [retención unbounded](retencion-unbounded.md) o un
  rango de días ("días 8 a 14").
- Qué es "un día" depende de la herramienta: 24 horas desde la entrada de cada usuario, o el día
  de calendario en la zona horaria del proyecto.

## Cómo se llama en cada herramienta

En Amplitude y PostHog es la opción por defecto; en GA4 corresponde al cálculo "estándar". Los
nombres exactos están en [Cohortes en herramientas de analítica](cohortes-en-herramientas-de-analitica.md).

## Al responder con una D7

- **Preguntas que responde**: "¿qué porcentaje vuelve al día siguiente?", "¿cuál es la D7 de la
  cohorte de esta semana?".
- **Instrucciones**: una D7 de una herramienta no se compara con la retención unbounded de otra.
