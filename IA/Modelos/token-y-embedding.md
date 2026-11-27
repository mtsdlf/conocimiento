---
resumen: >-
  Un token es la unidad en que el modelo parte el texto para leerlo y escribirlo (una palabra, un
  pedazo de palabra o un byte), y un embedding es el vector de números con que el modelo representa
  cada token por dentro.
estado: borrador
estabilidad: estable
fuentes:
  - https://arxiv.org/abs/1508.07909
  - https://arxiv.org/abs/2305.15425
  - https://github.com/karpathy/minbpe
  - https://jalammar.github.io/illustrated-transformer/
  - https://web.stanford.edu/~jurafsky/slp3/
  - http://cs336.stanford.edu/spring2025/
aliases: [token, tokens, tokenización, tokenizer, tokenizador, embedding, embeddings, BPE, byte pair encoding, vocabulario]
creado: 2026-11-27
revisado:
---

# Token y embedding

Un token es la unidad en que el modelo parte el texto para leerlo y escribirlo (una palabra, un
pedazo de palabra o un byte), y un embedding es el vector de números con que el modelo representa
cada token por dentro.

Para quien construye un producto, el token es la unidad de cuenta de todo: el precio se cobra por
token, la [ventana de contexto](transformer.md#la-ventana-de-contexto) se mide en tokens y la latencia
crece con los tokens que el modelo tiene que generar ([Inferencia](../Produccion/inferencia.md)). El
embedding importa por otro lado: es la representación que usa la
[recuperación](../Contexto/recuperacion.md) para buscar por significado.

## Del texto al número y de vuelta

El modelo no ve letras. El camino de una consulta es este:

1. El **tokenizador** parte el texto en tokens y reemplaza cada uno por su número en un vocabulario
   fijo.
2. Cada número se convierte en un **embedding**, un vector de números (lectura de esta base: esos
   vectores son parámetros del modelo y se ajustan durante el [preentrenamiento](preentrenamiento.md)).
3. El [Transformer](transformer.md) procesa esos vectores y, al final, da una probabilidad para cada
   token del vocabulario como próximo token.
4. El [muestreo](muestreo.md) elige uno, que se vuelve texto y se agrega a la entrada para predecir
   el siguiente.

Lectura de esta base: el vocabulario se fija antes de entrenar, porque cada embedding corresponde a un
token de ese vocabulario.

## Por qué se parte en pedazos de palabra

Un vocabulario de palabras enteras deja afuera las palabras raras, los nombres propios y las
palabras mal escritas. Sennrich, Haddow y Birch (2015) propusieron codificar las palabras raras o
desconocidas "as sequences of smaller subword units" con *byte pair encoding* (BPE). El procedimiento,
según la sección 3.2 del paper: se arranca con un vocabulario de caracteres, se representa cada
palabra como una secuencia de caracteres, y se cuentan todos los pares de símbolos y se reemplaza
el par más frecuente por un símbolo nuevo, una y otra vez. El tamaño final del vocabulario es el
inicial más el número de fusiones, "the only hyperparameter of the algorithm". El paper era de traducción automática: mejoró 1,1 BLEU en inglés-alemán y 1,3 en
inglés-ruso sobre el respaldo por diccionario.

El repositorio [`minbpe`](https://github.com/karpathy/minbpe) de Andrej Karpathy muestra que la idea
sigue en los LLM: implementa BPE en tres versiones, una de ellas (`GPT4Tokenizer`) que reproduce el
tokenizador de la biblioteca tiktoken. La versión con expresión regular impide que una fusión cruce
categorías como letras, números y puntuación.

> [!NOTE]
> Sin fuente todavía: por qué partir los números en tokens daña la aritmética del modelo.

## El mismo texto cuesta distinto según el idioma

Petrov et al. (NeurIPS 2023) midieron que el mismo texto traducido a distintos idiomas puede dar
hasta 15 veces más tokens según el idioma, y que los modelos a nivel de carácter o de byte muestran
diferencias de más de 4 veces entre algunos pares. Quien escribe en esos idiomas paga más por la
misma consulta, espera más la respuesta y le entra menos texto en la ventana. La cifra para
castellano frente a inglés no está en las fuentes leídas: conviene medirla con el tokenizador del
modelo que se use.

Lo mismo pasa entre versiones de un proveedor: un tokenizador nuevo cambia cuántas palabras entran en
la misma cantidad de tokens, y con eso el costo de un mismo prompt. La ficha de
[Modelos disponibles](modelos-disponibles.md) trae un caso fechado.

## Qué representa un embedding

Dentro del modelo, cada token es un vector de muchas dimensiones, y la atención del
[Transformer](transformer.md) opera sobre esos vectores: según Alammar, cada token genera a partir de
su vector una consulta, una clave y un valor. Fuera del modelo, "embedding" nombra también el vector
que representa un texto entero, que es lo que se guarda en un índice para la
[recuperación](../Contexto/recuperacion.md).

> [!NOTE]
> Sin fuente todavía: una fuente primaria sobre los embeddings como representación del significado
> (Bengio et al., 2003; word2vec). El capítulo 5 de Jurafsky y Martin los trata, pero solo se leyó su
> índice.

## Qué leer sobre tokens

El README de [`minbpe`](https://github.com/karpathy/minbpe), y el video "Let's build the GPT
Tokenizer" que enlaza (no se pudo ver para esta nota), para ver BPE funcionando paso a paso. El
abstract de [Petrov et al.](https://arxiv.org/abs/2305.15425), para el costo por idioma. Para
embeddings, Jurafsky y Martin, [*Speech and Language Processing*](https://web.stanford.edu/~jurafsky/slp3/),
capítulos 2 ("Words and Tokens") y 5 ("Embeddings"); la clase 1 de
[CS336](http://cs336.stanford.edu/spring2025/) (Stanford) también empieza por la tokenización.
Fijarse en cuántos tokens da una frase en castellano frente a la misma en inglés.
