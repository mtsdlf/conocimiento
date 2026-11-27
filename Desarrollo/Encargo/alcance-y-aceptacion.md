---
resumen: >-
  El alcance es lo que el encargo se compromete a entregar, con lo que queda afuera escrito; la
  aceptación es el momento en que el cliente dice que un incremento o el proyecto están
  terminados, y conviene que dependa de criterios verificables acordados antes de construir.
estado: vigente
estabilidad: estable
fuentes:
  - "Arbogast, Larman y Vodde (2012), Agile Contracts Primer v5, secciones Acceptance, Warranty y Deliverables, leídas: http://www.agilecontracts.org/agile_contracts_primer.pdf"
  - "Schwaber y Sutherland, The Scrum Guide (2020), Increment y Definition of Done: https://scrumguides.org/scrum-guide.html"
  - "ISTQB Glossary, acceptance criteria y acceptance testing (según resumen del buscador): https://api.glossary.istqb.org/storage/help/R0uz58NqLzUz48LVUuyGSF76NFj4LHQazSs0GlNS.pdf"
  - "Caroli, Lean Inception: https://www.martinfowler.com/articles/lean-inception"
  - "Desarrollo/.investigacion/encargo.md"
aliases: [alcance, scope, aceptación, acceptance, definición de terminado, definition of done, DoD, UAT, pruebas de aceptación, línea base de alcance, scope baseline]
creado: 2026-11-27
revisado: 2026-11-27
---

# Alcance y aceptación

El alcance es lo que el encargo se compromete a entregar, con lo que queda afuera escrito; la aceptación es el momento en que el cliente dice que un incremento o el proyecto están terminados, y conviene que dependa de criterios verificables acordados antes de construir.

Las dos cosas van en una nota porque son los extremos de la misma cadena: el alcance escrito es la línea base, los [cambios de alcance](cambios-de-alcance.md) se comparan contra ella y la aceptación se hace contra lo que quedó. Viene del [acuerdo inicial](acuerdo-inicial.md) y pasa a [Definición](../Definicion/definicion.md), donde cada parte del alcance se vuelve [especificación](../Definicion/especificacion.md) y [criterios de aceptación](../Definicion/criterios-de-aceptacion.md). Cómo se fija el alcance en un contrato a precio cerrado, y por qué ese caso tiende a perder plata, está en [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md#el-alcance-por-escrito-y-los-cambios-contra-ese-escrito).

## Qué quiere decir terminado

En criterio de esta base, terminado tiene dos niveles, y se confunden. El primero es del equipo: el *Scrum Guide* define que «The Definition of Done is a formal description of the state of the Increment», y agrega que «In order to provide value, the Increment must be usable». El segundo es del cliente: el glosario de ISTQB, según su resumen, define los criterios de aceptación como los que un sistema «must satisfy in order to be accepted by a user, customer, or other authorized entity», y la prueba de aceptación como el nivel que decide si se acepta el sistema.

En criterio de esta base, la definición de terminado es la misma para todos los incrementos (por ejemplo, probado, revisado y desplegado), y los criterios de aceptación son de cada incremento y dicen qué tiene que hacer. Un incremento puede cumplir la primera y no la segunda: está bien hecho y no es lo que el cliente pidió.

## Lo que queda afuera también es alcance

Un alcance que solo dice qué entra deja abierta cualquier interpretación de lo demás. Lean Inception lo trabaja con el ejercicio «Is – Is not – Does – Does not», que obliga a escribir qué no es y qué no hace el producto. La lista explícita de fuera de alcance la recomiendan los blogs de agencia; no se encontró un estudio que la mida.

## La aceptación por partes

Si se entrega por incrementos, se acepta por incrementos. El *Agile Contracts Primer* pregunta «Is it done?» y «What to do if not done?», y propone que en entrega iterativa la aceptación final sea la suma de aceptaciones por iteración, basadas en «conformance to a prior agreed-on acceptance-test». La prueba de aceptación se acuerda antes de construir y se usa al aceptar.

Esto tiene dos efectos que el *Primer* nombra. El riesgo de la garantía final baja, «especially enhanced if automated acceptance testing is employed», porque cada parte ya se probó; la garantía se ata a cada entregable. Y el pago se puede atar a cada aceptación, que es el sistema que el *Primer* llama el más popular (ver [modelos de contrato y cobro](modelos-de-contrato-y-cobro.md)). Qué se hace con los defectos menores que no traban la aceptación y cómo se cierra formalmente está en [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md#aceptar-y-cerrar); en Argentina, la recepción provisional con plazo de garantía del art. 1272 del Código Civil y Comercial está en [contrato de servicio](../../Emprender/Legal-e-impuestos/contrato-de-servicio.md#lo-que-conviene-que-diga).

En criterio de esta base, la prueba de aceptación de usuarios como una fase única al final, con planillas de casos manuales, [pierde peso](../Fundamentos/lo-que-pierde-peso-en-desarrollo.md#lo-que-pierde-peso-en-cada-etapa) frente a la aceptación incremental con demostraciones y criterios automatizados. No se encontró una fuente que mida ese cambio; es la lectura del *Primer* que hace esta base.

## Qué va en el contrato y qué no

El *Primer* recomienda no fijar en el contrato una lista detallada de entregables: «Avoid such specificity and rigidity—avoid including a detailed deliverables list in the contract», porque se termina produciendo documentos en lugar de software andando. Con una excepción que cuenta como advertencia: «we have seen custom software for which the source code was never provided by the supplier—somebody forgot». El código fuente y los accesos tienen que figurar como entregables explícitos; el resto se detalla en el [traspaso](traspaso.md).

La documentación técnica se suele pedir en los contratos tradicionales, pero según el *Primer* «could be wasteful to require it as an early deliverable». Si el cliente va a mantener el sistema, puede escribirse al final, «perhaps in a joint agile-documentation workshop».

## Qué cambia cuando verifica un agente

Los criterios escritos como ejemplos verificables valen más que antes. Son lo que un agente usa para saber cuándo terminó y lo que una persona usa para no leer cada línea; el detalle está en [criterios de aceptación](../Definicion/criterios-de-aceptacion.md) y en [verificar lo que hizo un agente](../Verificacion/verificar-lo-que-hizo-un-agente.md). La idea de que la aceptación automatizada baja el riesgo ya estaba en el *Primer*.

Lo que no se delega es que el cliente confirme que el criterio dice lo que quiere. Un agente verifica contra el criterio escrito, no contra la intención del cliente. En criterio de esta base, por eso la aceptación tiene dos firmas distintas: el cliente aprueba los criterios antes de que se construya, y acepta el incremento después de verlo andar. Esa segunda firma es la validación, que [Verificación](../Verificacion/verificacion.md#verificar-contra-lo-definido-validar-contra-lo-que-se-necesitaba) separa de verificar.

## Cómo falla

- Los criterios se escriben después de construir, y la aceptación se vuelve una negociación sobre qué se había querido decir.
- El incremento pasa las pruebas pero no se puede usar (no está desplegado, le falta una pieza), y no cumple la condición de usable del *Scrum Guide*.
- Nadie dice qué pasa si algo no está terminado, que es la segunda pregunta del *Primer*.
- El código fuente o una cuenta quedan fuera de los entregables y aparecen en el traspaso.

Para leer: el *Agile Contracts Primer*, secciones Acceptance, Warranty y Deliverables, libre y de pocas páginas por tema. Fijate en que la aceptación sea por conformidad con pruebas acordadas antes.
