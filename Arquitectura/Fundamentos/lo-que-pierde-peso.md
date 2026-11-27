---
resumen: >-
  Lo que pierde peso son las prácticas y estilos que este tema dejó fuera o puso en segundo plano
  (entrenar desde cero, trucos de prompt, frameworks de agentes pesados, SOA con ESB, space-based,
  ML clásico a medida, microservicios por defecto, GoF primero), cada uno con la evidencia a favor
  y en contra y con quién lo dice.
estado: borrador
estabilidad: semi
fuentes:
  - https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html
  - https://github.com/chiphuyen/aie-book
  - https://www.anthropic.com/engineering/building-effective-agents
  - https://www.anthropic.com/engineering/multi-agent-research-system
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - https://openai.com/index/harness-engineering/
  - https://cognition.com/blog/dont-build-multi-agents
  - https://arxiv.org/abs/2407.01502
  - https://www.thoughtworks.com/en-us/radar/techniques/summary/
  - https://www.thoughtworks.com/en-us/radar/techniques/agent-skill-cognitive-surrender
  - https://www.thoughtworks.com/en-us/radar/techniques/blanket-frontier-model-usage
  - https://www.thoughtworks.com/en-us/radar/techniques/esbs-in-api-gateway-s-clothing
  - https://www.thoughtworks.com/radar/archive
  - https://arxiv.org/abs/2303.17564
  - https://arxiv.org/abs/2305.05862
  - https://arxiv.org/abs/2310.11324
  - https://arxiv.org/abs/2406.06608
  - https://martinfowler.com/articles/microservices.html
  - https://nealford.com/books/SAF2e.html
  - https://www.oreilly.com/library/view/software-architecture-patterns/9781491971437/ch05.html
  - https://arxiv.org/abs/2207.08815
  - https://pubmed.ncbi.nlm.nih.gov/39780007/
  - https://arxiv.org/abs/2512.00888
  - https://world.hey.com/dhh/even-amazon-can-t-make-sense-of-serverless-or-microservices-59625580
  - https://www.infoq.com/news/2023/05/prime-ec2-ecs-saves-costs/
  - https://martinfowler.com/bliki/MicroservicePremium.html
  - https://martinfowler.com/bliki/MonolithFirst.html
  - https://www.martinfowler.com/articles/dont-start-monolith.html
  - https://www.infoq.com/news/2020/05/monolith-decomposition-newman/
  - https://norvig.com/design-patterns/
  - https://github.com/johnousterhout/aposd-vs-clean-code
aliases: [posición contraria, lo que ya no conviene estudiar primero]
creado: 2026-11-27
revisado:
---

# Lo que pierde peso

Lo que pierde peso son las prácticas y estilos que este tema dejó fuera o puso en segundo plano
(entrenar desde cero, trucos de prompt, frameworks de agentes pesados, SOA con ESB, space-based, ML
clásico a medida, microservicios por defecto, GoF primero), cada uno con la evidencia a favor y en
contra y con quién lo dice.

"Pierde peso" quiere decir que conviene estudiarlo después, no que esté muerto. Casi todo es
criterio de esta base, y ningún ítem tiene un estudio independiente que lo zanje.

## El Radar no respalda la mayoría

El Thoughtworks Technology Radar marca con su anillo exterior lo que conviene evitar. Hoy ese anillo
se llama **Caution**; antes se llamaba **Hold**, y no se sabe en qué edición cambió. Entre 2024 y 2026,
en lo que se pudo verificar, **ninguno de estos ítems figura en Hold o Caution**: ni microservicios
por defecto, ni space-based, ni GoF, ni entrenar desde cero. Solo tocan la lista, de forma indirecta,
los frameworks de agentes pesados ("Agent skill cognitive surrender", Caution, noviembre de 2026),
usar el modelo más grande para todo ("Blanket frontier model usage", Caution, noviembre de 2026) y la
ESB (Hold, octubre de 2020). No se pudieron leer completos los volúmenes de 2024 y 2025.

## Resumen por ítem

| Ítem | Quién lo dice | Evidencia en contra | Veredicto |
|---|---|---|---|
| Entrenar desde cero | Criterio de la base | El modelo de dominio gana en tareas de dominio | Pierde peso, con excepciones |
| Trucos de prompt | Anthropic, criterio de la base | El formato del prompt mueve hasta 76 puntos | Pierden peso los trucos, no la técnica |
| Frameworks de agentes pesados | Huyen, Anthropic, Radar | Multiagente con +90,2 % en un caso | Pierde peso el framework opaco |
| SOA con ESB | Lewis y Fowler, Radar 2020 | Richards y Ford mantienen el estilo | Pierde peso la ESB, no el servicio |
| Space-based | Criterio de la base | No hay evidencia ni a favor ni en contra | Uso público escaso, no obsoleto |
| ML clásico a medida | Criterio de la base | Los árboles siguen ganando en tabular | No pierde peso en tabular |
| Microservicios por defecto | Fowler, Newman, DHH | Tilkov; escala de equipos | Pierde peso como punto de partida |
| GoF primero | Criterio de la base | Siguen siendo vocabulario común | Sin evidencia sobre el orden |

## Entrenar modelos propios desde cero

**A favor de dejarlo fuera.** BloombergGPT (50.000 millones de parámetros) se entrenó con unos 708.000
millones de tokens. Li et al. (2023) encontraron
que modelos generales en zero o few-shot superan a ese modelo de dominio y a modelos ajustados en
muchas tareas (según el resumen del buscador). **En contra.** BloombergGPT reportó ganar "por amplios
márgenes" en tareas financieras, y Li et al. muestran que el modelo general falla donde hace falta
conocimiento de dominio. Huyen no dice "nunca": dedica el capítulo 7 a cuándo sí hacer fine-tuning,
que es otra cosa que entrenar desde cero. El Radar puso modelos de pesos abiertos y modelos chicos en
Trial. **Quién.** Criterio de esta base; Huyen solo critica insistir en fine-tuning "when prompting
works". La decisión práctica está en [prompt, RAG o fine-tuning](../Sistemas-con-modelos/prompt-rag-o-finetuning.md).

## Prompt engineering como conjunto de trucos

**A favor.** Anthropic presenta el *context engineering* como sucesor del prompt engineering, y el
Radar puso en Caution "Agent instruction bloat": instrucciones largas, contradictorias o viejas.
**En contra.** Sclar et al. midieron "performance differences of up to 76 accuracy points" por cambios
de formato que no cambian el sentido, y Schulhoff et al. sistematizaron 58 técnicas: hay un cuerpo de
técnica, no solo trucos. Huyen le dedica un capítulo entero. **Quién.** Anthropic y criterio de esta
base. El estudio de Sclar usa modelos de 2023; no se verificó si la sensibilidad bajó.

## Frameworks de agentes pesados

**A favor.** Huyen cuenta como error "Use an agentic framework when direct API calls work", porque
los frameworks "abstract away critical details, making it hard to understand and debug your system".
Anthropic pide "start by using LLM APIs directly" y sumar complejidad "only when it demonstrably
improves outcomes". El Radar (Caution) critica adoptar "heavyweight AI agent frameworks" sin
entenderlos. Kapoor et al. muestran que los benchmarks de precisión producen agentes "needlessly
complex and expensive". **En contra.** Anthropic reporta +90,2 % de su sistema multiagente frente a
un agente solo, con unas 15 veces más tokens, y el Radar tiene harness y runtimes de agentes en Trial
o Assess. **Quién.** Huyen y laboratorios que también venden SDK de agentes; no hay estudio
independiente. Lo que pierde peso es el framework opaco, no la orquestación. Ver
[agente](../Sistemas-con-modelos/agente.md).

## SOA con ESB

**A favor.** Lewis y Fowler oponen "smart endpoints and dumb pipes" a "the tendency to hide
complexity away in ESB's". El Radar (Hold, 2020) dice que centralizar orquestación y transformación
"adds architectural coupling, reduces transparency, and increases vendor lock-in". **En contra.** Los
mismos autores admiten que "others consider microservices to be one form of SOA", y Richards y Ford
mantienen la SOA orquestada en su índice de 2025. **Quién.** Thoughtworks, con postura histórica; no
apareció ninguna defensa reciente de la ESB. Lo que cae es la ESB como lugar de la lógica, no el
servicio como unidad.

## Space-based

Richards la presenta para escalabilidad, con nodos que comparten una grilla de datos en memoria;
según fuentes secundarias, es mala para consistencia fuerte y escrituras intensas. **No hay evidencia de que pierda
peso**: no se encontró un caso de adopción, ni una crítica independiente, ni una entrada del Radar.
Sigue en el índice de Richards y Ford. Corresponde decir "evidencia de uso pública escasa". **Quién.** Criterio de esta base.

## ML clásico a medida

La idea era que un LLM resuelve lo que antes pedía un modelo entrenado a medida. **La evidencia va
en contra en datos tabulares.** Grinsztajn et al. (2022), en 45 datasets, encontraron que los árboles
"remain state-of-the-art on medium-sized data". Un trabajo chico de 2025 (4 datasets) vio árboles que
terminaban en 0,40 s o menos contra 960 s de un modelo fundacional tabular. **A favor del cambio.**
TabPFN (Nature, 2025) supera a los métodos previos hasta 10.000 muestras, y el Radar puso los modelos
fundacionales para datos estructurados en Assess. Usar el modelo más grande para todo está en Caution.
**Quién.** Criterio de esta base, sostenido solo para tareas de lenguaje; no hay estudio que compare
costos de un LLM contra un modelo clásico en las mismas tareas.

## Microservicios por defecto

**A favor de dejarlos fuera como default.** Fowler: no considerarlos "unless you have a system that's
too complex to manage as a monolith" y "you shouldn't start a new project with microservices".
Newman: "Microservices should not be the default choice". DHH los llama "perhaps the biggest siren
song for needlessly complicating your system". Según InfoQ, Prime Video juntó un componente en un
solo proceso y logró "a 90% reduction in operational costs". **En contra.** Tilkov: "starting with a
monolith is usually exactly the wrong thing to do" si el sistema va a terminar en servicios, porque
partirlo después es difícil. Fowler admite que monolith-first es "by no means unanimous", y el caso
Prime Video movió un componente, no un sistema. **Quién.** Voces de práctica y consultoría; no hay
estudio empírico. La disputa es sobre dominio entendido y escala de equipos, no sobre rendimiento.
Ver [monolito modular](../Estilos/monolito-modular.md) y [microservicios](../Estilos/microservicios.md).

## Patrones GoF como lo primero que se estudia

**A favor de bajarlos.** Norvig (1996) mostró que 16 de 23 patrones son "invisible or simpler" en
lenguajes dinámicos (la cifra viene de un resumen). Ousterhout discute otra ortodoxia de diseño, la
descomposición extrema, que según él produce "teeny-tiny methods that suffer from both shallow
interfaces and entanglement". **En contra.** En los lenguajes de uso corriente los patrones siguen
siendo vocabulario común. **Quién.** Criterio de esta base; no hay estudio sobre el orden de
enseñanza. Los patrones de código viven en [Desarrollo](../../Desarrollo/desarrollo.md).

## Lo que gana peso

- **Evaluación propia** antes que las piezas: el centro de
  [Evaluación y observabilidad](../Evaluacion-y-observabilidad/evaluacion-y-observabilidad.md).
- **Context engineering**: en Adopt en el Radar de abril de 2026, y "Progressive context disclosure"
  en Adopt en noviembre de 2026. Ver [contexto y RAG](../Sistemas-con-modelos/contexto-y-rag.md).
- **Harness**: "coding harness for general-purpose agents" en Trial y "harness quality evaluation" en
  Assess (noviembre de 2026).
- **Chequeos automáticos**: "Feedback sensors for coding agents" en Trial (abril de 2026), heredero de
  la [fitness function](../Caracteristicas/fitness-function.md).
- **Monolito modular**: estilo nuevo en la segunda edición de Richards y Ford.
- **Modelos chicos y abiertos**: en Trial, frente al modelo más grande para todo.

## Qué leer de la posición contraria

Anthropic, ["Building effective agents"](https://www.anthropic.com/engineering/building-effective-agents),
con los pitfalls de Huyen: fijarse en "demonstrably improves outcomes". Para el resto, la
[bibliografía](bibliografia-de-arquitectura.md).
