---
resumen: >-
  El sueldo sale de una cuenta de la empresa y llega a una cuenta que elige el empleado, en un lote que el banco reparte; la tesorería cuida que la plata salga de la cuenta correcta, que cada destino sea de verdad del empleado, que el empleado la tenga el día de pago y que lo rechazado o pagado por error se corrija.
estado: borrador
estabilidad: semi
fuentes:
  - "Nacha, RMAG Originator Essentials (2024), guía para quien origina pagos (leída completa): https://www.nacha.org/sites/default/files/2024-10/RMAG_Originator_Essentials.pdf"
  - "Nacha, regla Providing Faster Funds Availability (efectiva el 20/09/2019) (leída): https://www.nacha.org/rules/providing-faster-funds-availability"
  - "Nacha, regla Funds Availability Requirements for Non-Same Day Credit Entries (efectiva el 18/09/2026) (leída): https://www.nacha.org/rules/funds-availability-requirements-non-same-day-credit-entries"
  - "Nacha, regla Reversals and Enforcement y su End-user Briefing: Reversals (emitido el 4/05/2021, efectiva el 30/06/2021) (leídas): https://www.nacha.org/rules/reversals-and-enforcement"
  - "Nacha, regla Company Entry Descriptions (efectiva el 20/03/2026) (leída): https://www.nacha.org/rules/risk-management-topics-company-entry-descriptions"
  - "Nacha, regla Fraud Monitoring Phase 1 y página de novedades de reglas (leídas): https://www.nacha.org/rules/risk-management-topics-fraud-monitoring-phase-1"
  - "Nacha, pedido de información sobre el día bancario y la prenotificación (según un fragmento del buscador; la página pide login): https://www.nacha.org/rules/request-information-definition-banking-day-and-related-operational-topics"
  - "Documentación de devoluciones ACH de un banco de plataforma (leída; repite las definiciones de Nacha): https://increase.com/documentation/ach-returns"
  - "European Payments Council, SEPA Credit Transfer Scheme Rulebook 2025 v1.0 (EPC125-05), secciones 4.2.3, 4.3.2 y AT-T008 (leídas): https://europeanpaymentscouncil.eu/sites/default/files/kb/file/2024-11/EPC125-05%202025%20SCT%20Rulebook%20version%201.0.pdf"
  - "ISO 20022, listas externas de códigos de propósito, en una transcripción publicada como paquete (leída; el sitio oficial devolvió error): https://cdn.jsdelivr.net/npm/@taprsvp/iso20022_external_codes@1.0.1/dist/CategoryPurpose.d.ts"
  - "Guía de un banco nórdico sobre la categoría de propósito en pagos de sueldos (leída): https://knowledge.xmldation.com/support/nordea/ctgypurp"
  - "OpenStax, Principles of Financial Accounting, 8.4, caja chica (leído): https://openstax.org/books/principles-financial-accounting/pages/8-4-define-the-purpose-and-use-of-a-petty-cash-fund-and-prepare-petty-cash-journal-entries"
  - "FBI IC3, alerta I-091818-PSA del 18/09/2018 sobre desvío de sueldos (leída): https://www.ic3.gov/PSA/2018/PSA180918"
  - "FBI IC3, alerta PSA190910 del 10/09/2019, Business Email Compromise The $26 Billion Scam (leída la parte de nómina): https://www.ic3.gov/PSA/2019/PSA190910"
  - "ACFE, Occupational Fraud 2024: A Report to the Nations (leídas las tablas de esquemas de nómina): https://www.acfe.com/-/media/files/acfe/pdfs/rttn/2024/2024-report-to-the-nations.pdf"
  - "Regulation E, 12 CFR 1005.10(e)(2) y 1005.18(b)(2)(xiv)(A), eCFR al 1/11/2026 (leído): https://www.ecfr.gov/current/title-12/chapter-X/part-1005"
  - "Documentación de recibos de sueldo de un sistema de gestión abierto, versión 18 (leída; como evidencia de práctica): https://www.odoo.com/documentation/18.0/applications/hr/payroll/payslips.html"
  - "Tesoreria/.investigacion/pago-de-sueldos.md, secciones 1, 2, 5 y 6 (2026-11-27)"
aliases: [cuenta de sueldos, payroll account, cuenta pagadora de sueldos, cuenta de saldo cero, zero balance account, depósito directo, direct deposit, acreditación de sueldos, prenotificación, prenote, rechazo de un pago, ACH return, reversa, reversal, desvío de sueldos, payroll diversion, empleado fantasma, ghost employee, tarjeta de nómina, payroll card, SALA]
creado: 2026-11-27
revisado:
---

# Cuentas y acreditación

El sueldo sale de una cuenta de la empresa y llega a una cuenta que elige el empleado, en un lote que el banco reparte; la tesorería cuida que la plata salga de la cuenta correcta, que cada destino sea de verdad del empleado, que el empleado la tenga el día de pago y que lo rechazado o pagado por error se corrija.

Es la mitad mecánica del [pago de sueldos](pago-de-sueldos.md); la otra mitad, cuándo tiene que estar la plata, está en [fondeo y calendario](fondeo-y-calendario.md). Las fuentes con más detalle son las reglas de la red de pagos entre bancos de Estados Unidos, que escribe Nacha, y el reglamento de las transferencias europeas (SEPA); sirven como ejemplo de cómo funciona cualquier red. Lo de Argentina está en [pago de sueldos en Argentina](pago-de-sueldos-en-argentina.md).

## La cuenta de la que sale el sueldo

Una cuenta separada para sueldos es una de las cuentas por uso que describe [cuentas bancarias](../Caja-y-liquidez/cuentas-bancarias.md#para-qué-se-abre-cada-cuenta). La idea es la del fondo fijo: OpenStax define la caja chica como «a type of imprest account», con un monto fijo que se repone a medida que se gasta (8.4). En lectura de esta base, aplicada a una cuenta de sueldos, la empresa le transfiere el neto exacto del lote, el lote la vacía y la cuenta vuelve a cero; así su extracto trae solo sueldos y cualquier débito que no sea del lote salta a la vista.

> [!NOTE]
> Sin fuente todavía: una fuente primaria que defina la cuenta de sueldos de fondo fijo o la cuenta de saldo cero aplicada a sueldos, y que explique por qué se separa. Lo de arriba es lectura de esta base sobre la definición de caja chica.

Separada o no, el banco puede pedir la plata antes. Nacha llama prefondeo a que la empresa no pueda mandar un archivo de créditos mayor que su saldo disponible, y aclara que «Prefunding is not an exposure limit and does not control fraud risks or the risk of returns». Aparte, el banco le fija a cada empresa un límite de exposición: cuánto puede mandar en un período (*RMAG Originator Essentials*, 2024). El banco debita la cuenta de la empresa por pago, por lote o por archivo. En lectura de esta base, si es por archivo, el extracto muestra un solo débito por todos los sueldos, y la conciliación lo reparte como en la [corrida de pagos](../Pagos-a-proveedores/corrida-de-pagos.md#lo-que-el-banco-devuelve).

## La cuenta del empleado y cómo se valida

La cuenta destino la elige el empleado y queda en su [legajo](../../Administracion-de-personal-y-nomina/Legajo/legajo.md), cargada en el alta ([ingreso y egreso](../../Administracion-de-personal-y-nomina/Legajo/ingreso-y-egreso.md#lo-que-deja-hecho-el-alta)). En Estados Unidos, la Regulation E prohíbe exigir una cuenta en un banco determinado como condición de empleo (12 CFR 1005.10(e)(2)). Si el empleador ofrece una tarjeta de nómina, el folleto tiene que decir primero «You do not have to accept this payroll card», o listar las otras formas de cobro (1005.18(b)(2)(xiv)(A)).

Antes del primer pago a una cuenta nueva conviene validarla. Nacha nombra tres métodos: «Prenotes, Micro-Deposits, or a commercial verification system». La prenotificación es un registro de prueba que se manda antes del primer pago; según un fragmento de una página de Nacha que pide login, después hay que esperar tres días hábiles antes de pagar. En lectura de esta base sobre la guía de Nacha, sin la regla leída, para sueldos la validación es opcional: la regla que la exige es para otro tipo de débitos.

El pago se marca como sueldo. Desde el 20 de marzo de 2026, Nacha exige la descripción «PAYROLL» en los créditos de sueldos, para «reduce the incidence of fraud involving payroll redirections». En los mensajes ISO 20022 el código de categoría de propósito es SALA, «Transaction is the payment of salaries», y hay otro para el bono, BONU. Un banco nórdico exige SALA en sus pagos de sueldos; qué tratamiento distinto les da cada banco no se encontró.

## Cuándo tiene la plata el empleado

En la red de Estados Unidos, desde 2019 un crédito que no es del mismo día tiene que estar disponible «by 9:00 a.m. RDFI's local time on Settlement Date» (a las 9 de la mañana, hora del banco del empleado, el día en que los bancos se liquidan el pago entre ellos), si el banco del empleado lo recibió antes de las 5 de la tarde del día anterior. Desde el 18 de septiembre de 2026 esa condición de las 5 de la tarde desaparece, y Nacha nombra la nómina entre los pagos que se benefician. En SEPA, el banco del ordenante tiene que acreditar al banco del beneficiario dentro de un día hábil bancario desde que recibe la orden (4.2.3).

Para la tesorería eso fija el último momento útil, en lectura de esta base: el día en que los bancos se liquidan el pago tiene que ser, a más tardar, el día de pago. Cuánto antes hay que mandar el archivo está en [fondeo y calendario](fondeo-y-calendario.md#cuándo-tiene-que-estar-la-plata).

## Lo que vuelve: rechazos, cambios y reversas

El banco del empleado devuelve lo que no puede acreditar, con un código. Los que aparecen en sueldos, según un banco de plataforma que repite las definiciones de Nacha:

| Código | Qué pasó |
|---|---|
| R02 | La cuenta se cerró |
| R03 | El número de cuenta no corresponde a la persona del registro |
| R04 | El número de cuenta está mal o mal formado |
| R16 | El banco restringió el acceso a la cuenta |
| R20 | La cuenta no admite ese movimiento |

Un crédito rechazado vuelve a la cuenta de la empresa y el empleado no cobró: en lectura de esta base, hay que pagarle de nuevo por otro carril antes de que venza el plazo. Si el dato es viejo pero el banco pudo acreditar, devuelve un aviso de cambio, y la empresa tiene que corregir la cuenta «within six banking days or prior to initiating another Entry, whichever is later». En SEPA, el banco del beneficiario devuelve a más tardar tres días hábiles después de la liquidación.

Un pago de sueldo mandado por error se puede reversar solo en cuatro casos, según la regla de Nacha de 2021: pago duplicado, cuenta distinta de la que se quería, monto equivocado, o un crédito procesado más tarde de lo previsto. La página de la regla suma ciertos créditos por desvinculación; el resumen oficial no los lista, y no se leyó el texto de la regla. La reversa tiene que llegar «within 5 banking days following the Settlement Date». Tiene tres límites:

- La falta de fondos no se arregla con una reversa: «Failure to fund is not an error».
- El banco del empleado puede devolver la reversa por fondos insuficientes. En lectura de esta base, eso pasa si el empleado ya sacó la plata, y entonces el recupero pasa a la liquidación como un descuento acordado o un reclamo.
- En SEPA el pedido de anulación vale solo por envío duplicado, error técnico (diez días hábiles) o fraude (trece meses); comparando las dos reglas, un monto equivocado no está entre los motivos de SEPA.

## El desvío de sueldos

El desvío de sueldos es el fraude en que alguien cambia la cuenta de un empleado para cobrar su sueldo. El FBI lo describió en 2018: con un correo de phishing obtienen la contraseña del empleado, muchas veces en un sitio que imita el de Recursos Humanos, cambian la cuenta de depósito y crean reglas para que el empleado no vea los avisos. La variante de 2019 llega a Recursos Humanos como un correo falso «appearing to be from employees requesting a change to their direct deposit account». Entre enero de 2018 y junio de 2019 el FBI recibió 1.053 denuncias, con pérdidas por 8.323.354 dólares y un promedio de 7.904 por denuncia. El informe del FBI de 2025 no separa la nómina, y no hay cifra más nueva.

Lo que recomienda el FBI: credenciales de nómina distintas de las de otros sistemas, «heightened scrutiny» sobre los cambios de cuenta que piden los empleados, vigilar los ingresos fuera de horario y doble factor en los sistemas sensibles. Desde 2026 las reglas de Nacha nombran la «payroll impersonation» entre los fraudes que los bancos receptores tienen que intentar detectar.

El control principal es el mismo que para el cambio de cuenta de un proveedor en [seguridad de los pagos](../Pagos-a-proveedores/seguridad-de-los-pagos.md): confirmar el cambio por un canal distinto del que trajo el pedido. Aplicarlo al empleado es inferencia de esta base, que ya hace el recorrido [de la contratación a la baja](../../Procesos-de-negocio/de-la-contratacion-a-la-baja.md#lo-que-pasa-de-un-dominio-a-otro). Un sistema de gestión abierto bloquea el pago a una cuenta de empleado que no está marcada como confiable.

## Los empleados fantasma

El otro fraude es interno. La ACFE llama esquema de nómina al de un empleado que hace que la empresa pague compensaciones falsas, como horas extra no trabajadas o un empleado fantasma en la nómina. En su informe de 2024 son 190 casos, el 10 % del total, con una pérdida mediana de 50.000 dólares y 18 meses hasta que se detectan. Pesan más en las organizaciones de menos de 100 empleados (14 % de sus casos, contra 9 % en las más grandes).

Contra eso, en lectura de esta base y sin fuente con método leída, sirven tres cosas: comparar la suma del archivo con el total de netos del lote cerrado, comparar cada cuenta del archivo con la del legajo y buscar dos empleados que cobran en la misma cuenta, y que quien carga empleados no libere el pago. La separación de funciones en sueldos es de [separación de funciones](../../Contabilidad/Control-interno/separacion-de-funciones.md), que también marca que falta un catálogo por ciclo.

> [!NOTE]
> Sin fuente todavía: una guía neutral (de auditoría interna o de un regulador) con los controles del archivo de sueldos, y el texto completo de la regla de reversas de Nacha.
