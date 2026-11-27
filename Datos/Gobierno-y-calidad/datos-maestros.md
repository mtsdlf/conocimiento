---
resumen: >-
  Los datos maestros son las entidades centrales del negocio que comparten todos los sistemas
  (clientes, productos, proveedores), y gestionarlos es lograr que cada una tenga un solo registro
  que vale, el registro de oro, aunque aparezca en la tienda, el punto de venta y el sistema de
  gestión.
estado: vigente
estabilidad: semi
fuentes:
  - "TechTarget, Master data management (según el resumen del buscador): https://www.techtarget.com/searchdatamanagement/definition/master-data-management"
  - "TechTarget, Master data (según el resumen del buscador): https://www.techtarget.com/searchdatamanagement/definition/master-data"
  - "SAP, What is MDM (según el resumen del buscador): https://www.sap.com/mena/resources/what-is-mdm"
  - "IBM, What is MDM (según el resumen del buscador): https://ibm.com/topics/master-data-management"
  - "Built In, Master data management (según el resumen del buscador): https://builtin.com/articles/master-data-management"
  - "DAMA-DMBOK2, cap. Reference & Master Data (Technics Publications), no leído: https://technicspub.com/dmbok2"
  - "Datos/.investigacion/gobierno-y-privacidad.md"
aliases: [datos maestros, master data, MDM, gestión de datos maestros, master data management, registro de oro, golden record, datos de referencia, reference data]
creado: 2026-11-27
revisado: 2026-11-27
---

# Datos maestros

Los datos maestros son las entidades centrales del negocio que comparten todos los sistemas (clientes, productos, proveedores), y gestionarlos es lograr que cada una tenga un solo registro que vale, el registro de oro, aunque aparezca en la tienda, el punto de venta y el sistema de gestión.

Es la pieza de [Gobierno y calidad](gobierno-y-calidad.md) que resuelve la [unicidad](calidad-de-datos.md#las-seis-dimensiones-de-un-dato-bueno) entre sistemas, no dentro de una tabla. La gestión de datos maestros (MDM, por *master data management*) busca, según TechTarget, «a uniform set of data on customers, products, suppliers and other business entities across different IT systems».

> [!NOTE]
> Las fuentes de esta nota son de proveedores y de prensa técnica que repiten la misma idea con otras palabras; valen como una sola. La definición de DAMA no se leyó.

## Tres clases de datos que se cuidan distinto

| Clase | Qué es | Ejemplo en un comercio | Cambia |
|---|---|---|---|
| Maestros | Las entidades sobre las que se registran los hechos | Clientes, productos y sus variantes, proveedores, sucursales | Poco, y cada cambio importa |
| De referencia | Códigos fijos que clasifican a los demás | Países, provincias, monedas, estados de un pedido | Casi nunca |
| Transaccionales | Los hechos mismos | Ventas, pagos, envíos, devoluciones | Todo el tiempo |

La separación entre maestros y transaccionales es la misma que hace el [modelado dimensional](../Modelado-y-almacenamiento/modelado-dimensional.md) entre dimensiones y hechos: una venta (hecho) apunta a un cliente y a un producto (maestros). Si el cliente está dos veces, la venta queda colgada de uno solo y el análisis lo cuenta como dos clientes distintos (lectura de la base). Los datos de referencia aparecen en TechTarget como códigos genéricos, del tipo países, monedas o estados de pedido.

## El mismo cliente en tres sistemas

Un comercio que vende por su tienda online, en un local y por un marketplace suele tener tres registros de la misma persona: uno con el email en la tienda, otro con el DNI en la factura del local y otro con un apodo en el marketplace. Ninguno está mal; ninguno es el cliente entero (ejemplo de la base). Mientras no se unan, no se puede contestar cuántos clientes compran por más de un canal ni hacer un [análisis de cohortes](../Analitica-de-producto/Cohortes/analisis-de-cohortes.md) que no cuente doble a los que vuelven por otro lado. Por qué un comercio termina con esos canales está en [venta en varios canales](../../Comercio-electronico/Venta-en-varios-canales/venta-en-varios-canales.md).

Con los productos pasa lo mismo, con una ventaja: el comercio controla el identificador. La variante que se vende se identifica por su SKU, como explica [catálogo y stock](../../Comercio-electronico/Operaciones-del-comercio/catalogo-y-stock.md), y si el mismo SKU se usa en todos los canales el producto ya tiene un registro maestro de hecho.

## Cómo se encuentra a la misma persona en dos registros

El trabajo central es identificar los registros que se refieren a la misma entidad real y unirlos en uno: «Identify records that refer to the same real-world entity and combine them into a single, complete master record», según SAP. Built In, una fuente de divulgación, describe tres métodos de coincidencia:

1. Reglas exactas: dos registros son la misma persona si coinciden en un campo que identifica, como el email o el DNI.
2. Puntuación probabilística: se comparan nombre, dirección y teléfono, se suma un puntaje y por encima de un umbral se los da por iguales.
3. Modelos de aprendizaje automático.

Para un comercio chico, la primera alcanza casi siempre: normalizar el email (minúsculas, sin espacios) y el teléfono (mismo formato con código de área) ya une buena parte de los duplicados (lectura de la base). La segunda conviene revisarla a mano antes de unir, porque dos hermanos con el mismo apellido y domicilio no son la misma persona.

Una vez encontrados, hay dos formas de guardar el resultado. Se puede armar el registro de oro copiando el mejor valor de cada campo a un registro nuevo. O se puede llevar solo un índice de equivalencias sin tocar los sistemas: Built In lo llama estilo *registry*, «record #123 in System A is the same as record #456 in System B».

## Quién manda en cada dato

Unir registros obliga a decidir qué sistema manda cuando dos dicen cosas distintas: si el cliente cambió el domicilio en la tienda, ¿se pisa el del sistema de gestión? Es una decisión de [gobierno](gobierno-y-calidad.md#el-gobierno-decide-quién-responde-por-cada-dato), y conviene tomarla por campo y no por sistema: el precio puede mandar desde el sistema de gestión y el email desde la tienda. En el comercio electrónico la misma idea aparece como «un sistema que manda en cada dato y el otro que lo refleja», en la [integración con tiendas y marketplaces](../../Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion/integracion-con-tiendas-y-marketplaces.md).

Unir registros de personas tiene además un lado legal. Juntar en un perfil lo que un cliente dejó en tres canales es un tratamiento de datos personales, y la ley pide que los datos sean «adecuados, pertinentes y no excesivos» para la finalidad con que se juntaron (art. 4 de la Ley 25.326). Lo que eso implica está en [privacidad de datos personales](privacidad-de-datos-personales.md).

> [!NOTE]
> Sin fuente todavía: un caso documentado de un comercio que unió sus clientes entre canales, con cuántos duplicados encontró.
