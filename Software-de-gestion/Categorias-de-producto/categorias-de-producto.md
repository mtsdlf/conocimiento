---
resumen: >-
  Las categorías de producto son los nombres con que el mercado corta el software de gestión según los dominios que lleva cada caja: ERP, CRM, HCM, cadena de suministro, MES, mesa de ayuda, servicio de campo, PSA y mantenimiento. Ninguna tiene una frontera fija; dos productos de la misma categoría agrupan módulos distintos.
estado: borrador
estabilidad: estable
fuentes:
  - "Klaus, Rosemann y Gable (2000), «What is ERP?», Information Systems Frontiers 2(2):141-162 (solo el abstract): https://ideas.repec.org/a/spr/infosf/v2y2000i2d10.1023_a1026543906354.html"
  - "Gartner, definición de postmodern ERP y división en administrativo y operativo, según una nota de un proveedor de suite que la cita (resumen): https://www.netsuite.com/portal/resource/articles/erp/how-does-netsuite-fit-gartners-definition-of-postmodern-erp.shtml"
  - "Software Advice, «Postmodern ERP defined» (resumen del buscador): https://www.softwareadvice.com/resources/postmodern-erp-defined/"
  - "Gartner, documento sobre composable ERP (resumen): https://www.gartner.com/en/documents/6206787"
  - "Gartner, Magic Quadrant for Cloud ERP for Product-Centric Enterprises, octubre de 2025 (resumen): https://www.gartner.com/en/documents/7058198"
  - "IDC, nota de prensa sobre ingresos mundiales de aplicaciones empresariales 2023 (resumen): https://www.idc.com/resource-center/press-releases/worldwide-enterprise-applications-revenue-grew-12-0-in-2023-and-is-forecast-to-surpass-600-billion-in-2028-according-to-idc/"
  - "APQC, Understanding the PCF Elements (leído): https://www.apqc.org/sites/default/files/files/PCF%20Collateral/Understanding%20the%20PCF%20Elements%20%20-%20FINAL.pdf"
  - "Documentación de aplicaciones de un ERP de código abierto, versión 18.0 (leída): https://www.odoo.com/documentation/18.0/applications.html"
  - "Lista de módulos de otro ERP de código abierto y de su aplicación de personal (leídas): https://github.com/frappe/erpnext/blob/develop/erpnext/modules.txt y https://github.com/frappe/hrms/blob/develop/hrms/modules.txt"
  - "Light, Holland, Kelly y Willis (2000), «Best of Breed IT Strategy: An Alternative to ERP Systems», ECIS 2000 (abstract leído): https://aisel.aisnet.org/ecis2000/180"
  - "Light, Holland y Wills (2001), «ERP and best of breed: a comparative analysis», Business Process Management Journal 7(3):216-224 (solo el abstract): https://doi.org/10.1108/14637150110392683"
  - "TechTarget, «Postmodern ERP countered by continued appeal of single suite» (leído; cita a Denise Ganly, de Gartner, y a analistas de otras firmas): https://www.techtarget.com/enterprise-software/feature/Postmodern-ERP-countered-by-continued-appeal-of-single-suite"
  - "Software-de-gestion/.investigacion/fundamentos-y-categorias.md, taxonomias-externas-96.md y contraria.md (2026-11-27)"
aliases: [categorías de producto, categorías de software de gestión, enterprise application categories, suite, suite integrada, best of breed, best-of-breed, lo mejor de cada clase, ERP administrativo, ERP operativo, administrative ERP, operational ERP, postmodern ERP, ERP posmoderno, composable ERP]
creado: 2026-11-27
revisado:
---

# Categorías de producto

Las categorías de producto son los nombres con que el mercado corta el software de gestión según los dominios que lleva cada caja: ERP, CRM, HCM, cadena de suministro, MES, mesa de ayuda, servicio de campo, PSA y mantenimiento. Ninguna tiene una frontera fija; dos productos de la misma categoría agrupan módulos distintos.

Es la vertical que mira el [software de gestión](../software-de-gestion.md) desde afuera: qué dominios junta cada producto y para qué empresa. El saber de cada dominio vive en su tema del área «Gestión de la empresa»; acá se cuenta cómo lo empaqueta cada categoría y dónde termina. La pregunta que más se repite entre categorías, qué sistema manda en cada dato, está en [integración y migración](../Columnas-tecnicas/integracion-y-migracion.md), y de dónde viene cada sigla, en la [historia del software de gestión](../Fundamentos/historia-del-software-de-gestion.md).

## Cómo corta el mercado: por dominio y por tipo de empresa

Las categorías salen de los analistas de mercado y de los proveedores, no de una norma. Gartner afirma que el ERP «is neither defined as a single integrated suite, nor is it a specific set of modules» (según una nota de un proveedor que la cita). Klaus, Rosemann y Gable (2000) compararon las definiciones de ERP de la literatura y de expertos, y concluyeron que «it is unlikely that at this stage a broadly agreed definition of ERP can be achieved». La categoría es una forma de empaquetar, no un saber.

| Categoría | Dominio que lleva | Cómo la parte el mercado (según resúmenes) |
|---|---|---|
| [ERP](erp.md) | Contabilidad, tesorería, impuestos, compras, stock, producción | Gartner: un cuadrante para empresas de producto y otro para empresas de servicios (octubre de 2025) |
| [CRM](crm.md) | Relación con clientes, y a veces atención y marketing | Gartner: automatización de ventas y centro de atención por separado; marketing aparte |
| [HCM](hcm.md) | Administración de personal y nómina, y el talento | Gartner: suites para empresas de más de 1.000 empleados |
| [SCM, WMS y TMS](scm-wms-y-tms.md) | Planificación de la cadena, depósito, transporte | Gartner: planificación por un lado, ejecución (WMS y TMS) por otro |
| [MES](mes.md) | Ejecución en planta y calidad | ISA-95 lo ubica en el nivel 3 |
| [Servicio de campo y mesa de ayuda](servicio-de-campo-y-mesa-de-ayuda.md) | Servicio al cliente y servicio de campo | Dos mercados distintos |
| [PSA](psa.md) | Servicios profesionales y proyectos | Gartner: guía de mercado, sin cuadrante |
| [EAM y CMMS](eam-y-cmms.md) | Activos y mantenimiento | El CMMS es el antecesor del EAM |

IDC corta distinto, según el resumen de una nota de prensa: gestión de recursos de la empresa, CRM, ingeniería, cadena de suministro y producción. Los productos tampoco coinciden: un ERP de código abierto pone las reparaciones en la familia de cadena de suministro, y otro saca el personal y la nómina a una aplicación aparte. Por eso esta base clasifica por el dominio que lleva cada categoría y no por los menús de un producto.

## Administrativo frente a operativo

Gartner reparte la funcionalidad del ERP en dos mitades: la administrativa (finanzas, personal, compras) y la operativa (producción, distribución). La fuente primaria no se pudo leer; el corte aparece en resúmenes de terceros y en la definición de composable ERP, «a technology strategy that automates and links administrative and operational business capabilities». APQC hace un corte parecido en su marco de procesos: categorías operativas (1.0 a 6.0) y de gestión y soporte (7.0 a 13.0).

En la lectura de esta base, lo administrativo es lo que toda empresa registra igual: el asiento, la factura, la orden de compra, el recibo de sueldo. Lo operativo depende del negocio: órdenes de producción en una fábrica, horas imputadas en una consultora, órdenes de trabajo en una empresa de mantenimiento. Los dos cuadrantes de ERP de Gartner, para empresas de producto y de servicios, siguen esa línea.

El núcleo administrativo es parecido en todos los rubros y pesa por la normativa de cada país; lo operativo cambia de rubro en rubro, y ahí nace el [software por rubro](software-por-rubro.md) (inferencia de esta base).

> [!NOTE] Sin fuente todavía: la definición primaria de Gartner de ERP administrativo y operativo. Sin ella no se puede fijar la frontera exacta; por ejemplo, si compras es administrativa u operativa.

## Suite o lo mejor de cada clase

Una empresa puede comprar una **suite**, un solo producto de un proveedor que lleva varios dominios sobre una base común, o elegir **lo mejor de cada clase** (*best-of-breed*): el mejor producto para cada dominio, conectado con los otros. El debate tiene 25 años y pocas pruebas.

> [!IMPORTANT]
> **Qué conviene, suite o lo mejor de cada clase, está en disputa, y ninguna posición tiene evidencia medida.**
>
> - **A favor de lo mejor de cada clase.** Light, Holland, Kelly y Willis (2000) sostienen, según su abstract, que los paquetes de un solo proveedor «often fail to fit specific organizational and industry needs», y que combinar productos de varios proveedores ajusta mejor. Su evidencia es un caso, una empresa global de entretenimiento; Light, Holland y Wills (2001) comparan las dos estrategias en otro caso. Gartner llamó *postmodern ERP* (2013 o 2014, según la fuente) a federar «the best applications, likely from two or more vendors, in each business area», y esperaba que esa estrategia pasara de cerca del 15 % de las empresas a más del 40 % hacia 2020. No se encontró si se cumplió. Después vino el *composable ERP*, según resúmenes, bloques unidos por interfaces.
> - **A favor de la suite.** El artículo de la prensa del sector que cuenta el *postmodern ERP* se titula «countered by continued appeal of single suite». Cita a analistas de otras firmas: las empresas siguen con un solo proveedor y los pronósticos de Gartner no se estaban cumpliendo. Un exanalista cuenta que clientes que querían reemplazar el módulo de finanzas lo encontraron atado a compras y a pagos.
> - **Lo que falta.** No hay un estudio independiente que mida cuál de las dos rinde más. Casi todas las voces tienen interés comercial, y la evidencia académica más citada es de 2000 y 2001.

En la lectura de esta base, el debate es sobre dónde poner la frontera de integración. La suite paga en ajuste: lleva los dominios como los modeló el proveedor. Lo mejor de cada clase paga en integración: cada frontera entre productos obliga a decidir qué sistema es la [fuente de verdad](../Columnas-tecnicas/integracion-y-migracion.md) del cliente, del artículo o del precio, y a mantener esa conexión en cada actualización. El caso del módulo de finanzas atado a compras muestra que la frontera más cara de mover es la que pasa por un documento con efecto contable.

## Lo que no es categoría en este tema

Tres cosas que venden los proveedores grandes no tienen nota acá:

- **La inteligencia de negocio**, que junta datos de varias fuentes para decidir. Es de [Visualización y BI](../../Datos/Visualizacion-y-BI/visualizacion-y-bi.md), en Datos, que se va a ampliar con «BI sobre el software de gestión». Lo que el sistema entrega de su propia base (los libros, los listados del día) es una columna técnica, la de reportes operativos y legales.
- **El comercio electrónico y el punto de venta.** Son del tema Comercio electrónico, que tiene su propia nota de [sistemas de gestión en el comercio](../../Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion/sistemas-de-gestion.md).
- **La gestión de servicios de TI, la gestión documental y las plataformas de integración.** No llevan un dominio de negocio de esta base. La primera aparece como vecina de la [mesa de ayuda](servicio-de-campo-y-mesa-de-ayuda.md).

## Lo que hay adentro de Categorías de producto

- [Escalones por tamaño](escalones-por-tamano.md) — del facturador al ERP de una empresa grande, y qué cambia en cada escalón.
- [ERP](erp.md) — los dominios administrativos y, en empresas de producto, el stock y la producción; el centro contra el que se integran las demás.
- [CRM](crm.md) — el registro del cliente y lo que pasa antes del pedido, con la atención y el marketing que a veces suma.
- [HCM](hcm.md) — el legajo, la nómina y el talento.
- [SCM, WMS y TMS](scm-wms-y-tms.md) — la planificación de la cadena, el depósito y el transporte.
- [MES](mes.md) — la ejecución en planta, su frontera con el ERP y la gestión de calidad.
- [Servicio de campo y mesa de ayuda](servicio-de-campo-y-mesa-de-ayuda.md) — dos mercados de la posventa: el caso del cliente y el técnico en la calle.
- [PSA](psa.md) — el software de las firmas que venden horas de gente por proyecto.
- [EAM y CMMS](eam-y-cmms.md) — el registro de los equipos y su mantenimiento.
- [Software por rubro](software-por-rubro.md) — el software hecho para una industria frente al que sirve a cualquiera.
