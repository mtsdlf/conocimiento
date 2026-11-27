---
resumen: >-
  Facturar por hito es cobrar un proyecto a precio cerrado según un calendario de facturación: un anticipo al firmar, cuotas que se liberan cuando se alcanzan los hitos acordados y, a veces, una retención de garantía hasta el final. La hora trabajada es costo y no dispara factura; lo que la dispara es el hito.
estado: borrador
estabilidad: semi
fuentes:
  - "Microsoft Learn, Dynamics 365 Project Operations, Manage contract values for project-based sales: https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/sales/manage-contract-values-project-based-sales"
  - "Microsoft Learn, Dynamics 365 Project Operations, Invoice schedules on a contract line: https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/sales/invoice-schedules-contract-line-sales"
  - "Microsoft Learn, Dynamics 365 Project Operations, Set up advances and retainer-based contracts: https://learn.microsoft.com/en-us/dynamics365/project-operations/pro/sales/set-up-advances-retainer-based-contracts-sales"
  - "Microsoft Learn, Dynamics 365 Project Operations, Revise project invoices: https://learn.microsoft.com/en-us/dynamics365/project-operations/proforma-invoicing/revise-project-invoices"
  - "Odoo 19, Down payments: https://www.odoo.com/documentation/19.0/applications/sales/sales/invoicing/down_payment.html"
  - "Odoo 19, Invoice project milestones: https://www.odoo.com/documentation/19.0/applications/sales/sales/invoicing/milestone.html"
  - "IFRS Foundation, NIIF 15, párrafos 60-65 (componente de financiación), 106 y B44-B47 (pagos por adelantado y derechos no ejercidos): https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15.html"
  - "Grant Thornton, Revenue from Contracts with Customers: Navigating the guidance in ASC 606 and ASC 340-40 (enero 2022), ASC 606-10-45-2, 606-10-55-46 a 55-49 y la tabla de componente de financiación: https://www.grantthornton.com/content/dam/grantthornton/website/assets/content-page-files/audit/pdfs/2022/revenue-from-contracts-with-customers-updated-220124.pdf"
  - "FAR 52.232-5 Payments under Fixed-Price Construction Contracts, párrafo (e) Retainage: https://www.acquisition.gov/far/52.232-5"
  - "FAR 52.232-7 Payments under Time-and-Materials and Labor-Hour Contracts, párrafo (a)(7): https://www.acquisition.gov/far/52.232-7"
  - "Servicios-profesionales-y-proyectos/.investigacion/proyecto-y-facturacion.md (sección 3.2)"
  - "Servicios-profesionales-y-proyectos/.investigacion/practica-de-sistemas.md (secciones 4.3 y 4.4)"
aliases: [facturación por hito, milestone billing, calendario de facturación, billing schedule, invoice schedule, anticipo, adelanto, down payment, advance, retención, retainage, retención de garantía]
creado: 2026-11-27
revisado:
---

# Facturación por hito

Facturar por hito es cobrar un proyecto a precio cerrado según un calendario de facturación: un anticipo al firmar, cuotas que se liberan cuando se alcanzan los hitos acordados y, a veces, una retención de garantía hasta el final. La hora trabajada es costo y no dispara factura; lo que la dispara es el hito.

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

El anticipo es plata que el cliente paga antes de que se haga el trabajo. En un sistema abierto se pide como porcentaje o como monto fijo sobre el pedido confirmado, entra como renglón de la factura y queda en una sección de anticipos del pedido; aun con un anticipo del 100 %, hace falta otra factura para completar el pedido. En la Argentina, cobrar un anticipo obliga a facturarlo: está en [servicios profesionales en la Argentina](../servicios-profesionales-en-argentina.md#cuándo-nace-la-obligación-de-facturar). En un sistema de gestión de servicios, el anticipo es un pago único que se concilia contra lo que el proyecto va devengando, y no está disponible para aplicar hasta que se factura.

Para la contabilidad, lo cobrado antes de trabajar es un pasivo del contrato: la firma le debe el servicio al cliente. Ese asiento está en [ingresos y cuentas a cobrar](../../Contabilidad/Operaciones/ingresos-y-cuentas-a-cobrar.md#cobrar-antes-de-entregar-anticipos-e-ingresos-diferidos), y cómo se descuenta a medida que se trabaja, en [trabajo en curso](trabajo-en-curso.md).

La NIIF 15 lo dice así (B44): al recibir un pago por adelantado, la firma reconoce un pasivo del contrato por el monto del pago, por su obligación de transferir, o de «stand ready to transfer», bienes o servicios en el futuro, y lo da de baja, reconociendo ingreso, cuando los transfiere. Si el cliente no ejerce todos sus derechos (B45 lo llama *breakage*), la firma que espera tener derecho a ese monto lo reconoce como ingreso «in proportion to the pattern of rights exercised by the customer», y la que no lo espera, cuando la probabilidad de que el cliente ejerza lo que le queda se vuelve remota (B46); para saber si lo espera, se aplican las reglas de restricción de la contraprestación variable (párrafos 56-58). Lo que se cobró y la ley obliga a entregar a un tercero, como un organismo público por bienes no reclamados, es un pasivo y no ingreso (B47). El ASC 606-10-55-46 a 55-49 de los Estados Unidos dice lo mismo, según el texto que reproduce Grant Thornton: dos fuentes.

En un sistema abierto, la factura final de un pedido con anticipo trae un campo «Already invoiced» y se arma «for the exact amount needed to complete the total payment». Con facturación por cantidades entregadas, si todavía no se entregó nada, el anticipo no se puede descontar porque el sistema no admite facturas con total negativo, y la salida es una nota de crédito que cancela el borrador.

## La retención de garantía

La retención de garantía (*retainage*) es una parte de cada pago que el cliente se guarda hasta que el trabajo avanza como se pactó o termina. No es la retención de impuestos que hace un cliente agente de retención, que está en [Servicios profesionales en la Argentina](../servicios-profesionales-en-argentina.md#las-retenciones-que-sufre-quien-factura). Hay dos textos primarios, de contratos públicos de los Estados Unidos, que la regulan, uno de obra y otro de servicios:

- **Obra** (FAR 52.232-5, párrafo (e)): si el avance no fue satisfactorio, el comprador puede retener «a maximum of 10 percent» del pago hasta que lo sea; cuando la obra está sustancialmente terminada, puede retener lo que considere adecuado para su protección y libera el resto.
- **Servicios por tiempo y materiales** (FAR 52.232-7, párrafo (a)(7)): salvo que el contrato diga otra cosa, el comprador puede exigir que el contratista retenga de sus facturas una reserva, «5 percent» de lo debido, con un total que no pase de 50.000 dólares, que se mantiene hasta que el contratista entrega la liberación de reclamos del párrafo (g).

Quedan afuera los números del Reino Unido y del plazo de defectos que traía la fuente anterior, que era una enciclopedia en línea y no se pudo respaldar. Dinero y norma: son dos cláusulas de la misma regulación, no dos fuentes independientes, y valen para contratos públicos de los Estados Unidos; un contrato privado fija sus propios porcentajes. Lectura de esta base: en servicios profesionales la retención de garantía es poco común y aparece sobre todo en ingeniería y arquitectura, donde los contratos se parecen a los de obra. Se buscó una fuente que lo diga (formularios del Instituto Americano de Arquitectos y del FIDIC, guías de estudios) y no apareció una que se pudiera leer entera. Si existe, el registro tiene que separar la parte retenida de cada factura y llevar su saldo hasta liberarlo en el [cierre financiero](../Proyecto-del-cliente/proyecto-del-cliente.md#el-cierre-financiero).

## Cobrar antes o después cuesta plata

Un anticipo grande es financiación del cliente a la firma; un hito final pesado, financiación de la firma al cliente. La NIIF 15 pide ajustar el precio por el valor del dinero en el tiempo cuando el contrato tiene un componente de financiación significativo (párrafos 60-65), con una excepción práctica: la firma «need not adjust» si entre la entrega y el pago espera que pase un año o menos (párrafo 63). Y hay otras dos salidas. No hay componente de financiación significativo si el cliente pagó por adelantado y el momento de la entrega queda a su criterio (62(a)), que es el caso de una bolsa de horas que el cliente usa cuando quiere. Tampoco si la diferencia entre el precio prometido y el de contado se debe a algo que no es financiar, como que los términos de pago protejan a una parte de que la otra no cumpla (62(c)), que es lo que hace una retención de garantía. Grant Thornton recoge el caso en una tabla del ASC 606: un cliente que paga en cuotas trimestrales y retiene el 10 % hasta terminar la obra no genera un componente de financiación. En la mayoría de los proyectos cortos de servicios, entonces, el anticipo y la retención de garantía no se ajustan contablemente. Dinero y norma: dos fuentes, la IFRS Foundation y el ASC 606 según Grant Thornton.

El costo de financiar el proyecto sí pesa en la caja, aunque no se ajuste en el asiento. Cómo pesan los hitos en la caja de una firma chica está en el [plan financiero mínimo](../../Emprender/Finanzas/plan-financiero-minimo.md); el cobro en sí es de Tesorería y finanzas de la empresa en marcha, un tema que todavía no está escrito.
