---
resumen: >-
  Fabricar para stock o contra pedido es la decisión de en qué punto de la fabricación un producto pasa a ser de un cliente: antes de ese punto se trabaja con pronóstico y después, con pedidos. La literatura distingue cinco posiciones (para stock, ensamblar, fabricar, comprar y fabricar, y diseñar contra pedido), y cada una cambia qué se planifica en el plan maestro, qué lista de materiales hace falta y qué se le promete al cliente.
estado: borrador
estabilidad: estable
fuentes:
  - "Petropoulos, F. y otros (2025), Operations & Supply Chain Management: Principles and Practice, arXiv:2503.05749v2 (CC BY 4.0), pasaje sobre el CODP con la cita de Sharman (1984): https://arxiv.org/pdf/2503.05749"
  - "Sharman, G. (1984), «The rediscovery of logistics», Harvard Business Review 62(5), 71-79, p. 75; citado por Petropoulos y otros (2025), no leído"
  - "Harfeldt-Berg, M. (2024), tesis doctoral, Lund University, introducción y tabla 1.1: https://lup.lub.lu.se/search/files/194792365/e-spik_ex_Magnus.pdf"
  - "Olhager, J. y Van Donk, D. P. (2024), «Managing customer order decoupling points in supply chains», The Palgrave Handbook of Supply Chain Management, Springer, pp. 1115-1137 (según el resumen): https://lup.lub.lu.se/record/2f6f2a70-d314-4ea2-b252-140f6d5396c3"
  - "Olhager, J. (2003), «Strategic positioning of the order penetration point», International Journal of Production Economics 85(3), 319-329 (metadatos): https://ideas.repec.org/a/eee/proeco/v85y2003i3p319-329.html"
  - "Wikipedia, Order fulfillment (secundaria; definiciones de MTS, ATO, MTO y ETO): https://en.wikipedia.org/wiki/Order_fulfillment"
  - "IBM, COPICS, Volume III, cap. 4 (marzo de 1972), listas de opciones y programa de ensamble final: https://mirrorservice.org/sites/www.bitsavers.org/pdf/ibm/370/COPICS/G320-1976-0_COPICS_Volume_3_197203.pdf"
  - "Solucionario de preguntas de discusión sobre MRP, curso IE 314, KSU: https://faculty.ksu.edu.sa/sites/default/files/mrp.pdf"
  - "Documentación de un sistema comercial, «Overview of Two-Level Master Scheduling» (según el resumen): https://docs.oracle.com/cd/A60725_05/html/comnls/us/mrp/2levover.htm"
  - "Documentación de «Lead times» de un sistema abierto (v17.0): https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/warehouses_storage/replenishment/lead_times.html"
  - "Documentación de «Production Plan» de otro sistema abierto: https://docs.frappe.io/erpnext/user/manual/en/production-plan"
  - "ASCM, CPIM Version 6.1, 2019 Edition, módulo 1, sección F (order promising, capable-to-promise): https://learningsystem.ascm.org/wp-content/uploads/2018/11/APICS_CPIM_2019_Excerpt.pdf"
  - "Produccion/.investigacion/planificacion.md (sección 1) y planificacion-2.md (secciones 3 y 7), 2026-11-27"
aliases: [fabricar para stock, make to stock, MTS, ensamblar contra pedido, assemble to order, ATO, fabricar contra pedido, make to order, MTO, build to order, BTO, comprar y fabricar contra pedido, purchase and make to order, PMTO, diseñar contra pedido, engineer to order, ETO, punto de desacople del pedido, customer order decoupling point, CODP, punto de penetración del pedido, order penetration point, OPP, estrategia de respuesta, estrategia de producción]
creado: 2026-11-27
revisado:
---

# Fabricar para stock o contra pedido

Fabricar para stock o contra pedido es la decisión de en qué punto de la fabricación un producto pasa a ser de un cliente: antes de ese punto se trabaja con pronóstico y después, con pedidos. La literatura distingue cinco posiciones (para stock, ensamblar, fabricar, comprar y fabricar, y diseñar contra pedido), y cada una cambia qué se planifica en el plan maestro, qué lista de materiales hace falta y qué se le promete al cliente.

Es la primera decisión de [Planificación de la producción](planificacion-de-la-produccion.md), porque fija qué objeto planifica el [plan maestro de producción](plan-maestro-de-produccion.md). Del lado de la demanda, el pronóstico que alimenta la parte de antes del punto es de Cadena: [pronóstico de demanda](../../Cadena-de-suministro-y-logistica/Planificacion/pronostico-de-demanda.md).

## El punto de desacople, según Sharman

El concepto tiene un origen citado por todos: un artículo de Sharman en la *Harvard Business Review* de 1984. Una revisión abierta de 2025 (Petropoulos y otros) lo cita así: «the point at which product becomes earmarked for a particular customer. Downstream of this order penetration (OP) point, customer orders drive the systems that control materials flow; upstream, forecast and plans do the driving» (Sharman, 1984, p. 75). La cita es de segunda mano: el artículo original no se leyó.

Una tesis de Lund de 2024 lo resume en una oración: el punto de desacople del pedido (CODP) separa el flujo en «an upstream part which is driven by forecasts and a downstream part which is driven by actual customer orders». Según la paráfrasis de la misma tesis, Sharman lo veía como variable clave porque suele ser donde se congela la especificación del producto, el último punto con stock y el límite entre lo que se hace por pronóstico y lo que se hace por pedido. Olhager (2003) lo llama punto de penetración del pedido; su artículo da factores de mercado, producto y producción para ubicarlo, pero solo se vieron sus metadatos.

## Las cinco posiciones

La revisión de 2025 dice que, por el equilibrio entre lo que pide el mercado (cuán específica es la demanda, cuán rápido hay que entregar) y lo que cuesta fabricar, «five distinct position of the CODP have been distinguished in the literature»: «make to stock (MTS), assemble to order (ATO), make to order (MTO), purchase and make to order (PMTO), and engineer to order (ETO)». El capítulo de Olhager y Van Donk (2024) da la misma lista, según su resumen. La tesis de Lund trabaja con cuatro, sin la de comprar y fabricar.

| Posición | Qué se hace antes del pedido | Qué se hace después | Definición |
|---|---|---|---|
| Para stock (MTS) | todo; el producto terminado espera en el depósito | despachar | «the product is built against a sales forecast, and sold to the customer from finished goods stock» |
| Ensamblar contra pedido (ATO) | componentes y subconjuntos | el armado final con las opciones del cliente | «the product is built to customer specifications from a stock of existing components» |
| Fabricar contra pedido (MTO) | se compran y guardan las materias primas | fabricar | «the product is based on a standard design» |
| Comprar y fabricar contra pedido (PMTO) | nada físico; el diseño existe | comprar los materiales y fabricar | sin definición leída |
| Diseñar contra pedido (ETO) | nada | diseñar, comprar y fabricar | «the product is designed and built to customer specifications» |

Las definiciones de la última columna son de la entrada «Order fulfillment» de Wikipedia, que es secundaria. Lo que se hace antes y después de cada una es lectura de la base sobre esas definiciones y la revisión de 2025, que resume los extremos: el primero «directly delivers a product form inventory upon arrival of an order», y el último «starts engineering and purchasing once an order arrives».

> [!NOTE] Sin fuente todavía: una definición de cada posición en una fuente primaria abierta (Olhager 2010, Hoekstra y Romme 1992) y una definición propia de comprar y fabricar contra pedido. Wikipedia iguala «make to order» con «build to order», y la revisión de 2025 separa fabricar de comprar y fabricar contra pedido.

## Qué cambia al mover el punto

Mover el punto hacia el cliente acorta la entrega y obliga a pronosticar más; alejarlo achica el riesgo de stock y alarga la entrega. La revisión de 2025 lo dice así: entre las posiciones hay «a huge difference in delivery leadtime, but also in product specificity and the number of activities performed after ordering». La tesis de Lund compara los dos lados del punto:

| | Antes del punto | Después del punto |
|---|---|---|
| Producto | «Standardized products, produced according to forecast» | «Customized products, produced based on actual customer orders» |
| Demanda | «Demand is predictable and demand volumes are high» | «Market demand is spiky and unpredictable, volumes vary but are typically lower (per product variant)» |
| Qué tiene que hacer bien | «Cost-efficiency, lean, high throughput rate, and a level schedule» | «Flexibility, agility, capacity to deal with demand spikes» |

En el punto hay stock: Wikipedia lo dice como «The decoupling point always is an inventory buffer». El dimensionamiento de ese stock es de [stock de seguridad](../../Inventario-y-depositos/Reposicion/stock-de-seguridad.md), de Inventario.

Una empresa no tiene una sola posición: cada familia de productos puede tener la suya. Una fábrica de muebles puede tener sillas estándar para stock y mesas a medida contra pedido (ejemplo de la base).

## Qué planifica el plan maestro en cada caso

El plan maestro se arma en el nivel donde está el punto, que es el nivel con menos artículos distintos (inferencia de la base). Un solucionario de un curso lo resume: el plan maestro se expresa en «(1) End items in a continuous (make-to-stock) company; (2) Customer orders in a job shop (make-to-order) company; and (3) Modules in a repetitive (assemble-to-stock) company». Es un solucionario, no el libro.

- **Para stock**: el plan maestro es de productos terminados, con pronóstico, y el pedido se atiende del depósito.
- **Ensamblar contra pedido**: el plan maestro es de módulos o subconjuntos, y el producto terminado aparece recién en el programa de ensamble final. Un manual de 1972 lo explica: cuando el plazo de fabricación supera el que acepta el cliente, el programa de ensamble final «is created - usually on receipt of actual orders - later in time than the master production schedule». Los componentes que dejó listos el plan maestro funcionan como restricción: «It is impossible, on short notice, to build more, or different, products than the quantities of available components allow». El programa de ensamble final está en [plan maestro de producción](plan-maestro-de-produccion.md#el-programa-de-ensamble-final).
- **Fabricar contra pedido**: el plan maestro es de pedidos de clientes, y lo que se planifica con pronóstico son las materias primas. En un sistema abierto, la fecha de la orden se calcula hacia atrás: «the expected delivery date subtracted by the manufacturing lead time». En otro, el plan de producción se arma trayendo los artículos de los pedidos de venta.
- **Diseñar contra pedido**: el producto no existe al recibir el pedido, y el trabajo se parece más a un proyecto (inferencia de la base; ver [Servicios profesionales y proyectos](../../Servicios-profesionales-y-proyectos/servicios-profesionales-y-proyectos.md) para la gestión por proyectos).

## La lista de planificación para las opciones

En ensamble contra pedido, el MRP no puede explotar un producto que todavía no se configuró. La salida es planificar con porcentajes por opción, y la [lista de materiales](../Producto-y-proceso/lista-de-materiales.md) que los guarda es la lista de planificación.

El manual de 1972 lo muestra con números: si históricamente la opción A se usa «40% of the time and B 60%» y el plan pide 100 unidades, hacen falta 40 de A y 60 de B. Para cubrirse, «one could add "10% for protection" and cover 44 of option A and 66 of option B». La documentación de un sistema comercial describe lo mismo con otro nombre: listas de modelo y de planificación para familias y productos con opciones, con porcentajes que representan «estimates of anticipated product and option mixes». Programar solo los subconjuntos clave y armar la configuración con el pedido es lo que esa documentación llama plan maestro en dos niveles.

El colchón del 10 % sobre las dos opciones suma 110 componentes para 100 productos; es el costo de no saber la mezcla (cuenta de la base).

> [!NOTE] Sin fuente todavía: la definición de lista de planificación y de plan maestro en dos niveles del diccionario de ASCM.

## Qué se le promete al cliente

La promesa cambia con la posición. Para stock y en ensamble contra pedido, se promete lo que no está comprometido en el stock y en el plan maestro: el disponible para prometer, que se calcula en [plan maestro de producción](plan-maestro-de-produccion.md#el-disponible-para-prometer-del-plan-maestro). Contra pedido, el stock no alcanza y hay que mirar la capacidad. El diccionario de ASCM, citado en el CPIM, dice que para lo fabricado contra pedido la promesa «usually involves a check of uncommitted material and availability of capacity», y define el capaz de prometer (CTP) como comprometer pedidos «against available capacity as well as inventory». La fecha que se escribe en el pedido es de Relación con clientes, en [fecha prometida](../../Relacion-con-clientes/Pedido-de-venta/fecha-prometida.md).

## Qué registra un sistema por estrategia

- Por producto o familia: la posición del punto de desacople, o al menos si se repone para stock o se fabrica por pedido. No se confirmó como campo en los sistemas abiertos leídos; uno de ellos arma el plan desde el pronóstico o desde los pedidos de venta, según cómo se lo dispare.
- Por lista de planificación: los porcentajes de cada opción y el colchón.
- Por orden contra pedido: el pedido de venta que la originó, para el rastreo que explica [MRP](mrp.md#rastreo-de-la-demanda).
- Por pedido: la fecha prometida y si salió del disponible para prometer o de la capacidad.
