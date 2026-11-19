---
resumen: >-
  La tasa de retención por cohorte es el porcentaje de los usuarios de una cohorte que
  vuelven a hacer el evento de retorno en el período N contado desde su entrada (día, semana o
  mes N).
estado: borrador
estabilidad: semi
creado: 2026-10-03
fuentes:
  - https://amplitude.com/docs/analytics/charts/retention-analysis/retention-analysis-calculation
  - https://docs.mixpanel.com/docs/reports/retention
  - https://support.google.com/analytics/answer/9670133?hl=en
aliases: [cohort retention, retención de cohorte, retention rate]
---

# Tasa de retención por cohorte

La tasa de retención por cohorte es el porcentaje de los usuarios de una cohorte que
vuelven a hacer el evento de retorno en el período N contado desde su entrada (día, semana o
mes N).

## La fórmula R(c, N)

Cuantifica la [retención](retencion.md) sobre una [cohorte](../Cohortes/cohorte.md):

- **Fórmula**: usuarios de la cohorte *c* que hicieron el evento de retorno en el período *N* ÷
  usuarios de la cohorte *c* al entrar: `R(c, N) = retornados(c, N) / tamaño(c)`.
- **Unidad y grano**: % por cohorte y por período desde la entrada. El período 0 es 100 % por
  definición.
- **Incluye**: a todos los que entraron a la cohorte; el denominador no cambia entre períodos.
- **Excluye**: a quien entró en otra cohorte, aunque haya estado activo en ese período.

## Cómo baja, se aplana y se compara

Baja a medida que crece *N* y, si el producto retiene a alguien, se aplana (ver
[Curva de retención](../Lectura-de-cohortes/curva-de-retencion.md)). Se compara entre cohortes a la misma *N*. Contar el retorno solo en el
período exacto ([retención de N días](retencion-de-n-dias.md)) da números más bajos que contarlo en
ese período o después ([retención unbounded](retencion-unbounded.md)). Su complemento es la
[tasa de churn](tasa-de-churn.md) solo cuando las dos se miden sobre el mismo grupo y período.

## Períodos abiertos, cohortes chicas y el evento de retorno

- Un período que todavía no terminó subestima la retención: se marca o se excluye.
- Las cohortes chicas dan porcentajes ruidosos: 2 de 10 es 20 %, pero dice poco.
- Cambiar el evento de retorno (abrir la app o comprar) cambia el número entero.

## Herramienta o SQL

En una herramienta de analítica de producto (ver [Cohortes en herramientas de analítica](cohortes-en-herramientas-de-analitica.md)) o
con SQL sobre una tabla de eventos (ver [Armar una tabla de cohortes](../Lectura-de-cohortes/armar-una-tabla-de-cohortes.md)).

## Al responder con una retención por cohorte

- **Preguntas que responde**: "¿qué porcentaje de los que llegaron en marzo sigue activo en el
  mes 3?", "¿las cohortes nuevas retienen mejor que las viejas?".
- **Instrucciones**: se indican siempre la cohorte, el evento de retorno, el período y si es de
  N días o unbounded. Para promediar varias cohortes, se pondera cada una por su tamaño.
