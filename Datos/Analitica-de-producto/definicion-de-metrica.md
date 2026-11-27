---
resumen: >-
  Una definición de métrica es la receta escrita que fija qué se cuenta, sobre qué total, en qué
  ventana y con qué filtros, para que dos personas que la siguen sobre los mismos datos lleguen al
  mismo número.
estado: vigente
estabilidad: semi
fuentes:
  - "dbt Docs, Metrics: types and definition components (según su resumen): https://docs.getdbt.com/docs/build/metrics-overview"
  - "Eric Ries, Why Vanity Metrics Are Dangerous, reimpresión (según su resumen): https://nextbigideaclub.com/magazine/ericries-vanity-metrics-dangerous/4781/istock_000028679138_large-2/"
  - "Marilyn Strathern, 'Improving Ratings': Audit in the British University System, European Review 5(3), 305-321 (1997), solo la ficha: https://ideas.repec.org/a/cup/eurrev/v5y1997i03p305-321_00.html"
  - "Wikipedia, Goodhart's law (citas de Goodhart 1975, Hoskin 1996 y Strathern 1997): https://en.wikipedia.org/wiki/Goodhart%27s_law"
  - "Datos/.investigacion/metricas-y-visualizacion.md (sección 1)"
  - "Datos/.investigacion/posicion-contraria.md (sección 3)"
aliases: [definición de una métrica, metric definition, KPI, indicador, árbol de métricas, metric tree, driver tree]
creado: 2026-11-27
revisado: 2026-11-27
---

# Definición de métrica

Una definición de métrica es la receta escrita que fija qué se cuenta, sobre qué total, en qué
ventana y con qué filtros, para que dos personas que la siguen sobre los mismos datos lleguen al
mismo número.

Es la base de toda la [analítica de producto](analitica-de-producto.md): la conversión de un
[embudo](embudo.md) y la [tasa de retención por cohorte](Retencion-y-churn/tasa-de-retencion-por-cohorte.md)
son métricas y llevan las mismas piezas. Donde se escribe una vez para que todas las herramientas la
usen es la [capa semántica](../Visualizacion-y-BI/capa-semantica.md).

## «Ventas del mes» puede dar tres números

Un comercio pide las ventas del mes. Una persona suma el total de los pedidos con fecha de creación
en el mes. Otra suma solo los pagados, por fecha de pago, y resta las devoluciones. Una tercera
cuenta pedidos y no pesos. Las tres trabajan bien y llegan a números distintos, porque cada una
eligió sin decirlo qué se cuenta, qué fecha manda y qué se excluye. Ninguna gráfica lo arregla: el
desacuerdo está antes, en la definición (ejemplo de la base).

## Las piezas que fija una definición

| Pieza | Qué decide | Ejemplo en un comercio |
|---|---|---|
| Numerador | Qué se cuenta y cómo se agrega: suma, conteo, conteo de distintos | suma del importe pagado |
| Denominador | Sobre qué total se divide, si la métrica es una tasa | clientes que compraron alguna vez |
| Unidad contada | Si se cuentan entidades únicas o eventos | clientes distintos, no compras |
| [Grano](../Analisis/sql-para-analisis.md#el-grano-qué-es-una-fila) | Qué representa cada fila (pedido, cliente, sesión) y en qué período se agrupa la fecha | por pedido, agrupado por mes |
| Fecha de referencia | Qué fecha ubica a cada fila en un período | la del pago, no la del pedido |
| Ventana | En cuánto tiempo tiene que ocurrir lo que se cuenta | recompra dentro de los 90 días |
| Filtros | Qué filas quedan afuera | sin pedidos de prueba ni cancelados |

Esta lista es una síntesis de la base. Sale de los parámetros que pide una herramienta real de
definición de métricas y de las opciones de las herramientas de embudo; no se halló un texto
independiente de un proveedor que la enuncie así.

La documentación de dbt, leída por resumen, muestra qué pide escribir una herramienta. Cada métrica
lleva nombre, tipo (simple, ratio, acumulada, derivada o de conversión), agregación y expresión.
Lleva también un filtro, que la documentación compara con el `WHERE` de una consulta ("Consider it as
your WHERE clause"). Las de ratio llevan numerador y denominador, y las acumuladas y de conversión,
una ventana. El grano de tiempo no va en la métrica: lo declara la columna de fecha y se elige al
consultar, solo igual o más grueso que el de la tabla.

Para escribir una definición, contestá cada fila de la tabla por escrito y agregá un caso límite
resuelto: un pedido pagado el 1 de un mes y devuelto el 3 del siguiente, ¿en qué mes resta? Si dos
personas contestan distinto, la definición todavía no está cerrada.

## KPI: una métrica atada a un objetivo

En el uso corriente, un KPI (indicador clave de desempeño) es una métrica que se eligió para seguir
un objetivo, casi siempre con una meta y un responsable. La definición es la misma; lo que cambia es
el papel. Qué métrica elegir como principal en un producto es la [North Star](../../Producto/Medicion/north-star.md),
y según la etapa de un negocio, [una métrica que importa](../../Marketing/Medicion/metrica-que-importa.md).

> [!NOTE]
> Sin fuente todavía: la distinción entre KPI y métrica no tiene una fuente primaria leída; es el uso
> habitual.

## El árbol de métricas descompone un resultado en palancas

Un árbol de métricas parte una métrica de resultado en las métricas que la producen. En una tienda
online, las ventas son las sesiones por la tasa de conversión por el ticket promedio, y cada rama
se vuelve a partir: las sesiones por canal, la conversión por paso del embudo. La descomposición
muestra qué palanca movió el resultado y qué equipo la toca. Es la misma idea que la North Star con
sus métricas de entrada: el equipo mueve las ramas, no la raíz.

Las ramas tienen que multiplicarse o sumarse de verdad hasta la raíz. Si no, el árbol es una lista
de métricas con flechas, y una rama puede subir sin que suba el resultado (lectura de la base).

> [!NOTE]
> Sin fuente todavía: una fuente primaria sobre árboles de métricas (metric tree o driver tree) como
> método.

## Métricas de vanidad

Una métrica de vanidad sube y hace sentir bien, pero no dice si algo funcionó. Ries, según un
resumen de su texto, les atribuye tres rasgos: cuentan "a technical process, not a number of human
beings" (por ejemplo, visitas a una página y no personas; ejemplo de la base), son totales agregados y tienen "no built-in measure
of causality". Las métricas accionables, dice, son "more work". Una lista de «tres A» (accionable,
accesible, auditable) que circula atribuida a Ries no aparece en ese texto. La distinción completa,
en el contexto de una empresa nueva, está en [contabilidad de la innovación](../../Emprender/Validacion/contabilidad-de-la-innovacion.md).

En términos de la tabla de arriba, una métrica de vanidad suele ser un numerador sin denominador ni
ventana: «usuarios registrados» en lugar de «registrados en el mes que compraron dentro de 30 días»
(lectura de la base).

## Cuando la métrica se vuelve meta

Una métrica que se premia deja de seguir lo que medía, porque la gente aprende a mover el número sin
mover la cosa. La frase popular es «When a measure becomes a target, it ceases to be a good
measure», y no es de Goodhart. Según Wikipedia, que compila las citas:

- Goodhart (1975), sobre política monetaria: "Any observed statistical regularity will tend to
  collapse once pressure is placed upon it for control purposes."
- Hoskin (1996): "That every measure which becomes a target becomes a bad measure".
- Strathern (1997) la deja en la forma que circula, siguiendo a Hoskin. La referencia del artículo
  está confirmada; la frase no se leyó en el original.

Campbell había formulado algo parecido para indicadores sociales, posiblemente antes, así que la
atribución no está cerrada. Cómo pega esto en los equipos de producto, con la taxonomía de Manheim y
Garrabrant, está en [resultados y entregables](../../Producto/Estrategia/resultados-y-entregables.md#goodhart-cuando-el-resultado-se-vuelve-meta).

Lo que se puede hacer desde la definición: acompañar la métrica principal con una de guarda que
muestre si se la está forzando, como la tasa de devoluciones junto a las ventas, y dejar escritos
los filtros para que nadie los cambie en silencio (lectura de la base).

## Dónde vive la definición

Una definición escrita en la cabeza de una persona o en una consulta suelta se pierde. Lo mínimo es
una hoja con cada métrica y sus piezas; con varias herramientas y varias personas consultando, la
definición pasa a la [capa semántica](../Visualizacion-y-BI/capa-semantica.md). De dónde sale cada
número que la métrica usa es tema de [metadatos y linaje](../Gobierno-y-calidad/metadatos-y-linaje.md).
