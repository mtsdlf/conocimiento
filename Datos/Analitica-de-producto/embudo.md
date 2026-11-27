---
resumen: >-
  Un embudo es una secuencia ordenada de eventos que se mide como la proporción de usuarios que,
  después de hacer el primero, completa cada paso siguiente dentro de una ventana de tiempo.
estado: borrador
estabilidad: estable
fuentes:
  - "Amplitude, Funnel analysis, build (según su resumen): https://amplitude.com/docs/analytics/charts/funnel-analysis/funnel-analysis-build"
  - "Amplitude, Funnel analysis, interpret (según su resumen): https://amplitude.com/docs/analytics/charts/funnel-analysis/funnel-analysis-interpret"
  - "PostHog, Funnels (según su resumen): https://posthog.com/docs/product-analytics/funnels"
  - "Google, Funnel exploration en GA4 (según su resumen): https://support.google.com/analytics/answer/9327974"
  - "dbt Docs, Metrics: types and definition components, tipo conversion (según su resumen): https://docs.getdbt.com/docs/build/metrics-overview"
  - "Datos/.investigacion/metricas-y-visualizacion.md (sección 2)"
aliases: [funnel, análisis de embudo, funnel analysis, conversión por pasos]
creado: 2026-11-27
revisado:
---

# Embudo

Un embudo es una secuencia ordenada de eventos que se mide como la proporción de usuarios que,
después de hacer el primero, completa cada paso siguiente dentro de una ventana de tiempo.

Es una de las tres formas de contar de la [analítica de producto](analitica-de-producto.md), junto
con la [definición de métrica](definicion-de-metrica.md) y las [cohortes](Cohortes/cohortes.md). La
conversión de un embudo es una métrica más, y lleva sus mismas piezas: numerador, denominador,
unidad contada y ventana. El caso de una tienda, con los eventos de comercio electrónico y las tasas
de checkout, es el [embudo de conversión](../../Comercio-electronico/Checkout-y-conversion/embudo-de-conversion.md).
El embudo de crecimiento AARRR, que va de la adquisición a los ingresos, está en la
[medición de Producto](../../Producto/Medicion/medicion-de-producto.md#heart-y-aarrr-dos-mapas-para-elegir-métricas).

## Conversión global y conversión relativa

Amplitude define la conversión total como "(Users who triggered every event in the funnel) divided
by (Users who triggered the funnel's first event)", y a quien convierte como "one who triggers the
events you specified, in the specified order". PostHog distingue dos formas de leer cada paso: la
global, contra el primer paso, y la relativa, contra el paso anterior.

Un ejemplo con números inventados: 1.000 personas ven un producto, 300 lo agregan al carrito y 60
pagan.

| Paso | Usuarios | Global (contra el primero) | Relativa (contra el anterior) |
|---|---|---|---|
| Ve el producto | 1.000 | 100 % | — |
| Agrega al carrito | 300 | 30 % | 30 % |
| Paga | 60 | 6 % | 20 % |

La global dice cuánto rinde el recorrido entero; la relativa, en qué paso se pierde más gente. Un
informe que dice «convierte el 20 %» sin aclarar cuál de las dos es ambiguo.

## Cinco decisiones que cambian la conversión

Las herramientas de analítica dejan elegir cómo se cuenta un embudo, y no coinciden en los nombres
ni en los valores por defecto. Antes de comparar dos embudos hay que saber qué se eligió en cada
una de estas cinco decisiones.

1. El orden. Se puede exigir que los pasos ocurran en orden con otros eventos en el medio, en
   orden sin nada en el medio o en cualquier orden. Amplitude llama a esos modos "This order",
   "Exact order" y "Any order"; PostHog, "Sequential", "Strict" y "Any order"; GA4 distingue
   "indirectly followed by" de "directly followed by". Un orden estricto da conversiones más bajas (lectura de la base).
2. La entrada. En un embudo cerrado solo cuenta quien empieza en el primer paso; en uno abierto,
   se puede entrar en cualquiera. GA4 ofrece los dos. Es un eje distinto del orden, aunque los dos
   se llamen «estricto» en la conversación.
3. La ventana. Amplitude la define como "the longest a converting user can take between
   entering a funnel and completing it", con un día por defecto (en UTC), un mínimo de un segundo y
   un máximo de 90 días, que en algunas organizaciones llega a 366. PostHog la define como "how long
   a user has to complete the funnel after their first step", sin valor por defecto en su página.
   Una ventana de un día para una compra que se piensa una semana mide casi solo a los impulsivos (lectura de la base).
4. La unidad contada. Amplitude cuenta usuarios únicos por defecto, o el total de eventos si se
   elige. Con eventos, quien agrega tres veces al carrito cuenta tres veces (lectura de la base).
5. La fecha de entrada. Al mirar la conversión en el tiempo, Amplitude ubica a cada usuario en
   el período en que entró al embudo, aunque convierta después. Por eso la conversión de la última
   semana sube a medida que pasan los días, igual que una fila nueva de una
   [tabla de cohortes](Lectura-de-cohortes/tabla-de-cohortes.md) (lectura de la base).

A esto se suman los filtros. Amplitude permite excluir a quien dispara un evento de exclusión entre
dos pasos, y aplica el segmento de usuario solo al evento inicial. En PostHog, un usuario cuyo
evento cae fuera del rango de fechas o no pasa el filtro sale del embudo.

## Armar un embudo desde la tabla de eventos

Cuando la herramienta no da el embudo, o se quiere controlar cada decisión, se calcula desde la
[tabla de eventos](../Modelado-y-almacenamiento/tabla-de-eventos.md) con
[SQL](../Analisis/sql-para-analisis.md) o una planilla:

1. Escribí los pasos y las cinco decisiones de arriba antes de consultar.
2. Para cada usuario, buscá la primera vez que hizo el paso 1 en el período: esa es su fecha de
   entrada.
3. Para cada paso siguiente, buscá la primera vez que lo hizo después del paso anterior y antes de
   que se cierre la ventana contada desde la entrada.
4. Contá cuántos usuarios distintos llegaron a cada paso y dividí por el paso 1 (global) o por el
   anterior (relativa).

Algunas herramientas de definición de métricas traen este cálculo como un tipo de métrica: dbt tiene
uno de conversión, un evento base seguido de un evento de conversión de la misma entidad dentro de
una ventana.

## Lo que un embudo no dice

Un embudo muestra dónde cae la gente, no por qué. Una caída puede venir de un cambio de diseño, de
una campaña que trajo otro tráfico o de un error en el registro de un evento. Mirar el embudo por
[segmento](../Analisis/segmentacion-de-clientes.md) (canal, dispositivo, cliente nuevo o que vuelve) separa la
mezcla de tráfico del recorrido en sí. Saber si un cambio causó una mejora pide un
[experimento A/B](../../Producto/Medicion/experimento-ab.md), y con pocas conversiones, una
diferencia entre dos semanas puede ser ruido: eso es tema de [significancia](../Estadistica/significancia.md).

El embudo tampoco dice si los que convirtieron vuelven. Mide un recorrido corto, dentro de una
ventana; si vuelven lo dice la [retención](Retencion-y-churn/retencion.md).

La explicación más completa de las opciones está en la página "interpret" de Amplitude (fórmula,
ventana y unidad contada) junto con la de PostHog (los modos de orden y la conversión relativa).
Conviene leerlas sabiendo que son de proveedores y que cada una describe sus propios valores por
defecto.
