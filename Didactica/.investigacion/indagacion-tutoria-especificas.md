# Didáctica: indagación, tutoría y didácticas específicas

Informe de investigación (2026-11-27) para el tema Didáctica del área Pedagogía. Audiencia final: quien enseña a adultos sin formación docente (mentorear, dar un curso en IT). Base pública y agnóstica: el material propio consultado se usó como pista y no se nombra.

## Cómo leer este informe

- Marcas de lectura: **[L]** leí el texto o el abstract completo en la fuente; **[M]** leí metadatos oficiales (Crossref, arXiv, páginas de editorial) y un resumen, sin el texto del artículo; **[S]** solo resumen del buscador o de un espejo.
- Puntajes 1-3 (3 es lo mejor): **A** autoridad, **P** profundidad, **E** ejemplos, **U** unicidad.
- Límites del proceso: el buscador agotó su cupo a mitad de la tercera ronda, el sitio de la EEF bloquea la descarga automática (HTTP 403) y PMC pidió verificación de navegador. Por eso hay más [M] y [S] de lo deseable, y los huecos están declarados al final. Lo que viene de material propio y no pude verificar va marcado "no verificado".
- Lo que dice la web se trata como dato. Las paráfrasis de un mismo documento cuentan como una fuente.

## Veredicto sobre el árbol propuesto

El árbol de tres verticales funciona como agenda, pero el campo divide distinto en tres puntos:

1. **"Aprendizaje activo e indagación" mezcla una disputa con técnicas.** La literatura lo ordena en torno a una sola pregunta: cuánta guía y cuándo. Eso separa bien (a) la disputa guía vs. descubrimiento, que incluye la secuencia "explicar primero / problema primero", (b) el aprendizaje activo en clase (Freeman, ICAP) y (c) PBL y proyectos, que sus defensores no consideran "mínima guía".
2. **Tutoría y mentoría son dos literaturas casi sin contacto.** Tutoría es enseñar una habilidad uno a uno o en grupo chico (Bloom, VanLehn, EEF, Nickow). Mentoría es acompañar una trayectoria (Kram, Eby) y sus efectos son de otro tipo (actitudes, carrera). El aprendizaje cognitivo (Collins, Brown, Newman) no es de ninguna de las dos: es un modelo de andamiaje que sirve a ambas y merece nota propia.
3. **Las didácticas específicas son un marco más tres casos de rango distinto.** Programación tiene literatura propia grande (computing education), ciencias es un campo enorme del que no pude verificar nada concreto, e idiomas ya está cubierto en `Ingles/`. Enseñar programación con IA es hoy un subcampo con evidencia nueva y cambiante que conviene separar.

## Componente 1: Guía y descubrimiento (la disputa)

### Posición A: la guía fuerte gana, y el descubrimiento puro no sirve

- Mayer (2004), *American Psychologist* 59(1), 14-19, DOI 10.1037/0003-066X.59.1.14. Revisó tres áreas (descubrimiento de reglas de resolución de problemas, enseñanza de estrategias de conservación y enseñanza de programación) y concluyó que el descubrimiento guiado rinde más que el puro en aprendizaje y transferencia. Su título propone una "regla de tres strikes" contra el descubrimiento puro. Fuente: https://bibsonomy.org/bibtex/2afaf704c1c0c9adebec5339afaf209c2/ji [S], más metadatos Crossref [M]. No arguye contra todos los métodos centrados en el alumno: su conclusión es "guía instruccional", no instrucción directa.
- Kirschner, Sweller y Clark (2006), "Why Minimal Guidance During Instruction Does Not Work", *Educational Psychologist* 41(2), DOI 10.1207/s15326985ep4102_1 [M]. Argumento: la experticia se explica en buena parte por la memoria a largo plazo; las tareas de poca guía cargan la memoria de trabajo del novato; el cómo trabaja una disciplina no determina cómo enseñarla. Reseña de lectura: https://notes.andymatuschak.org/zUiDqjKiS3udc3wcvcFbcpc [S]. No pude leer su abstract literal.
- **La mejor evidencia de esta posición es el metaanálisis de Alfieri et al. (2011)**, *Journal of Educational Psychology* 103(1), 1-18, https://www.fisme.science.uu.nl/publicaties/literatuur/2011_alfieri_discovery_learning.pdf [L abstract]. 164 estudios. Descubrimiento sin asistencia contra instrucción explícita: d = -0,38 (IC 95% [-0,44, -0,31], 580 comparaciones). Descubrimiento asistido contra otras formas de instrucción: d = 0,30 (IC [0,23, 0,36], 360 comparaciones). Cita literal: "unassisted discovery does not benefit learners, whereas feedback, worked examples, scaffolding, and elicited explanations do."

### Posición B: PBL e indagación no son descubrimiento puro

- Hmelo-Silver, Duncan y Chinn (2007), *Educational Psychologist* 42(2), 99-107, DOI 10.1080/00461520701263368 [M] y resumen del buscador [S]. Su tesis: Kirschner et al. juntaron PBL e indagación con el descubrimiento sin guía, pero ambos usan andamiaje extenso que reduce la carga cognitiva. En el mismo número, Schmidt, Loyens, van Gog y Paas (2007) sostienen que PBL es compatible con la arquitectura cognitiva humana (pp. 91-97), y Sweller, Kirschner y Clark responden en pp. 115-121 [S]. No leí estos tres textos completos.
- **La mejor evidencia de esta posición** son los metaanálisis de PBL (componente 3) y el propio Alfieri: el "descubrimiento asistido" (con andamiaje, explicaciones elicitadas, retroalimentación) sí funciona. Es un punto de coincidencia: la disputa se reduce a si PBL cuenta como "asistido" o como "mínimo".

### Lectura conjunta

Ambos bandos aceptan el hallazgo de Alfieri (el descubrimiento sin ayuda pierde, el asistido gana). Discrepan en cómo clasificar PBL e indagación. Para un lector sin formación docente: el dato accionable es que la pregunta no es "explicar o dejar descubrir" sino "cuánta ayuda, y de qué tipo, en cada momento".

### Secuencia: explicar primero vs. problema primero

- Sinha y Kapur (2021), *Review of Educational Research* 91(5), 761-798, DOI 10.3102/00346543211019105 [L abstract vía Crossref]. 53 estudios, 166 comparaciones. Efecto moderado a favor de resolver un problema antes de recibir la instrucción (PS-I): Hedges g = 0,36 [0,20; 0,51]; entre 0,37 y 0,58 cuando se aplica con alta fidelidad a los principios de la falla productiva; g = 0,87 tras corregir por sesgo de publicación. Tendencias opuestas en alumnos de segundo a quinto grado y en el aprendizaje de habilidades de dominio general, donde favorecen "instrucción primero". Cobertura: matemática, física, química, biología y medicina (según resumen del buscador [S]; dominios de humanidades excluidos). Observar que el g = 0,87 es una estimación de los propios autores y debe tomarse con cautela.
- Kapur (2008), "Productive Failure", *Cognition and Instruction* 26(3), DOI 10.1080/07370000802212669 [M]. Origen de la idea: dejar fallar a los alumnos en un problema que todavía no saben resolver, y después enseñar la solución canónica.
- Loibl, Roll y Rummel (2017), *Educational Psychology Review* 29(4), 693-715, DOI 10.1007/s10648-016-9379-x [S]. Revisión: problema-primero ayuda solo con ciertos rasgos de diseño (casos contrastantes, instrucción que parte de las soluciones de los alumnos). Matiz importante: el resultado depende de cómo se diseña el problema.
- Del buscador: un trabajo de ETH Zurich de 2021 con 118 comparaciones y 33 artículos halló que agregar andamiaje a la fase de problema no mostró diferencia significativa frente a PS-I [S]. No lo cité como fuente principal porque no pude abrirlo.

**Recurso canónico:** Alfieri et al. (2011) para el estado de la disputa; Sinha y Kapur (2021) para la secuencia.

**Fuentes del componente**

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Alfieri et al. 2011 (URL arriba) | metaanálisis | 3 | 3 | 2 | 3 | [L] |
| Mayer 2004 (Crossref + espejo) | revisión | 3 | 2 | 2 | 2 | [M] |
| Kirschner, Sweller y Clark 2006 (https://doi.org/10.1207/s15326985ep4102_1) | artículo de posición | 3 | 3 | 1 | 3 | [M] |
| Hmelo-Silver, Duncan y Chinn 2007 (https://doi.org/10.1080/00461520701263368) | réplica | 3 | 2 | 2 | 3 | [M] |
| Sinha y Kapur 2021 (https://doi.org/10.3102/00346543211019105) | metaanálisis | 3 | 3 | 2 | 3 | [L abstract] |
| Loibl, Roll y Rummel 2017 (https://link.springer.com/10.1007/s10648-016-9379-x) | revisión | 3 | 2 | 2 | 2 | [S] |

## Componente 2: Aprendizaje activo en clase

- Freeman et al. (2014), *PNAS* 111(23), "Active learning increases student performance in science, engineering, and mathematics". Texto leído en https://www.bu.edu/eng/files/2025/01/Active-learning-increases-student-performance-in-science-engineering-and-mathematics.pdf [L]. 225 estudios, grupos de clase con algo de aprendizaje activo contra exposición magistral continua. Examen/inventarios: +0,47 desviaciones (158 estudios). Reprobación: 21,8% con aprendizaje activo contra 33,8% con clase magistral, odds ratio 1,95 de reprobar con clase magistral. Los números de 21,8% y 33,8% son promedios de la muestra, y el "55% más" que circula es una diferencia relativa entre ellos, no el odds ratio. Los autores calcularon números "fail-safe" (114 estudios para exámenes, 438 para reprobación) para descartar sesgo de publicación, y el efecto es similar con asignación aleatoria (0,514, 16 estudios) y con otros diseños. Declaran que el beneficio es mayor en clases chicas y en inventarios conceptuales; "aprendizaje activo" cubre intervenciones muy distintas.
- Chi y Wylie (2014), "The ICAP Framework", *Educational Psychologist*, DOI 10.1080/00461520.2014.965823 [M]. Marco de lo que significa "activo": pasivo, activo, constructivo, interactivo. No leí el texto.
- Peer instruction (Porter, Bailey Lee y Simon 2013, SIGCSE, DOI 10.1145/2445196.2445250 [M]): la cifra "baja 61% la tasa de reprobados" viene de material propio y no la verifiqué en la fuente. Ver componente 8.

**Recurso canónico:** Freeman et al. (2014).

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Freeman et al. 2014 (URL arriba) | metaanálisis | 3 | 3 | 2 | 3 | [L] |
| Chi y Wylie 2014 | marco teórico | 3 | 2 | 2 | 2 | [M] |

## Componente 3: Aprendizaje basado en problemas y en proyectos

- Dochy, Segers, Van den Bossche y Gijbels (2003), *Learning and Instruction* 13(5), 533-568, DOI 10.1016/S0959-4752(02)00025-7. Resumen en https://cris.maastrichtuniversity.nl/en/publications/effects-of-problem-based-learning-a-meta-analysis/ [S]. 43 estudios de educación superior. Efecto positivo robusto en habilidades; en conocimiento el efecto combinado fue negativo pero dependiente de dos estudios y sin significación en el conteo de votos (no robusto); los alumnos de PBL aprenden algo menos al principio y recuerdan más con el tiempo.
- Strobel y van Barneveld (2009), *Interdisciplinary Journal of Problem-based Learning* 3(1), DOI 10.7771/1541-5015.1046. https://docs.lib.purdue.edu/ijpbl/vol3/iss1/4/ [S]. Metasíntesis de ocho metaanálisis: PBL gana en retención a largo plazo, habilidades y satisfacción; la instrucción tradicional gana en retención de corto plazo medida con exámenes estandarizados.
- Discrepancia con la posición A: Kirschner et al. cuentan PBL entre los métodos de mínima guía y predicen resultados peores; los metaanálisis de PBL dan resultados mixtos que dependen de qué se mide. Ambos pueden ser ciertos: PBL con andamiaje no es "mínima guía" (Hmelo-Silver et al.) y el conocimiento de corto plazo puede rendir menos.
- Hueco: no encontré metaanálisis de **aprendizaje basado en proyectos** distinto de PBL, ni nada sobre adultos que aprenden tecnología.

**Recurso canónico:** Strobel y van Barneveld (2009) para orientarse; Dochy et al. (2003) para el detalle.

## Componente 4: Tutoría uno a uno y en grupos chicos

### El problema de las dos sigmas y su revisión

- Bloom (1984), "The 2 Sigma Problem", *Educational Researcher* 13(6), DOI 10.3102/0013189X013006004 [M]. Afirmó que el alumno promedio con tutoría individual más aprendizaje de dominio rinde dos desviaciones estándar por encima de la clase.
- Von Hippel (2024), "Two-Sigma Tutoring: Separating Science Fiction from Science Fact", *Education Next*, https://www.educationnext.org/wp-content/uploads/2024/03/ednext_XIV_2_von_hippel.pdf [L parcial]. Sostiene que el efecto de dos sigmas salió de dos tesis doctorales (Anania y Burke) con grupos de unos 30 alumnos, que "it wasn't just tutoring" (se combinó con dominio), y que "it's never been replicated". Entre los 96 estudios de Nickow et al. "none produced a two-sigma effect". La fecha de publicación varía entre fuentes (el PDF dice primavera de 2024).
- VanLehn (2011), "The Relative Effectiveness of Human Tutoring, Intelligent Tutoring Systems, and Other Tutoring Systems", *Educational Psychologist* 46(4), DOI 10.1080/00461520.2011.611369. Abstract leído vía ERIC: https://eric.ed.gov/?id=EJ946764 [L]. Se creía que los sistemas basados en respuesta, los tutores inteligentes y los tutores humanos expertos rendían d = 0,3, 1,0 y 2,0; la revisión "did not confirm these beliefs": tutoría humana d = 0,79, tutores inteligentes d = 0,76. Según el buscador, la conclusión de la hipótesis de meseta es que la efectividad deja de crecer con la granularidad de la interacción [S].

### Tutoría de alta dosis

- Nickow, Oreopoulos y Quan (2020), NBER w27476, https://www.nber.org/papers/w27476 [L resumen]. Efecto combinado 0,37 desviaciones estándar en ensayos aleatorizados de preescolar a 12.º; mayor con maestros o paraprofesionales que con voluntarios o padres; mayor en grados tempranos; mayor dentro de la jornada que después. J-PAL cita 96 evaluaciones aleatorizadas [S]. **Discrepancia**: la versión publicada en *American Educational Research Journal* (2023, DOI 10.3102/00028312231208687) reportaría 0,288 con 89 estudios y tutorías de al menos tres veces por semana [S, solo metadatos del buscador]. Citar el borrador de 2020 con su cifra o la versión de 2023 con la suya, nunca mezclar.
- Es evidencia de escuela primaria y secundaria. No hay metaanálisis equivalente que haya encontrado para adultos aprendiendo habilidades técnicas (hueco).

### Qué hacen los buenos tutores

- Chi, Siler, Jeong, Yamauchi y Hausmann (2001), "Learning from human tutoring", *Cognitive Science* 25(4), DOI 10.1207/s15516709cog2504_1 [L abstract]. Contrastaron tres hipótesis (centrada en el tutor, en el alumno, interactiva). En el segundo estudio, los tutores no podían dar explicaciones ni retroalimentación, solo hacer preguntas guía, y "students learned just as effectively even when tutors were suppressed from giving explanations and feedback". Lo atribuyen a la construcción del alumno y a más episodios de andamiaje.
- Lepper y Woolverton (2002), "The wisdom of practice", en Aronson (ed.), *Improving Academic Achievement* [S, abstract de un sitio secundario con resumen generado; sin verificar contra el capítulo]: tutores expertos usan un enfoque predominantemente socrático, pistas graduales, retroalimentación indirecta para bajar la presión evaluativa, y equilibran transferencia de información con apoyo emocional.

### Grupos chicos y colaboración (EEF Toolkit)

La EEF bloquea la descarga; usé el espejo australiano Evidence for Learning, que publica los mismos datos del Toolkit, y el buscador.
- Tutoría uno a uno: +5 meses de progreso, evidencia moderada, 123 estudios (EEF, vía buscador [S]); más en primaria (+6) que en secundaria (+4), menos en matemática (+2) que en lectoescritura (+6).
- Tutoría en grupos chicos: +4 meses, evidencia moderada, 62 estudios, grupos de dos a cinco. "A noticeable reduction in effectiveness" cuando pasan de seis o siete; apuntar a necesidades específicas y entrenar a quien tutorea aumenta el impacto. https://evidenceforlearning.org.au/education-evidence/teaching-learning-toolkit/small-group-tuition/ [L]. Las evaluaciones de los propios proveedores tienden a informar efectos mayores.
- Aprendizaje colaborativo: +5 meses, costo muy bajo, 212 estudios, grupos de tres a cinco con meta compartida; la evidencia figura como **baja** en el espejo australiano pero el Toolkit de 2018 de la EEF decía "extensive evidence" [S]; discrepancia de versión. https://evidenceforlearning.org.au/education-evidence/teaching-learning-toolkit/collaborative-learning-approaches/ [L]. Condición: los de menor rendimiento deben participar activamente.
- Hueco: la página de tutoría entre pares de la EEF no pude abrirla.

**Recurso canónico:** VanLehn (2011) y Nickow et al. (2020) juntos; von Hippel (2024) como corrección de la cita de Bloom.

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| VanLehn 2011 | revisión | 3 | 3 | 2 | 3 | [L abstract] |
| Nickow, Oreopoulos y Quan 2020 | metaanálisis | 3 | 3 | 2 | 3 | [L resumen] |
| von Hippel 2024 | crítica | 2 | 3 | 2 | 3 | [L parcial] |
| Bloom 1984 | informe de investigación | 3 | 2 | 1 | 3 | [M] |
| Chi et al. 2001 | estudio experimental | 3 | 3 | 3 | 3 | [L abstract] |
| Lepper y Woolverton 2002 | capítulo | 2 | 2 | 2 | 3 | [S] |
| EEF / Evidence for Learning (URLs arriba) | síntesis | 3 | 2 | 2 | 2 | [L espejo] |

## Componente 5: Aprendizaje cognitivo y andamiaje

- Collins, Brown y Newman (1989), "Cognitive apprenticeship: Teaching the crafts of reading, writing, and mathematics", en Resnick (ed.), *Knowing, Learning, and Instruction*. Reseña del buscador [S]; sin texto. Seis métodos: modelado, coaching y andamiaje (el núcleo), más articulación, reflexión y exploración. La idea central: el razonamiento experto está oculto y hay que hacerlo visible. Existe un informe técnico de acceso libre de 1986-87 (https://apps.dtic.mil/sti/pdfs/ADA178530.pdf) que no leí. Para el lector: es la descripción más clara de qué hace un mentor que enseña, y encaja con lo que Chi et al. encuentran sobre preguntas y andamiaje.
- Ninguna evidencia verificada de efecto: es un marco de diseño. Hueco.

**Recurso canónico:** Collins, Brown y Newman (1989). **Marca:** [S].

## Componente 6: Mentoría

- Eby, Allen, Evans, Ng y DuBois (2008), "Does mentoring matter?", *Journal of Vocational Behavior* 72(2), 254-267, DOI 10.1016/j.jvb.2007.04.005 [L resumen vía Europe PMC]. Metaanálisis de mentoría juvenil, académica y laboral: asociada con "a wide range of favorable behavioral, attitudinal, health-related" y otros resultados, pero los efectos son generalmente pequeños; la mentoría académica y laboral muestra efectos mayores que la juvenil. Un resumen del buscador da 116 muestras y N de 45.705 con efectos de 0,11 a 0,19 [S]; los números de esa diapositiva no los pude confirmar contra el artículo.
- Kram (1983), "Phases of the Mentor Relationship", *Academy of Management Journal* 26(4), 608-625, DOI 10.2307/255910 [M]. Origen de la distinción entre funciones de carrera y psicosociales y de las cuatro fases de la relación. No leí el texto.
- EEF (vía Evidence for Learning): mentoría +2 meses, evidencia moderada, 44 estudios; los efectos suelen desvanecerse al terminar y los mentores que abandonan pueden perjudicar al mentoreado. https://evidenceforlearning.org.au/education-evidence/teaching-learning-toolkit/mentoring/ [L]. Otro documento de un consejo local basado en el Toolkit lista +1 mes [S]: discrepancia de versión.
- Conclusión para el lector: mentorear no es lo mismo que enseñar. Sirve para actitudes, orientación y carrera con efectos modestos; el aprendizaje de una habilidad lo explican mejor los componentes 4 y 5.

**Recurso canónico:** Eby et al. (2008).

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Eby et al. 2008 | metaanálisis | 3 | 2 | 2 | 3 | [L resumen] |
| Kram 1983 | artículo teórico | 3 | 2 | 1 | 3 | [M] |
| EEF mentoring vía E4L | síntesis | 3 | 1 | 1 | 1 | [L espejo] |

## Componente 7: Didáctica general y didácticas específicas, y PCK

- **Qué es didáctica general frente a específica.** En la tradición alemana, *Allgemeine Didaktik* trata la enseñanza en general y las *Fachdidaktiken* tratan la enseñanza de cada materia; "Fachdidaktik" es difícil de traducir y hay quien dice "subject-matter didactics". Una revisión de 1991 (Plöger) describe un diálogo intenso entre ambas en los 50-60 y propone reconectarlas; un abstract señala que la crisis de la didáctica general fortaleció a las Fachdidaktiken; Meyer sostiene que en Hamburgo estudiantes y docentes piensan "didáctica" como específica de materia; una publicación de 2024 (Vollmer y Rothgangel, *General Subject Didactics*) compara didácticas de materia como disciplinas académicas. Fuente: resultados del buscador sobre https://www.pedocs.de/volltexte/2024/30696/pdf/Vollmer_Rothgangel_2024_General_subject_didactics.pdf [S]. No leí ninguno de estos textos. Hueco: una fuente en castellano o inglés que resuma la distinción.
- **PCK.** Shulman (1986), "Those Who Understand: Knowledge Growth in Teaching", *Educational Researcher* 15(2), 4-14. Texto leído en https://home.miracosta.edu/rfrench/documents/Shulman_1986.pdf [L parcial: el pasaje]. Cita literal: PCK incluye, para los temas más enseñados, "the most useful forms of representation of those ideas, the most powerful analogies, illustrations, examples, explanations, and demonstrations-in a word, the ways of representing and formulating the subject that make it comprehensible to others", y "an understanding of what makes the learning of specific topics easy or difficult: the conceptions and preconceptions that students of different ages and backgrounds bring". Shulman también escribe: "there are no single most powerful forms of representation", y habla de un "armamentarium" de representaciones alternativas.
- Evidencia de que importa: Hill, Rowan y Ball (2005), *American Educational Research Journal* 42(2), DOI 10.3102/00028312042002371 [M]; Baumert et al. (2010), AERJ, DOI 10.3102/0002831209345157 [M]; Sadler et al. (2013), AERJ, DOI 10.3102/0002831213477680 [M]. Solo verifiqué título, año y autores. Los resultados que la literatura les atribuye (el conocimiento matemático para enseñar predice el progreso de los alumnos; en física de secundaria el efecto del conocimiento docente depende de que se corrijan las ideas erróneas) no los pude confirmar.

**Recurso canónico:** Shulman (1986).

## Componente 8: Enseñar programación

- **Panorama.** *The Cambridge Handbook of Computing Education Research* (Fincher y Robins, eds., 2019). Estructura: Parte II (fundamentos: ciencias del aprendizaje, ciencias cognitivas, pedagogía de la educación superior) y Parte III con capítulos 12 "Novice Programmers and Introductory Programming" y 15 "Pedagogic Approaches". https://www.cambridge.org/core/product/F8CFAF7B81A8F6BF5C663412BA0A943D [S]. Luxton-Reilly et al. (2018), "Introductory programming: a systematic literature review", ITiCSE Companion, DOI 10.1145/3293881.3295779 [M]; no leí su contenido. Ericson et al. (2022), "Parsons Problems and Beyond", ITiCSE Working Group Reports, DOI 10.1145/3571785.3574127 [M].
- **Leer y trazar antes de escribir.** Lister et al. (2004), ITiCSE working group, DOI 10.1145/1044550.1041673 [M] y Lopez, Whalley, Robbins y Lister (2008), DOI 10.1145/1404520.1404531 [M]. Solo confirmé título, venue y autores. Lo que la pista propia dice (trazar y explicar explican el 46% de la varianza en escribir código; muchos alumnos no predicen qué hace un fragmento corto) **no está verificado**; son correlaciones, no experimentos.
- **Estrategia explícita de trazado.** Xie, Nelson y Ko (2018), "An Explicit Strategy to Scaffold Novice Program Tracing", SIGCSE, DOI 10.1145/3159450.3159527 [M]. La cifra "+15% en menos de una hora" viene de la pista y no está verificada.
- **Subobjetivos nombrados.** Margulieux, Morrison y Decker (2020), *International Journal of STEM Education* 7, DOI 10.1186/s40594-020-00222-7 [L abstract]. 265 estudiantes de un curso introductorio durante un semestre, mitad con enseñanza orientada a subobjetivos. Mejores notas en quizzes (dentro de una semana de aprender el procedimiento) pero no en exámenes sumativos; menor varianza de notas y menos abandonos y reprobados. Contexto: el abstract dice que las tasas de abandono y reprobación en cursos introductorios "are regularly as high as 50%".
- **PRIMM.** Sentance, Waite y Kallia (2019), *Computer Science Education* 29(2-3), DOI 10.1080/08993408.2019.1608781 [M]. Los detalles (13 escuelas, 500 alumnos de 11 a 14 años, métodos mixtos) vienen de la pista y no están verificados. Es evidencia escolar, no de adultos.
- **Problemas de Parsons.** Ericson et al. (2022), arriba [M]. Que la literatura esté "desordenada y sin réplicas a gran escala" viene de la pista, no verificado.
- **Máquina nocional.** Sorva (2013), "Notional Machines and Introductory Programming Education", *ACM TOCE* 13(2), DOI 10.1145/2483710.2483713 [L abstract vía Crossref resumido]. Argumenta que las máquinas nocionales son un desafío mayor de la programación introductoria y que quienes enseñan deberían convertirlas en objetivo de aprendizaje explícito. Es revisión y posición, no experimento. Nota: el DOI 10.1145/2490822 que parece cercano es otro paper (visualización de programas); no confundirlos.
- **Live coding.** Selvaraj, Zhang, Porter y Soosai Raj (2021), "Live Coding: A Review of the Literature", ITiCSE, DOI 10.1145/3430665.3456382 [M]. Que sea recomendado pero con poca evidencia empírica viene de la pista, no verificado.
- **Peer instruction y pares.** Porter, Bailey Lee y Simon (2013), "Halving fail rates using peer instruction", DOI 10.1145/2445196.2445250 [M]. La cifra de la pista (reducción promedio de 61%) no la verifiqué; el título del artículo habla de reducir a la mitad las tasas de reprobación.

**Recurso canónico:** *Cambridge Handbook of Computing Education Research* (2019) como mapa, Margulieux et al. (2020) como estudio concreto con efecto, Sorva (2013) como marco.

## Componente 9: Enseñar a programar con IA

Dos tipos de evidencia: experimentos sobre aprender con IA y propuestas de diseño.

| Estudio | Diseño | Resultado verificado | Marca |
|---|---|---|---|
| Kazemitabaar et al. 2023, CHI, arXiv 2302.07427 | experimento, 69 novatos de 10 a 17 años, 45 tareas | con Codex, completan 1,15 veces más y puntúan 1,8 veces más en autoría; la modificación manual no empeora; a una semana, mejor pero no significativo; los de mayor puntaje previo en Scratch retienen significativamente más | [L abstract] |
| Prather et al. 2024, ICER, arXiv 2405.17739 | 21 sesiones de laboratorio con observación, entrevistas y seguimiento ocular | quienes usan bien la IA producen el código que ya planeaban; los que tienen dificultades terminan con "an illusion of competence" y sus dificultades metacognitivas pueden empeorar | [L abstract] |
| Kazemitabaar et al. 2025, arXiv 2410.08922 | 82 participantes entre sujetos, luego 42 intra sujetos | la técnica más eficaz hace que el alumno diga qué debe pasar en cada etapa antes de ver el código; es un preprint | [L abstract] |
| Bastani et al. 2025, *PNAS* 122(26), e2422633122 | experimento de campo, casi 1000 estudiantes secundarios de matemática | con GPT-4 en práctica, +48% (GPT Base) y +127% (GPT Tutor); sin acceso, GPT Base 17% por debajo del control; GPT Tutor casi sin daño | [L abstract vía fetch de Crossref] |
| Kestin et al. 2025, *Scientific Reports* 15, 17458, DOI 10.1038/s41598-025-97652-6 | ensayo aleatorizado con universitarios, física | "learn significantly more in less time" con el tutor de IA que con clase de aprendizaje activo; el abstract no da cifras | [L abstract parcial] |
| Denny et al. 2024, *Communications of the ACM* 67(2), DOI 10.1145/3624720 | artículo de posición | autores: Denny, Prather, Becker y otros; no leí el contenido | [M] |

- Patrón: la IA sin guía sube el desempeño durante la práctica y no necesariamente lo aprendido (Bastani), ayuda más a quien ya sabía (Kazemitabaar 2023, Prather) y los diseños que obligan a predecir o explicar antes de mostrar el código funcionan mejor (Kazemitabaar 2025). Cuidado: dos de los cinco estudios son de menores y uno de matemática, no de programación; Kestin es física. Ninguno es de adultos aprendiendo programación.
- La pista propia agrega estudios (Bassner 2025, Zi 2025, Xiao 2026, Perry 2023, etc.) que **no verifiqué**.

**Recurso canónico:** no hay uno estable; Bastani et al. (2025) para el riesgo y Kazemitabaar et al. (2025) para el diseño, sabiendo que el campo cambia rápido.

## Componente 10: Ciencias

Sin evidencia verificada. Solo tengo metadatos de Sadler et al. (2013) (conocimiento docente y aprendizaje de física en secundaria) y de Hill, Rowan y Ball (2005) y Baumert et al. (2010) para matemática (ver componente 7). No busqué didáctica de las ciencias por agotamiento del cupo de búsquedas. **Hueco completo.** Pistas para cerrarlo: ideas previas y concepciones erróneas; indagación guiada frente a descubrimiento (componente 1); *Taking Science to School* (NRC 2007, sin verificar); Hake (1998) sobre interacción en clase (sin verificar).

## Componente 11: Idiomas

Cubierto por el tema `Ingles/` de la base (entrada `Ingles/ingles.md`: adquisición, pronunciación, gramática, léxico, discurso y práctica; su fuente de práctica es Nation y su marco de niveles el MCER). Ese tema está escrito desde quien aprende y "no cubre la didáctica para docentes"; esta nota solo debe enlazarlo y marcar que enseñar un idioma tiene su didáctica propia (hueco) sin repetir lo que ya dice.

## Huecos declarados

1. **Texto completo de casi todos los artículos.** Salvo Alfieri, Freeman, Shulman (pasaje) y partes de von Hippel, trabajé con abstracts y metadatos.
2. **Kirschner et al. 2006, Mayer 2004 y Hmelo-Silver et al. 2007**: sin abstract literal; la disputa está reconstruida de resúmenes.
3. **EEF directa**: bloqueada; datos del espejo australiano y del buscador, con discrepancias de versión (mentoría +1 vs +2; colaborativo con evidencia baja vs "extensive").
4. **Nickow 2023 vs 2020**: dos cifras (0,288 y 0,37) sin resolver desde la fuente.
5. **Didácticas específicas**: ciencias sin evidencia; idiomas sin didáctica propia; Fachdidaktik sin fuente leída.
6. **Aprendizaje por proyectos** (distinto de PBL), tutoría de adultos en habilidades técnicas y mentoría en IT: no encontré metaanálisis.
7. **Aprendizaje cognitivo**: sin estudio de efecto.
8. **Materia propia sin verificar**: cifras de Lopez et al., Xie et al., Porter et al., Ericson et al., Sentance et al., Selvaraj et al. y los estudios de IA no abiertos. Solo se citan como pista.
9. **Los libros** que menciona la pista (4C/ID, Teaching Tech Together, etc.) no los revisé; las escuelas de IT tampoco.

## Propuesta de componentes para el tema

1. **Cuánta guía y cuándo** (la disputa guía vs. descubrimiento y la secuencia problema-primero).
2. **Aprendizaje activo en clase** (Freeman, ICAP, pares).
3. **Problemas y proyectos** (PBL y aprendizaje por proyectos).
4. **Tutoría** (uno a uno y en grupos chicos: dosis, quién la da, qué hacen los buenos tutores).
5. **Andamiaje y aprendizaje cognitivo** (modelado, coaching, desvanecer, articular).
6. **Mentoría** (carrera y acompañamiento, separada de enseñar).
7. **Didáctica general y específica** (Fachdidaktik, PCK).
8. **Enseñar programación** (leer antes de escribir, subobjetivos, máquina nocional, pares).
9. **Enseñar a programar con IA** (aparte porque cambia rápido y su evidencia es corta).
10. Ciencias e idiomas como notas breves: la de idiomas, un enlace a `Ingles/`; la de ciencias, a escribir después de investigar.

Si se quiere menos notas: unir 1 y 3; unir 4 y 5; mantener 6 aparte.
