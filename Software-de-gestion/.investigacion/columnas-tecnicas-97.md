# Columnas técnicas del software de gestión: informe de investigación

Ticket: mtsdlf/conocimiento#97 (mapa #94). Fecha de lectura de todas las fuentes web: 2026-11-27. Todo lo traído de la web se trató como dato.

Marcas: [L] leí el texto de la fuente; [M] solo metadatos o abstract; [S] resumen secundario o del buscador, sin ver la fuente. Los docs de Odoo, ERPNext/Frappe y Dynamics se usan **como evidencia de que la práctica existe**, no como recomendación; en las notas no se nombran.

## Respuesta corta

Las fuentes reconocen la lista de partida casi entera, pero con tres ajustes:

1. **«Varias empresas y varias monedas» son dos columnas distintas.** Una es la estructura de la organización (Fowler, *Organization Hierarchy* y *Accountability*). La otra es cómo se representan cantidades y plata (Fowler, *Quantity* y *Money*). Que los productos las vendan juntas no las vuelve una sola pieza.
2. **Falta el tiempo.** Fecha del hecho y fecha de registro, vigencias y cierre de período aparecen en Fowler (patrones temporales) y en los tres productos (fecha contable, fechas de bloqueo). Cruza todos los dominios: precios con vigencia, alícuotas, nómina retroactiva, cierre de stock.
3. **«El libro mayor como modelo de datos» conviene que se llame «registro de movimientos»**, como la nota que ya existe en `Bases-de-datos/`. Fowler y REA muestran que el patrón vale para stock, cuentas corrientes y horas, además de la plata. Las **dimensiones analíticas** (centro de costo, región, proyecto) entran adentro de esta columna.

Además, tres cosas que parecían columnas se absorben: la **parte con roles** (persona u organización que es cliente y proveedor a la vez) va en datos maestros, la **numeración y las aprobaciones** van en el documento, y la **migración de datos** va en integración. **Multi-tenancy no es columna**: es cómo se aloja un SaaS y ya está en `Arquitectura/`; no hay que confundirla con varias empresas dentro de un mismo cliente.

## Lista propuesta (11 columnas)

| # | Columna | Definición en una línea | Quién la reconoce | ¿De todos los dominios? |
|---|---|---|---|---|
| 1 | Datos maestros | Las entidades que todos los dominios comparten (parte, producto, cuenta), con un solo registro que vale y roles en lugar de copias. | Fowler *Party*; Dynamics address book; Davenport (base única); Soh et al. (*data misfits*) | Sí |
| 2 | El documento y sus estados | La unidad de trabajo del negocio (pedido, factura, remito) con su ciclo borrador → confirmado → anulado, su numeración y quién lo aprueba. | ERPNext/Frappe docstatus; Dynamics workflow; Fowler (*Accounting Event*, *Posting Rule*) | Sí |
| 3 | Registro de movimientos y dimensiones | Cada cambio de un saldo es una fila que no se edita; se corrige con otra fila; el saldo se suma; cada fila lleva dimensiones para analizarla. | Fowler *Account*, *Accounting Entry*, ajustes; REA (McCarthy); ERPNext libro inmutable; Dynamics y ERPNext dimensiones | Sí |
| 4 | Fechas, vigencias y cierre (nueva) | Lo que pasó, cuándo se supo y desde cuándo vale; y el período que se cierra para que nadie lo toque. | Fowler, patrones temporales y *Audit Log*; Odoo fechas de bloqueo; ERPNext fecha contable | Sí |
| 5 | Cantidades, unidades y monedas (sale de partir la 8) | Un número de negocio siempre viaja con su unidad o su moneda; convertir, redondear y registrar la diferencia de cambio es parte del diseño. | Fowler *Money* y *Quantity*; Odoo multimoneda | Sí |
| 6 | Estructura de la organización: varias empresas (sale de partir la 8) | Qué empresas, sucursales o unidades lleva el sistema, qué datos comparten y cuáles son propios de cada una. | Fowler *Organization Hierarchy*, *Accountability*; Odoo multiempresa; Dynamics entidades legales | Sí, pero opcional: el software chico lleva una sola |
| 7 | Permisos y separación de funciones | Quién puede hacer qué con qué tipo de documento, sobre qué registros, y qué combinaciones de tareas no puede tener una misma persona. | Control interno (COSO, vía secundarias); Dynamics reglas de SoD; ERPNext permisos de rol y de usuario; Odoo grupos y reglas de registro; Soh et al. (*access* y *control misfits*) | Sí |
| 8 | Auditoría | El rastro de quién cambió qué y cuándo, aparte de los movimientos, para reconstruir lo que el sistema creía en cada momento. | Fowler *Audit Log*; Odoo seguimiento de campos; ERPNext *Track Changes* | Sí |
| 9 | Integración y migración | Cómo entra y sale el dato (otros sistemas, canales, la carga inicial), con un sistema que manda en cada dato. | Hohpe y Woolf (cuatro estilos); Brehm et al. (*interfaces*); Davenport | Sí |
| 10 | Configurar frente a personalizar | Cuánto del comportamiento se cambia con datos (configuración) y cuánto con código (extensión o modificación), y lo que cuesta cada uno al actualizar. | Fowler *Knowledge Level*; Brehm et al. (tipos de adaptación); Dynamics extensibilidad; Frappe *Customize Form*; Davenport | Sí |
| 11 | Reportes | Los listados operativos y legales que salen del sistema; la analítica de fondo va en Datos. | Soh et al. (*output misfits*, los más frecuentes); Brehm et al. (*extended reporting*); dimensiones (ver 3) | Sí |

## Columna por columna

### 1. Datos maestros

- **Definición.** Las entidades que todos los dominios comparten (la parte, el producto, la cuenta), con un solo registro que vale. La parte (persona u organización) tiene **roles** (cliente, proveedor, empleado) y no se duplica por rol.
- **Fuentes.**
  - Fowler, *Organization Structures* (borrador del segundo volumen de *Analysis Patterns*): «I usually define party as the supertype of person and organization». https://martinfowler.com/apsupp/accountability.pdf [L]
  - Dynamics, *Global address book overview*: «a centralized repository for master data... for all internal and external persons and organizations»; cada parte tiene uno o más roles (customer, vendor, worker...) y la dirección se cambia «in only one place». https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/overview-global-address-book [L]
  - Davenport, «Putting the Enterprise into the Enterprise System», HBR 76(4), 1998: el núcleo es una base central que alimenta todas las aplicaciones. https://maaw.info/ArticleSummaries/ArtSumDavenport98.htm [S]
  - Soh, Kien y Tay-Yap, «Cultural fits and misfits: is ERP a universal solution?», CACM 43(4), 2000: los *data misfits* (formato o relaciones del modelo de datos) son los más caros de arreglar porque tocan las tablas del núcleo. https://cacm.acm.org/research/enterprise-resource-planning-cultural-fits-and-misfits [S] (la página dio 403)
- **¿De todos los dominios?** Sí: no hay dominio sin parte ni producto.
- **Enlazar, no copiar:** `Datos/Gobierno-y-calidad/datos-maestros.md` (registro de oro, MDM) ya existe y es vigente. La columna del software solo agrega lo que es del diseño: la parte con roles y qué es maestro frente a qué es transacción.

### 2. El documento y sus estados

- **Definición.** El pedido, la factura o el remito son la unidad de trabajo: se arman en borrador, se confirman (y desde ahí producen movimientos), y se anulan con otro documento en lugar de borrarse. Lleva numeración propia y, a veces, una cadena de aprobaciones.
- **Fuentes.**
  - Frappe, *DocStatus*: tres estados (borrador 0, confirmado 1, anulado 2); de confirmado o anulado no se vuelve a borrador; para corregir se anula y se hace una enmienda, un borrador nuevo que apunta al anulado (`amended_from`). https://docs.frappe.io/framework/doctypes/docstatus [S] y https://docs.frappe.io/erpnext/user/manual/en/edit-submitted-document [S]
  - ERPNext, *Naming Series*: «Masters and transactions can be given prefixes in the form of naming series»; es común una serie por ejercicio o por local. https://docs.frappe.io/erpnext/user/manual/en/naming-series [L]
  - Dynamics, *Workflow system overview*: el workflow «defines how a document flows... who must complete a task, make a decision, or approve a document», con umbrales por importe. https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/overview-workflow-system [L]
  - Fowler: el asiento nace de un evento del dominio a través de reglas de contabilización («When a Domain Event is processed, it can produce a set of Accounting Transactions»). https://martinfowler.com/eaaDev/AccountingNarrative.html [L]. *Accounting Entry*: los asientos pueden ser «mutable until they are booked». https://martinfowler.com/eaaDev/AccountingEntry.html [L]
- **¿De todos los dominios?** Sí: compras, ventas, stock, producción y nómina trabajan con documentos que pasan por estados.
- **Lo que se absorbe:** la numeración correlativa (que muchas leyes exigen; no verifiqué el texto legal) y las aprobaciones no son columnas aparte: son atributos del documento.
- **Enlazar:** `Arquitectura/Sistemas-distribuidos/saga.md` cuando un documento confirmado dispara pasos en otros sistemas.

### 3. Registro de movimientos y dimensiones

- **Definición.** Cada cambio de un saldo (plata, stock, horas) es una fila que no se edita; el saldo es la suma; los errores se corrigen con filas nuevas (reversa o diferencia). Cada fila lleva dimensiones (centro de costo, proyecto, región) para analizarla sin multiplicar cuentas.
- **Fuentes.**
  - Fowler, *Accounting Narrative*: «The value, or balance, of the Account is derived as the sum of all the Accounting Entrys»; tres maneras de corregir (reemplazo, reversa, diferencia), y las dos últimas conservan la historia. Una cuenta es en el fondo un descriptor para clasificar movimientos, y se pueden usar otros objetos como descriptores. https://martinfowler.com/eaaDev/AccountingNarrative.html [L]
  - Fowler, *Analysis Patterns* (1997), cap. 6 «Inventory and Accounting»: *Account*, *Transactions*, *Summary Account*, *Memo Account*, *Posting Rules*. El inventario y la contabilidad comparten el mismo patrón. Índice en https://www.oreilly.com/library/view/analysis-patterns-reusable/9780134271453/ [M] (la página dio 403; el índice salió del buscador). El borrador de los capítulos de contabilidad (https://martinfowler.com/apsupp/accounting.pdf) no se pudo leer: el PDF tiene las fuentes ofuscadas; solo se leyó el índice (*Posting Rule*, *Reversal Adjustment*, *Difference Adjustment*, *Replacement Adjustment*, *Accounting Transaction*) [M].
  - McCarthy, «The REA Accounting Model: A Generalized Framework for Accounting Systems in a Shared Data Environment», *The Accounting Review* 57(3):554-578, 1982. Recursos, eventos y agentes, con la **dualidad** (cada intercambio es un evento que entrega y otro que recibe). [M]. Según Wikipedia, en REA «double-entry bookkeeping disappears»: cuentas por cobrar y por pagar se derivan de los eventos y no se guardan; influyó en ISO 15944-4. https://en.wikipedia.org/wiki/Resources,_Events,_Agents [S]
  - ERPNext, *Immutable Ledger*: «Corrections are made through traceable follow-up documents instead of silently rewriting history»; al anular se agregan filas opuestas. https://docs.frappe.io/erpnext/user/manual/en/immutable-ledger-in-erpnext [L]
  - Dimensiones: Dynamics, «Financial dimension values become segments within the ledger account». https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-dimensions [L]. ERPNext, las dimensiones agregan «business context to the same accounting entry». https://docs.frappe.io/erpnext/user/manual/en/accounting-dimensions [L]
- **¿De todos los dominios?** Sí. Es la columna más reconocida de todas: Fowler la nombra igual para inventario y contabilidad, y REA la generaliza a cualquier intercambio.
- **Posición contraria que conviene recoger:** REA dice que el libro mayor es una **vista** derivada de los eventos económicos, no el modelo. La nota debería presentar las dos lecturas: libro de movimientos (Fowler, la práctica de los productos) y eventos económicos con dualidad (REA).
- **Enlazar, no copiar:** `Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md` ya explica el patrón de fila que no se edita y saldo calculado (con Fowler, *Event Sourcing* y el libro de stock de ERPNext). La columna del software tiene que enlazarla y agregar solo lo propio: reglas de contabilización (del documento al asiento), partida doble frente a REA y dimensiones. También `Datos/Modelado-y-almacenamiento/tabla-de-eventos.md`, `Arquitectura/Sistemas-distribuidos/cqrs.md` y `Arquitectura/Estilos/event-driven.md`. La contabilidad en sí (qué es un asiento, el plan de cuentas) va en el dominio Contabilidad, no acá.

### 4. Fechas, vigencias y cierre de período (nueva)

- **Definición.** Todo hecho del negocio tiene dos fechas, la de cuándo pasó y la de cuándo se registró, y muchos datos valen desde y hasta una fecha (precio, alícuota, sueldo). El cierre de período congela lo anterior para que los saldos informados no cambien.
- **Fuentes.**
  - Fowler, *Temporal Patterns*: «we really need to provide two dates: a record date and an actual date»; la vigencia (*Effectivity*) marca el período en que algo vale; el ejemplo es un aumento de sueldo retroactivo y la pregunta del fisco sobre lo que se creía en tal fecha. https://martinfowler.com/eaaDev/timeNarrative.html [L]
  - Odoo, *Year-end closing*: con la fecha de bloqueo general, los asientos con fecha anterior «cannot be created or modified during the audit», con excepciones que solo da un administrador. https://raw.githubusercontent.com/odoo/documentation/19.0/content/applications/finance/accounting/reporting/year_end.rst [L]
  - ERPNext, *Immutable Ledger*: no correr la fecha de contabilización para saltar controles; un movimiento de stock con fecha pasada revaloriza lo posterior. https://docs.frappe.io/erpnext/user/manual/en/immutable-ledger-in-erpnext [L]
- **¿De todos los dominios?** Sí: precios y listas (ventas, compras), alícuotas (impuestos), nómina retroactiva, valorización de stock, cierre contable.
- **Por qué no queda dentro de la 3:** las vigencias valen también para datos maestros y configuración, que no son movimientos. Si al escribir queda flaca, se puede unir con la auditoría (Fowler trata el *Audit Log* como la dimensión «tiempo de registro»).

### 5. Cantidades, unidades y monedas (sale de partir la 8)

- **Definición.** Un número de negocio viaja con su unidad (kilos, cajas, horas) o su moneda. Convertir unidades, redondear sin perder centavos, guardar la moneda de origen junto a la de la empresa y registrar la diferencia de cambio son decisiones de diseño, no de un dominio.
- **Fuentes.**
  - Fowler, *Money* (PoEAA): «Represents a monetary value»; evita sumar dólares con yenes y encapsula el redondeo, porque «it's easy to lose pennies». https://martinfowler.com/eaaCatalog/money.html [L]
  - Fowler, *Analysis Patterns* cap. 3 (*Quantity*, *Conversion Ratio*, *Compound Units*). Índice vía O'Reilly [M].
  - Odoo, *Multi-currency system*: moneda principal de la empresa; diferencias de cambio registradas automáticamente en cuentas y diario propios. https://raw.githubusercontent.com/odoo/documentation/19.0/content/applications/finance/accounting/get_started/multi_currency.rst [L]
- **¿De todos los dominios?** Sí: la unidad de medida pesa en stock, compras, producción y ventas; la moneda, en ventas, compras, tesorería y contabilidad.

### 6. Estructura de la organización: varias empresas (sale de partir la 8)

- **Definición.** Qué empresas, sucursales, depósitos o unidades lleva el sistema, cómo se ordenan, qué datos comparten (maestros, plan de cuentas) y cuáles son de cada una (numeración, impuestos, permisos).
- **Fuentes.**
  - Fowler, *Organization Hierarchy* («Represents the hierarchy of organizational units within a business») y *Accountability*, para cuando hay más de una jerarquía (legal, de gestión, regional). https://martinfowler.com/apsupp/accountability.pdf [L]
  - Odoo, *Multi-company Guidelines*: campos que dependen de la empresa (un mismo registro con valores distintos según la empresa), chequeo de coherencia (no mezclar productos de la empresa B en un pedido de la A) y reglas de seguridad por empresa. https://raw.githubusercontent.com/odoo/documentation/19.0/content/developer/howtos/company.rst [L]
  - Dynamics, dimensiones compartidas entre entidades legales con excepciones por entidad, y la advertencia de que una dimensión no reemplaza a una entidad legal (impuestos, stock). https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-dimensions [L]
- **¿De todos los dominios?** Sí cuando existe, pero es opcional: el software para un comercio chico lleva una sola empresa. Conviene que la nota lo diga.
- **No confundir con multi-tenancy:** varias empresas de un mismo cliente comparten datos a propósito; varios clientes (tenants) de un SaaS no comparten nada. Enlazar `Arquitectura/Sistemas-distribuidos/multi-tenancy.md` para esa diferencia, sin copiarla.

### 7. Permisos y separación de funciones

- **Definición.** Tres capas: qué puede hacer un rol con cada tipo de documento; sobre qué registros (su empresa, su zona); y qué combinaciones de tareas no puede tener una misma persona (autorizar, registrar y custodiar).
- **Fuentes.**
  - Control interno: COSO pide separar las tareas incompatibles y, donde no se pueda, controles alternativos; la división clásica es autorizar, registrar y custodiar (más conciliar). https://aaahq.org/node/35020 y https://www.mcgill.ca/internalaudit/node/647 [S]. No leí el texto de COSO 2013.
  - Dynamics, reglas de separación de funciones que se aplican al asignar roles, con conflictos que se resuelven con una razón registrada. https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/sysadmin/identify-resolve-conflicts-segregation-duties [S]
  - ERPNext, *User Permissions*: los permisos de rol dan acceso al tipo de documento entero; los de usuario lo restringen «based on the link fields in the document» (empresa, territorio). https://docs.frappe.io/erpnext/user/manual/en/user-permissions [L]
  - Odoo, *Restrict access to data*: grupos, derechos de acceso por modelo y reglas de registro, más seguridad multiempresa. https://raw.githubusercontent.com/odoo/documentation/19.0/content/developer/tutorials/restrict_data_access.rst [L]
  - Soh et al.: entre los desajustes funcionales están los de acceso y los de control (validaciones que faltan). [S]
- **¿De todos los dominios?** Sí.
- **Enlazar:** `DevOps/Repositorios/trazabilidad-de-cambios.md` (separación de funciones en el despliegue, que es otra cosa: quién cambia el software, no quién opera el negocio) y `Cloud/Gobernanza-e-identidad/identidad-y-acceso-en-azure.md` (RBAC de la nube, también otra capa). No hay nota de RBAC de aplicación en la base: esta columna sería la primera.

### 8. Auditoría

- **Definición.** El rastro de quién cambió qué dato y cuándo, sobre todo en maestros y configuración, que no dejan movimientos. Sirve para reconstruir lo que el sistema creía en una fecha.
- **Fuentes.**
  - Fowler, *Audit Log*: «A simple log of changes, intended to be easily written and non-intrusive»; guardar la fecha real y la de registro; fácil de escribir, difícil de consultar. https://martinfowler.com/eaaDev/AuditLog.html [L]
  - Odoo, seguimiento de campos (`tracking=True`) que deja cada cambio en el historial del registro. https://raw.githubusercontent.com/odoo/documentation/19.0/content/developer/reference/backend/mixins.rst [L]
  - Frappe, *Customize Form* ofrece *Track Changes* por tipo de documento. https://docs.frappe.io/erpnext/user/manual/en/customize-form [L]. La página de *Audit Trail* de ERPNext no cargó (404).
- **¿De todos los dominios?** Sí.
- **Frontera con la 3:** los movimientos ya son su propio rastro (no se editan); la auditoría cubre lo que sí se edita. Enlazar `DevOps/Repositorios/trazabilidad-de-cambios.md` y `Datos/Gobierno-y-calidad/metadatos-y-linaje.md`.

### 9. Integración y migración

- **Definición.** Cómo entra y sale el dato: hacia otros sistemas y canales, y la carga inicial desde el sistema viejo. La decisión de fondo es qué sistema manda en cada dato.
- **Fuentes.**
  - Hohpe y Woolf, *Enterprise Integration Patterns*: cuatro estilos, transferencia de archivos, base compartida, invocación remota y mensajería. https://www.enterpriseintegrationpatterns.com/patterns/messaging/IntegrationStylesIntro.html [L]
  - Brehm, Heinzl y Markus, «Tailoring ERP systems: a spectrum of choices and their implications», HICSS 2001: el desarrollo de interfaces es uno de los tipos de adaptación. [S]
  - Davenport 1998: el sistema integrado reemplaza aplicaciones que no se hablaban. [S]
- **¿De todos los dominios?** Sí.
- **Enlazar, no copiar (es la columna con más material ya escrito):** `Arquitectura/Sistemas-distribuidos/outbox.md`, `clave-de-idempotencia.md`, `saga.md`, `api-led-connectivity.md`, `circuit-breaker.md`; `Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion-en-el-comercio/integracion-con-tiendas-y-marketplaces.md` (el caso de canales, con «un sistema que manda en cada dato»); `Datos/Ingesta-y-transformacion/etl-y-elt.md`. La nota de la columna debería ser corta: qué es propio del software de gestión (sistema que manda, maestros compartidos, carga inicial) y enlaces.
- **Frontera:** la migración como actividad de proyecto va en la vertical Implementación del mismo tema; acá va solo el mecanismo (importar maestros y saldos iniciales).

### 10. Configurar frente a personalizar

- **Definición.** Cuánto del comportamiento se cambia cargando datos (tipos, reglas, parámetros) y cuánto con código; y, dentro del código, extender por puntos previstos o modificar el núcleo, que se paga en cada actualización.
- **Fuentes.**
  - Fowler, *Knowledge Level*: objetos cuyas instancias gobiernan el comportamiento de los operativos, lo que permite cambiar el sistema «without programming»; «This choosing and wiring together of objects is how the system is configured». https://martinfowler.com/apsupp/accountability.pdf [L]. Es el fundamento de diseño de la configuración.
  - Brehm, Heinzl y Markus 2001: tipología de adaptación de un ERP de menos a más invasiva (configuración, reportes extendidos, workflow, interfaces, hasta modificar código). Las listas secundarias difieren en el número de tipos; no leí el texto. DOI 10.1109/HICSS.2001.927130 [S]
  - Dynamics, *Extensibility*: la modificación por capas (*overlayering*) se reemplazó por extensiones porque las actualizaciones frecuentes exigen «a less intrusive customization model»; «Overlayering isn't supported». https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/extensibility/extensibility-home-page [L]
  - Frappe, *Customize Form*: campos y propiedades nuevos desde la interfaz, sin tocar el tipo de documento base, con «Reset All Customizations». https://docs.frappe.io/erpnext/user/manual/en/customize-form [L]
  - Davenport 1998: el sistema impone su lógica y muchas veces la empresa cambia sus procesos en lugar del software. [S]
- **¿De todos los dominios?** Sí.
- **Frontera con Implementación:** el mecanismo (nivel de conocimiento, puntos de extensión) va acá; la decisión en un proyecto (adaptar el proceso o el software, el costo de la brecha) va en la vertical Implementación. Conviene enlazarlas en los dos sentidos.

### 11. Reportes

- **Definición.** Los listados operativos (qué hay que despachar, quién debe) y legales (libros, declaraciones) que el sistema tiene que sacar de sus propios datos. La analítica (tableros, almacén de datos) va en Datos.
- **Fuentes.**
  - Soh et al. 2000: los *output misfits* (formato y contenido de las salidas) son, según los resúmenes, «by far, the most prevalent form of misfit». [S]
  - Brehm et al. 2001: el reporte extendido es un tipo de adaptación propio. [S]
  - Dimensiones (ver columna 3): los productos las justifican por el informe, por ejemplo un estado de resultados por dimensión (Dynamics) [L].
- **¿De todos los dominios?** Sí, pero es la más delgada en fuentes primarias. Si al escribir no da para una nota propia, se puede mover a la vertical de inteligencia de negocio que el mapa prevé en Datos y dejar acá solo un enlace.
- **Enlazar:** `Datos/Modelado-y-almacenamiento/oltp-y-olap.md` (por qué el reporte pesado no corre sobre la base operativa), `Datos/Visualizacion-y-BI/capa-semantica.md`, `Datos/Modelado-y-almacenamiento/modelado-dimensional.md`.

## Lo que no es columna

- **Multi-tenancy.** Es alojamiento SaaS, no diseño del negocio; está en `Arquitectura/Sistemas-distribuidos/multi-tenancy.md`. La columna 6 la enlaza para marcar la diferencia.
- **Saga, idempotencia, circuit breaker, api-led, outbox.** Son patrones de sistemas distribuidos que la columna 9 usa; se enlazan.
- **La parte con roles, la numeración, las aprobaciones, las dimensiones, la migración.** Atributos de otras columnas (1, 2, 3 y 9), no piezas propias.
- **Transacciones de base de datos.** Están en `Bases-de-datos/Transacciones/`; la columna 2 las enlaza si hace falta explicar por qué confirmar un documento y escribir sus movimientos va junto.

## Huecos y cosas sin verificar

- No pude leer el texto de *Analysis Patterns* (1997) ni el borrador de contabilidad (PDF ofuscado). El capítulo de *Accountability* sí. Lo de inventario y contabilidad se apoya en el índice y en las páginas de Fowler en `eaaDev`.
- REA: solo abstract y Wikipedia. Si la nota de la columna 3 va a dar la posición REA, vale leer McCarthy 1982 o Hruby, *Model-Driven Design Using Business Patterns* (2006), que no busqué.
- Brehm et al. 2001 y Soh et al. 2000: solo por resúmenes; las categorías exactas difieren entre ellos.
- Separación de funciones: no leí COSO 2013; las citas son secundarias.
- Numeración correlativa obligatoria de facturas: lo doy por sabido pero no verifiqué el texto legal (por ejemplo, la directiva de IVA de la UE, art. 226). Lo de Argentina va en notas aparte, como dice el mapa.
