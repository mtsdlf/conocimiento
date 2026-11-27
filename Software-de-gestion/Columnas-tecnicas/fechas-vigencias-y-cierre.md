---
resumen: >-
  En un software de gestión, todo hecho tiene dos fechas, cuándo pasó y cuándo se registró; muchos datos valen desde y hasta una fecha (un precio, una alícuota, un sueldo); y el cierre de período bloquea lo anterior para que los saldos ya informados no cambien.
estado: borrador
estabilidad: estable
fuentes:
  - "Martin Fowler, Temporal Patterns (Time Narrative): https://martinfowler.com/eaaDev/timeNarrative.html"
  - "Martin Fowler, Audit Log: https://martinfowler.com/eaaDev/AuditLog.html"
  - "Documentación de un ERP de código abierto, Year-end closing (fecha de bloqueo): https://raw.githubusercontent.com/odoo/documentation/19.0/content/applications/finance/accounting/reporting/year_end.rst"
  - "Documentación de otro ERP de código abierto, Immutable Ledger: https://docs.frappe.io/erpnext/user/manual/en/immutable-ledger-in-erpnext"
  - "Software-de-gestion/.investigacion/columnas-tecnicas-97.md (2026-11-27)"
aliases: [fecha del hecho, fecha de registro, fecha contable, posting date, record date, actual date, vigencia, effectivity, fecha de bloqueo, lock date, cierre de período, period close, período cerrado, bitemporal]
creado: 2026-11-27
revisado:
---

# Fechas, vigencias y cierre

En un software de gestión, todo hecho tiene dos fechas, cuándo pasó y cuándo se registró; muchos datos valen desde y hasta una fecha (un precio, una alícuota, un sueldo); y el cierre de período bloquea lo anterior para que los saldos ya informados no cambien.

El tiempo no es de ningún dominio y aparece en todos: la lista de precios de ventas, la alícuota de impuestos, el aumento retroactivo de la nómina, la valuación del stock y el cierre contable. Cada tema de dominio lo explica para su caso. Acá va el patrón común y lo que el software tiene que guardar para sostenerlo.

## La fecha del hecho y la fecha de registro

Fowler abre sus patrones temporales con un aumento de sueldo que llega tarde, y concluye: «we really need to provide two dates: a record date and an actual date». La fecha del hecho dice cuándo pasó algo en el negocio; la de registro, cuándo lo supo el sistema. Con las dos se contestan dos preguntas distintas: cuánto correspondía pagar en marzo y cuánto se creía en marzo que correspondía.

El caso entero, con las cifras de un aumento retroactivo y cómo se paga la diferencia en el período abierto, está en [retroactivos y reliquidaciones](../../Administracion-de-personal-y-nomina/Liquidacion-de-sueldos/retroactivos-y-reliquidaciones.md#la-fecha-del-hecho-y-la-fecha-de-registro), y el [legajo](../../Administracion-de-personal-y-nomina/Legajo/legajo.md#la-historia-del-legajo-con-sus-dos-fechas) guarda las dos fechas en cada cambio. En contabilidad el mismo par aparece como fecha del comprobante y fecha contable: una factura de proveedor de octubre que llega en noviembre se registra en noviembre con su fecha original (ejemplo de esta base).

Para el diseño, cada documento y cada movimiento llevan al menos dos fechas: la del hecho, que la carga la persona, y la de registro, que la pone el sistema y nadie edita. La segunda es la que usa la [auditoría de cambios](auditoria-de-cambios.md): Fowler trata el *Audit Log* como la forma simple de guardar esa dimensión.

## Vigencias: datos que valen desde y hasta

Fowler llama *Effectivity* al período en que algo vale. Muchos datos maestros y de configuración no se pisan cuando cambian: se agrega un valor nuevo con su fecha de inicio, y el anterior queda para lo que pasó antes.

| Dato con vigencia | Dominio | Qué pasa si se pisa |
|---|---|---|
| Regla de una lista de precios | [precio y descuentos](../../Relacion-con-clientes/Presupuesto/precio-y-descuentos.md#de-dónde-sale-el-precio-de-un-renglón) | un presupuesto viejo cambia de precio al reimprimirlo |
| Alícuota de un impuesto | [IVA](../../Impuestos/Impuestos-al-consumo/iva.md) | una nota de crédito sobre una factura vieja calcula el impuesto con la tasa de hoy |
| Sueldo o categoría | [legajo](../../Administracion-de-personal-y-nomina/Legajo/legajo.md) | una reliquidación no puede reconstruir lo que valía en cada mes |
| Versión de la lista de materiales | [orden de producción](../../Produccion/Ejecucion-en-planta/orden-de-produccion.md) | el costo de una orden cerrada cambia con un [cambio de ingeniería](../../Produccion/Producto-y-proceso/cambios-de-ingenieria.md) posterior |

La tercera columna es lectura de esta base. La regla que sale de ella: el sistema busca el valor vigente a la fecha del hecho del documento, no a la fecha de hoy. Un precio cambiado mañana no toca el pedido de ayer.

## La fecha de bloqueo

El cierre de período congela lo anterior a una fecha. La documentación de un ERP de código abierto lo resuelve con una fecha de bloqueo general: los asientos con fecha anterior «cannot be created or modified during the audit», y las excepciones solo las da un administrador. Los ajustes que se hacen antes de cerrar son de [ajustes de cierre](../../Contabilidad/Estados-contables/ajustes-de-cierre.md); la regla de que un período cerrado no admite asientos con fecha anterior está en [asiento y libros](../../Contabilidad/Registro/asiento-y-libros.md#corregir-con-un-asiento-nuevo).

En lectura de esta base, un sistema suele necesitar más de un bloqueo: uno contable, otro de stock, otro de impuestos, porque cada uno se cierra cuando se presenta lo suyo. El de impuestos coincide con la [declaración](../../Impuestos/Cumplimiento/declaracion-y-pago.md) del período. Un hecho que se descubre después del cierre no reabre el período: entra en el período abierto con su fecha del hecho, como el retroactivo de nómina.

## Lo que mueve una fecha pasada

Una fecha pasada no es inocente. La documentación de otro ERP de código abierto advierte dos cosas: no correr la fecha contable para saltarse controles, y que un movimiento de stock con fecha anterior revaloriza todo lo posterior, porque el costo de cada salida depende de lo que había entrado antes. Un remito de compra cargado con fecha del mes pasado cambia el costo de lo vendido de todas las ventas que vinieron después (ejemplo de esta base).

Por eso la fecha del hecho es un campo que se controla. Quién puede cargar una fecha anterior a cierto límite es de [permisos](permisos-y-separacion-de-funciones.md); hasta dónde llega el límite lo pone la fecha de bloqueo.

## Cómo falla el tiempo

- **Una sola fecha.** Sin fecha de registro no se puede saber qué se informó en su momento; sin fecha del hecho, el retroactivo se mezcla con el mes en que se cargó.
- **Pisar en lugar de versionar.** Una alícuota o un precio que se sobreescribe cambia los recálculos de documentos viejos.
- **Editar la fecha de registro.** Fowler dice que cambiar hacia atrás el tiempo de registro rompe la integridad del registro; la cita completa está en [retroactivos y reliquidaciones](../../Administracion-de-personal-y-nomina/Liquidacion-de-sueldos/retroactivos-y-reliquidaciones.md#corregir-con-movimientos-nuevos).
- **Un período que se reabre sin rastro.** Si el administrador mueve la fecha de bloqueo, el cambio tiene que quedar en la auditoría.

Los [reportes legales](reportes-operativos-y-legales.md) dependen de esta columna: un libro con corte a una fecha solo se puede volver a emitir igual si lo anterior al cierre no cambió. Lo que la norma argentina pide a un sistema sobre plazos y libros está en [software de gestión en la Argentina](../software-de-gestion-en-argentina.md).
