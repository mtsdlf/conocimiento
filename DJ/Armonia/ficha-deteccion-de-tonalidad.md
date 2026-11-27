---
resumen: >-
  Cuánto aciertan los detectores automáticos de tonalidad en música electrónica de baile: las
  cifras académicas medidas en el conjunto GiantSteps, cómo se cuentan los aciertos parciales y lo
  que afirman los fabricantes, que no está contrastado.
estado: borrador
estabilidad: volatil
fuentes:
  - "Korzeniowski y Widmer, End-to-End Musical Key Estimation Using a CNN, EUSIPCO 2017, Tabla I: https://arxiv.org/pdf/1706.02921"
  - "GiantSteps key dataset, README (Knees et al., ISMIR 2015): https://github.com/GiantSteps/giantsteps-key-dataset"
  - "mir_eval, documentación de la métrica de tonalidad (resumen del buscador): https://mir-eval.readthedocs.io/latest/api/key.html"
  - "Faraldo, Gómez, Jordà y Herrera, Key Estimation in Electronic Dance Music, ECIR 2016 (abstract): https://recercat.cat/handle/10230/33060"
  - "Faraldo, Tonality Estimation in Electronic Dance Music, tesis doctoral UPF, 2017 (descripción): https://zenodo.org/records/1154586"
  - "Mixxx, manual 2.5, Key Detection: https://manual.mixxx.org/2.5/en/chapters/preferences/key_detection"
  - "Mixxx, New in 2.3: KeyFinder support, 2021-04-08 (resumen del buscador): https://mixxx.org/news/2021-04-08-new-in-2-3-keyfinder"
  - "Mixed In Key, Harmonic Mixing Guide (fabricante): https://mixedinkey.com/harmonic-mixing-guide/"
  - "Ryan Keeling, How do DJs approach harmonic mixing?, Pioneer DJ Blog: https://blog.pioneerdj.com/?p=711"
creado: 2026-11-27
revisado:
---

# Ficha de detección de tonalidad

Cuánto aciertan los detectores automáticos de tonalidad en música electrónica de baile: las
cifras académicas medidas en el conjunto GiantSteps, cómo se cuentan los aciertos parciales y lo
que afirman los fabricantes, que no está contrastado.

Implementa la parte de "qué dice la máquina"
de [tonalidad y compatibilidad](tonalidad-y-compatibilidad.md) y de la
[armonía](armonia.md).

Copiado de las fuentes del frontmatter el 2026-11-27. La fuente viva de las cifras académicas es
la Tabla I de [Korzeniowski y Widmer 2017](https://arxiv.org/pdf/1706.02921).

## Contra qué se mide

El conjunto GiantSteps key tiene 604 fragmentos de dos minutos de una tienda de música
electrónica de baile. Sus etiquetas salieron de "forum entries of people correcting the key
annotations": correcciones de usuarios, sin verificación experta descrita
([README](https://github.com/GiantSteps/giantsteps-key-dataset)). Es la vara de casi todas las
cifras de abajo, con ese límite.

La métrica corriente (MIREX, implementada en mir_eval) da puntaje parcial a los errores cercanos,
según su resumen ([mir_eval](https://mir-eval.readthedocs.io/latest/api/key.html)). La columna "En
la rueda" es de esta nota, sin fuente:

| Resultado | Puntaje | En la rueda |
|---|---|---|
| Misma tonalidad y modo | 1,0 | Acierto |
| Una quinta arriba | 0,5 | Una hora al lado |
| Relativa mayor/menor | 0,3 | Misma hora, otra letra |
| Paralela mayor/menor | 0,2 | Otra hora |
| Cualquier otra | 0,0 | Error |

Por eso el "puntaje ponderado" es más alto que el porcentaje de aciertos exactos. Para un DJ, los
errores de quinta y de relativa son los menos graves, porque caen en tonalidades que la rueda da
como compatibles (inferencia).

## Lo que miden los papers

De la Tabla I de [Korzeniowski y Widmer 2017](https://arxiv.org/pdf/1706.02921), en GiantSteps:

| Sistema | Tonalidad exacta | Puntaje ponderado MIREX |
|---|---|---|
| Red neuronal de los autores, entrenada con electrónica | 67,9 % | 74,3 |
| Mejor sistema de referencia para electrónica (EDMM) | 63,7 % | 70,1 |
| Sistema de referencia general (QM) | 39,6 % | 50,4 |

- Los errores "otros" (ni quinta, ni relativa, ni paralela) van del 13,9 % al 18,5 % en los
  mejores sistemas, según la misma tabla.
- Un sistema entrenado con pop y rock cae a 57,3 de puntaje ponderado en electrónica, contra
  74,3 entrenado con electrónica: lo que sirve en un género no vale en otro.
- Los sistemas EDM de la tabla son "de referencia" de un trabajo previo que el texto describe como
  los mejores de MIREX en electrónica; que sean los de Faraldo y otros (ECIR 2016) es inferencia
  del informe, no está verificado. Ese paper solo se leyó por su abstract, que habla de
  "interesting improvements" sin cifras ([ECIR 2016](https://recercat.cat/handle/10230/33060)).

En números redondos: el mejor sistema académico acierta la tonalidad exacta en dos de cada tres
fragmentos, y uno de cada seis le erra lejos.

## Lo que dicen los fabricantes

- Mixed In Key, empresa dueña de la rueda Camelot, afirma que "independent tests consistently
  show Mixed In Key to be the most accurate key detection system on the planet", sin fuentes ni
  método en la página ([guía del fabricante](https://mixedinkey.com/harmonic-mixing-guide/)). Es
  una afirmación del fabricante.
- Mixxx llama a su detector "de alta precisión" en su manual, sin cifras; por defecto analiza
  el tema entero, y su modo "Fast Analysis" usa solo el primer minuto
  ([manual](https://manual.mixxx.org/2.5/en/chapters/preferences/key_detection)). Su analizador por
  defecto es el Queen Mary Key Analyzer, y desde la versión 2.3 suma KeyFinder, según su resumen
  ([noticia](https://mixxx.org/news/2021-04-08-new-in-2-3-keyfinder)). El manual no lista las
  notaciones de tonalidad disponibles.
- Un DJ citado por un fabricante de equipos dice que Mixed In Key "is not always 100% accurate"
  ([Pioneer DJ Blog](https://blog.pioneerdj.com/?p=711)).

> [!NOTE] Sin fuente todavía: una comparación independiente de los detectores comerciales
> (Mixed In Key, rekordbox, Traktor, Serato) en techno. Hay tablas con productos comerciales en
> Knees y otros (ISMIR 2015) y en la [tesis de Faraldo](https://zenodo.org/records/1154586), que no
> se pudieron leer. Las cifras que circulan en foros no se usan.

## Qué hacer con estas cifras

Con un acierto exacto de dos de cada tres en el mejor caso académico, conviene tomar la tonalidad
que muestra el programa como una pista y confirmarla de oído antes de superponer dos temas con
notas. Si el análisis rápido usa solo el primer minuto, y la intro de un techno suele ser solo
percusión, el resultado puede salir de una parte sin notas (inferencia, sin fuente).
