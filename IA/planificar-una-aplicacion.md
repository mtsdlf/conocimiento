---
resumen: >-
  Planificar una aplicación con un modelo adentro es decidir, antes de construir, si el caso de uso
  necesita un modelo, cuánto error tolera, qué tiene que lograr el primer hito y cómo se va a
  mantener cuando el modelo cambie; casi siempre lo que falla es el producto o el problema, no el
  modelo.
estado: borrador
estabilidad: semi
fuentes:
  - https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/
  - https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-ii/
  - https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-iii-strategy/
  - https://hamel.dev/blog/posts/evals/
  - https://hamel.dev/blog/posts/evals-faq/
  - https://www.rand.org/pubs/research_reports/RRA2680-1.html
  - https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
  - https://80000hours.org/podcast/episodes/ai-workplace-mit-study/
aliases: [planificar una aplicación de IA, AI product planning, caso de uso de IA, should we build it]
creado: 2026-11-27
revisado:
---

# Planificar una aplicación

Planificar una aplicación con un modelo adentro es decidir, antes de construir, si el caso de uso
necesita un modelo, cuánto error tolera, qué tiene que lograr el primer hito y cómo se va a mantener
cuando el modelo cambie; casi siempre lo que falla es el producto o el problema, no el modelo.

Cruza todo el tema. Usa la [evaluación](Evaluacion/evaluacion.md) para definir qué es "anda", elige
entre [prompt, RAG o finetuning](prompt-rag-o-finetuning.md) para el primer hito y prepara las capas
de [sistemas con modelos](Produccion/sistemas-con-modelos.md) que se van a sumar después. Según el
resumen de capítulos del libro, Huyen no tiene una sección de planificación: lo más cercano es la
pregunta de si conviene construirlo, en el capítulo 1. Lo que sigue sale sobre todo de practicantes
(Huyen en sus posts, Yan et al., Husain) y de dos estudios con método limitado.

## Si el caso de uso necesita un modelo

La primera pregunta es si hace falta IA generativa. Huyen la pone primera en su lista de errores
comunes: "Not everything is a nail." Un modelo emite texto probable, no verdadero (ver
[alucinación](Modelos/alucinacion.md)); un problema que una regla, una búsqueda o un formulario
resuelven no gana nada con él.

El otro error que Huyen describe es elegir los casos de uso por pedido interno: cada área propone el
suyo y salen muchas aplicaciones chicas de poco impacto, sin una estrategia de conjunto. Por
inferencia de esta base, el caso de uso se elige como cualquier apuesta de producto, mirando los
[cuatro riesgos](../Producto/Descubrimiento/cuatro-riesgos.md) y probando los supuestos antes de
construir, como en un [producto mínimo viable](../Emprender/Validacion/producto-minimo-viable.md).

## Cuánto error tolera el caso

El nivel de exigencia depende del daño que hace una respuesta mala. Yan et al. lo plantean con dos
extremos: un chatbot de atención que da consejos médicos o financieros necesita "a very high bar for
safety and accuracy", mientras que en otros casos "excessively strict requirements only slow progress
without adding much value". La tolerancia decide cuánta evaluación hace falta antes de lanzar, qué
[guardrails](Produccion/guardrails.md) entran desde el principio y si una persona revisa la salida.

Yan et al. recomiendan diseñar la experiencia con una persona en el bucle: "By allowing users to
provide feedback and corrections easily, we can improve the immediate output", y esas correcciones
vuelven como [feedback de usuario](Evaluacion/feedback-de-usuario.md). Según un resumen de la parte
III, la forma que más funciona es "a human-computer centaur": la persona y el modelo trabajando
juntos, no el modelo solo.

> [!NOTE]
> Sin fuente todavía: el marco de automatizar por etapas (primero el modelo sugiere, después actúa con
> revisión, después solo), que se usa en la práctica de producto y no apareció en ninguna fuente
> leída.

## Lo que se puede esperar del primer hito

Una demo sale rápido; un producto, no. Huyen lo dice como "It's easy to build a demo, but hard to
build a product" y da dos números del mismo post, los dos de un caso de LinkedIn: llevó "1 month to
achieve 80% of the experience they wanted, and an additional 4 months to surpass 95%", y "getting from
0 to 80% took as long as from 80% to 90%". Yan et al. llaman a pasar de la demo al producto "a
deceptively difficult endeavor".

De ahí sale cómo se arma el primer hito:

1. Definí qué es "anda" con unos pocos casos reales y un criterio por caso, antes de escribir el
   prompt (ver [evals](Evaluacion/evals.md)).
2. Empezá por lo más simple que pueda funcionar. Huyen cuenta como error "Use an agentic framework
   when direct API calls work" e "Insist on finetuning when prompting works"; es la regla de
   [empezar simple](../Arquitectura/Decisiones/empezar-simple.md).
3. Lanzá a pocos usuarios e iterá: Yan et al. proponen "launch and iterate" en lugar de pulir antes.
4. Planificá el tramo final como el más caro, no como el último 10 %.

Husain ordena la evaluación en tres niveles de costo creciente y deja el A/B testing para "more mature
products"; el primer hito usa los dos primeros. Tampoco se apunta al 100 %: "If you're passing 100% of
your evals, you're likely not challenging your system enough."

## Cuando el modelo cambia debajo del producto

Una aplicación con un modelo ajeno se mantiene aunque nadie toque el código, porque el proveedor
cambia y retira modelos. Yan et al. dan cuatro prácticas: fijar la versión ("Pinning model versions
in production can help avoid unexpected changes in model behavior"), correr en paralelo una copia
con el modelo nuevo, contar con que migrar "will take more time than simply swapping the API
endpoint", y no suponer que el mismo prompt da lo mismo: "Don't assume that plugging in the same
prompt will lead to similar or better results." Lo que permite migrar sin adivinar son
[evals](Evaluacion/evals.md) automatizados que se corren antes y después.

Según un resumen de su parte III, Yan et al. llaman al modelo "the least durable component in the
system", y ponen lo duradero en los evals, los guardrails, el
[cache](Produccion/cache-de-modelos.md) y el ciclo de datos. Por inferencia de esta base, el
presupuesto de una aplicación con modelos tiene que incluir una nueva
[elección de modelo](Evaluacion/benchmarks-y-eleccion-de-modelo.md) cada tanto, no solo la primera.

> [!NOTE]
> Sin fuente todavía: cada cuánto los proveedores retiran modelos; la fuente serían las páginas
> oficiales de deprecación de cada uno.

## Qué dicen los estudios sobre por qué fracasan

Hay dos estudios con método, los dos limitados, y ninguno mide lo que circula de ellos.

**RAND (Ryseff et al., 2024).** 65 entrevistas semiestructuradas, entre agosto y diciembre de 2023, a
científicos de datos e ingenieros con cinco años o más de experiencia (50 de la industria, 15 de la
academia). Encuentra cinco causas de fracaso: liderazgo que no comunica qué problema resolver ni con
qué métrica (la más frecuente), datos, equipos que empiezan por la tecnología nueva antes que por la
solución adecuada, poca inversión en infraestructura y tecnología inmadura: "AI is not a magic wand
that can make any challenging problem disappear." Es sobre proyectos de IA y ML en general, anterior
a la ola de aplicaciones con modelos de lenguaje, y con una muestra de no gerentes. El "más del 80 %
fracasa" que aparece en el informe lo toma de una nota de prensa de 2022, no de su muestra.

**MIT NANDA, "The GenAI Divide" (Challapally et al., 2025).** Un informe de "Preliminary Findings",
sin revisión por pares, sobre enero a junio de 2025: una revisión de más de 300 iniciativas públicas,
entrevistas con representantes de 52 organizaciones y 153 encuestados en conferencias. Cuenta como
éxito un impacto "marked and sustained productivity and/or P&L impact" medido seis meses después del
piloto, y estudia herramientas empresariales a medida. Con esa definición informa que "Just 5% of
integrated AI pilots are extracting millions in value". El propio informe dice que sus cifras son
"directionally accurate based on individual interviews rather than official company reporting" y que
seis meses pueden ser poco, "potentially understating success rates".

> [!IMPORTANT]
> **Lo que circuló.** "El 95 % de los proyectos de IA fracasa", con una muestra que la prensa dio
> como 150 entrevistas y 350 encuestados. **Lo que dice el informe.** Casi ningún piloto de
> herramientas a medida llegó a impacto marcado y sostenido en seis meses, según 52 organizaciones.
> Un análisis crítico (80,000 Hours, 2026) señala que el 95 % cuenta como falla a toda organización
> que no llegó a producción, aunque nunca haya hecho un piloto; que entre las que sí hicieron uno,
> según su propia cuenta, cerca de un cuarto tuvo éxito; que con tan pocas organizaciones la cifra
> podría errar por un factor de tres en cualquier dirección, y que los autores desarrollan los marcos
> de agentes que el informe recomienda, sin declararlo. No se encontró una respuesta de los autores.
>
> **Las causas tampoco coinciden.** RAND pone la causa principal en el liderazgo y en cómo se define
> el problema; NANDA, en una brecha de aprendizaje de las herramientas; Huyen, en productos mal
> diseñados y casos de uso mal elegidos. Lo que comparten, como lectura de esta base, es que casi
> nunca señalan al modelo. No son la misma evidencia: unas son entrevistas y otras, experiencia de
> practicantes.

## Qué leer antes de empezar

El post de errores comunes de Huyen, completo porque es corto: fijarse en los seis errores. Yan et
al., partes II (versiones fijas, persona en el bucle, riesgo) y III (comprar o construir). Para la
evidencia, el informe de RAND: leer el método antes que las conclusiones.
