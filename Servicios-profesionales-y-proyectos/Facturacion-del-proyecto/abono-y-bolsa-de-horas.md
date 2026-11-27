---
resumen: >-
  El abono es un pago periódico fijo por tener un servicio disponible, se use o no; la bolsa de horas es un paquete de horas que el cliente paga por adelantado y que se descuenta a medida que se trabaja. Los dos se facturan antes de trabajar, pero se registran distinto: el abono se gana con el paso del tiempo y la bolsa con cada hora consumida.
estado: borrador
estabilidad: semi
fuentes:
  - "IFRS Foundation, NIIF 15 Ejemplos ilustrativos, Ejemplo 18 (cuota de un club de salud): https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15-ie.html"
  - "IFRS Foundation, NIIF 15, párrafo 106 (pasivo del contrato): https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15.html"
  - "Microsoft Learn, Dynamics 365 Project Operations, Set up advances and retainer-based contracts: https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/sales/set-up-advances-retainer-based-contracts-sales"
  - "Microsoft Learn, Dynamics 365 Project Operations, Invoice a retainer or advance: https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/proforma-invoicing/invoice-retainer-advance-sales"
  - "Servicios-profesionales-y-proyectos/.investigacion/proyecto-y-facturacion.md (sección 3.3)"
  - "Servicios-profesionales-y-proyectos/.investigacion/practica-de-sistemas.md (sección 4.4)"
aliases: [abono, bolsa de horas, horas prepagas, prepaid hours, retainer, iguala, abono mensual, monthly retainer, block of hours, drawdown, horas incluidas]
creado: 2026-11-27
revisado:
---

# Abono y bolsa de horas

El abono es un pago periódico fijo por tener un servicio disponible, se use o no; la bolsa de horas es un paquete de horas que el cliente paga por adelantado y que se descuenta a medida que se trabaja. Los dos se facturan antes de trabajar, pero se registran distinto: el abono se gana con el paso del tiempo y la bolsa con cada hora consumida.

Son las reglas de [facturación del proyecto](facturacion-del-proyecto.md) para la relación que sigue en el tiempo, más que para un proyecto con fin. El abono como modelo de negocio (qué incluye, cuánto se cobra, por qué se dan de baja) está en [abono de cuidado](../../Emprender/Modelo-de-negocio/abono-de-cuidado.md); el servicio con alcance y precio fijos anunciados, en [servicio productizado](../../Emprender/Modelo-de-negocio/servicio-productizado.md). Acá, qué se registra y cómo se factura.

## Tres cosas con el mismo nombre

En la práctica, «abono» y *retainer* nombran por lo menos tres arreglos distintos, y cada uno pide un registro distinto. La separación es criterio de esta base:

| Arreglo | Qué paga el cliente | Qué consume el trabajo | Qué pasa con lo no usado |
|---|---|---|---|
| Abono de disponibilidad | Una cuota por período | Nada; el trabajo entra en la cuota | Se pierde; la firma lo gana igual |
| Bolsa de horas | Un paquete de horas por adelantado | Horas del saldo | Depende del contrato: vence, se traslada o se devuelve |
| Anticipo periódico conciliado | Una cuota por período a cuenta | Horas a tarifa, que se comparan con lo cobrado | Se concilia al cierre del período |

## El abono se gana con el tiempo

El Ejemplo 18 de la NIIF 15 es un club de salud que cobra «CU100 per month (CU1,200 over the year)». La obligación es tener el club disponible, y el ingreso se reconoce parejo a lo largo del año «whether or not the customer uses the clubs». Es la base contable de un abono de disponibilidad: la cuota de cada mes es ingreso de ese mes aunque el cliente no haya pedido nada.

Para el registro eso quiere decir, en lectura de esta base, que en un abono de disponibilidad las horas trabajadas son costo y no consumen nada: sirven para saber si el abono deja plata, no para facturar. Si el contrato pone un cupo de cambios chicos dentro de la cuota, el cupo se cuenta para avisarle al cliente, no para reconocer el ingreso. Dinero y norma: una sola fuente, la IFRS Foundation.

## La bolsa se gana hora por hora

En una bolsa de horas, el cliente compra, por ejemplo, 40 horas y la firma le descuenta cada hora que trabaja. El registro natural es un saldo que se mueve: una entrada por la compra y una salida por cada hora aprobada, sin pisar el número. Es el patrón de [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md), aplicado a horas en lugar de stock, y su uso acá es criterio de esta base.

> [!NOTE] Sin fuente todavía: que el saldo de horas no consumidas sea un pasivo del contrato hasta que se consume o vence es inferencia de esta base desde la definición de pasivo del contrato (NIIF 15, párrafo 106) y de lo que dice [ingresos y cuentas a cobrar](../../Contabilidad/Operaciones/ingresos-y-cuentas-a-cobrar.md#cobrar-antes-de-entregar-anticipos-e-ingresos-diferidos) sobre el cobro adelantado. No se leyó una fuente que trate la bolsa de horas, ni los párrafos B44-B47 de la norma sobre los derechos que el cliente no ejerce.

Las horas que vencen sin usarse son el punto delicado. Si el contrato dice que vencen, la firma deja de deber ese servicio; si dice que se trasladan o se devuelven, la deuda sigue. El registro tiene que guardar la regla de vencimiento con la bolsa, no en la cabeza de quien la vendió.

> [!NOTE] Sin fuente todavía: cómo se reconoce el ingreso de las horas que vencen sin usarse, y si en la Argentina una cláusula de vencimiento de horas prepagas es válida frente a un consumidor.

Los practicantes que escriben sobre abonos desaconsejan venderlos como horas incluidas, porque atan al cliente a la tarifa y le ponen techo al ingreso; está en [abono de cuidado](../../Emprender/Modelo-de-negocio/abono-de-cuidado.md#cómo-se-cobra). Es una discusión de modelo de negocio; el registro tiene que poder llevar las dos formas.

## El anticipo periódico que se concilia

Un sistema de gestión de servicios llama *retainer* a algo intermedio: «a negotiated set of equally distributed payments that the customer pays throughout the duration of a project», pensado para contratos por tiempo y materiales en los que el cliente quiere una factura y un cobro previsibles. Funciona así:

1. Cada período se factura la cuota del anticipo.
2. Las horas se aprueban a tarifa, como en [facturación por hora](facturacion-por-hora.md).
3. Al cierre del período se compara lo devengado con lo cobrado. Si lo devengado excede la cuota, se factura solo el exceso, o se deja la conciliación para una factura final.
4. Las facturas siguientes aplican el anticipo disponible y el cliente ve su factura reducida.

El monto del anticipo no está disponible hasta que se factura, y el sistema lleva por cada anticipo el monto, lo usado y el saldo. Al cerrar el proyecto, un saldo sin usar se puede devolver desde una factura o desde el contrato. El mismo sistema marca la diferencia con el precio cerrado: en precio cerrado el monto de la factura no está atado a los costos incurridos; en el anticipo conciliado, sí.

## Cómo se factura y cómo falla

La factura del abono y la de la bolsa salen antes del trabajo, como un [pedido recurrente](../../Relacion-con-clientes/Pedido-de-venta/tipos-de-pedido.md#el-pedido-recurrente) en el caso del abono. Lectura de esta base sobre lo anterior: el registro falla cuando no se sabe cuál de los tres arreglos se vendió. Un abono tratado como bolsa le debe horas al cliente que nadie le prometió; una bolsa tratada como abono reconoce como ingreso un saldo que todavía se debe. La diferencia entre lo cobrado y lo ganado, en los tres casos, se ve en [trabajo en curso](trabajo-en-curso.md).
