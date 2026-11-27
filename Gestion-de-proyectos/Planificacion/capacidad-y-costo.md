---
resumen: >-
  La capacidad es cuánto trabajo puede terminar un equipo por período y el costo es lo que se gasta en hacerlo; con personas la capacidad es casi fija y se paga aunque esté ociosa, y con agentes el costo crece con el uso y los reintentos, mientras la revisión de las personas acota cuánto se termina.
estado: vigente
estabilidad: semi
fuentes:
  - "PMI, PMBOK 8, dominios de finanzas y recursos (según resumen): https://www.pmi.org/standards/pmbok/about"
  - "Reinertsen, The Principles of Product Development Flow (2009) (según resúmenes): https://www.informit.com/articles/article.aspx?p=2928185&seqNum=6"
  - "Kapoor et al. (2024), AI Agents That Matter, arXiv 2407.01502 (según el abstract): https://arxiv.org/abs/2407.01502"
  - "Anthropic, How we built our multi-agent research system (2025) (según resumen): https://www.anthropic.com/engineering/multi-agent-research-system"
  - "Anthropic, Building effective agents (según resumen): https://www.anthropic.com/research/building-effective-agents"
  - "OpenTelemetry, convenciones semánticas de IA generativa para spans de agente (según resumen): https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/index.md"
  - "Gestion-de-proyectos/.investigacion/planificacion-y-riesgo.md"
  - "Gestion-de-proyectos/.investigacion/personas-y-agentes.md"
  - "Gestion-de-proyectos/.investigacion/seguimiento.md"
aliases: [capacidad, capacity, costo del proyecto, project cost, presupuesto, budget, utilización, utilization, costo por tarea, costo de agentes]
creado: 2026-11-27
revisado: 2026-11-27
---

# Capacidad y costo

La capacidad es cuánto trabajo puede terminar un equipo por período y el costo es lo que se gasta en hacerlo; con personas la capacidad es casi fija y se paga aunque esté ociosa, y con agentes el costo crece con el uso y los reintentos, mientras la revisión de las personas acota cuánto se termina.

La capacidad pone el ritmo del [pronóstico](pronostico.md): con las piezas de la [descomposición](descomposicion-del-trabajo.md) y el ritmo al que se terminan sale cuándo se termina todo. El costo entra a la [justificación](../Encuadre/justificacion.md) del proyecto y se controla contra el presupuesto en [medir el avance](../Seguimiento/medir-el-avance.md). Según un resumen de la 8.ª edición del PMBOK, los estándares reparten esto entre los dominios de recursos y de finanzas; esta base los junta porque con agentes una cosa se convierte en la otra.

## Cargar a todos al 100 % alarga el proyecto

La intuición de gestión dice que un recurso ocioso es plata perdida. Reinertsen, practicante, sostiene lo contrario, según resúmenes de su libro: el costo del trabajo que espera en una cola supera al de los recursos ociosos, y operar cerca del 100 % de utilización es mala economía. Cuando todos están ocupados, cada pieza nueva espera, y la espera alarga el plazo de todo lo que está en curso. La matemática de colas que lo sostiene y la ley de Little están en [trabajo en curso y colas](../Seguimiento/trabajo-en-curso-y-colas.md).

La consecuencia para planificar es que la capacidad útil no es la suma de las horas disponibles. Es lo que el sistema termina por semana sin que la cola crezca, y se mide con el rendimiento real.

## Personas: capacidad fija que se paga por período

Una persona es capacidad fija: cuesta lo mismo por mes haga lo que haga, y su disponibilidad se reparte entre proyectos. En un servicio que se lanza con tres personas a media dedicación, la capacidad no son tres personas: es media jornada de cada una, menos lo que se pierde al cambiar de un trabajo a otro. Cuántos proyectos en paralelo aguanta un equipo se decide en [portafolio](../Gobierno-y-cierre/portafolio.md).

## Agentes: costo variable por uso y por reintento

Un agente cuesta por lo que consume, no por estar disponible. La lectura de esta base, sin fuente específica todavía, es que el costo de un agente es variable con el uso y con los reintentos, y que su capacidad no la acota una agenda sino el presupuesto y la supervisión de las personas. Una tarea que el agente resuelve en un intento cuesta poco; una que falla, se reintenta y vuelve tres veces de la revisión puede costar más que hacerla a mano.

Dos fuentes apoyan la forma del costo, no su monto:

- Kapoor et al. (2024) proponen evaluar a los agentes por costo además de por exactitud: "Our focus on cost in addition to accuracy motivates the new goal of jointly optimizing the two metrics", según el abstract. Medir solo si el agente acierta esconde cuánto costó acertar.
- Anthropic informó que su sistema de investigación con varios agentes usa ~15× más tokens que una conversación de chat, y advierte que solo conviene si el valor de la tarea justifica el costo. El dato y sus límites están en [patrones de trabajo](../Personas-y-agentes/patrones-de-trabajo.md).

Esta base no registra precios por token: cambian seguido y envejecerían la nota. Lo que dura es la estructura del costo: tokens por intento, intentos por tarea y horas de revisión humana por tarea.

> [!NOTE] Sin fuente todavía: un estudio revisado por pares que compare el costo de agentes con el de horas-persona en proyectos reales, y una fuente sobre topes de gasto como práctica.

## El presupuesto de un agente

Como el costo es variable, el presupuesto se convierte en un límite que se le fija al agente al delegar: un máximo de intentos, de tiempo o de gasto por tarea y por período. Anthropic recomienda condiciones de parada como "a maximum number of iterations". Cómo se fija ese presupuesto junto con la intención, los límites y el criterio de terminado está en [delegar a un agente](../Personas-y-agentes/delegar-a-un-agente.md). Qué pasa cuando el gasto pronosticado sale del tope está en [problemas y escalamiento](../Incertidumbre-y-riesgo/problemas-y-escalamiento.md).

Medir el costo por tarea todavía exige armarlo a mano. Las convenciones abiertas de telemetría para IA generativa cuentan los tokens de entrada y de salida de cada paso, pero, según un resumen de la especificación, siguen en desarrollo y no definen un atributo de costo ni de tarea. El costo de una tarea se obtiene sumando los pasos de esa tarea y multiplicando por el precio vigente. Las herramientas que lo registran van a la ficha de [herramientas de seguimiento](../Seguimiento/herramientas-de-seguimiento.md).

## La capacidad que limita es la revisión

Si los agentes ejecutan en paralelo y una persona revisa, la capacidad del sistema es la de esa persona. Agregar agentes sin agregar capacidad de revisión solo alarga la cola de lo que espera ser aceptado. Es una inferencia de esta base, coherente con Reinertsen y con la teoría de restricciones, y está desarrollada en [la atención humana como restricción](../Personas-y-agentes/la-atencion-humana-como-restriccion.md).

Para planificar, eso cambia qué se cuenta. Se cuenta cuántas piezas por semana puede aceptar con evidencia quien revisa, cuánto retrabajo vuelve y cuánto cuesta cada intento del agente. Las horas-persona por tarea, que eran la unidad del plan clásico, [pierden peso](../Fundamentos/lo-que-pierde-peso-en-gestion-de-proyectos.md).

Los recursos canónicos son Kapoor et al. (2024), para evaluar costo junto con exactitud, y el libro de Reinertsen, para la economía de las colas. Fijarse en que una tarea barata que pide varias rondas de revisión humana puede costar más que hacerla a mano.
