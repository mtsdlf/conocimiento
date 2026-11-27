---
resumen: >-
  La destilación es entrenar un modelo chico (el alumno) para que imite a uno grande (el maestro),
  de modo que haga una tarea casi tan bien a menor costo y latencia; según la lectura habitual del
  paper original, el alumno aprende de las probabilidades del maestro, y en el uso actual con modelos
  de lenguaje, de sus textos.
estado: borrador
estabilidad: estable
fuentes:
  - https://arxiv.org/abs/1503.02531
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - https://developers.openai.com/api/docs/guides/distillation
  - https://crfm.stanford.edu/2023/03/13/alpaca.html
  - https://openai.com/policies/terms-of-use/
  - https://arxiv.org/abs/2501.12948
  - https://github.com/deepseek-ai/DeepSeek-R1
aliases: [distillation, knowledge distillation, destilación de conocimiento, maestro y alumno, teacher-student]
creado: 2026-11-27
revisado:
---

# Destilación

La destilación es entrenar un modelo chico (el alumno) para que imite a uno grande (el maestro),
de modo que haga una tarea casi tan bien a menor costo y latencia; según la lectura habitual del
paper original, el alumno aprende de las probabilidades del maestro, y en el uso actual con modelos
de lenguaje, de sus textos.

A diferencia del resto del ajuste, la destilación apunta menos a subir la calidad que a bajar el [costo y la latencia](../../Arquitectura/Caracteristicas/costo-y-latencia.md) de
servir el modelo (lectura de esta base). Es uno de los casos en que el ajuste vale la pena según
[Prompt, RAG o finetuning](../prompt-rag-o-finetuning.md). Huyen la vuelve a nombrar entre las
técnicas de optimización del cap. 9 (según el resumen del libro); el resto de lo que abarata servir
un modelo está en [Inferencia](../Produccion/inferencia.md).

## Los dos sentidos de destilar

La palabra nombra dos cosas que conviene no confundir, porque el alumno aprende cosas distintas.

| | Qué recibe el alumno | De dónde viene |
|---|---|---|
| Destilación de probabilidades | la distribución completa del maestro sobre las salidas posibles | Hinton, Vinyals y Dean (2015), según la lectura habitual; el abstract no lo dice |
| Destilación por datos | solo los textos que el maestro generó, como ejemplos de un [finetuning](finetuning.md) supervisado | el uso corriente con modelos de lenguaje |

El abstract de Hinton, Vinyals y Dean abre con "A very simple way to improve the performance of
almost any machine learning algorithm is to train many different models" y parte de un problema de
despliegue: un conjunto de modelos es caro de servir, y su conocimiento se puede comprimir en un solo
modelo. Según el abstract, lo probaron en MNIST y en un modelo acústico comercial de reconocimiento
de voz, que mejoró. El mecanismo que da nombre al paper (entrenar al alumno
con las probabilidades "suaves" del maestro, con una temperatura) no figura en el abstract, y su
texto no se leyó.

Lo que hoy se llama destilar en el ajuste de modelos de lenguaje suele ser lo segundo: generar datos
con el modelo grande y ajustar al chico con ellos. Huyen la ubica así: en su índice, "Model
Distillation" es una subsección de "Data Augmentation and Synthesis", del capítulo de datos (según
el índice del libro). Por eso la destilación por datos es también un caso de
[datos sintéticos](datos-sinteticos.md), y hereda sus riesgos.

> [!NOTE]
> Sin fuente todavía: el texto de Hinton et al. sobre probabilidades suaves y temperatura, que es lo
> que separa los dos sentidos.

## Cómo se destila un modelo para una tarea

El flujo que documenta un gran proveedor tiene los primeros cuatro pasos; el quinto lo agrega esta
base:

1. Ajustá el prompt en un modelo grande hasta que pase tus [evals](../Evaluacion/evals.md).
2. Corré ese modelo sobre entradas reales o representativas y guardá sus respuestas.
3. Filtrá las respuestas que pasan los evals; las que no, se descartan.
4. Ajustá un modelo chico con los pares de entrada y respuesta filtrados.
5. Medí el modelo chico con los mismos evals, contra el grande (agregado de esta base).

El paso 3 es el que hace la diferencia: sin filtrar, el alumno aprende también los errores del
maestro (lectura de esta base). La plataforma de ese proveedor está en retirada; el estado de los
servicios de ajuste está en la ficha [Plataformas de IA](../Produccion/plataformas-de-ia.md).

## Dos casos con cifras

**Alpaca** (Stanford, 13 de marzo de 2023): un LLaMA de 7.000 millones de parámetros ajustado con
52.000 demostraciones generadas por un modelo de OpenAI a partir de 175 pares escritos a mano.
Según la página del proyecto, generar los datos costó menos de 500 dólares y el ajuste, unas 3 horas
en 8 GPU (menos de 100 dólares). El mismo caso muestra el límite: "Alpaca is intended only for
academic research" y "any commercial use is prohibited", por la licencia del modelo de partida, por los
términos del proveedor del maestro y por falta de medidas de seguridad.

**DeepSeek-R1** (enero de 2025; publicado en *Nature* 645): según su abstract, los patrones de
razonamiento de un modelo grande se pueden transferir a modelos chicos. El repositorio publica seis
modelos destilados sobre modelos de partida de otras familias, "finetuned with 800k samples curated with
DeepSeek-R1": es destilación por datos, no por probabilidades. Cada modelo destilado conserva la
licencia de su modelo de partida, aunque el código y los pesos propios sean MIT. Los
[modelos de razonamiento](../Modelos/razonamiento.md) explican qué es lo que se transfiere.

## Lo que limita usar las salidas de otro modelo

Destilar con salidas de un modelo cerrado choca con los términos de uso del proveedor. Los de
OpenAI prohíben, literalmente: "Use Output to develop models that compete with OpenAI." Destilar
sobre un modelo abierto choca con la licencia del modelo de partida, que el alumno hereda, como muestran Alpaca
y DeepSeek-R1. Antes de destilar hay que leer los términos vigentes del maestro y la licencia de la
base; esta base no da consejo legal.

> [!NOTE]
> Sin fuente todavía: las cláusulas equivalentes de otros proveedores de modelos cerrados y de las
> licencias de modelos abiertos.

## Qué leer sobre destilación

El paper de [Hinton, Vinyals y Dean](https://arxiv.org/abs/1503.02531), en las secciones sobre
probabilidades suaves y temperatura, para el sentido original; la
[página de Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html), como caso con costo y
restricción de licencia. Fijarse en dos cosas: qué se le enseña al alumno (probabilidades o solo
textos) y de quién son los términos que limitan el uso de las salidas.
