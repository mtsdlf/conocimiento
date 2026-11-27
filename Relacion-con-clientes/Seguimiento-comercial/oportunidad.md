---
resumen: >-
  La oportunidad es el registro de una venta posible a un cliente o a un interesado calificado: qué podría comprar, por cuánto, en qué etapa está, con qué probabilidad y para cuándo se espera cerrar. Termina ganada o perdida, y si se pierde, guarda por qué y contra quién.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft Learn, tabla Opportunity: https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/opportunity (como evidencia de práctica)"
  - "ERPNext, Opportunity: https://docs.frappe.io/erpnext/user/manual/en/opportunity (como evidencia de práctica)"
  - "Odoo 19.0, «Lost opportunities»: https://www.odoo.com/documentation/19.0/applications/sales/crm/pipeline/lost_opportunities.html (como evidencia de práctica)"
  - "APQC, Process Classification Framework, 3.5.1 y 3.5.3, copia de un tercero sin versión declarada: https://capechamber.co.za/enterprise/improve-your-business-processes/3-market-and-sell-products-and-services"
  - "Relacion-con-clientes/.investigacion/registro-y-seguimiento.md, componente 5"
aliases: [opportunity, oportunidad de venta, negocio, deal, trato, etapa de venta, sales stage, probabilidad de cierre, motivo de pérdida, lost reason, fecha estimada de cierre]
creado: 2026-11-27
revisado:
---

# Oportunidad

La oportunidad es el registro de una venta posible a un cliente o a un interesado calificado: qué podría comprar, por cuánto, en qué etapa está, con qué probabilidad y para cuándo se espera cerrar. Termina ganada o perdida, y si se pierde, guarda por qué y contra quién.

Es el centro del [seguimiento comercial](seguimiento-comercial.md). Nace cuando un [interesado](interesado.md) se califica o cuando un cliente existente pide algo nuevo, se concreta en uno o varios [presupuestos](../Presupuesto/presupuesto.md) y acumula [actividades](actividad.md). Un CRM de un proveedor grande la define como un posible evento de ingreso que hay que seguir por un proceso de venta hasta terminarlo; un sistema abierto, como un interesado calificado. Un cliente o un interesado puede tener varias oportunidades abiertas a la vez.

## Qué datos lleva

| Dato | Para qué sirve |
|---|---|
| Cuenta o interesado | A quién se le vendería |
| Monto estimado y moneda | Cuánto ingreso podría traer, para la previsión |
| Etapa | Cuánto avanzó la venta, con valores que define la empresa |
| Probabilidad | De 0 a 100, qué tan probable es cerrarla |
| Fecha estimada de cierre | Cuándo se espera ganarla o perderla, para la previsión |
| Próximo contacto | Cuándo y quién vuelve a hablar con el cliente |
| Productos, si se cargan | El detalle de lo que se vendería, con cantidades y precios de una lista |
| Origen | De dónde vino, heredado del interesado |
| Competidores | Contra quién se compite |
| Estado y motivo | Abierta, ganada o perdida, y por qué |

Los productos son opcionales: un sistema abierto los activa con una casilla, y un CRM grande calcula el monto como la suma de los productos cargados según la lista de precios. Para muchas ventas alcanza con un monto estimado; el detalle de renglones aparece en el presupuesto.

## Etapa y estado son dos ejes

La etapa dice cuánto avanzó la conversación; el estado, si la venta sigue viva. Un CRM grande trae de fábrica cuatro etapas (calificar, desarrollar, proponer, cerrar) y, aparte, tres estados: abierta (en curso o en espera), ganada y perdida (cancelada o perdida contra otro). Las ganadas y perdidas quedan de solo lectura hasta que alguien las reactiva.

Mezclar los dos ejes en un solo campo es un error común: si «perdida» es una etapa más, no se sabe en qué etapa se perdió. Con dos campos se puede contar cuántas oportunidades se pierden en cada etapa. Qué etapas conviene usar y qué criterio de entrada tiene cada una no es de acá: está en [medición comercial](../../Ventas/Medicion-comercial/medicion-comercial.md), que además advierte que no hay una definición canónica de las etapas. Para este tema la etapa es un campo con una lista configurable.

> [!NOTE] Sin fuente todavía: el historial de cambios de etapa (cuándo entró la oportunidad a cada etapa). Sin ese historial no se puede medir cuánto tarda cada etapa; las fuentes leídas no lo describen.

## La probabilidad: de la etapa o de la persona

En los sistemas leídos la probabilidad es un campo que el vendedor edita. La alternativa es que cada etapa traiga una probabilidad por defecto, una práctica que las fuentes leídas no documentan. Ninguna fuente dice cuál conviene. Como criterio de la base: la del vendedor depende de su optimismo, y la de la etapa ignora lo que el vendedor sabe del cliente. La previsión de ventas que se arma con estos números, y cuánto falla, está en [medición comercial](../../Ventas/Medicion-comercial/medicion-comercial.md).

## Ganar y perder

Una oportunidad ganada se convierte en pedido a través de su presupuesto aceptado: en un CRM grande, una oportunidad tiene varios presupuestos y ganar uno la gana; en un sistema abierto, el presupuesto se crea desde la oportunidad y copia sus datos. APQC separa igual las dos cosas: gestionar oportunidades (3.5.1) y armar propuestas y presupuestos (3.5.3) son procesos hermanos. La oportunidad es la intención y la previsión; el presupuesto es el documento con renglones, precio y vigencia (ver [presupuesto](../Presupuesto/presupuesto.md)).

Una oportunidad perdida guarda el motivo. Un sistema abierto lo pide como opcional, con una lista que configura la empresa, y explica que sirve para ver problemas que se repiten y para entrenar al equipo. Otro pide al perder los motivos, los competidores y una explicación. Un CRM grande solo marca si hay información de competidores y los guarda en un objeto aparte.

Ese registro es la materia prima del [análisis de ventas ganadas y perdidas](../../Estrategia-competitiva/Analisis-de-competidores/analisis-de-ventas-ganadas-y-perdidas.md): el motivo cargado por el vendedor dice qué cree él; el análisis pregunta al cliente. Una lista de motivos corta y cerrada se puede contar; un texto libre, no.

## Cómo falla

Falla cuando el monto y la fecha de cierre no se actualizan: el embudo muestra oportunidades viejas que nadie va a cerrar y la previsión se infla. Falla también cuando se crean oportunidades para todo, incluso consultas sin calificar, lo que le quita sentido a la [calificación](../../Ventas/Descubrimiento-y-calificacion/calificacion.md). Por qué los vendedores no actualizan se discute en [actividad](actividad.md).
