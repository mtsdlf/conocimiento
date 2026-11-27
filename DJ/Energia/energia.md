---
resumen: >-
  Energía es la parte del oficio que trata la intensidad que la música le transmite a la pista y
  cómo cambia a lo largo de una sesión: la tensión y la descarga dentro de un tema, la repetición,
  el arco del set y la lectura del público. No tiene una medida aceptada: es una categoría que los
  DJs usan para describir a la vez la música y el baile.
estado: vigente
estabilidad: estable
fuentes:
  - "Marchiano y Tanco, El baile en la música del DJ, El Oído Pensante 9(2), 2021: https://www.redalyc.org/journal/5529/552969184005/552969184005.pdf"
  - "Kell y Tzanetakis, Empirical Analysis of Track Selection and Ordering in Electronic Dance Music using Audio Feature Extraction, ISMIR 2013: https://archives.ismir.net/ismir2013/paper/000210.pdf"
  - "Williams, Meehan, Lattner, Pauwels y Barthet, Temporal Considerations in DJ Mix Information Retrieval and Generation, TIME 2025: https://drops.dagstuhl.de/storage/00lipics/lipics-vol355-time2025/html/LIPIcs.TIME.2025.20/LIPIcs.TIME.2025.20.html"
  - "Guía de un fabricante de software de análisis, Sorting playlists by energy level: https://mixedinkey.com/harmonic-mixing-guide/sorting-playlists-by-energy-level/"
  - "Documentación de una API de streaming, audio features: https://developer.spotify.com/documentation/web-api/reference/get-audio-features"
aliases: [Energy, Nivel de energía]
creado: 2026-11-27
revisado: 2026-11-27
---

# Energía

Energía es la parte del oficio que trata la intensidad que la música le transmite a la pista y cómo cambia a lo largo de una sesión: la tensión y la descarga dentro de un tema, la repetición, el arco del set y la lectura del público. No tiene una medida aceptada: es una categoría que los DJs usan para describir a la vez la música y el baile.

Es la dimensión de dirección del [oficio](../dj.md). [Tiempo](../Tiempo/tiempo.md) y [Forma](../Forma/forma.md) ponen a dos temas en el mismo lugar y [Espectro](../Espectro/espectro.md) los hace convivir; Energía decide hacia dónde va la sesión con eso. Recibe del espectro la densidad (cuántas capas suenan a la vez) y de la forma los lugares donde un tema carga y descarga, sus [secciones](../Forma/secciones-de-un-tema.md). Le entrega a [Selección](../Seleccion/seleccion.md) la pregunta de qué tema hace falta ahora.

## Lo que los DJs llaman energía

No hay una definición medible única y aceptada de energía de baile. Lo que hay es el uso de la palabra entre quienes pinchan. Marchiano y Tanco entrevistaron a tres DJs de fiestas en La Plata y encontraron que describen con la misma categoría, "nivel de energía", tanto la intensidad del baile como la música. La escala tiene dos polos, "arriba" y "abajo", y un extremo, la "explosión". Los DJs perciben la intensidad del baile como efecto de la energía de la música, "estableciendo una relación causal entre ambos" ([Marchiano y Tanco 2021](https://www.redalyc.org/journal/5529/552969184005/552969184005.pdf), sección 2.2).

Es una muestra chica: tres entrevistas semiestructuradas, de noviembre y diciembre de 2019, en una escena local de fiestas que no es la del techno de los ejemplos. Aun así es el único texto abierto que encontró la investigación sobre la energía tal como la vive el DJ, y es la definición que usa este tema. Para leerlo: el resumen y la sección 2.2, "Nivel de energía de la música y del baile", con la relación causa y efecto entre música y baile y la alternancia de momentos "de explosión y de calma".

## Densidad e intensidad, los dos ejes de trabajo

Para hablar de energía sin un número, las notas del tema la descomponen en dos ejes. Son una convención de trabajo para ordenar ideas; ninguna fuente los publica como medida:

| Eje | Qué es | Con qué se mueve |
|---|---|---|
| Densidad | Cuántas capas y eventos suenan a la vez | Sumar o quitar percusión, bajo, sintetizadores; abrir o cerrar bandas con el [ecualizador](../Espectro/ecualizador-y-filtros.md) |
| Intensidad | Con cuánta fuerza llega lo que suena | Sonoridad, peso del bombo, brillo del timbre, tempo |

La literatura de reconocimiento de emoción musical apunta a insumos parecidos para la energía percibida: sonoridad, tempo y timbre, con la advertencia de que no hay consenso sobre cómo se relacionan con la emoción (según el resumen de [un preprint de 2022](https://arxiv.org/pdf/2212.13369)). En sets reales de música electrónica de baile, Kell y Tzanetakis encontraron que "Timbre appears to be an important factor when selecting tracks and ordering tracks" ([ISMIR 2013](https://archives.ismir.net/ismir2013/paper/000210.pdf), abstract).

Subir el volumen aumenta la intensidad sin cambiar nada de la música; eso se trata en [ganancia y volumen percibido](../Espectro/ganancia-y-volumen-percibido.md).

> [!IMPORTANT]
> Algunos programas de análisis ponen a cada tema un número de energía. Un fabricante la puntúa de 1 a 10, con anclas como el nivel 5, donde según ella la gente empieza a bailar; la investigación no encontró el algoritmo publicado ([su guía](https://mixedinkey.com/harmonic-mixing-guide/sorting-playlists-by-energy-level/), según su resumen). Una plataforma de streaming la definió como "a perceptual measure of intensity and activity" de 0,0 a 1,0, basada en rango dinámico y sonoridad percibida ([su documentación](https://developer.spotify.com/documentation/web-api/reference/get-audio-features), según su resumen). Los DJs entrevistados por Marchiano y Tanco, en cambio, miden la energía por lo que ven en la pista. El número puede ayudar a etiquetar la [colección](../Seleccion/coleccion.md), pero no reemplaza mirar qué le pasa al público con el tema.

## Tres escalas de la energía

La energía cambia en tres escalas de tiempo, y cada una tiene su nota. La investigación sobre mezclas separa tres niveles parecidos: la transición, el tema que sigue y el flujo de toda la mezcla ([Williams y otros, TIME 2025](https://drops.dagstuhl.de/storage/00lipics/lipics-vol355-time2025/html/LIPIcs.TIME.2025.20/LIPIcs.TIME.2025.20.html), según su resumen).

1. Dentro de un tema: la carga y la descarga entre break, subida y regreso del bombo, y la tensión que junta un loop que no cambia.
2. Entre temas: cuánto sube o baja la energía en cada unión.
3. En toda la sesión: el arco, de la apertura al cierre, que se corrige mirando la pista.

Los DJs de Marchiano y Tanco piensan la sesión como una alternancia: "tampoco poner 5 temas que exploten todo porque se les va la energía... tienen que recargar la pila" (DJ 1).

## Cómo falla la energía

- Saturación: descarga tras descarga, sin lugar para recargar; es la advertencia del DJ 1 citado arriba.
- Meseta sin respiro: muchos temas seguidos en lo alto. Williams y otros señalan que, tras varios temas de tempo alto, un DJ puede bajar la energía "para dar un respiro" (según su resumen).
- Salto: un tema mucho más denso o intenso que el anterior. La guía del fabricante citada arriba advierte, sobre saltar de 5 a 7 en su escala: "It'll sound like a different DJ got on the decks" (según su resumen).
- Rumbo ciego: un plan que no cambia con la pista. El DJ 2 de Marchiano y Tanco lleva una base de temas elegidos y se aparta de ella según lo que ve; eso se desarrolla en [leer la pista](leer-la-pista.md).

## Qué hay adentro de Energía

- [Tensión y descarga](tension-y-descarga.md): break, subida y regreso del bombo, y lo que miden los estudios de respuesta corporal.
- [Repetición y variación](repeticion-y-variacion.md): el loop que junta tensión, la paciencia y los cambios mínimos, según Jeff Mills y Surgeon.
- [Arco del set](arco-del-set.md): apertura, pico y cierre; qué hay de convención y qué de evidencia, y los sets largos.
- [Leer la pista](leer-la-pista.md): qué señales da el público y cómo se traducen en la próxima decisión.
