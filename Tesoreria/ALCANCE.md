---
tema: Tesorería y finanzas de la empresa en marcha
para: entender cómo una empresa que ya opera maneja su plata real (cuánta hay, cuánta va a haber, cómo cobra, cómo paga, cómo se financia y qué riesgos cuida), para quien construye software de gestión y, en segundo lugar, para quien lo vende o lo implementa
nivel: sabe de negocio y de software, no es tesorero ni contador; no se da por sabido qué es la posición de caja, el ciclo de conversión del efectivo, la aplicación de cobros ni una corrida de pagos
escuela: la tesorería operativa de una pyme o empresa mediana, como la ordenan los libros de texto de finanzas de corto plazo y el cuerpo profesional de los tesoreros (AFP, ACT); lo propio de una empresa grande (centralización, cash pooling entre países) se dice como tal
fuera:
  - registrar lo devengado, los asientos de cobros y pagos, las cuentas corrientes como auxiliares, la previsión de incobrables, la diferencia de cambio, el estado de flujo de efectivo, el presupuesto económico, la separación de funciones y la conciliación bancaria, que son de Contabilidad; acá se enlazan
  - la pista, el consumo mensual, default alive, el plan financiero de 12 meses y las fuentes del capital inicial (bootstrapping, SAFE, capital de riesgo) de una empresa que empieza, que se quedan en Emprender/Finanzas
  - el límite de crédito y la condición de pago como datos del cliente, que se registran en Relación con clientes; quién los fija y cómo se cobra es de acá
  - el pedido al proveedor y el cruce de tres vías, que son de Compras y abastecimiento (todavía no escrito); acá se paga la factura ya aprobada
  - qué impuesto se paga y cuándo vence (incluidos el impuesto a los débitos y créditos bancarios, retenciones y percepciones), que va al tema Impuestos (todavía no escrito); acá pesa solo como salida de caja
  - cobrar online con tarjeta, billeteras y QR, su costo y sus contracargos, que están en Comercio-electronico/Pagos; la cuenta corriente de un mayorista, en Comercio-electronico/Comercio-B2B
  - el recorrido de punta a punta del pedido al cobro y de la compra al pago, que va al tema Procesos de negocio (todavía no escrito)
  - cómo lo resuelve un software (el documento de pago y sus estados, el registro de movimientos, la integración con bancos), que va al tema Software de gestión (todavía no escrito)
  - las finanzas corporativas de una empresa grande: valuación, estructura de capital, presupuesto de capital con VAN y TIR, emisión de acciones y fusiones
fuentes: []
preguntas:
  - "Estoy diseñando la pantalla de posición de caja de un sistema: ¿qué saldos tiene que mostrar, de dónde salen y en qué se diferencia de lo que dice la contabilidad?"
  - "La empresa vende bien y da ganancia pero no le alcanza la plata para pagar: ¿cómo se ve eso en el ciclo de conversión del efectivo y qué palancas hay?"
  - "Un cliente pagó una transferencia por un monto que no coincide con ninguna factura: ¿cómo se aplica el cobro y qué tiene que permitir el sistema?"
  - "¿Cómo se decide a qué cliente darle crédito, con qué límite y qué hacer cuando no paga?"
  - "Tengo que armar la corrida de pagos semanal: ¿qué se paga primero, quién aprueba y cómo se evita pagarle a una cuenta bancaria falsa?"
  - "En Argentina, ¿conviene descontar un cheque electrónico o tomar un descubierto, y dónde se pone la plata que sobra un mes?"
  - "Tengo que pagar los sueldos del mes: ¿cuándo tiene que estar la plata en la cuenta, cómo se arma la acreditación y cómo evito que un sueldo se vaya a una cuenta ajena?"
  - "En Argentina, ¿en qué cuenta se acredita el sueldo, hasta qué día se puede pagar, cuándo sale el aguinaldo y cuándo vencen las cargas?"
aprobado:
---

# Alcance: Tesorería y finanzas de la empresa en marcha

Tesorería es el tema del área «Gestión de la empresa» que trata la plata real de una empresa que ya opera: cuánta hay y dónde, cuánta va a haber, cómo entra (crédito y cobranzas), cómo sale (pagos a proveedores), cómo se consigue la que falta, dónde se pone la que sobra y qué riesgos financieros se cuidan. Sale del mapa del mundo del software de gestión (issue #94) y de sus decisiones: «Forma del árbol» (#95), «Taxonomías externas» (#96), «Huecos del árbol» (#104), «Límites entre dominios vecinos» (#98), «Procesos de punta a punta» (#99) y «Orden de armado» (#101). Es la sesión 3 de 16 (issue #110). El árbol general y los límites los aprobó la persona en el mapa (2026-11-27); el árbol de adentro del tema lo propuso esta sesión sin esperar respuesta, por indicación de quien la abrió, y queda para revisar en el PR.

Es un tema agnóstico: cierto en cualquier empresa y cualquier producto, se sostiene sin software (una planilla de caja, una chequera y un banco hacen lo mismo que un módulo de tesorería) y lo de Argentina va en una nota aparte. No nombra productos.

## Árbol

```
Tesoreria/
  tesoreria.md                    el todo: la plata real, caja frente a resultado, de qué está hecha, sus vecinos; qué leer según lo que estés haciendo
  politica-de-tesoreria.md        el documento que gobierna todo: quién decide, límites, bancos, inversiones permitidas, controles
  tesoreria-en-argentina.md       cheques y ECHEQ, transferencias, financiamiento pyme (descuento, avales), colocaciones con inflación y acceso al mercado de cambios
  tasas-de-referencia-en-argentina.md  ficha fechada: tasas de descubierto, plazo fijo, descuento de cheques e inflación de una fecha, con la fuente viva
  Caja-y-liquidez/                cuánta plata hay, dónde, por dónde se mueve y cuánta va a haber
    caja-y-liquidez                 entrada: liquidez, la posición y la proyección como las dos preguntas de la caja
    posicion-de-caja                los saldos de hoy: contable y disponible, en tránsito, comprometido; la posición diaria
    cuentas-bancarias               la estructura de cuentas, firmantes, la relación con los bancos y sus comisiones, la concentración de fondos
    medios-de-cobro-y-pago          transferencia, cheque, débito directo, tarjeta y efectivo vistos desde la caja: cuándo se acredita, cuánto cuesta, quién lo puede revertir
    proyeccion-de-caja              el pronóstico de corto plazo por semanas, el de 13 semanas, el método directo y cómo se mide si acierta
    capital-de-trabajo              el ciclo de conversión del efectivo (días de cobro, de inventario y de pago) y por qué crecer consume caja
    colocacion-de-excedentes        la reserva de liquidez y dónde se pone lo que sobra: seguridad, liquidez y rendimiento
  Credito-y-cobranzas/            cómo entra la plata que los clientes deben
    credito-y-cobranzas             entrada: vender a plazo es prestar; el ciclo del crédito al cobro
    credito-a-clientes              la política de crédito, las cinco C, el límite, las garantías y el seguro de crédito
    gestion-de-la-cobranza          la secuencia de recordatorios, la mora, las disputas y deducciones, los acuerdos de pago, el paso a legales y cómo se mide (DSO, CEI)
    aplicacion-de-cobros            identificar un cobro y aplicarlo a facturas: aviso de pago, parciales, sin identificar, anticipos, diferencias y retenciones
  Pagos-a-proveedores/            cómo sale la plata que la empresa debe
    pagos-a-proveedores             entrada: de la factura aprobada al pago, y quién decide qué se paga
    programacion-de-pagos           qué se paga cuándo: vencimientos, descuento por pronto pago, prioridades cuando no alcanza
    corrida-de-pagos                la propuesta, la aprobación, el lote, el envío al banco, las firmas y la orden de pago
    seguridad-de-los-pagos          el fraude por cambio de cuenta del proveedor, el correo comprometido, los pagos duplicados y los controles
  Pago-de-sueldos/                cómo sale la plata que se les debe a los empleados (ampliación, issue #170)
    pago-de-sueldos                 entrada: del archivo de netos a la plata en la cuenta del empleado; en qué se diferencia de pagar a un proveedor
    cuentas-y-acreditacion          la cuenta de sueldos de la empresa, la cuenta del empleado, el archivo, la acreditación, los rechazos, el cambio de cuenta y el desvío
    fondeo-y-calendario             cuándo tiene que estar la plata, el calendario del año (día de pago, feriados, aguinaldo, cargas) y qué pasa si no alcanza
    pago-de-sueldos-en-argentina    la cuenta sueldo del BCRA, la acreditación, los plazos de la LCT, el aguinaldo, el vencimiento de las cargas y la mora
  Financiamiento/                 cómo se consigue la plata que falta en una empresa que ya opera
    financiamiento                  entrada: corto o largo plazo, con o sin garantía; qué financia cada cosa
    financiamiento-de-corto-plazo   descubierto, línea de crédito, descuento de documentos y factoring
    financiamiento-de-la-cadena     el reverse factoring: cómo funciona, por qué no siempre se ve como deuda, Carillion, Greensill y lo que pide revelar el IASB
    prestamos                       el préstamo a plazo, los sistemas de amortización francés y alemán, las garantías, los covenants y el leasing
    costo-del-financiamiento        tasa nominal y efectiva, costo financiero total, tasa real y cómo se comparan alternativas
  Riesgos-financieros/            lo que puede salir mal con la plata y cómo se acota
    riesgos-financieros             entrada: liquidez, tasa y contraparte, y cómo se decide qué cubrir
    riesgo-de-tipo-de-cambio        exposición de transacción, traslación y económica; cobertura natural, forward y futuros
  Fundamentos/
    fundamentos-de-tesoreria        entrada: cómo se divide el campo, tesorería frente a contabilidad, la pyme frente a la empresa grande, mitos
    glosario-de-tesoreria           los términos del tema, con su nombre en inglés
    fuentes-de-tesoreria            dónde se produce el saber de tesorería y qué leer
```

## Límites con los vecinos

Regla del mapa (#98): cada dominio es dueño de un objeto y un verbo; un saber vive en un solo lugar y los demás enlazan. Tesorería es dueña de **la plata real** y de los verbos **cobrar, pagar, proyectar, financiar y colocar**.

| Vecino | Tesorería es dueña de | El vecino es dueño de | Ejemplo de frontera |
|---|---|---|---|
| [Contabilidad](../Contabilidad/contabilidad.md) | la posición de caja, el cobro y el pago como movimientos de plata, la proyección | registrar lo devengado, el asiento del cobro y del pago, las cuentas corrientes, la [conciliación bancaria](../Contabilidad/Control-interno/conciliaciones.md) | Tesorería ejecuta el pago; el asiento y la conciliación son de Contabilidad |
| [Emprender/Finanzas](../Emprender/Finanzas/finanzas.md) | la caja de una empresa que ya opera: semanas, no meses de pista | la pista, el consumo mensual, el plan de 12 meses y el capital inicial | el pronóstico de 13 semanas es de acá; el [plan financiero mínimo](../Emprender/Finanzas/plan-financiero-minimo.md), de Emprender |
| [Relación con clientes](../Relacion-con-clientes/relacion-con-clientes.md) | decidir el crédito y cobrar | el límite y la condición de pago como datos del cliente, y el pedido que se bloquea | Tesorería fija el límite; la [ficha del cliente](../Relacion-con-clientes/Registro-del-cliente/condiciones-comerciales.md) lo guarda |
| [Comercio-electronico/Pagos](../Comercio-electronico/Pagos/pagos.md) | el medio de cobro visto desde la caja | cobrar online: tarjeta, billeteras, QR, su costo y sus contracargos | cuánto cuesta cobrar con tarjeta es de allá; cuándo se acredita y cómo se aplica, de acá |
| [Comercio-electronico/Comercio-B2B](../Comercio-electronico/Comercio-B2B/cuenta-corriente-y-credito.md) | el crédito y la cobranza en general | la cuenta corriente en el comercio mayorista argentino | allá, cómo se ve en un distribuidor; acá, el concepto |
| [Administración de personal y nómina](../Administracion-de-personal-y-nomina/administracion-de-personal-y-nomina.md) | pagar los sueldos: la cuenta, el fondeo, la acreditación y la fecha | el legajo, la liquidación, el neto de cada uno, el recibo y las cargas que se declaran | la [liquidación](../Administracion-de-personal-y-nomina/Liquidacion-de-sueldos/liquidacion-de-sueldos.md) dice cuánto se le paga a cada uno; que la plata esté en su cuenta el día que corresponde es de acá |
| Compras y abastecimiento (no escrito) | pagar | el pedido, la recepción y el cruce de tres vías | Compras aprueba que se deba; Tesorería decide cuándo y cómo se paga |
| Impuestos (no escrito) | el impuesto como salida de caja en la proyección | qué se paga, cuándo vence y cómo se declara | la fecha del vencimiento es de Impuestos; tener la plata ese día, de acá |
| Procesos de negocio (no escrito) | cada paso de cobrar y pagar | los recorridos del pedido al cobro y de la compra al pago | el recorrido es del proceso; la aplicación del cobro, de acá |
| Software de gestión (no escrito) | el saber de tesorería, que existe sin software | el documento de pago, la integración con bancos y el registro de movimientos como columnas técnicas | la corrida de pagos se explica acá; cómo se modela, allá |

Los temas que todavía no existen se nombran sin enlace; la sesión 16 del mapa los enlaza.

## Supuestos

- **Cinco verticales** (seis desde la ampliación de Pago de sueldos). Caja y liquidez, Crédito y cobranzas, Pagos a proveedores, Financiamiento y Riesgos financieros. Siguen los capítulos de finanzas de corto plazo de los libros de texto (caja, cuentas a cobrar, cuentas a pagar, financiamiento de corto plazo) y la categoría 9.7 de APQC (gestión de caja, deuda e inversiones, riesgo financiero). Crédito y cobranza están en APQC 9.2 (contabilidad de ingresos) y los pagos en 9.6: el corte de esta base los pone en Tesorería porque el mapa (#98) le dio a Tesorería cobrar y pagar, y a Contabilidad registrar.
- **Tesorería y no «finanzas».** El nombre del mapa es «Tesorería y finanzas de la empresa en marcha»; la carpeta y el título corto son «Tesorería», y «finanzas de la empresa en marcha» va como alias.
- **La colocación de excedentes va en Caja y liquidez**, junto con la reserva, y no en Financiamiento: es la otra cara de la misma pregunta (cuánta caja tener).
- **Lo de Argentina, en una nota y una ficha** en la raíz del tema, porque tocan las cinco verticales: la nota explica los instrumentos y las reglas; la ficha guarda las tasas de una fecha, que cambian cada semana.
- **Cambios después de investigar** (2026-11-27). La política de tesorería sube a nota del todo, al lado de la entrada, porque APQC la pone primera (9.7.1) y gobierna las cinco verticales. Los medios de cobro y los de pago son los mismos rieles vistos de dos lados: van en una sola nota de Caja y liquidez, que es donde pesa cuándo se acredita la plata. El financiamiento de la cadena (reverse factoring) tiene nota propia, por su riesgo y por la enmienda del IASB de 2023. Las disputas y deducciones (APQC 9.2.5) van en gestión de la cobranza, y el aviso de pago en aplicación de cobros. La relación con los bancos y sus comisiones (APQC 9.7.2.7 y 9.7.2.8) va en cuentas bancarias.
- **El riesgo de tasa y el de contraparte no tienen nota propia**: van en la entrada de Riesgos financieros, porque en una pyme se resuelven con dos decisiones (tasa fija o variable; en qué bancos y con qué límite). El banco interno, el netting y la cobertura formal se nombran como cosa de empresa grande.
- **Fuentes flacas.** El cupo de búsqueda web se agotó en las dos rondas de investigación. Muchos componentes se apoyan en OpenStax, APQC, la Credit Research Foundation, el FBI y AFP, y en Wikipedia marcada como tal; lo que no tuvo fuente queda en cada nota como «sin fuente todavía».
- **Pago de sueldos, sexta vertical** (ampliación del 2026-11-27, issue #170). El pago de sueldos no entra en Pagos a proveedores: no se elige la fecha, no se renegocia, se paga a muchas personas a la vez y la ley fija el medio y el plazo. APQC también lo separa: la nómina (9.5) no está en cuentas a pagar (9.6). Va como vertical propia, al lado de Pagos a proveedores, y lo de Argentina en una nota dentro de ella, porque toca solo esta vertical. La sesión no esperó respuesta sobre el árbol, por indicación de quien la abrió, y queda para revisar en el PR.
- **Lo que queda pendiente para otra sesión**: Contabilidad, Relación con clientes y Emprender dicen hoy «Tesorería, todavía no escrito»; pasan a enlazar este tema en la sesión 16 (#101).
