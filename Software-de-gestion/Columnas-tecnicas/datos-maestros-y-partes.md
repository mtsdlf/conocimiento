---
resumen: >-
  Los datos maestros de un software de gestión son las entidades que todos los módulos comparten (la parte, el artículo, la cuenta), cada una con un solo registro que leen los documentos. La parte es una persona u organización que puede tener varios roles a la vez, como cliente, proveedor o empleado, sin duplicarse por rol.
estado: borrador
estabilidad: estable
fuentes:
  - "Martin Fowler, Organization Structures, borrador del segundo volumen de Analysis Patterns (Party, Accountability): https://martinfowler.com/apsupp/accountability.pdf"
  - "Documentación de un ERP de un proveedor grande, Global address book overview: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/organization-administration/overview-global-address-book"
  - "Davenport (1998), Putting the Enterprise into the Enterprise System, HBR 76(4) (según resumen de terceros): https://maaw.info/ArticleSummaries/ArtSumDavenport98.htm"
  - "Soh, Sia y Tay-Yap (2000), Enterprise resource planning: cultural fits and misfits: is ERP a universal solution?, CACM 43(4):47-51 (según extractos; la página dio 403): https://cacm.acm.org/research/enterprise-resource-planning-cultural-fits-and-misfits"
  - "Software-de-gestion/.investigacion/columnas-tecnicas-97.md y columnas-tecnicas-complemento.md (2026-11-27)"
aliases: [datos maestros, maestros, master data, parte, party, parte con roles, party role, libreta de direcciones, address book, maestro frente a transacción]
creado: 2026-11-27
revisado:
---

# Datos maestros y partes

Los datos maestros de un software de gestión son las entidades que todos los módulos comparten (la parte, el artículo, la cuenta), cada una con un solo registro que leen los documentos. La parte es una persona u organización que puede tener varios roles a la vez, como cliente, proveedor o empleado, sin duplicarse por rol.

Qué son los datos maestros en general, el registro de oro y cómo se unen registros duplicados entre sistemas está en [datos maestros](../../Datos/Gobierno-y-calidad/datos-maestros.md). Acá va lo que es del diseño del software: cómo se modela la parte, qué es maestro y qué es transacción, y qué se rompe cuando el modelo está mal.

## Una base central que leen todos los módulos

Según el resumen de Davenport (1998), el núcleo de un sistema empresarial es una base central que alimenta a todas las aplicaciones modulares. Los maestros son la parte de esa base que no pertenece a ningún módulo: el cliente lo leen el presupuesto, el pedido, la factura y la cobranza; el artículo lo leen compras, el depósito, la producción y la venta.

La regla de diseño es que cada entidad tenga un registro y que los demás la referencien. Un módulo de ventas con su propia tabla de clientes y un módulo de cobranzas con otra obligan a mantener las dos iguales a mano. Ese es el problema que la base central viene a sacar, y el que vuelve cada vez que un módulo nuevo trae su propia copia.

## La parte: persona u organización con roles

Fowler lo dice así: «I usually define party as the supertype of person and organization». Cliente, proveedor y empleado son roles de una parte y no clases distintas, como lo plantea Fowler según la nota de Relación con clientes. Cómo se modelan esos roles y por qué no conviene la herencia simple está desarrollado en [cuenta y contacto](../../Relacion-con-clientes/Registro-del-cliente/cuenta-y-contacto.md), dentro de Relación con clientes.

La documentación de un ERP de un proveedor grande muestra el patrón en un producto. Su libreta de direcciones global es «a centralized repository for master data» de todas las personas y organizaciones, internas y externas; cada parte tiene uno o más roles (cliente, proveedor, trabajador) y una dirección se cambia «in only one place».

El caso que lo justifica aparece en dos dominios a la vez. Una empresa que le vende a un distribuidor y además le compra repuestos tiene una cuenta corriente de cliente y otra de proveedor con la misma contraparte. Con una parte y dos roles, el sistema puede mostrar lo que se le debe y lo que debe juntos, y un cambio de domicilio llega a la [orden de compra](../../Compras-y-abastecimiento/Orden-de-compra/orden-de-compra.md) y al [pedido de venta](../../Relacion-con-clientes/Pedido-de-venta/pedido-de-venta.md). Con dos registros, la compensación entre las dos [cuentas corrientes](../../Contabilidad/Registro/cuentas-corrientes.md) depende de que alguien sepa que son la misma empresa (lectura de esta base).

## Qué es maestro y qué es transacción

| Maestro | Dominio que lo define | Lo leen |
|---|---|---|
| Parte con rol de cliente | [registro del cliente](../../Relacion-con-clientes/Registro-del-cliente/registro-del-cliente.md) | presupuesto, pedido, factura, cobranza |
| Parte con rol de proveedor | [alta de proveedor](../../Compras-y-abastecimiento/Proveedores/alta-de-proveedor.md) | orden de compra, recepción, factura del proveedor, pago |
| Parte con rol de empleado | [legajo](../../Administracion-de-personal-y-nomina/Legajo/legajo.md) | asistencia, liquidación, cargas |
| Artículo | [artículo](../../Inventario-y-depositos/Existencias/articulo.md) | compras, depósito, producción, venta |
| Equipo | [registro de activos](../../Activos-y-mantenimiento/Registro-de-activos/registro-de-activos.md) | orden de trabajo, mantenimiento preventivo |
| Cuenta contable | [plan de cuentas](../../Contabilidad/Registro/plan-de-cuentas.md) | todas las reglas que generan asientos |

Un maestro cambia poco y cada cambio importa; una transacción es un hecho con fecha que no se edita una vez confirmado. Esa diferencia decide el resto del diseño. Los hechos quedan en el [documento](documento-y-estados.md) y en el [registro de movimientos](registro-de-movimientos-y-dimensiones.md), que son su propio rastro. Los maestros sí se editan, y por eso su rastro es la [auditoría de cambios](auditoria-de-cambios.md).

El documento copia algunos datos del maestro al confirmarse (el domicilio de entrega, la condición de IVA del cliente, el precio) y referencia el resto. Una factura emitida tiene que mostrar el domicilio que tenía el cliente ese día, no el de hoy. Qué se copia y qué se referencia es una decisión por campo, y equivocarse en un sentido o en el otro reescribe la historia o la congela de más (lectura de esta base). Los datos que valen desde una fecha, como un precio o un sueldo, se resuelven con [vigencias](fechas-vigencias-y-cierre.md).

## Cómo falla el modelo de maestros

- Duplicados por rol. El proveedor que también es cliente se carga dos veces con dos códigos. Cómo se encuentran y se unen está en [datos maestros](../../Datos/Gobierno-y-calidad/datos-maestros.md#cómo-se-encuentra-a-la-misma-persona-en-dos-registros).
- Un desajuste de datos con el producto. Soh, Sia y Tay-Yap (2000) clasificaron como desajustes de datos los de formato o de relaciones entre entidades del modelo del paquete; según los extractos del trabajo, arreglarlos obliga a reestructurar tablas del núcleo, que es el cambio más caro. Un producto que no admite que una parte tenga dos roles, o que un artículo tenga dos unidades, cae acá. El estudio es de un hospital de Singapur, y la decisión de cómo resolver cada desajuste es del [análisis de brechas](../Implementacion/analisis-de-brechas.md).
- Un cambio sin control en un dato sensible. El cambio de la cuenta bancaria de un proveedor tiene que volver a pasar por aprobación ([alta de proveedor](../../Compras-y-abastecimiento/Proveedores/alta-de-proveedor.md#el-cambio-de-cuenta-bancaria-vuelve-a-pasar-por-el-alta)). En el software eso se apoya en dos columnas: [permisos](permisos-y-separacion-de-funciones.md) para quién puede cambiarlo y [auditoría](auditoria-de-cambios.md) para el valor viejo y el nuevo.

## Con qué columnas se cruza

Con varias empresas en el mismo sistema, hay que decidir qué maestros se comparten entre ellas y cuáles son propios de cada una ([estructura de la organización](estructura-de-la-organizacion.md)). Cuando conviven varios sistemas, hay que decidir cuál manda en cada maestro ([integración y migración](integracion-y-migracion.md)). Y la carga inicial de un sistema nuevo empieza siempre por los maestros, porque todo lo demás los referencia.
