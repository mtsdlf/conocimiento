---
resumen: >-
  La entrevista de cambio (switch interview) reconstruye, con alguien que cambió de producto hace poco, la historia de ese cambio: desde el primer pensamiento hasta la compra y el primer uso. Es el método de Moesta y Spiek para encontrar el trabajo que el cliente quería resolver y las fuerzas que lo movieron o lo frenaron.
estado: borrador
estabilidad: semi
fuentes:
  - "Bob Moesta y Chris Spiek, How to Run a JTBD Switch Interview, jobstobedone.org (sin fecha): https://jobstobedone.org/switch-interview/ (leída a través del resumen de una herramienta)"
  - "Bob Moesta y Chris Spiek, The JTBD Timeline: First Thought to Purchase, jobstobedone.org (sin fecha): https://jobstobedone.org/the-timeline/ (leída a través del resumen de una herramienta)"
  - "thoughtbot, Playbook, Switch Interviews: https://thoughtbot.com/playbook/validation/switch-interviews (leída a través del resumen de una herramienta)"
  - "Bob Moesta (con Greg Engle según algunos listados), Demand-Side Sales 101 (2020), 224 págs. (según resúmenes; libro no leído)"
  - "UX/.investigacion/evaluacion-competitiva-y-cambio.md"
aliases: [switch interview, entrevista de switch, JTBD interview, entrevista JTBD, entrevista de línea de tiempo, timeline interview]
creado: 2026-11-22
revisado:
---

# Entrevista de cambio

La entrevista de cambio (switch interview) reconstruye, con alguien que cambió de producto hace poco, la historia de ese cambio: desde el primer pensamiento hasta la compra y el primer uso. Es el método de Moesta y Spiek para encontrar el trabajo que el cliente quería resolver y las fuerzas que lo movieron o lo frenaron.

Es una variante de la [entrevista de usuario](entrevista-de-usuario.md): comparte su forma (una conversación guiada, cualitativa) y su límite (cuenta lo que la persona recuerda, no lo que hizo). Se diferencia en el sujeto y en la regla de oro. No pregunta por la vida en general ni por la tarea, sino por una decisión de compra concreta y reciente, y la reconstruye evento por evento. El marco que la sostiene, el trabajo y las cuatro fuerzas (empuje, atracción, ansiedad y hábito), está en [jobs to be done](../../Marketing/Mercado-y-cliente/jobs-to-be-done.md).

## A quién se entrevista

Moesta y Spiek piden gente que cambió hace poco: "Interview people who switched in the last 30 to 90 days." Incluyen a quien estuvo a punto de cambiar y no lo hizo, y excluyen a los "best customers". El que se fue del producto propio hacia un rival también cambió, y su historia dice qué atrajo del otro lado (lectura de esta base; la guía no lo trata aparte).

En un SaaS, las tres fuentes son los clientes que llegaron en los últimos tres meses, los que se dieron de baja hacia un rival y los que hicieron una prueba gratis y no pagaron. Así la entrevista sirve al análisis de competidores: cada historia nombra contra qué se comparó el producto, que puede no ser un rival directo (ejemplo de esta base).

## La línea de tiempo del cambio

La entrevista ordena la historia en una línea de tiempo con estas etapas, según la página de los autores:

1. **Primer pensamiento**: "the moment someone first realizes they might need something different". Suele ser antes de lo que la persona dice, así que se sondea hacia atrás.
2. **Búsqueda pasiva**: la persona mira sin urgencia y no está lista para actuar.
3. **Primer evento**: algo cambia y "debería ver esto" pasa a "tengo que hacer algo".
4. **Búsqueda activa**: compara opciones y, al resignar unas cosas por otras, va definiendo el trabajo ("shaping the job in their mind").
5. **Segundo evento**: el disparador que la lleva de buscar a decidir.
6. **Decisión, compra y consumo**: la persona se imagina usándolo al comprar y lo usa de verdad después; la distancia entre las dos cosas define la satisfacción.

La línea puede durar medio segundo, en una compra impulsiva, o varios años, en una compra corporativa. Algunos resúmenes del libro de 2020 cierran la línea con el primer uso y el uso continuo en vez de con la compra.

## El guion: un documental, no una encuesta

La regla es pedir eventos y no opiniones. Moesta y Spiek proponen presentarse como quien hace un documental sobre lo que pasó, sin respuestas correctas, y preguntar una y otra vez "and then what happened?". El ancla es "When did you first start thinking about this?". Después se avanza por hechos concretos: qué pasó, dónde estaba, con quién y qué hizo justo después.

Las fuerzas no se preguntan; salen de los eventos. La guía sugiere hacerse el que no entiende, unir a propósito mal dos hechos para que la persona corrija, y no apurarse: "Rushing produces opinions, not events." Cuando la persona se contradice, no es un error: "Contradictions aren't errors. They're refinements." Thoughtbot usa la misma imagen del documental y pide detalles chicos (qué tenía puesto ese día), porque destraban el recuerdo.

Se planean de 45 a 90 minutos, con dos entrevistadores: "One person drives the conversation while the other listens for forces and timeline gaps." En la práctica se marca primero el momento de la compra y se rellena la línea saltando entre etapas a medida que la historia aparece.

## Cómo se analiza

Cada entrevista se vuelca a una línea de tiempo y a un diagrama de las cuatro fuerzas. Después se buscan, entre entrevistas, los trabajos y las fuerzas que se repiten. La guía no describe un método formal de agrupamiento: para ordenar los fragmentos sirve el [análisis temático](analisis-de-resenas.md#codificar-por-temas), con un código por fuerza. Thoughtbot pide una puesta en común al terminar cada entrevista y una ficha por entrevista en los días siguientes.

Lo que sale se usa en tres lados. Las fuerzas de ansiedad y de hábito muestran qué frena la adopción, que es material de [interacción](../Interaccion/interaccion.md) y de incorporación de usuarios. Las palabras literales del cliente sirven para el [posicionamiento](../../Marketing/Propuesta/posicionamiento.md) y los textos. Y las alternativas que la persona comparó dicen contra quién se compite de verdad, que alimenta la [identificación de competidores](../../Estrategia-competitiva/Analisis-de-competidores/identificacion-de-competidores.md).

Es prima del [win/loss](../../Estrategia-competitiva/Analisis-de-competidores/analisis-de-ventas-ganadas-y-perdidas.md), que entrevista a quien decidió una compra para saber por qué se ganó o se perdió. El win/loss mira la venta; la entrevista de cambio mira toda la historia anterior, incluido lo que pasó antes de que hubiera venta.

## Cuántas alcanzan y qué tan confiable es

Las cifras de cuántas entrevistas hacen falta son de practicantes, no de estudios:

| Fuente | Cuántas |
|---|---|
| Moesta y Spiek | "often within 5 to 8 interviews for a given job" aparecen patrones |
| thoughtbot | "Typically it takes about 8-10 interviews", aunque dicen haber hecho menos |

Los dos buscan fuerzas y líneas de tiempo que se repitan, no significancia estadística. La evidencia más cercana sobre saturación, la de Guest y otros (alrededor de 12 entrevistas en un grupo homogéneo), está en [entrevista de usuario](entrevista-de-usuario.md#cuantas-entrevistas-hacer) y no se midió con este método.

> [!IMPORTANT]
> El método depende del recuerdo retrospectivo, y su única defensa contra ese límite la dan sus propios autores. Moesta y Spiek fijan la ventana de 90 días porque "Memory fades fast; beyond about 90 days the details you need are gone", y piden eventos porque "Rushing produces opinions, not events". NN/g describe los límites de todo autorreporte (recuerdo imperfecto, omisiones, deseabilidad social), detallados en [entrevista de usuario](entrevista-de-usuario.md#lo-que-la-entrevista-no-puede-ver), y la entrevista de cambio los hereda. No se encontró ningún estudio que valide el método: ni cuánto coincide la línea de tiempo reconstruida con lo que pasó, ni si dos analistas sacan las mismas fuerzas de la misma entrevista. Una lectura prudente lo trata como una fuente de hipótesis sobre el trabajo y las fuerzas, que se contrastan con datos de uso o con un [experimento](../Evaluacion/metricas-de-ux.md#donde-entra-el-experimento-ab).

> [!NOTE] Sin fuente todavía: evidencia empírica sobre la validez y la confiabilidad de la entrevista de cambio, y la estructura de capítulos de Demand-Side Sales 101 (editorial y capítulos sin verificar).

## Qué leer

La guía de los autores, [How to Run a JTBD Switch Interview](https://jobstobedone.org/switch-interview/), es corta y concreta: fijarse en a quién reclutar, la pregunta ancla y la regla de eventos y no opiniones. La página de la [línea de tiempo](https://jobstobedone.org/the-timeline/) explica cada etapa. Para el marco completo, Moesta, *Demand-Side Sales 101* (2020), que según sus resúmenes junta las fuentes de energía del comprador, las cuatro fuerzas y la línea de tiempo.
