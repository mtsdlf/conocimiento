---
resumen: >-
  El documento es la unidad de trabajo de un software de gestión (el pedido, la factura, el remito, la orden de trabajo): se arma en borrador, se confirma y desde ahí produce movimientos, y se corrige anulándolo con otro documento en lugar de editarlo. Lleva su numeración y, cuando hace falta, una cadena de aprobaciones.
estado: vigente
estabilidad: estable
fuentes:
  - "Framework de un ERP de código abierto, DocStatus (según resumen): https://docs.frappe.io/framework/doctypes/docstatus"
  - "Documentación de un ERP de código abierto, Edit submitted document (según resumen): https://docs.frappe.io/erpnext/user/manual/en/edit-submitted-document"
  - "Documentación de un ERP de código abierto, Naming Series: https://docs.frappe.io/erpnext/user/manual/en/naming-series"
  - "Documentación de un ERP de un proveedor grande, Workflow system overview: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/overview-workflow-system"
  - "Martin Fowler, Accounting Narrative: https://martinfowler.com/eaaDev/AccountingNarrative.html"
  - "Martin Fowler, Accounting Entry: https://martinfowler.com/eaaDev/AccountingEntry.html"
  - "Directiva 2006/112/CE, art. 226, copia del BOE: https://www.boe.es/doue/2006/347/L00001-00118.pdf"
  - "Comisión Europea, Explanatory notes: VAT invoicing rules (Directive 2010/45/EU), 2011, nota C-2: https://taxation-customs.ec.europa.eu/system/files/2016-09/explanatory_notes_en.pdf"
  - "Software-de-gestion/.investigacion/columnas-tecnicas-97.md y columnas-tecnicas-complemento.md (2026-11-27)"
aliases: [documento, comprobante, estados del documento, ciclo del documento, document lifecycle, docstatus, borrador, confirmado, anulado, enmienda, amendment, numeración, serie de numeración, naming series, workflow, flujo de aprobación]
creado: 2026-11-27
revisado: 2026-11-27
---

# Documento y estados

El documento es la unidad de trabajo de un software de gestión (el pedido, la factura, el remito, la orden de trabajo): se arma en borrador, se confirma y desde ahí produce movimientos, y se corrige anulándolo con otro documento en lugar de editarlo. Lleva su numeración y, cuando hace falta, una cadena de aprobaciones.

Casi todo lo que una persona hace en un software de gestión es cargar, confirmar o anular un documento. El [pedido de venta](../../Relacion-con-clientes/Pedido-de-venta/pedido-de-venta.md), la [orden de compra](../../Compras-y-abastecimiento/Orden-de-compra/orden-de-compra.md), la [hoja de horas](../../Servicios-profesionales-y-proyectos/Registro-de-horas/hoja-de-horas.md) y la [orden de trabajo](../../Activos-y-mantenimiento/Orden-de-trabajo/orden-de-trabajo.md) tienen datos distintos y el mismo problema de diseño: hasta cuándo se puede cambiar, qué pasa al confirmar y cómo se deshace.

## Borrador, confirmado y anulado

El framework de un ERP de código abierto lo resuelve con tres estados, según el resumen de su documentación: borrador, confirmado y anulado. Un documento confirmado o anulado no vuelve a borrador. Para corregirlo se anula y se crea una enmienda, un borrador nuevo que apunta al anulado.

Fowler describe la misma frontera desde la contabilidad. Un asiento puede ser «mutable until they are booked», y lo contable nace de un hecho del negocio: «When a Domain Event is processed, it can produce a set of Accounting Transactions». En el vocabulario de este tema, el hecho del negocio es la confirmación del documento, y lo que produce son movimientos.

| Estado | Se puede editar | Produce movimientos | Cómo se sale |
|---|---|---|---|
| Borrador | sí | no | se confirma o se descarta |
| Confirmado | no | sí, al confirmarse | se anula |
| Anulado | no | sí: los opuestos a los que había producido | no se sale; se corrige con una enmienda |

La consecuencia es la regla de toda la columna: lo confirmado no se edita. Anular no borra, agrega los movimientos opuestos, como explica el [registro de movimientos y dimensiones](registro-de-movimientos-y-dimensiones.md). La contabilidad tiene la misma regla para el asiento ([asiento y libros](../../Contabilidad/Registro/asiento-y-libros.md#corregir-con-un-asiento-nuevo)) y el fisco para la factura, que se corrige con una nota de crédito ([comprobante fiscal](../../Impuestos/Cumplimiento/comprobante-fiscal.md#la-factura-no-se-borra-nota-de-crédito-y-nota-de-débito)).

## El estado del ciclo y el avance del negocio

Los tres estados dicen si el documento se puede tocar. No dicen cuánto se cumplió. Un pedido confirmado puede estar sin entregar, entregado en parte o entregado y sin facturar, y el dominio lo describe como [dos ejes cruzados](../../Relacion-con-clientes/Pedido-de-venta/pedido-de-venta.md#los-estados-dos-ejes-cruzados). La orden de compra lleva tres: aprobación, recepción y facturación.

En lectura de esta base, conviene guardar por separado el estado del ciclo, que gobierna qué se puede editar, y el avance de cada eje, que se calcula desde los documentos que siguen (remitos, facturas, recepciones). La hoja de horas muestra un ciclo con un paso más: borrador, enviada, aprobada o devuelta; al aprobarse genera costo y venta pendiente del proyecto, y desde ahí se corrige revirtiendo. La orden de trabajo separa terminar el trabajo físico de cerrar el registro. Cada dominio pone sus estados; el software pone la regla de qué se congela en cada uno.

## Confirmar es una sola operación

Confirmar cambia el estado, asigna el número y escribe los movimientos. Si una parte queda escrita y otra no, el documento dice «confirmado» y el stock no se movió. Por eso va en una sola [transacción](../../Bases-de-datos/Transacciones/transaccion.md) de la base (lectura de esta base).

Cuando la confirmación tiene que disparar pasos en otro sistema (avisar a la tienda, pedir el comprobante electrónico al fisco, reservar en el depósito de un tercero), la transacción ya no alcanza. Esos casos se resuelven con un [outbox](../../Arquitectura/Sistemas-distribuidos/outbox.md) que publica el aviso en la misma transacción, o con una [saga](../../Arquitectura/Sistemas-distribuidos/saga.md) que compensa si un paso falla. Cuál conviene es de [integración y migración](integracion-y-migracion.md).

## Cuándo se numera

La documentación del ERP de código abierto dice que «Masters and transactions can be given prefixes in the form of naming series», y es común una serie por ejercicio o por local. La ley europea pide, para la factura, «un número secuencial, basado en una o varias series, que identifique la factura de forma única» (Directiva 2006/112/CE, art. 226). La Comisión aclara en su guía de 2011 que la elección de series «lies with the business»: puede haber una por sucursal, por tipo de operación o por cliente.

Ninguno de los dos textos dice «sin huecos». Ese requisito sale de la práctica y del derecho de cada país, y la nota de [comprobante fiscal](../../Impuestos/Cumplimiento/comprobante-fiscal.md#por-qué-la-numeración-no-puede-tener-huecos) lo marca como inferencia. Lo que exige la norma argentina a un sistema para numerar y emitir comprobantes está en [software de gestión en la Argentina](../software-de-gestion-en-argentina.md).

La decisión de diseño es en qué estado se asigna el número. Si se asigna al confirmar, un borrador descartado no deja hueco; si se asigna al crear el borrador, cada descarte deja un número sin documento. Un número asignado no se reusa: el documento anulado conserva el suyo. La nota de [autorizaciones](../../Contabilidad/Control-interno/autorizaciones.md#numeración-correlativa-y-formularios-prenumerados) lo da como inferencia a partir de los formularios prenumerados de OpenStax, y no como cita. Las dos cosas son lectura de esta base sobre las fuentes.

## Las aprobaciones

Una aprobación es un estado más entre borrador y confirmado, que solo puede pasar alguien con cierta autoridad. La documentación del ERP de un proveedor grande define el flujo de trabajo como lo que dice «who must complete a task, make a decision, or approve a document», con umbrales por importe. Qué tramos y quién aprueba cada uno lo define la empresa en su matriz de [autorizaciones](../../Contabilidad/Control-interno/autorizaciones.md); un ejemplo de dominio es la aprobación de un descuento en [precio y descuentos](../../Relacion-con-clientes/Presupuesto/precio-y-descuentos.md).

Para el software, la aprobación tiene que quedar registrada con quién, cuándo y sobre qué versión del documento, según la lectura propia que hace la nota de autorizaciones. Quién puede aprobar es de [permisos y separación de funciones](permisos-y-separacion-de-funciones.md).

## Cómo falla un documento

- Un solo campo de estado para todo. Mezclar el ciclo con el avance hace que el pedido diga «entregado» cuando faltan renglones.
- Editar lo confirmado. El saldo puede quedar igual, pero se pierde qué se registró, cuándo y quién lo cambió.
- Aprobar una versión y confirmar otra. Si el documento se puede cambiar después de aprobado sin volver a aprobación, la aprobación no controla nada (lectura de esta base).
- Confirmar con fecha de un período cerrado. Lo impide la fecha de bloqueo de [fechas, vigencias y cierre](fechas-vigencias-y-cierre.md).
