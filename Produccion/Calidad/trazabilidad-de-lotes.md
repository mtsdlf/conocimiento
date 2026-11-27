---
resumen: >-
  La trazabilidad de lotes, en la fabricación, es la genealogía del lote fabricado: qué lotes de componente entraron en cada lote de producto, y a qué clientes fue cada uno. Permite rastrear hacia atrás, de un producto a sus materiales y proveedores, y hacia adelante, de un material a los productos y clientes, y es lo que limita un retiro a lo que de verdad está afectado.
estado: borrador
estabilidad: estable
fuentes:
  - "Reglamento (CE) n.º 178/2002, versión en español del DOCE L 31 del 1.2.2002, arts. 3.15, 18 y 19 (texto extraído del PDF; el art. 19 parcialmente ilegible): https://www.boe.es/doue/2002/031/L00001-00024.pdf"
  - "AESAN, «Trazabilidad»: https://www.aesan.gob.es/AECOSAN/web/seguridad_alimentaria/detalle/trazabilidad.htm"
  - "ISO 22005:2007, ficha (según el buscador; la página da 403): https://www.iso.org/standard/36297.html"
  - "Código Alimentario Argentino, Cap. II, art. 18 tris y 18 tris 1 (Res. Conj. SCS y SAGyP N° 2/2023): https://www.argentina.gob.ar/sites/default/files/capitulo_ii_establecactualiz_2025-04.pdf"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 4.3.4: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "NSAI, presentación «Overview 9001:2015» (23 de septiembre de 2015), diapositiva sobre 8.5.2: https://www.nsai.ie/download/certification/Overview-9001-2015-presentation-23-Sep-15-Web-Compatibility-Mode.pdf"
  - "Produccion/.investigacion/calidad.md (sección 6), argentina.md (sección de alimentos) y fundamentos-y-contraria.md (PCF 4.3.4), 2026-11-27"
aliases: [trazabilidad de lotes, trazabilidad, traceability, lot traceability, genealogía, genealogía del lote, lot genealogy, batch genealogy, rastreo hacia atrás, backward traceability, trace back, rastreo hacia adelante, forward traceability, trace forward, tracking and tracing, un paso atrás, un paso adelante, one step back one step forward, retiro de mercado, retiro de producto, recall, product recall, ISO 22005]
creado: 2026-11-27
revisado:
---

# Trazabilidad de lotes

La trazabilidad de lotes, en la fabricación, es la genealogía del lote fabricado: qué lotes de componente entraron en cada lote de producto, y a qué clientes fue cada uno. Permite rastrear hacia atrás, de un producto a sus materiales y proveedores, y hacia adelante, de un material a los productos y clientes, y es lo que limita un retiro a lo que de verdad está afectado.

El lote como atributo del stock, con su vencimiento, el orden de salida y el rastreo entre proveedor, depósito y cliente, es de Inventario y está en [lote y serie](../../Inventario-y-depositos/Existencias/lote-y-serie.md). Lo que agrega la fabricación es el eslabón del medio: el lote que entra a una [orden de producción](../Ejecucion-en-planta/orden-de-produccion.md) y el que sale de ella. Esa unión es de esta vertical, [Calidad](calidad.md), porque sirve sobre todo para contener una [no conformidad](no-conformidad.md) y para un retiro. APQC 7.4 la ubica en 4.3.4 «Maintain production records and manage lot traceability», con dos actividades: definir el sistema de numeración de lotes y definir el uso del lote.

## La genealogía: de qué está hecho cada lote

Una orden de producción consume lotes de componentes y produce uno o más lotes de producto. La genealogía guarda esa relación. Un ejemplo de la base:

| Orden | Lote fabricado | Componente | Lote de componente | Proveedor |
|---|---|---|---|---|
| OP-0412 | MERM-2611-A (500 frascos) | Frutilla congelada | FR-1033 | Proveedor X |
| OP-0412 | MERM-2611-A | Azúcar | AZ-0877 | Proveedor Y |
| OP-0412 | MERM-2611-A | Frasco 450 ml | FV-2290 | Proveedor Z |
| OP-0415 | MERM-2611-B (480 frascos) | Frutilla congelada | FR-1033 y FR-1041 | Proveedor X |

Si el producto tiene varios niveles en su [lista de materiales](../Producto-y-proceso/lista-de-materiales.md), la genealogía también: el lote de un subconjunto es componente del lote del nivel de arriba, y el rastreo recorre la cadena entera (criterio de la base). La versión de la lista y la ruta con que se fabricó cada lote queda en la orden, y eso permite separar lo fabricado antes y después de un [cambio de ingeniería](../Producto-y-proceso/cambios-de-ingenieria.md).

La genealogía es más fina cuanto más chicos son los lotes. Si toda la producción de una semana es un solo lote, un problema en un componente obliga a retirar la semana entera (criterio de la base).

## Hacia atrás y hacia adelante

Las dos preguntas que contesta la genealogía, con el ejemplo de arriba:

- **Hacia atrás**: un cliente reclama por el lote MERM-2611-B. ¿Qué entró? Los lotes de frutilla FR-1033 y FR-1041, y los del azúcar y el frasco de esa orden, con sus proveedores y sus recepciones.
- **Hacia adelante**: el proveedor X avisa que el lote FR-1033 tiene un problema. ¿Dónde está? En los lotes MERM-2611-A y MERM-2611-B, y de ahí, en todos los clientes que recibieron alguno de los dos. El FR-1041 no está comprometido, pero comparte el lote MERM-2611-B con el FR-1033, y por eso ese lote entero queda alcanzado.

El rastreo hacia adelante desde el lote fabricado hasta el cliente usa los despachos, que son de Inventario. El de acá termina en el lote fabricado; el de allá sigue hasta el cliente.

## Lo que pide la ley y lo que no

La referencia más citada es el Reglamento (CE) 178/2002 de la Unión Europea, para alimentos y piensos. Define la trazabilidad (art. 3.15) como «la posibilidad de encontrar y seguir el rastro, a través de todas las etapas de producción, transformación y distribución, de un alimento, un pienso, un animal destinado a la producción de alimentos o una sustancia destinada a ser incorporada en un alimento o un pienso».

El artículo 18 dice qué hay que poder hacer, y es menos de lo que parece:

| Apartado | Qué pide, literal |
|---|---|
| 18.2 | los explotadores «deberán poder identificar a cualquier persona que les haya suministrado un alimento, un pienso, un animal destinado a la producción de alimentos, o cualquier sustancia destinada a ser incorporada en un alimento o un pienso» |
| 18.3 | «deberán poner en práctica sistemas y procedimientos para identificar a las empresas a las que hayan suministrado sus productos» |
| 18.4 | los productos «deberán estar adecuadamente etiquetados o identificados para facilitar su trazabilidad mediante documentación o información pertinentes» |

El reglamento pide conocer el proveedor inmediato y el cliente inmediato. **No pide la genealogía interna**: qué lote de ingrediente entró en qué lote de producto. La expresión «un paso atrás, un paso adelante» no está en el artículo; la usa la AESAN, la agencia española de seguridad alimentaria, que lo explica así: los explotadores «contarán con un sistema que les permita identificar a sus proveedores inmediatos y a sus clientes inmediatos», salvo cuando el cliente es el consumidor final.

Sin la genealogía interna, la ley se cumple, pero un retiro alcanza todo lo fabricado mientras hubo stock del ingrediente malo (inferencia de la base). La norma que trata el diseño de un sistema de trazabilidad en la cadena alimentaria es la ISO 22005:2007; según el buscador, fija principios y requisitos mínimos y se confirmó en 2022. No se leyó.

En la Argentina, el Código Alimentario va más lejos que el reglamento europeo en la letra: pide procedimientos que permitan seguir el rastro de un producto «como así también de sus materias primas y aditivos», y un plan de retiro documentado. Lo que pide cada rubro (alimentos, medicamentos, productos médicos) está en [Producción en la Argentina](../produccion-en-argentina.md).

Para la gestión de la calidad en general, ISO 9001:2015 trata la identificación y la trazabilidad en la cláusula 8.5.2. Según NSAI, la edición 2015 no le agregó requisitos nuevos; el texto no se leyó.

## El retiro

El retiro es para lo que se lleva la genealogía. El artículo 19.1 del mismo reglamento dice, parafraseado, que si un explotador considera o tiene motivos para pensar que un alimento que importó, produjo, transformó, fabricó o distribuyó no cumple los requisitos de seguridad, inicia de inmediato el retiro del mercado e informa a las autoridades. Si el producto puede haber llegado al consumidor, también lo informa y recupera lo entregado. El PDF tenía partes ilegibles: es una paráfrasis que falta recotejar.

Los pasos de un retiro, como criterio de la base:

1. Rastrear hacia adelante desde el lote o el componente con problema.
2. Bloquear el stock alcanzado en todos los depósitos; el estado es de Inventario, en [estados del stock](../../Inventario-y-depositos/Existencias/estados-del-stock.md).
3. Frenar las órdenes abiertas que estén consumiendo ese lote de componente.
4. Avisar a los clientes que recibieron los lotes alcanzados y recuperar lo que se pueda.
5. Abrir la [no conformidad](no-conformidad.md) por lo recuperado y la [acción correctiva](accion-correctiva.md) por la causa.

## Qué tiene que registrar un sistema

La genealogía no se carga aparte: sale de los movimientos de la orden. Cada entrega de material y cada [declaración de consumo](../Ejecucion-en-planta/consumo-y-declaracion.md) tiene que decir qué lote se usó, y cada declaración de producción, qué lote salió. Con eso, la genealogía es una consulta (criterio de la base).

- **Por lote fabricado**: número de lote, artículo, orden de producción, fecha, cantidad, versión de la lista y la ruta, y vencimiento si corresponde.
- **Por consumo**: orden, componente, lote de componente, cantidad y, por el lote, su proveedor y su recepción.
- **Por despacho**: lote, cliente, cantidad y fecha; esto es de Inventario.
- **La regla de numeración** de los lotes propios y si el lote del proveedor se conserva o se reemplaza por uno interno, que es la actividad 4.3.4.1 de APQC.

El punto débil es el consumo automático. Si el sistema descuenta los componentes según la lista de materiales al declarar lo producido, sin que nadie diga qué lote se tomó, tiene que elegirlo por una regla (el más viejo, el que vence antes). Si la planta usó otro, la genealogía registrada no es la real. En los artículos que se siguen por lote, el consumo tiene que confirmar el lote, o la regla tiene que coincidir con lo que se hace en la línea (criterio de la base).

En papel, la genealogía es la hoja de la orden con una columna para el lote de cada componente, que el operario llena al cargar la máquina, y el remito con el lote de lo despachado.
