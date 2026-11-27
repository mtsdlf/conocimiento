---
resumen: >-
  SCM, WMS y TMS son tres categorías de software de gestión de la cadena de suministro: la planificación de la cadena (cuánto vender, producir y mover), el sistema de gestión de depósitos (lo que pasa adentro del depósito) y el sistema de gestión de transporte (el viaje de la carga). Las dos últimas el mercado las agrupa como ejecución de la cadena.
estado: borrador
estabilidad: estable
fuentes:
  - "Gartner, glosario «Supply Chain Execution (SCE)» (resumen; no leído): https://gcom.pdo.aws.gartner.com/en/information-technology/glossary/supply-chain-execution-sce"
  - "Gartner, Magic Quadrant for Supply Chain Planning Solutions, abril de 2025 (resumen): https://www.gartner.com/en/documents/6356179"
  - "TechTarget, definición de warehouse management system (resumen): https://www.techtarget.com/enterprise-software/definition/warehouse-management-system-WMS"
  - "Un proveedor de TMS, «What is a transportation management system» (resumen): https://www.manh.com/resources/articles/what-is-transportation-management-system-tms"
  - "Un operador logístico, documento sobre TMS y WMS que cita a Gartner (resumen; no leído entero): https://www.dhl.com/content/dam/dhl/global/dhl-supply-chain/documents/pdf/glo-dsc-next-gen-tms-wms.PDF"
  - "APQC, Process Classification Framework Cross-Industry 7.2.1, copia de terceros (resumen): https://www.slideshare.net/AsgharAghiliDehkordi/cross-industry-v721-final"
  - "Documentación de aplicaciones de un ERP de código abierto, versión 18.0 (leída): https://www.odoo.com/documentation/18.0/applications.html"
  - "Software-de-gestion/.investigacion/fundamentos-y-categorias.md y taxonomias-externas-96.md (2026-11-27)"
aliases: [SCM, supply chain management, gestión de la cadena de suministro, SCP, supply chain planning, planificación de la cadena de suministro, SCE, supply chain execution, ejecución de la cadena de suministro, WMS, warehouse management system, sistema de gestión de depósitos, sistema de gestión de almacenes, TMS, transportation management system, sistema de gestión de transporte]
creado: 2026-11-27
revisado:
---

# SCM, WMS y TMS

SCM, WMS y TMS son tres categorías de software de gestión de la cadena de suministro: la planificación de la cadena (cuánto vender, producir y mover), el sistema de gestión de depósitos (lo que pasa adentro del depósito) y el sistema de gestión de transporte (el viaje de la carga). Las dos últimas el mercado las agrupa como ejecución de la cadena.

Son parte de las [categorías de producto](categorias-de-producto.md) y llevan dos temas de esta base: [Inventario y depósitos](../../Inventario-y-depositos/inventario-y-depositos.md), que mira lo que pasa adentro del depósito, y [Cadena de suministro y logística](../../Cadena-de-suministro-y-logistica/cadena-de-suministro-y-logistica.md), que mira el plan y el movimiento entre lugares. El saber de cada uno está allá; acá, cómo lo cortan los productos.

## Planificación por un lado, ejecución por otro

Gartner, según resúmenes, agrupa el WMS y el TMS bajo la ejecución de la cadena de suministro (*supply chain execution*), como «execution-oriented applications», y evalúa la planificación aparte, en un cuadrante de soluciones de planificación de la cadena (abril de 2025). La sigla SCM se usa para las dos cosas juntas o solo para la planificación, según quién la use.

| Categoría | Qué lleva | Dónde está el saber |
|---|---|---|
| Planificación de la cadena (SCP) | Pronóstico, plan de ventas y operaciones, distribución entre depósitos | [Planificación](../../Cadena-de-suministro-y-logistica/Planificacion/planificacion.md) |
| WMS | Recepción, ubicación, reserva, preparación, conteo | [Operación del depósito](../../Inventario-y-depositos/Operacion-del-deposito/operacion-del-deposito.md) y [control del stock](../../Inventario-y-depositos/Control-del-stock/control-del-stock.md) |
| TMS | Modo, transportista, consolidación, ruteo, costo del flete | [Transporte](../../Cadena-de-suministro-y-logistica/Transporte/transporte.md) y [despacho y entrega](../../Cadena-de-suministro-y-logistica/Despacho-y-entrega/despacho-y-entrega.md) |

Según un resumen de la prensa del sector, un WMS es «software and processes that control and administer warehouse operations from the time goods or materials enter a warehouse until they move out». Un proveedor de TMS lo define como lo que «enables enterprise-wide management, optimization, planning, and execution of logistics services for transporting goods». Un documento de un operador logístico, citando a Gartner, atribuye al TMS un ahorro de 5 a 10 % del gasto en transporte; es una sola fuente, con interés, y no se leyó entera.

## Dónde corta el software y dónde corta esta base

El software no corta donde corta la base. Esta base separa el depósito del transporte en la puerta de salida: lo de adentro es de Inventario, el despacho y el viaje son de Cadena de suministro. APQC junta los dos en un solo proceso (4.4, logística y depósitos), y la [operación del depósito](../../Inventario-y-depositos/Operacion-del-deposito/operacion-del-deposito.md#dónde-corta-la-base-y-dónde-corta-el-campo) ya anota que los sistemas de gestión de depósitos incluyen el despacho. Un ERP de código abierto pone stock, compras, producción, calidad y mantenimiento en una sola familia de cadena de suministro.

En la práctica, el WMS llega hasta el bulto cargado en el camión y el TMS empieza en el viaje, con una franja compartida (la cita con el transportista, el documento del despacho) que cada producto resuelve a su manera (lectura de esta base).

## Dónde termina frente al ERP

El [ERP](erp.md) ya lleva stock y pedidos. En la lectura de esta base, la diferencia es de detalle: el ERP sabe cuánto hay de cada artículo en cada depósito, y el WMS sabe en qué ubicación, en qué estado y qué tarea de preparación lo va a mover. Una empresa con un depósito chico vive con el módulo de stock del ERP; el WMS aparece cuando el costo de caminar y buscar justifica dirigir cada tarea. El mismo razonamiento vale para el TMS frente a la logística que el ERP registra como un despacho con transportista.

Las categorías vecinas también tienen stock: el [MES](mes.md) lleva el inventario de la planta, que ISA-95 trata como una de las operaciones del nivel 3, y la tienda en línea lleva el stock que publica. Cada una cree ser dueña del número.

## Quién manda en el stock

Con varias cajas, la pregunta de fondo es qué sistema es la fuente de verdad de la cantidad. Una regla común, en la lectura de esta base, es que el WMS manda en la ubicación y el estado y el ERP en el saldo por depósito y su valor, y que el WMS le informa cada movimiento al ERP en vez de sobrescribir el número. Así lo pide el [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md): cada recepción y cada salida es una fila nueva, no una cantidad pisada. Cómo se arma esa conexión está en [integración y migración](../Columnas-tecnicas/integracion-y-migracion.md); el caso de la tienda y el marketplace, con la sobreventa que causa tener dos dueños del stock, en [integración con tiendas y marketplaces](../../Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion/integracion-con-tiendas-y-marketplaces.md).

> [!NOTE] Sin fuente todavía: la historia del WMS y del TMS, una definición primaria de cada uno (las de Gartner están detrás de un muro y las leídas son de prensa o de proveedores) y la edición vigente de los cuadrantes de WMS y TMS.
