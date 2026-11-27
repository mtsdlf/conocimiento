---
resumen: >-
  Los patrones de trabajo son las formas de repartir un trabajo entre personas y agentes: un orquestador que reparte y junta, hacer y revisar en manos distintas, piezas en paralelo, una cadena de pasos o una mesa de entrada que deriva. Se toman de los patrones de diseño de agentes y se leen como organización del trabajo.
estado: borrador
estabilidad: semi
fuentes:
  - "Anthropic (2024-12-19), Building effective agents (resumen): https://www.anthropic.com/research/building-effective-agents"
  - "Anthropic (2025-06-13), How we built our multi-agent research system (resumen): https://www.anthropic.com/engineering/multi-agent-research-system"
  - "Feng, McDonald y Zhang (2025), Levels of Autonomy for AI Agents, arXiv 2506.12469 (abstract): https://arxiv.org/abs/2506.12469"
  - "Gestion-de-proyectos/.investigacion/personas-y-agentes.md"
aliases: [patrones de organización con agentes, orquestador y trabajadores, orchestrator-workers, hacer y revisar, maker-checker, evaluador-optimizador, multiagente]
creado: 2026-11-27
revisado:
---

# Patrones de trabajo

Los patrones de trabajo son las formas de repartir un trabajo entre personas y agentes: un orquestador que reparte y junta, hacer y revisar en manos distintas, piezas en paralelo, una cadena de pasos o una mesa de entrada que deriva. Se toman de los patrones de diseño de agentes y se leen como organización del trabajo.

Los patrones vienen del diseño de sistemas con modelos, donde están descritos como código: cómo se encadenan llamadas, qué decide el modelo y qué el programa. Eso está en [patrones de flujo](../../IA/Agentes/patrones-de-flujo.md). Acá se mira otra cosa: qué forma toma el equipo cuando algunos de sus miembros son agentes. La lectura como organización es de esta base; ninguna fuente compara un patrón con una organización humana equivalente.

## Cinco formas de repartir, vistas como un equipo

Anthropic describe, en su guía de 2024, cinco patrones: encadenamiento, enrutamiento, paralelización, orquestador-trabajadores y evaluador-optimizador. Cada uno tiene un equivalente conocido en un equipo humano:

| Patrón | Qué hace | Equivalente en un equipo | Quién suele ser persona |
|---|---|---|---|
| Encadenamiento | Un paso le pasa el resultado al siguiente, con un control entre medio | Una línea de producción con puntos de inspección | Quien aprueba en los puntos de control |
| Enrutamiento | Una entrada se clasifica y va a quien corresponde | Una mesa de entrada que deriva pedidos | Quien atiende los casos que no encajan |
| Paralelización | Varias piezas independientes se hacen a la vez y se juntan | Un equipo que se reparte capítulos | Quien junta y resuelve contradicciones |
| Orquestador y trabajadores | Uno parte el trabajo sobre la marcha, lo reparte y sintetiza | Un jefe de equipo que descompone y arma el resultado | El orquestador, o quien recibe su síntesis |
| Evaluador-optimizador | Uno produce y otro critica en un bucle hasta que pasa | Hacer y revisar (maker-checker) | Quien fija el criterio con el que se revisa |

La última columna es criterio de esta base. Responde a la pregunta de [quién hace qué](quien-hace-que.md): en cada patrón hay un punto donde una persona decide o responde.

## Hacer y revisar en manos distintas

Para esta base, el patrón que más importa en un proyecto es el de hacer y revisar. Esta base supone (ninguna fuente consultada lo mide) que quien produjo algo es mal juez de su propio trabajo, y que eso vale también para un agente que dice haber terminado. Con agentes, separar los papeles parece costar poco, aunque cada revisión consume tokens: un agente produce y otro revisa contra el criterio de terminado.

El límite es que el revisor automático comparte puntos ciegos con el que produjo si usan el mismo modelo o el mismo encargo. Esto es inferencia de esta base. Por eso la revisión entre agentes filtra, pero la aceptación final sigue el criterio de [aceptar con evidencia](../Seguimiento/aceptar-con-evidencia.md). En software, las señales concretas de trabajo inventado están en [verificar lo que hizo un agente](../../Desarrollo/Verificacion/verificar-lo-que-hizo-un-agente.md).

## Persona en el bucle o en el borde

Que una persona apruebe antes de seguir, o que solo vigile y pueda intervenir, es a la vez un patrón y un nivel de autonomía. Se trata en [niveles de autonomía](niveles-de-autonomia.md), que lo vincula con los niveles de aprobador y observador de Feng y colegas. Acá alcanza con una consecuencia: cada punto de aprobación es una cola que espera a una persona, y su costo se ve en [la atención humana como restricción](la-atencion-humana-como-restriccion.md).

## Cuándo conviene repartir entre muchos agentes

Repartir entre muchos agentes cuesta más y no siempre rinde. El caso documentado es el sistema de investigación de Anthropic, con un agente líder y subagentes. Según un resumen de su post, "outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval". El costo: los agentes usan "about 4× more tokens than chat interactions", y los sistemas multiagente, unas 15 veces más que el chat. En un benchmark de búsqueda, el uso de tokens solo explicó alrededor del 80 % de la varianza del resultado.

El mismo post marca dónde no sirve: cuando todos los agentes necesitan el mismo contexto, cuando hay muchas dependencias entre piezas y en la mayoría de las tareas de código, que tienen menos partes paralelizables que la investigación. Es una evaluación interna de un laboratorio que vende el modelo. La disputa con quienes recomiendan un solo agente para escribir código está en [patrones de flujo](../../IA/Agentes/patrones-de-flujo.md).

Traducido a un proyecto, como lectura de esta base: paralelizar entre agentes rinde en trabajo que se lee y se resume (relevar proveedores, comparar normativas, revisar fuentes), donde las piezas no comparten decisiones. Lo que tiene que quedar coherente (un plan, un contrato, un cambio en un sistema) va en un solo hilo. Es el criterio que esta base propone también para un equipo humano: repartir lo que se puede hacer sin coordinarse; no está comparado con evidencia. El costo de ese cómputo entra en [capacidad y costo](../Planificacion/capacidad-y-costo.md).

> [!NOTE] Sin fuente todavía: estudios independientes de patrones multiagente en trabajo real, y cualquier comparación entre un patrón con agentes y una organización humana equivalente.

Ver también: [Personas y agentes](personas-y-agentes.md), [delegar a un agente](delegar-a-un-agente.md), [descomposición del trabajo](../Planificacion/descomposicion-del-trabajo.md).
