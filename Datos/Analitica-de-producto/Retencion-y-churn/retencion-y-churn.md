---
resumen: >-
  Retención y churn es la parte del análisis que dice qué se mide sobre una cohorte: cuántos
  siguen usando o pagando el producto y cuántos se fueron, con las métricas que lo cuentan.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Retención y churn

Retención y churn es la parte del análisis que dice qué se mide sobre una cohorte: cuántos
siguen usando o pagando el producto y cuántos se fueron, con las métricas que lo cuentan.

Dentro de [Analítica de producto](../analitica-de-producto.md), parte de [Datos](../../datos.md), recibe de [Cohortes](../Cohortes/cohortes.md) el grupo que se sigue y
su tamaño, que es el denominador. Sus tasas son lo que va en cada celda de la tabla y en cada punto
de la curva de [Lectura de cohortes](../Lectura-de-cohortes/lectura-de-cohortes.md).

## El mismo fenómeno desde los dos lados

La retención mira a los que se quedan; el churn, a los que se van. La retención decide cuánto vale
cada usuario adquirido, y un churn alto pone techo al crecimiento. Las dos suman 100 % solo si se
miden sobre el mismo grupo, el mismo período y la misma definición de "seguir": la retención de
una cohorte en el mes 3 y el churn mensual de toda la base no suman 100 %.

Irse también se define. En una suscripción el cliente cancela o no renueva; en un producto sin
contrato, el churn se declara por una ventana de inactividad, y esa ventana cambia el número.

## Dos formas de contar el retorno

La tasa de retención por cohorte es la métrica central: el porcentaje de la cohorte que vuelve en
el período N. Contar el retorno solo en el período exacto (retención de N días) conviene en
productos de uso frecuente; contarlo en ese período o después (retención unbounded) da números más
altos y conviene en productos de uso irregular. Las herramientas de analítica usan nombres
distintos para cada forma, y "rolling" y "cumulative" no significan lo mismo en todas.

La tasa de churn, en cambio, promedia toda la base: mezcla clientes nuevos, que se van más, con
veteranos, que se van menos. Para ver si los nuevos se van más rápido se usa la retención por
cohorte.

## Lo que hay adentro de retención y churn

- [Retención](retencion.md) — qué significa que un usuario "se quede" y las tres cosas que se definen para
  medirlo.
- [Churn](churn.md) — la pérdida de clientes; cómo se define "irse" con contrato y sin él.
- [Tasa de retención por cohorte](tasa-de-retencion-por-cohorte.md) — la métrica central: % de la cohorte que vuelve en el
  período N.
- [Retención de N días](retencion-de-n-dias.md) — volver en el período exacto (D1, D7, D30); para productos de uso
  frecuente.
- [Retención unbounded](retencion-unbounded.md) — volver en N o después; para productos de uso irregular.
- [Tasa de churn](tasa-de-churn.md) — % de la base que se va en un período, y por qué el promedio engaña.
- [Cohortes en herramientas de analítica](cohortes-en-herramientas-de-analitica.md) — ficha: dónde está la retención en GA4, Amplitude,
  Mixpanel y PostHog, y cómo se llama cada variante en cada una; copiada el 2026-10-03.
