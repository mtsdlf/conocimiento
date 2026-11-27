---
resumen: >-
  Delegar a un agente es pasarle una pieza de trabajo con cuatro cosas dichas: la intención (para qué sirve), los límites (qué no puede hacer), el criterio de terminado (cómo se comprueba) y el presupuesto (cuánto puede gastar antes de parar). La lista es una síntesis de esta base.
estado: vigente
estabilidad: semi
fuentes:
  - "Anthropic (2024-12-19), Building effective agents (resumen): https://www.anthropic.com/research/building-effective-agents"
  - "Anthropic (2025-09-29), Effective context engineering for AI agents (resumen): https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
  - "Tomašev, Franklin y Osindero (2026), Intelligent AI Delegation, arXiv 2602.11865, preprint (resumen del HTML, secciones 4.1 y 4.2): https://arxiv.org/html/2602.11865"
  - "Ejército de EE. UU., ADP 6-0 Mission Command (2019) (solo localizada; principios según un resumen): https://irp.fas.org/doddir/army/adp6_0.pdf"
  - "army.mil (2019), Mission command requires sharp commander's intent (resumen): https://www.army.mil/article/215297/mission_command_requires_sharp_commanders_intent"
  - "DTIC ADA234125, estudio sobre órdenes de misión (resumen): https://apps.dtic.mil/sti/pdfs/ADA234125.pdf"
  - "Gestion-de-proyectos/.investigacion/personas-y-agentes.md"
aliases: [encargo a un agente, brief para un agente, especificar una tarea para un agente, delegating to an agent, task specification]
creado: 2026-11-27
revisado: 2026-11-27
---

# Delegar a un agente

Delegar a un agente es pasarle una pieza de trabajo con cuatro cosas dichas: la intención (para qué sirve), los límites (qué no puede hacer), el criterio de terminado (cómo se comprueba) y el presupuesto (cuánto puede gastar antes de parar). La lista es una síntesis de esta base.

Delegar en una persona es otra cosa: se le pasa la autoridad para decidir sobre un área, y la persona pregunta cuando algo no cierra. Eso está en [delegación](../../Liderazgo-y-direccion/Decidir/delegacion.md). Con un agente, la base supone que conviene no contar con que pregunte (ninguna fuente consultada mide cuánto preguntan los agentes), y completar lo que falta con lo que supone es un riesgo. Por eso el encargo a un agente tiene que decir por escrito lo que con una persona se aclara conversando.

## Las cuatro piezas del encargo y de dónde sale cada una

Ninguna fuente da esta lista. Sale de juntar tres tradiciones:

| Pieza | Qué dice | De dónde viene |
|---|---|---|
| Intención | Para qué sirve el resultado y qué estado final se busca | El mando por misión militar |
| Límites | Qué no se toca, qué acciones no puede hacer sin pedir permiso | El nivel de autonomía y las condiciones de parada |
| Criterio de terminado | Cómo se comprueba que está hecho, antes de empezar | Tomašev y colegas |
| Presupuesto | Tiempo, iteraciones o gasto máximo antes de parar y avisar | Las condiciones de parada de Anthropic |

**Intención.** En la doctrina militar de mando por misión, quien ordena dice el propósito y el estado final, y deja el cómo a quien ejecuta. Según un resumen, la doctrina del Ejército de EE. UU. de 2019 lista siete principios, entre ellos intención clara, órdenes de misión e iniciativa disciplinada. La lista de elementos de la intención (tarea, propósito, factores críticos, estado final) viene de un artículo de un general, no de la definición doctrinal. Un estudio sobre órdenes de misión dice, en síntesis, que actuar dentro de la intención no suele dar problemas, y alterarla sí. Para esta base (inferencia, no cita), con un agente la intención es lo que le permitiría elegir bien cuando el encargo no previó un caso.

**Criterio de terminado.** Tomašev y colegas sostienen que delegar es "contingent upon the outcome having precise verification" (sección 4.1): la base lo lee como que, si el resultado no se puede verificar, no conviene delegar así (esa consecuencia es lectura de esta base). Proponen además que el contrato sea bidireccional, con obligaciones para las dos partes (sección 4.2). En un proyecto, el criterio sale de [resultado y terminado](../Encuadre/resultado-y-terminado.md) y se aplica al recibir el trabajo con [aceptación con evidencia](../Seguimiento/aceptar-con-evidencia.md).

**Límites y presupuesto.** Anthropic recomienda poner "stopping conditions (such as a maximum number of iterations)" y que el agente pause "for human feedback at checkpoints or when encountering blockers", según un resumen de su guía. Para esta base, el presupuesto es el tope que evita que un agente trabado siga gastando; Anthropic lo plantea como tope de iteraciones. Cuánto decide solo dentro de esos límites es su [nivel de autonomía](niveles-de-autonomia.md); qué hace cuando un límite se toca, la [tolerancia y el escalamiento](../Incertidumbre-y-riesgo/problemas-y-escalamiento.md).

## Cuánto contexto darle

Ninguna fuente consultada mide cuál es el error más frecuente; el riesgo que esta base ve es escribir para alguien que ya sabe lo que uno sabe. Anthropic recomienda apuntar a la "right altitude", según un resumen: ni reglas rígidas que prevén cada caso ni una vaguedad que asume contexto compartido. Y dar "the minimal set of information that fully outlines your expected behavior".

Un ejemplo fuera del software. Encargarle a un agente "armá la lista de proveedores para el evento" deja todo abierto. El encargo con las cuatro piezas dice: la intención (un evento de 200 personas en tal ciudad, con presupuesto de catering cerrado), los límites (no contactar proveedores, solo investigar), el criterio de terminado (al menos tres opciones por rubro, con precio publicado y fuente) y el presupuesto (una hora de trabajo o 30 búsquedas, lo que llegue primero).

## Antes de soltar el encargo

1. Fijate si la tarea cae dentro de lo que el agente hace bien: [frontera irregular](frontera-irregular.md) y el largo de tarea en [horizonte de tareas](horizonte-de-tareas.md).
2. Partila hasta que cada pieza se pueda verificar sola, como dice [descomposición del trabajo](../Planificacion/descomposicion-del-trabajo.md).
3. Escribí el criterio de terminado antes que las instrucciones. Si no podés escribirlo, todavía no es un encargo.
4. Decidí quién va a verificar y si tiene tiempo para hacerlo: [la atención humana como restricción](la-atencion-humana-como-restriccion.md).

En software, cómo partir una tarea para un agente de código y escribir su criterio está en [descomposición en tareas](../../Desarrollo/Definicion/descomposicion-en-tareas.md) y [criterios de aceptación](../../Desarrollo/Definicion/criterios-de-aceptacion.md). Cómo planifica el agente por dentro, en [planificación de agentes](../../IA/Agentes/planificacion.md).

> [!NOTE] Sin fuente todavía: evidencia de que un encargo mejor especificado hace rendir más a un agente; la búsqueda no la encontró, y las guías de otros laboratorios no se consultaron.

Ver también: [Personas y agentes](personas-y-agentes.md), [quién hace qué](quien-hace-que.md).
