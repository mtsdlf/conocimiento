---
resumen: >-
  Un modelo de razonamiento genera pasos intermedios antes de responder y gasta más cómputo en la
  inferencia para acertar en tareas de varios pasos; esa conducta se entrena con aprendizaje por
  refuerzo sobre tareas verificables y se regula con cuántos tokens se lo deja pensar.
estado: borrador
estabilidad: semi
fuentes:
  - https://magazine.sebastianraschka.com/p/understanding-reasoning-llms
  - https://arxiv.org/abs/2201.11903
  - https://arxiv.org/abs/2408.03314
  - https://openai.com/index/learning-to-reason-with-llms/
  - https://arxiv.org/abs/2501.12948
  - https://arxiv.org/abs/2402.03300
  - https://arxiv.org/abs/2411.15124
  - https://platform.claude.com/docs/en/build-with-claude/extended-thinking
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://arxiv.org/abs/2506.06941
  - https://arxiv.org/abs/2506.09250
  - https://arxiv.org/abs/2507.01231
aliases: [reasoning, modelos de razonamiento, reasoning models, LRM, test-time compute, cómputo en inferencia, cadena de pensamiento, chain of thought, CoT, thinking, pensamiento extendido, RLVR, GRPO]
creado: 2026-11-27
revisado:
---

# Razonamiento

Un modelo de razonamiento genera pasos intermedios antes de responder y gasta más cómputo en la
inferencia para acertar en tareas de varios pasos; esa conducta se entrena con aprendizaje por
refuerzo sobre tareas verificables y se regula con cuántos tokens se lo deja pensar.

Sebastian Raschka define razonar, en este sentido, como "the process of answering questions that
require complex, multi-step generation with intermediate steps". Es lo que más cambió después de
2024 y lo que más se discute: si los modelos "razonan" o buscan con fuerza bruta entre patrones está
abierto (ver [más abajo](#si-los-modelos-razonan-o-colapsan)).

## Dos ejes: entrenar para pensar y dejar pensar más

El razonamiento cruza dos etapas de la vertical, y cada técnica se entiende mejor ubicándola en una:

- **En el entrenamiento**, es [post-entrenamiento](post-entrenamiento.md) con aprendizaje por
  refuerzo: se premia al modelo cuando llega a una respuesta comprobable, y aprende por su cuenta a
  escribir pasos, verificar y corregirse.
- **En la inferencia**, es gastar más tokens por pregunta: escribir un razonamiento largo antes de
  contestar, o generar varias respuestas y elegir. Es el *test-time compute* o cómputo en inferencia.

Raschka distingue cuatro vías para construir o mejorar un modelo de razonamiento, que combinan los
dos ejes:

| Vía | Qué hace |
|---|---|
| Escalar la inferencia | Más tokens de pensamiento o más muestras por pregunta, sin cambiar los pesos |
| Aprendizaje por refuerzo puro | Recompensa por respuesta correcta, sin ejemplos de razonamiento escritos por personas |
| Ajuste supervisado más refuerzo | Ejemplos de razonamiento primero y refuerzo después (la receta de DeepSeek-R1) |
| Ajuste supervisado puro con destilación | Un modelo chico aprende de los razonamientos de uno grande ([Destilación](../Ajuste/destilacion.md)) |

Huyen, según el índice de su libro, pone el cómputo en inferencia como una subsección del
[muestreo](muestreo.md), y OpenAI lo liga al refuerzo. No se contradicen: cortan el mismo tema por
lugares distintos.

## De pedir los pasos a entrenarlos

**Pedirlos en el prompt.** Wei y otros (2022) mostraron que dar unos pocos ejemplos con los pasos
intermedios escritos (*chain-of-thought prompting*) mejora el razonamiento: un modelo de 540 mil
millones de parámetros con ocho ejemplos alcanzó el mejor resultado de la época en GSM8K, problemas
de matemática escolar, por encima de un GPT-3 ajustado con verificador. Funcionaba solo en modelos
suficientemente grandes. Es una técnica de [prompt](../Contexto/prompt.md).

**Gastar el cómputo con criterio.** Snell y otros (2024, preprint) encontraron que repartir el
cómputo de inferencia según la dificultad de cada pregunta es "over 4x more efficient than a best-of-N
baseline" (según su abstract), y que, a igual cómputo total, un modelo más chico con más cómputo en
inferencia superó a uno 14 veces mayor en problemas donde el chico ya acertaba a veces. El resultado
depende de la dificultad: no reemplaza a un modelo mejor en lo que el chico no sabe hacer.

**Entrenarlos con refuerzo.** OpenAI presentó o1 en septiembre de 2024 diciendo que un algoritmo de
refuerzo a gran escala "teaches the model how to think productively using its chain of thought", y
que los resultados mejoran tanto con más entrenamiento como con más tiempo de pensamiento. DeepSeek-R1
(enero de 2025, publicado después en *Nature*) fue el primer caso abierto y documentado: su variante
R1-Zero mostró que el razonamiento puede incentivarse con refuerzo puro, sin ejemplos humanos, y que
aparecen conductas como la autorreflexión, la verificación y el cambio de estrategia. Usa GRPO, una
variante de PPO que gasta menos memoria, con la que DeepSeekMath 7B había llegado a 51,7 % en el
benchmark MATH sin herramientas.

## Solo se entrena lo que se puede verificar

La recompensa de estos métodos sale de comprobar la respuesta: si la cuenta dio, si el código pasó
las pruebas. Tulu 3 llama a eso "Reinforcement Learning with Verifiable Rewards" (RLVR), y DeepSeek-R1
reporta su mejor rendimiento en tareas verificables (matemática, programación, ciencias). Lectura de
esta base: donde no hay una respuesta comprobable (un resumen, un mail, una recomendación) la mejora
no está garantizada, y un modelo de razonamiento puede costar más sin rendir más. Qué modelo conviene
para cada tarea se decide midiendo ([Benchmarks y elección de modelo](../Evaluacion/benchmarks-y-eleccion-de-modelo.md)).

## Lo que cuesta pensar

Los tokens de pensamiento se pagan y se esperan. En la documentación de Anthropic se facturan como
tokens de salida, y cada uno se genera antes de la respuesta
([Costo y latencia](../../Arquitectura/Caracteristicas/costo-y-latencia.md),
[Inferencia](../Produccion/inferencia.md)). Los proveedores dejan regular cuánto piensa el modelo, y
en al menos uno la forma de hacerlo pasó de un presupuesto fijo de tokens a un nivel de esfuerzo; el
estado actual está en la ficha de [Modelos disponibles](modelos-disponibles.md). Lectura de esta base:
un [router](../Produccion/router-y-gateway-de-modelos.md) puede mandar las preguntas fáciles a un
modelo, o a un nivel de esfuerzo, que piense menos.

Lo que se ve del pensamiento no es necesariamente lo que el modelo calculó: la documentación de
Anthropic habla de bloques de pensamiento resumidos.

> [!NOTE]
> Sin fuente todavía: si la cadena de pensamiento que el modelo escribe es fiel a cómo llegó a la
> respuesta.

## Si los modelos razonan o colapsan

> [!IMPORTANT]
> **Colapso.** Shojaee y otros (Apple, "The Illusion of Thinking", NeurIPS 2025) probaron modelos
> de razonamiento con puzzles de complejidad controlable (Torre de Hanoi, cruzar el río) y
> encontraron un "complete accuracy collapse beyond certain complexities". Distinguen tres regímenes:
> en baja complejidad los modelos comunes superan a los de razonamiento, en media ganan los de
> razonamiento y en alta colapsan los dos. Además, al subir la complejidad los modelos razonan menos
> aunque les quede presupuesto de tokens (según su abstract).
>
> **Defecto del experimento.** Lawsen (junio de 2025) respondió que los resultados "mostly reflect
> flawed experiments": en Hanoi las salidas superaban el límite de tokens y los modelos lo decían; el
> corrector no distinguía un error de razonamiento de un límite práctico, y las instancias de cruzar
> el río con más de 5 parejas eran imposibles por la capacidad del bote, pero se contaron como fallas.
> Pidiendo una función que genere la solución en vez de la lista de movimientos, la precisión en Hanoi
> fue alta. Sus experimentos son preliminares.
>
> **Parte y parte.** Dellibarda Varela y otros (julio de 2025) confirman algo de cada lado: en Hanoi
> los modelos "stumble when complexity rises moderately (around 8 disks)", así que no todo era límite
> de salida; en cruzar el río, con solo casos resolubles, resuelven "instances with over 100 agent
> pairs". Los describen como "stochastic, RL-tuned searchers in a discrete state space we barely
> understand".
>
> **Estado.** Parte del colapso fue un defecto de diseño (puzzles irresolubles y límites de salida),
> según dos réplicas independientes; parte persiste, como el límite cerca de 8 discos. "Razonan" y "no
> razonan" son demasiado fuertes para lo que muestran estas pruebas. No se encontró una segunda ronda
> posterior a 2025, y los tres trabajos se leyeron por su abstract.

## Qué leer sobre razonamiento

[DeepSeek-R1](https://arxiv.org/abs/2501.12948), la parte de R1-Zero y las secciones sobre la
recompensa y las conductas que aparecen: es el caso abierto mejor documentado. El artículo de
[Raschka](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms), para el mapa de las
cuatro vías. Para la discusión, [Shojaee y otros](https://arxiv.org/abs/2506.06941),
[Lawsen](https://arxiv.org/abs/2506.09250) y [Dellibarda Varela y otros](https://arxiv.org/abs/2507.01231)
juntos: fijarse en qué instancias eran irresolubles y qué sigue fallando cerca de los 8 discos.
