---
resumen: >-
  El alta de proveedor es el paso en que un proveedor nuevo entra al registro: se cargan sus datos, se verifica que existe y es quien dice ser y, si lo que se le va a comprar lo justifica, se lo homologa antes de la primera compra. El mismo registro guarda el bloqueo, que impide comprarle, recibirle facturas o pagarle.
estado: borrador
estabilidad: semi
fuentes:
  - "APQC, Process Classification Framework 7.4 (2024), 4.2.2.2 «Certify and validate suppliers» y 4.2.4.1 «Monitor/Manage supplier information»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Washington State Auditor's Office, Protect your vendor master file from fraudsters (leído por extracto): https://sao.wa.gov/the-audit-connection-blog/protect-your-vendor-master-file-fraudsters"
  - "Deloitte, Case 22-7c «EGF Apparel» (2025), caso didáctico de auditoría con empresa y fechas ficticias, leído completo: https://www.deloitte.com/content/dam/assets-zone3/us/en/docs/about/2025/us-dfdtn-22-7c-egf-apparel.pdf"
  - "Corpay, Vendor verification: banking validation (según su resumen; fuente comercial con interés): https://www.corpay.com/en-NZ/resources/blog/vendor-verification-banking-validation"
  - "Queensland Government, Procurement guide: prequalifying suppliers (según su resumen): https://www.forgov.qld.gov.au/__data/assets/pdf_file/0025/187504/procurement-guide-prequalifying.pdf"
  - "New Zealand Government Procurement Rules, Pre-qualified suppliers list (según su resumen): https://www.procurement.govt.nz/procurement/principles-and-rules/government-procurement-rules/types-of-supplier-lists/pre-qualified-suppliers-list/"
  - "USPS, Supplying Principles and Practices, calificación previa (según su resumen): https://about.usps.com/manuals/spp012011/html/spp2_176.htm"
  - "ERPNext, Supplier y Supplier Scorecard (como evidencia de práctica; Supplier según su resumen): https://docs.frappe.io/erpnext/supplier ; https://docs.frappe.io/erpnext/user/manual/en/buying/supplier-scorecard"
  - "Compras-y-abastecimiento/.investigacion/proveedores.md (2026-11-27), secciones 1, 2 y 4"
  - "Compras-y-abastecimiento/.investigacion/orden-y-seguimiento.md (2026-11-27), fuente 6.5"
aliases: [alta de proveedores, alta de proveedor nuevo, vendor onboarding, supplier onboarding, homologación, homologación de proveedores, calificación de proveedores, supplier qualification, precalificación, prequalification, lista de proveedores aprobados, approved vendor list, AVL, proveedor bloqueado, bloqueo de proveedor, supplier block]
creado: 2026-11-27
revisado:
---

# Alta de proveedor

El alta de proveedor es el paso en que un proveedor nuevo entra al registro: se cargan sus datos, se verifica que existe y es quien dice ser y, si lo que se le va a comprar lo justifica, se lo homologa antes de la primera compra. El mismo registro guarda el bloqueo, que impide comprarle, recibirle facturas o pagarle.

Es la puerta de entrada de [Proveedores](proveedores.md). APQC 7.4 pone la homologación en 4.2.2.2 «Certify and validate suppliers», dentro de seleccionar proveedores y mantener contratos, y el mantenimiento posterior de los datos en 4.2.4.1 «Monitor/Manage supplier information». Por lo general, antes del alta [Abastecimiento estratégico](../Abastecimiento-estrategico/abastecimiento-estrategico.md) ya eligió a quién comprarle, por ejemplo con una [cotización](../Abastecimiento-estrategico/cotizacion-y-licitacion.md); después, la primera [orden de compra](../Orden-de-compra/orden-de-compra.md) puede salir. La homologación puede ir antes de elegir, como precalificación, o después de elegir y antes de la primera orden.

## Los datos que se cargan

Como lectura de esta base sobre la ficha del proveedor, el alta carga tres grupos de datos. Quién es: razón social, identificación fiscal, direcciones y contactos. Cómo se le paga: la cuenta bancaria y la condición de pago. Cómo se le compra: el grupo al que pertenece y sus [condiciones](condiciones-del-proveedor.md) por artículo. La forma del registro, con la regla de que lo del proveedor gana sobre lo de su grupo, está en [proveedores](proveedores.md#qué-guarda-el-registro-del-proveedor).

Lo que pide la Argentina (la constancia de inscripción, la condición frente al IVA, la consulta de la base de facturas apócrifas) está en [Compras y abastecimiento en la Argentina](../compras-y-abastecimiento-en-argentina.md).

## Verificar antes de cargar

El auditor del estado de Washington lo pone como regla: «You need a process to vet new vendors before you add them to your vendor master file». El proceso que propone pide los formularios fiscales del proveedor, verifica su número tributario y su habilitación, y busca información sobre él en fuentes externas. Pide también que la persona que registra facturas no pueda dar de alta proveedores: «accounts payable clerks should not be able to add new vendors or change vendor information». Esa regla es de [separación de funciones](../../Contabilidad/Control-interno/separacion-de-funciones.md); quién aprueba un alta está en la matriz de [autorizaciones](../../Contabilidad/Control-interno/autorizaciones.md).

Verificar sirve contra el proveedor inventado, el primero de los dos fraudes clásicos. Sus cifras están en [autorizaciones](../../Contabilidad/Control-interno/autorizaciones.md#la-aprobación-de-pagos-y-el-alta-de-proveedores) y no se repiten acá.

## El cambio de cuenta bancaria vuelve a pasar por el alta

Cambiar la cuenta bancaria de un proveedor que ya existe es el segundo fraude clásico, y se controla como un alta nueva. El auditor de Washington pide confirmar el cambio «directly with your vendor… by phone, using contact information that is known, reliable and already on file», es decir, con el teléfono que ya estaba cargado y no con el que trae el pedido de cambio.

La llamada no alcanza si alguien no la hace. En un caso didáctico de una consultora (la empresa y las fechas son ficticias), la política exigía llamar al proveedor con el teléfono de una factura ya pagada, y aun así se transfirieron unos 3 millones de dólares a una cuenta equivocada después de un pedido de cambio por correo. El pedido venía de un dominio casi igual al del proveedor, con un guion de más, y el fraude apareció recién cuando el proveedor preguntó por sus facturas impagas. El caso señala como falla el control de revisión, que no dice qué mirar. Una empresa que vende validación bancaria propone verificar la titularidad de la cuenta en vez de depender de una llamada; tiene interés comercial, así que vale como dato de que la práctica existe. Las dos fuentes sobre el fraude son de Estados Unidos.

## Homologación: probar que el proveedor puede antes de comprarle

La homologación verifica que el proveedor puede cumplir antes de la primera compra, y no hace falta para todo. La guía de Queensland, según su resumen, la recomienda para bienes o servicios que se compran con regularidad y que son complejos, costosos o riesgosos, y dice que sirve para detectar pronto a proveedores con poca solidez financiera. Cuánto homologar a cada uno depende de su lugar en la [matriz de Kraljic](../Abastecimiento-estrategico/matriz-de-kraljic.md) (criterio de la base).

El manual de compras del correo de Estados Unidos, según su resumen, describe los pasos: un relevamiento previo, la revisión de los registros financieros y una visita a la planta para evaluar instalaciones, personal, subcontratistas y otros recursos. La guía de Nueva Zelanda agrega dos reglas para quien mantiene una lista de proveedores precalificados: publicar las condiciones para entrar y cómo se verifican, y explicar por qué se saca a un proveedor. Las tres son guías del Estado, tomadas acá como práctica y no como régimen legal.

En esta base, el resultado de la homologación es la lista de proveedores aprobados: los que se pueden usar para una [categoría de compra](../Abastecimiento-estrategico/analisis-del-gasto.md). Lo que pide ISO 9001:2015 en su cláusula 8.4 sobre evaluar y reevaluar a los proveedores externos está en [evaluación de proveedores](evaluacion-de-proveedores.md).

> [!NOTE] Sin fuente todavía: una definición de la lista de proveedores aprobados en empresas privadas (las fuentes leídas son guías del Estado), y cómo se piden y se evalúan muestras durante la homologación.

## El bloqueo de un proveedor

El bloqueo es una marca en el registro del proveedor que impide operar con él sin borrarlo. El proveedor sigue existiendo con su historia, sus órdenes viejas y su saldo, pero no se le puede comprar, recibir facturas o pagar, según lo que se bloquee. Sin sistema, es una marca en la carpeta.

| Qué se bloquea | Qué impide | De dónde sale en la práctica |
|---|---|---|
| Comprar | Nuevos pedidos de cotización y órdenes de compra | Un puntaje de [evaluación](evaluacion-de-proveedores.md) por debajo del umbral |
| Facturar | Registrar facturas del proveedor | Una decisión manual, a veces hasta una fecha |
| Pagar | Emitir pagos al proveedor | Una decisión manual, por ejemplo mientras se verifica un cambio de cuenta |

La documentación de un sistema abierto muestra las dos formas, como evidencia de práctica. En la ficha del proveedor se pueden bloquear facturas, pagos o ambos, hasta una fecha (según su resumen). En su tablero de evaluación, un estado puede solo advertir, y el comprador sigue, o bloquear nuevos pedidos de cotización y órdenes; según un resumen, ese mismo manual pide dejar una excepción para emergencias o para el [proveedor único](relacion-con-proveedores.md#proveedor-único-o-varios-proveedor-por-proveedor).

Como criterio de la base, el bloqueo de pagos es el que corresponde mientras se verifica un cambio de datos bancarios, y el de compras, el que corresponde a un proveedor que no cumple. Como lectura de esta base, inactivar no es bloquear: el auditor de Washington pide inactivar a los proveedores que no se usan, una vez al año, para que no queden registros vivos que nadie mira.
