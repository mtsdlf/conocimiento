---
resumen: >-
  Un marco de procesos clasifica por función todo lo que hace una empresa, sin decir en qué orden; un proceso de punta a punta toma piezas de varias funciones y las ordena hasta un resultado. El marco general es el Process Classification Framework (PCF) de APQC, del que salen los códigos de los ocho recorridos de este tema; los marcos de un solo dominio se explican en su tema.
estado: borrador
estabilidad: estable
fuentes:
  - "APQC, Process Classification Framework, Cross-Industry, versión 7.4 (agosto de 2024), entero: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "APQC, PCF Business Rules, reglas 1, 3, 4 y 6: https://www.apqc.org/sites/default/files/files/PCF%20Collateral/PCF%20Business%20Rules.pdf"
  - "APQC, Understanding the Elements of APQC's Process Classification Framework: https://www.apqc.org/sites/default/files/files/PCF%20Collateral/Understanding%20the%20PCF%20Elements%20%20-%20FINAL.pdf"
  - "Lundquist (APQC), Why are end-to-end processes important?, 15 de enero de 2024: https://www.apqc.org/blog/why-are-end-end-processes-important"
  - "APQC, página del PCF 8.0 (27 de febrero de 2026; según el buscador, no leída): https://www.apqc.org/pcf-pdf"
  - "ITU-T, Recomendación M.3050.1 (03/2007), resumen e índice: https://www.itu.int/dms_pubrec/itu-t/rec/m/T-REC-M.3050.1-200703-I!!SUM-HTM-E.htm"
  - "Wikipedia, Business Process Framework (eTOM): https://en.wikipedia.org/wiki/Business_Process_Framework_(eTOM) (secundaria)"
  - "Procesos-de-negocio/.investigacion/marcos-de-procesos.md (informe del 2026-11-27)"
aliases: [marco de procesos, process framework, Process Classification Framework, PCF, APQC PCF, códigos APQC, marco funcional, end-to-end process, E2E, proceso de punta a punta, eTOM, Business Process Framework, MECE]
creado: 2026-11-27
revisado:
---

# Marcos de procesos

Un marco de procesos clasifica por función todo lo que hace una empresa, sin decir en qué orden; un proceso de punta a punta toma piezas de varias funciones y las ordena hasta un resultado. El marco general es el Process Classification Framework (PCF) de APQC, del que salen los códigos de los ocho recorridos de este tema; los marcos de un solo dominio se explican en su tema.

Es parte de los [fundamentos de procesos de negocio](fundamentos-de-procesos-de-negocio.md), y sus términos están en el [glosario](glosario-de-procesos-de-negocio.md). Los marcos se citan y no tienen vertical propia: así lo decidió el issue #99 del mapa de la base.

## Clasificar por función o recorrer hasta un resultado

El PCF clasifica y no ordena. Sus reglas lo dicen: «The PCF reflects a functional view of an organization, rather than a cross-functional view». La portada del PCF 7.4 lo llama, en cambio, «taxonomy of cross-functional business processes». Por lectura de la base, la estructura es funcional y «cross-functional» describe el alcance, toda la empresa. Arranca por las grandes funciones y las descompone siguiendo el principio MECE, mutuamente excluyentes y colectivamente exhaustivas: las categorías «should collectively describe all of the work done at an organization and should not overlap each other».

El marco deja el orden afuera a propósito. Quiere juntar «the complete collection of what happens at each part of the organization, not the order in which these things happen or the dependency between these elements». Por eso «the order of process elements within a hierarchy does not imply execution order». Que 3.5.4 venga antes de 4.4.3 no dice que el pedido vaya antes de la preparación.

El proceso de punta a punta es lo que el marco no da. APQC lo define como «cross-functional processes that comprise all the steps to accomplish a specific outcome or goal», con order-to-cash, hire-to-retire e idea-to-market de ejemplo. Para armarlo usa el PCF como «ingredient list»: order-to-cash toma 3.5.4.1, aceptar y validar el pedido, y 3.5.4.3, ver la disponibilidad, y sigue con piezas de las categorías 4.0 y 9.0. Ordenar esas piezas, decir qué documento pasa entre ellas y medir el recorrido entero es el trabajo de este tema.

APQC publica una colección de mapas y medidas de punta a punta (según el buscador, entre ellos procure-to-pay y S&OP; la investigación previa de la base lista además record-to-report, order-to-cash, hire-to-retire e issue-to-resolution, sin comprobarlo). No se encontraron del proyecto al cobro, de la planificación a la producción ni de la compra a la baja del activo. Ninguno se leyó, así que la selección de piezas de la tabla de abajo es de esta base.

## Las trece categorías del PCF 7.4

El PCF tiene 13 categorías de nivel 1, seis operativas y siete de gestión y soporte, con «more than 1,000 processes and associated activities». El PCF existe desde 1992.

| Código | Categoría | Grupo |
|---|---|---|
| 1.0 | Develop Vision and Strategy | Operating processes |
| 2.0 | Develop and Manage Products and Services | Operating processes |
| 3.0 | Market and Sell Products and Services | Operating processes |
| 4.0 | Manage Supply Chain for Physical Products | Operating processes |
| 5.0 | Deliver Services | Operating processes |
| 6.0 | Manage Customer Service | Operating processes |
| 7.0 | Develop and Manage Human Capital | Management and support services |
| 8.0 | Manage Information Technology (IT) | Management and support services |
| 9.0 | Manage Financial Resources | Management and support services |
| 10.0 | Acquire, Construct, and Manage Assets | Management and support services |
| 11.0 | Manage Enterprise Risk, Compliance, Remediation, and Resiliency | Management and support services |
| 12.0 | Manage External Relationships | Management and support services |
| 13.0 | Develop and Manage Business Capabilities | Management and support services |

Los nombres cambian entre versiones. En el índice de la 7.4, 5.0 es «Deliver Services» y en el cuerpo, «Deliver Service». Otro documento de APQC, sin versión, llama a 4.0 «Deliver Physical Products».

## Cómo se numera y qué versión se leyó

Cada categoría baja cuatro niveles más: grupo de procesos (nivel 2, como 9.2), proceso (nivel 3, como 9.2.3), actividad (nivel 4, como 9.2.3.3) y tarea (nivel 5). Cada elemento tiene dos números. El jerárquico lo ubica y cambia con cada versión: «The numbers are specific to a particular release and are not comparable across version numbers». El de cinco dígitos, como el 10185 de 3.5.4 «Manage sales orders», sigue al concepto entre versiones.

Esta base leyó entera la versión 7.4, de agosto de 2024, en la copia que publica la Federación Internacional de la Cruz Roja. Según el buscador, APQC publicó la 8.0 el 27 de febrero de 2026. No se pudo leer, y los números de abajo pueden haber cambiado. Algunos temas de la base citan la 7.2.1, y sus números no se comparan con los de la 7.4. Un sistema que guarde códigos APQC tiene que guardar la versión y el identificador de cinco dígitos (inferencia de esta base).

## Los códigos de los ocho recorridos

Los códigos y nombres son literales del PCF 7.4; qué piezas entran en cada recorrido es lectura de esta base. Cada nota de proceso los copia en una línea.

| Recorrido | Piezas del PCF 7.4 |
|---|---|
| [Del pedido al cobro](../del-pedido-al-cobro.md) | 3.5.4 Manage sales orders; 4.1.2.4 Determine available to promise; 4.4.3.4 Pick, pack, and ship product for delivery; 4.4.4.1 Plan, transport, and deliver outbound product; 9.2.1 Process customer credit; 9.2.2 Invoice customer; 9.2.3 Process accounts receivable (AR), con 9.2.3.3 Apply cash remittances; 9.2.4 Manage and process collections; 9.2.5 Manage and process adjustments/deductions; 9.7.2.1 Manage and reconcile cash positions |
| [De la compra al pago](../de-la-compra-al-pago.md) | 4.2.3 Order materials and services; 4.2.4.4 Monitor quality of product delivered; 4.4.3.2 Receive, inspect, and store inbound deliveries; 9.6.1 Process accounts payable (AP), con 9.6.1.3 Audit invoices and key data in AP system, 9.6.1.4 Approve payments y 9.6.1.8 Process payments; 9.7.2.3 Process and oversee electronic fund transfers (EFTs) |
| [Del registro al balance](../del-registro-al-balance.md) | 9.3.1 Manage financial policies and procedures; 9.3.2 Perform general accounting, con 9.3.2.4 Process period end adjustments, 9.3.2.5 Post and reconcile intercompany transactions, 9.3.2.6 Reconcile general ledger accounts, 9.3.2.7 Perform consolidations and process eliminations y 9.3.2.8 Prepare trial balance; 9.3.3.6 Calculate and record depreciation expense; 9.3.4 Perform financial reporting; 9.1.2.1 Perform inventory accounting; 9.7.2.1 Manage and reconcile cash positions; 9.8 Manage internal controls; 9.9.2 Process taxes, con 9.9.2.2 Prepare tax returns |
| [De la planificación a la producción](../de-la-planificacion-a-la-produccion.md) | 4.1.2 Manage demand for products; 4.1.3 Create materials plan; 4.1.4 Create and manage master production schedule; 4.2.3 Order materials and services; 4.3 Produce/Assemble/Test product (4.3.1 a 4.3.4); 4.4.3.7 Manage physical finished goods inventory; 9.1.2.4 Perform product costing; 9.1.2.5 Perform variance analysis |
| [De la contratación a la baja](../de-la-contratacion-a-la-baja.md) | 7.2.1 Manage employee requisitions; 7.2.4 Manage new hire/re-hire; 7.3.1 Manage employee orientation and deployment; 7.5.2 Manage and administer benefits; 7.5.4 Administer payroll; 7.6.1 Manage promotion and demotion process; 7.6.2 Manage separation; 7.6.3 Manage retirement; 7.6.4 Manage leave of absence; 7.7.3 Manage and maintain employee data; 9.5 Process payroll (9.5.1 Report time, 9.5.2 Manage pay, 9.5.3 Manage and process payroll taxes) |
| [Del reclamo a la resolución](../del-reclamo-a-la-resolucion.md) | 6.2.2 Manage customer service problems, requests, and inquiries; 6.2.3 Manage customer complaints; 6.2.4 Process returns; 6.3.2 Process warranty claims; 6.3.4 Service products; 6.5.2 Measure customer satisfaction with customer-complaint handling and resolution; 4.4.2.4 Manage flow of returned products; 4.4.2.5 Manage disposition of returned products; 4.3.3.5 Track and analyze non-conformance trends; 9.2.2.5 Resolve customer billing inquiries; 9.2.5 Manage and process adjustments/deductions |
| [Del proyecto al cobro](../del-proyecto-al-cobro.md) | 5.2.2 Create and manage resource plan; 5.3.1 Initiate service delivery; 5.3.2 Execute service delivery; 5.3.3 Complete service delivery; 9.5.1 Report time; 9.6.2 Process expense reimbursements; 9.2.2 Invoice customer; 9.2.3 Process accounts receivable (AR); 9.2.4 Manage and process collections; 9.1.4.1 Assess customer and product profitability |
| [De la compra a la baja del activo](../de-la-compra-a-la-baja-del-activo.md) | 9.4.1 Perform capital planning and project approval; 10.1.1.3 Determine build, buy, or lease decision; 4.2.3 Order materials and services; 9.3.3 Perform fixed-asset accounting; 9.4.2 Perform capital project accounting; 10.3 Maintain assets; 10.4 Manage asset end-of-life |

Cuatro cosas que el PCF no nombra, y que este tema pone en los traspasos: el cruce de tres vías (lo más cercano es 9.6.1.3), la nota de crédito, la factura por horas o hitos (en el PCF, la hora es nómina: 9.5.1) y el cierre como un todo, porque los ajustes están repartidos en 9.3.2.4, 9.5.2.7 y 9.6.1.5. Los subprocesos de producción y de cadena, uno por uno, están en [marcos de la producción](../../Produccion/Fundamentos/marcos-de-la-produccion.md#el-pcf-de-apqc-de-41-a-43) y [marcos de la cadena de suministro](../../Cadena-de-suministro-y-logistica/Fundamentos/marcos-de-la-cadena-de-suministro.md#el-pcf-de-apqc-proceso-por-proceso).

## Los marcos de un solo dominio

Cada uno de estos marcos corta un dominio con más detalle que el PCF y se explica en el tema de ese dominio.

| Marco | Quién lo publica | Dónde está en la base |
|---|---|---|
| SCOR | ASCM | [Marcos de la cadena de suministro](../../Cadena-de-suministro-y-logistica/Fundamentos/marcos-de-la-cadena-de-suministro.md#scor-qué-versión-se-leyó), con Make en [marcos de la producción](../../Produccion/Fundamentos/marcos-de-la-produccion.md#scor-y-cpim-lo-poco-que-se-sabe) |
| ISA-95 (IEC 62264) | ISA | [Marcos de la producción](../../Produccion/Fundamentos/marcos-de-la-produccion.md#isa-95-cinco-niveles-y-la-frontera-entre-erp-y-mes) |
| Ciclo de compras de 13 pasos | CIPS | [Fundamentos de compras](../../Compras-y-abastecimiento/Fundamentos/fundamentos-de-compras-y-abastecimiento.md#cómo-dividen-el-dominio-cips-apqc-y-esta-base) |
| BASK | SHRM | [Fundamentos de administración de personal](../../Administracion-de-personal-y-nomina/Fundamentos/fundamentos-de-administracion-de-personal.md#cómo-dividen-el-dominio-los-marcos-y-los-productos) |
| ISO 10002, ISO 18295-1 e ITIL 4 | ISO; las guías de ITIL | [Fundamentos de servicio al cliente](../../Servicio-al-cliente/Fundamentos/fundamentos-de-servicio-al-cliente.md#cómo-se-divide-el-campo-a-sí-mismo) |

### eTOM, el marco de una industria

El eTOM, o Business Process Framework, es el marco de procesos de las telecomunicaciones, y en esta base no tiene tema. Lo mantiene TM Forum, una asociación de proveedores de servicios y de sus proveedores en las industrias de telecomunicaciones y entretenimiento, y la UIT lo publicó como la serie M.3050. Según el resumen de la M.3050.1, de 2007, «describes the enterprise processes required by a service provider» y es «a reference framework for categorizing the business activities that a service provider will use».

Según Wikipedia, tiene tres áreas («Strategy, Infrastructure & Product», «Operations» y «Enterprise Management»), y en Operations cruza filas por objeto (cliente, servicio, recurso, proveedor) con columnas por resultado: «Operations Support & Readiness, Fulfillment, Assurance and Billing». Esas columnas se parecen más a recorridos que las categorías del PCF (lectura de esta base; el texto de TM Forum da 403). APQC prevé el caso con versiones de industria del PCF para lo que es «materially different or absent» en el general.

## Qué le sirve a quien construye software, y qué no

El marco sirve para tres cosas, todas lectura de esta base sobre las reglas de APQC:

- **Un vocabulario común.** Cada elemento empieza con un verbo y es descriptivo. Cuando un cliente dice «cuentas a pagar», 9.6.1 dice qué entra y qué no.
- **Comparar.** El PCF es la base del banco de medidas de APQC, el Open Standards Benchmarking, y cada medida cuelga de un elemento. Las notas de proceso citan esas medidas por su número.
- **Revisar cobertura.** Como las categorías no se pisan y cubren todo, recorrer una categoría muestra qué hace la empresa que el producto no lleva.

Tiene dos límites que importan para un sistema. No dice el orden ni las dependencias entre pasos, que es lo que un sistema tiene que validar. Y no dice qué se registra: ningún elemento nombra el documento que deja ni los datos que lleva, que vienen del dominio. Además, cada marco reparte distinto: en el PCF el crédito y la cobranza son contabilidad de ingresos (9.2) y no tesorería (9.7), y la nómina aparece dos veces (7.5.4 y 9.5).

> [!NOTE] Sin fuente todavía: el PCF 8.0 y los mapas de punta a punta de APQC (el acceso no se pudo comprobar: la página responde 403), para cotejar los códigos de la tabla; el texto de TM Forum sobre el eTOM.
