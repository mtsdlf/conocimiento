---
tema: Procesos de negocio
para: entender los ocho recorridos de punta a punta que cruzan los dominios de una empresa (qué pasos tienen, qué documento pasa de un dominio a otro, dónde se traban y qué se mide del recorrido entero), para quien construye software de gestión y, en segundo lugar, para quien lo vende o lo implementa
nivel: entiende de software y de negocio en general; el detalle de cada paso se da por leído en su tema de dominio, y acá se explica solo lo que no es de ningún dominio: el hilo, los traspasos y las medidas del recorrido
escuela: neutral; los recorridos se cuentan como los publica APQC (procesos de punta a punta armados con piezas de su marco funcional) y como los ordenan los libros de sistemas de información contable (los ciclos de transacciones); la crítica de la mirada por procesos (la reingeniería y sus fracasos) va en Fundamentos
fuera:
  - el detalle de cada paso (cómo se registra un asiento, cómo se arma una orden de compra, cómo se prepara un pedido) — en el tema de dominio que es dueño del paso; acá se enlaza
  - del contacto al pedido (lead-to-order): el embudo y el método de vender — Ventas; el interesado, la oportunidad y el presupuesto — Relacion-con-clientes (decisión de #99: no hay nota «del contacto al pedido»)
  - la calidad como proceso propio — es un paso dentro de la compra al pago, la planificación a la producción y el reclamo a la resolución (decisión de #99); su detalle en Produccion/Calidad
  - de la idea al mercado (idea-to-market) y el desarrollo de producto físico — fuera del perímetro del mapa (#99, #104)
  - riesgo, cumplimiento y comercio exterior como recorridos — no son recorridos (#99); comercio exterior es de Cadena-de-suministro-y-logistica y lo fiscal de Impuestos
  - la gestión por procesos como disciplina (modelar con BPMN, mejora continua, gobierno de procesos) — no es de este tema; se nombra en Fundamentos solo como contexto
  - cómo un producto de software lleva el recorrido (el flujo de trabajo, los estados del documento, la integración entre módulos) — tema Software de gestión
  - los procesos de cómo trabaja la organización propia (runbooks, quién decide) — repo mtsdlf/procesos
fuentes: []
preguntas:
  - "Estoy diseñando la facturación de un sistema para un mayorista que vende en cuenta corriente: ¿qué documentos pasan de mano entre el pedido y el cobro, en qué dominio nace cada uno y dónde se traba el recorrido?"
  - "¿Qué es el cruce de tres vías, en qué paso de la compra al pago va y qué pasa cuando la factura del proveedor no coincide con lo recibido?"
  - "¿Qué tiene que entregar cada área, y en qué orden, para cerrar un mes y emitir los estados contables? ¿Cómo se mide si el cierre es rápido?"
  - "Una firma de servicios cobra tarde: ¿dónde se pierde tiempo y plata entre la hora cargada y el cobro, y qué conviene medir?"
  - "Un cliente reclama por un producto fallado: ¿qué recorre el reclamo hasta cerrarse, con la devolución, la nota de crédito y el stock?"
  - "Tengo que facturar y pagar en la Argentina: ¿dónde entran la factura electrónica, las percepciones y las retenciones en cada recorrido, y dónde está el detalle?"
aprobado:
---

# Alcance: Procesos de negocio

El tema cubre los recorridos que atraviesan varios dominios de la empresa y terminan en un resultado del negocio: del pedido al cobro, de la compra al pago, del registro al balance y otros cinco. Sale del mapa «el mundo del software de gestión» (issue #94) y de sus decisiones: forma del árbol (#95), taxonomías externas (#96), columnas técnicas (#97), límites entre dominios (#98), procesos de punta a punta (#99, que fija los ocho procesos, dónde empieza y termina cada uno y que los marcos se citan sin vertical), verticales de Software de gestión (#100), orden de armado (#101) y huecos del árbol (#104). Es la sesión 13 de 16 (issue #120), y la última de los temas de dominio: los doce ya están escritos y este tema los enlaza.

Es un tema agnóstico: vale para cualquier producto sin nombrar proveedores y se sostiene sin software (un recorrido se puede seguir con papeles que pasan de un escritorio a otro, y así se hizo durante siglos). Lo propio de la Argentina va en una nota aparte que enlaza a Impuestos, Contabilidad y Administración de personal en lugar de repetirlos.

## Límites con los vecinos

Cada dominio es dueño de un objeto y un verbo, y lo que cruza dominios va acá (decisión de #98). Este tema no es dueño de ningún documento: es dueño del **recorrido**, o sea, del orden de los pasos, de los **traspasos** (qué documento pasa de un dominio a otro y qué tiene que coincidir) y de las **medidas del recorrido entero** (el tiempo de punta a punta, los días de cobro, los días de cierre). Cada paso se explica en su dominio y desde acá se enlaza.

| Vecino | Es dueño de | La frontera con este tema |
|---|---|---|
| [Relación con clientes](../Relacion-con-clientes/relacion-con-clientes.md) | el cliente, la oportunidad, el presupuesto y el pedido de venta | El pedido aceptado abre el recorrido del pedido al cobro; cómo se arma el pedido es de allá |
| [Ventas](../Ventas/ventas.md) | el método de vender y el embudo | Lo anterior al pedido no es recorrido de acá: se enlaza hacia atrás |
| [Servicio al cliente](../Servicio-al-cliente/servicio-al-cliente.md) | el caso, el reclamo, el escalamiento y los niveles de servicio | Acá, el recorrido del reclamo a la resolución con lo que toca en otros dominios (devolución, nota de crédito, visita); el caso, allá |
| [Inventario y depósitos](../Inventario-y-depositos/inventario-y-depositos.md) | lo que pasa dentro del depósito: recibir, reservar, preparar, contar | La reserva, la preparación y la recepción son pasos de varios recorridos; su detalle, allá |
| [Compras y abastecimiento](../Compras-y-abastecimiento/compras-y-abastecimiento.md) | el proveedor, la solicitud y la orden de compra, y el control de lo recibido contra lo pedido | Compras termina cuando lo recibido coincide con lo pedido; la factura, el control contra la orden y el pago siguen el recorrido de la compra al pago |
| [Cadena de suministro y logística](../Cadena-de-suministro-y-logistica/cadena-de-suministro-y-logistica.md) | el pronóstico, el S&OP, el transporte, el despacho y la entrega | El despacho y la prueba de entrega son pasos del pedido al cobro; el S&OP abre la planificación a la producción. SCOR, que es un marco de la cadena, se explica allá y se nombra acá |
| [Producción](../Produccion/produccion.md) | el plan maestro, el MRP, la orden de producción, el costo de lo fabricado y la calidad | Cada paso de la planificación a la producción tiene su detalle allá |
| [Contabilidad](../Contabilidad/contabilidad.md) | el registro de lo devengado, los ajustes de cierre, la conciliación y los estados | El cierre como recorrido entre áreas (quién entrega qué y cuándo) es de acá; el asiento de ajuste, allá |
| [Impuestos](../Impuestos/impuestos.md) | cómo se determina, se declara y se paga cada impuesto | Acá, en qué paso de cada recorrido aparece el impuesto; el cálculo y la declaración, allá |
| [Tesorería](../Tesoreria/tesoreria.md) | la plata real: el crédito al cliente, la cobranza, la aplicación del cobro, la corrida de pagos | Cobrar y pagar son los últimos pasos de dos recorridos; su detalle, allá |
| [Administración de personal y nómina](../Administracion-de-personal-y-nomina/administracion-de-personal-y-nomina.md) | el legajo, la asistencia, la liquidación y las cargas | Cada paso de la contratación a la baja se explica allá; acá, la cadena entera y lo que toca en Contabilidad y Tesorería |
| [Servicios profesionales y proyectos](../Servicios-profesionales-y-proyectos/servicios-profesionales-y-proyectos.md) | el proyecto del cliente, la asignación, las horas, la facturación del proyecto y el margen | Cada paso del proyecto al cobro tiene su detalle allá |
| [Activos y mantenimiento](../Activos-y-mantenimiento/activos-y-mantenimiento.md) | el registro del equipo, la estrategia de mantenimiento y la orden de trabajo | La orden de trabajo es un paso de la compra a la baja del activo; la amortización, de Contabilidad |
| [Software de gestión](../Software-de-gestion/software-de-gestion.md) | las [categorías de producto](../Software-de-gestion/Categorias-de-producto/categorias-de-producto.md) y las [columnas técnicas](../Software-de-gestion/Columnas-tecnicas/columnas-tecnicas.md) (documento y estados, integración) | Acá, el recorrido que existe sin software; allá, cómo un producto lo lleva entre módulos |

## Árbol

El tema tiene trece notas: las ocho de los procesos, la de la Argentina y tres de Fundamentos, más la entrada. Por el tamaño, los procesos no van en verticales con carpeta (regla de `documentar` para temas chicos): la entrada los agrupa en secciones por ciclo.

```
Procesos-de-negocio/
  procesos-de-negocio.md               el todo: qué es un proceso de punta a punta, los ocho agrupados por ciclo, la tabla proceso × dominio; qué leer según lo que estés haciendo
  del-pedido-al-cobro.md               order-to-cash: del pedido aceptado al cobro aplicado; variantes minorista, mayorista en cuenta corriente y suscripción
  de-la-compra-al-pago.md              procure-to-pay: de la necesidad al pago al proveedor, con el control de tres vías
  del-registro-al-balance.md           record-to-report: del registro diario a los estados contables, el cierre como recorrido entre áreas
  de-la-planificacion-a-la-produccion.md  plan-to-produce: del plan agregado al producto terminado y costeado
  de-la-contratacion-a-la-baja.md      hire-to-retire: del puesto aprobado a la liquidación final
  del-reclamo-a-la-resolucion.md       issue-to-resolution: del reclamo del cliente al caso cerrado, con la devolución y la nota de crédito
  del-proyecto-al-cobro.md             project-to-cash: del proyecto vendido al cobro de lo facturado por hora, hito o abono
  de-la-compra-a-la-baja-del-activo.md acquire-to-retire: la vida del activo, de la compra a la baja, con el mantenimiento como paso
  procesos-de-negocio-en-argentina.md  dónde entran la factura electrónica, las percepciones, las retenciones, el cierre con vencimientos y las altas y bajas laborales; enlaza a Impuestos, Contabilidad y Administración de personal
  Fundamentos/
    fundamentos-de-procesos-de-negocio.md  (entrada) de dónde viene la mirada por procesos, los ciclos de transacciones, la posición contraria y las fuentes
    marcos-de-procesos.md                 marco funcional frente a proceso de punta a punta: APQC PCF, SCOR, ISA-95, CIPS, SHRM, eTOM; a qué dominio va cada uno y los códigos APQC de cada proceso
    glosario-de-procesos-de-negocio.md    términos con su nombre en inglés
```

## Supuestos

- Los ocho procesos, dónde empieza y termina cada uno, y que los marcos se citan sin vertical vienen decididos en #99. El árbol de adentro del tema lo propone esta sesión sin esperar respuesta, por indicación de quien la abrió, y queda para revisar en el PR.
- Cada nota de proceso tiene la misma forma: dónde empieza y termina, los pasos con el dominio dueño y el documento que deja cada uno, los traspasos, dónde se traba, qué se mide del recorrido entero y las variantes como apartados. El detalle de cada paso se enlaza, no se repite.
- Una medida que ya está definida en un tema de dominio (los días de cobro en Tesorería, la utilización en Servicios profesionales) se enlaza; acá se definen solo las que miden el recorrido entero.
- La nota de la Argentina es una sola, como en los otros temas del área, con un apartado por recorrido que lo necesita.
- Los códigos APQC salen del PCF 7.4 (agosto de 2024), que se leyó entero en la copia que publica la Federación Internacional de la Cruz Roja (la misma que cita Producción). La 8.0 (febrero de 2026) no se pudo leer.
- La nota de marcos es de Fundamentos y no es vertical (decisión de #99). Los marcos de un solo dominio (SCOR, ISA-95, CIPS, SHRM) se explican en el tema de ese dominio cuando ya están escritos ahí, y acá se dice a qué dominio va cada uno.
