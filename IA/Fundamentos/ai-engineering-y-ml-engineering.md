---
resumen: >-
  AI engineering se diferencia de ML engineering en que adapta un modelo base que entrenó otro en
  lugar de entrenar uno propio, y por eso pone el peso en la evaluación y en el producto antes que
  en el modelado; la pila se divide en tres capas (aplicación, desarrollo de modelos e
  infraestructura).
estado: borrador
estabilidad: semi
fuentes:
  - https://newsletter.pragmaticengineer.com/p/the-ai-engineering-stack
  - https://www.latent.space/p/ai-engineer
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - https://github.com/chiphuyen/aie-book
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/resources.md
  - https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html
  - https://applied-llms.org/
  - https://hamel.dev/blog/posts/evals/
  - https://arxiv.org/abs/2604.16304
  - https://arxiv.org/abs/2507.09089
  - https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
  - https://80000hours.org/podcast/episodes/ai-workplace-mit-study/
aliases: [AI engineering vs ML engineering, AI engineer, ML engineer, ingeniería de IA, ingeniería de ML, AI engineering stack, pila de AI engineering]
creado: 2026-11-27
revisado:
---

# AI engineering y ML engineering

AI engineering se diferencia de ML engineering en que adapta un modelo base que entrenó otro en
lugar de entrenar uno propio, y por eso pone el peso en la evaluación y en el producto antes que
en el modelado; la pila se divide en tres capas (aplicación, desarrollo de modelos e
infraestructura).

## Qué se deja de hacer y qué se hace más

La diferencia central es dónde empieza el trabajo. Huyen, en el capítulo 1 de *AI Engineering*
(extracto publicado en The Pragmatic Engineer, mayo de 2025), lo dice en tres frases: "AI
engineering focuses less on modeling and training, and more on model adaptation"; "This makes
evaluation a much bigger problem in AI engineering"; y "ML knowledge is no longer a must-have for
building AI applications".

| | ML engineering | AI engineering |
|---|---|---|
| Punto de partida | Juntar datos y entrenar un modelo | Un [modelo base](../Modelos/modelo-base.md) ya entrenado, propio de otro |
| Dónde se adapta | Las features y los pesos | El [contexto](../Contexto/contexto.md), las herramientas y, si hace falta, el [ajuste](../Ajuste/ajuste.md) |
| Problema más difícil | Que el modelo aprenda | Saber si la salida sirve: la [evaluación](../Evaluacion/evaluacion.md) |
| Orden | Modelo primero, producto después | Producto primero, datos después |

El cambio de orden también es de Huyen: "With traditional ML engineering, you usually start with
gathering data and training a model", mientras que ahora "it's possible to start with building the
product first". Como el modelo está al alcance de cualquiera, "differentiation must be gained
through the application development process". Según el resumen de su capítulo 10, "AI engineering
is moving closer to product".

Lo que no cambia, según los resúmenes del libro, es buena parte del oficio de base: "many principles
from ML engineering are still applicable to AI engineering". Y la pregunta que más se saltea es
previa a la técnica: "whether you should build it", que en este tema trata
[planificar una aplicación](../planificar-una-aplicacion.md). La tabla es una síntesis de esta base
a partir de esas citas.

## La pila en tres capas

Huyen divide el oficio en tres capas, de la más cercana al usuario a la más cercana al hardware.
Las definiciones son citas del extracto del capítulo 1; el capítulo entero no se leyó.

| Capa | Qué es, según Huyen | Dónde está en este tema |
|---|---|---|
| Desarrollo de la aplicación | "providing a model with good prompts and necessary context" | [Contexto](../Contexto/contexto.md), [Agentes](../Agentes/agentes.md) y [Evaluación](../Evaluacion/evaluacion.md) |
| Desarrollo de modelos | "tooling for developing models" | [Ajuste](../Ajuste/ajuste.md) y sus datos |
| Infraestructura | "tooling for model serving, managing data and compute, and monitoring" | [Producción](../Produccion/produccion.md) |

La correspondencia entre capas y verticales es de esta base (la entrada [IA](../ia.md) la usa para ordenar el tema), igual que la lectura que sigue: quien construye productos pasa la
mayor parte del tiempo en la primera capa, toca la segunda cuando la evaluación muestra un límite
que el contexto no resuelve (la decisión está en [prompt, RAG o finetuning](../prompt-rag-o-finetuning.md))
y la tercera cuando el costo o la latencia lo piden.

Cómo se reparten esas capas entre los puestos que publican las empresas no lo dice el libro, que
describe capas y tareas, no roles. Ese cruce, con los avisos leídos, está en
[el caso de los roles de AI engineering](../../Presentacion-profesional/Posicionamiento/caso-roles-de-ai-engineering.md),
dentro del tema Presentación profesional, que es donde vive el mercado laboral del oficio.

## De dónde sale el rol

El nombre "AI engineer" se popularizó con un ensayo de Swyx y Latent Space, "The Rise of the AI
Engineer" (junio de 2023). Define el oficio como "productionizing AI APIs and OSS models" y da una
razón de oferta: "There are ~5000 LLM researchers in the world, but ~50m software engineers". Si
el modelo ya viene hecho, quien lo lleva a un producto no tiene que ser investigador: alcanza con
saber construir software y aprender a evaluar.

El mismo ensayo matiza el entusiasmo. Dice que el prompt engineering "was both overhyped and here
to stay", y que el rol puede sentirse "inferior to people with good Data Science/ML backgrounds".
Para quien se prepara para un puesto, la lectura de esta base es que el oficio no pide saber
entrenar modelos, pero sí medir: la [evaluación](../Evaluacion/evaluacion.md) es lo que separa un
prototipo de un producto.

> [!NOTE]
> Sin fuente todavía: si se cumplió la predicción de Swyx de 2023 de que sería "the highest-demand
> engineering job of the decade", con datos de empleo posteriores. Los datos de mercado que hay
> están en [Presentación profesional](../../Presentacion-profesional/Posicionamiento/caso-roles-de-ai-engineering.md).

## El sesgo de comunidad de las voces del campo

Las voces de referencia del oficio son pocas y se conocen entre sí. Huyen, Hamel Husain y Eugene
Yan escriben los textos que todo el mundo cita; Yan y Husain son coautores, con Bryan Bischof,
Charles Frye, Jason Liu y Shreya Shankar, de *What We've Learned From A Year of Building with LLMs*
(2024); y la lista de recursos del libro de Huyen recomienda a Yan, a Husain y a ese ensayo. Este
tema se construyó leyéndolos, y hereda su mirada: pro-evaluación y pro-producto.

Por eso una coincidencia entre ellos parece más firme de lo que es: que se empiece por el producto
lo dicen Huyen, Swyx y los resúmenes del libro, y cuentan como una opinión, no como tres
confirmaciones. Que Husain defienda la
evaluación en su propio blog y también como coautor de *Applied LLMs* no suma una segunda fuente
independiente sobre esa tesis.

> [!IMPORTANT]
> **Que la evaluación va primero es criterio, no hecho medido.** Husain escribe que los productos
> que fallan "almost always share a common root cause: a failure to create robust evaluation
> systems". Es una afirmación retrospectiva, sin denominador (cuántos productos que fallaron sí
> evaluaban) y sin grupo de comparación. La única investigación con método que se encontró son 19
> entrevistas a practicantes (van der Maden y otros, preprint de 2026): hallaron prácticas que van
> "from informal 'vibe checks' to organizational meta-work" y concluyen que las informales "appear
> to be reasonable adaptations to LLM characteristics, not simply methodological failures". El
> argumento a favor sigue en pie: sin una medida no se sabe si un cambio mejoró. La propia Huyen
> advierte también en la otra dirección, contra "Start too complex".

Hay otros tres sesgos documentados que tocan a quien lee el campo:

- **La percepción de quien usa la IA.** En el ensayo controlado de METR (2025), los desarrolladores
  creyeron haber ahorrado 20 % de tiempo y se midió que tardaron 19 % más; economistas y expertos
  en ML habían predicho reducciones de 39 % y 38 %, según el abstract. El detalle está en
  [Agentes](../Agentes/agentes.md).
- **La cifra que circula sin método.** El informe preliminar del proyecto NANDA del MIT (2025), no
  revisado por pares, dice que "95% of organizations are getting zero return". Sale de 52
  entrevistas y 153 encuestados, mide el éxito como un impacto "marked and sustained" a seis meses
  del piloto y cuenta como fracaso a quien no llegó a producción. Circuló como "el 95 % de los
  proyectos de IA fracasa" cuando el PDF todavía pedía un formulario, según el análisis de 80,000
  Hours.
- **El proveedor como fuente.** Muchas de las guías más leídas (sobre agentes, contexto o
  recuperación) las publican laboratorios y empresas sobre sus propios sistemas. Son primarias para
  su producto e interesadas en todo lo demás.

## Cómo leer una afirmación del campo

Pasos armados por esta base a partir de los sesgos de arriba:

1. Fijate quién lo dice y si cita a alguien de fuera de la misma comunidad.
2. Buscá el denominador: de cuántos casos sale y contra qué se compara.
3. Separá lo medido (un ensayo, un benchmark con método) de lo observado en la práctica.
4. Si la fuente vende el producto que recomienda, tomala como documentación de ese producto.
5. Buscá la evidencia en contra antes de tratar la afirmación como hecho.

## Qué leer sobre el oficio

Huyen y Orosz, ["The AI Engineering Stack"](https://newsletter.pragmaticengineer.com/p/the-ai-engineering-stack),
para la definición y las tres capas, y Swyx, ["The Rise of the AI Engineer"](https://www.latent.space/p/ai-engineer),
para el origen del rol. Fijarse en cómo cada uno define qué se deja de hacer (entrenar) y qué se
hace más (evaluar y construir producto). Del libro, el capítulo 1 completo (esta base solo leyó el
extracto). Para el contrapeso, van der Maden y otros,
["Results-Actionability Gap"](https://arxiv.org/abs/2604.16304): fijarse en las diez prácticas y en
que es una muestra de 19 sin medir resultados. El resto está en la [bibliografía de IA](bibliografia-de-ia.md),
y la historia que explica el cambio de oficio, en [historia de la IA generativa](historia-de-la-ia-generativa.md).
