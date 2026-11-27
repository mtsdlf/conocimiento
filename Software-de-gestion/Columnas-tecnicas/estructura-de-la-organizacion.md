---
resumen: >-
  La estructura de la organización es qué empresas, sucursales, depósitos y unidades lleva un software de gestión, cómo se ordenan y qué datos comparten entre ellas y cuáles son propios de cada una. Es opcional (el sistema de un comercio chico lleva una sola empresa) y no es lo mismo que multi-tenancy.
estado: vigente
estabilidad: estable
fuentes:
  - "Martin Fowler, Organization Structures, borrador del segundo volumen de Analysis Patterns (Organization Hierarchy, Accountability): https://martinfowler.com/apsupp/accountability.pdf"
  - "Documentación de un ERP de código abierto, Multi-company Guidelines: https://raw.githubusercontent.com/odoo/documentation/19.0/content/developer/howtos/company.rst"
  - "Documentación de un ERP de un proveedor grande, Financial dimensions (entidades legales): https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-dimensions"
  - "Software-de-gestion/.investigacion/columnas-tecnicas-97.md (2026-11-27)"
aliases: [estructura organizativa, organization structure, organization hierarchy, multiempresa, multi-company, varias empresas, entidad legal, legal entity, sucursal, unidad de negocio, business unit, empresa del grupo]
creado: 2026-11-27
revisado: 2026-11-27
---

# Estructura de la organización

La estructura de la organización es qué empresas, sucursales, depósitos y unidades lleva un software de gestión, cómo se ordenan y qué datos comparten entre ellas y cuáles son propios de cada una. Es opcional (el sistema de un comercio chico lleva una sola empresa) y no es lo mismo que multi-tenancy.

Un grupo con dos sociedades, tres sucursales y cuatro depósitos necesita que el sistema sepa a qué unidad pertenece cada documento, cada movimiento y cada usuario. El software chico lo resuelve con una empresa fija; el que crece tiene que decidir desde el modelo de datos qué es de la organización entera y qué es de cada parte.

## Una jerarquía o varias

Fowler define la jerarquía de la organización como lo que «Represents the hierarchy of organizational units within a business»: la empresa, sus divisiones, sus sucursales. Cuando hay más de una jerarquía a la vez propone otro patrón, *Accountability*, que modela cada relación entre unidades con su tipo. Una misma sucursal puede depender de una sociedad en la jerarquía legal, de una gerencia regional en la de gestión y de una zona en la comercial (ejemplo de esta base).

Los dominios ya traen sus propias jerarquías. Personal y nómina tiene la de [puestos y áreas](../../Administracion-de-personal-y-nomina/Legajo/puesto-y-estructura.md); Activos y mantenimiento, la [jerarquía de activos](../../Activos-y-mantenimiento/Registro-de-activos/jerarquia-de-activos.md) de planta, sistema y equipo; Contabilidad, los [centros de costo](../../Contabilidad/Contabilidad-de-gestion/centros-de-costo.md). En lectura de esta base, la columna no las reemplaza: da el esqueleto (empresa legal, sucursal, depósito) del que cuelgan las demás.

## Lo compartido y lo propio de cada empresa

La documentación de un ERP de código abierto describe tres mecanismos para varias empresas en un mismo sistema:

| Mecanismo | Qué hace | Ejemplo |
|---|---|---|
| Campos que dependen de la empresa | un mismo registro guarda un valor distinto según la empresa | el mismo artículo con una cuenta contable distinta en cada sociedad |
| Chequeo de coherencia | impide mezclar registros de dos empresas en un documento | un pedido de la empresa A no puede llevar un depósito de la B |
| Reglas de seguridad por empresa | cada usuario ve los registros de las empresas que tiene asignadas | el vendedor de una sociedad no ve los clientes de la otra |

Qué se comparte es una decisión por dato. En lectura de esta base, lo habitual es compartir los [datos maestros](datos-maestros-y-partes.md) (la parte, el artículo) y separar lo que la ley o la contabilidad atan a cada sociedad: la numeración de comprobantes, la condición fiscal, el plan de cuentas cuando difiere y los saldos. Un cliente que le compra a las dos empresas del grupo es una parte con dos cuentas corrientes, una por sociedad.

## Una dimensión no es una empresa

La documentación del ERP de un proveedor grande permite compartir dimensiones entre entidades legales, con excepciones por entidad, y advierte que una dimensión no reemplaza a una entidad legal: los impuestos y el stock se llevan por entidad. Una sucursal que es solo un lugar de venta puede ser una [dimensión](registro-de-movimientos-y-dimensiones.md#dimensiones-en-lugar-de-cuentas) de los movimientos; una sociedad con su propia identificación fiscal, sus propios libros y su propia declaración de impuestos tiene que ser una empresa del sistema (ejemplo de esta base).

La decisión pesa en dos dominios al mismo tiempo. Para Impuestos, cada empresa emite su [comprobante fiscal](../../Impuestos/Cumplimiento/comprobante-fiscal.md) con su numeración y lleva sus [registros fiscales](../../Impuestos/Cumplimiento/registros-fiscales.md). Para Inventario, cada depósito tiene su saldo y un traspaso entre depósitos de dos sociedades es una venta entre empresas, no un movimiento interno. Cómo se pone precio a lo que una unidad le da a otra de la misma empresa está en [precios de transferencia](../../Contabilidad/Contabilidad-de-gestion/centros-de-costo.md#precios-de-transferencia-entre-centros-de-la-misma-empresa).

## Varias empresas no es multi-tenancy

[Multi-tenancy](../../Arquitectura/Sistemas-distribuidos/multi-tenancy.md) es servir a varios clientes desde una misma instancia con los datos de cada uno aislados: los tenants no comparten nada entre sí. Varias empresas dentro de un mismo cliente comparten datos a propósito, como el maestro de artículos o la parte que es cliente de las dos. Un software de gestión vendido como servicio suele tener las dos cosas: cada cliente es un tenant, y adentro de cada tenant puede haber varias empresas (lectura de esta base).

Confundirlas tiene un costo en los dos sentidos. Si cada empresa del grupo se da de alta como tenant, no hay forma de compartir el maestro ni de consolidar. Si dos clientes distintos se cargan como empresas de un mismo tenant, quedan separados solo por las reglas de seguridad, que es lo que multi-tenancy existe para evitar.

## Cómo falla la estructura

- Empezar con una sola empresa fija. Agregar la segunda obliga a poner la empresa en cada tabla y en cada consulta, como pasa con `tenant_id` en multi-tenancy (lectura de esta base).
- Una sociedad modelada como dimensión. Los reportes por dimensión cuadran, pero la sociedad no tiene libros ni declaración propia.
- Documentos que mezclan empresas. Sin el chequeo de coherencia, una factura de la empresa A descuenta stock del depósito de la B.

Los [permisos](permisos-y-separacion-de-funciones.md) usan la estructura para restringir qué registros ve cada usuario, y la [integración](integracion-y-migracion.md) tiene que saber a qué empresa pertenece cada dato que entra.
