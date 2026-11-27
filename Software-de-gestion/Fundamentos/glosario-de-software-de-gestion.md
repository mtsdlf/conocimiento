---
resumen: >-
  Los términos del tema Software de gestión, cada uno con su nombre en inglés, una definición corta y la nota donde vive, agrupados por la vertical del tema a la que pertenecen.
estado: borrador
estabilidad: estable
fuentes:
  - "Klaus, Rosemann y Gable (2000), What is ERP? (abstract): https://ideas.repec.org/a/spr/infosf/v2y2000i2d10.1023_a1026543906354.html"
  - "ISA, ISA-95 Standard: https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard"
  - "Fowler, Accounting Narrative: https://martinfowler.com/eaaDev/AccountingNarrative.html"
  - "Fowler, Temporal Patterns: https://martinfowler.com/eaaDev/timeNarrative.html"
  - "Fowler, Audit Log: https://martinfowler.com/eaaDev/AuditLog.html"
  - "Fowler, Organization Structures (Accountability, Knowledge Level, Party): https://martinfowler.com/apsupp/accountability.pdf"
  - "Hohpe y Woolf, Enterprise Integration Patterns, estilos de integración: https://www.enterpriseintegrationpatterns.com/patterns/messaging/IntegrationStylesIntro.html"
  - "Documentación de un ERP de código abierto, DocStatus (según el resumen): https://docs.frappe.io/framework/doctypes/docstatus"
  - "Documentación de un ERP de código abierto, cierre del ejercicio y fecha de bloqueo: https://raw.githubusercontent.com/odoo/documentation/19.0/content/applications/finance/accounting/reporting/year_end.rst"
  - "Guía de corte de un proveedor grande: https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/prepare-go-live-cutover-strategy"
  - "Guía de extensibilidad de un proveedor grande: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/extensibility/extensibility-home-page"
  - "Soh, Sia y Tay-Yap (2000), Cultural fits and misfits (según resúmenes): https://cacm.acm.org/research/enterprise-resource-planning-cultural-fits-and-misfits"
  - "Brehm, Heinzl y Markus (2001), Tailoring ERP systems, HICSS-34 (según resúmenes): https://doi.org/10.1109/HICSS.2001.927130"
  - "Software-de-gestion/.investigacion/ (fundamentos-y-categorias.md, columnas-tecnicas-97.md, implementacion.md, mercado-y-economia.md y taxonomias-externas-96.md, 2026-11-27)"
aliases: [glosario de ERP, ERP glossary, términos de software de gestión, vocabulario de ERP, siglas de software de gestión]
creado: 2026-11-27
revisado:
---

# Glosario de software de gestión

Los términos del tema Software de gestión, cada uno con su nombre en inglés, una definición corta y la nota donde vive, agrupados por la vertical del tema a la que pertenecen.

En lectura de esta base, el campo no tiene una norma de terminología propia, y cada producto llama distinto a lo mismo (confirmar, validar, contabilizar, asentar). Estas son las palabras que usa la base, con un solo sentido cada una. Cuando un término es de un dominio, la definición es la de su tema y la columna «Dónde» enlaza las dos notas. La definición completa y sus fuentes están en la nota enlazada; el contexto del campo, en [fundamentos](fundamentos-de-software-de-gestion.md).

## El todo

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Software de gestión | Enterprise software, business software | El software que lleva los dominios de una empresa sobre registros compartidos; ERP, CRM o MES son formas de empaquetarlo | [software de gestión](../software-de-gestion.md) |
| Dominio | Domain | Un saber de la empresa que existe sin software (contabilidad, compras, producción), con su propio tema en la base | [software de gestión](../software-de-gestion.md) |
| Módulo | Module | La parte de un producto que lleva un dominio o una parte de él; cada producto corta los módulos distinto | [categorías de producto](../Categorias-de-producto/categorias-de-producto.md) |
| Localización | Localization | Lo que un producto agrega para cumplir las normas de un país: comprobantes, libros, impuestos, plan de cuentas | [software de gestión en la Argentina](../software-de-gestion-en-argentina.md), [mercado en la Argentina](../Mercado-y-economia/mercado-en-argentina.md) |
| MRP | Material requirements planning | El cálculo de qué materiales hacen falta y cuándo; el primer software de gestión vendido como producto | [MRP](../../Produccion/Planificacion-de-la-produccion/mrp.md), [historia](historia-del-software-de-gestion.md) |
| MRP II | Manufacturing resource planning | La ampliación del MRP que Oliver Wight desarrolló en 1983 | [historia](historia-del-software-de-gestion.md) |
| ERP II, ERP postmoderno, ERP componible | ERP II, postmodern ERP, composable ERP | Tres etiquetas de Gartner (2000, 2013-2014, años veinte) para lo que vendría después del ERP; la postmoderna propone armarlo con piezas de varios proveedores | [historia](historia-del-software-de-gestion.md#erp-ii-postmoderno-y-componible) |

## Categorías de producto

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| ERP | Enterprise resource planning | La categoría que junta los dominios administrativos y, en las empresas de producto, los operativos sobre una base común; no tiene definición acordada | [ERP](../Categorias-de-producto/erp.md) |
| Suite | Suite | Varios módulos de un mismo proveedor que comparten datos y se venden juntos | [categorías de producto](../Categorias-de-producto/categorias-de-producto.md) |
| Lo mejor de cada clase | Best-of-breed | Combinar productos de varios proveedores, el mejor para cada dominio, e integrarlos | [categorías de producto](../Categorias-de-producto/categorias-de-producto.md), [fundamentos](fundamentos-de-software-de-gestion.md#cuatro-posiciones-en-disputa) |
| Administrativo, operativo | Administrative ERP, operational ERP | El corte de Gartner: finanzas, personal y compras de un lado; producción y distribución del otro | [categorías de producto](../Categorias-de-producto/categorias-de-producto.md) |
| Escalón | Tier | El tamaño de empresa para el que se hace un producto, del facturador al ERP de una empresa grande | [escalones por tamaño](../Categorias-de-producto/escalones-por-tamano.md) |
| Facturador | Invoicing software | El escalón más chico: lleva el comprobante y el cliente y casi no se adapta a la empresa | [escalones por tamaño](../Categorias-de-producto/escalones-por-tamano.md), [sistemas de gestión del comercio](../../Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion/sistemas-de-gestion.md) |
| CRM | Customer relationship management | El registro del cliente y lo que pasa antes del pedido (interesado, oportunidad, actividades del vendedor); a veces suma la atención y el marketing | [CRM](../Categorias-de-producto/crm.md), [Relación con clientes](../../Relacion-con-clientes/relacion-con-clientes.md) |
| Automatización de la fuerza de ventas | Sales force automation (SFA) | La parte del CRM que lleva interesados, oportunidades y actividades de un equipo de ventas | [CRM](../Categorias-de-producto/crm.md), [historia del CRM](../../Relacion-con-clientes/Fundamentos/historia-del-crm.md) |
| HCM | Human capital management | El software que lleva el registro del personal, el tiempo trabajado y la nómina y, en las suites grandes, el talento | [HCM](../Categorias-de-producto/hcm.md), [Administración de personal y nómina](../../Administracion-de-personal-y-nomina/administracion-de-personal-y-nomina.md) |
| SCM | Supply chain management | El software de la cadena: planificación, por un lado, y ejecución (depósito y transporte), por otro | [SCM, WMS y TMS](../Categorias-de-producto/scm-wms-y-tms.md) |
| WMS | Warehouse management system | El software que controla el depósito desde que entra la mercadería hasta que sale | [SCM, WMS y TMS](../Categorias-de-producto/scm-wms-y-tms.md), [Inventario y depósitos](../../Inventario-y-depositos/inventario-y-depositos.md) |
| TMS | Transportation management system | El software del viaje de la carga: modo, transportista, ruteo y costo del flete | [SCM, WMS y TMS](../Categorias-de-producto/scm-wms-y-tms.md), [Cadena de suministro y logística](../../Cadena-de-suministro-y-logistica/cadena-de-suministro-y-logistica.md) |
| MES | Manufacturing execution system | El software de la planta: nivel 3 de ISA-95, que despacha, registra consumos y sigue lotes; el ERP queda en el nivel 4 | [MES](../Categorias-de-producto/mes.md), [marcos de la producción](../../Produccion/Fundamentos/marcos-de-la-produccion.md#isa-95-cinco-niveles-y-la-frontera-entre-erp-y-mes) |
| QMS | Quality management system | El software de calidad: no conformidades, acciones correctivas, control de documentos | [MES](../Categorias-de-producto/mes.md), [Calidad](../../Produccion/Calidad/calidad.md) |
| Mesa de ayuda | Help desk | El software de casos de atención al cliente; con el mismo nombre se vende el de soporte interno de TI | [servicio de campo y mesa de ayuda](../Categorias-de-producto/servicio-de-campo-y-mesa-de-ayuda.md), [Servicio al cliente](../../Servicio-al-cliente/servicio-al-cliente.md) |
| FSM | Field service management | El software que programa, despacha y sigue a los técnicos que van a casa del cliente | [servicio de campo y mesa de ayuda](../Categorias-de-producto/servicio-de-campo-y-mesa-de-ayuda.md), [Servicio de campo](../../Activos-y-mantenimiento/Servicio-de-campo/servicio-de-campo.md) |
| PSA | Professional services automation | El software de las firmas de servicios: proyectos, horas, asignación de personas y facturación | [PSA](../Categorias-de-producto/psa.md), [Servicios profesionales y proyectos](../../Servicios-profesionales-y-proyectos/servicios-profesionales-y-proyectos.md) |
| EAM | Enterprise asset management | El software del activo en toda su vida, de la compra a la baja | [EAM y CMMS](../Categorias-de-producto/eam-y-cmms.md), [Activos y mantenimiento](../../Activos-y-mantenimiento/activos-y-mantenimiento.md) |
| CMMS | Computerized maintenance management system | El software que se centra en ejecutar el mantenimiento con órdenes de trabajo; el EAM nació de él | [EAM y CMMS](../Categorias-de-producto/eam-y-cmms.md) |
| Software vertical, horizontal | Vertical software, horizontal software | El hecho para un rubro, con sus procesos y su norma, frente al que sirve a cualquiera | [software por rubro](../Categorias-de-producto/software-por-rubro.md) |

## Columnas técnicas

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Columna técnica | — | Nombre de la base para una pieza de diseño que comparte todo software de gestión, sea cual sea el dominio | [columnas técnicas](../Columnas-tecnicas/columnas-tecnicas.md) |
| Datos maestros | Master data | Las entidades que todos los dominios comparten (clientes, productos, proveedores), con un solo registro que vale, el registro de oro | [datos maestros y partes](../Columnas-tecnicas/datos-maestros-y-partes.md), [datos maestros](../../Datos/Gobierno-y-calidad/datos-maestros.md) |
| Parte | Party | La persona u organización registrada una sola vez, que puede cumplir varios roles (cliente, proveedor); término de Fowler | [datos maestros y partes](../Columnas-tecnicas/datos-maestros-y-partes.md), [cuenta y contacto](../../Relacion-con-clientes/Registro-del-cliente/cuenta-y-contacto.md) |
| Rol | Role | Lo que una parte es para la empresa (cliente, proveedor, empleado), sin duplicarla | [datos maestros y partes](../Columnas-tecnicas/datos-maestros-y-partes.md) |
| Documento | Document, transaction | La unidad de trabajo del negocio (pedido, factura, remito, orden de trabajo), que pasa por estados y al confirmarse deja movimientos | [documento y estados](../Columnas-tecnicas/documento-y-estados.md) |
| Borrador, confirmado, anulado | Draft, submitted, cancelled | Los tres estados básicos de un documento; del confirmado no se vuelve a borrador, se anula con otro | [documento y estados](../Columnas-tecnicas/documento-y-estados.md) |
| Numeración | Numbering series | La serie correlativa de cada tipo de documento, a veces por ejercicio o por punto de venta | [documento y estados](../Columnas-tecnicas/documento-y-estados.md) |
| Flujo de aprobación | Approval workflow | Quién tiene que aprobar un documento antes de confirmarlo, a veces según el importe | [documento y estados](../Columnas-tecnicas/documento-y-estados.md) |
| Registro de movimientos | Ledger | Cada cambio de un saldo (plata, stock, horas) como una fila que no se edita; el saldo es la suma | [registro de movimientos y dimensiones](../Columnas-tecnicas/registro-de-movimientos-y-dimensiones.md), [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md) |
| Regla de contabilización | Posting rule | La regla que convierte un documento confirmado en asientos; término de Fowler | [registro de movimientos y dimensiones](../Columnas-tecnicas/registro-de-movimientos-y-dimensiones.md) |
| Dimensión | Dimension, financial dimension | Un atributo de cada movimiento (centro de costo, proyecto, región) para analizarlo sin multiplicar cuentas | [registro de movimientos y dimensiones](../Columnas-tecnicas/registro-de-movimientos-y-dimensiones.md) |
| REA | Resources, events, agents | El modelo de McCarthy (1982) que registra los hechos económicos y deriva de ellos el asiento; según un informe técnico, los ERP no lo adoptaron | [registro de movimientos y dimensiones](../Columnas-tecnicas/registro-de-movimientos-y-dimensiones.md), [fundamentos de contabilidad](../../Contabilidad/Fundamentos/fundamentos-de-contabilidad.md#rea-registrar-los-hechos-y-no-los-asientos) |
| Fecha del hecho, fecha de registro | Actual date, record date | Cuándo pasó algo y cuándo lo supo el sistema; Fowler pide guardar las dos | [fechas, vigencias y cierre](../Columnas-tecnicas/fechas-vigencias-y-cierre.md) |
| Vigencia | Effectivity | Desde y hasta cuándo vale un dato (un precio, una alícuota, un sueldo) | [fechas, vigencias y cierre](../Columnas-tecnicas/fechas-vigencias-y-cierre.md), [cambios de ingeniería](../../Produccion/Producto-y-proceso/cambios-de-ingenieria.md#vigencia-por-fecha-por-número-de-serie-o-al-agotar) |
| Fecha de bloqueo | Lock date | La fecha antes de la cual el sistema no deja crear ni modificar movimientos, salvo excepción de un administrador | [fechas, vigencias y cierre](../Columnas-tecnicas/fechas-vigencias-y-cierre.md) |
| Multimoneda | Multi-currency | Guardar cada importe en su moneda de origen y en la de la empresa, y registrar la diferencia de cambio | [cantidades, unidades y monedas](../Columnas-tecnicas/cantidades-unidades-y-monedas.md) |
| Unidad de medida | Unit of measure (UoM) | La unidad con la que viaja cada cantidad (kilos, cajas, horas), con sus conversiones | [cantidades, unidades y monedas](../Columnas-tecnicas/cantidades-unidades-y-monedas.md) |
| Multiempresa | Multi-company | Llevar varias empresas o sucursales de un mismo cliente, que comparten algunos datos a propósito | [estructura de la organización](../Columnas-tecnicas/estructura-de-la-organizacion.md) |
| Multi-tenancy | Multi-tenancy | Servir a varios clientes desde una misma instancia con los datos aislados; es alojamiento, no columna, y no es multiempresa | [multi-tenancy](../../Arquitectura/Sistemas-distribuidos/multi-tenancy.md), [estructura de la organización](../Columnas-tecnicas/estructura-de-la-organizacion.md) |
| Permiso de rol, permiso de registro | Role permission, record rule | Qué puede hacer un rol con un tipo de documento, y sobre qué registros (su empresa, su zona) | [permisos y separación de funciones](../Columnas-tecnicas/permisos-y-separacion-de-funciones.md) |
| Separación de funciones | Segregation of duties (SoD) | Que ninguna persona autorice, registre y custodie la misma operación de punta a punta | [permisos y separación de funciones](../Columnas-tecnicas/permisos-y-separacion-de-funciones.md), [separación de funciones](../../Contabilidad/Control-interno/separacion-de-funciones.md) |
| Pista de auditoría (rastro de auditoría) | Audit trail, audit log | Quién creó, modificó o anuló cada registro, y cuándo; cubre lo que sí se edita, como maestros y configuración | [auditoría de cambios](../Columnas-tecnicas/auditoria-de-cambios.md), [controles sobre sistemas](../../Contabilidad/Control-interno/controles-sobre-sistemas.md) |
| Sistema que manda (sistema de registro, fuente de verdad) | System of record, source of truth | El sistema cuyo valor de un dato vale cuando dos sistemas lo tienen | [integración y migración](../Columnas-tecnicas/integracion-y-migracion.md), [sistemas de gestión del comercio](../../Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion/sistemas-de-gestion.md) |
| Estilo de integración | Integration style | Cómo se pasan datos dos sistemas: archivo, base compartida, llamada remota o mensajería (Hohpe y Woolf) | [integración y migración](../Columnas-tecnicas/integracion-y-migracion.md) |
| Configurar | Configure | Cambiar el comportamiento cargando datos (tipos, reglas, parámetros), sin código | [configurar o personalizar](../Columnas-tecnicas/configurar-o-personalizar.md) |
| Nivel de conocimiento | Knowledge level | Los objetos cuyas instancias gobiernan el comportamiento de los demás; el fundamento de la configuración, según Fowler | [configurar o personalizar](../Columnas-tecnicas/configurar-o-personalizar.md) |
| Extender | Extend | Agregar código por puntos previstos del producto, sin tocar su núcleo | [configurar o personalizar](../Columnas-tecnicas/configurar-o-personalizar.md) |
| Modificar | Modify, overlayer | Cambiar el código del núcleo; se paga en cada actualización | [configurar o personalizar](../Columnas-tecnicas/configurar-o-personalizar.md) |
| Personalizar | Customize, tailor | Adaptar el producto a la empresa; según la fuente, incluye configurar o se reserva para el código | [configurar o personalizar](../Columnas-tecnicas/configurar-o-personalizar.md) |
| Reporte operativo, reporte legal | Operational report, statutory report | Lo que el sistema entrega de su propia base: el listado del día y el libro que pide la norma | [reportes operativos y legales](../Columnas-tecnicas/reportes-operativos-y-legales.md) |
| Punto de extensión | User exit | Un lugar que el producto prevé para enganchar código propio sin modificar el suyo | [configurar o personalizar](../Columnas-tecnicas/configurar-o-personalizar.md) |

## Implementación

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Implementación, implantación | Implementation | Llevar un producto a una empresa: elegirlo, adaptarlo, migrar, ponerlo en marcha y sostenerlo | [implementación](../Implementacion/implementacion.md) |
| Fases de Markus y Tanis | Chartering, project, shakedown, onward and upward | El ciclo de una implantación en cuatro fases: decidir, hacer, estabilizar y mejorar | [implementación](../Implementacion/implementacion.md) |
| Factor crítico de éxito | Critical success factor (CSF) | Lo que las encuestas asocian con implantaciones que salen bien; listas inducidas, sin causalidad probada | [implementación](../Implementacion/implementacion.md) |
| Análisis de brechas | Fit-gap analysis | Comparar lo que trae el producto con lo que la empresa necesita y decidir, por cada brecha, si se adapta el proceso o el software | [análisis de brechas](../Implementacion/analisis-de-brechas.md) |
| Brecha | Gap | Algo que la empresa necesita y el producto no hace como viene | [análisis de brechas](../Implementacion/analisis-de-brechas.md) |
| Desajuste | Misfit | En Soh y otros, la distancia entre el paquete y la organización: de datos, funcional o de salida | [análisis de brechas](../Implementacion/analisis-de-brechas.md) |
| Vainilla | Vanilla | Implantar el producto sin personalizarlo | [análisis de brechas](../Implementacion/analisis-de-brechas.md), [mitos](mitos-del-software-de-gestion.md) |
| Migración de datos | Data migration | Pasar maestros, saldos y documentos abiertos del sistema viejo al nuevo, y conciliarlos | [migración de datos](../Implementacion/migracion-de-datos.md) |
| Saldos de apertura | Opening balances | Los saldos con los que arranca el sistema nuevo a la fecha de corte; tienen que cuadrar con el balance aprobado | [migración de datos](../Implementacion/migracion-de-datos.md) |
| Corte | Cutover | El paso de un sistema al otro, una ventana en la que no se usa ninguno | [puesta en marcha](../Implementacion/puesta-en-marcha.md) |
| Ensayo de corte | Mock cutover | Repetir el corte con los mismos datos, herramientas y personas antes de hacerlo de verdad | [puesta en marcha](../Implementacion/puesta-en-marcha.md) |
| Seguir o no seguir | Go/no-go | La decisión, con criterios fijados antes, de hacer o postergar el corte | [puesta en marcha](../Implementacion/puesta-en-marcha.md#el-corte) |
| Puesta en marcha | Go-live | El momento en que la empresa empieza a trabajar con el sistema nuevo | [puesta en marcha](../Implementacion/puesta-en-marcha.md) |
| De una vez, por fases, en paralelo | Big bang, phased, parallel | Las tres formas de poner en marcha: todo junto, por módulos o sedes, o con los dos sistemas a la vez | [puesta en marcha](../Implementacion/puesta-en-marcha.md) |
| Hipercuidado | Hypercare | El soporte reforzado de las primeras semanas; el término sale de la metodología de un proveedor y no tiene definición neutral | [puesta en marcha](../Implementacion/puesta-en-marcha.md) |
| Estabilización | Shakedown | La fase después del arranque en que la operación vuelve a la normalidad, a veces con una caída de desempeño | [después de la puesta en marcha](../Implementacion/despues-de-la-puesta-en-marcha.md) |
| Integrador | System integrator (SI) | La empresa que implanta el producto de otro y lo conecta con el resto | [partners de implementación](../Implementacion/partners-de-implementacion.md) |

## Mercado y economía

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| Licencia perpetua | Perpetual license | El derecho a usar una versión para siempre, pagado una vez | [licencia y suscripción](../Mercado-y-economia/licencia-y-suscripcion.md) |
| Mantenimiento | Maintenance, support | Lo que se paga cada año sobre una licencia perpetua por el soporte del proveedor; se cotiza como porcentaje de la licencia | [licencia y suscripción](../Mercado-y-economia/licencia-y-suscripcion.md) |
| Suscripción | Subscription | El pago periódico por usar el software, que se corta cuando se deja de pagar | [licencia y suscripción](../Mercado-y-economia/licencia-y-suscripcion.md), [SaaS](../../Emprender/Modelo-de-negocio/saas.md) |
| Usuario nombrado, usuario concurrente | Named user, concurrent user | Cobrar por persona habilitada o por cuántas usan el sistema a la vez | [licencia y suscripción](../Mercado-y-economia/licencia-y-suscripcion.md) |
| Partner | Partner | La empresa que revende, implanta o extiende el producto de un proveedor | [canal de partners](../Mercado-y-economia/canal-de-partners.md), [partners de implementación](../Implementacion/partners-de-implementacion.md) |
| Revendedor de valor agregado | Value-added reseller (VAR) | El partner que revende la licencia y suma servicios de implantación y soporte | [canal de partners](../Mercado-y-economia/canal-de-partners.md) |
| Tienda de extensiones | Marketplace, app store | El lugar donde terceros publican extensiones del producto, con un reparto de ingresos | [ecosistema de extensiones](../Mercado-y-economia/ecosistema-de-extensiones.md), [ecosistema de terceros](../../Producto/Plataformas/ecosistema-de-terceros.md) |
| Costo total de propiedad | Total cost of ownership (TCO) | Todo lo que paga quien compra: licencia, implantación, personalización, operación, actualización y su propio equipo | [costo total para quien compra](../Mercado-y-economia/costo-total-para-quien-compra.md), [costo total de adquisición](../../Compras-y-abastecimiento/Abastecimiento-estrategico/costo-total-de-adquisicion.md) |
| Costo de cambio | Switching cost | Lo que le cuesta a una empresa dejar un sistema por otro | [costos de cambio](../../Estrategia-competitiva/Fuentes-de-ventaja/costos-de-cambio.md) |

## Lo propio de la Argentina

| Término | Inglés | Qué es | Dónde |
|---|---|---|---|
| ARCA | — | El fisco nacional, que reemplazó a la AFIP por el Decreto 953/2024 | [impuestos en Argentina](../../Impuestos/impuestos-en-argentina.md) |
| CAE | — | Código de autorización electrónico que ARCA le da a cada comprobante en el momento, por web service; sin él el comprobante no está autorizado | [software de gestión en la Argentina](../software-de-gestion-en-argentina.md), [factura electrónica de ARCA](../../Comercio-electronico/Normativa/factura-electronica-de-arca.md) |
| CAEA | — | Código que se pide por anticipado para una quincena y se informa después; desde el 1 de junio de 2026 queda para las contingencias | [software de gestión en la Argentina](../software-de-gestion-en-argentina.md#el-caea-pasó-a-ser-la-contingencia) |
| Controlador fiscal | — | El equipo homologado con el que se emiten comprobantes como alternativa a la factura electrónica por web service; lo que se homologa es el equipo, no el software de gestión | [software de gestión en la Argentina](../software-de-gestion-en-argentina.md) |
| CUIT | — | La clave de identificación tributaria de cada contribuyente; identifica al emisor y al receptor en cada comprobante | [impuestos en Argentina](../../Impuestos/impuestos-en-argentina.md) |
| WSAA y WSFEv1 | — | Los web services de ARCA: el primero autentica al sistema con su certificado y le da un ticket de acceso; el segundo autoriza los comprobantes y devuelve el CAE | [software de gestión en la Argentina](../software-de-gestion-en-argentina.md) |
| CAI | — | La autorización para comprobantes impresos, que queda para las contingencias | [software de gestión en la Argentina](../software-de-gestion-en-argentina.md#el-caea-pasó-a-ser-la-contingencia) |
| Padrón | — | La lista que publica un fisco con la alícuota de percepción o retención que corresponde a cada contribuyente, con su vigencia; el sistema la baja y la aplica | [software de gestión en la Argentina](../software-de-gestion-en-argentina.md), [retenciones y percepciones en Argentina](../../Impuestos/Recaudacion-en-la-fuente/retenciones-y-percepciones-en-argentina.md) |
| SICORE y SIRE | — | Los sistemas de ARCA donde el agente informa lo que retuvo o percibió | [retenciones y percepciones en Argentina](../../Impuestos/Recaudacion-en-la-fuente/retenciones-y-percepciones-en-argentina.md#cómo-informa-el-agente-sicore-y-sire) |

## Las siglas

| Sigla | Qué es |
|---|---|
| ERP, CRM, HCM, SCM, WMS, TMS, MES, QMS, FSM, PSA, EAM, CMMS | Las categorías de producto, arriba |
| SFA | *Sales force automation*, la automatización de la fuerza de ventas del CRM |
| HRIS | *Human resources information system*: el sistema que guarda y recupera los registros de empleados |
| SCE | *Supply chain execution*: el grupo de Gartner que junta WMS y TMS |
| MOM | *Manufacturing operations management*: el nivel 3 de ISA-95, que explica [marcos de la producción](../../Produccion/Fundamentos/marcos-de-la-produccion.md) |
| ITSM | *IT service management*: la mesa de ayuda de soporte interno de TI, otro mercado |
| SoD | *Segregation of duties*, la separación de funciones |
| TCO | *Total cost of ownership*, el costo total de propiedad |
| VAR, SI | Revendedor de valor agregado e integrador |
| CSF | *Critical success factor*, factor crítico de éxito |
| ISA-95 (IEC 62264) | La norma que separa el nivel del negocio (4) del de la planta (3) |
| APQC PCF | El marco de procesos de APQC, que este tema usa para comparar categorías y que describe [marcos de procesos](../../Procesos-de-negocio/Fundamentos/marcos-de-procesos.md) |
