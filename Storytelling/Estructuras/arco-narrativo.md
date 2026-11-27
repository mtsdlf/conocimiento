---
resumen: >-
  El arco narrativo es la forma que toma una historia en el tiempo: cómo sube y baja la suerte del protagonista desde el comienzo hasta el final. Bajo ese nombre circulan tres cosas distintas: la pirámide atribuida a Freytag, el arco en tres actos del guion y los seis arcos emocionales que Reagan y colegas midieron por computadora en novelas.
estado: vigente
estabilidad: estable
fuentes:
  - "Reagan, Mitchell, Kiley, Danforth y Dodds (2016), EPJ Data Science (preprint arXiv:1606.07772): https://arxiv.org/abs/1606.07772 y https://arxiv.org/pdf/1606.07772 (texto)"
  - "Freytag (1863), Die Technik des Dramas: https://www.gutenberg.org/ebooks/50616; traducción: https://ia600208.us.archive.org/25/items/freytagstechniqu00freyuoft/freytagstechniqu00freyuoft.pdf (no se leyó; según resúmenes)"
  - "Liddle (2024), Falling Action: Against 'Freytag's Pyramid', Studies in the Novel 56(4), 415: https://www.ebsco.com/articles/history/f3f6cd28-136f-5185-998f-6a1b781c9469/falling-action-against-freytag-s-pyramid (abstract)"
  - "Pouli (2023), tesis de Leiden: https://studenttheses.universiteitleiden.nl/access/item%3A3641795/download (según resumen)"
  - "NULab (Northeastern), arcos emocionales en televisión: https://cssh.northeastern.edu/nulab/emotional-arcs-television-nulab-project/ (según resumen)"
  - "Electric Literature: https://electricliterature.com/data-analysis-of-novels-reveals-nothing-new/ (según resumen); Elkins, extracto de Cambridge: https://assets.cambridge.org/97810092/70397/excerpt/9781009270397_excerpt.pdf (según resumen)"
  - "Storytelling/.investigacion/historia-y-estructuras.md, nota sobre la división del árbol y sección 3"
aliases: [arco, arco narrativo, arco emocional, pirámide de Freytag, Freytag's pyramid, tres actos, three-act structure, narrative arc, emotional arc, seis arcos, man in a hole]
creado: 2026-11-27
revisado: 2026-11-27
---

# Arco narrativo

El arco narrativo es la forma que toma una historia en el tiempo: cómo sube y baja la suerte del protagonista desde el comienzo hasta el final. Bajo ese nombre circulan tres cosas distintas: la pirámide atribuida a Freytag, el arco en tres actos del guion y los seis arcos emocionales que Reagan y colegas midieron por computadora en novelas.

Es la más general de las [estructuras](estructuras.md): las otras, del [viaje del héroe](viaje-del-heroe.md) a las [estructuras cortas](estructuras-cortas.md), dibujan algún arco. El arco ordena las piezas de [la historia](../La-historia/la-historia.md): el [conflicto](../La-historia/personaje-y-conflicto.md) hace subir la tensión y el cambio la resuelve (lectura de esta base).

## Tres cosas con el mismo nombre

| Qué se llama arco | Qué es | De dónde sale | Qué evidencia tiene |
|---|---|---|---|
| Pirámide de Freytag | Cinco partes de una obra de teatro: exposición, ascenso, clímax, descenso y catástrofe | Freytag, *Die Technik des Dramas* (1863), sobre drama clásico y de Shakespeare | Análisis de obras; la pirámide sería una popularización posterior |
| Arco en tres actos | Una receta de guion en tres partes | Oficio del guion | Ninguna fuente primaria encontrada |
| Arcos emocionales | La curva de sentimiento de un texto, medida por computadora | Reagan y colegas (2016), sobre 1.327 novelas | Medición sobre un corpus, con réplicas parciales |

Las tres responden preguntas distintas. Freytag describe cómo se construye una obra de teatro. El arco en tres actos es una receta de escritura. Reagan y colegas miden la curva emocional de libros ya escritos.

## La pirámide atribuida a Freytag

Freytag publicó *Die Technik des Dramas* en 1863. La pirámide de cinco partes que se enseña con su nombre (exposición, ascenso, clímax, descenso y catástrofe) es, según resúmenes, una popularización posterior. Su análisis es de drama clásico y de Shakespeare, no de narrativa moderna en general.

> [!IMPORTANT]
> La pirámide quizás no sea de Freytag. Los resultados de búsqueda discrepan sobre si su esquema tiene cinco o siete partes. Liddle (2024) sostiene que la pirámide atribuida a Freytag no es realmente suya, y que su difusión escolar fue "historical accident and bureaucratic mandate" (según el abstract). No se contrastó con el libro.

## El arco en tres actos

El arco en tres actos es una receta del oficio del guion, no un hallazgo ni una teoría con autor identificado.

> [!NOTE] Sin fuente todavía: una fuente primaria que documente el arco en tres actos: quién lo formuló, cómo se llaman sus partes y dónde termina cada una. No se encontró ninguna.

## Los seis arcos de Reagan y colegas

Reagan, Mitchell, Kiley, Danforth y Dodds (2016) midieron la curva emocional de novelas con computadora. Partieron del corpus de Project Gutenberg, de cerca de 50.000 libros. Lo filtraron a obras en inglés con entre 20.000 y 100.000 palabras, con más de 40 descargas y clasificadas como ficción inglesa por la Biblioteca del Congreso. Quedaron 1.327 historias.

Para cada libro puntuaron ventanas de texto con el Hedonometer, una lista de palabras con valor emocional, y obtuvieron una curva. Tres métodos (descomposición matricial, aprendizaje supervisado y aprendizaje no supervisado) dieron seis arcos:

| Arco | Forma |
|---|---|
| "Rags to riches" | Sube |
| Tragedia, "Riches to rags" | Baja |
| "Man in a hole" | Cae y sube |
| "Icarus" | Sube y cae |
| "Cinderella" | Sube, cae y sube |
| "Oedipus" | Cae, sube y cae |

"Man in a hole" es la forma más fácil de reconocer en un caso comercial: el comercio estaba bien, algo lo hizo caer y salió. Es una lectura de esta base; el estudio no mide mensajes comerciales.

## Qué arcos se descargan más

Según el paper, "Icarus", "Oedipus" y dos "Man in a hole" seguidos son los tres arcos más exitosos medidos por descargas. Los primeros cuatro modos de la descomposición, que reúnen más libros, no son los más populares. Los propios autores advierten que "downloads are only a rough proxy for success" y que los resultados "are influenced by individual books".

## Los límites de la medición

El paper reconoce tres límites. Mide ficción larga en inglés y de dominio público, no mensajes de marca ni presentaciones. El arco sale de palabras con valor emocional, no de cómo lee una persona. Y las descargas son un indicador flojo del éxito.

Las réplicas encontradas son parciales:

- Pouli (2023), en una tesis de Leiden, usó otra herramienta de sentimiento: la mayoría de las formas reaparecen, pero a veces una historia cae en otra forma (según resumen).
- El proyecto NULab, de Northeastern, aplicó el método a televisión y no logró resultados tan fuertes: los arcos eran "only a rough fit" (según resumen).
- Elkins, en un extracto de Cambridge, dice que el arco refleja el sentimiento de fondo más que la trama, y que depende del modelo y del suavizado (según resumen).
- Electric Literature, una revista sin revisión por pares, lo llama reduccionista.

No se buscó un comentario revisado por pares sobre el paper.

## Para qué sirve el arco en un mensaje de negocio

El arco sirve para revisar si un texto tiene movimiento: si el lector ve una caída y una salida, o solo una lista de cosas buenas. Una propuesta que empieza con el problema del cliente y termina con el cliente resolviéndolo dibuja un "Man in a hole"; es una lectura de esta base, no algo que el estudio midiera. Ninguna fuente midió qué arco convence más en una venta o una presentación; la pregunta de cuánto convence una historia está en [historia o argumento](../Por-que-convence/historia-o-argumento.md).

## Qué leer

Reagan y colegas (2016), la sección "The Success of Stories" y las figuras de los seis modos. Fijarse en que es ficción larga en inglés, en que mide sentimiento por palabras y en que las descargas son un indicador flojo. Para Freytag, su propio texto, con el artículo de Liddle como contrapeso.
