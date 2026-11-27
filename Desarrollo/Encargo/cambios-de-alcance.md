---
resumen: >-
  Un cambio de alcance es un pedido del cliente que no estaba en lo acordado. Se maneja con una
  regla fijada antes del primer pedido: cotizarlo por escrito, cambiarlo por algo del mismo tamaño
  o recortar para que entre en el tiempo fijo; la regla depende del modelo de contrato, y las
  fuentes discrepan sobre cuánta formalidad hace falta.
estado: borrador
estabilidad: semi
fuentes:
  - "Arbogast, Larman y Vodde (2012), Agile Contracts Primer v5, sección Change Management y Part 3, leídas: http://www.agilecontracts.org/agile_contracts_primer.pdf"
  - "Sutherland (2008), Agile Contracts: Money for Nothing and Your Change for Free: http://jeffsutherland.com/scrum/2008/10/agile-contracts-money-for-nothing-and.html"
  - "Fowler (2004), Fixed Scope Mirage, leído: https://martinfowler.com/bliki/FixedScopeMirage.html"
  - "Singer, Shape Up, glosario (scope hammering, circuit breaker): https://basecamp.com/shapeup/4.5-appendix-06"
  - "PMI, PMBOK Guide 6a ed., Control Scope (según resúmenes): https://www.projectmanagement.com/blog-post/58284/project-scope-management-part-6--control-scope"
  - "Desarrollo/.investigacion/encargo.md"
  - "Desarrollo/.investigacion/posicion-contraria.md"
aliases: [cambio de alcance, change request, solicitud de cambio, change order, orden de cambio, control de cambios, scope creep, gold-plating, presupuesto de cambios]
creado: 2026-11-27
revisado:
---

# Cambios de alcance

Un cambio de alcance es un pedido del cliente que no estaba en lo acordado. Se maneja con una regla fijada antes del primer pedido: cotizarlo por escrito, cambiarlo por algo del mismo tamaño o recortar para que entre en el tiempo fijo; la regla depende del modelo de contrato, y las fuentes discrepan sobre cuánta formalidad hace falta.

Un cambio solo se puede reconocer contra una línea base, que es el [alcance](alcance-y-aceptacion.md) escrito y lo ya aceptado. El caso del precio cerrado (el cambio cotizado por escrito antes de hacerlo, el art. 1264 del Código Civil y Comercial, cuánto crece el alcance por mes y las causas del *scope creep*) está en [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md#el-alcance-por-escrito-y-los-cambios-contra-ese-escrito). Esta nota trata la decisión general: qué regla se elige y cómo se aplica.

## Tres reglas para un pedido nuevo

Cuando el cliente pide algo que no estaba, hay tres respuestas que las fuentes describen, y cada una calza con un modelo de [contrato y cobro](modelos-de-contrato-y-cobro.md).

| Regla | Qué se hace con el pedido | Calza con | Fuente |
|---|---|---|---|
| Cotizar el cambio | Se escribe qué se agrega, cuánto cuesta y cuánto mueve el plazo, y el cliente lo aprueba antes de hacerlo | Precio cerrado | PMBOK por resúmenes; práctica de agencias; art. 1264 |
| Intercambiar a igual esfuerzo | Entra si sale otra cosa del mismo tamaño; el total no crece | Precio fijo con alcance variable | *Primer*; Sutherland («change for free») |
| Recortar para que entre | El tiempo no se mueve; se cuestiona el diseño hasta que el trabajo entre, o se cancela | Apetito, tiempo fijo | Shape Up |

En tiempo y materiales el pedido se hace y se cobra por las horas que lleve. En criterio de esta base, igual conviene escribirlo, porque mueve la fecha y el presupuesto que el cliente tiene en la cabeza.

La tercera regla viene de Shape Up. El *scope hammering* es «Forcefully questioning a design, implementation, or use case to cut scope and finish inside the fixed time box», y el *circuit breaker* cancela por defecto lo que no termina en un ciclo, en lugar de extenderlo.

## Cuánta formalidad hace falta

> [!IMPORTANT]
> Las fuentes discrepan. El PMBOK, según resúmenes, trata el control de cambios como un proceso que gestiona los cambios a la línea base; la práctica de agencias pide cada cambio por escrito con costo, plazo y conformidad, y el Código Civil y Comercial exige autorización escrita para variar el proyecto aceptado. El *Agile Contracts Primer* toma la posición contraria para el trabajo ágil: «Avoid mandating change-management boards, change requests, or special change processes», porque el cambio tiene que ser fácil y frecuente. Admite grados: baja flexibilidad en precio fijo y media en costo objetivo. Las dos posturas son de practicantes, y no hay estudios que las comparen.

La lectura de esta base es que las dos posturas se reconcilian si la regla se acuerda una sola vez, al firmar, y después cada pedido se resuelve sin trámite nuevo. En precio cerrado, la autorización escrita es además lo que pide el art. 1264 en Argentina; qué vale como escrito y cómo se prueba está en [contrato de servicio](../../Emprender/Legal-e-impuestos/contrato-de-servicio.md#por-escrito-por-mail-o-por-whatsapp). Con intercambio a igual esfuerzo, alcanza con registrar qué entró y qué salió.

Fowler cuenta que hay proveedores que «deliberately low-bid the fixed price, with the explicit plan of making a profit on change requests». En criterio de esta base, un cliente que vio eso desconfía de cualquier cambio cotizado, y una regla escrita de antemano le muestra que ese no es el juego.

> [!NOTE]
> Sin fuente todavía: el presupuesto de cambios como técnica con nombre (una bolsa de horas o de unidades acordada al firmar, que se gasta sin trámite mientras dura) y su efecto medido. Sutherland hace algo parecido con «change for free» mientras el total no crezca, pero no lo describe como bolsa.

## Cómo se aplica a un pedido concreto

1. Compará el pedido contra el alcance escrito y lo aceptado, no contra la memoria de nadie. Si estaba, no es un cambio.
2. Si es un cambio, aplicá la regla acordada: cotizalo, buscá qué sale a cambio o decidí qué se recorta.
3. Si toca algo ya aceptado, sumá al costo volver a verificarlo: una parte aceptada que se rompe es una regresión, no un pedido nuevo.
4. Dejá escrito qué se decidió y actualizá la línea base, para que el próximo pedido se compare contra la versión nueva.

## Qué cambia cuando construye un agente

Rehacer una pieza se abarató. Si un agente la reconstruye en horas, el costo de un cambio cae más para el proveedor que para la planificación. Es lectura de esta base, sin medición. Lo que no cae es decidir, verificar y tocar partes ya aceptadas.

Que el cambio sea barato de programar empuja a aceptar más cambios y a que el alcance crezca sin que nadie lo decida. El agente también puede entregar de más por su cuenta: es el *gold-plating* que las agencias ya listaban entre las causas del *scope creep*, ahora sin esfuerzo visible. En criterio de esta base, el intercambio a igual esfuerzo sigue siendo la defensa, medido en tamaño de resultado y no en horas, y la [revisión](../Verificacion/revision-de-codigo.md) tiene que mirar también lo que se hizo sin que nadie lo pidiera. Con el mismo criterio, [pierden peso](../Fundamentos/lo-que-pierde-peso-en-desarrollo.md#lo-que-pierde-peso-en-cada-etapa) el formulario de cambio aprobado por comité y la estimación en horas de cada cambio como forma de cobrarlo.

Para leer: el *Primer*, sección Change Management, junto con el texto de Fowler como contraste y el glosario de Shape Up para el tiempo fijo. Fijate en qué regla existe antes del primer pedido.
