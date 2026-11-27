# Investigación: Espectro y Armonía en la mezcla de DJ

Fecha de la investigación: 2026-11-27. Lectora objetivo: quien empieza o mezcla poco, hasta intermedio. Estética de ejemplos: techno hipnótico y percusivo (ARTS), mezcla larga.

Todo lo de la web se trató como dato. Convenciones:

- Tipo: P = primaria (norma, paper, manual oficial, organismo); S = secundaria (práctica, divulgación, fabricante).
- Puntajes 1-3: Aut(oridad) / Prof(undidad) / Ej(emplos) / Uni(cidad).
- Marca de lectura: [L] página abierta y leída con el extractor de WebFetch (la herramienta resume con un modelo chico; las citas literales son las que la herramienta devolvió entre comillas); [M] solo metadatos o abstract; [S] solo resumen del buscador.
- Las tres rondas de búsqueda por componente no se agotaron en todos; lo no encontrado está en "Huecos".

## 0. Sobre la división Espectro / Armonía

La división sirve como organización didáctica pero no es como el campo la parte exactamente.

- La literatura de DJ práctica (Digital DJ Tips, Pioneer DJ, DJ TechTools) trata "EQ/graves" y "mezcla armónica/key" como dos técnicas separadas, así que la división coincide con la práctica. Fuente: https://www.digitaldjtips.com/how-important-is-it-to-mix-in-key/ [L].
- Pero ambas comparten un mismo mecanismo físico: dos señales sumadas en un oído. El masking, la suma de fase y la disonancia son del mismo problema (qué pasa en el mismo rango de frecuencias). Lo más honesto es decir que armonía es un caso de espectro: la clave solo importa donde hay contenido tonal (bajo, melodía, pads) en la zona que se solapa. Digital DJ Tips lo dice así: "Mixing in key is only necessary if the two tracks contain musical information in the parts you are mixing together." https://www.digitaldjtips.com/how-important-is-it-to-mix-in-key/ [L].
- Las bandas de graves (kick y bajo) caen a la vez en espectro y en armonía: el bajo es la nota que define la tonalidad percibida, pero en techno el kick suele estar afinado y también tiene tono. Esto no lo encontré documentado como tal en una fuente; es inferencia mía (hueco).

## 1. Componente: Espectro

### 1.1 Tabla de fuentes

| # | Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|---|
| E1 | Mike Senior, "Mixing Bass", Sound On Sound, sept. 2012 | https://www.soundonsound.com/techniques/mixing-bass | S (revista técnica, buena autoridad) | 3 | 3 | 2 | 2 | [L] |
| E2 | Wikipedia, "Critical band" (cita Fletcher 1933/1940, Glasberg & Moore 1990, Moore 1998) | https://en.wikipedia.org/wiki/Critical_band | S (enciclopedia; remite a primarias) | 2 | 2 | 1 | 1 | [L] |
| E3 | ISO 226 (curvas de igual sonoridad), registro ISO | https://www.iso.org/standard/34222.html | P (norma) | 3 | 1 | 1 | 3 | [S] (el sitio devolvió 403; ver buscador) |
| E4 | Wikipedia, "Equal-loudness contour" | https://en.wikipedia.org/wiki/Equal-loudness_contour | S | 2 | 2 | 1 | 1 | [S] |
| E5 | Manual de Mixxx, cap. 12 (mezcla), sección Gain/clipping | https://manual.mixxx.org/2.5/en/chapters/djing_with_mixxx | P (manual oficial) | 3 | 2 | 1 | 2 | [L] |
| E6 | Sound On Sound, gain staging (varios) | https://www.soundonsound.com/techniques/establishing-project-studio-reference-monitoring-levels ; https://www.soundonsound.com/techniques/gain-staging-logic-pro | S | 3 | 2 | 1 | 2 | [S] (de grabación/estudio, no de DJ) |
| E7 | Native Instruments, "Traktor Pro 2 EQ and filter models" | https://support.native-instruments.com/support/solutions/articles/69000879507-traktor-pro-2-eq-and-filter-models | P (manual de fabricante) | 3 | 1 | 1 | 2 | [L] |
| E8 | Foro Pioneer DJ (usuario), modos EQ vs isolator del DJM-900NXS2 | https://community.pioneerdj.com/hc/en-us/community/posts/22980396236697/comments/22989884666137 | S (foro, no oficial) | 1 | 1 | 1 | 2 | [S] |
| E9 | Digital DJ Tips, "Why Your DJ Mixes Sound Muddy (And 2 Easy Ways To Fix It)" | https://www.digitaldjtips.com/?p=2799689 | S (practicante, marcada) | 2 | 2 | 2 | 1 | [S] |
| E10 | Digital DJ Pool, EQ para principiantes; cursa.app; djclass.net (guías de bass swap) | https://digitaldjpool.com/blog/dj-eq-mixing-for-beginners/ | S (tres textos que dicen lo mismo = una sola fuente) | 1 | 1 | 2 | 1 | [S] |
| E11 | CDC/NIOSH, "Understand Noise Exposure" | https://www.cdc.gov/niosh/noise/prevent/understand.html | P (agencia pública, EE.UU.) | 3 | 2 | 1 | 3 | [L] |
| E12 | OMS, noticia del Estándar global de escucha segura en locales y eventos (2022-03-02) | https://www.who.int/news/item/02-03-2022-who-releases-new-standard-to-tackle-rising-threat-of-hearing-loss | P (organismo) | 3 | 2 | 1 | 3 | [L] |
| E13 | OMS, ficha de la publicación (ISBN 978-92-4-004311-4) | https://www.who.int/publications/i/item/9789240043114 | P | 3 | 1 | 1 | 2 | [L] (solo ficha, no el PDF de 107 págs.) |
| E14 | Microsoft, "Louder Sounds Better" (blog de ingeniería de audio) | https://learn.microsoft.com/en-us/archive/blogs/audiofool/louder-sounds-better | S (blog técnico, informal) | 2 | 1 | 1 | 2 | [S] |
| E15 | arXiv 2026, jueces LLM de voz favorecen el clip +6 dB | https://arxiv.org/pdf/2609.36979 | P (preprint, sobre voz y modelos, no música) | 1 | 1 | 1 | 1 | [S]; poco relevante para DJ, solo ilustra el sesgo |

No lei Zwicker & Fastl, *Psychoacoustics*: no es de acceso abierto. Va como hueco y como recurso canónico recomendado para leer por la biblioteca.

### 1.2 Afirmaciones

**Bandas y graves**
- La zona 20-100 Hz "presents probably the most difficult challenge" y contiene la mayoría de los fundamentales de los bajos; para bajos, "the main battleground is the 'warmth' region below about 300Hz". https://www.soundonsound.com/techniques/mixing-bass [L]
- "The most critical sub-100Hz conflict in modern mixes is that between bass and kick drum." Ídem. [L]. (Contexto: es consejo de mezcla de estudio, no de DJ.)
- Con varias partes de bajo: "I'd usually choose only one as the main low-end source, and high-pass filter the others around 100Hz." Es la versión de estudio de la regla DJ "un solo bajo por vez". Ídem [L]
- Las capas con desfase pueden cancelarse: "They can cancel gruesomely at certain frequencies if there are polarity or phase mismatches." Ídem [L]. Esto respalda lo de fase y suma de graves, pero la fuente habla de capas dentro de una mezcla, no de dos kicks de dos tracks desfasados lentamente; ese caso concreto (batido de kicks casi en fase) no lo encontré en una fuente citable (hueco).
- Qué instrumentos viven en cada banda en techno (kick, bajo, hats, percusión, pads): no encontré una fuente primaria con rangos para techno; los rangos por instrumento los doy como conocimiento común sin cita (hueco declarado).

**Masking y bandas críticas**
- Banda crítica: introducida por Harvey Fletcher en 1933 y refinada en 1940; "is the bandwidth of the 'auditory filter' created by the cochlea"; es "roughly, the band of frequencies within which a second tone interferes with the perception of a first tone through auditory masking". https://en.wikipedia.org/wiki/Critical_band [L]
- Solo los maskers dentro del ancho de banda crítico contribuyen a enmascarar; los graves enmascaran a los agudos más que al revés ("upward spread of masking"). Ídem [L]
- Cálculo mío con la fórmula ERB de Glasberg & Moore que cita la página: ERB aprox. 79 Hz a 500 Hz. Ídem [L]. Esto explica por qué en graves (donde las notas están separadas por pocos Hz) casi todo cae dentro de una misma banda y se enmascara.
- Zwicker: las 24 bandas Bark y "100 Hz de ancho por debajo de 500 Hz": la página de Wikipedia consultada no lo dice; se debe verificar en Zwicker & Fastl (hueco).

**EQ de mixer, kill, isolator, filtros**
- Un EQ de mixer estándar baja a unos -26 dB; el modo isolator da kill total (-inf dB); varía según el modelo. Fuente: usuario de foro Pioneer ("EQ mode = -26dB cut. Isolator = infinite cut") https://community.pioneerdj.com/hc/en-us/community/posts/22980396236697/comments/22989884666137 [S]. Es la única fuente de la cifra; el manual del DJM no lo confirmé (hueco). Algoriddim, en cambio, indica -24 dB a +6 dB para su EQ "Classic" (resumen de buscador) https://help.algoriddim.com/user-manual/djay-pro-mac/settings/sound [S]: las cifras discrepan entre aparatos.
- Traktor tiene seis modelos de EQ, y solo "Z ISO" es kill/isolator, con "24 db/octave slope". https://support.native-instruments.com/support/solutions/articles/69000879507-traktor-pro-2-eq-and-filter-models [L]. La página no da frecuencias de cruce.
- Frecuencias de cruce de los EQ de 3 bandas de mixers DJ: no las encontré en ninguna fuente primaria (hueco).

**Bass swap (práctica)**
- Procedimiento: bajar el LOW del tema entrante antes de entrar, y en un límite de frase (cada 8 o 16 compases) bajar el LOW saliente mientras sube el entrante. Fuentes: Digital DJ Pool / cursa.app / djclass.net (una sola fuente efectiva, que parafrasean lo mismo) https://digitaldjpool.com/blog/dj-eq-mixing-for-beginners/ [S]; Digital DJ Tips lo describe igual https://www.digitaldjtips.com/?p=2799689 [S].
- Diagnóstico: si suena como que "se hundió la sala", se sacó demasiado grave de golpe; si suena boomy, los graves se solaparon demasiado tiempo. (cursa.app, vía buscador) [S]
- Discrepancia de práctica: swap instantáneo para drops, swap gradual de 2-4 pulsos para grooves rodantes (Digital DJ Pool). Para techno hipnótico de mezcla larga no encontré fuente específica sobre el swap; queda para contraste con la práctica de ARTS (hueco).

**Ganancia y niveles**
- Manual de Mixxx: los niveles promedio deben estar "cerca del tope de la zona verde" y fuera del amarillo (headroom); "If a level meter is in its red region, the signal is clipping and the gain should be turned down." https://manual.mixxx.org/2.5/en/chapters/djing_with_mixxx [L] (la cita en español es mi traducción; la cita en inglés la devolvió el extractor).
- En digital no hay headroom sobre 0 dBFS, lo que pasa se recorta. SOS recomienda margen de 20 dB (nivel de operación -20 dBFS) en estudio. https://www.soundonsound.com/techniques/establishing-project-studio-reference-monitoring-levels [S]. Es convención de estudio, no de DJ; en DJ el mixer tiene medidor propio (hueco: sin fuente de DJ con números).
- Hay desacuerdo entre fuentes de estudio sobre el nivel objetivo (-6 vs -18 dBFS), no resuelto aquí. https://www.soundonsound.com/sound-advice/q-should-gain-stage-6dbfs-or-18dbfs [S]

**Volumen percibido**
- ISO 226:2003 especifica niveles de presión y frecuencias de tonos puros que oyentes juzgan igual de fuertes; supuestos: onda plana libre, fuente al frente, escucha binaural, oyentes otológicamente normales de 18 a 25 años. https://www.iso.org/standard/34222.html [S]. La misma página la marca "withdrawn" (retirada); no pude confirmar con qué edición se reemplazó (debería ser ISO 226:2023, no verificado). Hueco.
- Fletcher y Munson midieron en 1933 con auriculares, escalones de 10 dB; Robinson y Dadson re-determinaron en 1956, base de una norma ISO 226. https://en.wikipedia.org/wiki/Equal-loudness_contour [S]
- Bajo unos 100 Hz la sonoridad sube muy rápido con el nivel (hasta unos 24 dB por octava, según una fuente citada) y las diferencias entre estudios en graves "remain unexplained". Ídem [S]. Aplicación a DJ: a bajo volumen los graves se oyen menos que a volumen de club. Esa aplicación es inferencia mía.
- "Más fuerte suena mejor": el blog de Microsoft explica la idea común de que lo más fuerte suena más pleno porque se acerca a curvas más planas, y que "the louder one will often subjectively sound better regardless" de calidad. https://learn.microsoft.com/en-us/archive/blogs/audiofool/louder-sounds-better [S]; informal. Un preprint de 2026 con jueces LLM de voz muestra sesgo similar (+6 dB, preferencia media 0.578) pero no es música ni humanos: https://arxiv.org/pdf/2609.36979 [S]. No encontré un estudio de preferencia con música a igual nivel, con oyentes humanos (hueco).
- Auto gain / normalización: Serato lo describe como valor por tema "required to match the perceived loudness of the track to a reference level" (Serato, vía buscador) https://serato.com/latest/blog/15577/auto-gain-whats-all-that-about [S]. Para rekordbox no hallé manual oficial: hay un foro que dice que el auto gain solo funciona en rekordbox DJ y no en la exportación USB para CDJ (2016, a verificar) https://forums.pioneerdj.com/hc/it/community/posts/115019180963-Auto-Gain-confused [S]; y un vendedor de un producto competidor afirma que es por pico y no por sonoridad (interesado, no neutro) https://dj-master-web.vercel.app/en/blog/rekordbox-volume-normalize-en [S]. Sin resolver.

**Fase y suma de graves**
- Solo hay la cita de SOS sobre cancelación por desfase/polaridad (arriba). Una explicación de fase de DJ con dos kicks (batido, cancelación periódica) no la encontré en fuente confiable; hueco.

**Seguridad auditiva (dos fuentes independientes: NIOSH y OMS)**
- NIOSH: "The NIOSH recommended exposure limit (REL) for occupational noise exposure is 85 A-weighted decibels (dBA) over an eight-hour shift." La página usa "Exchange Rate: 3 dB". https://www.cdc.gov/niosh/noise/prevent/understand.html [L]. Página actualizada 2026-10-28.
- Que cada 3 dB de más reduce a la mitad el tiempo permitido (88 dBA, unas 4 h) viene del buscador sobre otra página NIOSH (https://cdc.gov/niosh/bulletin/2016/noise.html [S]); la página que abrí no trae tabla. OSHA usa 5 dB, no 3 (https://www.osha.gov/noise/standards [S]): discrepancia entre agencias; el 85 dBA/3 dB es lo más conservador.
- OMS (2022-03-02): seis recomendaciones del estándar, la primera "a maximum average sound level of 100 decibels"; otras: monitoreo en vivo con equipo calibrado, optimizar acústica, protección auditiva personal, zonas de descanso del oído, capacitación del personal. https://www.who.int/news/item/02-03-2022-who-releases-new-standard-to-tackle-rising-threat-of-hearing-loss [L]. "Over 1 billion people aged 12 to 35 years risk losing their hearing." Ídem.
- El período de promedio de los 100 dB (algunas fuentes secundarias dicen 15 minutos) no figura en la noticia ni en la ficha; solo puede confirmarse en el PDF de 107 págs. (hueco). Las dos fuentes (NIOSH ocupacional, OMS recreativo) son independientes; sus límites no son comparables entre sí (85 dBA/8 h vs 100 dB promedio de evento), y eso se debe decir al lector, no igualar.

### 1.3 Recursos canónicos (Espectro)

- **Mecanismo, masking y bandas críticas:** Zwicker & Fastl, *Psychoacoustics: Facts and Models* (Springer), capítulos de enmascaramiento y bandas críticas. No lo leí. Fijarse en: la escala Bark, el ancho de banda crítico en graves y el masking asimétrico (hacia arriba).
- **Cómo se resuelve kick vs bajo:** Senior, "Mixing Bass" (SOS 2012), https://www.soundonsound.com/techniques/mixing-bass. Fijarse en la sección de varias partes de bajo y en el conflicto kick/bajo bajo 100 Hz. Sirve como puente: es de estudio, pero el principio es el mismo que el swap.
- **Niveles en el mixer:** manual de Mixxx cap. 12, https://manual.mixxx.org/2.5/en/chapters/djing_with_mixxx. Fijarse en la regla del medidor (verde bien, rojo recorta).
- **Seguridad:** NIOSH (85 dBA / 3 dB) y OMS 2022 (100 dB y zonas de descanso).
- **Práctica:** Digital DJ Tips sobre mezclas "muddy", marcada como secundaria.

## 2. Componente: Armonía

### 2.1 Tabla de fuentes

| # | Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|---|
| A1 | Mixed In Key, "Harmonic Mixing Guide" (fabricante, interesado) | https://mixedinkey.com/harmonic-mixing-guide/ | S (fabricante) | 2 | 2 | 2 | 2 | [L] |
| A2 | Faraldo, Gómez, Jordà, Herrera, "Key Estimation in Electronic Dance Music", ECIR 2016, pp. 335-347, LNCS 9626, DOI 10.1007/978-3-319-30671-1_25 | https://rd.springer.com/chapter/10.1007/978-3-319-30671-1_25 (el sitio pide autenticación); repositorio UPF https://recercat.cat/handle/10230/33060 | P | 3 | 3 | 1 | 3 | [M] (abstract vía buscador) |
| A3 | Faraldo, tesis doctoral UPF 2017, "Tonality Estimation in Electronic Dance Music" | https://zenodo.org/records/1154586 | P | 3 | 3 | 2 | 3 | [L] (solo la descripción de Zenodo, no el PDF) |
| A4 | Knees et al., ISMIR 2015, dataset GiantSteps key (604 previews de Beatport) | https://github.com/GiantSteps/giantsteps-key-dataset | P (dataset, README) | 3 | 2 | 1 | 3 | [L] |
| A5 | mir_eval, documentación de la métrica de clave (score ponderado MIREX) | https://mir-eval.readthedocs.io/latest/api/key.html | P (documentación de software de evaluación) | 2 | 2 | 1 | 3 | [S] |
| A6 | Böck et al. 2016, extractor sobre GiantSteps (0.729 MIREX) y Korzeniowski & Widmer 2017, CNN de clave | https://arxiv.org/pdf/1706.02921 | P | 3 | 3 | 1 | 2 | [S] |
| A7 | Kim, Choi, Sacks, Yang, Nam, ISMIR 2020, análisis de mezclas reales | https://arxiv.org/abs/2008.10267 | P | 3 | 3 | 1 | 3 | [L] (abstract y resumen) |
| A8 | Manual de Mixxx, "Key Detection" | https://manual.mixxx.org/2.5/en/chapters/preferences/key_detection | P (manual oficial) | 3 | 1 | 1 | 2 | [L] |
| A9 | Mixxx, "New in 2.3: KeyFinder support" | https://mixxx.org/news/2021-04-08-new-in-2-3-keyfinder | P (noticia oficial) | 3 | 1 | 1 | 2 | [S] |
| A10 | Phil Morse, Digital DJ Tips, "How Important Is It For DJs To Mix In Key?" (act. 2024-02-21) | https://www.digitaldjtips.com/how-important-is-it-to-mix-in-key/ | S (practicante) | 2 | 2 | 1 | 2 | [L] |
| A11 | Ryan Keeling, Pioneer DJ blog, "How do DJs approach harmonic mixing?" (sin fecha) | https://blog.pioneerdj.com/?p=711 | S (fabricante de hardware, DJs citados) | 2 | 2 | 2 | 3 | [L] |
| A12 | DJ TechTools, "Mixing in Key: When and How to Change Track Key in DJ Software" (2013-05-15) | https://djtechtools.com/2013/05/15/mixing-in-key-when-and-how-to-change-track-key-in-dj-software/ | S | 2 | 2 | 2 | 1 | [L] |
| A13 | MusicRadar, "harmonic mixing" | https://musicradar.com/news/harmonic-mixing | S | 2 | 1 | 1 | 2 | [S] |
| A14 | Bonedo, "Harmonic Mixing Basics" | https://www.bonedo.de/artikel/harmonic-mixing/2 | S | 1 | 2 | 2 | 1 | [S] |
| A15 | Wikipedia, "Harmonic mixing" | https://en.wikipedia.org/wiki/Harmonic_mixing | S | 2 | 1 | 1 | 1 | [S] |

### 2.2 Afirmaciones

**Camelot y compatibilidad**
- Reglas de Mixed In Key (fabricante, interesado): misma clave sirve; mismo número, otra letra (8A y 8B) sirve; un paso arriba o abajo (8A a 9A o 7A) sirve; saltos grandes como 3A a 9A son un "curveball" riesgoso. "Our Camelot Easymix system makes navigating through keys as easy as counting up and down." https://mixedinkey.com/harmonic-mixing-guide/ [L]
- Mixed In Key afirma que su sistema "started the harmonic mixing movement in 2006" y que "independent tests consistently show Mixed In Key to be the most accurate key detection system on the planet", sin fuentes ni metodología en la página. Ídem [L]. Tratar como afirmación comercial no verificada.
- El Camelot Wheel se apoya en el círculo de quintas (relativas mayor/menor en la misma posición del reloj; números adyacentes = una quinta de distancia). https://producelikeapro.com/blog/camelot-wheel/ [S] y https://www.digitaldjtips.com/how-important-is-it-to-mix-in-key/ [L] (esta última da la regla de una hora arriba o abajo o la rueda alterna a la misma hora). La teoría musical de fondo (círculo de quintas) no la contrasté con un texto primario (hueco).
- Quién inventó la rueda Camelot: la página de Mixed In Key no nombra individuo, la atribuye a la empresa. La atribución a Mark Davis que pide el encargo no la pude verificar (hueco). Open Key: tampoco encontré fuente primaria que lo describa.

**Detección automática y su exactitud**
- Faraldo et al. (ECIR 2016): método basado en plantillas; crean perfiles de clave nuevos combinando observaciones y análisis de corpus, y agregan dos etapas de pre-procesado; prueban en datasets independientes de pop y EDM, con "interesting improvements". https://recercat.cat/handle/10230/33060 y https://rd.springer.com/chapter/10.1007/978-3-319-30671-1_25 [M] (el buscador no dio cifras; no leí el paper).
- Tesis de Faraldo (UPF, 2017): crítica la práctica corriente por usar un vocabulario centrado en la tonalidad clásica occidental y en un modelo binario mayor/menor "que puede no servir para música popular"; armó un corpus de más de 2000 extractos EDM y propone etiquetas de clave más abiertas (otras prácticas modales, configuraciones tonales ambiguas). https://zenodo.org/records/1154586 [L] (descripción, no el PDF). Este es el argumento más fuerte contra confiar en la clave automática en EDM.
- Dataset GiantSteps key: 604 previews de dos minutos de beatport.com, todos de música electrónica de baile; etiquetas "extracted from forum entries of people correcting the key annotations", es decir correcciones de usuarios, sin verificación experta descrita en el README. Referencia: Knees et al., ISMIR 2015. https://github.com/GiantSteps/giantsteps-key-dataset [L]
- Métrica MIREX/mir_eval: 1.0 misma clave y modo, 0.5 una quinta arriba, 0.3 relativa mayor/menor, 0.2 paralela mayor/menor, 0.0 el resto. https://mir-eval.readthedocs.io/latest/api/key.html [S]. Importa porque un "acierto parcial" cuenta, y para un DJ errar por relativa (A vs B en Camelot) es el error más benigno.
- Resultado reportado: 0.729 de score MIREX con el extractor de Böck et al. (2016) sobre GiantSteps. https://arxiv.org/pdf/1706.02921 [S], con la advertencia del mismo texto de que el modelo se entrenó con audio de la misma fuente (Beatport) y distribución de género, así que la cifra no es comparable con modelos entrenados en otros datos. No recuperé la tabla oficial de resultados MIREX (el sitio music-ir.org dio error de certificado). Hueco.
- Mixxx: detector de clave "de alta precisión" según su manual; análisis completo por defecto, o "Fast Analysis" que usa solo el primer minuto; la notación de la clave se elige en preferencias. https://manual.mixxx.org/2.5/en/chapters/preferences/key_detection [L]. El Queen Mary Key Analyzer es el predeterminado y KeyFinder se agregó en 2.3. https://mixxx.org/news/2021-04-08-new-in-2-3-keyfinder [S]. El manual no lista las notaciones.
- Un DJ citado por Pioneer dice que Mixed In Key "is not always 100% accurate". https://blog.pioneerdj.com/?p=711 [L]. No encontré un estudio independiente que compare Mixed In Key, rekordbox, Traktor y Serato en techno (hueco importante: la afirmación de MIK de ser el más exacto queda sin contrastar).

**Cambio de tono con pitch fader**
- Un semitono equivale a un factor 2^(1/12) = 1,0595, o sea unos 5,95 % de cambio de frecuencia. Es cálculo mío, no cita. El "aprox. 6 %" del encargo coincide con él; no encontré una fuente DJ que lo diga explícitamente: DJ TechTools no menciona el 6 % (https://djtechtools.com/2013/05/15/mixing-in-key-when-and-how-to-change-track-key-in-dj-software/ [L]).
- Con key lock apagado, mover el pitch cambia el tono y el tempo juntos; con key lock el tono queda fijo (en Serato, 0 %). Ídem [L]. En Mixxx, el sync puede producir un cambio de tono notable; el key lock lo reduce. https://manual.mixxx.org/2.5/en/chapters/djing_with_mixxx [L]
- Calidad: DJ TechTools advierte que cambiar la clave de un tema más de dos semitonos empieza a degradar la calidad del audio. Ídem [L]. Es afirmación de una sola fuente secundaria (2013).
- Los pasos de key shift en Traktor y Virtual DJ son de un semitono por pulsación. Ídem [L]. La CDJ-3000 añade Key Sync y Key Shift, según Pioneer. https://blog.pioneerdj.com/?p=711 [L]

**Peso de la armonía en techno percusivo / atonal (posición de practicantes)**
- Digital DJ Tips (Phil Morse, 2024): la clave solo importa si hay contenido musical en las partes que se mezclan; con solo percusión, "checking key gains nothing". Advierte que mezclar solo por clave lleva a elegir temas por compatibilidad y no por ser el disco justo, que una mezcla en clave puede sonar mal ("if a mix sounds bad, it is bad"), y que los botones de key sync pueden mover la clave tanto que el tema suena "ridiculous". https://www.digitaldjtips.com/how-important-is-it-to-mix-in-key/ [L]
- Pioneer DJ blog (practicantes citados): Sef Kombo, "Harmonic mixing is absolutely essential in my opinion"; Erol Alkan, "It's an incredible tool, I couldn't imagine not being able to use it", pero nunca deja que la clave "dictate" sus elecciones; DJ Puffy se sorprende de que "tracks that 'shouldn't fit'" encajen, "That often happens with minimal tracks". https://blog.pioneerdj.com/?p=711 [L]. Hay posiciones enfrentadas (esencial vs. herramienta), y ninguna de las citadas es de techno hipnótico/ARTS: hueco de práctica específica del sello.
- MusicRadar (vía buscador): un DJ dice que gran parte del techno tiene contenido melódico muy simple y que el cambio se hace con filtro y resonancia más que con acordes, así que chocar de clave es difícil. https://musicradar.com/news/harmonic-mixing [S]. Bonedo sugiere hacer la transición en una sección de percusión antes de que entren melodías o bajos. https://www.bonedo.de/artikel/harmonic-mixing/2 [S]. Estas dos se apoyan en lo que dice Digital DJ Tips; no son independientes en lo sustancial.
- Análisis académico de mezclas reales (Kim et al., ISMIR 2020): 1557 mezclas de 1001Tracklists, 13.728 temas y 20.765 transiciones, alineando mezcla a temas con rasgos "less sensitive to the tempo or key change of the original track in a mix"; obtienen puntos de cue, longitud de transición, segmentación y cambios musicales. https://arxiv.org/abs/2008.10267 [L]. El resumen no trata la compatibilidad armónica ni el EQ; no hay prueba empírica ahí de cuánto respetan la clave los DJ (hueco). Mismos autores, otros trabajos sobre fader y EQ: DAFx 2022 (5040 mezclas, 50.742 transiciones) https://mac.kaist.ac.kr/pubs/KimYangNam-dafx2022.pdf [S] y NIME 2021 (sub-bandas) https://mac.kaist.ac.kr/ai_dj.html [S]; podrían servir para Espectro (cómo mueven EQ los DJ), no leídos.

### 2.3 Recursos canónicos (Armonía)

- **Qué es y qué combina:** guía de Mixed In Key (https://mixedinkey.com/harmonic-mixing-guide/) para las reglas de la rueda, leída sabiendo que es del fabricante; complementar con un texto de teoría sobre el círculo de quintas (no elegido: hueco).
- **Qué tan fiable es la detección:** tesis de Faraldo (https://zenodo.org/records/1154586), capítulo sobre el vocabulario de claves, y el paper ECIR 2016. Fijarse en por qué mayor/menor binario falla en EDM.
- **Cómo se ve en el software:** Manual de Mixxx, "Key Detection" y cap. 12, sección key lock.
- **Cuánto importa en techno:** Digital DJ Tips, Morse 2024 (regla de "contenido musical en la parte que mezclás") más el artículo de Pioneer DJ para las voces enfrentadas.

## 3. Huecos declarados

1. Zwicker & Fastl, *Psychoacoustics*, no leído; el valor de las 24 bandas Bark y el ancho de banda crítico en graves quedan sin cita primaria.
2. Qué instrumentos ocupan qué banda en techno, y frecuencias de cruce de los EQ de mixers DJ (DJM, Xone, Traktor): sin fuente.
3. Explicación de batido y cancelación de dos kicks casi en fase: solo hay una cita general de SOS sobre fase en estudio; sin fuente DJ.
4. ISO 226: no abrí la norma (403). Figura como retirada; falta confirmar la edición vigente (¿ISO 226:2023?) y las curvas.
5. Cifras de kill vs corte suave (-26 dB, isolator -inf) de un foro y un resumen de buscador; falta manual oficial del DJM y de Allen & Heath.
6. Auto gain de rekordbox: no hallé manual oficial; lo que hay es de foros y de un competidor interesado.
7. Estudio de "más fuerte suena mejor" con música y nivel igualado: no lo hallé (hay uno de voz con jueces LLM, poco relevante).
8. Período de promedio del tope de 100 dB de la OMS (fuentes secundarias dicen 15 min): falta el PDF de 107 págs.
9. Exactitud real de la detección de clave: no recuperé las tablas de MIREX ni el texto del paper ECIR de 2016 (solo abstract); tampoco hay comparación independiente entre Mixed In Key, rekordbox, Traktor y Serato. La pretensión de Mixed In Key de ser el más exacto no está contrastada.
10. Origen de la rueda Camelot (Mark Davis) y de Open Key: no verificado. Notaciones disponibles en Mixxx: no listadas en el manual.
11. Fuente DJ que diga "6 % ≈ un semitono": no hallada; solo el cálculo 2^(1/12).
12. Posición de practicantes específicos del techno hipnótico/ARTS sobre armonía y sobre el swap de graves en mezcla larga: sin fuente.
13. Círculo de quintas: no contrasté con un texto de teoría musical primario.
14. Kim et al. ISMIR 2020 se leyó solo por abstract; los trabajos de DAFx 2022 y NIME 2021 no se leyeron.
