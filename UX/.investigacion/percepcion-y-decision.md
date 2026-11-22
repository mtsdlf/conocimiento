# Investigación: Percepción y decisión

Ángulo: cómo ve, recuerda y decide la gente frente a una pantalla. Componentes: modelo-mental, carga-cognitiva, leyes-de-fitts-y-hick, patron-oscuro.

Marcas: [L] leí el texto completo o la sección central; [M] metadatos o abstract; [S] resumen secundario o del buscador. Puntajes 1 a 3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U). Tipo: P = primaria, S = secundaria.

## Notas sobre la división del árbol

1. **Fitts y Hick juntos no es una división del campo.** Fitts es control motor (cuánto tarda un movimiento apuntado); Hick es decisión (cuánto tarda elegir entre alternativas). Juntos aparecen en la literatura de practicantes (por ejemplo, los "Laws of UX") y en el artículo de Liu et al. 2020, que los compara. Sirven como nota única, pero conviene que la nota separe las dos leyes y diga que la de Hick es la débil en diseño de interfaces (ver componente 3).
2. **Patrón oscuro no es solo percepción y decisión.** El campo lo trata como ética del diseño, derecho del consumidor y ciencias del comportamiento a la vez (Gray 2018, Mathur 2021, FTC, DSA). La nota tendrá que enlazar a Evaluación o a Fundamentos para la ética, y a Marketing para la persuasión del mensaje (que el brief deja fuera).
3. **Gestalt: las fuentes de UX la ponen en diseño visual, no acá.** NN/g llama a la proximidad "a foundational principle in visual design" y la aplica a layout, espaciado, secciones de formularios y responsive (https://www.nngroup.com/articles/gestalt-proximity/ [L]). Las fuentes de psicología sí la tratan como percepción, pero ninguna de las que leí la lista bajo "percepción y decisión". Recomendación: la teoría y las reglas de agrupamiento van en `Diseno-visual/jerarquia-visual`, y esta vertical la enlaza una sola vez como "la base perceptual". Si el árbol conserva el nombre "Percepción", conviene una frase que diga que la percepción visual se trata en diseño visual y que acá se trata la parte cognitiva.
4. **Mental model y carga cognitiva se solapan** (el modelo mental correcto baja la carga extrínseca; reconocer en vez de recordar es una heurística de Nielsen). No es un problema, pero las notas deben enlazarse entre sí.

---

## 1. modelo-mental

### Fuentes

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| NN/g, "Mental Models" (Megan Chan, 26-ene-2024; actualiza un texto de Nielsen de 2010) | S | [L] | 2/1/2/1 | https://www.nngroup.com/articles/mental-models/ |
| NN/g, "The Two UX Gulfs: Evaluation and Execution" (Kathryn Whitenton, 11-mar-2018) | S | [L] | 2/2/2/2 | https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/ |
| Norman, *The Design of Everyday Things* (ed. 2013), cap. "The System Image" | P (libro) | [S] (solo por diapositivas de curso y el índice; no lo leí) | 3/3/3/3 | https://courses.cs.washington.edu/courses/cse440/17au/slides/lecture/l06-doet.pdf |
| NN/g, "Recognition vs. Recall" (Raluca Budiu, 15-ene-2024) | S | [L] | 2/1/2/1 | https://www.nngroup.com/articles/recognition-and-recall/ |

### Afirmaciones

- NN/g define: un modelo mental es "what the user believes about the system (web, application, or other kind of product) at hand". El artículo no cita a Norman ni usa "conceptual model". https://www.nngroup.com/articles/mental-models/
- Los diseñadores arman modelos mentales detallados de lo que crean, por eso creen que cada función es fácil de entender; los de los usuarios suelen ser menos desarrollados y los llevan a errores. Misma URL.
- Los dos "golfos" (execution y evaluation) fueron acuñados en 1986 por Hutchins, Hollan y Norman, y Norman los explicó después en *The Design of Everyday Things*. NN/g: golfo de evaluación = entender el estado del sistema; golfo de ejecución = decidir y hacer la acción para llegar a un objetivo. Recomienda cerrarlos con un "transparent conceptual model". https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/
- Terminología de las diapositivas (que la atribuyen a Cooper, no a Norman): modelo de implementación, modelo manifiesto o imagen del sistema, y modelo mental. https://courses.cs.washington.edu/courses/cse440/17au/slides/lecture/l06-doet.pdf [S]
- El ciclo de Norman: establecer meta, formar intención, especificar la secuencia de acciones, ejecutar, percibir el estado, interpretar, evaluar. Misma URL [S].

### Discrepancia terminológica

Dos vocabularios conviven: Norman (modelo del diseñador / imagen del sistema / modelo del usuario) y Cooper (implementación / manifiesto / mental). NN/g usa un tercero (modelo mental vs. diseñador que conoce el producto). Hay que declararlo en la nota y no mezclarlos. La atribución exacta a Norman 2013 **no está verificada** con el libro.

### Recurso canónico

Norman, *The Design of Everyday Things*, ed. revisada 2013, cap. 1 (golfos y ciclo de acción) y cap. 2 (modelos conceptuales, imagen del sistema). Fijarse en el ciclo de siete etapas y en que el diseñador solo controla la imagen del sistema, no el modelo del usuario. Como puerta de entrada pública y corta: el artículo de NN/g sobre los dos golfos.

---

## 2. carga-cognitiva

### Fuentes

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| Miller 1956, "The Magical Number Seven, Plus or Minus Two", *Psychological Review* 63, 81-97 | P | [L] (copia en Classics in the History of Psychology) | 3/3/1/3 | https://psychclassics.yorku.ca/Miller/ |
| Cowan 2001, "The magical number 4 in short-term memory", *Behavioral and Brain Sciences* 24(1), 87-114 | P | [L] (abstract e introducción) | 3/3/1/3 | https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/magical-number-4-in-shortterm-memory-a-reconsideration-of-mental-storage-capacity/44023F1147D4A1D44BDC0AD226838496 (PDF de autor: https://memory.psych.missouri.edu/assets/doc/articles/2001/cowan-bbs-2001.pdf) |
| Sweller 1988, "Cognitive load during problem solving: effects on learning", *Cognitive Science* 12(2), 257-285 | P | [S] (solo abstract y resúmenes; PhilArchive dio 403) | 3/3/1/3 | https://dc2.philarchive.org/rec/SWECLD |
| Sweller, van Merriënboer y Paas 2019, "Cognitive Architecture and Instructional Design: 20 Years Later", *Educational Psychology Review* 31, 261-292 | P | [M] | 3/3/1/2 | https://link.springer.com/article/10.1007/s10648-019-09465-5 |
| NN/g, "Minimize Cognitive Load to Maximize Usability" (Whitenton, 22-dic-2013) | S | [L] | 2/1/2/1 | https://www.nngroup.com/articles/minimize-cognitive-load/ |
| NN/g, "Recognition vs. Recall" (Budiu, 2024) | S | [L] | 2/1/2/1 | https://www.nngroup.com/articles/recognition-and-recall/ |
| S. Walter, "Your navigation menu doesn't need Miller's 7±2 rule" (blog) | S, blog | [S] | 1/1/1/1 | https://stephaniewalter.design/blog/your-menu-doesnt-need-millers-7±2-rule/ |

### Afirmaciones

- Miller (1956): el límite de siete aplica a juicios unidimensionales ("this magical number seven applies to one-dimensional judgments"). "The number of bits of information is constant for absolute judgment" y "the number of chunks of information is constant for immediate memory". Resume: "Absolute judgment is limited by the amount of information. Immediate memory is limited by the number of items." El recodificado ("recoding") agrupa en menos chunks con más bits por chunk. https://psychclassics.yorku.ca/Miller/
- Cowan (2001), abstract literal: Miller "was meant more as a rough estimate and a rhetorical device than as a real capacity limit"; el límite real es "only three to five chunks"; "A single, central capacity limit averaging about four chunks is implicated". Hay cuatro condiciones para observarlo, entre ellas bloquear el recodificado. https://memory.psych.missouri.edu/assets/doc/articles/2001/cowan-bbs-2001.pdf
- Cowan dice además que lo central del artículo de Miller era el agrupamiento (chunking), no el número. Misma URL.
- NN/g define: "the cognitive load imposed by a user interface is the amount of mental resources that is required to operate the system". Carga intrínseca = esfuerzo de absorber información nueva y seguir la propia meta, no se elimina; carga extrínseca = procesamiento que usa recursos sin ayudar a entender el contenido (ejemplo: estilos de fuente decorativos). NN/g **no menciona la carga pertinente (germane)** ni cita a Sweller. https://www.nngroup.com/articles/minimize-cognitive-load/
- Sweller 1988 es citado como la primera descripción completa de la teoría; su abstract dice que los esquemas son el factor principal que distingue a expertos de novatos; la carga extrínseca viene de la búsqueda de diferencias entre estado actual y meta (análisis medios-fines); recomienda ejemplos resueltos. https://dc2.philarchive.org/rec/SWECLD [S]
- El marco de tres cargas (intrínseca, extrínseca, pertinente) es de Sweller, van Merriënboer y Paas 1998; la intrínseca se liga a la interactividad de elementos. El texto de 2019 revisa el marco, y una reseña posterior (Paas y van Merriënboer 2020, vista solo por el buscador) describe el procesamiento pertinente como recursos de la memoria de trabajo dedicados a la carga intrínseca. **No leí cómo la redefine exactamente.** https://link.springer.com/article/10.1007/s10648-019-09465-5 [M]
- Reconocer es más fácil que recordar: "Recognition is easier than recall because it involves more cues"; el menú es el ejemplo clásico de reconocimiento, el login el de recall. Es la heurística 6 de Nielsen. https://www.nngroup.com/articles/recognition-and-recall/
- Mal uso del 7±2: NN/g (según una cita en Medium, no leída directamente) dice que limitar menús a siete ítems por la memoria a corto plazo es un error común, porque un menú visible es una tarea de reconocimiento. https://stephaniewalter.design/blog/your-menu-doesnt-need-millers-7±2-rule/ [S, blog: solo pista]

### Disputa a declarar

- Cuántos chunks: Miller 7±2 (1956) frente a Cowan 4 (3 a 5) (2001). Las dos son de primera mano; Cowan revisa a Miller. En la nota: usar "unos cuatro" y decir que el número depende de qué cuenta como chunk.
- Carga pertinente: su definición cambió dentro de la propia escuela de Sweller; NN/g la omite. La nota debe decir que en UX se usa casi solo intrínseca vs. extrínseca.
- La teoría nació en educación (aprendizaje con problemas), no en interfaces; su aplicación a UX es una extrapolación de practicantes.

### Recurso canónico

Cowan 2001, abstract y sección 1, para el límite de capacidad; Miller 1956, la parte sobre chunking y recoding, para lo que realmente dijo; y NN/g "Minimize Cognitive Load" como puente a diseño. Fijarse en que lo medido es memoria de trabajo para ítems retenidos, no cuántos elementos puede mostrar una pantalla.

---

## 3. leyes-de-fitts-y-hick

### Fuentes

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| MacKenzie 1992, "Fitts' law as a research and design tool in HCI", *Human-Computer Interaction* 7, 91-139 (copia del autor) | P | [L] parcial (leí 100.000 de 131.000 caracteres) | 3/3/2/3 | https://www.yorku.ca/mack/hci1992.html |
| Fitts 1954, *J. Exp. Psychology* 47(6), 381-391 | P | no leído; solo citado por MacKenzie | 3/3/1/3 | sin URL verificada (DOI 10.1037/h0055392, **no comprobado**) |
| Hick 1952, "On the rate of gain of information", *Q. J. Exp. Psychology* 4(1), 11-26 | P | [S] | 3/3/1/3 | doi:10.1080/17470215208416600 (dado por el buscador; no abrí el texto) |
| Hyman 1953, "Stimulus information as a determinant of reaction time", *J. Exp. Psychology* 45(3), 188-196 | P | [S] | 3/3/1/3 | doi:10.1037/h0056940 (ídem) |
| Liu, Gori, Rioul, Beaudouin-Lafon, Guiard 2020, "How Relevant is Hick's Law for HCI?", CHI 2020 | P | [M] (abstract; el texto dio 403) | 3/3/2/3 | https://researchportal.ip-paris.fr/en/publications/how-relevant-is-hicks-law-for-hci/ (DOI 10.1145/3313831.3376878) |
| Wikipedia, "Hick's law" | S | [L] | 1/2/1/1 | https://en.wikipedia.org/wiki/Hick%27s_law |
| IxDF, "The Hick-Hyman Law" | S | [S] | 1/1/1/1 | https://ixdf.org/literature/article/the-hick-hyman-law-an-argument-against-complexity-in-user-interface-design |

### Fórmulas literales

- Fitts, forma original (MacKenzie, ecs. 3 y 6): `ID = log2(2A/W)` y `MT = a + b·log2(2A/W)`.
- Forma de Shannon propuesta por MacKenzie (ec. 10): `MT = a + b·log2(A/W + 1)`.
- A es la amplitud (distancia al blanco); W el ancho del blanco; a (ms) y b (ms/bit) son constantes empíricas; IP = 1/b, en bits/s. https://www.yorku.ca/mack/hci1992.html
- Hick–Hyman, alternativas equiprobables: `T = b · log2(n + 1)`; con probabilidades desiguales `T = b·H`, con `H = Σ pi · log2(1/pi + 1)`. El "+1" refleja la incertidumbre sobre si responder o no. https://en.wikipedia.org/wiki/Hick%27s_law [L, secundaria; las ecuaciones originales de Hick 1952 no las leí]

### Qué predicen y límites

- Fitts: el tiempo de un movimiento apuntado crece con el logaritmo de distancia sobre ancho. Límites según MacKenzie: el 2 de la forma original fue un ajuste arbitrario; esa forma da ID negativo cuando A < W/2, "a serious theoretical problem", y la de Shannon no; vale para movimientos rápidos y apuntados con error nominal cerca del 4 %; las predicciones empeoran bajo unos 3 bits; en blancos rectangulares abordados con ángulos distintos, qué es "W" no está resuelto. https://www.yorku.ca/mack/hci1992.html
- Hick: relaciona el tiempo de reacción de elección con el número de alternativas estímulo-respuesta. Hick 1952 concluyó que la tasa de ganancia de información es en promedio constante durante un acto perceptivo-motor; Hyman 1953 la extendió a alternativas con probabilidades desiguales. [S] https://www.pubmed.gov/28434379/ (resultado del buscador; no abrí el texto)
- Límites de Hick listados en Wikipedia (secundaria): buscar en una lista desordenada es lineal y "does not allow for the generalization of the scientific law"; con respuestas verbales a estímulos familiares, Longstreth et al. (1985) hallaron poca o ninguna relación; en sacádicos no hay relación o hay un efecto "anti-Hick"; la compatibilidad estímulo-respuesta cambia el tiempo. https://en.wikipedia.org/wiki/Hick%27s_law
- Liu et al. 2020 (CHI): la ley se usa en HCI para justificar menos ítems a la vez, pero ellos sostienen que la ley "no apoya" el principio de "menos es mejor"; que un crecimiento logarítmico en los datos no implica Hick; que el paradigma estímulo-respuesta rara vez es relevante en tareas de HCI; y concluyen que conviene mirar la búsqueda visual y la decisión en vez de citar la ley. https://researchportal.ip-paris.fr/en/publications/how-relevant-is-hicks-law-for-hci/ [M]. Seow (2005) ya había mostrado que Fitts y Hick no se justifican con la ley de Hick (según el mismo abstract y Wikipedia, [S]).

### Disputa a declarar

Hick como "base del diseño de menús" (práctica extendida, p. ej. IxDF) frente a Liu et al. 2020 ("little to offer to HCI"). Esto desmiente la lectura simple "menos opciones, decisión más rápida". Para la base de conocimiento conviene decirlo así: Hick vale para elecciones entre alternativas equiprobables y no conocidas de antemano, con la respuesta mapeada al estímulo; no para búsqueda en listas desordenadas ni para opciones conocidas, y no es evidencia de que "menos es mejor". Lo que sí tiene respaldo en diseño es Fitts (blancos más grandes y cercanos se alcanzan más rápido), con las precauciones de MacKenzie.

### Recurso canónico

MacKenzie 1992, secciones sobre la formulación de Shannon y el ancho efectivo (W_e): es la referencia que la ISO 9241-411 sigue (afirmación **no verificada** acá). Para Hick, Liu et al. 2020 (leer el texto completo; yo solo vi el abstract) antes que cualquier artículo de practicantes.

---

## 4. patron-oscuro

### Fuentes

| Fuente | Tipo | Marca | A/P/E/U | URL |
|---|---|---|---|---|
| Mathur et al. 2019, "Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites", CSCW 3, art. 81 | P | [L] | 3/3/3/3 | https://arxiv.org/abs/1907.07032 |
| Gray, Kou, Battles, Hoggatt, Toombs 2018, "The Dark (Patterns) Side of UX Design", CHI 2018, paper 534 | P | [L] | 3/3/3/3 | https://par.nsf.gov/servlets/purl/10057203 |
| Luguri y Strahilevitz 2021, "Shining a Light on Dark Patterns", *Journal of Legal Analysis* 13(1), 43-109 | P | [L] del borrador del 5-ago-2019 (SSRN); el publicado solo por metadatos | 3/3/3/3 | https://oag.ca.gov/sites/all/files/agweb/pdfs/privacy/shining-a-light-on-dark-patterns.pdf (versión publicada: https://academic.oup.com/jla/article/13/1/43/6180579) |
| Mathur, Mayer, Kshirsagar 2021, "What Makes a Dark Pattern... Dark?", CHI 2021 | P | [L] | 3/3/2/3 | https://arxiv.org/abs/2101.04843 |
| FTC, *Bringing Dark Patterns to Light* (staff report, sept-2022) | P (regulador) | [L] | 3/3/3/3 | https://www.ftc.gov/reports/bringing-dark-patterns-light (PDF: https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf) |
| Reglamento (UE) 2022/2065 (DSA), art. 25 | P (norma) | [L] artículo 25 | 3/3/1/3 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2065 |
| DSA considerando 67 (copia de Prighter, anotada) | S | [S] | 1/1/1/1 | https://prighter.com/resources/laws/dsa/recitals/recital-67 |
| deceptive.design (Harry Brignull) | S (practicante) | [L] | 2/2/3/2 | https://deceptive.design/ |
| Fogg, Behavior Model (Stanford Behavior Design Lab) | S | [S] | 2/1/1/2 | https://behaviordesign.stanford.edu/resources/fogg-behavior-model |
| Thaler y Sunstein, *Nudge* (2009 ed.), citado en Mathur et al. 2021 | P (libro) | [S] | 3/3/2/3 | https://arxiv.org/abs/2101.04843 |
| Maastricht Univ., "Destination 'dark patterns'..." (blog) | S | [S] | 1/1/1/1 | https://www.maastrichtuniversity.nl/blog/2023/04/destination-%E2%80%98dark-patterns%E2%80%99-eu-digital-legislative-train-and-line-drawing |

### Definición y origen

- Brignull acuñó el término en 2010 (https://par.nsf.gov/servlets/purl/10057203 y el informe de la FTC, que dice "Coined in 2010 by user design specialist Harry Brignull"). Su definición, citada por Gray et al.: "a user interface that has been carefully crafted to trick users into doing things...they are not mistakes, they are carefully crafted with a solid understanding of human psychology, and they do not have the user's interests in mind". Gray et al. aclaran que Brignull tiene un doctorado en ciencia cognitiva.
- deceptive.design (antes darkpatterns.org, "spreading awareness since 2010") los define como rasgos de apps, sitios y sistemas de IA que engañan a la gente para hacer cosas que no pretendía, y lista 18 tipos (Addictive Design, Comparison prevention, Confirmshaming, Currency Confusion, Disguised ads, Fake scarcity, Fake social proof, Fake urgency, Forced action, Hard to cancel, Hidden costs, Hidden subscription, Nagging, Obstruction, Preselection, Sneaking, Trick wording, Visual interference). https://deceptive.design/ . La página no nombra a Brignull; esa atribución sale de las otras dos fuentes.
- FTC: "design practices that trick or manipulate users into making choices they would not otherwise have made and that may cause harm". https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf

### Taxonomía de Gray et al. 2018

- Corpus de 118 artefactos que compartieron practicantes; análisis de contenido con la tipología de Brignull como base. https://par.nsf.gov/servlets/purl/10057203
- Cinco estrategias: nagging (redirección menor de la funcionalidad esperada, que puede persistir en varias interacciones), obstruction (impedir un flujo de tarea para disuadir una acción), sneaking (ocultar, disfrazar o demorar información relevante), interface interference (manipular la interfaz para privilegiar acciones, confundiendo o limitando el descubrimiento; tiene tres subtipos, el primero "hidden information"), forced action (exigir una acción para acceder o seguir accediendo a una función). Los tipos de Brignull (por ejemplo "Roach Motel", "Price Comparison Prevention") quedan anidados bajo estas cinco. Misma URL.
- Conclusión del resumen: los practicantes mezclan bajo "dark patterns" problemas éticos muy distintos, y los diseñadores pueden volverse cómplices de prácticas manipuladoras o "unreasonably persuasive". Misma URL.

### Taxonomía de Mathur et al. 2019

- Alcance: ~11.000 sitios de compras, ~53.000 páginas de producto; 1.818 instancias de patrones oscuros, 15 tipos en 7 categorías; 183 sitios con prácticas engañosas (234 instancias, según el cuerpo del texto); 22 terceros que los venden como solución "llave en mano". Los sitios más populares (ranking Alexa) tenían más. Las cifras son un piso, porque solo miraron texto en una muestra de páginas. https://arxiv.org/abs/1907.07032 [L, vía PDF]
- Siete categorías y quince tipos (instancias / sitios): **Sneaking** (Sneak into Basket 7/7, Hidden Costs 5/5, Hidden Subscription 14/13); **Urgency** (Countdown Timer 393/361, Limited-time Message 88/84); **Misdirection** (Confirmshaming 169/164, Visual Interference 25/24, Trick Questions 9/9, Pressured Selling 67/62); **Social Proof** (Activity Message 313/264, Testimonials 12/12); **Scarcity** (Low-stock Message 632/581, High-demand Message 47/43); **Obstruction** (Hard to Cancel 31/31); **Forced Action** (Forced Enrollment 6/6). Tabla 1 del paper.
- Un temporizador se juzgó engañoso si se reiniciaba tras vencer con la misma oferta vigente: 157 instancias en 140 sitios. Misma fuente.
- Segunda taxonomía, de cinco atributos con que un patrón altera la decisión: asimétrico, encubierto, engañoso, que oculta información y restrictivo; más los sesgos cognitivos que explotan (anclaje, bandwagon, default, framing, escasez, etc.). Misma fuente.

### Evidencia de que funcionan (Luguri y Strahilevitz)

- Experimento con una muestra representativa de consumidores de EE. UU., asignados al azar a control, patrones suaves o agresivos, tras decirles que estaban inscritos en un plan de protección contra robo de identidad. Aceptación: control 11,3 % (73 de 644), suave 25,8 % (155 de 600), agresivo 41,9 % (217 de 518); aumentos de 228 % y 371 % respecto del control. Si se cuentan los que abandonaron como que rechazaron, bajan a 25 % y 37 %. https://oag.ca.gov/sites/all/files/agweb/pdfs/privacy/shining-a-light-on-dark-patterns.pdf [L, borrador de 2019: las cifras de la versión publicada pueden diferir]
- Abstract: los patrones suaves más que duplicaron la probabilidad de seguir inscripto y los agresivos casi la cuadruplicaron; los agresivos generaron rechazo fuerte y los suaves no; las personas con menos educación fueron significativamente más susceptibles a los suaves; proponen una regla cuantitativa para decidir cuáles son ilegales usando pruebas A/B. Misma URL.
- La pantalla inicial (con "Accept and continue (recommended)" preseleccionado) explicó la mayoría de las aceptaciones: 75,5 % en suave, 65 % en agresivo. Misma URL.
- La FTC cita este estudio: los patrones oscuros "doubled the percentage of consumers who signed up", y el efecto aumenta al combinarlos. https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf

### Normativa

- **FTC 2022** (informe del personal, no una regla; votado 5-0 para su publicación según el comunicado, [S] vía buscador): cuatro categorías: (I) elementos de diseño que inducen creencias falsas; (II) que ocultan o demoran la divulgación de información material; (III) que llevan a cargos no autorizados; (IV) que oscurecen o subvierten opciones de privacidad. Se apoya en la sección 5 de la FTC Act, ROSCA (suscripciones con opción negativa), TILA, CAN-SPAM, COPPA y otras. Fuente: el PDF del informe.
- **DSA art. 25(1)**: "Providers of online platforms shall not design, organise or operate their online interfaces in a way that deceives or manipulates the recipients of their service or in a way that otherwise materially distorts or impairs the ability of the recipients of their service to make free and informed decisions." Art. 25(2): la prohibición no se aplica a prácticas cubiertas por la Directiva 2005/29/CE ni el Reglamento (UE) 2016/679. Art. 25(3): la Comisión puede emitir guías sobre, entre otras, dar más prominencia a ciertas opciones, pedir repetidamente una elección ya hecha ("pop-ups"), y "making the procedure for terminating a service more difficult than subscribing to it". https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2065
- El considerando 67 nombra a los dark patterns y habla de prácticas que "materially distort or impair, either on purpose or in effect" la autonomía; leído en una copia anotada [S], no en EUR-Lex. https://prighter.com/resources/laws/dsa/recitals/recital-67. El texto del artículo 25 no usa la expresión "dark patterns". Alcance: solo plataformas en línea, y sin definición legal general (Maastricht, [S]).

### Posiciones en disputa

1. **Intención del diseñador (Brignull 2010).** Patrón oscuro = interfaz "carefully crafted to trick"; "not mistakes". https://par.nsf.gov/servlets/purl/10057203
2. **Concepto de practicantes con ética mezclada (Gray 2018).** El término agrupa problemas éticos distintos; el valor del usuario queda desplazado por el del accionista. Misma URL.
3. **No hay una definición única (Mathur, Mayer, Kshirsagar 2021).** Hallaron 19 definiciones que difieren en si exigen engaño, intención del diseñador o daño; Confirmshaming suele ser transparente y Nagging no es engañoso por naturaleza, y aun así se los llama patrones oscuros; proponen cuatro lentes normativas (bienestar individual, bienestar colectivo, objetivos regulatorios, autonomía individual) y dos familias de atributos (modificar el espacio de decisión; manipular el flujo de información). https://arxiv.org/abs/2101.04843
4. **Enfoque legal-empírico (Luguri y Strahilevitz).** Hay que medir el efecto; los suaves son los que más justifican la intervención porque dan beneficio sin rechazo. https://oag.ca.gov/sites/all/files/agweb/pdfs/privacy/shining-a-light-on-dark-patterns.pdf
5. **Regulador de EE. UU. (FTC)**: engaño, ocultamiento, cargos y privacidad, con las leyes ya vigentes. **Regulador de la UE (DSA)**: engaño o manipulación o "distorsión material" de decidir con libertad e información, con exclusión expresa de lo que ya cubren las leyes de prácticas desleales y de datos. Las categorías no coinciden: la FTC se define por tipos de conducta; el DSA por el efecto sobre la decisión.

### La frontera con persuasión legítima

- **Nudge (Thaler y Sunstein)**: iniciativas que "steer people in particular directions but that also allow them to go their own way"; Thaler, más tarde, distingue "sludge": fricción excesiva que perjudica. Citado en https://arxiv.org/abs/2101.04843 [L del artículo secundario, no del libro].
- **Persuasión vs. manipulación** (filosofía, según Mathur et al. 2021): la persuasión apela al razonamiento consciente; la manipulación lo subvierte; hay desacuerdo sobre si la manipulación debe ser encubierta. Todo el marketing moldea preferencias, por eso la línea es un problema central de la lente de autonomía. Misma URL.
- **Fogg**: la conducta ocurre cuando coinciden motivación, capacidad y un disparador (B=MAP); si falta uno, no ocurre. https://behaviordesign.stanford.edu/resources/fogg-behavior-model [S]. Las fuentes que leí (Gray 2018 las cita en su sección sobre diseño persuasivo, "Fogg [27] views persuasive technology as...") tratan a Fogg como el marco de la tecnología persuasiva, no como una frontera ética. No encontré a Fogg trazando la frontera con los patrones oscuros.
- Gray et al. 2018: "Design is inherently a persuasive act"; el problema es el grado "unreasonable" de persuasión. https://par.nsf.gov/servlets/purl/10057203
- **Aplicado a los tres casos del brief**: los dos patrones más frecuentes de Mathur (mensaje de poco stock, 632 instancias; temporizador, 393) no son engañosos por naturaleza; lo son cuando el dato es falso (temporizador que se reinicia). Un criterio operativo: ¿la cifra es verdadera y la opción de rechazar es tan fácil como la de aceptar (asimetría)? Es una inferencia a partir de las fuentes, no una cita.

### Recurso canónico

Mathur et al. 2019, tabla 1 y sección 3 (taxonomía de atributos), como mapa de qué mirar en una landing o checkout; Luguri y Strahilevitz, sección de resultados, como evidencia de que funcionan; Mathur, Mayer y Kshirsagar 2021, sección 4 (lentes), como guía para decidir qué es y qué no es patrón oscuro; y el texto del art. 25 del DSA y el informe de la FTC como requisitos legales. Para consulta rápida de ejemplos: deceptive.design (fuente de practicante, marcada como tal).

---

## Huecos

- **Libros canónicos no leídos**: Norman 2013 (golfos, modelos conceptuales; solo diapositivas y NN/g), Thaler y Sunstein (*Nudge*; solo cita secundaria), Fogg 2003 (*Persuasive Technology*; no encontré su texto) y la fuente de Miller 1989 sobre que 7 era una alegoría (la afirmación circula en blogs, no la verifiqué).
- **Primarias de Fitts 1954, Hick 1952 y Hyman 1953**: no leí ninguna; las fórmulas de Hick vienen de Wikipedia y las de Fitts de MacKenzie (que cita a Fitts). Conviene verificarlas.
- **Liu et al. 2020** solo en abstract (el texto dio 403 en CORE y HAL); falta el argumento de convexidad que proponen como alternativa. **Landauer y Nachbar 1985** (menús alfabéticos y numéricos) solo como cita.
- **Sweller**: el artículo de 1988 y el de 2019 no los leí completos; falta saber cómo redefine la carga pertinente. NN/g no la menciona. No busqué evidencia empírica de carga cognitiva específica en interfaces web.
- **DSA considerando 67**: sin texto oficial de EUR-Lex; solo copia anotada. Tampoco busqué las guías de la Comisión ni la Directiva 2005/29/CE.
- **Luguri y Strahilevitz**: leí el borrador de 2019; las cifras de la versión publicada (JLA 2021) no se verificaron.
- **Fuente más débil del bloque**: la afirmación de NN/g sobre menús y 7±2 viene de una cita en un blog; no encontré el artículo de NN/g mismo ni nada de Baymard sobre el tema.
- **Gestalt**: leí solo NN/g (proximidad; la región común solo por el buscador). Falta un libro de texto de psicología de la percepción; no busqué si Norman la trata en su libro.
- **Patrones oscuros fuera de e-commerce**: casi toda la evidencia empírica es de tiendas online y suscripciones (EE. UU.); para apps internas y dashboards no encontré estudios.
- **Evidencia de "daño" en Europa**: no busqué el informe de la Comisión Europea de 2022 sobre dark patterns (la FTC lo cita como "EU Dark Patterns Report").
- NN/g sobre patrones oscuros y Baymard sobre checkout engañoso no se consultaron.
