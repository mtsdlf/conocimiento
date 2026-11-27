---
resumen: >-
  Los reportes operativos y legales son lo que un software de gestión saca de su propia base y tiene que entregar: los listados del día (qué despachar, quién debe, qué vence) y los libros y registros que pide la ley, con corte a una fecha. Lo que junta varias fuentes o mucha historia para decidir es inteligencia de negocio y vive en Datos.
estado: borrador
estabilidad: estable
fuentes:
  - "Martin Fowler, Reporting Database (2014): https://martinfowler.com/bliki/ReportingDatabase.html"
  - "Soh, Sia y Tay-Yap (2000), Enterprise resource planning: cultural fits and misfits: is ERP a universal solution?, CACM 43(4):47-51 (según extractos; la página dio 403): https://cacm.acm.org/research/enterprise-resource-planning-cultural-fits-and-misfits"
  - "Leyh (2012), Tailoring of ERP Systems, cap. 6 de Readings on Enterprise Resource Planning: https://web.eng.fiu.edu/chen/Summer%202012/EGN%205621%20Enterprise%20Systems%20Collaboration/Reading%20ERP/Readings_on_ERP_chapter06.pdf"
  - "Documentación de un ERP de un proveedor grande, Financial dimensions: https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-dimensions"
  - "Software-de-gestion/.investigacion/columnas-tecnicas-97.md y columnas-tecnicas-complemento.md (2026-11-27)"
aliases: [reportes, informes, listados, reportes operativos, operational reporting, reportes legales, libros legales, statutory reports, salidas del sistema, output, desajuste de salida, output misfit]
creado: 2026-11-27
revisado:
---

# Reportes operativos y legales

Los reportes operativos y legales son lo que un software de gestión saca de su propia base y tiene que entregar: los listados del día (qué despachar, quién debe, qué vence) y los libros y registros que pide la ley, con corte a una fecha. Lo que junta varias fuentes o mucha historia para decidir es inteligencia de negocio y vive en Datos.

Es una columna angosta a propósito. Los tableros, el almacén de datos y la capa semántica son de [Visualización y BI](../../Datos/Visualizacion-y-BI/visualizacion-y-bi.md), que va a sumar una parte sobre BI sobre el software de gestión. Acá queda lo que el sistema no puede dejar de producir por sí mismo.

## Los dos tipos de salida

Un reporte operativo le dice a alguien qué hacer hoy; un reporte legal deja constancia, ante un tercero, de lo que pasó en un período. Los dos salen de los mismos [documentos](documento-y-estados.md) y del mismo [registro de movimientos](registro-de-movimientos-y-dimensiones.md), pero se piden distinto (tabla de esta base):

| Reporte | Tipo | Dominio | Qué necesita del sistema |
|---|---|---|---|
| Pedidos pendientes de entrega | operativo | [pedido de venta](../../Relacion-con-clientes/Pedido-de-venta/pedido-de-venta.md) | el avance de cada renglón, al día |
| Órdenes de trabajo abiertas por equipo | operativo | [orden de trabajo](../../Activos-y-mantenimiento/Orden-de-trabajo/orden-de-trabajo.md) | el estado de cada orden |
| Antigüedad de saldos de clientes | operativo | [gestión de la cobranza](../../Tesoreria/Credito-y-cobranzas/gestion-de-la-cobranza.md) | las cuentas corrientes con sus vencimientos |
| Libro diario y mayor | legal | [asiento y libros](../../Contabilidad/Registro/asiento-y-libros.md) | los asientos de un período cerrado |
| Libros de IVA ventas y compras | legal | [registros fiscales](../../Impuestos/Cumplimiento/registros-fiscales.md#qué-tiene-que-poder-emitir-un-sistema) | los comprobantes con detalle por alícuota |
| Libro de sueldos | legal | [libro de sueldos](../../Administracion-de-personal-y-nomina/Cargas-y-declaraciones/libro-de-sueldos.md) | las liquidaciones del período, sin editar |

El operativo vale si está al día; el legal vale si se puede volver a emitir igual. Qué tiene que poder emitir un sistema para el fisco está enumerado en la nota de registros fiscales, y lo que pide la norma argentina a un sistema, en [software de gestión en la Argentina](../software-de-gestion-en-argentina.md).

## El reporte legal sale con corte a una fecha

En lectura de esta base, un libro legal tiene tres exigencias que no tiene un tablero. Se arma sobre la base donde se registraron los hechos, no sobre una copia atrasada. Se corta a una fecha y respeta el cierre: si el período está bloqueado, el libro de ese período no cambia ([fechas, vigencias y cierre](fechas-vigencias-y-cierre.md#la-fecha-de-bloqueo)). Y se puede reproducir: emitido hoy o dentro de cinco años, da lo mismo.

> [!NOTE]
> Sin fuente todavía: una fuente primaria que diga que los reportes legales se emiten sobre la base de registro, con corte a una fecha y reproducibles. Es lectura de esta base a partir de la regla de no editar lo registrado y del cierre de período.

## Qué sale de la base operativa y qué no

Fowler explica por qué el reporte pesado se separa de la base de la aplicación: «The operational needs and the reporting needs are, however, often quite different - with different requirements from a schema and different data access patterns». Propone una base de reportes con una copia de los datos en otro esquema, y una de sus ventajas es que «Queries run against the reporting database don't add to the load on the operational database». Agrega un matiz: «many reporting needs work perfectly well with yesterday's data».

La misma separación, con el ejemplo de una tabla de pedidos, está en [OLTP y OLAP](../../Datos/Modelado-y-almacenamiento/oltp-y-olap.md). En lectura de esta base, los listados operativos de la tabla de arriba se quedan en la base de la aplicación, porque necesitan el dato de este momento y tocan pocas filas. El análisis de varios años, o el que cruza el sistema de gestión con la tienda y el CRM, va a una copia, y ahí empieza Datos.

## Las dimensiones existen para el reporte

Las [dimensiones](registro-de-movimientos-y-dimensiones.md#dimensiones-en-lugar-de-cuentas) que lleva cada movimiento son lo que permite sacar del sistema un estado de resultados por centro de costo o por proyecto; la documentación de un ERP de un proveedor grande las justifica con ese ejemplo. Un reporte por dimensión solo cuadra con el total si la dimensión es obligatoria donde importa.

## El desajuste de salida

Soh, Sia y Tay-Yap (2000) clasificaron los desajustes entre un paquete y la organización que lo adopta en tres tipos, y uno es el de salida: el formato de presentación o el contenido de la información que el sistema entrega. Según los extractos del trabajo, fue «the most prevalent form of misfit noted». El estudio es de un hospital de Singapur, y no conviene generalizar esa frecuencia a cualquier empresa.

Leyh (2012) cuenta el ajuste de reportes entre los tipos de adaptación que no tocan el código del producto. En lectura de esta base, eso hace del reporte el lugar donde un sistema se adapta con menos riesgo, siempre que se arme sobre los datos sin cambiarlos. Cómo pesa cada adaptación al actualizar está en [configurar o personalizar](configurar-o-personalizar.md).

## Cómo falla un reporte

- **El libro que cambia.** Un libro de un período cerrado que da distinto al volver a emitirlo tiene un movimiento editado o un período reabierto.
- **El reporte pesado en la hora pico.** Un análisis de años corriendo sobre la base que factura frena la facturación.
- **El formato legal escrito en el código.** Cuando el fisco cambia el formato, cambia el programa y no un dato de configuración (lectura de esta base).
- **El total que no se puede reconciliar.** Un total por dimensión que no cuadra con el total contable, porque la dimensión era optativa.
