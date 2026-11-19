---
tipo: como-hacer
resumen: >-
  Pasos para armar una tabla de retención por cohorte a partir de una tabla de eventos (con
  SQL o una planilla), cuando la herramienta de analítica no la da o se quiere controlar la
  definición.
estado: borrador
estabilidad: semi
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - https://support.google.com/analytics/answer/9670133?hl=en
  - https://amplitude.com/docs/analytics/charts/retention-analysis/retention-analysis-calculation
aliases: [cómo hacer un análisis de cohortes, cohort table en SQL, tabla de cohortes en Excel]
parte_de: []
requiere: [cohorte-de-adquisicion, tabla-de-cohortes]
relacionado: []
---

# Armar una tabla de cohortes

Pasos para armar una tabla de retención por cohorte a partir de una tabla de eventos (con
SQL o una planilla), cuando la herramienta de analítica no la da o se quiere controlar la
definición.

## Antes de empezar

- Una tabla de eventos con, al menos, el identificador de usuario, el nombre del evento y la
  fecha.
- Saber leer una [Tabla de cohortes](tabla-de-cohortes.md), que es el resultado de estos pasos.
- Cuatro decisiones escritas: el evento de entrada, el evento de retorno, la granularidad (día,
  semana o mes) y la forma de contar el retorno, [N días](retencion-de-n-dias.md) o
  [unbounded](retencion-unbounded.md).

## Pasos

1. Para cada usuario, buscá la fecha mínima del evento de entrada y truncala a la granularidad.
   Queda una fila por usuario con su cohorte.
2. Contá los usuarios distintos por cohorte. Ese es el denominador de cada fila.
3. Para cada evento de retorno, truncá la fecha a la misma granularidad y quedate con los pares
   únicos (usuario, período). Queda cuándo estuvo activo cada usuario.
4. Uní los pasos 1 y 3 por usuario y calculá el número de período: período activo menos
   cohorte. Descartá las edades negativas.
5. Contá los usuarios distintos por (cohorte, número de período). Si contás unbounded, en cada
   celda *N* contá a los usuarios con algún período activo en *N* o después.
6. Dividí cada celda por el tamaño de su cohorte (paso 2).
7. Pivoteá: cohortes en filas, número de período en columnas. Marcá las celdas cuyo período
   todavía no terminó.

## Cómo saber que salió bien

- La columna 0 da 100 % en todas las filas, si el evento de retorno incluye al de entrada.
- Ninguna celda supera 100 %, y la esquina inferior derecha queda vacía: son los períodos que
  las cohortes nuevas todavía no vivieron.
- La suma de los tamaños de cohorte da el total de usuarios distintos con evento de entrada.
- Una celda calculada a mano para un par de usuarios coincide con la tabla.

## Relaciones

- Requiere: [Cohorte de adquisición](cohorte-de-adquisicion.md) — define las filas.
- Requiere: [Tabla de cohortes](tabla-de-cohortes.md) — es la forma del resultado y explica cómo se lee.
- Usa: [Tasa de retención por cohorte](tasa-de-retencion-por-cohorte.md) — es lo que se calcula en cada celda.
