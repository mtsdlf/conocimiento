---
resumen: >-
  El análisis de cohortes compara cómo se comporta en el tiempo cada grupo de usuarios que
  empezó en el mismo período, para ver si los grupos nuevos se comportan mejor o peor que los
  anteriores.
estado: borrador
estabilidad: estable
creado: 2026-10-03
fuentes:
  - http://www.brucehardie.com/notes/033/what_is_wrong_with_this_CLV_formula.pdf
  - https://plato.stanford.edu/entries/paradox-simpson/
  - https://archive.cdc.gov/www_cdc_gov/csels/dsepd/ss1978/lesson1/section7.html
  - https://www.publichealth.columbia.edu/research/population-health-methods/age-period-cohort-analysis
aliases: [cohort analysis, análisis de cohorte, análisis por cohortes]
---

# Análisis de cohortes

El análisis de cohortes compara cómo se comporta en el tiempo cada grupo de usuarios que
empezó en el mismo período, para ver si los grupos nuevos se comportan mejor o peor que los
anteriores.

## Por qué un promedio de toda la base engaña

Los promedios de toda la base mezclan usuarios de distintas antigüedades. Si en un mes entran
muchos usuarios nuevos, la [retención](../Retencion-y-churn/retencion.md) promedio cae aunque ninguna [Cohorte](cohorte.md) haya empeorado. Al
revés, una base vieja de clientes fieles puede esconder que los nuevos se van rápido. Separar
por cohorte saca ese efecto de mezcla, un caso de la paradoja de Simpson.

## Comparar cohortes a la misma edad

1. Se agrupa a los usuarios en cohortes, casi siempre de
   [adquisición](cohorte-de-adquisicion.md).
2. Se elige una métrica por período desde el inicio. La más común es la
   [tasa de retención por cohorte](../Retencion-y-churn/tasa-de-retencion-por-cohorte.md); también sirven los ingresos o
   las compras por usuario.
3. Se comparan las cohortes a la misma edad (todas en su semana 4, por ejemplo), en una
   [tabla de cohortes](../Lectura-de-cohortes/tabla-de-cohortes.md) o en [curvas de retención](../Lectura-de-cohortes/curva-de-retencion.md).

Comparar a la misma edad deja una sola diferencia entre las cohortes: la época en que llegaron.

## Enero contra abril, en el mes 3

La cohorte de enero retiene 20 % en el mes 3. La de abril, que llegó después de rediseñar el
onboarding, retiene 28 % en el mes 3. Como las dos se miden a la misma edad, la diferencia no es
efecto del tiempo: algo cambió entre enero y abril, y el rediseño es el primer sospechoso.

## Descriptivo, no causal: la diferencia con epidemiología

Un estudio de cohorte en epidemiología sigue a un grupo para estimar el efecto de una exposición
sobre un desenlace, con un diseño de investigación. En analítica de producto, el análisis de
cohortes es descriptivo: muestra diferencias entre grupos, no prueba causas.
