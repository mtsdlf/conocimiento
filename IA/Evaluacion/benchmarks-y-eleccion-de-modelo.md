---
resumen: >-
  Un benchmark es un conjunto público de tareas con respuesta conocida en el que se comparan modelos;
  sirve para descartar los que no alcanzan, pero el modelo de una aplicación se elige con una
  evaluación propia, que también decide si conviene una API o un modelo alojado.
estado: vigente
estabilidad: semi
fuentes:
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - https://arxiv.org/abs/2009.03300
  - https://arxiv.org/abs/2406.04127
  - https://arxiv.org/abs/2311.12022
  - https://arxiv.org/abs/2310.06770
  - https://openai.com/index/introducing-swe-bench-verified/
  - https://arxiv.org/abs/2501.14249
  - https://arxiv.org/abs/2406.04244
  - https://arxiv.org/abs/2405.00332
  - https://arxiv.org/abs/2511.04703
  - https://arxiv.org/abs/2403.04132
  - https://arena.ai/leaderboard/methodology
  - https://arxiv.org/abs/2504.20879
  - https://arxiv.org/abs/2211.09110
  - https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-iii-strategy/
aliases: [benchmark, benchmarks, leaderboard, ranking de modelos, model selection, elegir un modelo, build vs buy, construir o comprar]
creado: 2026-11-27
revisado: 2026-11-27
---

# Benchmarks y elección de modelo

Un benchmark es un conjunto público de tareas con respuesta conocida en el que se comparan modelos;
sirve para descartar los que no alcanzan, pero el modelo de una aplicación se elige con una
evaluación propia, que también decide si conviene una API o un modelo alojado.

Es la primera decisión de la [evaluación](evaluacion.md): antes de escribir un prompt hay que elegir
qué [modelo base](../Modelos/modelo-base.md) recibe ese prompt. Según el índice y el resumen de capítulos
del libro (no se leyó el texto), Huyen la trata en el capítulo 4 ("Model Selection": el flujo,
construir o comprar, los benchmarks públicos), y la comparación por pares en el capítulo 3. Los rankings de hoy, con sus cifras y sus nombres de modelos,
están en la ficha [benchmarks vigentes](benchmarks-vigentes.md); qué familias de modelos hay, en
[modelos disponibles](../Modelos/modelos-disponibles.md).

## Qué mide un benchmark y cuánto dura

Cada benchmark fija una tarea y una forma de puntuarla, y nace para separar modelos que todavía no la
resuelven. Tres ejemplos muestran el ciclo:

| Benchmark | Qué es | Al nacer | Después |
|---|---|---|---|
| MMLU (Hendrycks et al., 2020) | 57 materias de opción múltiple, de matemática elemental a derecho | Los modelos estaban cerca del azar | Según el abstract de Humanity's Last Exam, los modelos sacan "over 90%" |
| GPQA (Rein et al., 2023) | 448 preguntas de biología, física y química difíciles de buscar | Expertos 65 %, no expertos con más de 30 minutos de web 34 %, el mejor modelo 39 % | Sigue en uso su subconjunto Diamond; puntajes actuales en la [ficha](benchmarks-vigentes.md) |
| SWE-bench (Jimenez et al., 2023; ICLR 2024) | 2.294 issues reales de 12 repositorios Python | El mejor modelo resolvía "a mere 1.96%" | Se publicó una versión revisada, que después también se dejó de reportar (ver [benchmarks de agentes](../Agentes/benchmarks-de-agentes.md)) |

Cuando un benchmark se satura deja de separar, y aparece otro más difícil: Humanity's Last Exam
(Phan et al., 2025) son 2.500 preguntas de expertos que "cannot be quickly answered via internet
retrieval", hechas porque MMLU ya no distinguía. Por eso un puntaje sin fecha y sin versión del
benchmark dice poco, y las cifras vivas van en una ficha.

## Por qué el puntaje no es la tarea

Un benchmark puede fallar como medida de cuatro formas, todas documentadas:

- Errores en las respuestas. Gema et al. (preprint, leído en su abstract) estiman que "6.49% of
  MMLU questions contain errors" y re-anotaron 5.700 preguntas a mano.
- Tareas mal planteadas. Para armar SWE-bench Verified, 93 desarrolladores revisaron 1.699 ítems y
  se descartó 68,3 %: enunciados subespecificados o pruebas que rechazaban soluciones válidas. Lo
  publicó el mismo proveedor que reporta puntajes en ese benchmark, y dice que el filtro es
  probablemente demasiado estricto. Esa versión revisada después también se dejó de reportar (ver
  [benchmarks de agentes](../Agentes/benchmarks-de-agentes.md)).
- Contaminación. Los modelos pueden "inadvertently incorporate evaluation benchmark information
  from their training data" (Xu et al., survey). En GSM1k, un conjunto nuevo del mismo estilo que uno
  conocido de matemática escolar, la precisión cayó "up to 8%", con "evidence of systematic
  overfitting across almost all model sizes", aunque muchos modelos de frontera mostraron poca señal
  (Zhang et al., preprint, leído en su abstract).
- Validez de constructo. Bean et al. (NeurIPS 2025) pusieron a 29 revisores a analizar 445
  benchmarks de congresos y encontraron patrones que "weaken the validity of the resulting claims":
  un benchmark que se llama "razonamiento" o "seguridad" mide algo más angosto. Leído en su abstract.

La lectura de esta base es la de la investigación contraria del tema: los benchmarks miden algo, pero
menos de lo que dicen sus nombres. Ninguna de estas críticas alcanza a una evaluación propia sobre
casos del producto, que tiene sus propios riesgos (ver [evals](evals.md)).

## Rankings por pares y la disputa sobre Arena

La otra forma de comparar es pedir a personas que elijan la mejor de dos respuestas. Chatbot Arena (Chiang et al., 2024) juntó así más de 240.000 votos y reporta que "are in
good agreement with those of expert raters". Según su página de metodología, el puntaje sale de un
modelo de Bradley-Terry, "a paired-comparison model similar to Elo", con un ancla arbitraria, y un
control de estilo que "adds response length and formatting to the statistical model". Que ese
control apunte al mismo sesgo de verbosidad que tiene un [juez](ia-como-juez.md) es lectura de esta
base.

> [!IMPORTANT]
> **Que el ranking es justo.** Chiang et al. muestran acuerdo con expertos. **Que está sesgado por
> acceso.** Singh et al., "The Leaderboard Illusion" (preprint de 2025, leído en su abstract y un
> resumen), sostienen que las pruebas privadas no divulgadas "benefit a handful of providers": un
> proveedor probó 27 variantes privadas antes de lanzar un modelo, los modelos cerrados se muestrean
> más y se retiran menos, dos proveedores recibirían cerca de 19,2 % y 20,4 % de los datos frente a
> 29,7 % de 83 modelos abiertos juntos, y con datos de Arena un modelo gana hasta 112 % relativo en esa
> misma distribución. No se encontró una respuesta del operador; su página de metodología no describe
> una política de pruebas privadas. Lectura de esta base: un ranking de preferencias mide qué gusta en
> esa plataforma, y vale como señal para acotar, no para decidir.

Otros agregadores corren baterías de benchmarks y publican un índice: HELM (Liang et al., 2022) con 42
escenarios y 7 métricas, y agregadores vivos de institutos y empresas, listados con fecha en
[benchmarks vigentes](benchmarks-vigentes.md).

## Cómo se elige un modelo para una aplicación

Según el resumen de capítulos del libro, Huyen evalúa capacidades del dominio y de generación
(fluidez, coherencia, fidelidad, consistencia factual y seguridad), y compara la elección con
"creating a private leaderboard to rank models based on your needs". El índice del capítulo suma
secciones sobre seguir instrucciones y sobre
[costo y latencia](../../Arquitectura/Caracteristicas/costo-y-latencia.md) como criterios. Los
pasos que siguen los arma esta base a partir de eso; el flujo exacto del capítulo 4 no se leyó.

1. Descartá por restricciones duras: dónde pueden ir los datos, si hace falta un modelo abierto, el
   presupuesto por consulta, la [ventana de contexto](../Modelos/transformer.md) y la latencia
   máxima.
2. Acotá con benchmarks públicos a unos pocos candidatos, mirando los que se parecen a la tarea y su
   fecha.
3. Corré los mismos [evals](evals.md) del producto sobre cada candidato y compará calidad, costo y
   latencia juntos.
4. Dejá la elección y sus números en un [ADR](../../Arquitectura/Decisiones/adr.md), y repetí el paso 3
   cuando salga un modelo nuevo o cambie el que se usa.

El paso 4 importa porque el modelo es lo que más rápido cambia en el sistema: según un resumen de su
texto, Yan et al. lo describen como el componente menos durable, y un [router](../Produccion/router-y-gateway-de-modelos.md) permite
cambiarlo sin tocar la aplicación. Cómo se planifica ese mantenimiento está en
[planificar una aplicación](../planificar-una-aplicacion.md).

## Comprar una API o alojar un modelo

"Construir o comprar" tiene dos sentidos en el oficio. En el de Huyen, es usar un modelo por la API
de un proveedor o alojar un modelo abierto propio; según el resumen de su capítulo 4, lo compara en
siete ejes, entre ellos privacidad y linaje de los datos, rendimiento, funcionalidad, control y costo
(el resumen no enumera los siete). En el de Yan et al., es comprar una funcionalidad hecha o
desarrollarla:

- Empezar con APIs de inferencia y ajustar solo si el prompt claramente no alcanza (ver
  [prompt, RAG o finetuning](../prompt-rag-o-finetuning.md)).
- "No GPUs before PMF": no invertir en infraestructura propia antes de saber que el producto encaja
  en su mercado.
- Alojar puede tener sentido por privacidad, control o escala.
- "Don't build LLM features you can buy."

Yan et al. agregan, en 2024, que el costo de una capacidad fija tiene un "halving time of just six
months". Como lectura de esta base, lo que hoy justifica alojar un modelo puede dejar de
justificarlo pronto.

> [!NOTE]
> Sin fuente todavía: una comparación cuantitativa del costo de una API contra un modelo alojado, y el
> texto de los siete ejes de Huyen.

## Qué leer para elegir

Huyen, *AI Engineering*, capítulo 4, sección "Model Selection": fijarse en el leaderboard privado
(leído solo por índice y resúmenes). Para el estado vivo, el Benchmarking Hub de Epoch AI, que corre
sus propias evaluaciones y publica la fecha (enlazado en la ficha). Como contrapeso,
["The Leaderboard Illusion"](https://arxiv.org/abs/2504.20879), secciones sobre pruebas privadas y
asimetría de datos, y ["Measuring what Matters"](https://arxiv.org/abs/2511.04703), con sus ocho
recomendaciones para leer un benchmark.
