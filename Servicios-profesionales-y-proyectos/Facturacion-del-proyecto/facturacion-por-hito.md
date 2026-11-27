---
resumen: >-
  Facturar por hito es cobrar un proyecto a precio cerrado según un calendario de facturación: un anticipo al firmar, cuotas que se liberan cuando se alcanzan los hitos acordados y, a veces, una retención hasta el final. La hora trabajada es costo y no dispara factura; lo que la dispara es el hito.
estado: borrador
estabilidad: semi
fuentes:
  - "Microsoft Learn, Dynamics 365 Project Operations, Manage contract values for project-based sales: https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/sales/manage-contract-values-project-based-sales"
  - "Microsoft Learn, Dynamics 365 Project Operations, Invoice schedules on a contract line: https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/sales/invoice-schedules-contract-line-sales"
  - "Microsoft Learn, Dynamics 365 Project Operations, Set up advances and retainer-based contracts: https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/sales/set-up-advances-retainer-based-contracts-sales"
  - "Microsoft Learn, Dynamics 365 Project Operations, Revise project invoices: https://learn.microsoft.com/en-us/dynamics365/project-operations/proforma-invoicing/revise-project-invoices"
  - "Odoo 19, Milestone invoicing y Down payments (según resumen): https://www.odoo.com/documentation/19.0/applications/sales/sales/invoicing/down_payment.html"
  - "IFRS Foundation, NIIF 15, párrafos 60-65 (componente de financiación) y 106: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15.html"
  - "Wikipedia, Retainage (según resumen): https://en.wikipedia.org/wiki/Retainage"
  - "Servicios-profesionales-y-proyectos/.investigacion/proyecto-y-facturacion.md (sección 3.2)"
  - "Servicios-profesionales-y-proyectos/.investigacion/practica-de-sistemas.md (secciones 4.3 y 4.4)"
aliases: [facturación por hito, milestone billing, calendario de facturación, billing schedule, invoice schedule, anticipo, adelanto, down payment, advance, retención, retainage, retención de garantía]
creado: 2026-11-27
revisado:
---

# Facturación por hito

Facturar por hito es cobrar un proyecto a precio cerrado según un calendario de facturación: un anticipo al firmar, cuotas que se liberan cuando se alcanzan los hitos acordados y, a veces, una retención hasta el final. La hora trabajada es costo y no dispara factura; lo que la dispara es el hito.

Es una de las reglas de [facturación del proyecto](facturacion-del-proyecto.md). El hito como registro y como evento de aceptación está en [hitos y entregables](../Proyecto-del-cliente/hitos-y-entregables.md); el riesgo del precio cerrado y cómo se pierde plata con él, en [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md). Acá, cómo se arma el calendario y qué pasa con la plata que se cobra antes o después del trabajo.

## La hora es costo, el hito es venta

En un sistema de gestión de servicios, aprobar una hora de una línea a precio cerrado crea solo el costo, sin venta sin facturar. El monto del contrato es el valor pactado y no cambia con las horas. La consecuencia para el registro es que en un precio cerrado la [hoja de horas](../Registro-de-horas/hoja-de-horas.md) no alimenta la factura sino el [costo y margen del proyecto](../Rentabilidad-de-la-firma/costo-y-margen-del-proyecto.md) y el [presupuesto del proyecto](../Proyecto-del-cliente/presupuesto-del-proyecto.md).

## Cómo se arma el calendario de facturación

El sistema leído ofrece dos formas de facturar una línea a precio cerrado:

- **Por hito completo**, que es el valor por defecto: el renglón se factura solo cuando su hito está completo.
- **Por avance**: se factura un porcentaje del hito según cuánto se avanzó.

Además se pueden generar hitos periódicos, dividiendo el monto por la cantidad de períodos, o cargar hitos a mano con nombre, fecha y monto. La regla que no se negocia es que los hitos sumen el valor de la línea: si no suman, el sistema marca error.

Un sistema abierto separa alcanzar el hito de facturarlo: se marca el hito como alcanzado en el pedido y la factura se crea después, aparte. La corrección de un hito facturado, en el primer sistema, es siempre por crédito total; no admite acreditar una parte del hito.

> [!NOTE] Sin fuente todavía: cuántos hitos y con qué peso usan las firmas de servicios. Lo único leído es práctica de agencias, sin estudio: adelantos del 25 % al 50 % y el resto por hitos como la aprobación del diseño, la entrega en un entorno de prueba y el lanzamiento, según [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md#formas-de-repartir-el-riesgo).

## El anticipo

El anticipo es plata que el cliente paga antes de que se haga el trabajo. En un sistema abierto se pide como porcentaje o como monto fijo sobre el pedido confirmado, entra como renglón de la factura y queda en una sección de anticipos del pedido; aun con un anticipo del 100 %, hace falta otra factura para completar el pedido. En un sistema de gestión de servicios, el anticipo es un pago único que se concilia contra lo que el proyecto va devengando, y no está disponible para aplicar hasta que se factura.

Para la contabilidad, lo cobrado antes de trabajar es un pasivo del contrato: la firma le debe el servicio al cliente. Ese asiento está en [ingresos y cuentas a cobrar](../../Contabilidad/Operaciones/ingresos-y-cuentas-a-cobrar.md#cobrar-antes-de-entregar-anticipos-e-ingresos-diferidos), y cómo se descuenta a medida que se trabaja, en [trabajo en curso](trabajo-en-curso.md).

> [!NOTE] Sin fuente todavía: el tratamiento de los pagos por adelantado no reembolsables y de los derechos que el cliente no ejerce en la NIIF 15 (párrafos B44-B47); solo se leyó el título de la sección. Tampoco se leyó cómo un sistema abierto descuenta el anticipo de la factura final.

## La retención

La retención (*retainage*) es una parte del precio que el cliente se guarda hasta que el trabajo termina. La única fuente leída es secundaria y de construcción, no de servicios profesionales: la define como «a portion of the agreed upon contract price deliberately withheld until the work is complete», dice que suele ser del 5 % en el Reino Unido y del 10 % en los Estados Unidos, a veces bajando al 5 % cuando el trabajo llega a la mitad, y que se libera al terminar o, en el Reino Unido, al cierre del período de responsabilidad por defectos.

Para dinero, esta base pide dos fuentes independientes y acá hay una, secundaria y de otro rubro. Lectura de esta base: en servicios profesionales la retención es poco común y aparece sobre todo en ingeniería y arquitectura, donde los contratos se parecen a los de obra. Si existe, el registro tiene que separar la parte retenida de cada factura y llevar su saldo hasta liberarlo en el [cierre financiero](../Proyecto-del-cliente/proyecto-del-cliente.md#el-cierre-financiero).

## Cobrar antes o después cuesta plata

Un anticipo grande es financiación del cliente a la firma; una retención o un hito final pesado, financiación de la firma al cliente. La NIIF 15 pide ajustar el precio por el valor del dinero en el tiempo cuando el contrato tiene un componente de financiación significativo (párrafos 60-65), con una excepción práctica: la firma «need not adjust» si entre la entrega y el pago espera que pase un año o menos (párrafo 63). En la mayoría de los proyectos cortos de servicios, entonces, el anticipo y la retención no se ajustan contablemente. Dinero y norma: una sola fuente, la IFRS Foundation.

El costo de financiar el proyecto sí pesa en la caja, aunque no se ajuste en el asiento. Cómo pesan los hitos en la caja de una firma chica está en el [plan financiero mínimo](../../Emprender/Finanzas/plan-financiero-minimo.md); el cobro en sí es de Tesorería y finanzas de la empresa en marcha, un tema que todavía no está escrito.
