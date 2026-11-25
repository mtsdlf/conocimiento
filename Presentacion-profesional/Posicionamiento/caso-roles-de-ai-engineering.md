---
resumen: >-
  Caso que aplica el posicionamiento a un campo: los roles de AI engineering que piden los avisos,
  puestos contra las tres capas del stack que describe Chip Huyen en *AI Engineering*. El libro
  describe capas y tareas, no puestos: la correspondencia con los roles del mercado es inferencia
  de esta base.
estado: borrador
estabilidad: semi
fuentes:
  - "Presentacion-profesional/.investigacion/posicionamiento.md (sección 3)"
  - "Chip Huyen, AI Engineering, O'Reilly, enero 2025, índice: https://github.com/chiphuyen/aie-book/blob/main/ToC.md"
  - "Extracto del cap. 1, The AI Engineering Stack, The Pragmatic Engineer, 2025-05-20: https://newsletter.pragmaticengineer.com/p/the-ai-engineering-stack"
  - "LinkedIn, Jobs on the Rise 2026 (2026-01-07), vía Dice 2026-01-14: https://www.dice.com/career-advice/ai-related-jobs-top-linkedins-fastest-growing-roles-list-for-2026"
  - "Indeed Hiring Lab, 2026-01-22 (vía buscador): https://www.hiringlab.org/2026/01/22/january-labor-market-update-jobs-mentioning-ai-are-growing-amid-broader-hiring-weakness"
  - "Fortune, 2026-09-03, cifras de Lightcast (vía buscador): https://fortune.com/2026/09/03/forward-deployed-engineers-fast-growing-six-figure-silicon-valley-job-integrate-ai-with-customers-tech-careers-palantir/"
  - "Gergely Orosz, The Pulse: Forward deployed engineering heats up again, 2026-05-24: https://blog.pragmaticengineer.com/the-pulse-forward-deployed-engineering-heats-up-again/"
  - "Avisos de tres empresas de IA leídos el 2026-11-24: https://job-boards.greenhouse.io/scaleai/jobs/4720573005, https://databricks.com/company/careers/open-positions/job?gh_jid=8546367002, https://databricks.com/company/careers/open-positions/job?gh_jid=8367021002, https://job-boards.greenhouse.io/anthropic/jobs/5245851008, https://job-boards.greenhouse.io/anthropic/jobs/5198255008, https://databricks.com/company/careers/open-positions/job?gh_jid=8401114002"
aliases: [AI engineering, AI engineer, ingeniería de IA, roles de IA, Chip Huyen, forward-deployed engineer, FDE]
creado: 2026-11-24
revisado:
---

# Caso: roles de AI engineering

Caso que aplica el posicionamiento a un campo: los roles de AI engineering que piden los avisos,
puestos contra las tres capas del stack que describe Chip Huyen en *AI Engineering*. El libro
describe capas y tareas, no puestos: la correspondencia con los roles del mercado es inferencia
de esta base.

Sirve como ejemplo trabajado de [leer una búsqueda](leer-una-busqueda.md) y de armar una
[historia profesional](historia-profesional.md) para un cambio de área. Es un caso genérico, no el
perfil de nadie.

## El libro describe un stack, no puestos

*AI Engineering* (O'Reilly, enero de 2025) tiene diez capítulos: 1. Introduction to Building AI
Applications with Foundation Models; 2. Understanding Foundation Models; 3. Evaluation Methodology;
4. Evaluate AI Systems; 5. Prompt Engineering; 6. RAG and Agents; 7. Finetuning; 8. Dataset
Engineering; 9. Inference Optimization; 10. AI Engineering Architecture and User Feedback.

El capítulo 1 describe un stack de tres capas:

- **Desarrollo de aplicaciones**: «Application development involves providing a model with good
  prompts and necessary context», con evaluación rigurosa e interfaces.
- **Desarrollo de modelos**: «This layer provides tooling for developing models»: modelado,
  entrenamiento, ingeniería de datasets y optimización de inferencia.
- **Infraestructura**: «includes tooling for model serving, managing data and compute, and monitoring».

Según Huyen, al construir una aplicación se empieza probablemente por la capa de arriba y se baja
solo si hace falta. El libro no habla de títulos de puesto. Repartir los capítulos por capa es
lectura de esta base sobre el índice: aplicación, 3, 4, 5, 6 y 10; modelo, 2, 7 y 8;
infraestructura, 9 y partes del 10 (gateway, caches, monitoreo).

## En qué se separa de ML engineering

Para Huyen, AI engineering «evolved out of ML engineering» y las dos se superponen mucho. Las separa
en tres puntos. Hay menos desarrollo de modelos y más adaptación y evaluación de modelos ya hechos.
Los modelos de base son más grandes y caros, así que pesa más la eficiencia de entrenamiento y de
inferencia. Y las salidas abiertas hacen que la evaluación sea «a much bigger problem in AI
engineering». Según la autora, saber ML ya no es «a must-have for building AI applications», aunque
sigue sirviendo. El mismo capítulo compara AI engineering con full-stack engineering.

## Qué piden los avisos, rol por rol

Los nombres de rol de la tabla son etiquetas de esta base, y la columna de capítulos es inferencia.
La evidencia pedida sale de seis avisos de tres empresas de IA de EE.UU. leídos el 2026-11-24. La
última columna es síntesis propia: un ejemplo de proyecto que mostraría esa evidencia.

Algunos términos de los avisos: **RAG** es darle al modelo documentos recuperados de una base propia
antes de que responda; **serving** es servir el modelo como un servicio que responde pedidos;
**fine-tuning** es seguir entrenando un modelo con datos propios; un **golden dataset** es un set de
casos con la respuesta correcta conocida, contra el que se evalúa; **LLM-as-a-judge** es usar un
modelo para calificar las respuestas de otro; **Text2SQL** es traducir una pregunta en lenguaje
natural a una consulta SQL. Qué es un LLM y por qué su salida hay que verificarla está en
[LLM](../../IA/llm.md) y [guardrails](../../IA/guardrails.md).

| Rol del mercado | Capa y capítulos | Qué evidencia piden los avisos | Qué proyecto la mostraría |
|---|---|---|---|
| AI engineer / applied AI | Aplicación; 3-6, 10 | «Experience building production AI systems using LLMs»; «designing or evaluating AI systems using quantitative metrics»; golden datasets, regression suites, LLM-as-a-judge; 4+ años en un aviso | Un sistema con RAG o agentes usado por gente real, con un set de evaluación y sus resultados |
| Forward-deployed engineer de IA | Aplicación con algo de infraestructura; 3-6, 10 | Aplicaciones de IA generativa con RAG, multiagentes, Text2SQL o fine-tuning; despliegue en producción «including evaluation and optimizations»; comunicar a públicos técnicos y no técnicos; no es para nivel inicial | Una aplicación desplegada para un usuario concreto, con su evaluación y un documento que la explique a alguien no técnico |
| Inferencia / serving / plataforma de IA | Infraestructura; 9, partes de 10 | En un aviso, solo sistemas distribuidos como mínimo y «Desire to learn more about machine learning systems»; en otro, «10+ years» y «Deep expertise in model serving» (routing, scheduling, autoscaling, observabilidad) | Un servicio de inferencia de un modelo abierto con autoscaling, métricas de latencia y costo, y una mejora medida (batching, cache) |
| Evals | Aplicación y modelo; 3, 4 | «Have designed, run, and analyzed evaluations for ML models at scale»; estadística y diseño experimental; es un rol de investigación | Un benchmark propio sobre una tarea concreta, con diseño experimental y análisis publicado |
| ML engineer aplicado | Modelo; 2, 7, 8 | «2-8 years of machine learning engineering experience»; modelos de lenguaje; desarrollo de punta a punta, del prototipo al monitoreo | Un fine-tuning con su dataset, su evaluación contra la línea de base y su despliegue |

Lo que se repite en los avisos es producción, no demos: sistemas en uso, evaluación explícita y, en
infraestructura, sistemas distribuidos a escala. La palabra «portfolio» o «proyectos personales» no
aparece como requisito en ninguno. Un proyecto propio, entonces, vale si se parece a lo que se hace
en producción; cómo mostrarlo está en [portfolio y GitHub](../Vidrieras/portfolio-y-github.md).

## La demanda, con fecha

Las cifras de demanda cambian rápido y vienen de plataformas o de prensa:

- LinkedIn, en *Jobs on the Rise 2026* (2026-01-07, leído vía Dice), pone a AI engineer como el rol
  de crecimiento más rápido de EE.UU. por segundo año. Junta a «AI engineers» con «ML engineers» en
  una sola categoría, así que no distingue lo que Huyen distingue.
- Según Indeed Hiring Lab, vía buscador, los avisos de EE.UU. que mencionan IA llegaron a un pico de
  4,2 % en diciembre de 2025, y casi 90 % de los avisos de IA vienen de cerca de 1 % de las empresas.
- Según Fortune (2026-09-03), con cifras de Lightcast y vía buscador, los avisos «forward-deployed»
  subieron más de 1000 % entre enero y agosto de 2026 contra el año anterior. Orosz describe ese rol
  como mezcla de platform engineering, software y solutions engineering, cada vez más parecido a un
  arquitecto de soluciones o un consultor.

## Qué rol queda más cerca según de dónde se viene

> [!NOTE]
> Esta sección es síntesis de esta base, a partir del mapeo del libro y de los seis avisos. Ninguna
> fuente la afirma.

- **Desde infraestructura o plataforma**: lo más cercano es inferencia, serving o plataforma de IA,
  la capa de infraestructura de Huyen y su capítulo 9. Uno de los avisos pide como mínimo sistemas
  distribuidos y ganas de aprender ML; lo específico de modelos de lenguaje está en preferidos. Los
  avisos de plataforma leídos son más senior que los de aplicación. Segunda opción: forward-deployed
  con perfil de plataforma. La historia muestra Kubernetes y nube, observabilidad, autoscaling, costo
  y latencia, y un proyecto de serving con números.
- **Desde backend**: lo más cercano es AI engineer o applied AI, la capa de aplicación. Huyen compara
  AI engineering con full-stack y dice que ML ya no es obligatorio. La historia muestra un sistema con
  RAG o agentes en producción con evaluación, no una demo.
- **Desde datos**: lo más cercano es ML engineer aplicado, y evals para quien trae estadística y
  diseño experimental. El capítulo 8, ingeniería de datasets, es terreno conocido. Las evals de
  modelos como rol de investigación quedan un escalón arriba en seniority.

En los tres casos el cambio se cuenta como dice [historia profesional](historia-profesional.md): lo
que ya se hacía del rol nuevo, más un experimento que cubre lo que falta. Cómo tratar el cambio de
área en el CV está en [huecos y cambios de carrera](../Material/huecos-y-cambios-de-carrera.md).

## Cómo repetir el caso

1. **Leé el capítulo 1 del libro**, la sección «The AI Engineering Stack», para el mapa; y los
   capítulos 3 y 4, sobre evaluación, que es lo que más piden los avisos.
2. **Juntá tres a cinco avisos vigentes por rol** y armá tu propia tabla: ningún informe de mercado
   reemplaza esa lectura.
3. **Marcá en cada uno mínimos y preferidos**, como en [leer una búsqueda](leer-una-busqueda.md).
4. **Elegí el rol donde tu inventario cubre más mínimos** y planeá el proyecto que cubre el resto.

## Límites del caso

La muestra es de seis avisos de tres empresas de IA de EE.UU., leídos en una sola fecha. No hay
datos del mercado argentino ni regional. No apareció ningún aviso con el título «LLMOps» o «LLM
platform»: el rol de plataforma figura como serving o inferencia. Los requisitos de forward-deployed
salen de un solo aviso, y sus cifras de crecimiento solo de prensa.
