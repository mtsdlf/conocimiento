---
resumen: >-
  Las dimensiones conformadas son las dimensiones que todos los hechos de gestión comparten con
  los mismos nombres y los mismos valores (el cliente, el artículo, el proveedor, el centro de
  costo, la empresa y el calendario con sus períodos fiscales), para que ventas, stock, compras y
  mayor se puedan poner lado a lado en un mismo reporte.
estado: borrador
estabilidad: estable
fuentes:
  - "Kimball Group, Conformed Dimensions: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/conformed-dimension/"
  - "Kimball Group, Enterprise Data Warehouse Bus Architecture y Bus Matrix: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/enterprise-data-warehouse-bus-matrix/"
  - "Kimball Group, Drilling Across, Shrunken Rollup Dimensions, Role-Playing Dimensions, Multiple Hierarchies in Dimensions, Calendar Date Dimensions, Multiple Units of Measure Facts y Natural, Durable, and Supernatural Keys (mismas técnicas)"
  - "Kimball Group, Value Chain: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/value-chain/"
  - "Ralph Kimball, Design Tip #51, Latest Thinking On Time Dimension Tables (2004): https://www.kimballgroup.com/2004/02/design-tip-51-latest-thinking-on-time-dimension-tables/"
  - "Kimball y Ross, The Data Warehouse Toolkit, 3.ª ed. (Wiley, 2013), índice oficial (solo títulos): https://media.wiley.com/product_data/excerpt/02/11185308/1118530802-34.pdf"
  - "Datos/.investigacion/bi-gestion-modelado.md (2026-11-27)"
aliases: [dimensiones conformadas, conformed dimensions, matriz de bus, bus matrix, arquitectura en bus, drill across, dimensión de fecha, calendario fiscal, período fiscal, dimensión de cliente, dimensión de artículo]
creado: 2026-11-27
revisado:
---

# Dimensiones conformadas

Las dimensiones conformadas son las dimensiones que todos los hechos de gestión comparten con los mismos nombres y los mismos valores (el cliente, el artículo, el proveedor, el centro de costo, la empresa y el calendario con sus períodos fiscales), para que ventas, stock, compras y mayor se puedan poner lado a lado en un mismo reporte.

Es la pieza que integra el [BI sobre el software de gestión](bi-sobre-software-de-gestion.md): los [hechos de gestión](hechos-de-gestion.md) dicen qué pasó, y las dimensiones conformadas permiten compararlos. Qué es una dimensión en un modelo de análisis está en [modelado dimensional](../../Modelado-y-almacenamiento/modelado-dimensional.md#hechos-dimensiones-y-la-estrella), y cómo se logra que un cliente sea uno solo en todos los sistemas, en [datos maestros](../../Gobierno-y-calidad/datos-maestros.md).

## Dos sentidos de la palabra dimensión

En un sistema de gestión, una dimensión es una etiqueta más en cada movimiento (centro de costo, proyecto, sucursal, región), como explica [dimensiones en lugar de cuentas](../../../Software-de-gestion/Columnas-tecnicas/registro-de-movimientos-y-dimensiones.md#dimensiones-en-lugar-de-cuentas). En el BI, es una tabla con el contexto por el que se corta un hecho. Las dimensiones del sistema pasan al BI, y se suman el cliente, el artículo y la fecha, que en el sistema son datos maestros y no etiquetas (lectura de esta base). En esta parte del tema, «dimensión» va en el sentido del BI, y la otra se nombra como dimensión del sistema.

## Qué es conformar

Kimball: «Dimension tables conform when attributes in separate dimension tables have the same column names and domain contents». Con eso, «information from separate fact tables can be combined in a single report», y lo llama «the essence of integration in an enterprise DW/BI system». Las dimensiones conformadas se definen una vez, con quienes gobiernan los datos, y se reusan en todos los hechos.

El *drill across* compara dos hechos sin juntarlos en una tabla: «making separate queries against two or more fact tables where the row headers of each query consist of identical conformed attributes», y alinea los resultados por esos encabezados. Ventas por categoría y stock por categoría se consultan por separado y se ponen lado a lado. Si las dos usan la misma categoría, el resultado tiene sentido; si una usa la del sistema y otra la de una planilla, las filas no coinciden.

## La matriz de procesos y dimensiones

Kimball ordena el diseño con una matriz: «The rows of the matrix are business processes and the columns are dimensions». Cada celda marcada dice que esa dimensión corta ese proceso, y la matriz sirve para priorizar, porque los equipos deberían «implement one row of the matrix at a time». Para un sistema de gestión queda así (lectura de esta base):

| Proceso | Fecha y período | Empresa | Cliente | Artículo | Proveedor | Depósito | Centro de costo | Proyecto | Persona |
|---|---|---|---|---|---|---|---|---|---|
| Ventas | sí | sí | sí | sí | | sí | sí | | sí (vendedor) |
| Pedidos | sí (varias) | sí | sí | sí | | sí | | | sí (vendedor) |
| Compras | sí (varias) | sí | | sí | sí | sí | sí | sí | |
| Stock | sí | sí | | sí | | sí | | | |
| Cuentas a cobrar | sí | sí | sí | | | | | | |
| Cuentas a pagar | sí | sí | | | sí | | | | |
| Mayor | sí | sí | | | | | sí | sí | |
| Horas | sí | sí | sí | | | | sí | sí | sí |

Las columnas con más marcas son las que más conviene conformar primero. Kimball describe también la cadena de valor de un comercio, de la compra al depósito y a la venta, y la de un mayor, del presupuesto a los compromisos y los pagos: cada paso produce sus métricas y «typically spawns at least one atomic fact table».

## Las dimensiones que comparten los dominios

El cliente y el proveedor son, en muchos sistemas, la misma [parte](../../../Software-de-gestion/Columnas-tecnicas/datos-maestros-y-partes.md) con dos roles. En el BI pueden ser una dimensión de partes con dos vistas o dos dimensiones con la clave de la parte, pero la misma empresa no puede aparecer con dos identificadores sin relación (lectura de esta base). Conviene una clave que no dependa del origen: Kimball advierte que las claves naturales «are subject to business rules outside the control of the DW/BI system» y propone una clave durable propia, que no cambia aunque cambie el perfil.

El [artículo](../../../Inventario-y-depositos/Existencias/articulo.md#la-unidad-de-medida-y-sus-conversiones) se compra en una unidad, se guarda en otra y se vende en una tercera. Kimball sugiere guardar los hechos en una unidad estándar con los factores de conversión en la misma fila, para que la consulta sea simple y correcta. Su categoría suele tener varias jerarquías (comercial, de compras, contable), y Kimball admite que «can gracefully coexist in the same dimension table».

El centro de costo y el proyecto vienen de las dimensiones del sistema, con su jerarquía. Contabilidad explica por qué el [centro de costo](../../../Contabilidad/Contabilidad-de-gestion/centros-de-costo.md#por-qué-los-centros-de-costo-van-en-dimensiones-y-no-en-el-plan-de-cuentas) va en una dimensión y no en el plan de cuentas. Si una reorganización cambia la jerarquía, el BI decide si muestra la vieja o la nueva, como trata [historia en el BI de gestión](historia-en-el-bi-de-gestion.md).

La empresa es una dimensión más, porque cada documento pertenece a una empresa legal del sistema, como pide la [estructura de la organización](../../../Software-de-gestion/Columnas-tecnicas/estructura-de-la-organizacion.md). Sumar empresas, en cambio, exige más que agrupar: es de [multiempresa y moneda en el BI](multiempresa-y-moneda-en-el-bi.md).

La cuenta contable llega con su jerarquía, porque el [plan de cuentas](../../../Contabilidad/Registro/plan-de-cuentas.md#niveles-rubros-que-agrupan-y-cuentas-que-se-imputan) ya agrupa rubros y cuentas imputables. En el BI lleva además el renglón del estado de resultados o del balance al que suma (lectura de esta base). Según su índice, el *Toolkit* trata estas jerarquías en su capítulo de contabilidad, con secciones sobre jerarquías de profundidad variable.

## El calendario y los períodos fiscales

La fecha está en todos los hechos. Kimball: las dimensiones de fecha «are attached to virtually every fact table» y llevan atributos como «week number, month name, fiscal period, and national holiday indicator». Pocos se calculan desde la fecha; los feriados, los días hábiles y los períodos fiscales «must be embedded in the calendar date dimension». Kimball propone armarla en una tarde con una planilla: «Ten years worth of days is less than 4000 rows».

Lo que agrega un sistema de gestión (lectura de esta base):

- El ejercicio no siempre coincide con el año calendario. Si el mes 1 es julio, «ventas del ejercicio» y «ventas del año» son dos números.
- Cada hecho tiene varias fechas: un pedido tiene la de toma, la de entrega prometida, la de entrega real y la de factura. Kimball usa una dimensión que juega varios roles, donde cada clave apunta a «a separate view of the date dimension so that the references are independent».
- La fecha del hecho y la de registro son distintas, y la diferencia importa para la [historia](historia-en-el-bi-de-gestion.md#lo-que-se-informó-y-lo-que-es).
- El calendario puede llevar el estado del período. El BI ya puede congelar un período cerrado, porque la [fecha de bloqueo](../../../Software-de-gestion/Columnas-tecnicas/fechas-vigencias-y-cierre.md#la-fecha-de-bloqueo) del sistema lo protege.

Dos empresas del grupo con ejercicios distintos necesitan dos calendarios fiscales en la misma dimensión. El *Toolkit* tiene una sección «Multiple Fiscal Accounting Calendars» que no se leyó.

## Las dimensiones achicadas

El presupuesto se arma por mes y por categoría, con menos detalle que las ventas. Kimball llama dimensiones achicadas (*shrunken*) a un subconjunto de filas o columnas de una dimensión base, necesarias para procesos que registran «at a higher level of granularity, such as a forecast by month and brand». El mes es una dimensión achicada de la fecha, y la categoría, del artículo. Siguen conformadas: el mes del presupuesto es el mismo mes del calendario.

## Cómo falla

- Dos categorías con el mismo nombre. Ventas usa la categoría del sistema y compras, la de una planilla del comprador; el *drill across* devuelve filas que no coinciden.
- El cliente duplicado entre sistemas. Sin clave durable ni registro de equivalencias, un cliente aparece como dos en el margen por cliente ([datos maestros](../../Gobierno-y-calidad/datos-maestros.md#el-mismo-cliente-en-tres-sistemas)).
- El año que no es el ejercicio. Un tablero muestra «acumulado del año» desde enero en una empresa cuyo ejercicio empieza en julio.
- La dimensión del sistema optativa. Un gasto sin centro de costo cae en «sin asignar» y el resultado por centro no cuadra con el total, como avisa [reportes operativos y legales](../../../Software-de-gestion/Columnas-tecnicas/reportes-operativos-y-legales.md#las-dimensiones-existen-para-el-reporte).
