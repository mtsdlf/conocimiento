---
resumen: >-
  Los permisos de un software de gestión dicen qué puede hacer cada rol con cada tipo de documento, sobre qué registros, y qué combinaciones de tareas no puede tener una misma persona. Son la forma en que el sistema lleva a la práctica la separación de funciones del control interno.
estado: borrador
estabilidad: estable
fuentes:
  - "COSO, Internal Control — Integrated Framework, Executive Summary, mayo 2013: https://www.coso.org/_files/ugd/3059fc_1df7d5dd38074006bce8fdf621a942cf.pdf"
  - "McGill University, Internal Audit, Internal Controls: https://www.mcgill.ca/internalaudit/node/647"
  - "Documentación de un ERP de código abierto, User Permissions: https://docs.frappe.io/erpnext/user/manual/en/user-permissions"
  - "Documentación de otro ERP de código abierto, Restrict access to data: https://raw.githubusercontent.com/odoo/documentation/19.0/content/developer/tutorials/restrict_data_access.rst"
  - "Documentación de un ERP de un proveedor grande, Identify and resolve conflicts in segregation of duties (según resumen): https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/fin-ops/sysadmin/identify-resolve-conflicts-segregation-duties"
  - "Soh, Sia y Tay-Yap (2000), Enterprise resource planning: cultural fits and misfits: is ERP a universal solution?, CACM 43(4):47-51 (según extractos; la página dio 403): https://cacm.acm.org/research/enterprise-resource-planning-cultural-fits-and-misfits"
  - "Software-de-gestion/.investigacion/columnas-tecnicas-97.md y columnas-tecnicas-complemento.md (2026-11-27)"
aliases: [permisos, roles, perfiles de acceso, control de acceso, access control, RBAC, permisos por rol, permisos por registro, record rules, row-level security, separación de funciones, segregation of duties, SoD, incompatibilidades]
creado: 2026-11-27
revisado:
---

# Permisos y separación de funciones

Los permisos de un software de gestión dicen qué puede hacer cada rol con cada tipo de documento, sobre qué registros, y qué combinaciones de tareas no puede tener una misma persona. Son la forma en que el sistema lleva a la práctica la separación de funciones del control interno.

La teoría está escrita en Contabilidad y no se repite: qué tareas no se juntan y por qué, en [separación de funciones](../../Contabilidad/Control-interno/separacion-de-funciones.md); lo que un sistema tiene que poder hacer para sostener los controles, en [controles sobre los sistemas](../../Contabilidad/Control-interno/controles-sobre-sistemas.md#lo-que-un-sistema-de-gestión-tiene-que-poder-hacer); quién aprueba qué según el monto, en [autorizaciones](../../Contabilidad/Control-interno/autorizaciones.md). Acá va cómo se modela eso en el software.

Una precisión sobre la fuente. COSO 2013 dice que «Segregation of duties is typically built into the selection and development of control activities», y que donde no es práctica la gerencia elige controles alternativos. No nombra la tríada de autorizar, registrar y custodiar: esa división sale de manuales y guías, como la de auditoría interna de la Universidad McGill.

## Tres capas de permisos

| Capa | Qué responde | Cómo lo resuelven los productos |
|---|---|---|
| Rol sobre tipo de documento | qué acciones puede hacer un rol (crear, confirmar, anular, aprobar) con las órdenes de compra, las facturas, los pagos | grupos y derechos de acceso por modelo, en la documentación de un ERP de código abierto |
| Restricción por registro | sobre cuáles de esos documentos: los de su empresa, su sucursal, su zona | permisos de usuario «based on the link fields in the document», en otro ERP de código abierto; reglas de registro en el primero |
| Incompatibilidad entre roles | qué combinaciones no puede tener una misma persona | reglas de separación de funciones que se controlan al asignar roles, en un ERP de un proveedor grande, según su resumen |

La primera capa distingue la acción del objeto, que es lo que pide la nota de separación de funciones: crear una orden de compra y aprobarla son dos permisos distintos sobre el mismo documento. Las acciones coinciden con los estados del [documento](documento-y-estados.md): quien puede pasar de borrador a confirmado no es necesariamente quien puede anular.

La segunda capa usa la [estructura de la organización](estructura-de-la-organizacion.md) y los [datos maestros](datos-maestros-y-partes.md): un vendedor ve los clientes de su zona porque el cliente tiene una zona, y el sistema filtra por ese campo. En un software vendido como servicio, esta capa trabaja adentro de cada cliente; el aislamiento entre clientes es de [multi-tenancy](../../Arquitectura/Sistemas-distribuidos/multi-tenancy.md).

## La incompatibilidad como dato

La tercera capa es la más propia del software de gestión. En lectura de esta base, una regla de incompatibilidad se guarda como dato: un par de permisos (dar de alta proveedores y liberar pagos) que el sistema no deja juntar en un mismo usuario. Según el resumen de su documentación, en el ERP del proveedor grande la regla se controla al asignar roles, y un conflicto que la empresa decide aceptar se resuelve dejando registrada una razón.

Dos casos de dominio muestran por qué hace falta. En compras y tesorería, quien crea o cambia un proveedor no aprueba sus facturas ni libera sus pagos ([autorizaciones](../../Contabilidad/Control-interno/autorizaciones.md#la-aprobación-de-pagos-y-el-alta-de-proveedores)); la [seguridad de los pagos](../../Tesoreria/Pagos-a-proveedores/seguridad-de-los-pagos.md) depende de eso. En servicios profesionales, la [hoja de horas](../../Servicios-profesionales-y-proyectos/Registro-de-horas/hoja-de-horas.md) la aprueba alguien distinto de quien la cargó, porque nadie aprueba lo propio. La primera regla compara dos permisos; la segunda compara al usuario con el autor del documento, y el sistema tiene que poder expresar las dos.

La nota de separación de funciones agrega dos exigencias: negar la combinación también al administrador y, cuando la empresa la permite, dejar rastro de quién hizo cada paso para el control compensatorio. Ese rastro es de la [auditoría de cambios](auditoria-de-cambios.md).

## Lo que no es esta columna

Hay otras dos capas de permisos que se confunden con esta. Quién puede cambiar el software y desplegarlo es separación de funciones en el desarrollo, y está en [trazabilidad de cambios](../../DevOps/Repositorios/trazabilidad-de-cambios.md). Quién accede a los recursos de la nube donde corre el sistema es [identidad y acceso](../../Cloud/Gobernanza-e-identidad/identidad-y-acceso-en-azure.md). Las dos protegen la plataforma; esta columna protege las operaciones del negocio.

## Cómo fallan los permisos

- **Solo la primera capa.** Con permisos por tipo de documento y sin restricción por registro, cada vendedor ve todos los clientes de la empresa.
- **El administrador como excepción.** Un usuario que puede saltearse una aprobación sin dejar rastro reproduce la debilidad que [controles sobre los sistemas](../../Contabilidad/Control-interno/controles-sobre-sistemas.md#lo-que-un-sistema-de-gestión-tiene-que-poder-hacer) asocia a la anulación de controles en los fraudes.
- **Un desajuste con el producto.** Soh, Sia y Tay-Yap (2000) cuentan, entre los desajustes funcionales de un paquete, los de acceso y los de control; según los extractos del trabajo, son procedimientos que la organización necesita y el producto no trae. Un producto que no puede negar una combinación de roles cae acá, y la decisión de cómo cubrirlo es del [análisis de brechas](../Implementacion/analisis-de-brechas.md).
- **Permisos que no se revisan.** El sistema tiene que poder emitir la lista de quién tiene qué permiso; sin ella, la revisión periódica que pide el control interno no se puede hacer.

Los permisos también ponen límite al tiempo: quién puede cargar una fecha anterior al cierre o mover la fecha de bloqueo es de esta columna ([fechas, vigencias y cierre](fechas-vigencias-y-cierre.md)).
