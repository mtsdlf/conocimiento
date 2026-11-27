---
tema: Impuestos
para: entender qué impuestos alcanzan a una empresa que ya opera, cómo se determinan, quién los cobra y qué tiene que hacer la empresa cada mes para cumplir, para quien construye software de gestión y, en segundo lugar, para quien lo vende o lo implementa
nivel: sabe de negocio y de software, no es contador ni abogado tributarista; no se da por sabido qué es un crédito fiscal, una retención o una declaración jurada
escuela: neutral; el núcleo sigue la división de los manuales de administración tributaria (la obligación, los impuestos por lo que gravan, la recaudación en la fuente y el cumplimiento), y lo de Argentina va en notas aparte
fuera:
  - las decisiones de una vez al empezar una empresa (qué forma legal, inscribirse, elegir el monotributo), que se quedan en Emprender/Legal-e-impuestos; acá va lo recurrente (recategorizar, liquidar, declarar)
  - cómo se registra un impuesto en la contabilidad (las cuentas de IVA débito y crédito, la provisión de Ganancias, el impuesto diferido), que es del tema Contabilidad
  - la liquidación de sueldos, los aportes y las contribuciones a la seguridad social, que van al tema Administración de personal y nómina; acá solo el empleador como agente de retención
  - la aduana como trámite y la logística del comercio exterior, que van al tema Cadena de suministro y logística; acá solo lo que el comercio exterior paga y cómo se factura
  - pagar los impuestos y manejar la caja que piden, que es del tema Tesorería y finanzas de la empresa en marcha; acá cuánto y cuándo
  - el recorrido de cierre entre áreas, que es del tema Procesos de negocio, en «del registro al balance»
  - cómo lo resuelve un software (la alícuota como dato con vigencia, el motor de impuestos, la conexión con el fisco), que va al tema Software de gestión; la factura electrónica de ARCA como implementación ya está en Comercio-electronico/Normativa
  - la planificación fiscal agresiva, la fiscalidad internacional de grupos (precios de transferencia, BEPS) y el derecho tributario procesal como profesión
  - los impuestos de las personas que no son una empresa (Bienes Personales, Ganancias de un empleado), salvo como mención
fuentes: []
preguntas:
  - "Estoy diseñando la factura de un sistema: ¿qué impuestos lleva cada renglón, de qué depende la alícuota y qué pasa con un descuento o una nota de crédito?"
  - "¿Cómo funciona el IVA de punta a punta, por qué la empresa no lo «paga» y qué es un saldo a favor que no se puede usar?"
  - "Un cliente me retuvo una parte de la factura: ¿qué es una retención, en qué se diferencia de una percepción y qué tengo que hacer con el certificado?"
  - "¿Qué tiene que hacer una empresa todos los meses para estar al día con el fisco, y qué pasa si se atrasa?"
  - "Tengo un monotributo y facturé más: ¿cuándo tengo que recategorizarme y qué pasa si me paso del tope?"
  - "Vendo a clientes de varias provincias: ¿cómo se reparte Ingresos Brutos y qué son SIRCREB y SIRTAC?"
aprobado: 2026-11-27
---

# Alcance: Impuestos

Impuestos es el segundo tema del área «Gestión de la empresa»: qué impuestos alcanzan a una empresa que ya opera, cómo se calcula cada uno, quién los cobra y cómo se cumple con el fisco mes a mes. Sale del mapa del mundo del software de gestión (issue #94) y de sus decisiones: «Forma del árbol» (#95), «Huecos del árbol» (#104), «Límites entre dominios vecinos» (#98), «Procesos de punta a punta» (#99) y «Orden de armado» (#101). Es la sesión 2 de 16 (issue #109). El árbol general y los límites los aprobó la persona en el mapa (2026-11-27); el árbol de adentro del tema lo propuso quien escribe y queda para revisar en el PR.

Es un tema agnóstico: cierto en cualquier país y cualquier producto, se sostiene sin software y lo de Argentina va en notas aparte (las que terminan en `-en-argentina`, más `monotributo-en-marcha` e `ingresos-brutos`, que solo existen allá). No nombra productos.

## Árbol

```
Impuestos/
  impuestos.md                    el todo: qué es un impuesto para una empresa, de qué está hecho el tema, sus vecinos; qué leer según lo que estés haciendo
  impuestos-en-argentina          el mapa argentino: impuestos nacionales, provinciales y municipales, ARCA, clave fiscal y el calendario de vencimientos
  comercio-exterior-en-argentina  derechos de exportación, percepciones en la aduana y factura E (pedido por #104)
  Obligacion-tributaria/          cómo nace un impuesto y a quién le toca pagarlo
    obligacion-tributaria           entrada: la relación entre el fisco y quien paga, y sus elementos
    hecho-imponible-y-base          el hecho que hace nacer el impuesto, la base, la alícuota, el período y la exención
    sujetos-del-impuesto            contribuyente, responsable y agente; residencia, jurisdicción y doble imposición
    regimen-simplificado            el régimen para pequeños contribuyentes: una cuota en lugar de varios impuestos, categorías y topes
    monotributo-en-marcha           Argentina: recategorizar, la exclusión y el paso al régimen general (recibe de Emprender)
  Impuestos-al-consumo/           los que gravan lo que se vende
    impuestos-al-consumo            entrada: valor agregado, venta minorista, en cascada y específicos; quién los soporta
    iva                             débito y crédito fiscal, exento frente a tasa cero, prorrata, saldo a favor
    impuesto-a-las-ventas           el impuesto a la venta final y el que se cobra en cada etapa (en cascada)
    lugar-de-la-operacion           origen o destino: importaciones, exportaciones y servicios digitales
    iva-en-argentina                alícuotas, crédito fiscal y prorrata, saldos, IVA Simple de los inscriptos y el Libro de IVA Digital de los exentos
    ingresos-brutos                 el impuesto provincial sobre lo facturado, el convenio multilateral y el monotributo unificado
  Impuestos-a-la-renta/           los que gravan la ganancia
    impuestos-a-la-renta            entrada: sociedades y personas, residencia y renta de fuente, anticipos
    resultado-impositivo            del resultado contable al impositivo: ajustes, diferencias permanentes y temporarias, quebrantos
    ganancias-en-argentina          Ganancias de sociedades: alícuotas, anticipos, ajuste por inflación impositivo
  Recaudacion-en-la-fuente/       cuando un tercero cobra el impuesto por adelantado
    recaudacion-en-la-fuente        entrada: retención y percepción, por qué existen
    agente-de-recaudacion           lo que hace quien retiene o percibe: padrones, cálculo, certificado, depósito
    pagos-a-cuenta                  lo que hace quien sufre la retención: computarla, acumular saldo a favor, pedir la exclusión
    retenciones-y-percepciones-en-argentina  regímenes de IVA, Ganancias e Ingresos Brutos, SIRCREB, SIRTAC y certificados
  Cumplimiento/                   lo que la empresa hace cada período para estar al día
    cumplimiento                    entrada: el ciclo de facturar, registrar, liquidar, declarar y pagar
    comprobante-fiscal              qué lleva una factura, numeración, nota de crédito y los modelos de factura electrónica
    declaracion-y-pago              liquidar, declarar, vencimientos, anticipos, saldo a favor y compensación
    registros-fiscales              libros de IVA, conservación y entrega de datos al fisco
    fiscalizacion-y-sanciones       inspección, intereses, multas, prescripción y planes de pago
  Fundamentos/
    fundamentos-de-impuestos        entrada: historia (del IVA, sobre todo), principios de un buen impuesto, posiciones contrarias y mitos
    glosario-de-impuestos           los términos del tema, con su nombre en inglés
    fuentes-de-impuestos            dónde se produce el saber tributario y qué leer
```

La factura electrónica de ARCA no tiene nota acá: ya está en [Comercio-electronico/Normativa/factura-electronica-de-arca.md](../Comercio-electronico/Normativa/factura-electronica-de-arca.md), y `comprobante-fiscal` y `impuestos-en-argentina` la enlazan.

## Límites con los vecinos

Regla del mapa (#98): cada dominio es dueño de un objeto y un verbo; un saber vive en un solo lugar y los demás enlazan.

| Vecino | Impuestos es dueño de | El vecino es dueño de | Ejemplo de frontera |
|---|---|---|---|
| [Emprender/Legal-e-impuestos](../Emprender/Legal-e-impuestos/legal-e-impuestos.md) | lo recurrente: recategorizar, liquidar, declarar, retener | las decisiones de una vez: forma legal, inscripción, elegir el monotributo | elegir el monotributo es de Emprender; recategorizarse en febrero, de acá |
| [Contabilidad](../Contabilidad/contabilidad.md) | qué se paga, sobre qué base, cuándo y cómo se declara | el asiento del impuesto (IVA débito y crédito, provisión de Ganancias, impuesto diferido) | la alícuota del IVA es de acá; la cuenta «IVA crédito fiscal», de Contabilidad |
| [Tesorería y finanzas de la empresa en marcha](../Tesoreria/tesoreria.md) | cuánto se debe y cuándo vence | el pago, la caja para pagarlo y el plan de pagos como financiamiento | el vencimiento del IVA es de acá; tener la plata ese día, de Tesorería |
| [Administración de personal y nómina](../Administracion-de-personal-y-nomina/administracion-de-personal-y-nomina.md) | el empleador como agente de retención del impuesto a la renta del empleado | la liquidación de sueldos, aportes y contribuciones | la retención de Ganancias sobre el sueldo se explica acá como régimen; su cálculo en el recibo, allá |
| [Relación con clientes](../Relacion-con-clientes/relacion-con-clientes.md) | qué impuesto lleva cada renglón y qué condición fiscal del cliente lo decide | el presupuesto y el pedido, con el dato fiscal en la ficha del cliente | la condición frente al IVA se guarda en la ficha (allá); qué cambia en la factura, acá |
| [Cadena de suministro y logística](../Cadena-de-suministro-y-logistica/cadena-de-suministro-y-logistica.md) | el impuesto que paga una importación o una exportación | el trámite de aduana, el despacho y el transporte | el derecho de exportación es de acá; la destinación aduanera, de Cadena |
| [Comercio electrónico](../Comercio-electronico/comercio-electronico.md) | el impuesto y el régimen en general | cómo los aplica una tienda online (factura electrónica de ARCA, SIRTAC sobre los cobros, percepciones en la venta B2B) | SIRTAC se explica acá como régimen; su efecto en el cobro de una tienda, allá |
| [Procesos de negocio](../Procesos-de-negocio/procesos-de-negocio.md) | cómo se determina y se declara cada impuesto | el recorrido entero (del pedido al cobro, de la compra al pago, del registro al balance) | el calendario del cierre es del proceso; la declaración jurada, de acá |
| [Software de gestión](../Software-de-gestion/software-de-gestion.md) | el saber tributario, que existe sin software | la alícuota como dato con vigencia, el motor de impuestos y la conexión con el fisco como columnas técnicas | la diferencia entre retención y percepción se explica acá; cómo se modela en una base, allá |

## Supuestos

- **Cinco verticales.** Obligación tributaria, Impuestos al consumo, Impuestos a la renta, Recaudación en la fuente y Cumplimiento. Mezclan dos cortes que el campo usa: por lo que grava cada impuesto (consumo y renta, los dos grupos que trata por separado el manual del FMI *Tax Law Design and Drafting*) y por las funciones de la administración tributaria (inscripción, declaración, pago, fiscalización, cobranza y controversias, como las ordenan el FMI y el CIAT; ver `.investigacion/cumplimiento.md`). La inscripción queda en Emprender y en `sujetos-del-impuesto`; las controversias se nombran en `fiscalizacion-y-sanciones`. Recaudación en la fuente va aparte porque cruza el consumo y la renta y es lo que más confunde a quien no es contador.
- **Sin vertical de impuestos al patrimonio, a los sueldos ni municipales.** Para una empresa pesan menos o son de otro tema; van en la entrada del tema y en `impuestos-en-argentina`.
- **Ingresos Brutos va en Impuestos al consumo**, porque grava lo facturado sin crédito por lo comprado, que es la definición de impuesto en cascada (Keen, FMI WP/13/57); que sea un impuesto en cascada es lectura de la base, sin un informe de organismo que lo diga de Ingresos Brutos en particular.
- **El régimen simplificado va en Obligación tributaria** y no en Impuestos a la renta: reemplaza a varios impuestos a la vez (en Argentina, IVA, Ganancias y aportes), así que es una forma de la obligación y no un impuesto más.
- **Comercio exterior** tiene una sola nota, la de Argentina; lo agnóstico (cómo tributa una importación o una exportación) va en `lugar-de-la-operacion`, y la aduana como trámite, a Cadena de suministro.
- **Lo de Argentina, en siete notas**: el mapa (`impuestos-en-argentina`), `comercio-exterior-en-argentina`, `monotributo-en-marcha`, `iva-en-argentina`, `ingresos-brutos`, `ganancias-en-argentina` y `retenciones-y-percepciones-en-argentina`. Son dinero y ley: no reemplazan a un contador.
- **Pendientes para otra sesión**: cuando existan Tesorería, Administración de personal y nómina, Cadena de suministro y Procesos de negocio, sus enlaces se suman a las notas de acá (hoy quedan como texto plano); `Emprender/Legal-e-impuestos` pasa a enlazar `monotributo-en-marcha` e `ingresos-brutos` en la sesión 16 (#101), y `Contabilidad/contabilidad.md` puede enlazar este tema en lugar de decir «todavía no escrito». Lo de este tema se resolvió en la sesión 16 (#123): las notas enlazan a Tesorería, Administración de personal y nómina, Cadena de suministro y logística, Procesos de negocio y Software de gestión. Ninguna nota de Software de gestión trata el motor que calcula el impuesto de cada renglón, y eso queda dicho como hueco.
