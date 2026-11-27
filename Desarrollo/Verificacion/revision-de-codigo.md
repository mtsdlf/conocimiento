---
resumen: >-
  La revisión de código es leer un cambio antes de integrarlo para encontrar problemas y entenderlo.
  Con agentes se reparte en tres: una herramienta controla lo mecánico, otro agente con contexto
  limpio contrasta contra la especificación y una persona revisa intención, diseño y riesgo.
estado: borrador
estabilidad: semi
fuentes:
  - https://researchr.org/publication/BacchelliB13
  - https://research.google/pubs/modern-code-review-a-case-study-at-google/
  - https://code.claude.com/docs/en/best-practices
  - https://arxiv.org/html/2602.08915v1
  - https://arxiv.org/html/2602.02345v1
  - https://dora.dev/research/2025/dora-report/
  - https://arxiv.org/abs/2211.03622
  - https://www.thoughtworks.com/radar
aliases: [code review, revisión de pull request, revisión de PR, peer review, revisión por pares]
creado: 2026-11-27
revisado:
---

# Revisión de código

La revisión de código es leer un cambio antes de integrarlo para encontrar problemas y entenderlo. Con agentes se reparte en tres: una herramienta controla lo mecánico, otro agente con contexto limpio contrasta contra la especificación y una persona revisa intención, diseño y riesgo.

## Para qué sirve una revisión en la práctica

La razón que se declara para revisar es encontrar defectos, pero eso no es lo que más rinde. Bacchelli y Bird estudiaron la revisión en Microsoft (ICSE 2013) y, según los resúmenes de su trabajo, encontraron menos defectos de lo esperado y más transferencia de conocimiento, conciencia del equipo sobre lo que cambia y soluciones alternativas; solo una parte chica de los comentarios trata defectos. La clave de cualquier revisión, para ellos, es entender el cambio y su contexto.

Google estudió su propia práctica (Sadowski et al., ICSE SEIP 2018) con 12 entrevistas, una encuesta a 44 personas y los registros de 9 millones de cambios revisados. Según un resumen, la sostienen como herramienta educativa y de claridad. De ahí esta base lee que ni siquiera antes de los agentes la revisión servía como único control de defectos.

## Qué revisa cada uno

| Quién | Qué revisa | Por qué ahí |
|---|---|---|
| Herramienta | formato, lint, tipos, análisis estático, que las pruebas pasen | es determinista |
| Otro agente, con contexto limpio | el cambio contra la especificación, casos borde, huecos de corrección | no lo arrastra el razonamiento que produjo el código |
| Persona | intención, diseño, seguridad, lo que el agente no puede saber del negocio | conserva el traspaso de conocimiento que Bacchelli y Bird vieron como beneficio |

El reparto es síntesis de esta base; no lo afirma una fuente única. La fila de la persona incluye lo que Bacchelli y Bird vieron como beneficio principal: que alguien más entienda el código. Si nadie lo lee, ese beneficio se pierde, y es un costo que hay que nombrar cuando se decide cuánto revisar.

Los comentarios de estilo y de formato salen de la revisión humana, porque los absorbe la herramienta. La herramienta también corre antes: el Radar de Thoughtworks (vol. 34, abril de 2026, según un resumen) pone controles deterministas antes de la revisión humana.

## Por qué la revisión humana sola ya no alcanza

Es inferencia de esta base que, con agentes, el volumen de código a revisar sube y el contexto del cambio lo tiene el agente, no quien revisa. DORA 2025 describe la IA como amplificador: "AI's primary role is as an amplifier, magnifying an organization's existing strengths and weaknesses." Leído sobre la revisión (inferencia de esta base), un equipo con revisión débil recibe más cambios que revisar mal.

Según un resumen del Radar vol. 35 (noviembre de 2026), cuando la revisión no da abasto la supervisión puede volverse una formalidad: se aprueba por rutina lo que no se entiende. Eso inclina a revisar contra la especificación y la evidencia (pruebas, salida de comandos) más que leer línea por línea. Las señales concretas para revisar el trabajo de un agente están en [verificar lo que hizo un agente](verificar-lo-que-hizo-un-agente.md).

La revisión humana tampoco se puede soltar. Perry et al. (CCS 2023) encontraron, según su resumen, que quienes usaban un asistente escribían código menos seguro y a la vez creían que era más seguro. Esta base lo lee como un pedido de más control humano, no de menos.

## Cómo se pide una revisión a otro agente

La guía de buenas prácticas de Anthropic para su agente de código (leída el 2026-11-27) recomienda revisar el diff en una sesión nueva, "that never saw your conversation. It isn't swayed by the reasoning that produced the code". Una segunda sesión es "the easiest independent reviewer you can get". Advierte además que un revisor al que se le pide encontrar problemas "will always find something", y por eso el pedido recomendado dice "report gaps that affect correctness and skip style" y revisa contra la especificación escrita.

Un revisor puede tener solo herramientas de lectura, y esa restricción la aplica la herramienta, no el prompt. Pasos, con eso:

1. Abrí una sesión que no vio la conversación y dale el diff y la especificación (sale de [Definición](../Definicion/definicion.md)).
2. Pedile huecos que afecten la corrección, no estilo.
3. Leé sus hallazgos como hipótesis: verificá cada uno antes de corregir.
4. Lo que queda para vos es la intención y el riesgo.

## Cuánto se aceptan los cambios de los agentes

> [!IMPORTANT]
> Las tasas de aceptación de pull requests hechos por agentes en GitHub discrepan según el filtro, y todas vienen de preprints conocidos por su resumen. Un estudio sobre 7.156 PRs da 77,9 % para un agente y 61,6 % para otro; otro, con el subconjunto AIDev-pop, da entre 0,83 y 0,45 según el agente. Coinciden en que los cambios de documentación, build y CI se aceptan más que las funcionalidades, y que rendimiento y corrección de bugs se aceptan menos. No hay un estudio sobre cómo revisar código de agentes.

Cómo encaja la revisión en el flujo de ramas está en [trunk-based development](../../DevOps/Ramas-y-versiones/trunk-based-development.md); el recurso para entender qué pasa realmente en una revisión es Bacchelli y Bird (2013), en los apartados de motivaciones y resultados.
