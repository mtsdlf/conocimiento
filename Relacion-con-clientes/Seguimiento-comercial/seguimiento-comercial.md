---
resumen: >-
  El seguimiento comercial es el registro de las ventas posibles antes de que haya un pedido: quién se interesó, qué venta podría salir con cada uno, por cuánto, en qué etapa está y qué se habló. Lo forman tres objetos: el interesado, la oportunidad y la actividad.
estado: vigente
estabilidad: estable
fuentes:
  - "APQC, Process Classification Framework, 3.5.1 «Manage leads/opportunities», copia de un tercero sin versión declarada: https://capechamber.co.za/enterprise/improve-your-business-processes/3-market-and-sell-products-and-services"
  - "Microsoft Learn, tablas Lead, Opportunity y Activity: https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/lead (como evidencia de práctica)"
  - "ERPNext, Lead y Opportunity: https://docs.frappe.io/erpnext/user/manual/en/opportunity (como evidencia de práctica)"
  - "SuiteCRM, Leads: https://docs.suitecrm.com/user/sales-relationships/leads/ (como evidencia de práctica)"
  - "Relacion-con-clientes/.investigacion/registro-y-seguimiento.md, componentes 4 a 6"
aliases: [seguimiento de oportunidades, gestión de oportunidades, automatización de la fuerza de ventas, sales force automation, SFA, pipeline management]
creado: 2026-11-27
revisado: 2026-11-27
---

# Seguimiento comercial

El seguimiento comercial es el registro de las ventas posibles antes de que haya un pedido: quién se interesó, qué venta podría salir con cada uno, por cuánto, en qué etapa está y qué se habló. Lo forman tres objetos: el interesado, la oportunidad y la actividad.

Dentro de [Relación con clientes](../relacion-con-clientes.md) es la vertical que solo existe cuando alguien sale a vender o responde consultas. Como inferencia de la base, un comercio que vende en el mostrador puede no tenerla; una empresa con vendedores la usa todos los días. Alimenta al [registro del cliente](../Registro-del-cliente/registro-del-cliente.md), porque un interesado que se convierte crea una cuenta y un contacto, y al [presupuesto](../Presupuesto/presupuesto.md), porque una oportunidad se concreta en uno o varios presupuestos.

## Registro, no método

El método de llevar una venta (a quién buscar, cómo calificar, qué etapas tiene el embudo y cuándo se pasa de una a otra) está en [Ventas](../../Ventas/ventas.md). Esta vertical registra lo que ese método produce:

| Ventas decide | Acá se registra |
|---|---|
| Si un contacto vale la pena ([calificación](../../Ventas/Descubrimiento-y-calificacion/calificacion.md)) | El estado del [interesado](interesado.md): abierto, calificado o descartado, con su motivo |
| Qué etapas tiene el embudo ([medición comercial](../../Ventas/Medicion-comercial/medicion-comercial.md)) | La etapa de cada [oportunidad](oportunidad.md) como un campo con valores que configura la empresa |
| Cuántas veces insistir ([seguimiento](../../Ventas/Prospeccion/seguimiento.md)) | Las [actividades](actividad.md) hechas y pendientes, con fecha |
| Qué tan rápido responder ([responder lo que entra](../../Ventas/Prospeccion/responder-lo-que-entra.md)) | El origen y la fecha de entrada del interesado |

APQC junta las dos cosas en un mismo proceso, «gestionar interesados y oportunidades» (3.5.1), con pasos para recibirlos, validarlos y calificarlos. La base las separa porque una cosa es cómo se trabaja y otra qué datos quedan.

## Cómo se encadenan los tres objetos

El recorrido típico va del interesado a la oportunidad y de la oportunidad al presupuesto. Alguien deja sus datos en un formulario o en una feria: es un interesado, todavía sin compromiso. Si se califica, se convierte: se crea o se vincula la cuenta, el contacto y una oportunidad, que dice qué podría comprar y por cuánto. La oportunidad avanza por etapas hasta que se gana o se pierde. Mientras tanto, cada llamada, visita o correo queda como una actividad colgada de la oportunidad, del contacto o de la cuenta.

Los sistemas leídos tienen los mismos objetos (un CRM de un proveedor grande, dos sistemas de gestión abiertos y un CRM abierto). Difieren en los detalles: uno permite apagar el paso del interesado y crear la oportunidad directamente, otro define la oportunidad como un interesado ya calificado. Que el interesado sea un objeto aparte es una decisión de diseño, no un hecho del dominio; se discute en [interesado](interesado.md).

## Las dos fechas y los dos ejes

Una oportunidad tiene dos ejes que conviene no mezclar: la **etapa** (cuánto avanzó la conversación) y el **estado** (abierta, ganada o perdida). Y dos fechas: cuándo se espera cerrar, que sirve para prever ingresos, y cuándo es el próximo contacto, que sirve para no olvidarse del cliente. Un sistema abierto tiene las dos fechas como campos distintos. El detalle está en [oportunidad](oportunidad.md).

## Dónde falla

Falla cuando los datos no se cargan. El vendedor carga las oportunidades y las actividades; como inferencia de la base, quien lee el embudo y la previsión suele ser su jefe. Las cifras que circulan sobre cuánto no se carga son de terceros que citan los proveedores de software, sin el estudio original a la vista, y están en [actividad](actividad.md) y en [mitos del CRM](../Fundamentos/mitos-del-crm.md). Falla también con interesados duplicados, que llegan por varios canales y nadie fusiona.

Contactar a un interesado tiene límites legales en la Argentina, que están en [Relación con clientes en la Argentina](../relacion-con-clientes-en-argentina.md) y, desde el lado del método, en [primer contacto](../../Ventas/Prospeccion/primer-contacto.md).

## Qué hay en el seguimiento comercial

- [Interesado](interesado.md) — quien mostró interés y todavía no es cliente: origen, estados, conversión y por qué se separa del cliente.
- [Oportunidad](oportunidad.md) — el registro de una venta posible: monto, etapa, probabilidad, fecha estimada, competidores y motivo de pérdida.
- [Actividad](actividad.md) — llamadas, visitas, correos y tareas, hechas o pendientes, y la línea de tiempo que arman; por qué los vendedores no las cargan.
