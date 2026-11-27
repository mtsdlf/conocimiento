---
resumen: >-
  Fondear la nómina es dejar la plata en la cuenta de la que sale el sueldo antes de la hora de corte del banco, y el calendario de sueldos es la lista de fechas del año en que salen el neto, los pagos extraordinarios y las cargas; los dos alimentan la proyección de caja y deciden qué pasa cuando la plata no alcanza.
estado: borrador
estabilidad: semi
fuentes:
  - "Federal Reserve Financial Services, FedACH Processing Schedule (vigente desde el 12/09/2022) (leído): https://www.frbservices.org/resources/resource-centers/same-day-ach/fedach-processing-schedule.html"
  - "Nacha, RMAG Originator Essentials (2024) (leída completa): https://www.nacha.org/sites/default/files/2024-10/RMAG_Originator_Essentials.pdf"
  - "Nacha, regla del límite de USD 1 millón por pago de Same Day ACH y su End-user Briefing (26/01/2022) (leídos): https://www.nacha.org/million"
  - "Nacha, Same Day ACH: Moving Payments Faster (Phase 3), página archivada (leída): https://www.nacha.org/rules/same-day-ach-moving-payments-faster-phase-3"
  - "Nacha, regla Reversals and Enforcement (leída): https://www.nacha.org/rules/reversals-and-enforcement"
  - "OIT, Convenio 95 sobre la protección del salario (1949), art. 12, copia de la Universidad de Minnesota (leído): https://hrlibrary.umn.edu/instree/ilo95.html"
  - "OIT, Convenio 173 sobre la protección de los créditos laborales en caso de insolvencia del empleador (1992), copia de la Universidad de Oslo (leídos los arts. 3, 5 a 9 y 12): https://jus.uio.no/english/services/library/treaties/02/2-09/ilo_insolvency.html"
  - "IRS, Publication 15 (2026), Circular E, Employer's Tax Guide, sección 11 Depositing Taxes (leída): https://www.irs.gov/publications/p15"
  - "GOV.UK, Running payroll: reporting to HMRC, Sending an FPS after payday y Pay employers' PAYE (leídas): https://www.gov.uk/running-payroll/reporting-to-hmrc"
  - "OpenStax, Principles of Financial Accounting, 12.5, nómina (leído): https://openstax.org/books/principles-financial-accounting/pages/12-5-record-transactions-incurred-in-preparing-payroll"
  - "CFPB, opinión consultiva Non-application to Earned Wage Access Products (Federal Register 2025-23735, 23/12/2025), partes I.A y I.C.2 y notas 2 a 5 (leídas): https://www.federalregister.gov/documents/2025/12/23/2025-23735/truth-in-lending-regulation-z-non-application-to-earned-wage-access-products"
  - "CFPB, opinión consultiva sobre pago a demanda (Federal Register 2020-26664, 10/12/2020), según su resumen: https://www.federalregister.gov/documents/2020/12/10/2020-26664/truth-in-lending-regulation-z-earned-wage-access-programs"
  - "CFPB, propuesta de regla interpretativa sobre adelantos de sueldo (Federal Register 2024-16827, 31/07/2024), según su resumen: https://www.federalregister.gov/documents/2024/07/31/2024-16827/truth-in-lending-regulation-z-consumer-credit-offered-to-borrowers-in-advance-of-expected-receipt-of"
  - "CFPB, opinión que rescinde la de 2020 (Federal Register 2025-00381, 15/01/2025), según su resumen: https://www.federalregister.gov/documents/2025/01/15/2025-00381/truth-in-lending-regulation-z-consumer-credit-offered-to-borrowers-in-advance-of-expected-receipt-of"
  - "CFPB, retiro de 67 guías (Federal Register 2025-08286, 12/05/2025) (leído el ítem): https://www.federalregister.gov/documents/2025/05/12/2025-08286/interpretive-rules-policy-statements-and-advisory-opinions-withdrawal"
  - "Tesoreria/.investigacion/pago-de-sueldos.md, secciones 3, 4 y 6 (2026-11-27)"
aliases: [fondeo de la nómina, payroll funding, prefondeo, prefunding, calendario de sueldos, calendario de pagos de nómina, payroll calendar, día de pago, payday, hora de corte, cut-off, Same Day ACH, depósito de retenciones, pago a demanda, earned wage access, EWA, adelanto de sueldo a demanda, Convenio 173 OIT, fondo de garantía salarial]
creado: 2026-11-27
revisado:
---

# Fondeo y calendario

Fondear la nómina es dejar la plata en la cuenta de la que sale el sueldo antes de la hora de corte del banco, y el calendario de sueldos es la lista de fechas del año en que salen el neto, los pagos extraordinarios y las cargas; los dos alimentan la proyección de caja y deciden qué pasa cuando la plata no alcanza.

Es la mitad del [pago de sueldos](pago-de-sueldos.md) que mira el reloj; la mitad que mira las cuentas está en [cuentas y acreditación](cuentas-y-acreditacion.md). Las fechas que fija la ley argentina están en [pago de sueldos en Argentina](pago-de-sueldos-en-argentina.md#el-calendario-del-año).

## Cuándo tiene que estar la plata

Cuentan tres horarios, cada uno anterior al otro. El de la red fija cuándo los bancos tienen que mandar los archivos. El del banco de la empresa es más temprano, porque revisa los archivos antes de mandarlos. El de la empresa, en lectura de esta base, es todavía anterior, porque tiene que cerrar el lote, fondear y liberar.

En Estados Unidos, la Reserva Federal, que opera la red, recibe archivos con fecha futura en seis ventanas, la última a las 2:15 de la madrugada (la de las 8 de la noche no existe los viernes), todas con liquidación a las 8:30 del día hábil futuro que lleva el archivo; para pagos del mismo día tiene tres, la primera hasta las 10:30 con liquidación a la 1 de la tarde (hora del Este, horario vigente desde septiembre de 2022). Nacha avisa que esos horarios son para los bancos: «FIs require time to review and process transactions before sending them to the Operator and will establish their own processing deadlines for their Originators». El plazo que le importa a la tesorería es el de su banco, y no se encontró una fuente general sobre cuántos días antes lo piden.

Si el archivo llega tarde, hay un carril rápido con límites. En la red de Estados Unidos, donde se llama Same Day ACH, un archivo con fecha de hoy o anterior se procesa como del mismo día si llega a tiempo para esa ventana, y el pago del mismo día tiene un tope de un millón de dólares por pago desde marzo de 2022. Por encima no se rechaza: pasa a la liquidación del día siguiente. Nacha justificó el pago del mismo día, entre otras cosas, con las nóminas de emergencia, porque «it is critical that an employee be able to withdraw cash on payday». En lectura de esta base, el tope pesa menos en un sueldo que en la transferencia grande que fondea la cuenta de sueldos.

En la práctica, en lectura de esta base, la fecha de fondeo sale de contar hacia atrás desde el día de pago: el día en que el empleado tiene que tener la plata, menos lo que tarda la red en acreditar, menos la hora de corte del banco, menos el tiempo de aprobar y liberar el lote. Ese día va a la [proyección de caja](../Caja-y-liquidez/proyeccion-de-caja.md) como salida.

## El calendario del año

El Convenio 95 de la OIT pide pagar «regularly», en los intervalos que fije la ley, el convenio colectivo o el laudo arbitral, y la liquidación final de quien se va según la ley o «within a reasonable period of time» (art. 12). El calendario de sueldos es esa regla puesta en fechas, y tiene cuatro tipos de fila:

| Fila | Cuándo sale | De dónde sale el dato |
|---|---|---|
| Neto del período | El día de pago de cada período | [Liquidación de sueldos](../../Administracion-de-personal-y-nomina/Liquidacion-de-sueldos/liquidacion-de-sueldos.md#frecuencias-y-período-de-liquidación) |
| Pagos extraordinarios | Bonos, sueldo anual complementario, vacaciones pagadas por adelantado: en su fecha propia | La ley o el convenio de cada país |
| Liquidaciones finales | Cuando alguien se va, en el plazo de la ley | [Liquidación final](../../Administracion-de-personal-y-nomina/Liquidacion-de-sueldos/liquidacion-final.md) |
| Retenciones y cargas | En el vencimiento de cada organismo, días o semanas después del pago | [Cargas y declaraciones](../../Administracion-de-personal-y-nomina/Cargas-y-declaraciones/cargas-y-declaraciones.md) |

Cuando el día de pago no es hábil, en Estados Unidos la práctica de la industria, según Nacha, es pagar el viernes anterior, como cuenta [el pago de sueldos](../../Administracion-de-personal-y-nomina/Liquidacion-de-sueldos/liquidacion-de-sueldos.md#el-pago-de-sueldos) en la liquidación. El Reino Unido solo dice cómo se informa: la declaración va el siguiente día hábil, con la fecha de pago de siempre. Cada país tiene su regla, y el calendario se arma con los feriados del año.

> [!NOTE]
> Sin fuente todavía: el sueldo anual complementario o decimotercer sueldo como concepto general, fuera de un país; y el pico de caja de fin de mes de una nómina mensual. La fila de sueldos en la proyección de 13 semanas ya está en [proyección de caja](../Caja-y-liquidez/proyeccion-de-caja.md#por-qué-trece-semanas), sin fuente nueva para la nómina.

## Las cargas tienen su propio calendario

Las retenciones y las contribuciones salen después del neto, a cada organismo. OpenStax dice que las cargas y beneficios se pagan «in the following period» (12.5). Lo retenido es plata del empleado que la empresa tiene en su cuenta hasta el vencimiento; por eso la proyección lleva dos filas con fechas distintas, y no una sola salida de sueldos (lectura de esta base).

El ejemplo de Estados Unidos muestra que el vencimiento no sigue a la frecuencia de pago. Según la Publicación 15 del IRS de 2026, el calendario de depósito «isn't determined by how often you pay your employees». Sale del total de impuestos de un período de referencia:

- Hasta 50.000 dólares en ese período, la empresa deposita por mes, «by the 15th day of the following month».
- Por encima, deposita dos veces por semana: lo pagado de miércoles a viernes, el miércoles siguiente; lo pagado de sábado a martes, el viernes siguiente.
- Si junta 100.000 dólares o más en un día, deposita el día hábil siguiente.

Depositar tarde cuesta un recargo del 2 % al 10 % según los días de atraso, y del 15 % si sigue impago más de diez días después del primer aviso. La sanción por no ingresar lo retenido (lo que el IRS llama «trust fund tax») es «100% of the unpaid trust fund tax», cobrable a la persona responsable que no lo pagó a sabiendas. En el Reino Unido, el pago a la autoridad fiscal vence el día 22 del mes fiscal siguiente si se paga por mes. Las reglas argentinas están en [pago de sueldos en Argentina](pago-de-sueldos-en-argentina.md#el-calendario-del-año), y la regla del IRS sobre qué pagar primero, en [programación de pagos](../Pagos-a-proveedores/programacion-de-pagos.md#las-prioridades-cuando-la-caja-no-alcanza).

## Cuando la plata no alcanza

Un lote mandado sin fondos no se deshace por la red: Nacha excluye de las reversas la «Lack of funding from a sender», y su guía lo dice corto, «Failure to fund is not an error». En lectura de esta base, si la plata no está, el lote no sale o el banco lo frena, y el sueldo se atrasa.

Fuera de la quiebra no hay una norma general leída que ordene qué se paga primero cuando la caja no alcanza; quién decide es de la [política de tesorería](../politica-de-tesoreria.md), y el criterio de práctica, sin respaldo leído, está en [programación de pagos](../Pagos-a-proveedores/programacion-de-pagos.md#las-prioridades-cuando-la-caja-no-alcanza). Lo que sí está escrito es qué pasa si el empleador quiebra. El Convenio 173 de la OIT (1992) le da a cada país dos caminos, y puede tomar los dos (art. 3):

- **Privilegio.** Los créditos laborales se pagan con los bienes del empleador antes que los acreedores comunes (art. 5), cubren como mínimo «wages relating to a prescribed period, which shall not be less than three months», vacaciones, otras ausencias pagas e indemnización (art. 6), y van por encima de casi todos los demás privilegios (art. 8).
- **Fondo de garantía.** Una institución paga los créditos cuando el empleador no puede (art. 9), como mínimo «not be less than eight weeks» de sueldo, más vacaciones e indemnización (art. 12).

En lectura de esta base, eso hace del sueldo la última deuda que conviene atrasar: si la empresa cae, se cobra antes que la de los acreedores comunes.

## El pago a demanda

El pago a demanda (*earned wage access*) le adelanta al empleado parte de lo ya trabajado antes del día de pago. La CFPB cambió cuatro veces de criterio sobre si es un crédito: una opinión de 2020, una propuesta de 2024 que lo trataba como crédito, la rescisión de la opinión de 2020 en enero de 2025 y su retiro en mayo, y una opinión del 23 de diciembre de 2025 que dice que el modelo cubierto no es crédito.

El modelo que describe la opinión de 2025 en que la empresa es socia funciona así: el proveedor adelanta hasta lo devengado según los datos de nómina y cobra con un descuento «in connection with the worker's next payroll event», que ejecuta el procesador de nómina o el propio empleador. Si el sueldo no alcanza, el proveedor no le reclama nada al trabajador. Algunos proveedores le piden al procesador que desvíe una parte del sueldo hacia ellos; otros reciben el sueldo entero y le giran al trabajador el resto.

Para la tesorería de la empresa, en lectura de esta base sobre esa opinión, el pago a demanda no adelanta su salida de caja, porque adelanta el proveedor. Lo que cambia es el archivo: parte del neto de algunos empleados va al proveedor y no a su cuenta, y la comparación del archivo con el lote tiene que contar esas líneas. La misma opinión nombra las «cash flow limitations» del empleador entre los obstáculos para pagar más seguido; en lectura de esta base, el costo de esa espera lo lleva el trabajador.
