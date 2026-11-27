---
resumen: >-
  El registro del cliente es lo que una empresa guarda de cada uno de sus clientes: quién es (una empresa o una persona, con sus contactos), quién compra, quién paga y a dónde se entrega, y en qué condiciones se le vende. Es el [dato maestro](../../Datos/Gobierno-y-calidad/datos-maestros.md) del dominio: se carga una vez y lo leen el presupuesto, el pedido, la factura y la cobranza.
estado: vigente
estabilidad: estable
fuentes:
  - "Martin Fowler, Analysis Patterns, cap. «Organization Structures» (borrador): https://martinfowler.com/apsupp/accountability.pdf (leído en parte)"
  - "APQC, Process Classification Framework, categoría 3.5.2 «Manage customers and accounts», copia de un tercero sin versión declarada: https://capechamber.co.za/enterprise/improve-your-business-processes/3-market-and-sell-products-and-services"
  - "Microsoft Learn, tabla Account (Dynamics 365 Customer Engagement): https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/entities/account (como evidencia de práctica)"
  - "ERPNext, Customer: https://docs.frappe.io/erpnext/user/manual/en/customer (como evidencia de práctica)"
  - "Relacion-con-clientes/.investigacion/registro-y-seguimiento.md"
aliases: [ficha del cliente, maestro de clientes, customer master, registro de clientes, customer record, cuenta del cliente]
creado: 2026-11-27
revisado: 2026-11-27
---

# Registro del cliente

El registro del cliente es lo que una empresa guarda de cada uno de sus clientes: quién es (una empresa o una persona, con sus contactos), quién compra, quién paga y a dónde se entrega, y en qué condiciones se le vende. Es el [dato maestro](../../Datos/Gobierno-y-calidad/datos-maestros.md) del dominio: se carga una vez y lo leen el presupuesto, el pedido, la factura y la cobranza.

Dentro de [Relación con clientes](../relacion-con-clientes.md) es la vertical que no cambia con cada venta. Recibe del [Seguimiento comercial](../Seguimiento-comercial/seguimiento-comercial.md) los clientes nuevos, cuando un [interesado](../Seguimiento-comercial/interesado.md) se convierte (un sistema abierto lo marca como convertido recién cuando hay un pedido). Le da al [Presupuesto](../Presupuesto/presupuesto.md) y al [Pedido de venta](../Pedido-de-venta/pedido-de-venta.md) la lista de precios, la condición de pago, el límite de crédito y las direcciones. Sin software, es la libreta o la planilla de clientes del mostrador; con software, es la tabla que todos los módulos leen.

## Por qué el cliente es un dato maestro

El cliente aparece en casi todos los documentos de la venta y de lo que sigue: el presupuesto, el pedido, el remito, la factura, el recibo. Si cada uno guardara su propia copia del nombre, la dirección y la condición de pago, un cambio de domicilio obligaría a corregir todo. Por eso el cliente se registra una vez y los documentos lo referencian. Según una copia del marco de APQC de versión no declarada, lo pone dentro del proceso de vender, en 3.5.2 «Manage customers and accounts», con pasos propios para juntar la información del cliente y para sacar los duplicados.

Lograr un solo registro cuando hay varios sistemas (la tienda, el punto de venta, el sistema de gestión) es el problema del [registro de oro](../../Datos/Gobierno-y-calidad/datos-maestros.md). Esta vertical se ocupa de lo de adentro: qué datos lleva el registro, cómo se arma la relación entre empresa y persona, y qué condiciones se guardan.

## Las tres decisiones de diseño del registro

Quien modela el registro del cliente decide tres cosas, y cada una tiene más de una respuesta que funciona:

1. **Empresa y persona en una tabla o en dos.** Fowler propone una sola abstracción, la parte, de la que la persona y la organización son subtipos, y el cliente como un rol de la parte. Algunos sistemas siguen esa idea con un único registro de contacto que puede ser persona o empresa; otros separan la cuenta (la empresa) del contacto (la persona). Está en [cuenta y contacto](cuenta-y-contacto.md).
2. **Un solo cliente o varios roles.** En una venta simple, el que compra, el que paga y el que recibe son el mismo. En una empresa con sucursales pueden ser tres registros distintos. El modelo chico (direcciones de factura y de entrega dentro de la misma cuenta) alcanza mientras el que paga sea el que compra.
3. **Dónde viven las condiciones.** La lista de precios, la condición de pago y el límite de crédito pueden ser del cliente, del pagador o de cada operación. Está en [condiciones comerciales](condiciones-comerciales.md).

## Dónde falla

Falla por duplicados: el mismo cliente cargado dos veces, con dos saldos y dos historias. Aparecen cuando nadie busca antes de crear, cuando una importación no compara contra lo que ya hay o cuando un formulario web inserta sin chequear. Como criterio de la base, falla también cuando un dato que debería ser del cliente se carga a mano en cada pedido, y cada vendedor lo escribe distinto. Lo general de la calidad de un dato está en [calidad de datos](../../Datos/Gobierno-y-calidad/calidad-de-datos.md).

Que exista una vista única y completa del cliente se discute: según resúmenes de comentarios de la industria, no de investigación, suele ser un objetivo difícil de alcanzar entero. Se presenta como objetivo de diseño con límites en [mitos del CRM](../Fundamentos/mitos-del-crm.md).

Lo que el registro tiene que guardar en la Argentina (la clave fiscal, la condición frente al IVA, el consentimiento para los datos personales) está en [Relación con clientes en la Argentina](../relacion-con-clientes-en-argentina.md).

## Qué hay en el registro del cliente

- [Cuenta y contacto](cuenta-y-contacto.md) — la parte con roles, empresa y persona, jerarquías de cuentas, comprador, pagador y destinatario, y cómo se evitan los duplicados.
- [Condiciones comerciales](condiciones-comerciales.md) — lista de precios, condición de pago, límite de crédito, moneda, vendedor y zona: lo que el cliente trae a cada presupuesto y pedido.
- [Cartera de clientes](cartera-de-clientes.md) — a quién le toca cada cliente, cómo se agrupan en territorios y cómo se clasifican.
