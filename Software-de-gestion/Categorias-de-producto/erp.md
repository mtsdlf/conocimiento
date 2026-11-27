---
resumen: >-
  El ERP (planificación de recursos de la empresa) es la categoría de software de gestión que lleva sobre una base de datos común los dominios administrativos de una empresa y, en las que mueven productos, el stock, la producción y la distribución. No tiene una definición acordada ni una lista fija de módulos.
estado: vigente
estabilidad: estable
fuentes:
  - "Klaus, Rosemann y Gable (2000), «What is ERP?», Information Systems Frontiers 2(2):141-162 (solo el abstract): https://ideas.repec.org/a/spr/infosf/v2y2000i2d10.1023_a1026543906354.html"
  - "Davenport (1998), «Putting the Enterprise into the Enterprise System», Harvard Business Review 76(4):121-131 (solo el resumen del buscador; copia con login sin leer): https://fenix.iseg.ulisboa.pt/downloadFile/281608120778205/HBR_1998_Davenport_ES.pdf"
  - "Gartner, glosario «Enterprise Resource Planning (ERP)» (403; solo el extracto del buscador): https://www.gartner.com/en/information-technology/glossary/enterprise-resource-planning-erp"
  - "Gartner, citado en una nota de un proveedor de suite (resumen): https://www.netsuite.com/portal/resource/articles/erp/how-does-netsuite-fit-gartners-definition-of-postmodern-erp.shtml"
  - "Gartner, Magic Quadrant for Cloud ERP for Product-Centric Enterprises, octubre de 2025 (resumen): https://www.gartner.com/en/documents/7058198"
  - "Wikipedia, «Enterprise resource planning» (leída en parte): https://en.wikipedia.org/wiki/Enterprise_resource_planning"
  - "Documentación de aplicaciones de un ERP de código abierto, versión 18.0 (leída): https://www.odoo.com/documentation/18.0/applications.html"
  - "Lista de módulos de otro ERP de código abierto y de su aplicación de personal (leídas): https://github.com/frappe/erpnext/blob/develop/erpnext/modules.txt y https://github.com/frappe/hrms/blob/develop/hrms/modules.txt"
  - "ISA, página «ISA-95 Standard» (leída): https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard"
  - "Software-de-gestion/.investigacion/fundamentos-y-categorias.md y taxonomias-externas-96.md (2026-11-27)"
aliases: [ERP, enterprise resource planning, planificación de recursos empresariales, planificación de recursos de la empresa, sistema integrado de gestión, ERP de producto, ERP de servicios, product-centric ERP, service-centric ERP]
creado: 2026-11-27
revisado: 2026-11-27
---

# ERP

El ERP (planificación de recursos de la empresa) es la categoría de software de gestión que lleva sobre una base de datos común los dominios administrativos de una empresa y, en las que mueven productos, el stock, la producción y la distribución. No tiene una definición acordada ni una lista fija de módulos.

En la lectura de esta base, es la categoría central de las [categorías de producto](categorias-de-producto.md): las demás se definen por lo que le sacan al ERP o por cómo se conectan con él. La sigla viene de extender el MRP de la manufactura al resto de la empresa; esa historia está en la [historia del software de gestión](../Fundamentos/historia-del-software-de-gestion.md).

## Una categoría sin definición acordada

En la lectura de esta base, las definiciones coinciden en un núcleo y discrepan en el borde. Klaus, Rosemann y Gable (2000) cruzaron un análisis histórico, la literatura de sistemas de información y una encuesta a académicos, encontraron «dissenting views on the phenomenon» y concluyeron que no era probable una definición común. Según un resumen, Davenport (1998) describe el sistema empresarial como una base de datos central que recibe datos de aplicaciones modulares y las alimenta, y que cubre casi todas las actividades de la empresa. Gartner, según extractos de su glosario, habla de aplicaciones que automatizan procesos administrativos y operativos, y aclara que el ERP no es una suite única ni un conjunto fijo de módulos.

El núcleo común son aplicaciones modulares sobre una base de datos compartida. El borde en disputa es si el CRM y la relación con proveedores son parte del ERP y si hace falta un solo proveedor. Esta base resuelve la disputa sin tomar partido: trata al ERP como una forma de empaquetar dominios y define cada categoría por el dominio que lleva.

## Qué dominios junta

Wikipedia lista como módulos comunes la contabilidad financiera y de gestión, el personal, la manufactura, el procesamiento de pedidos, la cadena de suministro, los proyectos, el CRM, la relación con proveedores y los contratos. Cada uno modela un dominio que existe sin software:

| Módulo del ERP | Dominio que modela | Lo que lleva casi siempre |
|---|---|---|
| Contabilidad | [Contabilidad](../../Contabilidad/contabilidad.md) | El [asiento y los libros](../../Contabilidad/Registro/asiento-y-libros.md), las cuentas corrientes, el activo fijo contable |
| Tesorería | [Tesorería](../../Tesoreria/tesoreria.md) | Bancos, cobros, la corrida de pagos |
| Impuestos y localización | [Impuestos](../../Impuestos/impuestos.md) | El comprobante fiscal y los registros que pide el fisco |
| Compras | [Compras y abastecimiento](../../Compras-y-abastecimiento/compras-y-abastecimiento.md) | La [orden de compra](../../Compras-y-abastecimiento/Orden-de-compra/orden-de-compra.md) y la recepción contra lo pedido |
| Ventas | [Relación con clientes](../../Relacion-con-clientes/relacion-con-clientes.md) | El presupuesto y el [pedido de venta](../../Relacion-con-clientes/Pedido-de-venta/pedido-de-venta.md) |
| Stock | [Inventario y depósitos](../../Inventario-y-depositos/inventario-y-depositos.md) | Las existencias por depósito y sus movimientos |
| Producción | [Producción](../../Produccion/produccion.md) | La lista de materiales, el MRP y la orden de producción |
| Personal y nómina | [Administración de personal y nómina](../../Administracion-de-personal-y-nomina/administracion-de-personal-y-nomina.md) | En unos productos sí; en otros va aparte |
| Proyectos | [Servicios profesionales y proyectos](../../Servicios-profesionales-y-proyectos/servicios-profesionales-y-proyectos.md) | En los ERP para empresas de servicios |

La tercera columna es lectura de esta base. Las tres últimas filas son las que más cambian de producto a producto. Un ERP de código abierto deja personal y nómina en una aplicación aparte, con diez módulos propios; otro los trae adentro, junto con la flota y el almuerzo. Los dos traen además calidad y mantenimiento, y uno trae también activos; en el mercado esos temas también se venden como categorías propias.

## Un ERP para empresas de producto y otro para empresas de servicios

Gartner evalúa el ERP en dos cuadrantes, ambos de octubre de 2025: uno para empresas centradas en el producto, que según su resumen soporta y automatiza «operational activities across manufacturing, distribution, and supply chain», y otro para empresas centradas en el servicio. El núcleo administrativo es el mismo en los dos; cambia la mitad operativa ([administrativo frente a operativo](categorias-de-producto.md#administrativo-frente-a-operativo)). En el de producto, la parte operativa es el stock, la producción y la distribución; en el de servicios, los proyectos, las personas y las horas, el terreno del [PSA](psa.md).

## Dónde termina el ERP

El ERP se pisa con casi todas las demás categorías, y la frontera la decide cada producto:

- Con el [CRM](crm.md), en el pedido: el CRM llega hasta la oportunidad o el presupuesto, el ERP toma desde el presupuesto o el pedido. Un ERP de código abierto separa en módulos distintos lo de antes del pedido y lo de después.
- Con el [MES](mes.md), en la planta: según ISA-95, el nivel 4 es el de la planificación del negocio y la logística, donde va el ERP, y el nivel 3 es el del MES. El ERP planifica y registra; el MES ejecuta.
- Con [SCM, WMS y TMS](scm-wms-y-tms.md), en el detalle: el ERP lleva el stock por depósito y el pedido; el WMS, cada ubicación y cada preparación; el TMS, el viaje.
- Con el [HCM](hcm.md), en el talento: el ERP puede llevar la nómina y su asiento, pero contratar, evaluar y desarrollar personas se vende aparte.
- Con el [EAM](eam-y-cmms.md), en el activo: el ERP lleva el bien de uso y su amortización; el EAM, el equipo físico y su mantenimiento.

## El ERP como centro de las integraciones

Todo documento con efecto económico termina en un asiento, y el asiento vive en el ERP. Por eso, en la lectura de esta base, las demás categorías se integran contra el ERP y no entre sí: el CRM le pasa el pedido, el HCM la nómina para contabilizar, el PSA las horas a facturar, el servicio de campo los repuestos y la mano de obra. La pregunta de cada conexión es qué sistema es la fuente de verdad de cada dato, y se trata en [integración y migración](../Columnas-tecnicas/integracion-y-migracion.md). Los recorridos que cruzan módulos, como [del pedido al cobro](../../Procesos-de-negocio/del-pedido-al-cobro.md), están en Procesos de negocio.

Qué tan grande es el ERP que necesita una empresa cambia con su tamaño: el sistema de una pyme y el de una multinacional comparten la sigla y poco más ([escalones por tamaño](escalones-por-tamano.md)).

> [!NOTE] Sin fuente todavía: el texto completo de Klaus, Rosemann y Gable (2000) y de Davenport (1998); la definición de Gartner es un extracto del buscador. Para fijar qué atributos del ERP son de consenso, leer la sección de definiciones y la encuesta de Klaus y otros, y fijarse en cuáles se repiten (integración, base común, modularidad) y cuáles se discuten.
