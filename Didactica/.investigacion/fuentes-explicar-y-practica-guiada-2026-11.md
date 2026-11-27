---
resumen: >-
  Búsqueda de fuentes para los avisos «Sin fuente todavía» de cinco notas de Explicar y modelar y Práctica guiada (issue #151), y corrección de las páginas de van de Pol et al. (2010).
creado: 2026-11-27
---

# Fuentes para Explicar y modelar y Práctica guiada (issue #151)

Cinco avisos en cinco notas, más una corrección de páginas en dos. No se cerró ninguno del todo, pero los cinco se achicaron. En dos notas aparecieron disputas nuevas: el *live coding* (Wilson contra los estudios comparativos) y el origen de la liberación gradual (Campione, no Vygotsky, en el informe técnico de Pearson y Gallagher).

Los extractos en inglés son literales de lo que se leyó. Los dos informes técnicos de ERIC son escaneos con OCR; las erratas del OCR se corrigieron solo donde eran obvias («Teachirg», «scaffolaing»).

## 0. Páginas de van de Pol, Volman y Beishuizen (2010)

**Notas**: `Practica-guiada-y-andamiaje/andamiaje.md` y `Practica-guiada-y-andamiaje/practica-guiada-y-andamiaje.md` daban 271-297.

**Se encontró**:

- Crossref (`https://api.crossref.org/works/10.1007/s10648-010-9127-6`): `page: 271-296`, volumen 22, número 3, septiembre de 2010.
- El PDF de la versión publicada que aloja la VU (`https://research.vu.nl/ws/files/2755348/252440.pdf`) lleva en el encabezado de cada página «Educ Psychol Rev (2010) 22:271–296».
- La portada que agrega el repositorio de la VU dice, en cambio, «Educational Psychology Review, 22(3), 271-297». De ahí venía el error.
- La página de Springer no abrió (redirige a un login).

**Qué se cambió**: 271-296 en las dos notas.

**Fuera de mis archivos, con el mismo 271-297**: `Psicologia-infantil/.investigacion/huecos-desarrollo-y-fundamentos.md` (línea 19) y `Didactica/.investigacion/explicita-practica-preguntas-feedback.md` (línea 115). Son informes; no se editaron. `Ciencias-del-aprendizaje/.investigacion/fuentes-aprender-con-otros-2026-11.md` ya había señalado la discrepancia.

## 1. Instrucción Directa (`Explicar-y-modelar/instruccion-directa.md`)

**Faltaba**: una revisión neutral y reciente de Follow Through, y el texto del informe de Abt (Stebbins et al. 1977).

**Se encontró**:

- Stebbins et al. (1977), *Education as Experimentation: A Planned Variation Model. Volume IV-A: An Evaluation of Follow Through*. Registro de ERIC ED148490, https://eric.ed.gov/?id=ED148490. **Solo el resumen**: ERIC no tiene el texto (`e_fulltextauth: 0`; el PDF redirige a la portada de ERIC). Extracto: «discusses the evaluation of the progress of Cohort III entering-kindergarten children during 4 years of Follow Through participation».
- Stebbins et al. (1976), *Volume IIIA: Findings: Cohort II; Interim Findings: Cohort III*. ERIC ED148489, https://eric.ed.gov/?id=ED148489. **Solo el resumen**: «reviews the background of the study, describes 13 of the Follow Through models involved, and presents an analysis of the effects of these models on students».
- Una búsqueda de fecha, editorial y otros datos del volumen IV-A dio un catálogo de Bank Street («Abt Associates, April 15, 1977»), que no se abrió.
- Revisión neutral reciente: no se encontró. Hay un reanálisis favorable a la Instrucción Directa, Bereiter y Kurland (1981), *A constructive look at Follow Through results*, Interchange 12(1):1-22 (doi 10.1007/BF01807392). Solo se vieron sus metadatos en Crossref; no se leyó y no se agregó a la nota.

**Qué se cambió**: la fuente de Stebbins apunta al registro de ERIC y se agregó el volumen III. Una oración en la posición de Abt (cohorte III, cuatro años) y otra que dice que el registro del volumen III coincide con House et al. en los 13 modelos. El aviso se achicó: el informe de Abt figura en ERIC sin texto.

**Sigue faltando**: el texto del informe de Abt y una revisión neutral reciente.

## 2. Live coding (`Explicar-y-modelar/modelado-y-ejemplos-resueltos.md`)

**Faltaba**: si programar en vivo rinde distinto que mostrar código ya escrito, y qué dice *Teaching Tech Together* en su capítulo sobre el tema.

**Se encontró**:

- Wilson, G. (2019), *Teaching Tech Together*, Taylor & Francis (ISBN 978-0-367-35328-5, según la página del libro). Sección 8.1, «Live Coding», en https://teachtogether.tech/en/index.html (ancla `s:performance-live`). **Texto completo de la sección**. Extractos:
  - «The most effective way to teach programming is live coding [Rubi2013,Haar2017,Raj2018]. Instead of presenting pre-written material, the teacher writes code in front of the class while the learners follow along, typing it in and running it as they go.»
  - Razones: «It slows the teacher down»; «Learners get to see how to diagnose and correct mistakes»; «Another benefit of live coding is that it demonstrates the order in which programs should be written.»
  - «The most important rule of live coding is to embrace your mistakes. No matter how well you prepare, you will make some; when you do, think through them with your audience.»
  - En la bibliografía del libro: Rubi2013 «Reports that live coding is as good as or better than using static code examples»; Raj2018 «A grounded theory analysis of live coding that includes references to previous works»; Haar2017 «An early look at live streaming of coding as a teaching technique».
- Rubin, M. J. (2013), *The effectiveness of live-coding to teach introductory programming*, SIGCSE '13, págs. 651-656, doi 10.1145/2445196.2445388. **Abstract** (OpenAlex): «The research design includes two experimental groups spread across four sections of an introductory C++ course at Colorado School of Mines.» «In the control group, students were taught using static code, meaning that instructors never typed, but instead viewed, compiled, and executed code examples.» «Based on our results, we conclude that teaching via live-coding is as good as if not better than using static code examples.»
- Soosai Raj, Patel, Halverson y Halverson (2018), *Role of Live-coding in Learning Introductory Programming*, Koli Calling '18, doi 10.1145/3279720.3279725. **Abstract** (OpenAlex): «We conducted a grounded theory analysis of the student feedback data». No se agregó a `fuentes`; se lo nombra en la disputa como lo que es.
- Shah, Hogan, Agarwal, Driscoll, Porter, Griswold y Soosai Raj (2023), *An Empirical Evaluation of Live Coding in CS1*, ICER '23, págs. 476-494 (Crossref), doi 10.1145/3568813.3600122. **Abstract** en la página del congreso, https://icer2023.acm.org/details/icer-2023-papers/34/An-Empirical-Evaluation-of-Live-Coding-in-CS1. Extractos:
  - «In our treatment-control quasi-experimental setup, one lecture group saw live-coding examples while the other saw only static-code ones. Both lecture groups were taught by the same instructor, were taught the exact same content, and completed the same assignments and exams.»
  - «Our findings did not show that live coding improved students' programming processes or performance in the course.»
  - «Student feedback suggests that more students in the live-coding group felt that lectures were too fast and failed to facilitate note-taking».
- Selvaraj et al. (2021), ya citado en la nota: OpenAlex da págs. 164-170. No se cambió en la nota (el formato de la nota no lleva páginas para esa entrada).
- También apareció Shah et al. (2025), *An Empirical Evaluation of Active Live Coding in CS1*, ACM TOCE, doi 10.1145/3743686 (abstract en Crossref): «findings showing that this form of live coding imparts similar learning to static-code examples». Compara dos formas de live coding entre sí; no se agregó a la nota.

**Qué se cambió**: un párrafo con lo que dice *Teaching Tech Together*, y un `[!IMPORTANT]` con las dos posiciones: Wilson («the most effective way») contra Rubin y Shah et al. (rinde igual que el código estático). La disputa señala que de las tres citas de Wilson solo Rubin compara con código estático. El aviso se achicó.

**Sigue faltando**: un experimento aleatorizado; Rubin y Shah et al. se leyeron solo por su abstract.

**Fuera de mis archivos**: `Didactica/Didacticas-especificas/ensenar-programacion.md` (línea 56) trata el *live coding* solo con Selvaraj. Le serviría la misma disputa. No se editó.

## 3. Aprendizaje para el dominio (`Practica-guiada-y-andamiaje/practica-independiente-y-dominio.md`)

**Faltaba**: el texto de Kulik et al. (1990) con su tamaño de efecto, la ficha de la EEF y la evidencia posterior a 1990.

**Se encontró**:

- Kulik, Kulik y Bangert-Drowns (1990), Review of Educational Research 60(2):265-299 (Crossref), doi 10.3102/00346543060002265. **Abstract** en OpenAlex (más largo que el de ERIC EJ415887): «A meta-analysis of findings from 108 controlled evaluations showed that mastery learning programs have positive effects on the examination performance of students in colleges, high schools, and the upper grades in elementary schools. The effects appear to be stronger on the weaker students in a class, and they also vary as a function of mastery procedures used, experimental designs of studies, and course content. Mastery programs have positive effects on student attitudes toward course content and instruction but may increase student time on instructional tasks. In addition, self-paced mastery programs often reduce the completion rates in college classes.» El abstract no da tamaño de efecto. El texto no se consiguió (JSTOR y SAGE cerrados; scispace devuelve un archivo vacío).
- Sobre el 0,52: un buscador lo encontró en Slavin (1987), que atribuye 0,52 y 0,54 a Kulik et al. **1986**, otra revisión. Solo se vio en el resumen del buscador; no se verificó. Puede ser el origen de la cifra que la nota no usa.
- EEF, Teaching and Learning Toolkit, «Mastery learning», https://educationendowmentfoundation.org.uk/education-evidence/teaching-learning-toolkit/mastery-learning. **Texto completo de la ficha** (abrió con curl y un User-Agent de navegador). Extractos:
  - «Moderate impact for very low cost based on limited evidence»; «+5 months».
  - «Learners must demonstrate mastery on unit tests, typically 80%, before moving on to new material.»
  - «The impact of mastery learning approaches is an additional five months progress, on average, over the course of a year.»
  - «There is large variation behind the average impact – mastery learning approaches have consistently positive impacts, but effects are higher for primary school pupils and in mathematics.»
  - «Mastery learning approaches are often associated with direct instruction, but many of the high impact studies identified included elements of collaborative learning.»
  - «mastery learning approaches have consistently positive impacts, but effects are higher for primary school pupils and in mathematics.»
  - «It seems to be important that a high bar is set for achievement of ‘mastery’ (usually 80% to 90% on the relevant test). By contrast, the approach appears to be much less effective when pupils work at their own pace».
  - «Studies involving primary school pupils have tended to be more effective (+8 months) than for secondary school pupils (+ 3 months).» «Effects are higher in mathematics and science (+6 months) than reading (+3 months).»
  - «The security of the evidence around mastery learning is rated as low. 80 studies were identified that meet the inclusion criteria of the Toolkit.» Perdió dos candados por «A small percentage of studies that have taken place recently» y «A large percentage of the studies are not randomised controlled trials».
  - «Number of studies 80»; «Review last updated September 2021».

**Qué se cambió**: el párrafo de Kulik usa el abstract (debilidad de los flojos, variación, menor finalización en programas a ritmo propio). Un párrafo nuevo con la ficha de la EEF. En el `[!IMPORTANT]`, la primera posición se apoya ahora en el abstract de Kulik y en la EEF; lo de Arlin (1984) sigue atribuido a la Wikipedia. El aviso se achicó.

**Sigue faltando**: el texto de Kulik et al. con su tamaño de efecto, la crítica de las pruebas hechas por los investigadores en su fuente primaria (Slavin 1987, que la nota atribuye a la Wikipedia) y la lista de estudios de la EEF con su fecha.

## 4. Andamiaje (`Practica-guiada-y-andamiaje/andamiaje.md`)

**Faltaba**: el texto de Pearson y Gallagher (1983), de Renkl et al. (2002) y de Wood, Bruner y Ross (1976); un estudio de efecto del andamiaje humano con adultos.

**Se encontró**:

- Pearson, P. D. y Gallagher, M. C. (octubre de 1983), *The Instruction of Reading Comprehension*, Technical Report No. 297, Center for the Study of Reading (Universidad de Illinois) y Bolt Beranek and Newman. ERIC ED236565, https://files.eric.ed.gov/fulltext/ED236565.pdf. **Texto completo** (escaneo de 54 págs.). Extractos de la sección del modelo:
  - «What appears warranted from all these studies is a particular model of instruction which we have extrapolated from Campione (1981).»
  - «The diagonal line on the graph represents a journey from total teacher responsibility (on the far left) to total student responsibility (on the far right). When the teacher is taking all or most of the responsibility for task completion, he is "Modeling" or demonstrating the desired application of some strategy. When the student is taking all or most of that responsibility, she is "practicing" or "applying" that strategy. What comes in between these two extremes is the gradual release of responsibility from teacher to student, or what Rosenshine might call "guided practice."»
  - «The critical stage of the model is the "guided practice," the stage in which the teacher gradually releases task responsibility to students.»
  - La nota dice ahora que, según ellos, Rosenshine «might call» práctica guiada a ese tramo; antes decía que la «equiparan» (corregido tras el cotejo).
  - En la bibliografía, Campione es una ponencia: «Paper delivered at the Second Annual Conference on Reading Research of the [Center for the] Study of Reading, New Orleans, April 1981».
  - Una búsqueda en el texto («ygot», «Wood», «Bruner») no encuentra a Vygotsky ni a Wood, Bruner y Ross; solo «Norwood», de una editorial. El OCR puede fallar, pero el modelo se atribuye a Campione.
- Versión de revista: Pearson y Gallagher (1983), Contemporary Educational Psychology 8(3):317-344 (Crossref), doi 10.1016/0361-476X(83)90019-X; ERIC EJ289063. **No leída**.
- Renkl, Atkinson, Maier y Staley (2002), *From Example Study to Problem Solving: Smooth Transitions Help Learning*, Journal of Experimental Education 70(4):293-315, doi 10.1080/00220970209599510. **Abstract** (OpenAlex): «the authors proposed a successive integration of problem-solving elements into example study until the learners solved problems on their own». «The authors tested the effectiveness of such a fading procedure against the traditional method of using example-problem pairs.» «In a field experiment and in 2 more controlled laboratory experiments, the authors found that (a) the fading procedure fosters learning, at least when near transfer performance is considered; (b) the number of problem-solving errors during learning plays a role in mediating this effect; and (c) it is more favorable to fade out worked-out solution steps in a backward manner (omitting the last solution steps first) as compared with a forward manner (omitting the first solution steps first).» El PDF del autor que ofrece Semantic Scholar (uni-freiburg) da «NotFound».
- Wood, Bruner y Ross (1976): Crossref confirma Journal of Child Psychology and Psychiatry 17(2):89-100, abril de 1976. El PDF de Wiley y la página del artículo dan 403; PubMed (PMID 932126) no tiene abstract. **No leído**.
- Estudio de efecto del andamiaje humano con adultos: no se buscó aparte (tres rondas se fueron en los originales).

**Qué se cambió**:

- La liberación gradual ahora se describe con el informe técnico: el gráfico de responsabilidad, «the critical stage» y la equivalencia con la práctica guiada de Rosenshine.
- Disputa nueva: la nota decía, por fuentes secundarias, que Pearson y Gallagher se apoyaron en Vygotsky y en Wood, Bruner y Ross. El informe técnico atribuye el modelo a Campione (1981) y no los cita. Se dejó un `[!IMPORTANT]` con las dos posiciones, porque la versión de revista no se leyó.
- Renkl et al. pasa de «según fuentes secundarias; el original no se leyó» a lo que dice su abstract, con el retiro hacia atrás.
- Páginas de van de Pol (sección 0). Pearson y Gallagher y Renkl con título completo y enlace. La Wikipedia queda como fuente terciaria aparte.
- El aviso se achicó.

**Sigue faltando**: Wood, Bruner y Ross en su fuente (el rompecabezas de pirámide sigue por fuentes secundarias), Renkl entero, la versión de revista de Pearson y Gallagher y un estudio con adultos.

**Fuera de mis archivos**: `Didactica/.investigacion/explicita-practica-preguntas-feedback.md` (línea 130) repite lo de Vygotsky y Wood. Es un informe; no se editó. Ninguna otra nota lo repite (grep de «Pearson y Gallagher» en todo el repo).

## 5. Aprendizaje cognitivo (`Practica-guiada-y-andamiaje/aprendizaje-cognitivo.md`)

**Faltaba**: el texto de Collins, Brown y Newman (1989) o su informe técnico, y algún estudio que mida el efecto del modelo completo.

**Se encontró**: Collins, A., Brown, J. S. y Newman, S. E. (enero de 1987), *Cognitive Apprenticeship: Teaching the Craft of Reading, Writing, and Mathematics*, Technical Report No. 403, Center for the Study of Reading (Universidad de Illinois) y BBN Laboratories. ERIC ED284181, https://files.eric.ed.gov/fulltext/ED284181.pdf. **Texto completo** (escaneo de 37 págs.). Extractos:

- «The following six teaching methods fall roughly into three groups: The first three (modelling, coaching, and scaffolding) are the core of cognitive apprenticeship, designed to help students acquire an integrated set of cognitive and metacognitive skills through processes of observation and of guided and supported practice. The next two (articulation and reflection) are methods designed to help students both to focus their observations of expert problem solving and to gain conscious access to (and control of) their own problem-solving strategies. The final method (exploration) is aimed at encouraging learner autonomy not only in carrying out expert problem solving processes, but also in defining or formulating the problems to be solved.»
- «Modelling involves showing an expert carrying out a task so that students can observe and build a conceptual model of the processes that are required to accomplish the task. In cognitive domains, this requires the externalization of usually internal (cognitive) processes». Ejemplo: «a teacher might model the reading process by reading aloud in one voice, while verbalizing her thought processes […] in another voice».
- «Coaching consists of observing students while they carry out a task and offering hints, scaffolding, feedback, modelling, reminders, and new tasks».
- «A requisite of such scaffolding is accurate diagnosis of the student's current skill level». «Fading consists of the gradual removal of supports until students are on their own.»
- «Exploration is the natural culmination of the fading of supports.»
- Sobre la enseñanza recíproca (Palincsar y Brown), uno de los tres métodos que toma: «In a pilot study with individual students who were poor readers, the method raised subjects' reading comprehension test scores from 15% to 85% accuracy after about 20 training sessions.» «In classroom studies with groups of five students, test scores increased from about 40% to 75% correct».

ERIC también registra Collins et al. (1991), *Cognitive Apprenticeship: Making Things Visible*, American Educator (EJ440511), versión de divulgación. No se leyó.

**Qué se cambió**: la descripción de los seis métodos y su agrupación sale ahora del informe técnico, no de una reseña. Una oración con la cita de la externalización y el ejemplo de la lectura en voz alta. Un párrafo con las cifras de la enseñanza recíproca, aclarando que son de un método que el modelo toma y no del modelo entero. Fuente nueva con el informe de ERIC; la de DTIC queda como posible copia no leída. El aviso se achicó.

**Sigue faltando**: el capítulo de 1989 en Resnick (ed.) y un estudio de efecto del modelo completo.

## 6. Práctica guiada (`Practica-guiada-y-andamiaje/practica-guiada-y-andamiaje.md`)

Sin aviso. Solo la corrección de páginas de van de Pol (sección 0) y este informe en `fuentes`.

## Para otros grupos

- `Didactica/Didacticas-especificas/ensenar-programacion.md`: el *live coding* podría llevar la disputa de la sección 2 (Rubin 2013, Shah et al. 2023).
- `Psicologia-infantil/.investigacion/huecos-desarrollo-y-fundamentos.md` y `Didactica/.investigacion/explicita-practica-preguntas-feedback.md`: van de Pol con 271-297.
- `Didactica/.investigacion/explicita-practica-preguntas-feedback.md` (línea 130): Pearson y Gallagher «apoyándose en Vygotsky (1978) y en Wood, Bruner y Ross (1976)», que el informe técnico no sostiene.
