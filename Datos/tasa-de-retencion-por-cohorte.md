---
tipo: metrica
resumen: >-
  La tasa de retención por cohorte es el porcentaje de los usuarios de una cohorte que
  vuelven a hacer el evento de retorno en el período N contado desde su entrada (día, semana o
  mes N).
estado: borrador
estabilidad: semi
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - https://amplitude.com/docs/analytics/charts/retention-analysis/retention-analysis-calculation
  - https://docs.mixpanel.com/docs/reports/retention
  - https://support.google.com/analytics/answer/9670133?hl=en
aliases: [cohort retention, retención de cohorte, retention rate]
parte_de: []
requiere: [cohorte, retencion]
relacionado: [tasa-de-churn]
---

# Tasa de retención por cohorte

La tasa de retención por cohorte es el porcentaje de los usuarios de una cohorte que
vuelven a hacer el evento de retorno en el período N contado desde su entrada (día, semana o
mes N).

## Definición

- **Fórmula**: usuarios de la cohorte *c* que hicieron el evento de retorno en el período *N* ÷
  usuarios de la cohorte *c* al entrar: `R(c, N) = retornados(c, N) / tamaño(c)`.
- **Unidad y grano**: % por cohorte y por período desde la entrada. El período 0 es 100 % por
  definición.
- **Incluye**: a todos los que entraron a la cohorte; el denominador no cambia entre períodos.
- **Excluye**: a quien entró en otra cohorte, aunque haya estado activo en ese período.

## Cómo leerla

Baja a medida que crece *N* y, si el producto retiene a alguien, se aplana (ver
[Curva de retención](curva-de-retencion.md)). Se compara entre cohortes a la misma *N*. Contar el retorno solo en el
período exacto ([retención de N días](retencion-de-n-dias.md)) da números más bajos que contarlo en
ese período o después ([retención unbounded](retencion-unbounded.md)).

## Limitaciones

- Un período que todavía no terminó subestima la retención: se marca o se excluye.
- Las cohortes chicas dan porcentajes ruidosos: 2 de 10 es 20 %, pero dice poco.
- Cambiar el evento de retorno (abrir la app o comprar) cambia el número entero.

## Dónde se calcula

En una herramienta de analítica de producto (ver [Cohortes en herramientas de analítica](cohortes-en-herramientas-de-analitica.md)) o
con SQL sobre una tabla de eventos (ver [Armar una tabla de cohortes](armar-una-tabla-de-cohortes.md)).

## Contexto para agentes

- **Preguntas que responde**: "¿qué porcentaje de los que llegaron en marzo sigue activo en el
  mes 3?", "¿las cohortes nuevas retienen mejor que las viejas?".
- **Instrucciones**: se indican siempre la cohorte, el evento de retorno, el período y si es de
  N días o unbounded. Para promediar varias cohortes, se pondera cada una por su tamaño.

## Relaciones

- Requiere: [Cohorte](cohorte.md) — define el denominador.
- Requiere: [Retención](retencion.md) — es la idea que esta métrica cuantifica.
- Relacionado: [Tasa de churn](tasa-de-churn.md) — su complemento solo cuando se mide sobre el mismo grupo y
  período.
