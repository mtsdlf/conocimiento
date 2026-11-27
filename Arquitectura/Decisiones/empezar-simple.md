---
resumen: >-
  Empezar simple es arrancar con la versión más chica que podría funcionar y sumar una pieza solo
  cuando la medición muestra que hace falta; es el principio que comparten Chip Huyen y
  Anthropic, y que Fowler defiende para los monolitos.
estado: vigente
estabilidad: semi
fuentes:
  - https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html
  - https://huyenchip.com/2024/07/25/genai-platform.html
  - https://www.anthropic.com/engineering/building-effective-agents
  - https://www.anthropic.com/engineering/multi-agent-research-system
  - https://github.com/chiphuyen/aie-book
  - https://arxiv.org/abs/2407.01502
  - https://www.martinfowler.com/articles/dont-start-monolith.html
  - https://martinfowler.com/bliki/MonolithFirst.html
  - https://en.wikipedia.org/wiki/John_Gall_(author)
aliases: [start simple, simplicidad, ley de Gall, YAGNI]
creado: 2026-11-27
revisado: 2026-11-27
---

# Empezar simple

Empezar simple es arrancar con la versión más chica que podría funcionar y sumar una pieza solo
cuando la medición muestra que hace falta; es el principio que comparten Chip Huyen y
Anthropic, y que Fowler defiende para los monolitos.

No es una técnica con capítulo propio en Richards y Ford: es un criterio que atraviesa las demás
decisiones. En estilos aparece como la postura monolith-first de Fowler, partir de un
[monolito modular](../Estilos/monolito-modular.md) en lugar de microservicios (está disputada, ver abajo); en un sistema con modelos, como probar el prompt antes que el contexto,
y el contexto antes que el fine-tuning o un agente.

## Cada pieza agrega fallas nuevas

La razón es de costo. Huyen lo dice en el resumen del capítulo de arquitectura de *AI Engineering*:
"Each added component can improve capability, safety, or speed, but also adds complexity and new
failure modes". Una pieza que no hacía falta no solo cuesta construirla: suma una forma más de
fallar, algo más que observar y algo más que entender al depurar (desarrollo de esta base).

Por eso su arquitectura de referencia arranca con lo mínimo, "query, model, response", y suma
componentes de a uno ("progressively add more components"), evaluando en cada paso. La misma
fuente aclara: "A component can be skipped if your system works well without it". Lo que decide si
una pieza entra es la [evaluación](../../IA/Evaluacion/evals.md), no la
disponibilidad de una herramienta.

## Los errores de empezar complejo con modelos

Huyen cuenta "Starting too complex" entre los errores comunes al construir aplicaciones con IA
generativa, con dos ejemplos que se repiten:

- "Use an agentic framework when direct API calls work": sumar un framework de
  [agentes](../../IA/Agentes/agente.md) cuando unas llamadas directas al modelo alcanzan.
- "Insist on finetuning when prompting works": hacer fine-tuning cuando el prompt resuelve; la
  escalera completa está en [prompt, RAG o fine-tuning](../../IA/prompt-rag-o-finetuning.md).

Anthropic llega a lo mismo desde el lado de quien fabrica el modelo: "we recommend finding the
simplest solution possible, and only increasing complexity when needed". Recomienda empezar
llamando a las APIs directamente, porque los frameworks "often create extra layers of abstraction
that can obscure the underlying prompts", y sumar complejidad "only when it demonstrably improves
outcomes". Distingue además los workflows, con caminos de código predefinidos, de los agentes, que
deciden sus propios pasos; lo simple es el workflow (lectura de esta base).

Huyen agrega por qué la complejidad tienta: "It's easy to build a demo, but hard to build a
product", y "The journey from 0 to 60 is easy, whereas progressing from 60 to 100 becomes
exceedingly challenging". Según esta base, la tentación es atacar el tramo difícil con más piezas, cuando lo que
suele faltar es mirar los datos: "staring at data for just 15 minutes usually gives me some
insight", que es lo que sistematiza el
[análisis de errores](../../IA/Evaluacion/analisis-de-errores.md).

## Cuándo la complejidad sí paga

Empezar simple no es quedarse simple. Anthropic reporta que su sistema de investigación con varios
agentes rindió un 90,2% más que un agente solo en su evaluación interna, a costa de unas 15 veces
los tokens de un chat; y aclara que no sirve cuando los agentes comparten contexto, hay muchas
dependencias entre tareas o la tarea vale poco. La complejidad entró porque una medición la
justificó, que es justo la regla. Kapoor y otros advierten el otro lado: los benchmarks que solo
miran precisión empujan a agentes "needlessly complex and expensive"; el
[costo](../Caracteristicas/costo-y-latencia.md) también es una característica que se mide.

> [!IMPORTANT] En el canon, empezar simple está disputado. Fowler defiende empezar con un monolito
> y aclara que la postura es "by no means unanimous". Stefan Tilkov, en el mismo sitio, sostiene que
> "starting with a monolith is usually exactly the wrong thing to do" para un sistema que va a ser
> de microservicios, porque partirlo después es muy difícil. La disputa completa está en
> [lo que pierde peso](../Fundamentos/lo-que-pierde-peso.md).

> [!IMPORTANT] Todas las fuentes sobre frameworks de agentes frente a llamadas directas son
> autores de práctica o empresas que venden modelos (y SDK de agentes). No se encontró un estudio
> independiente que los compare.

## Gall y YAGNI

El principio es más viejo que los modelos. La ley de Gall, de *Systemantics* (publicado en 1975 como *General Systemantics*), dice, según
la paráfrasis de Wikipedia, que "a complex system that works is invariably found to have evolved
from a simple system that worked", y que uno complejo diseñado desde cero no funciona ni se puede
arreglar para que funcione. YAGNI ("you aren't gonna need it") es la versión del desarrollo ágil:
no construir hoy lo que se supone que se va a necesitar mañana.

> [!NOTE] Sin fuente todavía: la cita literal de Gall en el libro original (solo se leyó la
> paráfrasis de Wikipedia) y una fuente primaria de YAGNI.

## Qué leer

Huyen, "Common pitfalls when building generative AI applications" (2025), la sección "Starting too
complex", y Anthropic, "Building effective agents" (2024), las partes sobre cuándo usar agentes y
sobre frameworks. Fijarse en los casos concretos de cuándo no usar un agente, un framework o
fine-tuning, y en la frase "demonstrably improves outcomes": la complejidad se justifica con una
medición. Cada pieza que se suma se registra en un [ADR](adr.md) con la evidencia que la justificó.
