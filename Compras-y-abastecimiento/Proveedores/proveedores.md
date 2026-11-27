---
resumen: >-
  Proveedores es la parte de Compras y abastecimiento que trata a quién se le compra y en qué condiciones: el proveedor como registro, su alta, sus precios y plazos, si cumple y cuánto depende la empresa de él. El registro del proveedor es el dato maestro del dominio: se carga una vez y lo leen la solicitud, la orden de compra, la recepción y la cuenta a pagar.
estado: borrador
estabilidad: estable
fuentes:
  - "APQC, Process Classification Framework 7.4 (2024), 4.2.2.2 «Certify and validate suppliers» y 4.2.4 «Manage suppliers»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "ERPNext, Supplier y Supplier Group (según su resumen; como evidencia de práctica): https://docs.frappe.io/erpnext/supplier ; https://docs.frappe.io/erpnext/supplier-group"
  - "Washington State Auditor's Office, Protect your vendor master file from fraudsters (leído por extracto): https://sao.wa.gov/the-audit-connection-blog/protect-your-vendor-master-file-fraudsters"
  - "Compras-y-abastecimiento/.investigacion/proveedores.md (2026-11-27), sección 1"
  - "Compras-y-abastecimiento/.investigacion/apqc-4-2.md (2026-11-27)"
aliases: [proveedores, registro del proveedor, ficha del proveedor, maestro de proveedores, vendor master, supplier master, supplier management, gestión de proveedores]
creado: 2026-11-27
revisado:
---

# Proveedores

Proveedores es la parte de Compras y abastecimiento que trata a quién se le compra y en qué condiciones: el proveedor como registro, su alta, sus precios y plazos, si cumple y cuánto depende la empresa de él. El registro del proveedor es el dato maestro del dominio: se carga una vez y lo leen la solicitud, la orden de compra, la recepción y la cuenta a pagar.

Dentro de [Compras y abastecimiento](../compras-y-abastecimiento.md) es la vertical que no cambia con cada compra. Recibe de [Abastecimiento estratégico](../Abastecimiento-estrategico/abastecimiento-estrategico.md) el proveedor elegido y los términos acordados con él. Le da a la [Orden de compra](../Orden-de-compra/orden-de-compra.md) los datos, los precios y los plazos que cada orden trae solos. Y recibe del [Seguimiento de la orden](../Seguimiento-de-la-orden/seguimiento-de-la-orden.md) las entregas y los rechazos con que se lo evalúa. Sin software, es la carpeta de proveedores con sus listas de precios; con software, es la tabla que leen los demás módulos (lectura de esta base).

APQC 7.4 reparte esta vertical en dos lugares: la homologación del proveedor (4.2.2.2 «Certify and validate suppliers») y su gestión (4.2.4 «Manage suppliers»). Este último grupo incluye mantener su información (4.2.4.1), analizar su desempeño (4.2.4.2) y controlar la calidad de lo que entrega (4.2.4.4).

## Qué guarda el registro del proveedor

El registro dice quién es el proveedor, cómo se le compra y cómo se le paga. La documentación de un sistema abierto lo arma así, según su resumen: varias direcciones y contactos (facturación, depósito, oficina) como registros enlazados, una cuenta bancaria por defecto, una plantilla de condición de pago y un grupo de proveedores que se puede anidar. Lo que se carga en el proveedor gana sobre lo de su grupo, y lo del grupo sobre el valor por defecto de la empresa.

El mismo registro guarda el bloqueo: una marca que impide comprarle, recibirle facturas o pagarle, a veces hasta una fecha. Se define en [alta de proveedor](alta-de-proveedor.md#el-bloqueo-de-un-proveedor), porque el alta, la evaluación y el fraude lo usan igual. Lo que el registro necesita para la Argentina (la CUIT, la condición frente al IVA, si emite facturas apócrifas) está en [Compras y abastecimiento en la Argentina](../compras-y-abastecimiento-en-argentina.md).

Es el espejo del [registro del cliente](../../Relacion-con-clientes/Registro-del-cliente/registro-del-cliente.md): la misma forma de datos, del otro lado de la venta.

## Por qué cada proveedor tiene un solo registro

Un proveedor cargado dos veces tiene dos saldos, dos historias y dos cuentas bancarias que controlar. Como inferencia de la base, que ninguna fuente dice, eso abre la puerta a pagar dos veces la misma factura y esconde cuánto se le compra en total, que es el dato del que parte el [análisis del gasto](../Abastecimiento-estrategico/analisis-del-gasto.md). El auditor del estado de Washington pide revisar el registro de proveedores al menos una vez al año, para sacar duplicados e inactivar a los que no se usan.

Lograr un solo registro cuando el proveedor aparece en varios sistemas es el problema del registro de oro, que está en [datos maestros](../../Datos/Gobierno-y-calidad/datos-maestros.md). Esta vertical se ocupa de lo de adentro: qué datos lleva y quién puede cambiarlos.

> [!NOTE] Sin fuente todavía: cómo se modela el proveedor que también es cliente (un registro con dos roles o dos registros enlazados), y qué pasa con la compensación de saldos entre los dos.

## Dónde el registro se cruza con el fraude

El registro del proveedor es el blanco de dos fraudes de compras que repiten las fuentes leídas: dar de alta un proveedor inventado y cambiarle la cuenta bancaria a uno verdadero. Las cifras de la ACFE y la regla de que quien carga un proveedor no aprueba sus facturas ni las paga están en [autorizaciones](../../Contabilidad/Control-interno/autorizaciones.md#la-aprobación-de-pagos-y-el-alta-de-proveedores) y en [separación de funciones](../../Contabilidad/Control-interno/separacion-de-funciones.md). Acá importa dónde se aplican: en el alta y en cada cambio de datos, que es lo que desarrolla [alta de proveedor](alta-de-proveedor.md).

## Qué hay en Proveedores

- [Alta de proveedor](alta-de-proveedor.md) — los datos que se cargan, la verificación de que el proveedor existe, la homologación antes de la primera compra y el bloqueo.
- [Condiciones del proveedor](condiciones-del-proveedor.md) — lista de precios, plazo de entrega, mínimos y condición de pago, y el registro artículo-proveedor que la orden trae solo.
- [Evaluación de proveedores](evaluacion-de-proveedores.md) — entregas a tiempo y completas, calidad aceptada, puntaje, estados y la revisión periódica.
- [Relación con proveedores](relacion-con-proveedores.md) — segmentar, desarrollar y decidir cuánto depender de cada uno: proveedor único o varios.
