---
resumen: >-
  Una cohorte de adquisición agrupa a los usuarios por el período en que llegaron al producto
  (registro, instalación o primera compra) y es la cohorte por defecto en el análisis de
  retención.
estado: borrador
estabilidad: estable
creado: 2026-10-03
fuentes:
  - https://support.google.com/analytics/answer/9670133?hl=en
  - http://www.brucehardie.com/notes/033/what_is_wrong_with_this_CLV_formula.pdf
aliases: [acquisition cohort, cohorte por fecha de alta, cohorte de alta]
---

# Cohorte de adquisición

Una cohorte de adquisición agrupa a los usuarios por el período en que llegaron al producto
(registro, instalación o primera compra) y es la cohorte por defecto en el análisis de
retención.

## Ver si mejoraron los usuarios nuevos

Responde preguntas como "¿los que llegaron en marzo se quedan más o menos que los que llegaron
en enero?". Así se ve si un cambio de producto, de precio o de canal de adquisición mejoró a los
usuarios nuevos, sin que los veteranos tapen el efecto.

## Un evento de llegada y una granularidad

Es un tipo de [cohorte](cohorte.md), con la llegada como evento de entrada. Se elige un único evento de llegada y una granularidad: día, semana o mes. Cada usuario cae en
una sola cohorte, la del período de su primer evento. La granularidad sigue el ritmo de uso del
producto: diaria para una app de uso diario, mensual para una suscripción.

## La cohorte de julio de una tienda online

En una tienda online, la cohorte "primera compra en julio de 2026" tiene 800 clientes. Se mide
cuántos de ellos vuelven a comprar en agosto, septiembre y octubre.

## Cuándo llegó contra qué hizo

La [cohorte de comportamiento](cohorte-de-comportamiento.md) agrupa por lo que el usuario hizo
(usó una función, completó un paso), no por cuándo llegó. La de adquisición dice *cuándo* empezó
cada grupo; la de comportamiento ayuda a explicar *por qué* unos se quedan más.
