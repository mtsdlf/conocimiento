# Evaluación educativa: adaptativa, calificación y evaluar un programa (2026-11-27)

Informe de investigación para el tema Evaluación educativa (área Pedagogía). Audiencia: personas sin formación docente que enseñan a adultos. Base pública y agnóstica: nada de lo que sigue nombra empresas propias; el material de contraste interno no se cita.

## Cómo leer este informe

- Marcas de fuente: **[L]** texto completo o capítulo leído; **[M]** abstract o registro del editor leído (Crossref, Semantic Scholar o la página del editor), sin el cuerpo; **[S]** secundaria (Wikipedia, resumen del buscador, páginas de terceros). Todo lo marcado [S] hay que reverificar antes de pasar a vigente.
- Puntajes 1-3 por fuente: A = autoridad, P = profundidad, E = ejemplos, U = unicidad (qué aporta que otra no tenga).
- Las paráfrasis del mismo documento cuentan como una fuente. Donde dos fuentes discrepan, van ambas.
- Cuando una herramienta resumió una página, los números van con la marca de esa fuente y está dicho.
- Limitaciones del método: se agotó el presupuesto de búsqueda web de la sesión a mitad de camino. Varias fuentes quedaron leídas solo por abstract; los huecos están en su sección y al final. Lo que dice la web se trató como dato.

## Veredicto sobre el árbol propuesto

El campo no divide exactamente en estas tres verticales, y conviene saberlo:

- **Adaptativa** reúne tres comunidades que casi no se citan: la psicometría (teoría clásica, IRT, tests adaptativos), los tutores inteligentes y la minería de datos educativos (seguimiento del conocimiento) y la psicología matemática (espacios de conocimiento). Para quien enseña a pocas personas, lo que sobrevive no es la estadística sino una idea (inferir por prerrequisitos y preguntar por el primer paso). Eso sugiere partir esta vertical por utilidad y no por escuela.
- **Calificación y acreditación** son dos temas distintos: cómo se informa lo aprendido dentro de un curso (referencia, notas, motivación) y qué señala un certificado afuera (mercado). La literatura de las dos no se superpone.
- **Evaluar un programa** pertenece a otro campo: psicología organizacional y capacitación (Kirkpatrick, transferencia) por un lado, y evaluación de programas educativos con grupo de comparación (WWC, EEF) por el otro. El primero casi no usa diseños con comparación; el segundo casi no habla de transferencia al puesto. Se mantienen juntas porque la pregunta es la misma (si el programa funcionó), pero con dos subcomponentes.
- El hallazgo transversal: casi todo lo que se estudió de evaluación adaptativa se hizo en matemática escolar y universitaria; en capacitación laboral hay muy poco sobre adaptar el diagnóstico.

Propuesta de componentes al final.

---

## Vertical 1. Evaluación adaptativa

### 1.1 Teoría clásica frente a teoría de respuesta al ítem (IRT)

**Qué se sabe.**

- La IRT modela la probabilidad de acertar un ítem en función de la habilidad de la persona y de rasgos del ítem. Variantes: 1PL o Rasch (solo dificultad), 2PL (agrega discriminación), 3PL (agrega acierto por azar; para un ítem de cuatro opciones el parámetro ronda 0,25). Difiere de la teoría clásica en que no supone ítems igualmente difíciles, deja variar el error de medición entre personas y sus parámetros no dependen (en teoría) de la muestra ni del test. La teoría clásica gana en simpleza de cálculo. https://en.wikipedia.org/wiki/Item_response_theory [S]
- Matiz: la escuela Rasch no lo ve como un caso particular de IRT sino como un enfoque distinto, que prioriza la medición fundamental y trata los datos que no encajan como problema a diagnosticar, no a absorber con más parámetros. Misma fuente [S].
- Referencia clásica citada por esa página: Embretson y Reise (2000), *Item Response Theory for Psychologists*; Lord (1980). No se leyeron. [S]

**Cuánta gente hace falta (dato que importa para grupos chicos).** Las fuentes no coinciden:

- König, Spoden y Frey (2019): "respondents are typically recommended for the two-parameter logistic (2PL) model" (el número no sobrevivió en el abstract del registro) y proponen un 2PL bayesiano jerárquico que da estimaciones precisas "even in sample sizes as small as" un N que el registro tampoco conserva. Es decir: la recomendación habitual es una muestra grande, y hay métodos para achicarla. https://doi.org/10.1177/0146621619893786 [M]
- Şahin y Weiss (2015): con un banco de 500 ítems simulado y calibrado con 10.000 examinados, "accurate ability parameter estimates can be obtained with a calibration sample of 150 examinees"; un banco de 200 ítems calibrado con 150 sirve "for some purposes". https://doi.org/10.12738/estp.2015.6.0102 [M]
- Ree (1981), simulación con 3PL: reducir el error de estimación "required at least 200 items calibrated on 2,000 subjects". https://doi.org/10.1177/014662168100500102 [M]
- Linacre (1994), Rasch Measurement Transactions 7(4): para que las dificultades de ítem queden estables dentro de ±1 logit con 95% de confianza, entre 16 y 36 personas según la puntería de la muestra, con 30 como recomendado mínimo para ítems dicotómicos; 50 personas bien apuntadas es "conservative" para estimaciones útiles; 250 para decisiones de alto riesgo. https://www.rasch.org/rmt/rmt74m.htm [S] (página de la propia revista leída vía resumen de herramienta)
- Lectura: la cifra "150 a 500 personas" del material de contraste es una simplificación; con Rasch hay recomendaciones de 30 a 50 para calibrar. El cuello de botella para un grupo chico es otro: el banco de ítems (cientos de preguntas ya calibradas), no solo las personas. Esto último es inferencia de esta investigación a partir de Ree y Şahin y Weiss.

**Fuentes.**

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| König, Spoden y Frey 2019, https://doi.org/10.1177/0146621619893786 | artículo, Applied Psychological Measurement | 3 | 1 | 1 | 2 | [M] |
| Şahin y Weiss 2015, https://doi.org/10.12738/estp.2015.6.0102 | artículo, simulación | 2 | 1 | 1 | 3 | [M] |
| Ree 1981, https://doi.org/10.1177/014662168100500102 | artículo, simulación | 2 | 1 | 1 | 2 | [M] |
| Linacre 1994, https://www.rasch.org/rmt/rmt74m.htm | nota técnica | 2 | 2 | 2 | 3 | [S] |
| Wikipedia, Item response theory, https://en.wikipedia.org/wiki/Item_response_theory | enciclopedia | 1 | 2 | 2 | 1 | [S] |

**Recurso canónico del componente:** Embretson y Reise (2000) (no leído; hueco) o, para el contraste sencillo, Hambleton y Jones (1993), "Comparison of classical test theory and item response theory", *Educational Measurement: Issues and Practice*, https://doi.org/10.1111/j.1745-3992.1993.tb00543.x (el registro de Crossref trae solo un título genérico; no se pudo leer) [M].

### 1.2 Tests adaptativos computarizados (CAT)

**Qué se sabe.**

- Un CAT elige cada ítem según el desempeño anterior: arranca asumiendo habilidad media, elige el ítem más informativo en la estimación actual, actualiza por máxima verosimilitud o métodos bayesianos y corta cuando el error estándar baja de un umbral. Existe desde los años 1970. Se usa en pruebas de admisión y evaluación a gran escala. Se puede acortar "typically by 50%" con más precisión que la versión fija. No se puede lanzar con ítems nuevos sin calibrar. Tiene problemas de seguridad (exposición de ítems), no permite volver atrás y los CAT con tiempo no sirven para decisiones de alto riesgo. https://en.wikipedia.org/wiki/Computerized_adaptive_testing [S]
- Weiss y Kingsbury (1984) describen tres aplicaciones escolares: dominio adaptativo (decidir si se dominó un contenido), calificación adaptativa y medición adaptativa del cambio; en la primera, el procedimiento adaptativo clasifica el dominio con más exactitud que el test convencional, con menos preguntas. https://doi.org/10.1111/j.1745-3984.1984.tb01040.x [M]

**Cuándo vale la pena (inferencia de esta investigación).** Un CAT paga cuando hay muchos examinados, un banco grande ya calibrado y consecuencias que justifican el costo. Con un curso o mentoría de unas decenas de personas o menos, el costo de armar y calibrar el banco no se recupera. Lo transferible es el principio (no gastar preguntas muy fáciles ni muy difíciles para esa persona), que se puede aplicar a mano con 5 a 10 preguntas ordenadas por dificultad y un corte simple, sin IRT.

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Weiss y Kingsbury 1984 | artículo | 3 | 1 | 2 | 3 | [M] |
| Wikipedia, Computerized adaptive testing | enciclopedia | 1 | 2 | 2 | 1 | [S] |

**Recurso canónico:** Wainer (ed.), *Computerized Adaptive Testing: A Primer* (2000), citado por la página de Wikipedia; no leído. Hueco. [S]

### 1.3 Seguimiento del conocimiento: Bayesian Knowledge Tracing y deep knowledge tracing

**Qué se sabe.**

- Corbett y Anderson, "Knowledge tracing: Modeling the acquisition of procedural knowledge", *User Modeling and User-Adapted Interaction* 4, 253-278. La fecha de la fuente discrepa: Springer lo da como 1994, y Wikipedia y Semantic Scholar como 1995 (el número 4 de la revista cae en 1994). En el material de contraste figura 1995; el pedido pedía 1994. Usar 1994 y anotar la discrepancia. https://doi.org/10.1007/BF01099821 [S] (resumen del buscador: el tutor mantiene una estimación de probabilidad de que el estudiante haya aprendido cada regla)
- BKT: cuatro parámetros por habilidad (conocimiento previo, probabilidad de aprender en cada oportunidad, "slip", "guess"); supone conocimiento binario por habilidad y respuestas binarias. https://en.wikipedia.org/wiki/Bayesian_knowledge_tracing [S]
- Piech et al. (2015), "Deep Knowledge Tracing" (NeurIPS): una red neuronal recurrente que no requiere conocimiento del dominio codificado a mano y mejora la predicción en varios conjuntos de datos. https://arxiv.org/abs/1506.05908 [M]
- Khajah, Lindsey y Mozer (2016), "How deep is knowledge tracing?": con extensiones de BKT (olvido, diferencias entre ítems, habilidades latentes) el rendimiento queda "indistinguishable" del de DKT; la ventaja de DKT no viene de representaciones nuevas. Tabla de AUC reportada (leída vía resumen de herramienta, a reverificar): Assistments, BKT clásico 0,73 (0,67 en Piech), BKT con extensiones 0,83 con olvido solo, DKT 0,86 (Piech); Statics, BKT extendido 0,75 y DKT 0,76; Spanish, 0,846 y 0,836. https://ar5iv.arxiv.org/html/1604.02416 [S]
- Xiong et al. (2016) encontró duplicados en el conjunto Assistments que inflaban resultados de DKT; Wilson et al. (2016) sostienen que seguir el conocimiento no se beneficia de la "profundidad". Ambos conocidos solo por el resumen del buscador. [S]

**Cuándo vale la pena para un grupo chico.** Ajustar parámetros requiere muchas respuestas de muchas personas; con pocos alumnos, los parámetros hay que inventarlos. El material de contraste concluye lo mismo. Su interés práctico para esta base es conceptual: distinguir "acertó" de "sabe" (se puede acertar por azar y fallar sabiendo), lo que justifica pedir más de una evidencia antes de dar por dominada una habilidad. Es una inferencia razonable, no un resultado medido.

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Corbett y Anderson 1994 | artículo fundacional | 3 | 1 | 1 | 3 | [S] |
| Piech et al. 2015 | paper de conferencia | 3 | 1 | 1 | 2 | [M] |
| Khajah et al. 2016 | paper (arXiv) | 3 | 2 | 2 | 3 | [S] |
| Wikipedia, BKT | enciclopedia | 1 | 1 | 1 | 1 | [S] |

**Recurso canónico:** Corbett y Anderson (1994) para BKT; Khajah et al. (2016) para la crítica a DKT. Hueco: no se leyó el texto de Corbett y Anderson.

### 1.4 Espacios de conocimiento (Doignon y Falmagne) y ALEKS

**Qué se sabe (esta es la fuente más sólida de la vertical).**

- Doignon y Falmagne (1985), "Spaces for the assessment of knowledge", *International Journal of Man-Machine Studies*; libro *Knowledge Spaces* (1999, Springer). Un espacio de conocimiento es una estructura de conjuntos cerrada bajo unión. https://en.wikipedia.org/wiki/Knowledge_space [S]; la referencia original de 1985 no se pudo leer ni verificar en Crossref.
- Capítulo de Cosyn, Doble, Falmagne et al. (2013), en *Knowledge Spaces: Applications in Education*, Springer [L]. Define el estado de conocimiento como "the set of 'problem types' that the student is capable of solving" y la estructura de estados como un espacio de aprendizaje con dos principios: un estudiante puede alcanzar a otro "by learning the missing concepts one at a time", y todo concepto que uno está listo para aprender, el otro lo domina o también está listo para aprenderlo. De ahí el teorema de las fronteras: un estado queda definido por sus dos fronteras, y la externa es "the set of problems that the student is ready to learn". Contrasta con el test psicométrico, que busca una puntuación numérica y puede descartar ítems poco correlacionados con el total aunque sean parte del currículo.
- Validación de ALEKS en ese capítulo: sobre 1.940.473 experiencias de aprendizaje, "the median probability of learning success was .93"; los propios autores reconocen que algunos ítems rinden mal (validez baja) y que no los eliminan porque forman parte del currículo. https://www.mheducation.com/content/dam/mhe/research/prek-12/essa-tier-4/aleks-assessing-learning-space.pdf [L]. Nota: el autor de esta fuente es la empresa que vende el sistema (conflicto de interés).
- Doignon y Falmagne (2015), arXiv:1511.06757: la evaluación no da un número sino una estructura combinatoria, es "adaptativa" en el sentido de que usa las respuestas previas, y usa procesos probabilísticos tipo Markov; millones de estudiantes usaron ALEKS. https://arxiv.org/abs/1511.06757 [M]
- Math Academy, página de método: el diagnóstico busca la "knowledge frontier", comprime el grafo al mínimo de temas que cubre el curso y las bases, elige el tema más informativo, un acierto es evidencia de que se sabe el tema y sus prerrequisitos y un error es evidencia de que no se sabe el tema ni lo que depende de él; un acierto muy lento pesa menos; lo que apenas se supera queda "conditionally completed" y se retrocede si el alumno se traba. Cubre 500 a 1.000 temas y reduce las preguntas "an order of magnitude" respecto de un enfoque ingenuo. https://mathacademy.com/how-our-ai-works [S] (leída vía resumen de herramienta). **Discrepancia con el material de contraste:** este dice que el sitio indica de 30 a 45 minutos; en la lectura de esta investigación la página no declara duración ni cantidad de preguntas. Tomar la duración como no verificada. Es una fuente comercial, sin datos publicados de exactitud.

**Aplicación a un grupo chico (inferencia).** La regla de inferencia es lógica sobre un grafo de prerrequisitos y no necesita muestra: si resuelve X, probablemente sabe lo que X requiere; si falla X, probablemente no sabe lo que depende de X. Lo costoso es construir el grafo y las preguntas. El riesgo de la regla (dar por sabido algo no demostrado) está reconocido por el propio método con la marca "conditionally completed".

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Cosyn, Doble, Falmagne et al. 2013 (cap. 2), enlace arriba | capítulo de libro académico | 3 | 3 | 2 | 3 | [L] |
| Doignon y Falmagne 2015, arXiv:1511.06757 | revisión de los autores | 3 | 2 | 1 | 2 | [M] |
| Doignon y Falmagne 1985 y 1999 | artículo y libro fundacionales | 3 | 3 | 2 | 3 | [S] (solo citados) |
| Math Academy, "How it works" | página de producto | 1 | 1 | 2 | 2 | [S] |

**Recurso canónico:** Falmagne et al. (2013), *Knowledge Spaces: Applications in Education* (Springer) y Doignon y Falmagne (1999).

### 1.5 Diagnóstico rápido: método del "primer paso" (Kalyuga y Sweller)

**Qué se sabe.**

- Kalyuga y Sweller (2004), *Journal of Educational Psychology* 96, 558-568. Abstract: la medida rápida basada en esquemas dio "a highly significant correlation (up to .92) between performance on the rapid measure and traditional measures of knowledge, with test times reduced by factors of 4.9 and 2.5", con materiales de álgebra y geometría de 9.º y 10.º grado; los experimentos 3 y 4 la usaron para elegir el diseño instruccional según la experticia (efecto de inversión de la experticia: lo que ayuda al novato deja de ayudar al experto). https://doi.org/10.1037/0022-0663.96.3.558 [M]
- Kalyuga y Sweller (2005), *ETR&D* 53, 83-93: con un tutor de álgebra elemental y diseño de control "yoked", el grupo con instrucción adaptada a rápidas pruebas de conocimiento más medidas de carga cognitiva mostró "higher knowledge and cognitive efficiency gains than the control group". https://doi.org/10.1007/BF02504800 [M]
- **Discrepancia con el material de contraste:** este da "2,8 veces menos tiempo" y "correlación 0,72" con N = 55 en octavo grado; esas cifras vienen de un resumen de otro trabajo de Kalyuga (aritmética), no del artículo de 2004, cuyo abstract da hasta 0,92 y factores de 4,9 y 2,5. Son estudios distintos; citar cada cifra con su artículo.
- Que el primer paso delata la experticia (el novato arranca por el principio, el experto salta) viene de la descripción de los propios autores (resumen del buscador). [S]
- Limitación: todos los estudios son con escolares y materiales de matemática; no se encontró validación en capacitación de TI. Declarar hueco.

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Kalyuga y Sweller 2004 | artículo experimental | 3 | 1 | 2 | 3 | [M] |
| Kalyuga y Sweller 2005 | artículo experimental | 3 | 1 | 2 | 2 | [M] |

**Recurso canónico:** Kalyuga y Sweller (2004).

### 1.6 Autoevaluación como punto de partida (complemento)

- Dunning, Heath y Suls (2004), *Psychological Science in the Public Interest* 5(3): "the correlation between self-ratings of skill and actual performance in many domains is moderate to meager"; la gente se sobrestima. https://doi.org/10.1111/j.1529-1006.2004.00018.x [M]
- Sitzmann, Ely, Brown y Bauer (2010), metaanálisis, *Academy of Management Learning & Education* 9(2): las correlaciones más fuertes de la autoevaluación del conocimiento fueron con motivación y satisfacción; con el aprendizaje cognitivo la relación fue moderada; "nearly a third" de los estudios de evaluación interpretaron el conocimiento autoevaluado como evidencia de aprendizaje. https://www.gwern.net/doc/psychology/cognitive-bias/illusion-of-depth/2010-sitzmann.pdf [L, solo abstract y primeras páginas]

**Recurso canónico de toda la vertical 1:** no hay uno. Para decidir qué hacer con un grupo chico, las piezas son Falmagne et al. (2013) y Kalyuga y Sweller (2004).

---

## Vertical 2. Calificación y acreditación

### 2.1 Referida a norma y a criterio

- Glaser (1963), "Instructional technology and the measurement of learning outcomes: some questions", *American Psychologist*, es el origen de los dos términos. https://doi.org/10.1037/h0049294 [M] (solo el registro; sin abstract)
- Una prueba referida a criterio usa el puntaje para afirmar qué puede hacer la persona; la referida a norma dice si le fue mejor o peor que a otros que la rindieron. El criterio es el dominio evaluado, no el punto de corte. Ejemplos: examen de manejo (criterio), prueba de ingreso diseñada para separar a los mejores de los peores (norma). https://en.wikipedia.org/wiki/Criterion-referenced_test [S]

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Glaser 1963 | artículo fundacional | 3 | 1 | 1 | 3 | [M] |
| Wikipedia, Criterion-referenced test | enciclopedia | 1 | 1 | 2 | 1 | [S] |

Hueco: no se leyó a Glaser.

### 2.2 Calificación por estándares y por dominio

**Qué se sabe.**

- Brookhart et al. (2016), "A century of grading research", *Review of Educational Research*: revisa cinco tipos de estudio (fiabilidad de las notas, composición de las notas escolares, percepciones docentes, calificación por estándares y calificación universitaria). Las primeras encuestas del siglo XX condenaron las notas por poco fiables; los estudios recientes sugieren que las notas evalúan "a multidimensional construct containing both cognitive and noncognitive factors reflecting what teachers value". https://doi.org/10.3102/0034654316672069 [M]
- Aprendizaje de dominio (*mastery learning*): Kulik, Kulik y Bangert-Drowns (1990), *Review of Educational Research*: metaanálisis de 108 evaluaciones controladas; efectos positivos sobre el rendimiento en exámenes de universidad, secundaria y primaria alta; "stronger on the weaker students"; efectos sobre actitudes positivos; los programas autoritmados "often reduce the completion rates in college classes". https://doi.org/10.3102/00346543060002265 [M]
- Críticas, desde Wikipedia (no se verificaron en el original): los efectos mayores salieron con pruebas hechas por los investigadores y casi desaparecen con pruebas estandarizadas; muchos estudios duraron 3 o 4 semanas; el trade-off tiempo-logro (Arlin 1984). https://en.wikipedia.org/wiki/Mastery_learning [S]. Bloom (1968) propuso mastery learning con 90% como umbral ilustrativo, y esa página le atribuye la afirmación de que más del 90% de los alumnos lograría aprender con éxito. [S]
- Página de Wikipedia sobre calificación por estándares: no existe en la URL probada (404); sin fuente adicional. Hueco para "calificación basada en estándares" como tal: la evidencia de que mejora el aprendizaje no se encontró, solo la revisión de Brookhart.

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Brookhart et al. 2016 | revisión | 3 | 2 | 1 | 3 | [M] |
| Kulik et al. 1990 | metaanálisis | 3 | 2 | 1 | 3 | [M] |
| Wikipedia, Mastery learning | enciclopedia | 1 | 2 | 2 | 1 | [S] |

**Recurso canónico:** Brookhart et al. (2016) para la calificación; Kulik et al. (1990) para el dominio.

### 2.3 Inflación de notas

- Denning, Eide, Mumford, Patterson y Warnick (2021), NBER w28710: la graduación universitaria cayó de los años 70 a los 90 y subió desde los 90; con datos nacionales y administrativos de nueve universidades públicas grandes encuentran que los GPA subieron sin que lo explique la composición, la preparación ni la escuela; y en una universidad pública de artes liberales "grades have increased over time conditional on final exam performance". Concluyen que la inflación explica buena parte de la suba de graduación. https://doi.org/10.3386/w28710 [M] (publicado después como artículo en revista; no verificado en esta investigación)
- Cifras de contexto desde Wikipedia: según Rojstaczer (2003), unas 80 instituciones y más de un millón de estudiantes, las notas subieron alrededor de 0,15 por década en escala de 4,0 desde los años 60; Princeton bajó la proporción de A de 47,9% (2002-03) a 39,7% (2008-09) con su política de 2004. https://en.wikipedia.org/wiki/Grade_inflation [S]. Esa misma página aclara que notas más altas no prueban por sí solas inflación; hay que mostrar que el trabajo no merece la nota. Casi todo el dato es de universidades de Estados Unidos; para adultos que aprenden en cursos cortos de TI no hay evidencia encontrada. Hueco.

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Denning et al. 2021 | documento de trabajo | 3 | 2 | 1 | 3 | [M] |
| Wikipedia, Grade inflation | enciclopedia | 1 | 2 | 3 | 1 | [S] |

**Recurso canónico:** Denning et al. (2021/2022).

### 2.4 Qué hacen las notas con la motivación y el aprendizaje

**Qué se sabe.**

- Butler (1987), *Journal of Educational Psychology* 79(4), 474-482 [L, texto completo]: 200 alumnos de quinto y sexto grado, tareas de pensamiento divergente en tres sesiones, con comentarios individuales, notas numéricas, elogio estandarizado o ningún feedback tras las sesiones 1 y 2. "interest, performance, and attributions of effort... were highest at both levels of achievement after receipt of comments". Las notas y el elogio dieron atribuciones centradas en el ego y, de forma notable, un impacto similar, que la teoría de la evaluación cognitiva no predecía.
- Butler (1988), *British Journal of Educational Psychology* 58, 1-14 (el que cita el pedido): 12 clases asignadas al azar a tres condiciones (notas, comentarios, ambos) y 132 alumnos medidos; "interest and performance on both tasks at both levels of school achievement were highest after comments"; "Grades and grades plus comments had similar and generally undermining effects". Es decir: agregar comentarios a la nota no salva el efecto. https://doi.org/10.1111/j.2044-8279.1988.tb00874.x [M]. Ojo: Butler 1987 y 1988 son artículos distintos y se confunden con frecuencia.
- Koenka, Linnenbrink-Garcia, Moshontz, Atkinson, Sanchez y Cooper, metaanálisis en *Educational Psychology* 41(7), 922-947 (publicado en línea en 2019; la fecha 2021 es la del número): cuatro metaanálisis; las notas, frente a no dar feedback, "positively influenced achievement but negatively influenced motivation"; frente a comentarios, quienes recibieron notas tuvieron peor logro y motivación menos óptima. Los moderadores variaron con el tipo de motivación, el contexto, la edad y el momento (anticipar frente a recibir). https://doi.org/10.1080/01443410.2019.1659939 [M]. No se leyeron los tamaños de efecto. Aclaración: es de escolares de primaria y secundaria; trasladarlo a adultos es una extrapolación.
- Wisniewski, Zierer y Hattie (2020), *Frontiers in Psychology*: 435 estudios, 994 tamaños de efecto, unos 61.000 participantes; efecto global del feedback d = 0,48, con enorme variación; la información contenida pesa mucho (feedback correctivo d = 0,46; de alta información d = 0,99; refuerzo o castigo d = 0,24); el feedback rinde más en resultados cognitivos y motores que en motivacionales y de conducta. Esta fuente no compara notas con comentarios. https://pmc.ncbi.nlm.nih.gov/articles/PMC6987456 [S] (leída vía resumen de herramienta)

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Butler 1987 | experimento | 3 | 3 | 2 | 2 | [L] |
| Butler 1988 | experimento | 3 | 1 | 2 | 3 | [M] |
| Koenka et al. 2019/2021 | metaanálisis | 3 | 1 | 1 | 3 | [M] |
| Wisniewski et al. 2020 | metaanálisis | 3 | 1 | 1 | 2 | [S] |

**Recurso canónico:** Koenka et al. (metaanálisis) con Butler (1988) como experimento original.

### 2.5 Certificados y microcredenciales: qué señalan al mercado

**Qué se sabe (poco, y lo encontrado limita lo que se puede afirmar).**

- Definición de política: las microcredenciales "certify the learning outcomes of short-term learning experiences, for example a short course or training"; sin estándares comunes de calidad, transparencia, comparabilidad, reconocimiento y portabilidad no alcanzan su potencial. https://education.ec.europa.eu/education-levels/higher-education/micro-credentials [S] (página oficial, sin datos de mercado laboral: son metas de política, no resultados).
- Experimento de campo de Deming, Yuchtman, Abulafi, Goldin y Katz (2016), *American Economic Review*: un título de grado en negocios de una institución online con fines de lucro recibe 22% menos de devoluciones de llamada que uno de una pública no selectiva; en puestos de salud los títulos con fines de lucro reciben menos llamados salvo que el puesto exija un indicador externo de calidad, como una licencia. No es sobre microcredenciales, pero muestra que el emisor y la verificación externa pesan en la señal. https://doi.org/10.1257/aer.20141757 [M]
- Ehlert y Schimke (2026), preprint en OSF, no revisado por pares: experimento de elección discreta preinscripto con 1.380 profesionales de recursos humanos de Alemania y 12.048 perfiles en 24 ocupaciones que requieren educación superior; "digital micro-credentials do not increase hiring probabilities and are valued significantly less than equivalent certificates obtained through in-person courses"; la diferencia se debe sobre todo a la confianza en la calidad de la señal; las microcredenciales presenciales de universidades mejoran las chances; entre postulantes con menor ajuste de campo, las presenciales pueden ayudar. https://doi.org/10.31235/osf.io/8a7h6_v1 [M]. Fuente débil por ser preprint y por limitarse a Alemania y puestos de educación superior, pero es la única encontrada que mide el efecto en contratación.
- Hueco: no se encontró evidencia sobre certificaciones de TI de proveedor, certificados de cursos cortos ni credenciales de escuelas de programación en contratación, ni metaanálisis de insignias digitales. La afirmación habitual de que "los certificados abren puertas" queda sin respaldo en esta investigación.

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Deming et al. 2016 | experimento de campo, revista | 3 | 2 | 2 | 2 | [M] |
| Ehlert y Schimke 2026 | preprint | 1 | 2 | 2 | 3 | [M] |
| Comisión Europea, página de microcredenciales | documento oficial | 2 | 1 | 1 | 1 | [S] |

**Recurso canónico:** ninguno suficiente; el más cercano es Deming et al. (2016) para la lógica de señal.

---

## Vertical 3. Evaluar un programa

### 3.1 Los cuatro niveles de Kirkpatrick y sus críticas

**Qué se sabe.**

- El marco de reacción, aprendizaje, conducta y resultados es de Kirkpatrick (1959-1960; el original no se leyó). Colquitt, LePine y Noe (2000, JAP) lo describen como un modelo que "posits that reactions to training, learning, behavior change, and results are linked in a positive, causal manner" y señalan que Alliger y colegas cuestionaron esa suposición, en especial entre reacciones, aprendizaje y cambio de conducta. [L, texto del paper] https://www.gwern.net/doc/iq/2000-colquitt.pdf
- Alliger, Tannenbaum, Bennett, Traver y Shotland (1997), *Personnel Psychology* 50, 341-358: marco ampliado con reacciones afectivas y de utilidad y aprendizaje, retención y demostración de conducta; 34 estudios y 115 correlaciones. Hallazgo clave: "Utility-type reaction measures were more strongly related to learning or on-the-job performance (transfer) than affective-type reaction measures", y las de utilidad fueron mejores correlatos de transferencia que el aprendizaje inmediato o retenido. https://doi.org/10.1111/j.1744-6570.1997.tb00911.x [M]
  - **Matiz respecto de la formulación del pedido** ("correlación casi nula entre reacción y aprendizaje"): lo que se pudo verificar es que las reacciones afectivas ("me gustó") se relacionan poco con los otros criterios, y que las de utilidad ("me sirve") se relacionan más. Los coeficientes corregidos no se pudieron leer (el informe técnico de DTIC dio error 403). No citar un número sin leer el artículo.
  - Cita secundaria literal de Arthur et al. (2003): "there is very little reason to believe that how trainees feel about or whether they like a training program tells researchers much, if anything, about" el aprendizaje, la conducta o los resultados, "supported by the lack of relationship between reaction criteria and the other three criteria" (citan a Alliger 1989 y 1997, Colquitt et al. 2000, entre otros). https://www.psychologie.uni-mannheim.de/cip/tut/seminare_wittmann/meta_fribourg/Arthur_etal_2003_MA_Trainings_in_organisations.pdf [L]
- Sitzmann, Brown, Casper, Ely y Zimmerman (2008), JAP 93(2), 280-295: las reacciones reflejan sobre todo características del curso; el estilo instruccional fue el mejor predictor (rho = 0,66), seguido de la interacción humana (0,56); las reacciones se asociaron con cambios posteriores en motivación y autoeficacia. https://doi.org/10.1037/0021-9010.93.2.280 [S] (resumen del buscador)
- Bell, Tannenbaum, Ford, Noe y Kraiger (2017), JAP, "100 years of training and development research": "trainee reactions are not necessarily a strong predictor of learning"; en un estudio longitudinal (Warr, Allan y Birdi) "reaction measures were predictive of changes in learning outcomes but not changes in job behavior"; "many studies continue to measure learning only in terms of declarative knowledge". https://doi.org/10.1037/apl0000142 [L] (texto del manuscrito aceptado)
- Holton (1996), "The flawed four-level evaluation model", *Human Resource Development Quarterly* 7, 5-21: "the four-level system of training evaluation is really a taxonomy of outcomes and is flawed as an evaluation model"; un modelo válido debe "specify outcomes correctly, account for the effects of intervening variables... and indicate causal relationships". Propone un modelo con variables intervinientes (motivación para aprender, trainability, actitudes laborales, características personales, condiciones de transferencia). https://doi.org/10.1002/hrdq.3920070103 [M] Kirkpatrick respondió en el mismo número (pp. 23-25) diciendo que nunca lo llamó "modelo" sino "los cuatro niveles"; esa cita es de un resumen del buscador. [S]
- Kraiger, Ford y Salas (1993), JAP 78, 311-328, propusieron como alternativa una clasificación de resultados cognitivos, de habilidad y afectivos. https://doi.org/10.1037/0021-9010.78.2.311 [M] (solo registro)
- Arthur, Bennett, Edens y Bell (2003), JAP 88(2), 234-245 [L]: diferencias medias estandarizadas de efecto de la capacitación en organizaciones: 0,60 para reacciones (k = 15, N = 936), 0,63 para aprendizaje (k = 234, N = 15.014), 0,62 para conducta (k = 122, N = 15.627) y 0,62 para resultados (k = 26, N = 1.748). Son efectos de capacitación frente a no capacitación, no correlaciones entre niveles; no se deben mezclar con el hallazgo de Alliger.

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Alliger et al. 1997 | metaanálisis | 3 | 1 | 1 | 3 | [M] |
| Holton 1996 | artículo teórico | 3 | 1 | 1 | 3 | [M] |
| Arthur et al. 2003 | metaanálisis | 3 | 3 | 2 | 3 | [L] |
| Sitzmann et al. 2008 | metaanálisis | 3 | 1 | 1 | 2 | [S] |
| Bell et al. 2017 | revisión del siglo | 3 | 3 | 2 | 3 | [L] |
| Colquitt, LePine y Noe 2000 | metaanálisis | 3 | 2 | 1 | 2 | [L] |

**Recurso canónico:** Alliger et al. (1997) para la crítica empírica y Holton (1996) para la teórica; para orientarse, Bell et al. (2017).

### 3.2 Transferencia: Baldwin y Ford, Blume et al., revisiones

- Baldwin y Ford (1988), "Transfer of training: A review and directions for future research", *Personnel Psychology* 41(1), 63-105. Organiza los factores en tres grupos (características del aprendiz, diseño de la capacitación y ambiente de trabajo) con dos fases: insumos que producen aprendizaje y retención, y condiciones de transferencia (generalización y mantenimiento en el trabajo). Descripción desde Wikipedia: es "the most commonly cited model of transfer" y define transferencia como "the generalization and maintenance of material learned in training to the work environment". El texto completo (PDF de Gwern) es una imagen escaneada sin OCR y no se pudo leer. https://doi.org/10.1111/j.1744-6570.1988.tb00632.x [S] https://en.wikipedia.org/wiki/Transfer_of_training [S]
- Blume, Ford, Baldwin y Huang (2010), *Journal of Management* 36(4), 1065-1105 [M, abstract completo]: 89 estudios; relaciones positivas de la transferencia con capacidad cognitiva, responsabilidad, motivación y ambiente de trabajo que apoya; la mayoría de los predictores (motivación, ambiente) se relacionan más fuerte con la transferencia cuando el entrenamiento es de habilidades "open" (ej. liderazgo) que "closed" (ej. software); cuando la transferencia se mide con la misma fuente y en el mismo contexto "consistently inflated transfer relationships". https://doi.org/10.1177/0149206309352880 Bell et al. (2017) agregan que los factores tuvieron efectos distintos según el criterio (uso o efectividad) y que los resultados "fail to provide compelling support" para las intervenciones previas y posteriores a la capacitación, y que las restricciones del ambiente se estudiaron poco. [L]. Los tamaños de efecto no se leyeron.
- Grossman y Salas (2011), *International Journal of Training and Development*: sobre el modelo de Baldwin y Ford, los factores con relaciones más fuertes y consistentes: de los aprendices (capacidad cognitiva, autoeficacia, motivación, utilidad percibida), del diseño (modelado conductual, gestión del error, ambientes realistas) y del trabajo (clima de transferencia, apoyo, oportunidad de practicar, seguimiento). https://doi.org/10.1111/j.1468-2419.2011.00373.x [M]
- Burke y Hutchins (2007), *Human Resource Development Review*: revisión integradora de la transferencia (características del aprendiz, diseño y entrega, ambiente de trabajo). https://doi.org/10.1177/1534484307303035 [M]
- Frecuente cita de "solo 10 % se transfiere": no se encontró una fuente primaria verificable en esta investigación; no usarla. (Saks 2002 la discute pero solo se halló el registro.) Hueco.
- Ya está en la base: la caída de los tamaños de efecto al pasar de criterios de aprendizaje a criterios de conducta, y el metaanálisis de Sitzmann y Ely, en `Desarrollo-personal/Efectividad-personal/aprender-por-cuenta-propia.md` (leída). Este componente no debe repetirlo: debe contar el modelo y el predictor del ambiente de trabajo, que esa nota no toca.

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Baldwin y Ford 1988 | revisión fundacional | 3 | 3 | 2 | 3 | [S] |
| Blume et al. 2010 | metaanálisis | 3 | 2 | 1 | 3 | [M] |
| Grossman y Salas 2011 | revisión | 3 | 1 | 2 | 2 | [M] |
| Burke y Hutchins 2007 | revisión | 3 | 1 | 1 | 1 | [M] |

**Recurso canónico:** Baldwin y Ford (1988) como marco y Blume et al. (2010) como evidencia; Grossman y Salas (2011) como guía legible.

### 3.3 ROI de Phillips y su debilidad

- Phillips añade un nivel 5 (retorno de la inversión) y un nivel 0 (insumos) a los de Kirkpatrick y una etapa de "aislar" el efecto del programa, con técnicas como grupo de control, análisis de tendencia, pronóstico y estimaciones de los participantes; las estimaciones se ajustan por la confianza que declara el participante, y se usan "only when other methods are unavailable or too time-consuming". Los materiales consultados son de la profesión (ATD, Training Industry, Whatfix), sin distancia crítica; reconocen que una estimación es solo una estimación, que algunos participantes no saben qué factores contribuyeron, y que aislar el efecto frente al mercado o cambios operativos es uno de los desafíos clave. https://trainingindustry.com/wiki/measurement-and-analytics/phillips-roi-methodology/ [S] https://assets.td.org/m/11b565b43e39e737/original/Was-it-the-training.pdf [S]
- Fuente académica: Bartel (2000), *Industrial Relations*: revisa tres tipos de estudio del retorno del empleador a la capacitación (encuestas grandes de empresas, estudios econométricos de caso con datos de una o dos empresas, y estudios de caso patrocinados por empresas) y evalúa sus fortalezas y debilidades; concluye que el retorno "may be much higher than previously believed" y que, para obtener información exacta, hay que acceder a bases de datos de las empresas y recoger variables que permitan "isolate the effect of training". https://doi.org/10.1111/0019-8676.00178 [M]
- La debilidad principal (inferencia de esta investigación, coherente con Phillips y Bartel): sin grupo de comparación, el aislamiento depende de estimaciones de los propios participantes, que además son quienes tienen interés en el programa; el número final de ROI hereda esa incertidumbre. No se encontró una crítica académica independiente que lo cuantifique. Hueco declarado.
- Los libros de Phillips no se leyeron.

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Training Industry wiki, ATD | divulgación profesional | 1 | 1 | 2 | 1 | [S] |
| Bartel 2000 | revisión | 3 | 1 | 1 | 3 | [M] |

**Recurso canónico:** Bartel (2000) como contrapunto académico; Phillips mismo (libros) no leído.

### 3.4 Evaluar un programa educativo: diseños con grupo de comparación

- What Works Clearinghouse, Procedures and Standards Handbook v5.0 [L]: los diseños de asignación controlada (experimentos aleatorizados, discontinuidad de regresión, diseños de caso único) son elegibles para la calificación más alta, "Meets WWC Standards Without Reservations"; los cuasi-experimentales y los aleatorizados con desgaste alto como máximo reciben "With Reservations"; para cuasi-experimentos y experimentos aleatorizados comprometidos se exige equivalencia en la línea de base: diferencias no mayores de 0,25 desviaciones estándar en covariables clave, con ajuste estadístico entre 0,05 y 0,25 y sin ajuste necesario por debajo de 0,05. https://ies.ed.gov/ncee/wwc/Docs/referenceresources/Final_WWC-HandbookVer5.0-0-508.pdf
- EEF (Education Endowment Foundation, Inglaterra): el mapa del área lo ubica como síntesis de evidencia (Teaching and Learning Toolkit). Las páginas de la EEF sobre evaluación y toolkit devolvieron error 403; no se pudo leer cómo califica la solidez (candados) ni su guía de evaluación. Hueco. https://educationendowmentfoundation.org.uk/education-evidence/teaching-learning-toolkit [S] (solo vía el vistazo del área)
- Lo transferible a un curso chico (inferencia): con pocas personas, un diseño aleatorizado formal no es viable; las opciones realistas son comparar contra el grupo anterior o contra una lista de espera con la misma prueba, medir antes y después, usar un criterio que no sea la opinión de los participantes y evitar que el evaluador sea quien enseñó. No se encontró una fuente que valide estas adaptaciones.

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| WWC Handbook v5.0 | manual oficial | 3 | 3 | 2 | 3 | [L] |
| EEF | síntesis y guía | 3 | – | – | – | [S] (no leída) |

**Recurso canónico:** WWC Handbook para los estándares de diseño; EEF pendiente.

---

## Huecos

1. Fuentes fundacionales no leídas en el cuerpo: Corbett y Anderson 1994, Doignon y Falmagne 1985/1999, Glaser 1963, Kirkpatrick 1959, Baldwin y Ford 1988 (PDF escaneado sin OCR), Alliger 1997 (solo abstract; sin coeficientes), Holton 1996 (solo abstract), Koenka 2019/2021 (sin tamaños de efecto), Blume 2010 (sin tamaños de efecto).
2. Se agotó el presupuesto de búsqueda web: el tercer round de varios componentes no se hizo (EEF, críticas académicas a Phillips, calificación por estándares, evidencia de microcredenciales de TI, fuentes de "solo 10% se transfiere").
3. Sin evidencia en adultos que aprenden TI sobre: diagnóstico de entrada validado, calificación por dominio, efecto de las notas en la motivación, inflación de notas. Casi todo es de escolares y universitarios.
4. Cifras del material de contraste que no se confirman: Math Academy "30 a 45 minutos" (la página no lo dice); Kalyuga "2,8 veces y r = 0,72" (es de otro trabajo; el de 2004 da 4,9 y 2,5 y hasta 0,92); IRT "150 a 500" (hay recomendaciones de 30 a 50 para Rasch y de 150 en un estudio de simulación de CAT; el número 500 de König no se pudo ver). Corbett y Anderson figura como 1995 en el material de contraste: 1994 es la fecha de la revista.
5. Fuentes leídas solo por resumen de herramienta (marca [S] con lectura de página): Khajah et al. (cifras de AUC), Math Academy, Linacre, Wisniewski et al., Wikipedia. Reverificar antes de pasar a vigente.
6. Conflicto de interés: ALEKS (capítulo escrito por empleados de la empresa) y Math Academy (página comercial).

## Propuesta de componentes

Para esta audiencia conviene dividir por decisión del docente, no por escuela académica:

1. **Saber desde dónde arranca alguien** (diagnóstico de entrada): inferir por prerrequisitos (espacios de conocimiento), preguntar por el primer paso (Kalyuga y Sweller) y límites de la autoevaluación (Dunning; Sitzmann 2010).
2. **Tests adaptativos y modelos estadísticos: qué son y por qué no para un grupo chico** (IRT, CAT, BKT y DKT en una sola nota breve, con las cifras de muestra y banco de ítems).
3. **Calificar por criterio y por dominio** (referida a norma y a criterio, aprendizaje de dominio, Brookhart; inflación de notas como advertencia).
4. **Notas, comentarios y motivación** (Butler, Koenka, Wisniewski).
5. **Certificados y señales al mercado** (con el hueco declarado de evidencia en TI).
6. **Evaluar si la capacitación funcionó: reacción, aprendizaje, conducta y resultados** (Kirkpatrick y críticas de Alliger y Holton).
7. **Que lo aprendido se use: transferencia** (Baldwin y Ford, Blume, Grossman y Salas), sin repetir lo que ya está en `aprender-por-cuenta-propia.md`.
8. **Medir el retorno y comparar contra algo** (ROI de Phillips y su debilidad; diseños con grupo de comparación: WWC, EEF).

El tema podría colgar de dos entradas del árbol (qué se evalúa al alumno, qué se evalúa del programa) en vez de tres verticales.
