---
tipo: concepto
resumen: >-
  Una tabla de cohortes es una matriz con una fila por cohorte y una columna por período
  desde la entrada, donde cada celda muestra la métrica (casi siempre la retención) de esa
  cohorte a esa edad.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - https://support.google.com/analytics/answer/9670133?hl=en
  - https://docs.mixpanel.com/docs/reports/retention
  - https://posthog.com/docs/product-analytics/retention
  - https://amplitude.com/docs/analytics/charts/retention-analysis/retention-analysis-calculation
aliases: [cohort table, triángulo de retención, retention table, cohort chart, matriz de cohortes]
parte_de: []
requiere: [tasa-de-retencion-por-cohorte]
relacionado: [curva-de-retencion]
---

# Tabla de cohortes

Una tabla de cohortes es una matriz con una fila por cohorte y una columna por período
desde la entrada, donde cada celda muestra la métrica (casi siempre la retención) de esa
cohorte a esa edad.

## Por qué importa

Es la forma estándar de mostrar un [análisis de cohortes](analisis-de-cohortes.md): en una vista
se ve cómo cae cada cohorte y si las nuevas retienen mejor que las viejas.

## Cómo funciona

- Filas: las cohortes, de la más vieja (arriba) a la más nueva (abajo), con su tamaño.
- Columnas: el período desde la entrada (semana 0, 1, 2…), no la fecha de calendario.
- Celdas: la [tasa de retención por cohorte](tasa-de-retencion-por-cohorte.md) en ese período. La
  columna 0 es 100 %.

Las cohortes nuevas todavía no vivieron los períodos tardíos, así que la esquina inferior derecha
queda vacía y la tabla toma forma de triángulo. La última celda de cada fila suele ser un período
sin terminar, y se marca.

Se lee de tres formas:

- Una fila muestra cómo decae una cohorte.
- Una columna compara las cohortes a la misma edad.
- Una diagonal junta las cohortes en una misma fecha de calendario: muestra una caída del sitio
  o una campaña.

## Ejemplo

| Cohorte | Usuarios | Sem 0 | Sem 1 | Sem 2 | Sem 3 |
|---|---|---|---|---|---|
| 1 sep | 1.000 | 100 % | 40 % | 31 % | 28 % |
| 8 sep | 1.200 | 100 % | 44 % | 35 % | |
| 15 sep | 900 | 100 % | 47 % | | |

La columna "Sem 1" sube de 40 % a 47 %: las cohortes nuevas retienen mejor en su primera semana.

## No confundir con

Un mapa de calor con fechas de calendario en las columnas muestra actividad, no edad: no alinea
a las cohortes en el mismo punto de su vida.

## Relaciones

- Requiere: [Tasa de retención por cohorte](tasa-de-retencion-por-cohorte.md) — es lo que va en cada celda.
- Relacionado: [Curva de retención](curva-de-retencion.md) — la misma información, con cada fila dibujada como línea.
- Usa: [Cohorte](cohorte.md) — cada fila es una.
