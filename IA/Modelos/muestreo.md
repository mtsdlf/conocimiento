---
resumen: >-
  El muestreo es la regla con que se elige el próximo token a partir de la distribución de
  probabilidad que calcula el modelo; decide cuánto varía la salida entre corridas, y en su forma
  restringida (salidas estructuradas) obliga a que la salida respete un esquema.
estado: borrador
estabilidad: estable
fuentes:
  - https://arxiv.org/abs/1904.09751
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - https://arxiv.org/abs/2307.09702
  - https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - https://developers.openai.com/api/docs/guides/structured-outputs
aliases: [sampling, decoding, decodificación, temperatura, temperature, top-p, nucleus sampling, top-k, greedy, salidas estructuradas, structured outputs, constrained decoding, decodificación restringida, modo JSON, JSON mode]
creado: 2026-11-27
revisado:
---

# Muestreo

El muestreo es la regla con que se elige el próximo token a partir de la distribución de
probabilidad que calcula el modelo; decide cuánto varía la salida entre corridas, y en su forma
restringida (salidas estructuradas) obliga a que la salida respete un esquema.

El [transformer](transformer.md) no devuelve una palabra: devuelve una probabilidad para cada
[token](token-y-embedding.md) del vocabulario. Algo tiene que elegir uno, agregarlo al texto y pedir
la distribución siguiente, y esa elección se repite por cada token de la respuesta. Huyen, en el
resumen del capítulo 2, saca de ahí la consecuencia que ordena el oficio: el muestreo hace que los
modelos sean probabilísticos, lo que permite salidas creativas pero también inconsistencia y
[alucinación](alucinacion.md), y hay que diseñar el sistema alrededor de ese comportamiento,
empezando por una buena [evaluación](../Evaluacion/evaluacion.md).

## Elegir siempre lo más probable sale mal

La regla más simple, llamada *greedy*, toma siempre el token más probable. Holtzman y otros (ICLR
2020) mostraron que el texto que sale así es "dull and repetitive", y que la estrategia de
decodificación sola cambia mucho la calidad del texto con el mismo modelo (según su abstract). Elegir
al azar según las probabilidades tiene el problema opuesto: la cola de tokens poco probables, sumada,
pesa, y de vez en cuando sale uno que descarrila la respuesta.

Su propuesta, el muestreo *top-p* o de núcleo, muestrea solo del "smallest set of top-probability
words" cuya probabilidad acumulada supera un umbral p. Así recorta la cola poco confiable y conserva
la variedad. Las APIs exponen además la **temperatura**, que afila la distribución (valores bajos,
salidas más repetibles) o la aplana (valores altos, salidas más variadas), y a veces *top-k*, que se
queda con los k tokens más probables.

> [!NOTE]
> Sin fuente todavía: una definición primaria de logits, temperatura y *top-k*; los rangos y valores
> por defecto de esos parámetros en las APIs actuales, y por qué una temperatura de 0 no garantiza la
> misma salida en cada corrida.

## Qué hace con esto quien construye

Que la salida varíe no es un defecto que se apaga con un parámetro: es cómo funciona el modelo. En la
práctica eso lleva a tres decisiones, que son de esta base a partir de las fuentes citadas:

- **Medir proporciones, no casos.** "Anda" pasa a ser un porcentaje sobre un conjunto de
  [evals](../Evaluacion/evals.md), corriendo cada caso más de una vez si la variación importa.
- **Encerrar lo variable.** El resto del sistema no debería depender de que dos llamadas den lo mismo
  ([Aislar lo no determinista](../../Arquitectura/Modularidad/aislar-lo-no-determinista.md)).
- **Usar la variación a favor.** Generar varias respuestas y quedarse con la mejor es una forma de
  gastar más cómputo en la inferencia; está en [Razonamiento](razonamiento.md), aunque Huyen, según el
  índice de su libro, pone el *test-time compute* como una subsección del muestreo.

## Salidas estructuradas: restringir lo que se puede muestrear

Cuando la salida la lee un programa (un JSON con campos, los argumentos de una
[herramienta](../Agentes/uso-de-herramientas.md)), un JSON mal formado rompe el flujo. Hay tres niveles
de garantía:

| Nivel | Qué asegura | Qué no asegura |
|---|---|---|
| Pedir el formato en el [prompt](../Contexto/prompt.md) | Nada; el modelo suele cumplir | Que el JSON sea válido |
| Modo JSON | Según OpenAI, que la salida sea JSON válido | Que respete el esquema |
| Salidas estructuradas con esquema | Que la salida respete el JSON Schema dado | Que los valores sean correctos |

El mecanismo de las salidas estructuradas actúa en el muestreo. Willard y Louf (2023) describen la
generación como transiciones de una máquina de estados finita, con un índice sobre el vocabulario que
dice qué tokens son válidos en cada estado según una expresión regular o una gramática; los demás
tokens quedan con probabilidad cero antes de elegir. Lo implementaron en la biblioteca Outlines. La
documentación de Anthropic llama a lo que ofrece "constrained decoding" y garantiza "No JSON parsing
errors"; la de OpenAI dice que "Structured Outputs constrains completed, non-refusal model output to
your supplied JSON Schema", sin describir el mecanismo.

Las dos documentaciones dejan ver los límites:

- **El rechazo y el corte quedan afuera.** La garantía de OpenAI cubre la salida completa y que no es
  un rechazo; un rechazo o una respuesta cortada por el límite de tokens se manejan aparte.
- **No todo JSON Schema está soportado.** La documentación de Anthropic, por ejemplo, excluye esquemas
  recursivos y restricciones de rango numérico y de largo.
- **El primer uso de un esquema tarda más**, porque hay que compilar la gramática.
- **La forma no es la verdad.** El esquema asegura que `total` sea un número, no que sea el número de
  la factura. OpenAI avisa que las reglas de negocio que el esquema no expresa hay que validarlas
  aparte; esa validación es un [guardrail](../Produccion/guardrails.md).

## Qué leer sobre muestreo

El abstract de [Holtzman y otros](https://arxiv.org/abs/1904.09751), para la intuición de por qué lo
más probable no es lo mejor. Para salidas estructuradas, la documentación del proveedor que se use,
porque ahí están la garantía concreta y lo que no se soporta: la de
[Anthropic](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) o la de
[OpenAI](https://developers.openai.com/api/docs/guides/structured-outputs). Fijarse en qué partes del
esquema se rechazan. Huyen, *AI Engineering*, capítulo 2, sección "Sampling", trata estrategias,
cómputo en inferencia y salidas estructuradas (leído solo por su índice).
