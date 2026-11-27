---
resumen: >-
  La analítica de producto es el análisis aplicado a lo que hacen usuarios y compradores: qué
  acciones registran, en qué orden las hacen y cuántos vuelven, contado con métricas definidas por
  escrito.
estado: borrador
estabilidad: estable
fuentes:
  - "dbt Docs, Metrics: types and definition components (según su resumen): https://docs.getdbt.com/docs/build/metrics-overview"
  - "Amplitude, Funnel analysis, interpret (según su resumen): https://amplitude.com/docs/analytics/charts/funnel-analysis/funnel-analysis-interpret"
  - "PostHog, Funnels (según su resumen): https://posthog.com/docs/product-analytics/funnels"
  - "Datos/.investigacion/metricas-y-visualizacion.md (secciones 1 y 2)"
  - "Datos/.investigacion/posicion-contraria.md (sección 3)"
aliases: [analítica de comportamiento, behavioral analytics, analítica de usuarios]
creado: 2026-11-27
revisado:
---

# Analítica de producto

La analítica de producto es el análisis aplicado a lo que hacen usuarios y compradores: qué
acciones registran, en qué orden las hacen y cuántos vuelven, contado con métricas definidas por
escrito.

Dentro de [Datos](../datos.md), toma el proceso de [Análisis](../Analisis/analisis.md) y lo aplica a
un tipo de dato: el comportamiento. De [Estadística](../Estadistica/estadistica.md) recibe qué se
puede concluir de una diferencia entre dos grupos. Sus números se muestran con
[Visualización y BI](../Visualizacion-y-BI/visualizacion-y-bi.md), donde cada métrica se define una
sola vez en la [capa semántica](../Visualizacion-y-BI/capa-semantica.md).

## Todo sale de una tabla de eventos

Los datos de esta vertical vienen de una [tabla de eventos](../Modelado-y-almacenamiento/tabla-de-eventos.md):
una fila por cada cosa que hizo alguien, con quién la hizo, qué hizo y cuándo. Ver un producto,
agregarlo al carrito, pagar, volver a entrar a la semana: cada una es una fila. Lo que la tabla no
registra no se puede analizar después, y por eso las preguntas de esta vertical terminan muchas
veces en un pedido de registrar un evento nuevo.

Las métricas, el embudo y las cohortes son tres formas de contar las mismas filas (lectura de la
base). Una métrica cuenta y divide. Un embudo cuenta en orden, dentro de una ventana de tiempo. Una
cohorte cuenta a lo largo del tiempo, siguiendo siempre al mismo grupo.

## Tres preguntas y la forma de contar de cada una

| Pregunta | Forma de contar | Nota |
|---|---|---|
| ¿Cuánto, y comparado con qué? | Una métrica con numerador, denominador, ventana y filtros fijados | [Definición de métrica](definicion-de-metrica.md) |
| ¿Dónde se pierde la gente en un recorrido? | La proporción que pasa de cada paso al siguiente | [Embudo](embudo.md) |
| ¿Los que llegaron siguen volviendo? | Grupos fijos por fecha de entrada, comparados a la misma edad | [Cohortes](Cohortes/cohortes.md), [Retención y churn](Retencion-y-churn/retencion-y-churn.md) y [Lectura de cohortes](Lectura-de-cohortes/lectura-de-cohortes.md) |

La definición de métrica va primero porque las otras dos son métricas: la conversión de un embudo y
la retención de una cohorte también tienen numerador, denominador y ventana. Las herramientas de
analítica no coinciden en esos valores por defecto. Según la documentación de dos de ellas, una usa una
ventana de conversión de un día si no se elige otra y la otra no muestra un valor por defecto; el
detalle está en [embudo](embudo.md#cinco-decisiones-que-cambian-la-conversión). Un número que sale de una herramienta sin su definición no se puede comparar con
otro.

## Dónde termina la analítica de producto

Esta vertical dice cómo se define y se calcula un número de comportamiento. Qué número elegir y qué
decidir con él es de otros temas:

- Qué métrica resume el valor de un producto, cuándo un usuario nuevo llegó a ese valor y si un
  cambio causó una diferencia son de la [medición de Producto](../../Producto/Medicion/medicion-de-producto.md):
  [North Star](../../Producto/Medicion/north-star.md), [activación](../../Producto/Medicion/activacion.md)
  y [experimento A/B](../../Producto/Medicion/experimento-ab.md). Esas notas usan las técnicas de acá
  sin repetirlas.
- Si un canal causa las ventas, si cada venta deja plata y qué métrica seguir según la etapa del
  negocio son de la [medición de Marketing](../../Marketing/Medicion/medicion.md):
  [incrementalidad](../../Marketing/Medicion/incrementalidad.md),
  [economía unitaria](../../Marketing/Medicion/economia-unitaria.md) y
  [una métrica que importa](../../Marketing/Medicion/metrica-que-importa.md).
- El embudo de una tienda, con sus eventos y sus tasas de checkout, es el
  [embudo de conversión](../../Comercio-electronico/Checkout-y-conversion/embudo-de-conversion.md)
  de Comercio electrónico.
- La experiencia de uso, medida con tests y cuestionarios, es de [métricas de UX](../../UX/Evaluacion/metricas-de-ux.md).

## Cómo falla un número de comportamiento

Casi todo lo que mide esta vertical es descriptivo. Que los usuarios que usan una función retengan
más es una correlación: puede que la función los retenga o que los más comprometidos la usen más.
Separar una cosa de la otra es tema de [correlación y causalidad](../Estadistica/correlacion-y-causalidad.md)
y, cuando hay volumen para probarlo, del experimento A/B.

La segunda falla es la métrica que se vuelve meta y deja de medir lo que medía, o la que sube sola y
no dice si algo funcionó. Las dos están en [definición de métrica](definicion-de-metrica.md#cuando-la-métrica-se-vuelve-meta).
Contra los tableros llenos de métricas sin decisión no hay estudios con método, solo opinión de
practicantes, según el informe de posición contraria; el criterio de diseño está en
[tablero](../Visualizacion-y-BI/tablero.md).

## Lo que hay adentro de la analítica de producto

- [Definición de métrica](definicion-de-metrica.md) — qué fija una definición para que dos personas lleguen al mismo número; KPI, árbol de métricas, métricas de vanidad y Goodhart. Se lee primero.
- [Embudo](embudo.md) — la conversión paso a paso: orden, ventana, unidad contada y conversión global contra relativa.
- [Cohortes](Cohortes/cohortes.md) — a quién se sigue: grupos fijos por evento y fecha de entrada.
- [Retención y churn](Retencion-y-churn/retencion-y-churn.md) — qué se mide sobre una cohorte: cuántos siguen y cuántos se fueron.
- [Lectura de cohortes](Lectura-de-cohortes/lectura-de-cohortes.md) — la tabla de cohortes y la curva de retención, y cómo se arma la tabla desde eventos.

Para practicar con un caso entero, el [recorrido de análisis de cohortes](../Fundamentos/recorrido-analisis-de-cohortes.md)
va de la cohorte a una tabla armada desde datos crudos.
