---
resumen: >-
  La auditoría de cambios es la pista de quién cambió qué dato, cuándo y de qué valor a qué valor, sobre todo en lo que un software de gestión sí deja editar (los datos maestros, la configuración y los permisos), que no deja movimientos. Sirve para reconstruir lo que el sistema creía en una fecha y quién lo cambió.
estado: vigente
estabilidad: estable
fuentes:
  - "Martin Fowler, Audit Log: https://martinfowler.com/eaaDev/AuditLog.html"
  - "Martin Fowler, Temporal Patterns (Time Narrative): https://martinfowler.com/eaaDev/timeNarrative.html"
  - "Documentación de un ERP de código abierto, mixins (seguimiento de campos): https://raw.githubusercontent.com/odoo/documentation/19.0/content/developer/reference/backend/mixins.rst"
  - "Documentación de otro ERP de código abierto, Customize Form (Track Changes): https://docs.frappe.io/erpnext/user/manual/en/customize-form"
  - "Software-de-gestion/.investigacion/columnas-tecnicas-97.md (2026-11-27)"
aliases: [auditoría, rastro de auditoría, pista de auditoría, audit trail, audit log, registro de cambios, historial de cambios, change log, seguimiento de cambios, track changes, field tracking]
creado: 2026-11-27
revisado: 2026-11-27
---

# Auditoría de cambios

La auditoría de cambios es la pista de quién cambió qué dato, cuándo y de qué valor a qué valor, sobre todo en lo que un software de gestión sí deja editar (los datos maestros, la configuración y los permisos), que no deja movimientos. Sirve para reconstruir lo que el sistema creía en una fecha y quién lo cambió.

El control interno pide esa pista. Según [controles sobre los sistemas](../../Contabilidad/Control-interno/controles-sobre-sistemas.md#el-registro-de-quién-hizo-qué), la guía GTAG del IIA exige un registro que siga el dato desde la entrada hasta la salida, y la Green Book lo liga a que nadie pueda negar después una acción suya. Acá va dónde se guarda en el software y qué parte del sistema la necesita.

## Lo que ya es su propia pista

Una parte del sistema no necesita auditoría aparte. Un [documento](documento-y-estados.md) confirmado no se edita, y el [registro de movimientos](registro-de-movimientos-y-dimensiones.md) solo agrega filas: el error y su corrección quedan los dos a la vista. Para eso alcanza con que cada documento guarde quién lo creó, lo aprobó, lo confirmó y lo anuló, con la fecha de cada paso.

Lo que sí se edita no deja esa pista solo. En lectura de esta base, son cuatro cosas:

| Lo que se edita | Ejemplo | Dominio |
|---|---|---|
| Datos maestros | la cuenta bancaria de un proveedor, el domicilio de un cliente | [alta de proveedor](../../Compras-y-abastecimiento/Proveedores/alta-de-proveedor.md), [registro del cliente](../../Relacion-con-clientes/Registro-del-cliente/registro-del-cliente.md) |
| Datos con vigencia | el sueldo de un empleado, la regla de una lista de precios | [legajo](../../Administracion-de-personal-y-nomina/Legajo/legajo.md), [precio y descuentos](../../Relacion-con-clientes/Presupuesto/precio-y-descuentos.md) |
| Configuración | una regla de contabilización, un umbral de aprobación | [configurar o personalizar](configurar-o-personalizar.md) |
| Permisos | quién recibió qué rol y quién se lo dio | [permisos y separación de funciones](permisos-y-separacion-de-funciones.md) |

Los borradores también se editan, pero mientras no producen movimientos su historia rara vez importa. La excepción es el documento que pasó por una aprobación: si se cambia después, la aprobación tiene que caer (lectura de esta base).

## El registro de auditoría según Fowler

Fowler define el *Audit Log* como «A simple log of changes, intended to be easily written and non-intrusive». Cada entrada guarda qué cambió, el valor, la fecha del hecho y la fecha de registro. Su diagnóstico es que es fácil de escribir y difícil de consultar: sirve para reconstruir un caso puntual, no para preguntas de todos los días.

Fowler lo trata como la forma simple de llevar la dimensión del tiempo de registro que describe en sus patrones temporales. Si un dato necesita contestar seguido «cuánto valía en tal fecha», la auditoría no alcanza y hace falta una [vigencia](fechas-vigencias-y-cierre.md#vigencias-datos-que-valen-desde-y-hasta). La auditoría contesta otra pregunta: quién lo cambió y cuándo se supo.

Los productos lo resuelven por campo o por tipo de documento. La documentación de un ERP de código abierto permite marcar un campo para que cada cambio quede en el historial del registro. Otro ERP de código abierto ofrece activar el seguimiento de cambios por tipo de documento desde la pantalla de personalización.

## Dos casos

El cambio de la cuenta bancaria de un proveedor es el caso de libro (ejemplo armado sobre las fuentes de Compras y Contabilidad). Alguien cambia el número de cuenta, la próxima corrida de pagos le transfiere a esa cuenta y el proveedor reclama que no cobró. La nota de [autorizaciones](../../Contabilidad/Control-interno/autorizaciones.md#la-aprobación-de-pagos-y-el-alta-de-proveedores) recoge que las guías de empresas que venden software de pagos (sin autoridad independiente) piden guardar el valor viejo, el nuevo, el usuario y la hora; sin eso no hay forma de saber quién lo hizo ni desde cuándo.

En nómina, un sueldo cargado mal y corregido al día siguiente cambia lo que se liquidó si la liquidación corrió en el medio. El legajo guarda las dos fechas de cada cambio, y la auditoría agrega quién lo hizo. Con las dos, el liquidador puede explicar por qué el recibo de ese mes salió distinto ([retroactivos y reliquidaciones](../../Administracion-de-personal-y-nomina/Liquidacion-de-sueldos/retroactivos-y-reliquidaciones.md)).

## Cómo falla la auditoría

- Auditar todo. Un registro de cada cambio de cada campo crece rápido y nadie lo lee; conviene elegir los campos que importan, empezando por los que mueven plata.
- Una auditoría que se puede apagar. Si el administrador desactiva el seguimiento o borra el registro sin dejar rastro, la pista no prueba nada. Según controles sobre los sistemas, el sistema tiene que registrar también quién desactivó un control.
- El registro en una tabla que se edita. La auditoría tiene que ser, ella misma, un registro de solo agregar.
- Confundirla con otras trazas. La historia de los cambios al código del sistema es de [trazabilidad de cambios](../../DevOps/Repositorios/trazabilidad-de-cambios.md); de dónde viene cada dato de un análisis, de [metadatos y linaje](../../Datos/Gobierno-y-calidad/metadatos-y-linaje.md).
