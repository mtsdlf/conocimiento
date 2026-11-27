---
resumen: >-
  Juntar varias fuentes de gestión es poner en el mismo análisis el sistema de gestión, el CRM, la
  tienda online y las planillas, que cuentan el mismo cliente, el mismo pedido y la misma venta con
  claves, granos y definiciones distintos. Se resuelve con dimensiones conformadas, una regla de
  qué fuente manda en cada dato y controles sobre las planillas como sobre cualquier otra fuente.
estado: vigente
estabilidad: estable
fuentes:
  - "Kimball Group, Conformed Dimensions, Conformed Facts y Drilling Across: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/conformed-fact/"
  - "Margy Ross, Design Tip #135, Conformed Dimensions as the Foundation for Agile Data Warehousing (2011): https://www.kimballgroup.com/2011/06/design-tip-135-conformed-dimensions-as-the-foundation-for-agile-data-warehousing/"
  - "Kimball y Ross, The Data Warehouse Toolkit, 3.ª ed. (Wiley, 2013), índice oficial, cap. 8 (solo títulos): https://media.wiley.com/product_data/excerpt/02/11185308/1118530802-34.pdf"
  - "Kimball y Ross, The Data Warehouse Toolkit, 3.ª ed., cap. 1, extracto oficial: https://media.wiley.com/product_data/excerpt/02/11185308/1118530802-32.pdf"
  - "Raymond Panko, Spreadsheet Errors: What We Know. What We Think We Can Do (EuSpRIG, 2000): https://arxiv.org/abs/0802.3457"
  - "Raymond Panko, What We Don't Know About Spreadsheet Errors Today (EuSpRIG, 2015): https://arxiv.org/abs/1602.02601"
  - "Datos/.investigacion/bi-gestion-conciliacion-moneda.md y bi-gestion-modelado.md (2026-11-27)"
aliases: [varias fuentes, integrar fuentes, ERP y CRM, ERP y tienda online, planillas como fuente, combinar sistemas, multi-source BI]
creado: 2026-11-27
revisado: 2026-11-27
---

# Varias fuentes de gestión

Juntar varias fuentes de gestión es poner en el mismo análisis el sistema de gestión, el CRM, la tienda online y las planillas, que cuentan el mismo cliente, el mismo pedido y la misma venta con claves, granos y definiciones distintos. Se resuelve con dimensiones conformadas, una regla de qué fuente manda en cada dato y controles sobre las planillas como sobre cualquier otra fuente.

Es una de las dos razones por las que existe el [BI sobre el software de gestión](bi-sobre-software-de-gestion.md); la otra es la [historia](historia-en-el-bi-de-gestion.md). Kimball y Ross lo dicen de los sistemas de origen: muchas veces son aplicaciones «without any commitment to sharing common data such as product, customer, geography, or calendar», y un ERP que cubre toda la empresa «could help address these shortcomings». Lo que el ERP no cubre (el CRM, la tienda, las planillas, el sistema anterior) es lo que hay que juntar.

## Qué trae cada fuente

| Fuente | Qué trae que el sistema de gestión no tiene | Con qué se cruza |
|---|---|---|
| CRM | oportunidades, etapas, actividades, el motivo de una venta perdida | el cliente y el pedido de venta |
| Tienda online y marketplaces | el pedido tal como lo hizo el cliente, el canal, la campaña, las comisiones de la plataforma | el pedido, el artículo y la factura |
| Planillas | el presupuesto, las metas comerciales, costos estimados, clasificaciones que nadie cargó en el sistema | casi siempre por mes y por categoría |
| El sistema anterior | la historia previa al cambio de sistema | todas las dimensiones, con claves viejas |

La tabla es lectura de esta base. Dónde termina el CRM frente al módulo de ventas del ERP está en [CRM](../../../Software-de-gestion/Categorias-de-producto/crm.md); qué viaja entre el sistema y la tienda, en [integración con tiendas y marketplaces](../../../Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion-en-el-comercio/integracion-con-tiendas-y-marketplaces.md).

## Las tres diferencias que hay que resolver

La clave cambia de una fuente a otra. El mismo cliente tiene un email en la tienda, un CUIT en la factura y un identificador interno en el CRM. Unirlos es el trabajo de [datos maestros](../../Gobierno-y-calidad/datos-maestros.md#cómo-se-encuentra-a-la-misma-persona-en-dos-registros), y el BI usa el resultado como [clave durable](dimensiones-conformadas.md#las-dimensiones-que-comparten-los-dominios) de la dimensión. Con los artículos es más fácil si todos los canales usan el mismo SKU.

El grano tampoco coincide: la tienda registra pedidos, y el sistema, facturas y remitos. Un pedido puede facturarse en dos veces, y una factura puede juntar dos pedidos. Juntar las dos tablas en una sola fila por pedido duplica importes sin avisar. El *Toolkit* tiene una sección «Avoiding Fact-to-Fact Table Joins», según su índice (no se leyó). Kimball propone en sus técnicas el *drill across*: consultar cada hecho por separado y alinear los resultados por las dimensiones conformadas, como explica [dimensiones conformadas](dimensiones-conformadas.md#qué-es-conformar).

La definición también cambia. «Venta» en el CRM puede ser una oportunidad ganada; en la tienda, un pedido pagado; en el sistema, una factura sin anular. Ross (2011) describe lo que pasa cuando nadie lo resuelve: los datos «may look like they can be compared and integrated due to similar labels, but the underlying business rules may be slightly different», y la gente pierde tiempo conciliando. Kimball pide que los hechos con la misma definición se llamen igual y que, si son incompatibles, «they should be differently named to alert the business users». En el BI conviven «oportunidad ganada», «pedido pagado» y «venta facturada», cada una con su nombre. Cuál cuenta como venta para cada pregunta lo fija la [definición de métrica](../../Analitica-de-producto/definicion-de-metrica.md#ventas-del-mes-puede-dar-tres-números).

## Qué fuente manda en cada dato

Cuando dos fuentes dicen cosas distintas del mismo dato, se decide por campo, no por sistema: el precio y el importe facturado mandan desde el sistema de gestión, el email desde la tienda, la etapa comercial desde el CRM. La regla general está en [quién manda en cada dato](../../Gobierno-y-calidad/datos-maestros.md#quién-manda-en-cada-dato) y, del lado de los sistemas, en [qué sistema manda en cada dato](../../../Software-de-gestion/Columnas-tecnicas/integracion-y-migracion.md#qué-sistema-manda-en-cada-dato). Para el dinero, en lectura de esta base, manda casi siempre el sistema de gestión, porque es lo que termina en el balance: un margen por canal que no parte de la factura no se va a poder [conciliar](conciliar-el-bi.md).

Un caso que cruza todo: el margen por canal de un comercio que vende por su tienda, un marketplace y un local (ejemplo de esta base). El canal y la comisión vienen de la tienda y del marketplace; el importe facturado y la nota de crédito, del sistema; el costo de lo vendido, del movimiento de stock del sistema. Las tres fuentes se unen por el pedido y el artículo, y el resultado tiene que cuadrar con las ventas del mayor.

## Las planillas como fuente

Las planillas entran al BI porque hay datos que no están en ningún sistema: el presupuesto, las metas, el costo estimado de un producto nuevo. Son una fuente más y fallan más que las otras. Panko (2000) junta quince años de estudios: «spreadsheet errors are both common and non-trivial». Las auditorías de campo con mejor método «found errors in at least 86% of the spreadsheets audited». En 2015 suma 85 inspecciones con errores en el 94 % de las planillas, y advierte que quienes las arman y las empresas «are highly overconfident in the accuracy of their spreadsheets». Son estudios de planillas en general, no de planillas usadas como fuente de un BI.

En lectura de esta base, eso pide tratarlas con las mismas reglas que una base:

- Una sola planilla por dato, con un responsable y una estructura fija ([datos ordenados](../../../Planillas-de-calculo/Datos-en-la-planilla/datos-ordenados.md)).
- Las mismas claves que el BI: el código de artículo o de centro de costo del sistema, no un nombre escrito a mano.
- Controles a la llegada, como cualquier otra fuente ([calidad de datos](../../Gobierno-y-calidad/calidad-de-datos.md#dónde-se-pone-cada-control)): que el presupuesto sume lo aprobado y que cada código exista.
- Cuando la planilla ya no alcanza, pasar el dato a una base, como explica [cuándo pasar a una base](../../../Planillas-de-calculo/cuando-pasar-a-una-base.md).

> [!NOTE]
> Sin fuente todavía: una fuente que mida cuántas empresas llevan el presupuesto en planillas fuera del sistema, y casos documentados de errores de una planilla que llegaron a un tablero de gestión.

## Cómo falla

- El pedido contado dos veces. La tabla junta pedidos de la tienda con facturas del sistema y el pedido facturado en dos partes duplica su importe.
- Tres ventas con un nombre. El tablero comercial muestra oportunidades ganadas y el de administración, facturas, y los dos dicen «ventas».
- El cliente partido. La tienda y el sistema no comparten clave y el margen por cliente muestra al mismo cliente como dos, uno sin costo y otro sin canal.
- La planilla que cambió de forma. Alguien agrega una columna a la planilla del presupuesto y la carga toma la meta de marzo como la de abril.
- Cada fuente a su hora. La tienda se extrae a la medianoche y el sistema a las seis; los pedidos de la noche están en una y no en la otra (lectura de esta base).
