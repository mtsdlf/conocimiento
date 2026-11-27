---
resumen: >-
  La armonía es la convivencia de las notas de dos temas que suenan a la vez. Importa solo donde
  hay material tonal (un bajo con notas, una melodía, un acorde) en lo que se superpone; con
  percusión sola no hay nada que pueda chocar.
estado: vigente
estabilidad: semi
fuentes:
  - "Phil Morse, How Important Is It For DJs To Mix In Key?, Digital DJ Tips (act. 2024-02-21): https://www.digitaldjtips.com/how-important-is-it-to-mix-in-key/"
  - "Ryan Keeling, How do DJs approach harmonic mixing?, Pioneer DJ Blog: https://blog.pioneerdj.com/?p=711"
  - "Kim et al., A Computational Analysis of Real-World DJ Mixes, ISMIR 2020: https://program.ismir2020.net/static/final_papers/352.pdf"
  - "Korzeniowski y Widmer, End-to-End Musical Key Estimation Using a CNN, EUSIPCO 2017: https://arxiv.org/pdf/1706.02921"
  - "Faraldo, Tonality Estimation in Electronic Dance Music, tesis doctoral UPF, 2017 (descripción): https://zenodo.org/records/1154586"
  - "Ryan Keeling, entrevista a Boris Brejcha, Pioneer DJ Blog: https://blog.pioneerdj.com/?p=4768"
  - "MusicRadar, harmonic mixing (resumen del buscador): https://musicradar.com/news/harmonic-mixing"
  - "Bonedo, Harmonic Mixing Basics (resumen del buscador): https://www.bonedo.de/artikel/harmonic-mixing/2"
aliases: [Mezcla armónica, Harmonic mixing, Mezclar en tono, Mixing in key]
creado: 2026-11-27
revisado: 2026-11-27
---

# Armonía

La armonía es la convivencia de las notas de dos temas que suenan a la vez. Importa solo donde
hay material tonal (un bajo con notas, una melodía, un acorde) en lo que se superpone; con
percusión sola no hay nada que pueda chocar.

Es la segunda dimensión de convivencia del [todo](../dj.md), y depende del
[Espectro](../Espectro/espectro.md): lo que el EQ saca de la transición ya no puede desafinar.
Recibe de [Tiempo](../Tiempo/tiempo.md) un problema propio, porque cambiar la velocidad de un tema
cambia su altura, y le sirve a la [Selección](../Seleccion/criterio-de-seleccion.md) como uno de
los criterios para elegir el próximo tema, nunca el único.

## Cuándo pesa la armonía

La regla que ordena todo lo demás es de Digital DJ Tips: "Mixing in key is only necessary if the
two tracks contain musical information in the parts you are mixing together"
([Digital DJ Tips](https://www.digitaldjtips.com/how-important-is-it-to-mix-in-key/)). Con solo
percusión, chequear la tonalidad "gains nothing", según el mismo artículo. El informe de
investigación la lee como un caso del espectro: dos notas solo chocan si suenan juntas, y el
[enmascaramiento](../Espectro/enmascaramiento.md) y el choque tonal pasan en el mismo lugar, la
zona que comparten los dos temas.

En techno de pista, eso pesa de dos maneras:

- Hay temas donde casi no importa. Un DJ citado por MusicRadar dice que gran parte del techno
  tiene contenido melódico muy simple y que el cambio se hace con filtro y resonancia más que con
  acordes, así que chocar es difícil, según su resumen
  ([MusicRadar](https://musicradar.com/news/harmonic-mixing)).
- El bajo puede tener notas. Que un bajo con altura definida choque con el bajo o el pad del otro
  tema, y que el bombo del techno también suela tener altura, es inferencia, sin fuente.

Una salida práctica es hacer la transición en una sección de percusión, antes de que entren las
melodías o los bajos del tema nuevo, según el resumen de
[Bonedo](https://www.bonedo.de/artikel/harmonic-mixing/2). MusicRadar y Bonedo se apoyan en lo que
dice Digital DJ Tips y no son independientes. Dónde están esas secciones lo dice la
[Forma](../Forma/secciones-de-un-tema.md); sacarle el grave al tema entrante con el
[swap de graves](../Espectro/swap-de-graves.md) también le saca, por inferencia, las notas del
bajo.

## Cuánto debe mandar la tonalidad

> [!IMPORTANT] Disputado: cuánto debe mandar la tonalidad. Para Sef Kombo, "Harmonic mixing is
> absolutely essential in my opinion"; Erol Alkan la llama "an incredible tool, I couldn't imagine
> not being able to use it", pero nunca deja que la tonalidad "dictate" sus elecciones; DJ Puffy
> cuenta que temas que "shouldn't fit" encajan, y que "that often happens with minimal tracks"
> ([Pioneer DJ Blog](https://blog.pioneerdj.com/?p=711)). Digital DJ Tips advierte que elegir solo
> por tonalidad lleva a elegir temas por compatibilidad y no por ser el disco justo, y que una
> mezcla en tono puede sonar mal: "if a mix sounds bad, it is bad"
> ([Digital DJ Tips](https://www.digitaldjtips.com/how-important-is-it-to-mix-in-key/)). Ninguna
> de las voces citadas habla del techno de pista ni del sello ARTS.

Los datos de mezclas reales no resuelven la discusión. En 24.202 temas de mezclas públicas, solo el
2,5 % se transpuso, y de esos el 94,3 % un solo semitono; los autores concluyen que los DJs
"generally do not perform key transposition much"
([Kim et al., ISMIR 2020](https://program.ismir2020.net/static/final_papers/352.pdf)). Eso dice que
cambiar la tonalidad de un tema es raro. No dice si los DJs eligen temas en tonalidades
compatibles: ninguna fuente consultada mide esa proporción.

Boris Brejcha usa la tonalidad en otro lugar. Cuenta que, después de una prueba en el auto,
encontró que G y F "had the most impact", y que la mayoría de sus temas están en esas tonalidades
([Pioneer DJ Blog](https://blog.pioneerdj.com/?p=4768)). Ahí la tonalidad es una decisión de
producción y no de empalme.

## Lo que la máquina dice de la tonalidad

Los programas de DJ analizan la tonalidad de cada tema y la muestran con una notación de rueda
(ver [tonalidad y compatibilidad](tonalidad-y-compatibilidad.md)). Ese dato es orientativo. En un
conjunto de música electrónica de baile, los mejores sistemas académicos de la comparación de
Korzeniowski y Widmer aciertan la tonalidad exacta en el 63,7 % y el 67,9 % de los fragmentos
([arXiv](https://arxiv.org/pdf/1706.02921)): cerca de dos de cada tres. Las cifras y sus límites
están en la [ficha de detección de tonalidad](ficha-deteccion-de-tonalidad.md).

La tesis de Faraldo aporta un argumento de fondo: la práctica corriente usa un vocabulario
centrado en la tonalidad clásica y un modelo binario mayor/menor que puede no servir para la
música popular; propone etiquetas más abiertas para configuraciones modales o tonalmente ambiguas
([tesis, descripción](https://zenodo.org/records/1154586)).

## Cómo se decide en la cabina

Los pasos combinan la regla de Digital DJ Tips, la rueda de Mixed In Key y la sugerencia de
Bonedo; el orden es de esta nota.

1. Fijate si en la parte que vas a superponer hay notas: bajo con altura, melodía, pad, voz. Si no
   hay, la tonalidad no decide nada.
2. Si hay, mirá la tonalidad que muestra el programa y la regla de la rueda: misma tonalidad o un
   paso al lado suele andar.
3. Confirmá en auriculares con los dos temas sonando. Si choca, manda el oído y no la etiqueta.
4. Si choca y querés el tema igual, hacé la transición en una zona sin notas o sacá el grave del
   entrante hasta que el otro se vaya.

## Qué hay adentro de la armonía

- [Tonalidad y compatibilidad](tonalidad-y-compatibilidad.md): tono y modo, la rueda de
  compatibilidad, qué combina y por qué mover el pitch cambia la tonalidad.
- [Ficha de detección de tonalidad](ficha-deteccion-de-tonalidad.md): cuánto aciertan los
  detectores automáticos según los papers, y lo que dicen los fabricantes; copiada el 2026-11-27.
