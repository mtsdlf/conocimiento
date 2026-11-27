---
resumen: >-
  El resultado de un proyecto es lo que tiene que ser verdad cuando termine, escrito de modo que se pueda comprobar; "terminado" es el momento en que la evidencia muestra que se logró, no el momento en que se acabaron las actividades.
estado: borrador
estabilidad: estable
fuentes:
  - "Atkinson (1999), Project management: cost, time and quality, two best guesses and a phenomenon..., IJPM (resumen secundario): https://edisciplinas.usp.br/mod/resource/view.php?id=5118664"
  - "Flyvbjerg (2014), What You Should Know About Megaprojects and Why: https://arxiv.org/abs/1409.0003"
  - "PRINCE2, principio de foco en los productos, resumen de la Universidad de Szeged (secundaria): https://inf.u-szeged.hu/kurzusleirasok/PMTananyag/22_principles.html"
  - "DIN/Beuth, índice de ISO 21502:2020 (solo el índice): https://www.din.de/de/mitwirken/normenausschuesse/nqsz/veroeffentlichungen/wdc-beuth:din21:334145134/toc-3233385/download"
  - "Anthropic, Effective harnesses for long-running agents: https://anthropic.com/engineering/effective-harnesses-for-long-running-agents"
  - "Anthropic, Building effective agents (el pasaje citado): https://www.anthropic.com/research/building-effective-agents"
  - "Cemri et al. (2025), Why Do Multi-Agent LLM Systems Fail?, arXiv 2503.13657 (según resúmenes): https://arxiv.org/abs/2503.13657"
  - "Gestion-de-proyectos/.investigacion/encuadre-y-gobierno.md"
aliases: [definición de terminado, definition of done, criterio de éxito, success criteria, resultado esperado, outcome, entregable, output]
creado: 2026-11-27
revisado:
---

# Resultado y terminado

El resultado de un proyecto es lo que tiene que ser verdad cuando termine, escrito de modo que se pueda comprobar; "terminado" es el momento en que la evidencia muestra que se logró, no el momento en que se acabaron las actividades.

Es la pieza del [encuadre](encuadre.md) de la que dependen el seguimiento y el cierre. [Medir el avance](../Seguimiento/medir-el-avance.md) mide contra este resultado, [aceptar con evidencia](../Seguimiento/aceptar-con-evidencia.md) lo comprueba pieza por pieza, y [cerrar o cancelar](../Gobierno-y-cierre/cerrar-o-cancelar.md) decide con él si el proyecto se dio por logrado.

## Entregable, resultado y beneficio

Conviene separar tres cosas que se suelen mezclar. El entregable es lo que el proyecto produce: un sistema instalado, un local abierto, un manual impreso. El resultado es el cambio que ese entregable provoca: los pedidos se toman por el sistema nuevo, el local atiende al público. El beneficio es lo que ese cambio vale para quien pagó: menos errores en los pedidos, más ventas en la zona. Un proyecto puede entregar todo y no lograr el resultado, y lograr el resultado sin que llegue el beneficio.

> [!NOTE]
> Sin fuente todavía: la distinción entre entregable, resultado y beneficio no se verificó en una fuente primaria (el glosario de PRINCE2 7 o una guía de beneficios). ISO 21502 tiene, según su índice, una práctica de gestión de beneficios (7.3) separada de la del alcance (7.4), lo que apoya separar el beneficio; el resto es vocabulario de esta base.

PRINCE2 pone el foco en el primer nivel. Según un material de curso de la Universidad de Szeged sobre sus principios (secundario, no el manual): "A PRINCE2 project focuses on the definition and delivery of the products, in particular their quality requirements". El beneficio queda en el [caso de negocio](justificacion.md), que se sigue mirando después de entregar.

## Cumplir costo, plazo y calidad no es lograr el resultado

El triángulo de costo, plazo y calidad mide si se hizo lo prometido al precio prometido. No mide si sirvió. Atkinson (1999) propuso por eso otros criterios de éxito, porque un proyecto puede cumplir los tres y fracasar; la fuente se vio en un resumen. Flyvbjerg, en cambio, define el éxito de un megaproyecto como entregar en presupuesto, en plazo y con los beneficios prometidos: agrega el beneficio a la vara. Qué tan seguido se cumple esa vara está en [por qué fallan los proyectos](../Incertidumbre-y-riesgo/por-que-fallan-los-proyectos.md).

## Cómo se escribe un terminado comprobable

Un terminado sirve si dos personas que no hablaron entre sí llegan a la misma conclusión mirando la misma evidencia. Para eso:

1. Escribí el resultado como un estado observable ("el servicio responde desde la plataforma nueva y la anterior está apagada"), no como una tarea ("migrar el servicio").
2. Para cada resultado, decí qué evidencia lo muestra: una prueba que pasa, una medición, una inspección, una firma.
3. Escribí el criterio antes de empezar y dejalo fuera del alcance de quien ejecuta: quien hace el trabajo no cambia la vara con la que se lo acepta.
4. Separá lo que se comprueba por máquina de lo que requiere el juicio de una persona, y decí quién hace ese juicio.

En software, este criterio se baja a [criterios de aceptación](../../Desarrollo/Definicion/criterios-de-aceptacion.md) por cada cambio, y la aceptación con un cliente está en [alcance y aceptación](../../Desarrollo/Encargo/alcance-y-aceptacion.md).

## Qué cambia cuando quien dice "terminado" es un agente

Con agentes, el terminado comprobable pasa de buena práctica a condición: es una lectura de esta base. Un agente declara haber terminado cuando cree que lo logró, y puede declararlo sin haberlo logrado (la taxonomía MAST, más abajo, incluye fallas de verificación); cuánto pasa eso y cómo se acepta igual está en [aceptar con evidencia](../Seguimiento/aceptar-con-evidencia.md).

Anthropic describe una forma concreta de armarlo. El trabajo arranca como una lista de funcionalidades, todas marcadas como fallidas, y el agente solo puede cambiar el campo que dice si pasan. La instrucción dice: "It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality", y "Only mark features as 'passing' after careful testing". La verificación de punta a punta funcionó recién cuando se le pidió de forma explícita que usara herramientas de automatización del navegador, y tuvo límites: no veía los diálogos nativos del navegador. En otro texto, Anthropic pide que el agente obtenga "ground truth" del entorno en cada paso. Las dos son fuentes de laboratorio, sin estudio comparativo.

Del lado de las fallas, la taxonomía MAST de Cemri y otros agrupa 14 modos de falla de sistemas multiagente en tres categorías, y una de ellas es la verificación de tareas, con modos como "No or Incomplete Verification" e "Incorrect Verification". Según los resúmenes, los autores atribuyen muchas fallas al diseño del sistema y no solo al modelo. Las fallas de agentes en general están en [fallas de agentes](../../IA/Agentes/fallas-de-agentes.md).

La lección práctica coincide con el paso 3: el criterio lo escribe quien encarga, antes, y quien ejecuta no lo puede editar. Cómo se arma el encargo está en [delegar a un agente](../Personas-y-agentes/delegar-a-un-agente.md), y cómo se revisa lo que hizo un agente de código, en [verificar lo que hizo un agente](../../Desarrollo/Verificacion/verificar-lo-que-hizo-un-agente.md).
