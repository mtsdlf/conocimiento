---
resumen: >-
  Dos marcos se usan para cortar la cadena de suministro en procesos: el Process Classification Framework (PCF) de APQC y SCOR, de ASCM. Ninguno corta como esta base, así que cada proceso del PCF y de SCOR se reparte entre este tema y sus vecinos; SCOR agrega cinco atributos de desempeño con sus métricas.
estado: borrador
estabilidad: estable
fuentes:
  - "APQC, Process Classification Framework, Cross Industry, versión 7.4 (2024), categoría 4.0, procesos 4.1 y 4.4: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "ASCM, SCOR Digital Standard, introducción y texto previo (© 2020, «SCOR v13 Updates»), tablas 1 y 2: https://www.ascm.org/globalassets/ascm_website_assets/docs/intro-and-front-matter-scor-digital-standard.pdf"
  - "Wikipedia, Supply-chain operations reference: https://en.wikipedia.org/wiki/Supply-chain_operations_reference (secundaria; solo para la versión de siete procesos)"
  - "Cadena-de-suministro-y-logistica/.investigacion/fundamentos-y-contraria.md y fundamentos-y-contraria-2.md (2026-11-27)"
aliases: [marcos de la cadena de suministro, marcos de procesos de la cadena, SCOR, SCOR DS, SCOR Digital Standard, Supply Chain Operations Reference, APQC, PCF, Process Classification Framework, atributos de desempeño de SCOR, Plan Source Make Deliver Return Enable]
creado: 2026-11-27
revisado:
---

# Marcos de la cadena de suministro

Dos marcos se usan para cortar la cadena de suministro en procesos: el Process Classification Framework (PCF) de APQC y SCOR, de ASCM. Ninguno corta como esta base, así que cada proceso del PCF y de SCOR se reparte entre este tema y sus vecinos; SCOR agrega cinco atributos de desempeño con sus métricas.

Es parte de los [fundamentos de cadena de suministro](fundamentos-de-cadena-de-suministro.md). La base le da a cada dominio un objeto y un verbo; la frontera de cada vecino está en el [alcance](../ALCANCE.md).

## El PCF de APQC, proceso por proceso

En la versión 7.4, la categoría 4.0 es «Manage Supply Chain for Physical Products». Este tema sale de dos procesos, 4.1 «Plan for and align supply chain resources» y 4.4 «Manage logistics and warehousing». Sus procesos de nivel 3 se reparten así (el reparto es de la base):

| Proceso del PCF 7.4 | Dónde va en la base |
|---|---|
| 4.1.1 Develop production and materials strategies | Producción (todavía no armado) |
| 4.1.2 Manage demand for products | [Pronóstico de demanda](../Planificacion/pronostico-de-demanda.md), [error de pronóstico](../Planificacion/error-de-pronostico.md) (4.1.2.7, «Measure demand forecast accuracy») y [plan de ventas y operaciones](../Planificacion/plan-de-ventas-y-operaciones.md); el 4.1.2.4, «Determine available to promise», es [disponible para prometer](../../Inventario-y-depositos/Existencias/disponible-para-prometer.md), de Inventario |
| 4.1.3 Create materials plan | Producción |
| 4.1.4 Create and manage master production schedule | Producción |
| 4.1.5 Plan distribution requirements | [Planificación de la distribución](../Planificacion/planificacion-de-la-distribucion.md) |
| 4.1.6 Establish distribution planning constraints | [Planificación de la distribución](../Planificacion/planificacion-de-la-distribucion.md): restricciones de depósito, inventario, transporte y almacenaje |
| 4.1.7 Review distribution planning policies | [Diseño de la red](../Red-de-distribucion/diseno-de-la-red.md) (4.1.7.1, «Review distribution network»); el 4.1.7.2, «Establish sourcing relationships», es de Compras y abastecimiento (todavía no armado); el 4.1.7.3, «Establish dynamic deployment policies», es dato de la [planificación de la distribución](../Planificacion/planificacion-de-la-distribucion.md) |
| 4.1.8 Develop quality standards and procedures | Ningún tema armado |
| 4.4.1 Provide logistics governance | [Red de distribución](../Red-de-distribucion/red-de-distribucion.md) (diseño de la red, necesidades de tercerización), [Transporte](../Transporte/transporte.md) (horarios y costos), [nivel de servicio logístico](../Despacho-y-entrega/nivel-de-servicio-logistico.md) (política de entrega e indicadores) y [logística inversa](../Despacho-y-entrega/logistica-inversa.md) (4.4.1.7) |
| 4.4.2 Plan and manage inbound material flow | La recepción es de [Inventario](../../Inventario-y-depositos/Operacion-del-deposito/recepcion.md); el flujo de devoluciones (4.4.2.4 y 4.4.2.5), de [logística inversa](../Despacho-y-entrega/logistica-inversa.md) |
| 4.4.3 Operate warehousing | [Inventario y depósitos](../../Inventario-y-depositos/inventario-y-depositos.md) |
| 4.4.4 Operate outbound transportation | [Despacho y entrega](../Despacho-y-entrega/despacho-y-entrega.md) y [Transporte](../Transporte/transporte.md); el 4.4.4.4, «Process and audit carrier invoices and documents», es [costo del flete](../Transporte/costo-del-flete.md) |

Dos diferencias con el árbol. El PCF no tiene un nodo para el S&OP: lo más cercano es 4.1.2.3, «Develop demand consensus forecast». Y la categoría 4 no tiene comercio exterior ni aduana; el resto del PCF no se revisó.

## SCOR: qué versión se leyó

La versión leída es la v13 del SCOR Digital Standard, de 2020, en la introducción que publica ASCM. Organiza la cadena en «the six primary management processes of Plan, Source, Make, Deliver, Return and Enable». Va «from the supplier's supplier to the customer's customer» y deja afuera «sales and marketing, including demand generation; product development; or research and development». ASCM define los tres primeros niveles de procesos, que son «industry neutral»; cada empresa tiene que extenderlo «at least to level 4».

Circula también una versión de siete procesos: Plan, Source, Transform, Order, Fulfill, Return y Orchestrate. Solo consta en una fuente secundaria, que la atribuye a 2022; ningún texto de ASCM con esa versión se pudo leer. Quien cite SCOR tiene que decir la versión.

Con la v13, el reparto es este (lectura de la base): Plan va a [Planificación](../Planificacion/planificacion.md), aunque el plan de compras y el de producción son de sus temas; Source es de Compras y abastecimiento; Make, de Producción; Deliver se parte entre el depósito, en Inventario, y lo que pasa desde la puerta, en [Despacho y entrega](../Despacho-y-entrega/despacho-y-entrega.md) y [Transporte](../Transporte/transporte.md); Return, en lo que viaja, es [logística inversa](../Despacho-y-entrega/logistica-inversa.md); Enable cruza todo.

## Los cinco atributos de desempeño

SCOR v13 mide la cadena con cinco atributos de nivel 1, cada uno con sus métricas. Según el documento, «Reliability, Responsiveness and Agility are considered customer-focused. Cost and Asset Management are considered internally focused.»

| Atributo | Qué es, según SCOR v13 | Métricas de nivel 1 |
|---|---|---|
| Confiabilidad (Reliability) | «The ability to perform tasks as expected» | Perfect Order Fulfillment (RL.1.1) |
| Capacidad de respuesta (Responsiveness) | «The speed at which tasks are performed» | Order Fulfillment Cycle Time (RS.1.1) |
| Agilidad (Agility) | «The ability to respond to external influences and marketplace changes» | Upside y Downside Supply Chain Adaptability (AG.1.1 y AG.1.2); Overall Value at Risk (AG.1.3) |
| Costo (Costs) | «The cost of operating the supply chain processes» | Total Supply Chain Management Costs (CO.1.1); Cost of Goods Sold (CO.1.2) |
| Gestión de activos (Asset Management) | «The ability to efficiently utilize assets» | Cash-to-Cash Cycle Time (AM.1.1); Return on Fixed Assets (AM.1.2); Return on Working Capital (AM.1.3) |

El pedido perfecto, la métrica de confiabilidad, se mide en [nivel de servicio logístico](../Despacho-y-entrega/nivel-de-servicio-logistico.md). No se leyó si la versión de siete procesos cambió los atributos.

> [!NOTE] Sin fuente todavía: los niveles 2 y 3 de SCOR, el diccionario de ASCM y el contenido de sus certificaciones (CSCP, CLTD, CPIM). El sitio de ASCM no se pudo leer.

## Lo que los marcos le piden a un sistema

Los marcos describen procesos y métricas. El dato mínimo que se deduce de ellos es inferencia de la base: el pedido perfecto de SCOR pide, por pedido, la fecha pedida y la real, si llegó completo, en qué estado y con qué documentos. Lo usa [nivel de servicio logístico](../Despacho-y-entrega/nivel-de-servicio-logistico.md#qué-hay-que-guardar-para-poder-medirlo). Lo que piden las escuelas y la evidencia del campo está en [fundamentos](fundamentos-de-cadena-de-suministro.md#lo-que-las-escuelas-y-la-evidencia-le-piden-a-un-sistema).
