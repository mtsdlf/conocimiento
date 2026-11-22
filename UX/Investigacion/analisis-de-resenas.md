---
resumen: >-
  El análisis de reseñas lee lo que la gente publica sobre un producto propio o ajeno (en tiendas de apps, directorios de software y foros) y lo codifica por temas para saber de qué se queja y qué valora. Es barato y llega a los rivales, pero las reseñas son una muestra sesgada: escriben sobre todo los muy conformes y los muy enojados, y una parte es falsa.
estado: vigente
estabilidad: semi
fuentes:
  - "Hu, Pavlou y Zhang (2009), Overcoming the J-shaped distribution of product reviews, Communications of the ACM 52(10):144-147, doi 10.1145/1562764.1562800 (solo la introducción, vía OpenAlex)"
  - "Hu, Pavlou y Zhang (2007), Why do Online Product Reviews have a J-shaped Distribution? Overcoming Biases in Online Word-of-Mouth Communication, manuscrito enviado a Marketing Science: https://archive.nyu.edu/bitstream/2451/14951/2/usedbook1.pdf (leídos el abstract, la introducción y el experimento)"
  - "Luca y Zervas (2016), Fake It Till You Make It: Reputation, Competition, and Yelp Review Fraud, Management Science 62(12):3412-3427, doi 10.1287/mnsc.2015.2304 (solo abstract)"
  - "Pagano y Maalej (2013), User feedback in the appstore: An empirical study, IEEE International Requirements Engineering Conference, pp. 125-134, doi 10.1109/RE.2013.6636712 (solo abstract)"
  - "Braun y Clarke (2006), Using thematic analysis in psychology, Qualitative Research in Psychology 3(2):77-101, doi 10.1191/1478088706qp063oa (solo abstract)"
  - "Maria Rosala, NN/g (17-ago-2022), Analyze Qualitative Data: Thematic Analysis: https://www.nngroup.com/articles/thematic-analysis/ (leída a través del resumen de una herramienta)"
  - "UX/.investigacion/evaluacion-competitiva-y-cambio.md"
aliases: [review mining, análisis de opiniones, minería de reseñas, análisis de reviews, reseñas de usuarios, user reviews, app store reviews, J-shaped distribution, distribución en J]
creado: 2026-11-22
revisado: 2026-11-22
---

# Análisis de reseñas

El análisis de reseñas lee lo que la gente publica sobre un producto propio o ajeno (en tiendas de apps, directorios de software y foros) y lo codifica por temas para saber de qué se queja y qué valora. Es barato y llega a los rivales, pero las reseñas son una muestra sesgada: escriben sobre todo los muy conformes y los muy enojados, y una parte es falsa.

En el [mapa de métodos](metodos-de-investigacion.md) es actitudinal y cualitativo, como la [entrevista de usuario](entrevista-de-usuario.md), con una diferencia: nadie pregunta. La persona escribió cuando quiso y sobre lo que quiso, y eso define tanto su valor como sus sesgos. Llega a los clientes de un rival sin pasar por él ni por ellos; las reseñas figuran entre las [fuentes públicas](../../Estrategia-competitiva/Analisis-de-competidores/fuentes-publicas.md) del análisis de competidores.

## Qué dicen las reseñas y qué no

Pagano y Maalej (2013) analizaron más de un millón de reseñas de la tienda de apps de Apple, según su abstract. Encontraron que la mayoría llega poco después de una versión nueva y decae rápido. Una reseña suele mezclar varios temas, como experiencia de uso, errores y pedidos de funciones. Y lo negativo "is typically destructive and misses context details and user experience": dice qué molestó, pero no en qué situación ni qué intentaba hacer la persona.

De ahí sale lo que el método puede contestar y lo que no (lectura de esta base a partir de esas fuentes):

| Contesta | No contesta |
|---|---|
| qué temas aparecen y cuáles se repiten | cuántos usuarios sufren cada problema |
| con qué palabras describe la gente el producto y al rival | qué hacía la persona cuando falló |
| qué cambio de versión disparó quejas | si el promedio de estrellas refleja la calidad |
| qué valoran del rival los que lo eligieron | por qué no lo eligieron los que nunca lo probaron |

Para la causa de un problema hace falta observar, con un [test de usabilidad](../Evaluacion/test-de-usabilidad.md); para saber por qué alguien se fue a un rival, una [entrevista de cambio](entrevista-de-cambio.md).

## Por qué las estrellas forman una J

Las reseñas de una tienda en línea no se reparten como las opiniones de todos los compradores. Hu, Pavlou y Zhang (2009) muestran una distribución en J, "with mostly 5-star ratings, some 1-star ratings, and hardly any ratings in between". Por eso, concluyen, "the average is a poor proxy of product quality".

En la versión de trabajo del estudio (2007) explican la J con dos sesgos de autoselección:

- **Sesgo de compra**: solo compra, y por eso solo reseña, quien ya tenía buena disposición hacia el producto.
- **Sesgo de subreporte**: quien quedó muy conforme o muy enojado escribe más que quien quedó a medias.

Lo probaron con un experimento. Dieron un mismo CD de música a 66 estudiantes y obtuvieron 60 reseñas (91%). Las opiniones de todos salieron con una distribución aproximadamente normal, mientras que las de Amazon para el mismo disco formaban una J. La media de Amazon fue 3,54 y la del experimento 3,12 (p<.05). En Amazon, más de 60% de las reseñas eran de 1 o 5 estrellas; en el experimento, menos de 10%.

Para leer reseñas, la consecuencia práctica es mirar la distribución y no el promedio (los autores proponen usar la media, el desvío y las dos modas). Una tienda de apps con 4,6 estrellas y otra con 4,3 pueden no diferir en calidad. Además, el que reseña ya eligió el producto: las reseñas de un rival hablan de sus clientes, no de los que lo descartaron.

## Las reseñas falsas

Una parte de las reseñas no la escribió un cliente. Luca y Zervas (2016) estudiaron restaurantes en Yelp y usaron como indicador de fraude las reseñas que el filtro del sitio marca como sospechosas. Según su abstract, "roughly 16% of restaurant reviews on Yelp are filtered", y esas reseñas son más extremas que las demás.

El fraude sigue incentivos. Es más probable cuando el negocio tiene una reputación débil (pocas reseñas o malas recientes). Las cadenas, que ganan menos con Yelp, lo cometen menos. Y cuando aumenta la competencia, los restaurantes reciben más reseñas falsas desfavorables; que algunas las escriban los rivales es una lectura de esta base, no un hallazgo del abstract.

El estudio es sobre restaurantes en un sitio. No se encontró un estudio equivalente sobre tiendas de apps ni sobre directorios de software como G2 o Capterra, donde además hay reseñas incentivadas por el propio proveedor. Por inferencia, conviene descartar las reseñas que no dan detalles de uso y desconfiar de los picos de reseñas extremas en pocos días.

## Codificar por temas

El análisis temático es el procedimiento estándar para ordenar texto libre. NN/g lo define como "a systematic method of breaking down and organizing rich data from qualitative research". Un código es "a word or phrase that acts as a label for a segment of text", y un tema "emerges when related findings appear multiple times across participants or data sources". Braun y Clarke (2006), en un artículo metodológico sobre el análisis temático, lo describen como poco delimitado y muy usado, y dan pautas para hacerlo con rigor (según su abstract).

Aplicado a reseñas propias y de rivales, los pasos son los de NN/g, con una adaptación de esta base:

1. Juntá las reseñas de un período fijo, del producto propio y de dos o tres rivales, con fecha, estrellas y versión.
2. Leelas todas antes de codificar, si es posible con alguien más.
3. Poné códigos descriptivos a cada fragmento ("no encuentra cómo exportar", "le cobraron dos veces"). Una reseña lleva varios.
4. Agrupá los códigos en temas interpretativos ("la configuración inicial frustra") y anotá cuántas reseñas y de qué productos tiene cada uno.
5. Tomá distancia y volvé a los datos.
6. Pedí a otra persona que revise si los temas se sostienen.

Contar reseñas por tema ordena, pero no mide la frecuencia del problema entre usuarios, por los sesgos de arriba. En una plataforma de tiendas online, si las reseñas de un rival se quejan de la configuración del envío y las propias no, eso es una hipótesis para probar en un [test competitivo](../Evaluacion/evaluacion-competitiva.md), no un resultado (ejemplo de esta base).

## Los datos son de personas

Una reseña es pública, pero la escribió una persona identificable o casi. En Argentina, armar una base con nombres de quienes reseñan cae en la Ley 25.326 de datos personales aunque los datos sean públicos, según la lectura de [ley argentina y competidores](../../Estrategia-competitiva/Analisis-de-competidores/ley-argentina-y-competidores.md), donde está el texto de la ley; las reglas para recolectar están en [ética y legalidad](../../Estrategia-competitiva/Analisis-de-competidores/etica-y-legalidad.md). Lo seguro es guardar el texto y el código, sin el nombre del autor, y leer los términos de cada sitio antes de automatizar la descarga.

## Qué leer

Hu, Pavlou y Zhang, "Overcoming the J-shaped distribution of product reviews" (CACM, 2009), son cuatro páginas: fijarse en la figura de la J y en los dos sesgos. Para el procedimiento, Rosala, [Analyze Qualitative Data: Thematic Analysis](https://www.nngroup.com/articles/thematic-analysis/), de NN/g: fijarse en la diferencia entre códigos descriptivos e interpretativos.

> [!NOTE] Sin fuente todavía: las seis fases de Braun y Clarke (el paper no se pudo abrir), estudios sobre sesgos y reseñas incentivadas en directorios de software B2B, y sobre cuántas reseñas hacen falta para que un tema sea estable. Las citas de NN/g salen de un resumen que una herramienta hizo de la página.
