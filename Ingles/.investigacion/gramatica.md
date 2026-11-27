# Gramática: informe de investigación (2026-11-27)

Alcance: vertical **Gramática** del tema Inglés (B2 a C1/C2, hispanohablante rioplatense), vista desde lo que separa B2 de C1/C2 y desde la transferencia del castellano.

Convenciones. Puntajes 1 a 3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U). Marca de lectura: [L] leído completo o el pasaje relevante del texto completo, [M] metadatos o abstract, [S] resumen del buscador o secundario. Tipo: P primaria, S secundaria. Todo lo que vino de la web se trató como dato.

Límite de esta tanda: la mayoría de los papers de revista están detrás de paywall (Cambridge, Benjamins) y los fetch devolvieron solo abstract. Lo que se pudo leer entero: Verratti-Souto et al. 2025 (EGP), Perez-Guerra y Smirnova 2024 (present perfect), Araújo 2019 (Buenos Aires) y la hoja de errores de Cambridge. El sitio del English Grammar Profile (englishprofile.org) es una app JavaScript que no se pudo leer con fetch ni con curl: **no pude verificar ningún enunciado concreto del EGP de B2, C1 o C2**.

---

## 0. Cómo divide el campo esta vertical (y si el árbol coincide)

Hallazgos:
- El campo no separa "tiempo y aspecto", "futuro", "modales" y "condicionales" como cuatro temas independientes; Leech los trata juntos como el sistema del sintagma verbal (tiempo, aspecto, modo y modalidad). El índice de *Meaning and the English Verb* tiene: presente y pasado simples, aspecto progresivo, pasado y futuro, modales primarios, modalidad, estilo indirecto, modo. https://www.routledge.com/Meaning-and-the-English-Verb/Leech/p/book/9780582784574 [S]. Con eso el árbol actual coincide bastante: es una partición por forma-función, no por "tiempo verbal".
- La investigación de adquisición (Bardovi-Harlig) trabaja "temporalidad" como un solo dominio: tiempo, aspecto, y la hipótesis del aspecto léxico. https://www.cambridge.org/core/journals/studies-in-second-language-acquisition/article/abs/aspect-hypothesis-and-the-acquisition-of-l2-past-morphology-in-the-last-20-years/353744B9E21B7B88989CD96A45E3B87F [M].
- Un punto donde el árbol se separa del campo: "futuro" en inglés es un tema de modalidad más que de tiempo (will es modal). Ese dato es de gramática descriptiva y **no lo verifiqué con URL en esta tanda** (Huddleston y Pullum, Leech lo sostienen, a confirmar en el capítulo de tiempo y modalidad).

Propuestas de cambio al árbol:
1. **Agregar un componente** para lo que no tiene casa: sujeto obligatorio, orden de adjetivos y adverbios, preguntas indirectas, preposiciones (que la hoja de Cambridge ubica como error nº 1). Nombre sugerido: `orden-y-estructura-basica` o `transferencia-del-castellano`. Alternativa mínima: sujeto obligatorio dentro de `tiempo-y-aspecto` (por la concordancia verbal) y preguntas indirectas dentro de `estructuras-avanzadas`.
2. **Los "verbos de estado"** van en `tiempo-y-aspecto` (aspecto léxico), como ya está planteado; es el eje de la hipótesis del aspecto.
3. **Artículos**: el árbol lo trata como vertical entera con error típico de genéricos; la evidencia dice que lo problemático para hispanohablantes es sobre todo el genérico, no el sistema entero (ver sección 7). Conviene que el componente lo diga.
4. La división por nivel EGP (B2 / C1 / C2) **no debería usarse como criterio de partición**: su asignación de niveles está en discusión (sección 1).

---

## 1. Entrada de la vertical: qué gramática es B2, C1, C2; descriptiva vs pedagógica; gramática cognitiva

### Fuentes

| # | Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|---|
| 1a | O'Keeffe y Mark (2017), "The English Grammar Profile of learner competence", *Int. J. of Corpus Linguistics* 22(4): 457-489 | P | 3/3/2/3 | [M] (abstract y datos citados por 1b; el PDF devolvió 403) | https://orca.cardiff.ac.uk/id/eprint/166496 |
| 1b | Verratti-Souto, Sagirov y Chen (2025), "NLP-powered quantitative verification of the English Grammar Profile's structure-level assignment", *Annual Review of Applied Linguistics* 45: 109-130 | P (crítica) | 3/3/2/3 | [L] | https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8323F1AD466EF982EA47DEFBB0D740D5/S0267190525100093a.pdf/nlp-powered-quantitative-verification-of-the-english-grammar-profiles-structure-level-assignment.pdf |
| 1c | Conferencia O'Keeffe y Mark, Birmingham 2017 (paper300) | P | 2/1/1/1 | [S] (PDF ilegible por fetch; solo lo que dijo el buscador: corpus de 55 millones de palabras, más de 200.000 exámenes) | https://www.birmingham.ac.uk/documents/college-artslaw/corpus/conference-archives/2017/general/paper300.pdf |
| 1d | Liu y Qin (2024), "The effectiveness of cognitive linguistics-inspired language pedagogies: a systematic review", *Modern Language Journal* 108(4): 794-814 | P | 3/2/1/3 | [S] (abstract vía buscador, no verificado en la editorial) | https://x-mol.com/paper/1849913055255535616 |
| 1e | Qin, Liu y Lei (2024), "Cognitive linguistics-inspired language instruction", *Language Teaching* 57(4): 478-500 (Research Timeline) | P | 3/1/1/2 | [M] | https://cambridge.org/core/journals/language-teaching/article/cognitive-linguisticsinspired-language-instruction/DEC3783A3777E66104B72B8B74ADA4C1 |
| 1f | Spada y Tomita (2010), meta-análisis de 41 estudios, *Language Learning* 60(2): 263-308 | P | 3/2/1/3 | [M] vía buscador | https://www.eas.utoronto.ca/node/790 |

### Afirmaciones

- El EGP tiene "over 1,200" estructuras gramaticales (en el abstract de 1b, "over 1,200 structure-level mappings derived from largely manual analysis of learner corpora") derivadas del Cambridge Learner Corpus (CLC) y asignadas a uno de los seis niveles del MCER. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8323F1AD466EF982EA47DEFBB0D740D5/S0267190525100093a.pdf/nlp-powered-quantitative-verification-of-the-english-grammar-profiles-structure-level-assignment.pdf [L]
- Criterios de O'Keeffe y Mark para dar una estructura por "adquirida" en un nivel (según 1b): frecuencia superior a la del British National Corpus, 60 % de usos correctos sintáctica y pragmáticamente, uso por una gama amplia de hablantes de distintas familias de lenguas, y aparición en varios contextos y tareas. Misma URL [L].
- El CLC tiene 55 millones de palabras y más de 200.000 exámenes (dato de la ficha de conferencia, no verificado en el PDF). https://www.birmingham.ac.uk/documents/college-artslaw/corpus/conference-archives/2017/general/paper300.pdf [S]
- **Discrepancia sobre la validez de los niveles.** Verratti-Souto et al. rehicieron la asignación de niveles con estadística sobre EFCAMDAT (otro corpus, de un curso en línea): solo 124 de las estructuras informativas (32,80 %) mostraron frecuencia significativamente mayor en su nivel EGP que en el anterior, y el acuerdo ponderado fue kappa = 0,193 ("slight agreement" según Landis y Koch). El acuerdo fue mayor en niveles bajos; "this was not the case for the CEFR B and C levels". Reconocen que EFCAMDAT es distinto del CLC (textos de curso contra redacciones de examen) y que su método no mide corrección. Misma URL [L]. Conclusión práctica: el EGP sirve como mapa orientativo de qué estructuras aparecen más en B2/C1/C2, no como lista cerrada de "esto es C1".
- Otro inventario (CIGE) también tuvo baja validación: solo 47 % de los ítems mostró evidencia suficiente del nivel asignado (Jones 2015, citado en 1b). Misma URL [L].
- Pedagogía: una revisión sistemática de 62 estudios encuentra efectivas las pedagogías "inspiradas en lingüística cognitiva" en 58 de 62 (93,5 %); la gramática es el objetivo principal. https://x-mol.com/paper/1849913055255535616 [S]. Cautela: en el buscador se señaló que la mayor parte es sobre construcciones de poco esquema (preposiciones, verbos frasales) y pocos estudios sobre cláusulas como los condicionales; y que otra revisión (Martín-Gascón 2024) dice que la evidencia empírica sigue siendo escasa. Ninguno de los dos pasajes fue verificado en texto completo. Es un conteo de vote-counting, no un tamaño de efecto.
- La instrucción explícita rinde más que la implícita tanto con rasgos simples como complejos (Spada y Tomita 2010, 41 estudios). https://www.eas.utoronto.ca/node/790 [M]. Norris y Ortega (2000), d≈1,13 explícita contra d≈0,54 implícita, ya está en el vistazo (https://core.ac.uk/download/201198976.pdf) y no se reverificó acá.

### Recurso canónico propuesto
- Para saber qué existe en cada nivel: **EGP online** (englishprofile.org, sección English Grammar Profile) filtrado por B2/C1/C2 y por categoría. Fijarse en los enunciados "can-do" con ejemplo real de alumno, no en el nivel como verdad exacta (ver 1b). Hueco: no pude leer el sitio.
- Para entender qué hacen los aprendices con eso: 1b (resumen de límites del EGP).

---

## 2. Tiempo y aspecto

### Fuentes

| # | Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|---|
| 2a | Leech, *Meaning and the English Verb* (3.ª ed., 2004) | P | 3/3/3/3 | [S] (ficha de editorial) | https://www.routledge.com/Meaning-and-the-English-Verb/Leech/p/book/9780582784574 |
| 2b | Bardovi-Harlig (2000), *Tense and Aspect in Second Language Acquisition* | P | 3/3/2/3 | [M] (ficha) | https://dsls.indiana.edu/research/publications/2000-tesne-bardovi-harlig.html |
| 2c | Bardovi-Harlig y Comajoan-Colomé (2020), "The aspect hypothesis and the acquisition of L2 past morphology in the last 20 years", *SSLA* 42(5): 1137-1167 | P | 3/3/1/3 | [M] (abstract) | https://www.cambridge.org/core/journals/studies-in-second-language-acquisition/article/abs/aspect-hypothesis-and-the-acquisition-of-l2-past-morphology-in-the-last-20-years/353744B9E21B7B88989CD96A45E3B87F |
| 2d | Bardovi-Harlig y Comajoan-Colomé (2022), *Language Teaching* 55(3): 289-345, reseña de la instrucción en tiempo-aspecto L2 | P | 3/3/1/3 | [M] (abstract; texto completo no disponible) | https://cambridge.org/core/services/aop-cambridge-core/content/view/S026144482200009X |
| 2e | Thane (2018), revisión crítica de la hipótesis del aspecto | S | 2/2/1/1 | [S] | https://dergipark.org.tr/en/download/article-file/542755 |
| 2f | Benhamlaoui (2021), tesis doctoral, Essex, enseñanza basada en conceptos de tiempo y aspecto (argelinos) | P (tesis) | 1/2/2/2 | [S] | https://repository.essex.ac.uk/29952/3/BENHAMLAOUI%20Maroua%20PhD%20Thesis%20CBI%20for%20Enhancing%20Understanding%20and%20Use%20of%20English%20Tense%20and%20Aspect%20Markers%20by%20Algerian%20Learners%20of%20L2%20English.pdf |

Nota: el vistazo y mi primera lectura confundían la autoría de 2d; la reseña de 2022 es de Bardovi-Harlig **y Comajoan-Colomé**, no de Bardovi-Harlig sola (el buscador la había atribuido a ella sola).

### Afirmaciones
- La hipótesis del aspecto es, según el abstract de 2c, "the most tested hypothesis in L2 temporality research"; el artículo revisa 20 años de pruebas empíricas y cuatro variables (no verifiqué cuáles ni sus conclusiones: texto completo bloqueado). [M]
- La reseña de instrucción de 2022 cubre 56 estudios de efecto instruccional y 38 propuestas pedagógicas (2000-2021) y concluye que "there are clear attempts to establish connections between research and practice" pero que los estudios no dialogan de manera consistente con la literatura de adquisición de tiempo-aspecto. https://cambridge.org/core/services/aop-cambridge-core/content/view/S026144482200009X [M]
- La crítica de Thane y de Salaberry indica que la capacidad predictiva de la hipótesis varía con la L1 y el nivel; Salaberry (2021) revisa propuestas que la extienden a aprendices intermedios y avanzados. https://dergipark.org.tr/en/download/article-file/542755 [S]; https://revistas.ucm.es/index.php/CLAC/article/download/76709/4564456558603/4564456624025 [S]. **Relevancia para este lector**: la hipótesis fue formulada para etapas tempranas de la morfología del pasado; para un B2 estancado en la elección del tiempo, la evidencia directa es escasa (hueco).
- Instrucción basada en conceptos (CBI): de una tesis solo recuperé que "revealed the effectiveness of the CBI model over traditional instruction" para pasado simple, pasado continuo y present perfect, con aprendices argelinos. https://repository.essex.ac.uk/29952/3/BENHAMLAOUI%20Maroua%20PhD%20Thesis%20CBI%20for%20Enhancing%20Understanding%20and%20Use%20of%20English%20Tense%20and%20Aspect%20Markers%20by%20Algerian%20Learners%20of%20L2%20English.pdf [S]. Es una tesis, sin pares, sin muestra citada: evidencia débil.
- Errores de tiempo en hispanohablantes: la hoja de errores de Cambridge dice que "use of present tenses instead of past tenses (and vice versa)" es el segundo error gramatical más común de los aprendices con L1 español y "it is high for Spanish learners in comparison to other first languages"; las palabras más confundidas son *had*, *was* y *would*. Ejemplos literales: "I buy bought a new bed because the other bed was very old". https://www.cambridge.org/elt/blog/wp-content/uploads/2020/03/Spanish.pdf [L]. Limitaciones: es una hoja de enseñanza "supplied by the language research team at Cambridge University Press", sin cifras ni método; los ejemplos mencionan España, no el Río de la Plata.
- Contraste con el castellano rioplatense, ver sección 3.

### Recurso canónico propuesto
- **Leech, *Meaning and the English Verb*, capítulos de presente/pasado simple, aspecto progresivo y expresiones de pasado y futuro.** Es la descripción del significado de cada forma (por qué), corta (unas 150 páginas). Fijarse en cómo reduce cada forma a un significado básico (por ejemplo, el progresivo como "temporalidad limitada") y en las listas de verbos de estado. Se usa para el modelo mental de las 12 combinaciones. [S, no leído]
- Para práctica con evidencia: no hay un recurso canónico verificado (ver Huecos).

---

## 3. Present perfect

### Fuentes

| # | Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|---|
| 3a | Perez-Guerra y Smirnova (2024), "L1 Influence on the Use of the English Present Perfect", *Journal of Language and Education* 10(1): 101-114 | P | 2/3/3/3 | [L] | https://jle.hse.ru/article/download/16720/18643 |
| 3b | Araújo (2019), "O impacto da referência temporal de passado sobre o uso do pretérito perfeito em Buenos Aires", *Revista Linguística* 15(2): 148-177 | P | 2/3/3/3 | [L] | https://revistas.ufrj.br/index.php/rl/article/download/21330/18977/88850 |
| 3c | Fuchs y Gonzalez Gonzalez (2022), "Perfect-perfective variation across Spanish dialects: a parallel-corpus study", *Languages* 7(3): 166 | P | 2/2/1/2 | [M] | https://doi.org/10.3390/languages7030166 |
| 3d | Fløgstad (2016), *Preterit Expansion and Perfect Demise in Porteño Spanish and Beyond*, Brill | P | 3/3/2/3 | [S] | https://library.oapen.org/bitstream/20.500.12657/38097/1/9789004309081_webready_content_text.pdf |
| 3e | Sheen (1992), "Variation between simple past and present perfect and its pedagogical implications", *JALT Journal* 14(2) | P | 2/1/1/2 | [M] | https://jalt-publications.org/jj/articles/2858-variation-between-simple-past-and-present-perfect-and-its-pedagogical-implications |
| 3f | Wynne (2000), tesis de Stirling, present perfect en inglés americano y británico (corpus de 5,5 millones de palabras) | P (tesis) | 1/2/1/2 | [S] (supera el límite de descarga) | https://www.storre.stir.ac.uk/bitstream/1893/3472/1/Wynne%20%282000%29%20-%20The%20present%20perfect%20-%20a%20corpus-based%20investigation.pdf |
| 3g | Yao (2024), libro sobre present perfect y pretérito en inglés tardomoderno y actual (reseña en De Gruyter) | P | 2/2/1/2 | [S] | https://www.degruyterbrill.com/document/doi/10.1515/flin-2025-2023/html |

### Afirmaciones
- **Rioplatense: el pretérito perfecto compuesto casi no se usa.** En 551 casos de entrevistas radiales de Buenos Aires, 499 (91 %) fueron pretérito simple (*estudié*) y 52 (9 %) compuesto (*he estudiado*). Dentro del "antepresente" (pasado conectado con el presente), el compuesto fue 0 % en el inmediato, 13 % en el específico (11 de 83) y 45 % en el ampliado (33 de 74). "Em nenhum dos valores possíveis predomina o PPC". Con verbos estativos el compuesto sube a 58 %. https://revistas.ufrj.br/index.php/rl/article/download/21330/18977/88850 [L]
- Trabajos previos de Araújo citados en 3b: Buenos Aires tiene la menor frecuencia de compuesto del país (6 %), contra Patagonia 7 %, Noreste 9 %, Litoral 10 %, Cuyo 15 %, Noroeste 25 %, Centro 28 %. En Buenos Aires el compuesto expresa sobre todo resultado (55 %) y experiencia (25 %). Misma URL [L]. (Cifras de segunda mano dentro del paper.)
- Fløgstad sostiene que el pretérito se expande y el perfecto desaparece ("preterit expansion and perfect demise"); Rodríguez Louro (2009) dice que en el español bonaerense las funciones del perfecto (resultado, continuidad, relevancia actual, noticias) las cubre hoy el pretérito. https://library.oapen.org/bitstream/20.500.12657/38097/1/9789004309081_webready_content_text.pdf [S]; cita de Rodríguez Louro en nota 22 de https://revistas.ufrj.br/index.php/rl/article/download/21330/18977/88850 [L].
- **Discrepancia** (castellano): hay registro de que el compuesto tiene algo de prestigio en el registro formal bonaerense (Rodríguez Louro 2008, citado en 3b) y de que en Tucumán se usa más que en Buenos Aires. Es decir, el rioplatense no es un bloque. Misma URL [L].
- Un estudio paralelo comparó Madrid, Ciudad de México y Buenos Aires: el rioplatense "systematically defaults to the Pretérito Indefinido" donde el peninsular usa el compuesto, aunque ambos dialectos tienden al compuesto en contextos continuativos. https://doi.org/10.3390/languages7030166 [M/S]; una reseña cuestionó si las traducciones de Madrid y Buenos Aires representan a cada dialecto. Evidencia más débil.
- **Hispanohablantes aprendiendo inglés: sobreuso, no subuso, pero con hablantes de España.** En ensayos universitarios, los aprendices españoles (WriCLE, 801.000 palabras, 716 textos) usaron el present perfect 423,41 veces por 100.000 palabras, contra 322,22 de los nativos (LOCNESS) y 115,13 de los rusos; razón PP/verbos 0,032 contra 0,019 y 0,007. Los españoles y los rusos tuvieron tasa de error casi idéntica; los errores se atribuyen a "challenges in comprehending the functions of the PP and in distinguishing its semantics from those of other English tenses, particularly the Past Simple". Los autores ven transferencia positiva en la frecuencia y transferencia negativa en la sobregeneralización de adverbios compatibles con PP y en la subgeneralización de contextos de relevancia. https://jle.hse.ru/article/download/16720/18643 [L]
- **Límite crítico**: 3a es lengua escrita de estudiantes de España, de un dialecto que usa mucho el compuesto. **No encontré ningún estudio que mida el present perfect de hablantes rioplatenses de inglés** (hueco). La hipótesis de este informe (que un rioplatense tiende a usar pasado simple donde el inglés quiere present perfect) es una predicción razonable a partir de 3b, no un resultado.
- Americano contra británico: varios estudios encuentran menor frecuencia del present perfect en inglés americano (Elsness 1997; Hundt y Smith 2009, citados en el resumen del buscador); Sheen (1992) estimó que "approximately 80 percent of prescribed uses of the present perfect" en inglés norteamericano pueden alternar con el pasado simple, con menos variación en inglés británico. https://jalt-publications.org/jj/articles/2858-variation-between-simple-past-and-present-perfect-and-its-pedagogical-implications [M]. Sheen es de 1992 y su método no se leyó; Yao (2024) encuentra que la especificación temporal, la negación y el presente simple previo predicen el present perfect en ambas variedades. https://www.degruyterbrill.com/document/doi/10.1515/flin-2025-2023/html [S]. Implicación práctica a verificar: para un rioplatense que aprende inglés americano, la brecha de transferencia es menor de lo que parece, pero no desaparece (los contextos "hasta ahora / ever / yet / for-since" siguen pidiendo present perfect).
- Instrucción específica del present perfect: Finger y Vasques (2010, brasileños, tres semanas) y Alfraikh (tesis de Leeds, 2022; 41 estudiantes, 29 y 12) hallaron mejoras con instrucción explícita, pero con efectos que decaen y diseños chicos. https://scielo.br/j/rbla/a/B5vw8KnKDCD8QqWDSSdn8fx/abstract/?lang=en [S]; https://etheses.whiterose.ac.uk/id/eprint/35403/1/ThesisClean2.pdf [S]. Evidencia débil.

### Recurso canónico propuesto
- **Swan, *Practical English Usage* (4.ª ed., OUP, 2016), entradas "present perfect" y "past simple vs present perfect" y la sección de diferencias americano/británico.** Es el más citado por docentes (OUP dice que vendió más de 2 millones de ejemplares). Fijarse en las listas de adverbios compatibles y en las notas de uso americano. https://eltpreprod.oup.com/catalogue/items/global/grammar_vocabulary/practical_english_usage_4th_edition [S, no leído]. Para el por qué, Leech (2a).
- Para el modelo mental del contraste con el castellano rioplatense: 3b (tablas 1-2) como evidencia de que el hablante rioplatense ya divide "pasado conectado" y "pasado cerrado" casi sin morfología, que es la base para enseñar el inglés por significado y no por equivalencia.

---

## 4. Futuro

### Fuentes

| # | Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|---|
| 4a | Engel y Szmrecsanyi (2022/2023), "Variable grammars are variable across registers: future temporal reference in English", *Language Variation and Change* | P | 3/2/2/3 | [S] | https://dx.doi.org/10.1017/S0954394522000163 |
| 4b | Dubois, Paquot, Szmrecsanyi et al. (2024), will contra be going to según nivel, Trinity Lancaster Corpus (3.616 casos) | P | 2/2/1/3 | [S] | https://research.dial.uclouvain.be/entities/publication/b00bd39b-5666-4b8c-ab0a-6aa9b7b4ebb8 |
| 4c | Szmrecsanyi (2003) (alternancia sensible a la complejidad sintáctica), citado en 4b | P | 3/2/1/2 | [S] | misma URL de 4b |

### Afirmaciones
- La elección entre *will* y *be going to* depende del registro: Engel y Szmrecsanyi analizaron unos 2.600 casos en conversación, debates parlamentarios, blogs y diarios más un experimento de aceptabilidad. https://dx.doi.org/10.1017/S0954394522000163 [S]
- Szmrecsanyi (2003), con datos hablados británicos y americanos, encontró que la alternancia es sensible a la complejidad sintáctica. https://research.dial.uclouvain.be/entities/publication/b00bd39b-5666-4b8c-ab0a-6aa9b7b4ebb8 [S]
- Los estudios sobre aprendices se centraron históricamente en la L1, ignorando el nivel; 4b incorpora el nivel con 3.616 casos del Trinity Lancaster Corpus. Misma URL [S].
- *be going to* es más frecuente en el habla informal y *will* en contextos independientes del BNC (Chuang 2022, PACLIC). https://aclanthology.org/2022.paclic-1.37.pdf [S]

### Recurso canónico propuesto
- **Leech, *Meaning and the English Verb*, capítulo "expressions of past and future time"** (por qué), y **Swan PEU entrada "future"** (cuándo). Ningún recurso verificado para los usos de future continuous / future perfect / be about to (ver Huecos). No leído.

---

## 5. Condicionales e hipótesis

### Fuentes

| # | Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|---|
| 5a | Leech, Hundt, Mair y Smith (2009), *Change in Contemporary English*, capítulo "Subjunctive mood" | P | 3/3/2/3 | [S] | https://resolve.cambridge.org/core/books/abs/change-in-contemporary-english/subjunctive-mood/665D2B8E2F225BB790783C98EA8375C8 |
| 5b | Rohdenburg y Schlüter (eds.), *One Language, Two Grammars?*, capítulo sobre el subjuntivo condicional | P | 3/2/1/2 | [S] (índice) | https://cambridge.org/core/books/one-language-two-grammars/conditional-subjunctive/D4DE0AE94935961A47F6040B9574FB04 |
| 5c | Estudio de *wish*/*if only* con COCA y COHA (revista *RAEI*) | P | 2/2/2/2 | [S] | https://raei.ua.es/article/view/29561 |

### Afirmaciones
- El pasado subjuntivo (*were*) se usa en condicionales y concesivas y tras *wish* y *suppose*; solo se distingue de *was* en primera y tercera persona del singular; *was* es más común en estilo menos formal. https://www.uni-marburg.de/de/fb10/iaa/institut/personen/ruehlemann/was-were-alternation.pdf [S]
- El inglés americano lidera el "renacimiento" del subjuntivo mandativo (*I suggest he go*) (Övergaard 1995, Hundt 1998, citados por un artículo de Diacronia). https://www.diacronia.ro/indexing/details/A23986/pdf [S]
- *Wish* e *if only* se usan en variación libre para un deseo improbable o imposible (estudio con COCA/COHA). https://raei.ua.es/article/view/29561 [S]
- Un error esperado en hispanohablantes (poner "would" en ambas mitades porque el castellano usa condicional en la apódosis y subjuntivo en la prótasis) **aparece solo en un sitio de enseñanza (elon.io), en la dirección inglés-a-español**, no hay estudio de hispanohablantes aprendiendo inglés. Es hueco, no hallazgo.

### Recurso canónico propuesto
- **Swan PEU, entradas "conditional sentences" y "wish/if only"**, y **Hewings, *Advanced Grammar in Use* (4.ª ed., 2023; 105 unidades, nivel C1-C2)**, unidades de condicionales mixtos y de "unreal" para práctica graduada. https://cambridge.es/en/catalogue/grammar-vocabulary-and-pronunciation/grammar/advanced-grammar-in-use-4 [S, no leído; no encontré qué unidades son]. Para saber qué usan de verdad los nativos con *were/was* y el subjuntivo mandativo: 5a.

---

## 6. Modales

### Fuentes

| # | Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|---|
| 6a | Collins (2009), *Modals and Quasi-modals in English*, Rodopi | P | 3/3/2/3 | [S] | https://www.jbe-platform.com/content/books/9789027289407-veaw.g39.05col |
| 6b | Blog de OUP "Modal verbs: has their use declined?" | S | 1/1/1/1 | [S] | https://learningenglishwithoxford.oup.com/2020/08/27/modal-verbs/ |

### Afirmaciones
- Hay un aumento de los cuasi-modales y descenso de los modales, y el inglés americano suele ir primero (resumen de un capítulo de Collins). https://benjamins.com/catalog/silv.2.12col [S]
- En corpus británicos *must* cayó -29,1 % en escrito y -54,2 % en hablado entre los años 60 y los 90; el blog propone que *have to* y *need to* lo reemplazan (interpretación, no medida). https://learningenglishwithoxford.oup.com/2020/08/27/modal-verbs/ [S]
- No encontré ningún estudio de hispanohablantes con modales en perfecto (*should have*, *must have*, *could have*), ni datos del CLC para L1 español.

### Recurso canónico propuesto
- **Leech, capítulos "primary modal auxiliaries" y "modality"** (por qué) + **Collins 2009** si hace falta la frecuencia real. **Hewings, unidades de modales** para práctica. No leído.

---

## 7. Pasiva y causativa

### Fuentes

| # | Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|---|
| 7a | Biber, Johansson, Leech, Conrad y Finegan (1999), *Longman Grammar of Spoken and Written English*, 1.204 págs.; corpus de 40 millones de palabras, 37.000 textos | P | 3/3/3/3 | [S] (reseña) | https://www.anglistik.uni-muenchen.de/personen/professoren/schmid/schmid_publ/review_biber_et_al.pdf |
| 7b | Rothman et al. (2016), adquisición de pasivas inglesas por niños de L1 español | P | 2/2/1/2 | [S] | https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2C19187B245C15F6E1472803A179A363/S0305000915000549a.pdf/older-age-of-onset-in-child-l2-acquisition-can-be-facilitative-evidence-from-the-acquisition-of-english-passives-by-spanish-natives.pdf |

### Afirmaciones
- LGSWE fue diseñada con cuatro registros (conversación, ficción, prensa, prosa académica) en inglés americano y británico, con frecuencias normadas por millón de palabras. https://www.anglistik.uni-muenchen.de/personen/professoren/schmid/schmid_publ/review_biber_et_al.pdf [S]. No obtuve cifras de pasivas ni de *get*-pasivas por registro: **hueco**; es el lugar para buscarlas.
- El castellano tiene una pasiva refleja (*se vende*) más frecuente que la perifrástica (dato de un estudio de pasivas en L2 español; secundaria). https://core.ac.uk/download/369756901.pdf [S]. No hay estudio de adultos hispanohablantes con pasivas inglesas, ni con *have/get something done* ni con "it is said that".

### Recurso canónico propuesto
- **Biber et al. (LGSWE), capítulo de voz pasiva y tabla de frecuencia por registro**, para decidir cuándo conviene la pasiva (académico, prensa) y cuándo no (conversación). Fijarse en la tabla agentless contra by-agent. No leído por mí; es la fuente adecuada. Alternativa práctica: Swan PEU "passive" y Hewings.

---

## 8. Artículos

### Fuentes

| # | Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|---|
| 8a | Ionin, Montrul y Crivos (2013), "A bidirectional study on the acquisition of plural noun phrase interpretation in English and Spanish", *Applied Psycholinguistics* 34(3): 483-518 | P | 3/2/2/3 | [M] | https://cambridge.org/core/journals/applied-psycholinguistics/article/bidirectional-study-on-the-acquisition-of-plural-noun-phrase-interpretation-in-english-and-spanish/19F32790A129950D989EF3CA0366A49E |
| 8b | Capítulo "Article choice by Spanish L2 learners of English: evidence for full transfer of the definiteness parameter" (*Language Acquisition and Language Disorders* 49) | P | 2/2/1/3 | [S] (autores no confirmados) | https://laslab.org/book_chapter/article-choice-by-spanish-l2-learnes-of-english-evidence-for-full-transfer-of-the-definiteness-parameter |
| 8c | Snape (2013), generic reference de aprendices españoles, turcos y japoneses, *Int. J. of English Studies* | P | 2/2/1/2 | [S] | https://revistas.um.es/ijes/article/download/138701/147991 |
| 8d | Hoja de errores de Cambridge para hispanohablantes | S | 2/1/2/1 | [L] | https://www.cambridge.org/elt/blog/wp-content/uploads/2020/03/Spanish.pdf |
| 8e | Ionin (2003), tesis MIT, hipótesis de la fluctuación | P | 3/3/2/3 | [S] | https://mitwpl.mit.edu/catalog/ioni01/ |

### Afirmaciones
- En castellano el plural definido puede ser genérico o específico; en inglés el genérico es plural sin artículo; en transferencia, hay efecto de la L1 "in both directions at lower proficiency levels", y mejora a niveles más altos. Los aprendices acertaron más con la gramaticalidad de los plurales sin artículo que con la interpretación correcta. https://cambridge.org/core/journals/applied-psycholinguistics/article/bidirectional-study-on-the-acquisition-of-plural-noun-phrase-interpretation-in-english-and-spanish/19F32790A129950D989EF3CA0366A49E [M]
- **Discrepancia sobre qué tan mal les va con artículos.** (i) Error típico de la L1: "I like the dogs" o "The patience is a virtue" por genéricos (Jaén; resumen de fuentes secundarias). https://creapre.ujaen.es/bitstreams/718b1563-960d-44bd-be86-7ad0abf57340/download [S]. (ii) Los hispanohablantes eligen *the* para definido y *a(n)* para indefinido de forma casi sistemática y no fluctúan entre definitud y especificidad (que sí hacen los de L1 sin artículos), lo que se interpreta como transferencia del sistema; mismo capítulo 8b [S]. (iii) Un estudio con avanzados en LINDSEI (oral) encontró "few errors in expressing definiteness", transferencia positiva dominante. Tesis de Padua citada por el buscador, no abierta. Interpretación: el sistema básico se transfiere bien; fallan los genéricos y las omisiones ante profesión (*She is engineer*), según fuentes secundarias.
- En la hoja de Cambridge los artículos **no** figuran entre los errores principales del hispanohablante; lo son preposiciones, tiempos y verbos léxicos. https://www.cambridge.org/elt/blog/wp-content/uploads/2020/03/Spanish.pdf [L]. Pero la hoja no tiene método ni cifras.
- Posesivos y partes del cuerpo (castellano usa artículo: *me lavo las manos*; inglés posesivo) y *su* para his/her/their: fuente solo secundaria (diapositivas basadas en Coe, en Swan y Smith). https://de.slideshare.net/kristenzadick/difficulties-for-spanish-speakers-learning-english [S]. Baja calidad.

### Recurso canónico propuesto
- **Swan y Smith, *Learner English* (2.ª ed., CUP, 2001), capítulo "Spanish" (Coe)**: es la lista de transferencia de referencia (artículos, sujeto, tiempos, preguntas, orden). Fijarse en la tabla de dificultades por área. No pude leer el capítulo; ficha: https://assets.cambridge.org/97805217/79395/excerpt/9780521779395_excerpt.pdf [M, ilegible]. Para práctica: Swan PEU "articles" y Hewings.

---

## 9. Estructuras avanzadas (inversión, cleft, relativos, nominalización)

### Fuentes

| # | Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|---|
| 9a | British Council LearnEnglish, "Emphasis: cleft sentences, inversion and auxiliaries" (C1) | S | 2/2/3/1 | [S] | https://learnenglish.britishcouncil.org/free-resources/grammar/c1/emphasis-cleft-sentences-inversion-auxiliaries |
| 9b | British Council, "Inversion after negative adverbials" | S | 2/2/3/1 | [S] | https://learnenglish.britishcouncil.org/free-resources/grammar/c1/inversion-after-negative-adverbials |
| 9c | Rankin (2025), negative inversion en avanzados germanohablantes, *Linguistic Approaches to Bilingualism* | P | 3/2/2/3 | [S] | https://www.jbe-platform.com/content/journals/10.1075/lab.24028.ran |

### Afirmaciones
- Los cleft se forman con *it* o con una cláusula con *what*; la inversión tras adverbial negativo agrega *do/does/did* si no hay auxiliar (*Little did I realise…*, *No sooner had we…*). https://learnenglish.britishcouncil.org/free-resources/grammar/c1/emphasis-cleft-sentences-inversion-auxiliaries [S]
- La inversión negativa sigue sin igualarse con la de nativos en avanzados germanohablantes (Rankin 2025). Es otra L1: no generaliza al español. https://www.jbe-platform.com/content/journals/10.1075/lab.24028.ran [S]
- No encontré estudios de cleft, relativos ni nominalización en hispanohablantes, ni datos de subuso de cleft en aprendices (hueco). Un resumen de EGP (tercero, Scribd) dice que lista cleft "Wh-" como C1; no verificable. https://www.scribd.com/document/511847239/Level-C1-Grammar-List-1 [S, baja calidad]

### Recurso canónico propuesto
- **Hewings, *Advanced Grammar in Use*, unidades de "emphasis", "inversion" y "relative clauses"** y **Swan PEU** para uso; para frecuencia y registro, LGSWE (sección de cláusulas relativas y dislocación). No leídos.

---

## 10. Sujeto obligatorio, orden y preguntas indirectas (propuesta: componente nuevo)

### Fuentes

| # | Fuente | Tipo | A/P/E/U | Marca | URL |
|---|---|---|---|---|---|
| 10a | White (1985, 1986), Davies (1996), Phinney (1987), Platt (1989): sujeto nulo en hispanohablantes aprendiendo inglés (según revisión) | P | 2/2/1/3 | [S] | https://eprints.whiterose.ac.uk/97341/1/paper2991.pdf ; https://www.ideals.illinois.edu/items/21943 |
| 10b | Escutia (2002), preguntas indirectas de aprendices españoles | P | 2/2/2/3 | [S] | https://revistas.ucm.es/index.php/CLAC/article/download/92038/4564456567115/4564456690220 |
| 10c | "Second language acquisition of English questions: an elicited production study", *Applied Psycholinguistics* (chinos y españoles) | P | 3/2/2/3 | [S] | https://resolve.cambridge.org/core/journals/applied-psycholinguistics/article/abs/second-language-acquisition-of-english-questions-an-elicited-production-study/DEA15C5C9B89E28B45A244E66FE3CDF9 |

### Afirmaciones
- Los hispanohablantes aceptaron oraciones sin sujeto al principio; la aceptación baja con el nivel. Los sujetos expletivos (*it is*, *there is*) persisten más, incluso en avanzados ("underlying [+prodrop] grammar"); Phinney (1987) encontró más omisión de expletivos que de sujetos referenciales en redacciones. https://eprints.whiterose.ac.uk/97341/1/paper2991.pdf [S]. Platt (1989): demora en reajustar el parámetro por suponer que el inglés es una lengua de concordancia. https://www.ideals.illinois.edu/items/21943 [S]. Datos de los años 80 y escritos; para un B2 que habla, el efecto probablemente es menor, pero no hay dato.
- Preguntas indirectas: los aprendices españoles tratan las subordinadas interrogativas como directas (*Do you know where is he?*). Escutia lo vincula a la preferencia castellana por inversión en subordinadas. https://revistas.ucm.es/index.php/CLAC/article/download/92038/4564456567115/4564456690220 [S]. **Discrepancia**: el estudio de 10c con chinos y españoles halló que la L1 no predecía la producción; las propiedades del inglés sí, y hubo más inversión no estándar en wh- subordinadas que en sí/no. https://resolve.cambridge.org/core/journals/applied-psycholinguistics/article/abs/second-language-acquisition-of-english-questions-an-elicited-production-study/DEA15C5C9B89E28B45A244E66FE3CDF9 [S].
- Preposiciones: error gramatical nº 1 en hispanohablantes según la hoja de Cambridge (*in*, *at*, *on* más omitidas). https://www.cambridge.org/elt/blog/wp-content/uploads/2020/03/Spanish.pdf [L].
- Orden de adjetivos y adverbios: ningún resultado (hueco).

### Recurso canónico propuesto
- Swan y Smith, cap. "Spanish" (sección de sintaxis) y Swan PEU "adjectives: order", "questions: indirect". No leídos.

---

## 11. Mapa de fuentes: lo que se pudo confirmar de las obras de referencia

| Obra | Dato verificado | URL | Marca |
|---|---|---|---|
| Swan, *Practical English Usage*, 4.ª ed., OUP 2016 | Más de 2 millones de ejemplares vendidos (dato de OUP). Edición impresa y en línea | https://eltpreprod.oup.com/catalogue/items/global/grammar_vocabulary/practical_english_usage_4th_edition | [S] |
| Biber et al., LGSWE (1999) | 1.204 págs., corpus de 40 millones de palabras, cuatro registros, frecuencias por millón | https://www.anglistik.uni-muenchen.de/personen/professoren/schmid/schmid_publ/review_biber_et_al.pdf | [S] |
| Huddleston y Pullum, *CGEL* (2002) | No verificado: la página de Cambridge dio error 500 | (sin URL válida) | no leído |
| Leech, *Meaning and the English Verb*, 3.ª ed. | Contenido por capítulos; la 3.ª ed. suma contraste americano/británico. Discrepancia de editorial y de páginas entre fichas (152 contra 141) | https://www.routledge.com/Meaning-and-the-English-Verb/Leech/p/book/9780582784574 | [S] |
| Hewings, *Advanced Grammar in Use*, 4.ª ed. | CUP, 23 de marzo de 2023, 105 unidades, 320 págs., nivel C1-C2, ISBN 9781108920216 | https://cambridge.es/en/catalogue/grammar-vocabulary-and-pronunciation/grammar/advanced-grammar-in-use-4 | [S] |
| Swan y Smith, *Learner English* | El capítulo del español no se pudo leer; lo que se cita viene de una hoja de Cambridge y de resúmenes secundarios | https://assets.cambridge.org/97805217/79395/excerpt/9780521779395_excerpt.pdf | [M] |

Nota sobre fuentes duplicadas: las diapositivas de SlideShare y los sitios de enseñanza que aparecen en las búsquedas sobre errores de hispanohablantes parafrasean el capítulo de Coe en *Learner English*; cuentan como **una** fuente secundaria (la obra de Swan y Smith), no varias.

---

## Huecos

1. **EGP concreto**: no leí ni un solo enunciado B2, C1 o C2 (sitio JavaScript; PDF de O'Keeffe y Mark con 403). Falta saber, estructura por estructura, qué cae en cada nivel. Alternativa: abrir el EGP online a mano, o bajar el PDF desde un repositorio accesible.
2. **Present perfect en rioplatenses aprendiendo inglés**: ningún estudio. Todo lo disponible es de España (3a). La predicción de subuso o evitación es inferencia.
3. **Evidencia de métodos para elegir el tiempo verbal al hablar (L2 adulto, B2 a C1)**: solo hay tesis y estudios cortos (Finger y Vasques; Alfraikh; Benhamlaoui); los dos meta-análisis generales (Norris y Ortega; Spada y Tomita) no son específicos de tiempo-aspecto. El texto completo de la reseña de 2022 (56 estudios) no se pudo leer; es la fuente a conseguir.
4. **Gramática cognitiva aplicada**: solo abstracts [S/M]; el conteo 58 de 62 no es un tamaño de efecto, y falta el contenido de cada intervención.
5. **Condicionales, modales (perfecto), pasiva, causativa, cleft y relativos con hispanohablantes**: sin estudios específicos. Los números de frecuencia y de dificultad de LGSWE y del CLC no se alcanzaron.
6. **Futuro** (future continuous, future perfect, *be about to*): sin ninguna fuente sobre cómo elegir ni sobre errores de hispanohablantes; solo variación will/going to.
7. **Orden de adjetivos y adverbios**: sin resultados.
8. **Huddleston y Pullum**: sin verificar (la página dio error); la afirmación de que el inglés no tiene futuro morfológico queda sin URL.
9. **Swan y Smith, capítulo "Spanish"**: no leído; la hoja de Cambridge no dice de qué corpus ni de qué muestra sale (se asume CLC, no lo declara).
10. **Diferencias americano/británico**: Sheen es de 1992 y los resúmenes de Elsness, Hundt y Smith son de segunda mano; Wynne (5,5 millones de palabras) no se pudo abrir.
