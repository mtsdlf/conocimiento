# Investigación: DJ — verticales Tiempo y Forma

Fecha de la investigación: 2026-11-27. Lectora: principiante a intermedio. Estética de ejemplos: techno hipnótico y percusivo (sello ARTS), mezcla larga.

Leyenda de marcas: **[L]** leído completo (o la parte relevante, vía texto extraído); **[M]** metadatos/abstract; **[S]** resumen secundario o del buscador. Puntajes 1-3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U). Tipo: **P** primaria (paper, manual oficial, libro), **S** secundaria (practicante o divulgación).

Convención: lo que es aritmética mía, sin fuente, está marcado "cálculo propio". Todo lo de la web se trató como dato.

## 0. ¿La división Tiempo / Forma coincide con la del campo?

Coincide en lo grueso y se solapa en un punto concreto.

- La música-teoría de EDM separa **pulso/compás (meter)** de **forma/diseño musical**: Butler titula su libro "Rhythm, Meter, and Musical Design in Electronic Dance Music" (https://search.worldcat.org/title/61162077 [S]) y dice que explora la organización rítmica "desde el compás hasta el set completo" (resumen del buscador, https://omnia.sas.upenn.edu/node/2043 [S]). Eso es Tiempo y Forma en ese orden.
- Los manuales de software, en cambio, parten por función: **beatgrid y sync** (Tiempo) por un lado, **cue points, phrase y estructura** (Forma) por otro (Mixxx https://manual.mixxx.org/2.4/chapters/djing_with_mixxx [L]; rekordbox, ver 2.4).
- **Solapamiento:** el *downbeat* (el "1" del compás) es la frontera. El beatgrid de una máquina es una grilla de pulsos con un "1" marcado; rekordbox marca "the first beat of bar" en rojo cada 4 beats (manual 7.1.4, https://cdn.rekordbox.com/files/20250718115648/rekordbox7.1.4_manual_EN.pdf [L parcial, texto extraído con pdftotext]). Si el "1" está mal puesto, la fase puede coincidir y la mezcla igual cae fuera de compás. Ahí Tiempo (fase) y Forma (compás) no se separan.
- **Falta en tu partición** (otras verticales, no mías): armonía/clave (los papers y manuales la tratan junto al tempo porque key lock la toca) y energía/EQ. Dejo key lock en Tiempo porque es efecto del cambio de tempo.

## 1. TIEMPO

### 1.1 Tabla de fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| T1 | Mixxx manual 2.4, cap. "DJing With Mixxx" (beatmatching, Sync Lock, quantize, keylock, tempo dinámico) | https://manual.mixxx.org/2.4/chapters/djing_with_mixxx | P (manual oficial, abierto) | 3/2/2/2 | [L] |
| T2 | rekordbox 7.1.4 manual EN (beat grid, Master Tempo, Tempo Range, Analysis Lock) | https://cdn.rekordbox.com/files/20250718115648/rekordbox7.1.4_manual_EN.pdf | P (manual oficial) | 3/2/1/2 | [L] parcial (secciones buscadas) |
| T3 | Kim, Choi, Sacks, Yang, Nam (2020), ISMIR, pp. 764-770 (arXiv 2008.10267) | https://arxiv.org/abs/2008.10267 ; HTML: https://ar5iv.labs.arxiv.org/html/2008.10267 | P (paper, MIR) | 3/3/2/3 | [L] (vía HTML ar5iv; el PDF no era legible) |
| T4 | Chris Cartledge, "How To Earn Your DJ Stripes, Part 3: Learn To Beatmatch", Digital DJ Tips (act. 27-mar-2018) | https://www.digitaldjtips.com/learn-to-beatmatch/ | S (practicante) | 2/2/3/2 | [L] |
| T5 | Phil Morse, "Beginners' Guide To Keylocking", Digital DJ Tips (act. 28-mar-2018) | https://www.digitaldjtips.com/keylocking-dj-beginners/ | S (practicante) | 2/2/2/2 | [L] |
| T6 | DJ Vintage, "Is Sync Really So Different To Beatmatching?", Digital DJ Tips (act. 5-abr-2018) | https://www.digitaldjtips.com/your-questions-is-sync-really-so-different-to-beatmatching/ | S (practicante) | 2/2/2/2 | [L] |
| T7 | Yemi Abiade, "Should DJs be using the sync button?", Mixcloud blog (25-mar-2026) | https://www.mixcloud.com/blog/2026/03/25/should-djs-be-using-the-sync-button | S (editorial) | 1/1/1/2 | [L] |
| T8 | Foros de usuarios (Pioneer community, Serato, Engine DJ, Algoriddim) sobre redondeo de BPM y deriva | https://community.pioneerdj.com/hc/en-us/community/posts/22980186469401/comments/22986132815257 ; https://community.enginedj.com/t/rounding-off-bpm/25949 | S (foros, no verificado) | 1/1/1/1 | [S] |
| T9 | DJ TechTools, comparación de keylock (2014) y foros NI/Serato/VirtualDJ sobre artefactos | https://djtechtools.com/2014/03/16/keylock-in-dj-softwares-compared-serato-dj-traktor-pro-virtual-dj/ | S | 2/2/1/2 | [S] |
| T10 | Pioneer community, ejemplo de % de pitch vs BPM | https://community.pioneerdj.com/hc/en-us/community/posts/22976661955097/comments/22982249986329 | S (foro) | 1/1/2/1 | [S] |

No encontré **ningún estudio académico** sobre beatmatching a oído ni sobre percepción de deriva entre dos kicks. Ver huecos.

### 1.2 Afirmaciones

**Definición y mecánica**
- Beatmatching = ajustar la velocidad de reproducción de un tema para igualar el tempo de otro, y además la **fase** de los beats: "Beatmatching is the process of adjusting the playback rate of a track so that it matches the tempo of another track" (https://manual.mixxx.org/2.4/chapters/djing_with_mixxx [L]).
- Dos pasos distintos: tempo con los sliders de velocidad; fase empujando/frenando momentáneamente (botones de pitch bend o arrastrar la onda). La deriva se oye como un bombo "doblado" (flam) (T1 [L]).
- Rutina de corrección en dos pasos y en este orden: primero nudge (jog/pitch bend) para alinear, después ajuste de tempo para que no vuelva a derivar. Cartledge: "Always remember that when adjusting you always need to make these two steps, and in that order" (T4 [L]). Es el consejo práctico más útil de la fuente porque separa lo que el principiante mezcla en un solo gesto.
- La deriva "se nota sutil al principio y crece cada compás" (T4 [L], paráfrasis). La música electrónica 4/4 es la más fácil de igualar; la banda en vivo deriva y "swings" (T4 [L]).

**Pitch % a BPM**
- El cambio es **proporcional**, no un paso fijo: el mismo 6% da 84,8 BPM sobre 80 y 137,8 sobre 130 (T10 [S]; coincide con foro DJTT, https://forum.djtechtools.com/t/tip-for-people-mixing-in-the-120-130-bpm-range/55493 [S]).
- Cálculo propio: BPM_final = BPM × (1 + %/100). 128 BPM a +6% = 135,68; a +8% = 138,24; a −4% = 122,88. La diferencia de 128 a 126 es 1,56%.
- La resolución del control es otra cosa: rekordbox cambia la velocidad "0.02% at ±6 / 0.04% at ±10 and ±16 / 0.5% at WIDE" por paso (T2 [L]). Esos son pasos de la perilla/rango, no de precisión absoluta: rango más corto = más fino.

**Deriva: por qué aparece**
- Redondeo y resolución: según usuarios, un deck puede estar en 120,1 y otro en 120,19, ambos mostrados como 120,1 (T8 [S]); el control de pitch puede tener dos decimales y la pantalla BPM uno (T8 [S]). Afirmación de foro, sin fuente oficial.
- Cálculo propio: a 128,00 vs 127,98 BPM cada beat difiere ~73 µs (0,46875 s vs 0,46882 s); en 512 beats (unos 4 min) se acumulan ~37 ms, audible como flam. Una diferencia de 0,5 BPM desfasa un beat entero cada ~2 minutos. Para una mezcla larga de techno, esto es lo que hace que haya que retocar cada tanto aunque el sync esté.
- Tempo no exacto del tema: el BPM "detectado" casi nunca es el BPM "de producción". Mixxx sugiere: "if the detected BPM value is not sufficiently accurate but very close to an integer value, try to set the BPM value manually to the integer" (https://manual.mixxx.org/2.5/ro/chapters/preferences/beat_detection [S, vía buscador]).
- Tracks con tempo variable (vinilos viejos, grabaciones en vivo): no encajan en una grilla constante (T7 [L]: "Tracks can drift"). Mixxx ≥2.4 sigue el tempo del líder "unconditionally": un seguidor "changes its tempo matching the leader which may result in a notable pitch change"; keylock lo reduce (T1 [L]).

**Oído contra máquina: qué hace el sync y cuándo falla**
- Mixxx: el Sync Lock "usually only makes sure the rate sliders are set correctly"; para fase hay que activar Quantize: "Quantize will ensure that the beats are perfectly lined up as well" (T1 [L]). O sea: **sync de tempo y sync de fase son cosas distintas** y varían según el software.
- Sync depende del análisis: "requires an accurately detected BPM value and a correct beat grid for both tracks" (T1 [L]). El análisis suele fallar en ubicar el primer beat, no el BPM; se puede estirar, comprimir y mover la grilla (T1 [L]; rekordbox "Adjust the beat grid", T2 [L]).
- rekordbox advierte que **re-analizar sobrescribe** la grilla corregida a mano y ofrece **Analysis Lock** para evitarlo (T2 [L]).
- Sync reconoce doble/mitad de tempo (140 con 70) (T1 [L]), útil con percusión a media velocidad.
- Cifra discutible: DJ Vintage afirma que el software acierta "between 65% and 80% accurate beatgrids" y que Traktor y rekordbox son pobres con BPM variable (T6 [L]). Sin metodología citada; tomarlo como opinión de practicante.
- **Debate:** a favor: libera atención para selección, capas y efectos y baja la barrera de entrada para atender frases y energía primero (T7 [L]); "like a carpenter... electric drill" (T6 [L]). En contra: sobreuso "can also limit your development and connection to the music" (T7 [L]); el DJ que solo sabe sync tiene problemas cuando falla o no existe (CDJ sin sync, USB, laptop ajena) (T6, T7 [L]). Las dos fuentes de practicantes convergen en: aprender a oído y usar sync después como herramienta. Es consenso de blogs, no hay estudio.
- Matiz que aparece en ambas y suele omitirse: sync no resuelve **qué frase** coincide con cuál (T6 no habla de frases [L]); eso es Forma.

**Key lock / master tempo**
- Definición: "When it is active changing the speed of a track won't affect the key" (T1 [L]). rekordbox lo llama Master Tempo ("MT"): "The pitch of the track does not change even when you change the playback speed" (T2 [L]).
- Sin key lock, cambiar el tempo cambia el tono: "Every 6% change in a track's tempo shifts its key by about one semitone" (T5 [L]). Cálculo propio: 2^(1/12) = 1,0595, o sea 5,95%. Con rekordbox sin Master Tempo, la tonalidad mostrada cambia si cambia el BPM por Beat Sync (T2 [L]).
- Costo en calidad: "can degrade the sound quality", más cuanto más lejos del tempo original y con material complejo; Morse recomienda quedarse en "no more than + or – 6%" (T5 [L]). Reportes de usuarios: en techno/minimal los artefactos metálicos y los transientes de bombo/agudos se embarran (T9 [S], foros NI/Serato; no verificable). DJTT 2014 menciona cortes y artefactos sobre todo fuera de ~5% del BPM original (T9 [S]).
- Datos de uso real (T3 [L]): solo **2,5%** de los 24.202 temas pasados en las mezclas analizadas estaban transpuestos, y de esos **94,3%** un semitono; los autores infieren que los DJ dejan "master tempo" encendido. Es dato sobre House/Trance, ver T3 más abajo.
- Para el ejemplo de techno: en una mezcla larga, por un tiempo se tocan dos bombos casi juntos; un artefacto de time-stretch en el bombo que se oye solo se nota. Esto es inferencia mía, no fuente.

**Cuánto tempo se mueve en la práctica (T3 [L])**
- Con 20.765 transiciones y 1.557 mezclas (promedio 60,5 min): **86,1%** de los temas con cambio de tempo menor a 5%, **94,5%** menor a 10%, **98,6%** menor a 20%.
- Los pares de tempos que se mezclan son, en su mayoría, cercanos: el pitch % grande es excepcional. Sirve para fijar "rango normal" en la nota.

**Cómo se practica a oído (practicantes, T4 [L]; ver también https://virtualdj.com/articles/how-to-beatmatch-by-ear [S])**
1. Dos temas conocidos de BPM cercano, 4/4. 2. Cue en el primer beat de un compás, inicio de frase, con 30 s de beat sin breakdown. 3. Uno en altavoces, otro en auriculares, un oído libre. 4. Elegir un sonido reconocible (snare, stab) que suene una o dos veces por compás y escuchar solo eso contra el otro. 5. Arrancar desde el cue, anotar si cae temprano o tarde, corregir en círculos cada vez más chicos (prueba con ±10% como diagnóstico). 6. Cuando se pueda, corregir al vuelo: nudge y después ajuste. 7. Volumen de auriculares bajo; grabar y escuchar de nuevo. Otras ideas de la búsqueda (foros/sitios de escuela, [S]): sesiones de 15 minutos; pausar un tema a los 16 compases y contar mentalmente; mezclar ida y vuelta 10 minutos con tempos cercanos y luego abrir la brecha.

### 1.3 Recurso canónico de Tiempo

- **Mixxx manual, cap. "DJing With Mixxx"** (https://manual.mixxx.org/2.4/chapters/djing_with_mixxx): leer la sección de beatmatching y Sync Lock vs Quantize. Fijarse en que define tempo y fase como dos problemas, y en que sync de tempo no asegura fase. Es abierto, neutral de marca y citable.
- **Kim et al. 2020 (ISMIR)**, solo las secciones de resultados sobre cambio de tempo y key (https://ar5iv.labs.arxiv.org/html/2008.10267): fijarse en 86,1% < 5% y 2,5% transpuestos como evidencia de uso real, y en su limitación con techno.
- **Digital DJ Tips, Cartledge** (https://www.digitaldjtips.com/learn-to-beatmatch/) como rutina de práctica, marcada como practicante.

## 2. FORMA

### 2.1 Tabla de fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| F1 | Kim et al. 2020 (mismo paper que T3), resultados de cue points y largo de transición | https://ar5iv.labs.arxiv.org/html/2008.10267 | P | 3/3/2/3 | [L] |
| F2 | Mark J. Butler, *Unlocking the Groove* (Indiana UP, 2006, xi+346 pp.) | https://search.worldcat.org/title/61162077 | P (libro) | 3/3/2/3 | [M] (ficha) y [S] (reseña); el libro no lo leí |
| F3 | Wayne Marshall, reseña del libro, *Music Theory Spectrum* 31 (2009), pp. 192-197 | https://wayneandwax.com/academic/mts-butler-unlocking-groove.pdf | S (reseña académica) | 3/2/1/2 | [L] |
| F4 | Butler, "Turning the Beat Around", *Music Theory Online* 7.6 (dic. 2001) | https://mtosmt.org/issues/mto.01.7.6/mto.01.7.6.butler.php | P (artículo) | 3/2/2/2 | [L] |
| F5 | rekordbox 7.1.4 manual: Phrase Analysis / Phrase Edit, cue points | https://cdn.rekordbox.com/files/20250718115648/rekordbox7.1.4_manual_EN.pdf | P (manual) | 3/2/1/2 | [L] parcial |
| F6 | Ryan Dejaegher, "How to DJ 101: Why You Must Understand Phrasing", DJ TechTools (16-nov-2014) | https://djtechtools.com/2014/11/16/how-to-dj-101-why-you-must-understand-phrasing/ | S (practicante) | 2/2/2/1 | [L] |
| F7 | Ryan Keeling, Pioneer DJ blog, técnicas de mezcla por género | https://blog.pioneerdj.com/?p=6295 | S (marca; fecha no consta) | 2/1/1/2 | [L] |
| F8 | Mixed In Key, "Control the Energy Level of Your DJ Sets"; Red Bull Music Academy, "DJing Slow, Fast and Everything In Between" (2019); DJ.Studio (techno: intros/outros largos) | https://mixedinkey.com/Book/Control-The-Energy-Level-Of-Your-DJ-Sets ; https://daily.redbullmusicacademy.com/2019/06/djing-slow-fast ; https://dj.studio/blog/dj-techno-music | S | 1-2/1/1/1 | [S] |
| F9 | Pioneer community, "Phrase editing" | https://community.pioneerdj.com/hc/en-us/community/posts/22978558473113-Phrase-editing | S (foro) | 1/1/1/1 | [S] |

Brewster & Broughton, *How to DJ Right* y *Last Night a DJ Saved My Life* (2000, citado en la reseña de Marshall): **no accedí** a ninguno de los dos. Hueco.

### 2.2 Afirmaciones

**Compás, tiempo fuerte**
- Butler: "almost all EDM can be transcribed in 44 (or, less commonly, 42)" (https://mtosmt.org/issues/mto.01.7.6/mto.01.7.6.butler.php [L]); los compases tienen normalmente ocho corcheas o dieciséis semicorcheas.
- El bombo "tends to function as a source of metrical stability in EDM", por ser el elemento más grave y resonante (F4 [L]). Es la base teórica de por qué se alinea con el bombo y por qué un bombo nuevo puede "turn the beat around" y reinterpretar el compás (F4 [L]). Coincide con la práctica del DJ de mezclar bombos y moverse por el "1".
- Butler sostiene que los grooves de EDM "support multiple interpretations and flexible interactions" (reseña de Marshall, F3 [L]); lo trabaja en hipermétrica (pp. 186-187 del libro, según F3 [L]). La reseña **no** da las cifras de 8/16/32; no puedo atribuir esa convención a Butler. Hueco.

**Frase y convención 8/16/32**
- F6 [L]: la música "is built from phrases of 16 and 32 counts"; el cambio audible "typically occurs every 32 counts"; con 4 beats por compás y 8 compases por frase, el contador de Traktor sube cada 32 beats; marcadores de frase: "a new instrument, a drum fill, or crash".
- Pioneer (F7 [L]) habla de eventos en frases de **8 o 16 compases** (en la sección de house). Ojo: **"16/32" en F6 son beats ("counts"), "8/16" en F7 son compases.** 32 beats = 8 compases; 16 compases = 64 beats. La convención se cita con unidades mezcladas; en la nota hay que fijar "compases" como unidad. Discrepancia de unidades entre fuentes, no de fondo.
- **Evidencia empírica** (F1 [L]): los histogramas de largo de transición en beats tienen **picos cada 32 beats (una frase)**; los autores lo leen como DJs que siguen la estructura repetitiva de la música de baile. Los puntos *cue-out* muestran picos cada 32 beats más claros que los *cue-in*. Cuando los DJ ponen cue en el mismo tema, 23,6% de los pares tiene desvío cero, 40,4% cae dentro de un compás (4 beats) y 73,6% dentro de 8 compases.
  Definiciones del paper: cue-out = "a timestamp that the previous track starts fading out and the next track starts fading in"; cue-in = cuando el anterior terminó de salir; cue-mid = medio de la región de transición.
  El paper **no reporta mediana de duración de transición en segundos** (aparece solo en beats) [L].
  Dataset: 1.557 mezclas, 13.728 temas, 20.765 transiciones, "mostly focuses on House and Trance"; reconoce que el alineado por subsecuencia "does not work well" en géneros como Techno, con mucho tambor y ambiente (F1 [L]).
  **Para el tema:** es la mejor evidencia de que alinear por frase es práctica real y no solo consejo; pero es de House/Trance, y la limitación sobre techno está declarada por los autores.

**Secciones (intro, groove, break, build, drop, outro)**
- rekordbox analiza la estructura y convierte cada sección en una "phrase"; según el modo (mood) los nombres son Intro/Verse/Bridge/Chorus/Outro (mood "mid") o Up/Down/Chorus (mood "high"), y detecta un **Fill-in** de hasta 4 beats al final de Intro, Up y Chorus (manual 7.1.4 [L parcial]; nombres por mood desde F9 [S]). Los nombres de rekordbox son categorías de pop/EDM, no el vocabulario de techno (intro/groove/break/build/drop/outro): hueco de vocabulario a resolver en la nota. Las frases se pueden cortar, mover y cambiar de tipo; "Clear" borra todo salvo el Intro (F5 [L] parcial / F9 [S]).
- Pioneer (F7 [L]): el techno se describe como pieza continua: "Sets feel like a single evolving machine, often making it hard to tell where one tracks ends and another begins"; vocales, melodías y breakdowns largos "break the audience's state of adrenalized focus". La sección de house habla de intros/outros "drum-led, DJ-friendly"; la de techno no menciona intros ni outros (F7 [L]).

**Puntos de entrada/salida, cue points**
- Mixed In Key (F8 [S]): lo más básico del phrasing es mezclar la intro de un tema sobre el outro de otro.
- rekordbox con quantize encendido ajusta el cue al beat más cercano de la grilla (T2 [L]). Cue y hot cue dependen de la grilla: otra vez Tiempo condiciona Forma.
- rekordbox CUE Analysis puede poner cues automáticos pero si el tema tiene pocas frases/compases "the number of Hot Cues/memory cues" es menor (manual 7.1.4 [L parcial]); sugiere que las marcas automáticas parten de la estructura detectada.

**Cómo se cuenta en vivo**
- F6 [L]: contador "phase . bar . beat" en el deck de Traktor (activar "Beats" en preferencias; 8 compases por fase). Escuchar el cambio al subir el número.
- Reglas citadas por sitios de escuela/tienda (DJKIT, Cursa), [S]: contar desde el bombo del inicio de frase hasta 32 y esperar un cambio; empezar a contar desde el principio de una frase, no desde mitad (https://www.djkit.com/blogs/news/djing-rule-of-32 [S]). Sin autoridad independiente; una sola idea repetida en varios sitios cuenta como una fuente.
- DJTT 2015, "Phrase mixing — Throwback Thursday" y Native Instruments, "phrase mixing" (Sara Simms) son versiones de lo mismo (https://djtechtools.com/2015/10/22/phrase-mixing-throwback-thursday-dj-technique/ ; https://blog.native-instruments.com/phrase-mixing/): [S] solo por título, no leídas.

**Temas que rompen la regla**
- F6 admite implícitamente excepciones ("most", "typically") pero no las trata [L]. Las notas de buscador citan hip-hop, open format y disco antiguo como menos rígidos [S, sin URL única de autoridad].
- Foro DJTT "Phrasing techno/tool techno/minimal techno" (https://forum.djtechtools.com/showthread.php?p=714701): **no pude leerlo** (404). Hueco.
- Butler documenta *metrical dissonance* y reinterpretación de compás en EDM (F4 [L]) como recurso del productor: es la base teórica de por qué algunos temas desplazan el "1" o entran con un patrón que parece fuera de compás.

**Techno DJ-friendly**
- Fuentes: DJ.Studio dice que los temas de techno son largos con intros y outros extendidos (F8 [S]); Red Bull Music Academy describe mezclar dos temas durante "tres o cuatro minutos" usando el espacio entre percusión y otros elementos (F8 [S]). Ambas secundarias de poca autoridad; no cubren ARTS ni sellos concretos.

### 2.3 Recurso canónico de Forma

- **Kim et al. 2020**, sección de análisis de cue points y largo de transición (https://ar5iv.labs.arxiv.org/html/2008.10267): fijarse en los picos cada 32 beats, en las definiciones cue-in/mid/out y en la advertencia sobre techno. Única evidencia empírica de mezclas reales.
- **Butler 2001** (https://mtosmt.org/issues/mto.01.7.6/mto.01.7.6.butler.php) para compás 4/4, rol del bombo y reinterpretación; **Butler 2006, cap. 6 "From the Record to the Set"** (según la reseña, F3 [L]: "the clearest and most robust example of such [sequencing techniques] in the vast and varied EDM literature") para cómo los DJ secuencian. No leído; leerlo antes de citar nada.
- **DJ TechTools, Dejaegher 2014** (https://djtechtools.com/2014/11/16/how-to-dj-101-why-you-must-understand-phrasing/) como explicación de práctica del conteo y de los marcadores de frase, marcado como practicante.

## 3. Discrepancias entre fuentes (las dos versiones)

1. **Unidad de la frase:** "16 y 32 counts" (DJTT 2014 [L]) vs "8 o 16 compases" (Pioneer [L]) vs "pico cada 32 beats" (Kim [L]). Conciliable si se fija la unidad; la nota debe decir "8 compases (32 beats)" como frase típica y "16 compases" como bloque mayor.
2. **Sync: a favor/en contra** (T6, T7): ver arriba; ambas lecturas se dan, no hay cifra independiente.
3. **Precisión del análisis de grillas:** "65-80% accurate" (T6, sin método) vs "Typically, the detected BPM is correct but the analyzer has failed to detect the location of the first beat" (Mixxx, vía buscador [S]). No son incompatibles, pero miden cosas distintas.
4. **Límite seguro de key lock:** ±6% (Morse, T5 [L]) vs "no hay límite universal" (guía de software, [S]) vs "fuera de ~5%" (DJTT 2014 [S]). No hay medición independiente.
5. **Nombres de fases en rekordbox editables o no:** un reply de Pioneer dice que sí, otro usuario dice que solo se edita el tipo (F9 [S]); resolver con la versión actual.

## 4. Huecos declarados

- **Sin estudio académico** sobre beatmatching a oído, sobre el umbral de deriva audible (ms entre bombos) ni sobre el sync como práctica. Los ~37 ms/4 min son cálculo mío, no hay fuente.
- **Butler 2006 no leído** (solo ficha y reseña). La convención 8/16/32 compases no está confirmada en Butler; necesita el libro (pp. 186-187 hipermétrica; cap. 6).
- **Brewster & Broughton, *How to DJ Right*:** no accedí.
- **Attack Magazine y Resident Advisor:** la búsqueda no devolvió artículos útiles sobre phrasing/beatmatching; no los cito. Tampoco hay nada específico sobre **ARTS / Emmanuel**; las menciones de techno son genéricas.
- **Kim et al. 2020:** leí el HTML (ar5iv); el PDF no era extraíble. No verifiqué los números contra el PDF original ni vi las figuras. El corpus es House/Trance; techno queda fuera según los autores.
- **rekordbox:** manual leído por secciones con pdftotext; no leí el apéndice de Phrase Analysis ni el "PHRASE EDIT operation guide" aparte. Nombres de secciones por mood vienen de un foro.
- **Mixxx:** la cita sobre "BPM cercano a entero" viene del resultado del buscador sobre la página de Beat Detection 2.5 (no fetchada) [S]; verificar. La mitad del manual sobre pitch rate range no la da (el manual no da rango del slider).
- **Cifras de deriva y redondeo:** solo foros [S]. Falta verificar en un manual oficial (CDJ, Traktor) cuántos decimales muestra y usa cada plataforma.
- **Qué mide la fase "a oído" en techno** (trucos para bombos solapados, uso de hi-hats/percusión de referencia): solo la rutina genérica de Cartledge; nada de practicantes reconocidos de techno leído.
- **Temas que rompen la regla:** sin fuente sólida; el foro de techno era inaccesible. Habría que buscar entrevistas (RA) con DJ de techno sobre fraseo irregular.
- **Vocabulario de secciones en techno** (groove, break, build, drop): no encontré fuente que lo fije; los términos de rekordbox son otros.
