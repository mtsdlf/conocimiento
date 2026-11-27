---
resumen: >-
  La aplicación de cobros es identificar de qué cliente es cada cobro que llega y asignarlo a las facturas que cancela, dejando a la vista lo que sobra, lo que falta y lo que no se sabe de quién es.
estado: borrador
estabilidad: semi
fuentes:
  - "APQC, Process Classification Framework 7.4 (2024), 9.2.3 y 9.2.5 (leído, los títulos): https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "APQC, Accounts Receivable and Collections: Key Benchmarks, definición de 9.2.3 (según su resumen): https://www.apqc.org/resource-library/resource-collection/accounts-receivable-and-collections-key-benchmarks"
  - "Wikipedia, Remittance advice (según su resumen): https://en.wikipedia.org/wiki/Remittance_advice"
  - "ERPNext, Payment Entry (como evidencia de práctica): https://docs.frappe.io/erpnext/user/manual/en/payment-entry"
  - "ERPNext, Payment Reconciliation (como evidencia de práctica): https://docs.frappe.io/erpnext/user/manual/en/payment-reconciliation"
  - "Tesoreria/.investigacion/credito-y-cobranzas.md, sección 3 (2026-11-27)"
  - "Tesoreria/.investigacion/caja-y-cobranzas-segunda-ronda.md, sección 7 (2026-11-27)"
  - "Tesoreria/.investigacion/credito-y-cobranzas-verificacion.md (2026-11-27)"
aliases: [aplicación de cobros, cash application, aplicar cobros, imputación de cobros, apply cash remittances, aviso de pago, remittance advice, remesa, detalle de pago, cobro sin identificar, unapplied cash, unidentified receipts, pago parcial, partial payment, anticipo de cliente, customer advance, pago corto, short payment]
creado: 2026-11-27
revisado:
---

# Aplicación de cobros

La aplicación de cobros es identificar de qué cliente es cada cobro que llega y asignarlo a las facturas que cancela, dejando a la vista lo que sobra, lo que falta y lo que no se sabe de quién es.

Es el último paso de [crédito y cobranzas](credito-y-cobranzas.md) y el que hace ciertos a los demás. Mientras un cobro no está aplicado, la cuenta corriente del cliente muestra facturas abiertas que ya se pagaron: la [gestión de la cobranza](gestion-de-la-cobranza.md) le reclama a quien pagó, el pedido nuevo se bloquea por un [límite de crédito](credito-a-clientes.md) que en realidad tiene margen, y la antigüedad de saldos miente (lectura de esta base).

## Lo que es de tesorería y lo que es de contabilidad

APQC separa los pasos dentro de 9.2.3 «Process accounts receivable (AR)»: recibir y depositar los pagos de los clientes (9.2.3.2), aplicar las remesas (9.2.3.3, «Apply cash remittances»), preparar los informes (9.2.3.4) y pasar la actividad al mayor (9.2.3.5). Según el resumen de su página de indicadores, el proceso incluye todo el tratamiento de los fondos recibidos, por cheque o por medio electrónico, y no incluye emitir facturas.

Esta base toma esa separación como frontera. Aplicar el cobro a facturas es de tesorería. El asiento del cobro es de la contabilidad, en [ingresos y cuentas a cobrar](../../Contabilidad/Operaciones/ingresos-y-cuentas-a-cobrar.md), y la comparación de los libros con el extracto es la [conciliación bancaria](../../Contabilidad/Control-interno/conciliaciones.md). Que un cobro se aplique a facturas concretas, y no solo al saldo, es lo que permite calcular la antigüedad por comprobante, uno de los requisitos que [cuentas corrientes](../../Contabilidad/Registro/cuentas-corrientes.md) le pone a un sistema.

## El aviso de pago

El aviso de pago (remittance advice) es la comunicación del cliente que informa que pagó y qué facturas cubre. Según el resumen de una enciclopedia abierta, debería indicar los números de factura que se pagan, y los avisos modernos pueden listar decenas o cientos de facturas en un solo pago. Si el cliente no lo manda, alguien de la empresa lo reconstruye.

Como lectura de esta base, el aviso suele viajar separado de la plata: el dinero llega por el banco y el detalle, por correo, por un portal o en el concepto de la transferencia. Cuándo se acredita cada medio está en [medios de cobro y pago](../Caja-y-liquidez/medios-de-cobro-y-pago.md).

## Los casos que el sistema tiene que prever

La documentación de un sistema de gestión abierto, leída como evidencia de práctica, muestra los casos que aparecen al aplicar:

| Caso | Qué pasa | Cómo lo trata ese sistema |
|---|---|---|
| Cobro exacto | El cobro iguala una o varias facturas | Se asigna y las facturas quedan canceladas |
| Cobro parcial | El cobro es menor que la factura | Propone asignar el menor entre el saldo de la factura y el del cobro; la factura queda con saldo |
| Cobro de más o anticipo | Sobra plata o no hay factura todavía | El resto queda sin asignar y disponible para aplicarlo después; hay una cuenta de anticipos por defecto |
| Sin elegir factura | El cobro no dice qué cancela | Asigna por antigüedad, primero la factura más vieja |
| Diferencia | Cobro y aplicación no coinciden | Muestra el monto de diferencia para revisarlo antes de confirmar |
| Aplicación equivocada | Se imputó a la factura o al cliente que no era | Se desaplica y se vuelve a conciliar |

Una regla atraviesa la tabla: el monto asignado no puede superar ni el saldo de la factura ni el del cobro.

### Las diferencias van a una cuenta con nombre

Cuando el cliente paga menos por una comisión bancaria, una retención, una diferencia de cambio o un redondeo chico, ese sistema manda la diferencia a una línea de deducciones o pérdidas con su cuenta explícita. Las comisiones no se cargan como impuestos o cargos del cliente, porque no es plata que se le pagó al cliente. El castigo de una deuda incobrable no se hace en el cobro: va por un asiento aparte, como cuenta [ingresos y cuentas a cobrar](../../Contabilidad/Operaciones/ingresos-y-cuentas-a-cobrar.md).

Una diferencia que el cliente descontó a propósito (una devolución, una diferencia de precio) es una deducción, y su gestión está en [disputas y deducciones](gestion-de-la-cobranza.md#disputas-y-deducciones). La lectura de esta base es que la aplicación tiene que distinguir las dos: una diferencia que se acepta y se cierra, y una deducción que queda abierta con motivo hasta que se resuelve.

### Las retenciones sufridas

En Argentina, un cliente que actúa como agente de retención paga neto y la diferencia es un impuesto retenido, no una deuda perdonada: la factura se cancela con la plata más el comprobante de la retención (lectura de esta base). Qué retenciones existen y cómo se acreditan está en [tesorería en Argentina](../tesoreria-en-argentina.md); qué impuesto es y cuándo se computa es del tema Impuestos, todavía no escrito.

> [!NOTE] Sin fuente todavía: cómo se aplica una retención sufrida (si cancela la factura al recibir el certificado o al validarlo) y qué pasa cuando el certificado no llega.

## El cobro sin identificar

Un cobro sin identificar es plata que entró al banco sin que se sepa de qué cliente es o qué cancela. Es el hueco de fondo del componente: ninguna fuente profesional leída explica cómo se empareja un cobro sin referencia, qué se hace con lo que no se empareja ni cuánto tiempo puede quedar así.

Lo que sigue es lectura de esta base, sin fuente:

- El emparejamiento usa, en orden, la referencia que el cliente escribió, la identificación del ordenante (en Argentina, su CUIT en la transferencia) y el monto contra las facturas abiertas.
- Lo que no se empareja va a una cuenta transitoria de cobros sin identificar, a nombre de nadie, y se revisa con una frecuencia fija. Dejarlo a cuenta de un cliente «probable» ensucia su saldo.
- La conciliación bancaria lo encuentra si nadie lo registró, pero no dice de quién es: eso lo resuelve tesorería, consultando al cliente.

> [!NOTE] Sin fuente todavía: una fuente profesional (AFP, ACT o un libro de texto) sobre emparejamiento de cobros, tratamiento de los no identificados y plazos de resolución. Una segunda pasada no encontró ninguna: ni OpenStax ni las guías de la CRF y la Comisión Europea tratan el tema, y la AFP y la ACT quedaron sin consultar.

## Los cheques y el momento de aplicar

Un cheque a fecha, físico o electrónico, se recibe hoy y se acredita después. Hay que decidir si cancela la factura al recibirlo o al acreditarse, y qué pasa si lo rechazan. La conciliación de [conciliaciones](../../Contabilidad/Control-interno/conciliaciones.md) muestra el caso del rechazo: la deuda del cliente renace, porque el cobro registrado no existió. Una lectura de esta base: si el cheque cancela la factura al recibirse, tiene que seguir contando en la exposición del cliente hasta que se acredite, como dice [crédito a clientes](credito-a-clientes.md#cómo-se-evalúa-al-cliente-y-cómo-se-fija-el-límite). El ECHEQ y sus plazos están en [tesorería en Argentina](../tesoreria-en-argentina.md).

## Cómo falla la aplicación

- Aplicar a cuenta. El cobro baja el saldo del cliente pero no cancela ninguna factura: la antigüedad sigue mostrando deuda vieja y la cobranza la reclama.
- Aplicar tarde. Entre que entra la plata y se aplica, el cliente figura moroso. El lote diario de cobros sin aplicar es el número a mirar.
- Cerrar diferencias sin motivo. Si cualquier diferencia se castiga contra una cuenta de redondeo, las deducciones que había que discutir desaparecen.

Las tres son lectura de esta base. La [proyección de caja](../Caja-y-liquidez/proyeccion-de-caja.md) también las sufre, porque estima los cobros sobre las facturas abiertas.
