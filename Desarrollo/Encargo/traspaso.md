---
resumen: >-
  El traspaso es el cierre del encargo en el que el sistema pasa a ser del cliente: se entregan el
  código, las cuentas y los accesos, la documentación y la forma de operarlo, y se acuerda qué
  pasa después con la garantía y el soporte. Se apoya casi solo en guías de agencias; no hay norma
  ni estudio.
estado: borrador
estabilidad: semi
fuentes:
  - "Arbogast, Larman y Vodde (2012), Agile Contracts Primer v5, Deliverables, Warranty y el caso de la fase de soporte: http://www.agilecontracts.org/agile_contracts_primer.pdf"
  - "Miquido, Software Project Handover Checklist (según resumen): https://miquido.com/blog/software-project-handover-checklist"
  - "Axonbuild, Software project handover checklist (según resumen): https://axonbuild.com/blog/software-project-handover-checklist/"
  - "Simplethread, Checklist for Handing Off a Software Project (según resumen): https://www.simplethread.com/handing-off-a-software-project/"
  - "Wavect, When a build ends (según resumen): https://wavect.io/software-development-guide/software-handover-checklist/"
  - "Sprintlaw, cláusulas de aceptación y garantía en contratos de software (según resumen): https://sprintlaw.co.uk/articles/software-acceptance-criteria-contracts/"
  - "Manifestly, Project Closure Checklist (según resumen): https://app.manifest.ly/public/checklists/project-closure-checklist"
  - "Desarrollo/.investigacion/encargo.md"
aliases: [traspaso, handover, handoff, entrega final, cierre del proyecto, project closure, transferencia de conocimiento, garantía, soporte posterior]
creado: 2026-11-27
revisado:
---

# Traspaso

El traspaso es el cierre del encargo en el que el sistema pasa a ser del cliente: se entregan el código, las cuentas y los accesos, la documentación y la forma de operarlo, y se acuerda qué pasa después con la garantía y el soporte. Se apoya casi solo en guías de agencias; no hay norma ni estudio.

Llega cuando se acepta el último incremento (ver [alcance y aceptación](alcance-y-aceptacion.md)) y entrega el sistema a [Evolución](../Evolucion/evolucion.md), sea en manos del cliente, de otro proveedor o del mismo proveedor con un abono. Tiene dos tiempos que las fuentes mezclan: el cierre del proyecto y lo que sigue. Esta nota los separa.

Las guías de agencias que se usan acá son todas secundarias y varias se parecen mucho entre sí. Cuentan como una sola fuente sobre qué suele incluirse, no como confirmación mutua.

## El cierre: qué pasa a manos del cliente

Según esas guías, leídas por resumen, el traspaso cubre cuatro cosas.

| Qué | Lo que piden las guías |
|---|---|
| Código | El repositorio en la cuenta del cliente o transferido a ella; después de transferirlo, revisar los webhooks, los secretos y las claves de despliegue que quedan atados |
| Cuentas y accesos | Una lista de quién tiene acceso y la fecha en que termina el de la agencia; rotar claves; pasar alojamiento, dominio y cuentas de terceros a nombre del cliente. Las cuentas atadas al correo de un ingeniero aparecen como fuente común de problemas |
| Documentación | Arquitectura, runbooks, registro de cambios, guía de contribución en el repositorio, y una lista de lo que vive fuera del control de versiones |
| Conocimiento | Sesiones de capacitación grabadas antes de cerrar el contrato |

Las guías también piden confirmar la transferencia de la propiedad del código, el pago final y el inicio de la garantía, y mencionan el depósito del código en un tercero (*escrow*). Según su resumen, la división entre el código hecho a medida y las herramientas reutilizables que se queda la agencia es cuestión de contrato, sin regla fija.

El *Agile Contracts Primer* agrega una advertencia y una postura. La advertencia es que hay software a medida cuyo código fuente nunca se entregó porque alguien se olvidó, y por eso el código y los accesos van como entregables explícitos desde el principio. La postura es que, con entrega incremental, el cliente ya viene recibiendo código desplegado, y la documentación se escribe al final solo si el cliente toma el mantenimiento, «perhaps in a joint agile-documentation workshop».

Para cuentas de un comercio, cómo se sale (pasar lo que estaba a nombre del prestador, quitar los usuarios propios, cambiar las contraseñas compartidas, destruir los datos exportados) ya está en [acceso a las cuentas del cliente](../../Emprender/Legal-e-impuestos/acceso-a-las-cuentas-del-cliente.md#cómo-se-sale). De quién es lo entregado según la ley argentina, y por qué conviene que lo diga el contrato, está en [contrato de servicio](../../Emprender/Legal-e-impuestos/contrato-de-servicio.md#lo-que-conviene-que-diga).

## Cómo se comprueba que el traspaso quedó

En criterio de esta base, que sale del informe de la vertical y no de una norma, el traspaso está hecho cuando alguien del lado del cliente puede, sin ayuda del proveedor:

1. Clonar el repositorio desde su cuenta, compilar y correr las pruebas.
2. Desplegar una versión.
3. Entrar a cada cuenta de terceros con un usuario propio.
4. Encontrar en la documentación cómo se opera lo que no está en el código.

> [!NOTE]
> Sin fuente todavía: el contenido de *Close Project or Phase* del PMBOK, un modelo de acta de entrega, y cualquier estudio o norma sobre traspaso de software a medida. Lo legal de Argentina (propiedad intelectual del código entregado por un independiente, garantía legal, validez de una aceptación por correo o por silencio) queda fuera de esta nota y en buena parte sin resolver.

## Lo que sigue: garantía y soporte

La garantía cubre fallas de lo entregado; el soporte y el mantenimiento cubren lo demás. Cuánto dura la garantía no tiene cifra que sirva como norma, y las tres que se encontraron discrepan:

| Fuente | Ventana de garantía |
|---|---|
| Una guía de cierre de proyecto (Manifestly, por resumen) | 30 días, con la recomendación de firmar el soporte antes de que venza |
| Un estudio web europeo, en [abono de cuidado](../../Emprender/Modelo-de-negocio/abono-de-cuidado.md#cuándo-se-ofrece) | Tres meses, porque muchas fallas aparecen con tráfico real a las seis u ocho semanas |
| Un blog legal del Reino Unido (Sprintlaw, por resumen) | 12 meses |

Lo que sí coincide es separar la garantía del mantenimiento y acordar el soporte antes de que la garantía termine, para que no quede un hueco. Con entrega incremental, el *Primer* ata la garantía a cada entregable aceptado, lo que achica la garantía final. Para la fase de soporte describe un caso de tiempo y materiales con tope mensual y alcance variable, que funcionó porque había confianza; el detalle está en [modelos de contrato y cobro](modelos-de-contrato-y-cobro.md#cómo-se-paga-a-lo-largo-del-encargo). El modelo de negocio del mantenimiento como producto es el [abono de cuidado](../../Emprender/Modelo-de-negocio/abono-de-cuidado.md).

## Qué cambia cuando el sistema lo construyó un agente

Tres cosas, todas lectura de esta base sin fuente que las mida.

El traspaso incluye ahora el contexto para agentes: el archivo de instrucciones del repositorio, los comandos, las pruebas y las convenciones, para que el cliente o su próximo proveedor siga trabajando con un agente desde el primer día. Qué lleva ese contexto está en [contexto del repositorio](../Construccion/contexto-del-repositorio.md).

La documentación se genera barata; lo caro es que sea verdadera y siga siéndolo. Un documento generado al cerrar que nadie verificó contra el sistema es peor que uno corto y cierto.

El cliente recibe código que quizás no puede revisar, hecho por un agente y verificado sobre todo por pruebas. Eso vuelve más importante entregar las pruebas y la forma de correrlas (ver [Verificación](../Verificacion/verificacion.md)), y es lo primero que va a mirar quien lo reciba como [sistema heredado](../Evolucion/sistema-heredado.md).

En criterio de esta base, pierden peso el documento de diseño de cien páginas como entregable de cierre y la capacitación presencial larga como único medio de pasar el conocimiento.

Para leer: no hay un recurso canónico con fuente fuerte. Lo más cercano es el *Primer* (Deliverables, Warranty y el caso de soporte) para el criterio, y una lista de agencia, como la de Simplethread, leída como práctica. Fijate en la propiedad de las cuentas y en que el cliente corra solo el build y las pruebas.
