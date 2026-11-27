# DJ (pinchar): verticales Energía y Selección. Informe de investigación

Fecha: 2026-11-27. Alcance: dos verticales (Energía, Selección) de la técnica fundamental de unir temas. Lectora: quien empieza o mezcla poco, hasta intermedio. Estética de ejemplos: techno hipnótico y percusivo (sello ARTS, Emmanuel), mezcla larga.

## Cómo leer las marcas

- Tipo: P = primaria (estudio, entrevista al practicante, texto del autor); S = secundaria (reseña, blog, manual de empresa).
- Puntajes 1-3: Aut(oridad) / Prof(undidad) / Ej(emplos) / Uni(cidad).
- Lectura: [L] completo, [M] metadatos/abstract, [S] resumen del buscador o de terceros.
- Advertencia de método: `WebFetch` devuelve un resumen hecho por un modelo chico, no el texto crudo. Por eso solo marco [L] lo que pude bajar y leer yo en texto (los PDF de Marchiano & Tanco y de Kell & Tzanetakis, leídos con `pdftotext`, parcialmente). Las citas literales de páginas web vienen de ese resumen: **verificar contra la fuente antes de citar en una nota**. Las citas del PDF de Marchiano & Tanco son literales del texto.
- Los libros (Butler, Thornton, Fikentscher, Brewster & Broughton) no se pudieron leer: solo [S].

## Hallazgo estructural: la división Energía / Selección

No coincide limpiamente con cómo el campo parte esto. Lo que encontré:

1. **El "set" (arco, lectura de pista, sets largos) es su propia parte, no un apéndice de Energía.** La literatura MIR separa tres niveles: transición, track (qué tema sigue) y mix (flujo de todo el set) (Williams et al., TIME 2025, https://drops.dagstuhl.de/storage/00lipics/lipics-vol355-time2025/html/LIPIcs.TIME.2025.20/LIPIcs.TIME.2025.20.html). "Unir dos temas" es el nivel 1; Selección es el nivel 2; el arco y la pista son el nivel 3. Mixed In Key también razona la energía como curva del set, no como atributo suelto. Propuesta: Energía queda como el atributo del tema y la teoría de tensión/descarga; el arco y leer la pista pasan a una parte "Set" (o "Construir el set").
2. **Energía es el criterio de selección más usado, así que las dos verticales se pisan.** Los DJs entrevistados por Marchiano & Tanco describen música y pista con la misma categoría ("nivel de energía") y arman el set con esa alternancia (ver C1). Etiquetar por energía es, a la vez, herramienta de selección (ver C2).
3. **Tool vs. pieza no es una categoría académica.** No encontré ninguna fuente que la defina; es vocabulario de práctica (ver hueco). Conviene tratarla como "función del tema en el set", que sí tiene respaldo en los manuales de etiquetado (Digital DJ Tips).

## Componente E1. Qué es la "energía" de un tema

### Fuentes

| Fuente | Tipo | Aut | Prof | Ej | Uni | Marca | URL |
|---|---|---|---|---|---|---|---|
| Marchiano & Tanco 2021, "El baile en la música del DJ", *El Oído Pensante* 9(2) | P | 2 | 2 | 3 | 3 | [L parcial: resumen y secciones de resultados] | https://www.redalyc.org/journal/5529/552969184005/552969184005.pdf |
| Mixed In Key, guía "Sorting playlists by energy level" | S (fabricante) | 1 | 2 | 2 | 2 | [M] | https://mixedinkey.com/harmonic-mixing-guide/sorting-playlists-by-energy-level/ |
| Spotify Web API, audio features ("energy", "danceability") | S (documentación comercial) | 1 | 1 | 1 | 2 | [M] | https://developer.spotify.com/documentation/web-api/reference/get-audio-features |
| arXiv 2302.13321, predicción de emoción musical con rasgos de alto nivel | P (preprint MER, no EDM) | 1 | 1 | 1 | 1 | [S] | https://arxiv.org/pdf/2302.13321 |
| Kell & Tzanetakis, ISMIR 2013 (timbre, tempo, sonoridad entre temas) | P | 2 | 2 | 2 | 3 | [M + introducción] | https://archives.ismir.net/ismir2013/paper/000210.pdf |

### Afirmaciones

- No hay una definición medible única y aceptada de "energía". Los DJs la usan como categoría de práctica: tres DJs de fiestas en La Plata describen tanto la intensidad del baile como la música con "nivel de energía", con dos polos, "arriba" y "abajo" (el extremo, "explosión"), y la intensidad del baile la perciben como efecto de la energía de la música ("estableciendo una relación causal entre ambos"). Fuente: Marchiano & Tanco, sección 2.2, https://www.redalyc.org/journal/5529/552969184005/552969184005.pdf. Es una muestra chica: 3 entrevistas semiestructuradas, noviembre-diciembre de 2019 (mismo PDF, sección Método).
- Mixed In Key la define como escala 1 a 10 ("The numbers go from 1 to 10"), dice que la inventó y la patentó, y da anclas: nivel 1 "no tiene beat", nivel 5 "es donde la gente empieza a bailar", nivel 7 "super high-energy", nivel 9 "the drop is so big that people run out of breath in 1-2 minutes". Fuente: https://mixedinkey.com/harmonic-mixing-guide/sorting-playlists-by-energy-level/. No publica el algoritmo: la búsqueda no lo encontró. Un artículo de DJ.Studio (secundario, [S]) dice que se basa en el contenido y no necesariamente en el tempo: https://help.dj.studio/en/articles/8119977-mixed-in-key-integration. Se dice que busca patrones de hi-hat y ruido blanco en build-ups, pero esa afirmación es de una fuente secundaria no verificada.
- Spotify definió "energy" como "a perceptual measure of intensity and activity" de 0.0 a 1.0, basada en rango dinámico y sonoridad percibida; "danceability" es otra cosa (tempo, estabilidad rítmica, fuerza del beat, regularidad). Fuente: https://developer.spotify.com/documentation/web-api/reference/get-audio-features. Nota mía sin verificar en esta ronda: tengo entendido que Spotify restringió ese endpoint a apps nuevas a fines de 2024; confirmar antes de citarlo como herramienta disponible.
- En MER (reconocimiento de emoción musical) general, "energy" de Spotify resulta el mejor predictor de arousal y capta sonoridad percibida; danceability tuvo coeficiente negativo para arousal, es decir, no es sinónimo de energía. Fuente: https://arxiv.org/pdf/2302.13321 [S, no es estudio de EDM].
- Insumos habituales de la energía percibida: sonoridad/RMS, tempo, timbre. Fuente: mismas búsquedas MER (https://arxiv.org/pdf/2212.13369); hay una advertencia de que "no hay consenso" sobre la relación rasgos-emoción. [S]
- En sets reales de EDM, el timbre aparece como un factor importante al elegir y ordenar temas (Kell & Tzanetakis: "Timbre appears to be an important factor when selecting tracks and ordering tracks", abstract). https://archives.ismir.net/ismir2013/paper/000210.pdf

Divergencia a registrar: la energía como número (Mixed In Key, Spotify) frente a la energía como categoría vivida por el DJ en relación con la pista (Marchiano & Tanco). Las dos conviven; la nota debería decir que el número es una ayuda para etiquetar, no una verdad.

### Recurso canónico

Marchiano & Tanco 2021 (gratis, español, CC BY-NC). Leer el resumen y la sección 2.2 ("Nivel de energía de la música y del baile"). Fijarse en: la energía como causa-efecto música→baile y la alternancia de momentos "de explosión y de calma". Complemento: la guía de Mixed In Key para tener una escala concreta (con la reserva de que es fabricante).

## Componente E2. Tensión y descarga (build-up, breakdown, drop)

### Fuentes

| Fuente | Tipo | Aut | Prof | Ej | Uni | Marca | URL |
|---|---|---|---|---|---|---|---|
| Solberg & Jensenius 2017, *Empirical Musicology Review* 11(3-4), 301-318 | P | 3 | 3 | 2 | 3 | [S] (buscador; DUO redirigió, core.ac.uk dio 403) | https://duo.uio.no/handle/10852/55312 |
| Solberg & Dibben 2019, "Peak experiences with electronic dance music...", *Music Perception* 36(4), 371-389, DOI 10.1525/mp.2019.36.4.371 | P | 3 | 3 | 2 | 3 | [M] | https://eprints.whiterose.ac.uk/145911/ |
| Butler 2006, *Unlocking the Groove* (Indiana UP) | P (libro) | 3 | 3 | 3 | 3 | [S] | https://search.worldcat.org/title/61162077 |
| Butler 2001, "Turning the Beat Around", *Music Theory Online* 7.6 | P | 3 | 2 | 2 | 2 | [S] | https://mtosmt.org/issues/mto.01.7.6/mto.01.7.6.butler.html |
| Marchiano & Tanco 2021 | P | 2 | 2 | 3 | 3 | [L parcial] | https://www.redalyc.org/journal/5529/552969184005/552969184005.pdf |

### Afirmaciones

- Solberg & Jensenius: 16 participantes bailaron a un mix de DJ en un entorno tipo club con captura de movimiento óptica, y respondieron cuestionarios; el movimiento del grupo cambió de forma marcada entre breakdown, build-up y drop; build-up y drop fueron lo más placentero y lo que más motivó a bailar; la presencia y la actividad de otros afectó la experiencia individual. Fuente (resumen del buscador, comentarios de Greasley y de Witek & Vuust incluidos): https://duo.uio.no/handle/10852/55312. Verificar números en el artículo.
- Los comentarios al estudio señalan que los temas con breakdown/build-up/drop produjeron mayores cambios de movimiento y placer que los de dinámica plana, y que falta control en el diseño (Witek & Vuust). Misma fuente, [S].
- Solberg & Dibben 2019: 24 oyentes sin bailar; extractos con "break routine" (breakdown, build-up, drop) y uno sin; mediciones de conductancia de piel, afecto autoinformado y vivencia corporal; el drop tuvo respuesta de conductancia significativamente mayor que las otras partes de la rutina; hubo afecto intenso también fuera del club. Fuente: https://eprints.whiterose.ac.uk/145911/ [M].
- Los DJs describen sus temas como alternancia entre "cargando" y "liberan": "Como uno es donde la gente está esperando, cargando... y en el otro es donde… liberan" (DJ 3), y "tampoco poner 5 temas que exploten todo porque se les va la energía... tienen que recargar la pila" (DJ 1). Fuente (texto leído): Marchiano & Tanco, https://www.redalyc.org/journal/5529/552969184005/552969184005.pdf.
- Butler: el libro cubre la organización rítmica de la EDM "desde el compás hasta el set completo de DJ"; la tabla de contenidos incluye un capítulo sobre las funciones de procesos continuos y la estética de las secciones de breakdown y build-up. Fuente: https://search.worldcat.org/title/61162077 y reseñas (https://wayneandwax.com/academic/mts-butler-unlocking-groove.pdf) [S]. No leí el capítulo: no puedo citar su argumento.

### Recurso canónico

Solberg & Jensenius 2017 (acceso abierto, EMR). Leer: método y la figura/resultados de movimiento por sección. Fijarse en que mide una mezcla de DJ real y en el control de dinámica plana. Para la teoría del "por qué", Butler 2006, capítulo sobre breakdown/build-up (hay que conseguir el libro; no lo leí).

Aviso para el caso ARTS: ambos estudios son de EDM con estructura de drop (más cercana a house/EDM de festival). El techno hipnótico minimal tiene poco breakdown/drop; Butler lo describe por capas y repetición. No hay estudio que mida la tensión en ese tipo de techno (ver huecos).

## Componente E3. Tensión hipnótica: repetición y variación mínima

### Fuentes

| Fuente | Tipo | Aut | Prof | Ej | Uni | Marca | URL |
|---|---|---|---|---|---|---|---|
| Jeff Mills, lectura RBMA (5 abr 1998, primera de la serie) | P (practicante) | 3 | 2 | 3 | 3 | [L por resumen de la página; transcripción completa según el resumen] | https://www.redbullmusicacademy.com/lectures/jeff-mills-lecture |
| Surgeon (Anthony Child), entrevista Ableton, 12 ago 2014 | P (practicante) | 3 | 2 | 3 | 3 | [M] | https://ableton.com/en/blog/surgeon-plugging-moment |
| Rietveld, "Machine Possession: Dancing to Repetitive Beats" (cap., manuscrito 2017) | P | 2 | 2 | 1 | 3 | [S] (descarga falló por certificado) | https://openresearch.lsbu.ac.uk/download/cc22adab77ea67b097c59ac741e3bcc76a2df6238aff27877c6810691013dd3e/217487/RIETVELD-Machine%20Possession%20-%20Accepted%202017.pdf |
| Butler 2006 (capas, loops) | P | 3 | 3 | 3 | 3 | [S] | https://search.worldcat.org/title/61162077 |

### Afirmaciones

- Mills: dejar correr un loop produce tensión; estima que tras unos "two-and-a-half to three minutes" de música sin cambios "someone's going to scream"; y dice de algunos temas "it enhances the more you hear it, the better it gets". Fuente: https://www.redbullmusicacademy.com/lectures/jeff-mills-lecture (citas vía resumen; verificar).
- Mills también dice que usa "breakdowns and silence" y "pockets" para dejar respirar a la gente en un club caliente (misma fuente). Útil como contrapeso: la tensión hipnótica convive con pausas diseñadas.
- Surgeon: sostenía las intros "as long as he felt necessary" para meter una capa extra de tensión; en House of God estiraba intros con dos copias del mismo disco; "knowing when to just let a track play is just as important" como alterarlo. Fuente: https://ableton.com/en/blog/surgeon-plugging-moment (resumen; verificar citas).
- Rietveld (según resumen del buscador): bailar techno a 130 bpm o más durante horas puede producir un trance impulsado por la máquina; menciona un "presente duradero" por sesiones largas y repetitivas y el "peaking" de la pista, apoyándose en Rouget. [S] https://openresearch.lsbu.ac.uk/download/cc22adab77ea67b097c59ac741e3bcc76a2df6238aff27877c6810691013dd3e/217487/RIETVELD-Machine%20Possession%20-%20Accepted%202017.pdf
- Butler contrasta el uso de "una secuencia repetida con partes silenciadas" con sucesiones de secuencias por capas (cita de la p. 207 de un tercero, [S] https://charlotterew.dgah.sites.carleton.edu/wp-content/uploads/2021/05/EDM-piece-statement.pdf; confirmar en el libro).
- No encontré texto de Mills "sobre repetición" más allá de la lectura RBMA, ni fuente de Emmanuel sobre su enfoque (ver huecos).

### Recurso canónico

La lectura de Jeff Mills en RBMA (transcripción). Fijarse en: el tiempo de loop de 2,5 a 3 minutos como umbral de tensión, y el "no pongas un disco con un solo buen tema". Para el marco académico, Butler 2006 (capas) y Rietveld (repetición y trance), ambos por conseguir.

## Componente E4. El arco del set y leer la pista

### Fuentes

| Fuente | Tipo | Aut | Prof | Ej | Uni | Marca | URL |
|---|---|---|---|---|---|---|---|
| Marchiano & Tanco 2021 | P | 2 | 2 | 3 | 3 | [L parcial] | https://www.redalyc.org/journal/5529/552969184005/552969184005.pdf |
| Gates, Subramanian & Gutwin, "DJs' perspectives on interaction and awareness in nightclubs", DIS 2006, pp. 70-79 | P | 2 | 2 | 2 | 2 | [S] | https://www.springerprofessional.de/doi/10.1145/1142405.1142418 |
| Williams, Meehan, Lattner, Pauwels, Barthet, "Temporal Considerations in DJ Mix Information Retrieval and Generation", TIME 2025 | P | 2 | 2 | 1 | 3 | [M] | https://drops.dagstuhl.de/storage/00lipics/lipics-vol355-time2025/html/LIPIcs.TIME.2025.20/LIPIcs.TIME.2025.20.html |
| Mixed In Key, guía de energía | S | 1 | 2 | 2 | 2 | [M] | https://mixedinkey.com/harmonic-mixing-guide/sorting-playlists-by-energy-level/ |
| Mills, RBMA 1998 | P | 3 | 2 | 3 | 3 | [L por resumen] | https://www.redbullmusicacademy.com/lectures/jeff-mills-lecture |
| Thornton 1995, *Club Cultures* | P (libro) | 3 | 3 | 2 | 2 | [S] | https://www.readings.com.au/product/9780745614434/9780745614434 |
| Fikentscher 2000, *"You Better Work!"* | P (libro) | 3 | 3 | 2 | 3 | [S] | https://fulcrum.org/concern/monographs/js956j59s |

### Afirmaciones

- Leer la pista: los DJs perciben a la pista como una unidad y la juzgan "arriba" o "abajo" por la intensidad del movimiento, no por individuos; "el set musical que el DJ arma durante la fiesta se define por estas atribuciones y se orienta a mantener al público arriba". Fuente (resumen leído): Marchiano & Tanco, https://www.redalyc.org/journal/5529/552969184005/552969184005.pdf.
- Señales de que un tema no funcionó, en palabras de un DJ: "cara aburrida, o mira para otro lado, o ya sacan el celu... se empiezan a ir, o se quedan parados" (DJ 2). Misma fuente.
- Planificación vs. improvisación: un DJ lleva "una base de 10 a 15" temas elegidos y 400-500 en el pendrive, y se aparta de esa base según lo que ve (DJ 2). Misma fuente. Es el único dato empírico que encontré de cuánto se planifica.
- Gates et al.: entrevistas a 11 DJs de varias ciudades; recopilan información sobre la pista para planificar y dar forma a la música de la noche, la leen visualmente incluso con poca luz mientras cargan con selección y mezcla, y desconfían de tecnología que dé más control a la pista. [S] https://www.springerprofessional.de/doi/10.1145/1142405.1142418
- Mills: lee la sala en unos 15 minutos ("read the crowd within 15 minutes"), "constantly watch the crowd", y planifica según composición de la sala (hombres/mujeres, edades). Fuente: https://www.redbullmusicacademy.com/lectures/jeff-mills-lecture (verificar citas).
- Curva de energía (receta comercial, no estudio): empezar en nivel 5, subir a 6 al llegar gente, 7 con la pista calentada, reservar 8+ para el headliner, moverse de a un nivel ("jumping from 5 to 7... It'll sound like a different DJ got on the decks"). Fuente: https://mixedinkey.com/harmonic-mixing-guide/sorting-playlists-by-energy-level/. Está pensada para EDM y open format; no para mezcla larga de techno hipnótico. Marcarla como práctica de fabricante.
- El nivel "mix" (el arco) casi no está estudiado en MIR: el paper de TIME 2025 dice que ningún sistema opera inteligentemente en los tres niveles, que tras varios temas de tempo alto un DJ puede bajar energía "para dar un respiro" y que no existe un corpus público de mixes con audio y etiquetas para entrenar objetivos de largo plazo. https://drops.dagstuhl.de/storage/00lipics/lipics-vol355-time2025/html/LIPIcs.TIME.2025.20/LIPIcs.TIME.2025.20.html [M].
- Thornton y Fikentscher: marco sociológico/etnográfico (capital subcultural; relación música-baile en clubes underground de Nueva York, el DJ como figura y el vinilo como instrumento). Solo descripciones de editorial; no pude verificar pasajes sobre lectura de pista. [S]

### Recurso canónico

Marchiano & Tanco 2021: el único texto abierto y reciente que describe cómo el DJ lee la pista y deriva de ahí el set. Leer: sección 2 (resultados) y 3-4 (acción musical). Fijarse en la tríada leer pista → cambio de estado del DJ → acción musical, y en el cuadro de "base de 10-15 temas". Para el arco, no hay un recurso canónico: ver huecos.

## Componente S1. Criterio de elegibilidad y coherencia/contraste en la secuencia

### Fuentes

| Fuente | Tipo | Aut | Prof | Ej | Uni | Marca | URL |
|---|---|---|---|---|---|---|---|
| Kell & Tzanetakis, "Empirical analysis of track selection and ordering in electronic dance music using audio feature extraction", ISMIR 2013 | P | 2 | 2 | 2 | 3 | [M + introducción leída] | https://archives.ismir.net/ismir2013/paper/000210.pdf |
| Kim, Choi, Sacks, Yang, Nam, ISMIR 2020, "A Computational Analysis of Real-World DJ Mixes using Mix-To-Track Subsequence Alignment", arXiv 2008.10267 | P | 2 | 2 | 1 | 3 | [M] | https://arxiv.org/abs/2008.10267v1 |
| Vande Veire & De Bie 2018, *EURASIP J. Audio Speech Music Process.* (DJ automático de drum and bass) | P | 2 | 2 | 1 | 2 | [S] | https://link.springer.com/article/10.1186/s13636-018-0134-8 |
| Williams et al., TIME 2025 | P | 2 | 2 | 1 | 3 | [M] | https://drops.dagstuhl.de/storage/00lipics/lipics-vol355-time2025/html/LIPIcs.TIME.2025.20/LIPIcs.TIME.2025.20.html |
| Mills, RBMA 1998 | P | 3 | 2 | 3 | 3 | [L por resumen] | https://www.redbullmusicacademy.com/lectures/jeff-mills-lecture |

### Afirmaciones

- Datos: 1,557 mixes de 1001Tracklists, 13,728 temas únicos, 20,765 transiciones; el método alinea cada mix con sus temas originales para recuperar puntos de cue, largo de transición y segmentación. Fuente: https://arxiv.org/abs/2008.10267v1 [M]. El abstract no da cifras de cuánto duran las transiciones ni dónde caen los cues; habría que leer el paper completo.
- Kell & Tzanetakis analizaron sets del programa Essential Mix de la BBC (1 o 2 horas cada uno): "track order itself matters", con diferencias estadísticamente significativas entre el orden original y una versión mezclada al azar; y sugieren que el modelo de playlist "por similitud decreciente al primer tema" quizá no sea óptimo para EDM. Fuente: https://archives.ismir.net/ismir2013/paper/000210.pdf (abstract y intro leídos en texto).
- Los mismos autores citan que a muchos DJs "two tracks 'work' or 'do not work' together" y no saben decir más: el criterio es en buena parte tácito. Misma fuente, introducción.
- Un DJ de fiestas (Argentina) lleva 10-15 temas base de 400-500 y se desvía según la pista (Marchiano & Tanco): la selección es un proceso en vivo, no solo previo.
- Mills elige discos por tener "at least two" buenos temas (para tocar cada uno más de una vez) y rota su caja: "very rarely do I ever play a record that only has one good track". Fuente: https://www.redbullmusicacademy.com/lectures/jeff-mills-lecture (resumen; verificar). También toca "the best part of it, and then move on to the next one", es decir, usa secciones de los discos como herramientas.
- Sistemas automáticos usan compatibilidad por clave (Camelot), tempo (±2 BPM) y energía sin saltos grandes (DJ-AI 2025, https://research.sabanciuniv.edu/52373/1/AI_DJ_AM2025.pdf [S]); el de Vande Veire & De Bie coloca los temas en un "espacio de estilo" continuo y 18 fans de drum and bass calificaron sus mixes de alta calidad. https://link.springer.com/article/10.1186/s13636-018-0134-8 [S]. Son reglas de ingeniería, no evidencia de qué hace elegible un tema para un DJ humano.

### Recurso canónico

Kell & Tzanetakis 2013. Leer: abstract, secciones de análisis de transiciones y de heurísticas de ordenamiento. Fijarse en que mide timbre, tempo, clave y sonoridad entre temas consecutivos de sets reales y que el orden importa. Complemento corto: Mills (RBMA) para el criterio de practicante.

## Componente S2. Función del tema: herramienta vs. pieza; colección como vocabulario; etiquetar

### Fuentes

| Fuente | Tipo | Aut | Prof | Ej | Uni | Marca | URL |
|---|---|---|---|---|---|---|---|
| Digital DJ Tips, Phil Morse, "Beyond Genre: 5 Tagging Tricks For Better DJ Sets" (act. 27 mar 2018) | S | 1 | 1 | 2 | 2 | [M] | https://www.digitaldjtips.com/2016/02/beyond-genre-5-tagging-tricks-better-dj-sets/ |
| VirtualDJ, "How to Organize DJ Playlists That Work" y "Music catalog for DJs" | S (fabricante) | 1 | 1 | 1 | 1 | [S] | https://virtualdj.com/articles/how-to-organize-dj-playlists |
| Butler 2014, *Playing with Something That Runs* (OUP), capítulo "Creating the 'Third Record'" | P | 3 | 3 | 3 | 3 | [S] | https://academic.oup.com/book/10424/chapter/158245998 |
| Mills, RBMA 1998 | P | 3 | 2 | 3 | 3 | [L por resumen] | https://www.redbullmusicacademy.com/lectures/jeff-mills-lecture |
| Surgeon, Ableton 2014 | P | 3 | 2 | 3 | 3 | [M] | https://ableton.com/en/blog/surgeon-plugging-moment |

### Afirmaciones

- Qué etiquetar según Digital DJ Tips: energía (estrellas de calentamiento a pico), función y escenario (apertura, cierre, relleno, club vs. lounge), rasgos musicales (tipo de voz, instrumentos, cambios de tempo) y pares de temas que mezclan bien (comentario "MWW"). Fuente: https://www.digitaldjtips.com/2016/02/beyond-genre-5-tagging-tricks-better-dj-sets/. No usa "mood" como término.
- VirtualDJ propone clasificar por efecto en la sala (abrir, construir, pico, enfriar) y aclara que la energía no es el BPM; una encuesta de DJ TechTools citada por un resumen dice que lo más común es un sistema propio de color por mood/energía/vibe. [S] https://virtualdj.com/articles/how-to-organize-dj-playlists, https://djtechtools.com/amp/tag/color/
- Butler 2014 trata las performances de DJ como actos de composición en tiempo real a partir de discos previos; un capítulo se titula "Creating the 'Third Record': Works and Texts in DJ Performances" (basado en etnografía en Berlín). Solo tabla de contenidos [S]: no sé qué dice del criterio de selección; es la pista más fuerte para "pieza vs. herramienta" desde la academia. https://academic.oup.com/book/10424/chapter/158245998
- Conocer la música: Surgeon, "I have to know the music I'm playing really well"; marca cues con warp markers. Fuente: https://ableton.com/en/blog/surgeon-plugging-moment (resumen; verificar). Mills: rota su caja y repite discos "twice, three times a night" para que una colección chica rinda. https://www.redbullmusicacademy.com/lectures/jeff-mills-lecture
- Tamaño de la colección: el único dato duro es de Marchiano & Tanco (10-15 base, 400-500 disponibles); no encontré normas ni estudios sobre "cuántos temas hacen falta".

### Recurso canónico

Para etiquetar: Digital DJ Tips, "Beyond Genre" (corto, práctico; secundaria). Para pensar el tema como material de una obra mayor: Butler 2014, capítulo "Third Record" (conseguir). No hay recurso canónico verificado para "herramienta vs. pieza".

## Componente S3. Digging, preparación y peso de selección vs. técnica

### Fuentes

| Fuente | Tipo | Aut | Prof | Ej | Uni | Marca | URL |
|---|---|---|---|---|---|---|---|
| Brewster & Broughton, *How to DJ Right* (2003; ed. 2.ª 2025/Open Road) | P (libro) | 3 | 3 | 3 | 3 | [S] | https://openroadmedia.com/ebook/how-to-dj-right/9780802199744 |
| Dave Segal, "Beatseeking Missives", *The Stranger*, 11 sep 2003 | S (entrevista/nota) | 2 | 1 | 2 | 2 | [M] | https://www.thestranger.com/?p=26400 |
| The Secret DJ, Mixmag, 12 oct 2017 | S (columna anónima) | 1 | 1 | 2 | 2 | [M] | https://mixmag.net/feature/the-secret-dj-a-proper-dj-selects-well-and-mixes-well |
| DJ TechTools, "How I dig: a DJ's guide to digital crate digging" (24 feb 2023) | S | 1 | 1 | 2 | 1 | [S] | https://djtechtools.com/2023/02/24/how-i-dig-a-djs-guide-to-digital-crate-digging |
| Surgeon, Ableton 2014 | P | 3 | 2 | 3 | 3 | [M] | https://ableton.com/en/blog/surgeon-plugging-moment |
| Mills, RBMA 1998 | P | 3 | 2 | 3 | 3 | [L por resumen] | https://www.redbullmusicacademy.com/lectures/jeff-mills-lecture |

### Afirmaciones

- Selección sobre técnica (Brewster & Broughton, vía entrevista de 2003): según el resumen de la nota, Broughton dice "loving music and having great records is far more important than smooth beatmatching" y "If your tunes are dull, the most flawless mixing won't save you". Fuente: https://www.thestranger.com/?p=26400. **No leí el libro ni verifiqué la cita literal; el resumen de la nota es lo único que tengo.** Brewster, en una entrevista de 2016 (Track Hunter), dice que los medios se fijaban sobre todo en la mezcla: https://www.trackhunter.co.uk/Blog/Interview-with-Bill-Brewster-Part-One [S].
- Discrepancia a dar: Mixmag (2017) responde que "A proper DJ selects well and mixes well" y que polarizar "es ridículo", dirigido contra artículos que dicen que mezclar no importa. https://mixmag.net/feature/the-secret-dj-a-proper-dj-selects-well-and-mixes-well. Es columna anónima: opinión, no evidencia.
- Digging: DJ TechTools describe Bandcamp como lugar de música independiente que no sale en otro lado, con búsqueda "alright, but not the best"; recomienda seguir a los sellos y sus listas de correo (muchos mandan promos gratis); otros DJs combinan Discogs, Juno, Deejay.de y Beatport. https://djtechtools.com/2023/02/24/how-i-dig-a-djs-guide-to-digital-crate-digging [S]. Los listados de tracklists (1001Tracklists) son fuente de datos en investigación (Kim et al.) pero no encontré una fuente que los documente como método de digging.
- Preparación: Surgeon marca cues y conoce cada tema; Mills elige en función de poder tocar dos buenos temas de cada disco. No encontré manual verificado sobre escuchar el tema entero, marcar cues y anotar (más allá de que Kim et al. 2020 estudia automáticamente dónde los DJs ponen cues: https://arxiv.org/pdf/2007.08411 [S]).

### Recurso canónico

Brewster & Broughton, *How to DJ Right*, capítulos sobre selección/armado del set (conseguir el libro; no pude leerlo). Contrapeso útil: la columna de Mixmag (corta). Para digging, no hay recurso canónico verificado; la guía de DJ TechTools sirve como ejemplo de herramientas, no como fuente de criterio.

## Huecos declarados

1. **Libros no leídos**: Butler 2006 y 2014, Thornton 1995, Fikentscher 2000, Brewster & Broughton. Todo lo que figura de ellos viene de fichas de editorial, reseñas o resúmenes de buscador. Hay que conseguirlos (Fulcrum tiene Fikentscher con login institucional) y leer los capítulos nombrados antes de citar argumentos.
2. **Solberg & Jensenius 2017**: solo resumen del buscador (el repositorio redirigió y core.ac.uk dio 403). Faltan cifras exactas y la cita literal del abstract.
3. **Definición medible de energía**: no hay estudio MIR/musicología que defina "energía de baile" en EDM. Mixed In Key no publica el algoritmo (menciona una patente sin número); Spotify es solo documentación. Hueco: un paper sobre energía percibida en EDM.
4. **Techno hipnótico**: ningún estudio mide tensión/trance en techno minimal con repetición y variación mínima; Rietveld y Butler son los candidatos, no leídos. Sin fuente directa de Jeff Mills sobre "hipnosis" fuera de la lectura de 1998.
5. **Emmanuel/ARTS**: no encontré entrevista larga en RA, Attack, Mixmag ni RBMA sobre su enfoque de selección o de sets. Para ejemplos de estética solo hay la ficha de RA (https://ra.co/dj/emmanuel) y una reseña de su EP de 2023 (https://dirty-epic.com/?p=6570); nada citable sobre método.
6. **Practicantes pedidos sin resultado**: no hallé lecturas RBMA de Surgeon ni de Function sobre DJing; de Ben Sims solo notas breves (XLR8R, VICE) sin material de arco ni de sets largos. Ø [Phase] no se buscó por el límite de rondas.
7. **Sets largos (4-8 horas)**: ninguna fuente sobre cómo se construyen ni sobre curvas de energía de sets largos. La receta de Mixed In Key es para sets cortos y EDM.
8. **Tool vs. pieza**: sin fuente que defina el término; es vocabulario de práctica. Hueco abierto.
9. **Qué hace elegible un tema**: solo datos indirectos (Kell & Tzanetakis; Mills). No hay un estudio de calidad de producción o groove como criterio.
10. **Selección vs. técnica**: la cita clásica aparece solo vía una nota de 2003 y sin verificar la frase en el libro; la RA no se consultó (no se hizo una ronda para entrevistas RA sobre este punto).
11. **Preparación de temas**: sin manual verificado de escuchar entero/marcar cues/anotar; solo Surgeon y estudios automáticos de cue points (Kim et al., arXiv 2007.08411, no leído).
12. **Gates et al. 2006, Marchiano & Tanco**: Gates solo [S]. Marchiano & Tanco es una muestra de 3 DJs de escena local en La Plata (nov-dic 2019), de una escena no techno-hipnótica: generalizar con cautela.
13. **Kim et al. 2020**: solo abstract; no sé qué estadísticas concretas reporta (duración de transiciones, posición de cues).
14. **Verificar vigencia**: el endpoint de audio features de Spotify (restricciones desde fines de 2024, de memoria) y la versión/año de la edición actual de *How to DJ Right*.
