---
resumen: >-
  Búsqueda de fuentes para los avisos «Sin fuente todavía» de Propositos e Instrumentos de Evaluacion-educativa, más la definición de acuerdo absoluto (issue #153).
creado: 2026-11-27
---

# Fuentes para los avisos de Propósitos e Instrumentos (issue #153)

Seis avisos en seis notas, más la definición de «acuerdo absoluto» del glosario. Ninguno se cerró del todo. Se achicaron cinco: evaluación como aprendizaje, rúbrica, tareas de desempeño, autoevaluación y pares, y opción múltiple. Quedó igual el de evaluación diagnóstica. La definición de acuerdo absoluto tiene fuente.

Una afirmación quedó disputada: en `rubrica.md`, que el beneficio para corregir tenga más respaldo que el beneficio para aprender.

Los extractos en inglés son literales de lo que se leyó. OpenAlex agotó su cupo diario a mitad de la búsqueda; después se usó Crossref para los abstracts.

## 1. Evaluación como aprendizaje (`Propositos/evaluacion-como-aprendizaje.md`)

**Faltaba**: el tamaño de efecto agrupado de Adesope et al. (2017) y la confirmación del d = 0,4 de transferencia de Pan y Rickard (2018).

**Se encontró**:

- Pan, S. C. y Rickard, T. C. (2018), *Transfer of Test-Enhanced Learning: Meta-Analytic Review and Synthesis*, Psychological Bulletin 144(7):710-756, doi 10.1037/bul0000151. https://sc-pan.github.io/pdf/PR_2018.pdf. **Texto completo** (PDF del autor).
  - «Our review encompassed 192 transfer effect sizes extracted from 122 experiments and 67 published and unpublished articles (N = 10,382) that together comprise more than 40 years of research.»
  - «A random-effects model revealed that testing can yield transferrable learning as measured relative to a nontesting reexposure control condition (d = 0.40, 95% CI [0.31, 0.50]).»
  - «That transfer of learning is greatest across test formats, to application and inference questions, to problems involving medical diagnoses, and to mediator and related word cues; it is weakest to rearranged stimulus-response items, to untested materials seen during initial study, and to problems involving worked examples.»
  - «Moderator analyses further indicated that response congruency and elaborated retrieval practice, as well as initial test performance, strongly influence the likelihood of positive transfer.»
  - «However, the intercept predictions were substantially reduced, often indicating no positive transfer when none of the aforementioned moderators are present.»
- Adesope, O. O., Trevisan, D. A. y Sundararajan, N. (2017), *Rethinking the Use of Tests: A Meta-Analysis of Practice Testing*, Review of Educational Research 87(3):659-701, doi 10.3102/0034654316689306. **Abstract** (OpenAlex y el repositorio de WSU): «Results reveal that practice tests are more beneficial for learning than restudying and all other comparison conditions.» El abstract no da el g agrupado. El PDF que citaba la nota (education.wsu.edu/documents/2018/01/rethinking-use-tests.pdf/) hoy redirige a la portada de la facultad, y OpenAlex marca el artículo como cerrado. El buscador devuelve cifras secundarias contradictorias (0,50 a 0,61; 0,67; 0,70); ninguna se usó.

**Qué se cambió**: Pan y Rickard pasa a texto completo; la tabla da d = 0,40 con su intervalo; un párrafo nuevo con dónde la transferencia es mayor y la advertencia por sesgo de publicación. La URL de Adesope pasa al DOI. El aviso se achicó.

**Sigue faltando**: el g agrupado de Adesope y su resultado por formato de prueba.

## 2. Evaluación diagnóstica (`Propositos/evaluacion-diagnostica.md`)

**Faltaba**: una validación de diagnósticos de entrada en capacitación de adultos o en cursos de informática.

**Se buscó**: una ronda en el buscador. Aparecieron estudios de pruebas de aptitud previas a un primer curso de programación universitario (Kerr et al., Universidad de Lancashire, 285 estudiantes; un cuestionario diagnóstico en ASEE; un test cognitivo de programación en *Computers* 2025). Miden aptitud para predecir quién va a aprobar, no conocimiento previo para decidir por dónde empezar, y son con estudiantes de grado. No se leyeron ni se usaron.

**Qué se cambió**: nada.

**Sigue faltando**: lo mismo que decía el aviso.

## 3. Rúbrica (`Instrumentos/rubrica.md`)

**Faltaba**: las cifras de acuerdo de Jönsson y Svingby (2007) y los resultados de Panadero y Jönsson (2013) leídos en el original.

**Se encontró**:

- Jonsson, A., Panadero, E., Pinedo, L. y Fernández-Castilla, B. (2025), *Using rubrics for formative purposes: identifying factors that may affect the success of rubric implementations*, Assessment in Education: Principles, Policy & Practice 32(2):192-211, doi 10.1080/0969594X.2025.2486947. **Texto completo** (acceso abierto; copia en https://deustoteka.deusto.es/bitstreams/250f3dd0-ef57-4a29-b4f6-fb5cf82a94c9/download). Es el trabajo de 2025 que la nota citaba «según el buscador».
  - «However, research findings on such formative use of rubrics are not uniform (Panadero et al., 2023).»
  - Sobre Jönsson y Svingby (2007): «In the first systematic review on the use of rubrics (Jonsson & Svingby, 2007), it was noted that rubrics seem to have the potential of promoting student learning. […] However, due to a small number of studies (n = 25), no strong claims could be made about the formative potential of rubrics at that time.»
  - «This was investigated by analysing 15 'high-quality studies' reporting on rubric interventions.»
  - «Our analysis revealed two key characteristics common to successful interventions: First, teachers explain both the content of the rubric and its application for formative purposes. Second, an effective sequence involves students writing or producing work, followed by feedback or self-assessment, and subsequent revision.»
  - «Taken together, there is substantial evidence supporting the claim that the use of rubrics may have a positive impact on student self-regulation and performance.»
- Panadero, E., Jönsson, A., Pinedo, L. y Fernández-Castilla, B. (2023), *Effects of Rubrics on Academic Performance, Self-Regulated Learning, and Self-Efficacy: a Meta-analytic Review*, Educational Psychology Review 35(4):113, doi 10.1007/s10648-023-09823-4. **Abstract** (OpenAlex). Springer bloqueó la descarga.
  - «After correcting for publication bias, a moderate and positive effect was found in favor of rubrics on academic performance (g = 0.45, k = 21, m = 54, 95% CI [0.312, 0.831]; SMC = 0.38, 95% CI [0.02, 0.75], k = 12, m = 30), whereas a small pooled effect was observed for self-regulated learning (g = 0.23, k = 5, m = 17, 95% CI [-0.15, 0.60]) and for self-efficacy (g = 0.18, k = 3, m = 5, 95% CI [-0.81, 0.91]). Most of the moderator variables were not significant.»
  - Entre los moderadores: «gender, mean age, educational level».
- Messer, M., Brown, N. C. C., Kölling, M. y Shi, M. (2024, v3 de julio de 2025), *How Consistent Are Humans When Grading Programming Assignments?*, preprint arXiv 2409.12967, **sin revisión por pares**. https://arxiv.org/abs/2409.12967. **Texto completo**.
  - «we asked 28 participants to each grade 40 CS1 introductory Java assignments, providing grades and feedback for correctness, code elegance, readability and documentation»; «The 28 participants were divided into seven groups of four».
  - «We measured the inter-rater reliability of the groups using Krippendorff's α – an α > 0.667 is recommended to make tentative conclusions based on the rating. Our groups were inconsistent, with an average α = 0.2 when grading correctness and an average α < 0.1 for code elegance, readability and documentation.»
  - «the rubric we provided our participants was the original rubric from the course».
  - «This highlights that a shared rubric alone is not enough to ensure consistency».
- Jönsson y Svingby (2007), doi 10.1016/j.edurev.2007.05.002, y Panadero y Jönsson (2013), doi 10.1016/j.edurev.2013.01.002: cerrados según OpenAlex; Crossref no trae abstract; el handle de Malmö (hdl.handle.net/2043/6007) dio error 500; la ficha de figshare de 2013 no tiene archivos; CORE dio 403. Un buscador atribuye a Jönsson y Svingby que «most assessments were below the threshold for acceptable reliability», de una cita secundaria; no se usó.

**Contradicción**: la nota afirmaba «El beneficio para corregir tiene más respaldo que el beneficio para aprender», sobre las revisiones de 2007 y 2013. El metaanálisis de 2023 da g = 0,45 sobre el desempeño, y del lado de la corrección no hay cifras leídas y un preprint encontró acuerdo bajo con rúbrica compartida. Se dejó un `> [!IMPORTANT]` con las dos posiciones, en lugar de borrar la frase en silencio.

**Qué se cambió**: el resumen y la primera oración (efecto formativo moderado, g = 0,45, con resultados dispares; la rúbrica sola no garantiza el acuerdo); el dato de los 25 estudios formativos de 2007; dos párrafos nuevos (metaanálisis de 2023 y factores de 2025); la cita de 2025 ya no es «según el buscador»; un párrafo con Messer et al. en la sección de corrección; el paso 5 suma explicar cómo usar la rúbrica para revisar (de Jonsson et al., 2025). El aviso se achicó.

**Sigue faltando**: Jönsson y Svingby (2007) y Panadero y Jönsson (2013) en el original, y el metaanálisis de 2023 entero.

## 4. Tareas de desempeño (`Instrumentos/tareas-de-desempeno.md`)

**Faltaba**: la confiabilidad entre correctores de rúbricas de calidad de código, la revisión de código como instrumento de evaluación, y cuántas tareas hacen falta para generalizar.

**Se encontró**:

- Shavelson, R. J., Gao, X. y Baxter, G. P. (marzo de 1993), *Sampling Variability of Performance Assessments*, CSE Technical Report 361, CRESST/UCLA. https://cresst.org/wp-content/uploads/TECH361.pdf. **Texto completo** del informe técnico. Se publicó como Shavelson, Baxter y Gao (1993) en Journal of Educational Measurement 30(3):215-232 (datos del buscador).
  - «Results at both the individual and school level indicate that rater-sampling variability is not an issue: raters (e.g., teachers, job incumbents) can be trained to consistently judge performance on complex tasks. Rather, task-sampling variability is the major source of measurement error. Large numbers of tasks are needed to get a reliable measure of mathematics and science achievement at the elementary level, or to get a reliable measure of job performance in the military.»
  - «The relative G coefficients were 0.15, 0.21, and 0.32 for the Science, Math, and the CAP studies respectively when only one rater and one task were used. These G coefficients were similar to those reported for the Navy and Marine Corps data, .19 and .12, respectively.»
  - «To reach an approximate .80 relative G coefficient, about 23 tasks would be needed for the Science study, 15 tasks for the Math study, only 8 tasks for the CAP study, 17 tasks for the Navy study, and 35 tasks for the Marine Corps study.»
  - CAP es «California Assessment Program».
- Shavelson, R. J., Wiley, E. W. y Ruiz-Primo, M. A. (1999), *Note on sources of sampling variability in science performance assessments*, Journal of Educational Measurement 36(1):61-71. https://nepc.colorado.edu/publication/note-on-sources-sampling-variability-science-performance-assessments. **Resumen** (página de NEPC, leída con un lector que limita las citas). Extractos: en 1993 habían dicho que «task-sampling variability was the Achilles' heel of science performance assessment»; Cronbach et al. (1997) objetaron que «Task and occasion sampling are confounded because tasks are typically given on only a single occasion»; según el resumen, el reanálisis apoyó esa objeción y atribuyó la variabilidad a las interacciones persona × tarea y persona × tarea × ocasión.
- Messer et al. (2024), arriba en el punto 3. Además:
  - «Only one participant of the 22 who didn't notice that the assignment was a duplicate was awarded the same grade for correctness, code elegance, readability and documentation.»
  - «Seven participants were PhD students, 13 were Masters students, and eight were third-year undergraduate students.» «21 participants had not been assessed before.» «These are a relatively typical profile of those recruited to act as graders at our institution».
  - «This supports the idea that to conduct a consistent assessment, assessors require adequate training to interpret and apply a rubric».
- Indriasari, T. D., Luxton-Reilly, A. y Denny, P. (2020), *A Review of Peer Code Review in Higher Education*, ACM Transactions on Computing Education 20(3):1-25, doi 10.1145/3403935. **Abstract** (Crossref).
  - «We initially identified 187 potential studies and analyzed 51 empirical studies pertinent to our goals. We report the most commonly cited benefits (e.g., the development of programming-related skills) and barriers (e.g., low student engagement)».
  - «While we argue that more empirical work is needed to validate currently reported results related to learning outcomes».

**Tensión, no contradicción con la nota**: Shavelson et al. dicen que los correctores entrenados casi no agregan error; Messer et al., que correctores con rúbrica y sin experiencia acuerdan poco en código. La nota da las dos con su contexto.

**Qué se cambió**: una sección nueva, «Cuántas tareas hacen falta», con Shavelson 1993 y la corrección de 1999; dos párrafos en «Corregir código y proyectos técnicos» (Messer et al. e Indriasari et al.). El aviso se achicó.

**Sigue faltando**: un estudio con revisión por pares sobre el acuerdo en calidad de código, la confiabilidad de la revisión de código entre estudiantes como nota, y estudios de generalizabilidad con tareas de programación o con adultos.

## 5. Autoevaluación y evaluación entre pares (`Instrumentos/autoevaluacion-y-evaluacion-entre-pares.md`)

**Faltaba**: calibración de pares en cursos técnicos y evaluación entre pares con adultos; leer Falchikov y Goldfinch (2000) y la revisión de 2019.

**Se encontró**:

- Double, K. S., McGrane, J. A. y Hopfenbeck, T. N. (2020, en línea en 2019), *The Impact of Peer Assessment on Academic Performance: A Meta-analysis of Control Group Studies*, Educational Psychology Review 32(2):481-509, doi 10.1007/s10648-019-09510-3. **Texto completo** (copia en ORA, Oxford: https://ora.ox.ac.uk/objects/uuid:0a09975c-e7e6-416f-b888-977230b29ba4). Es la «revisión de 2019» de la nota.
  - «High correlations have been observed between peer and teacher assessments in three meta-analyses to date (r = .69, .63, and .68 respectively; Falchikov and Goldfinch 2000; H. Li et al. 2016; Sanchez et al. 2017).»
  - «Here, we present a meta-analysis (54 studies, k = 141) of experimental and quasi-experimental studies»; «An overall small to medium effect of peer assessment on academic performance was found (g = 0.31, p < .001). The results suggest that peer assessment improves academic performance compared with no assessment (g = 0.31, p = .004)».
  - «A meta-regression with tertiary students as the reference category indicated that there was no significant difference in effect size as a function of education level. The effect of peer assessment was similar for secondary students (g = .44, p < .001) and primary school students (g = .41, p = .006) and smaller for tertiary students (g = .21, p = .043).»
- Falchikov, N. y Goldfinch, J. (2000), *Student Peer Assessment in Higher Education: A Meta-Analysis Comparing Peer and Teacher Marks*, Review of Educational Research 70(3):287-322, doi 10.3102/00346543070003287. **Abstract** (OpenAlex; el artículo está cerrado).
  - «Forty-eight quantitative peer assessment studies comparing peer and teacher marks were subjected to meta-analysis.»
  - «Peer assessments were found to resemble more closely teacher assessments when global judgements based on well understood criteria are used rather than when marking involves assessing several individual dimensions. Similarly, peer assessments better resemble faculty assessments when academic products and processes, rather than professional practice, are being rated.»
  - «Hypotheses concerning the greater validity of peer assessments in advanced rather than beginner courses and in science and engineering rather than in other discipline areas were not supported. In addition, multiple ratings were not found to be better than ratings by singletons.»
  - El abstract no da el r = 0,69; esa cifra sale de Double et al.
- Koo y Li (2016), en el punto 7.

**Corrección**: la tabla decía «sin variación por materia ni nivel». El abstract dice algo más acotado: no se confirmó que la validez fuera mayor en cursos avanzados ni en ciencias e ingeniería. La celda ahora dice «48 estudios en educación superior» y el detalle va en un párrafo aparte.

**Qué se cambió**: fuentes nuevas (Double et al. como texto completo, Falchikov y Goldfinch por abstract, Koo y Li); la entrada vieja «según una revisión de 2019 (resumen)» se reemplazó; un párrafo con lo que dice el abstract de Falchikov y Goldfinch (sirve para calibrar pares en cursos técnicos); la definición de acuerdo absoluto con fuente; un párrafo con el efecto de la evaluación entre pares sobre el desempeño. El aviso se achicó y se reescribió.

**Sigue faltando**: el acuerdo absoluto medido entre pares y docentes, la calibración de pares en cursos de programación, la evaluación entre pares con adultos en capacitación y el texto completo de Falchikov y Goldfinch.

## 6. Opción múltiple (`Instrumentos/opcion-multiple.md`)

**Faltaba**: evidencia sobre cuándo la opción múltiple mide comprensión y no solo reconocimiento, y una comparación de la confiabilidad de preguntas abiertas frente a cerradas.

**Se encontró**:

- Rodriguez, M. C. (2003), *Construct Equivalence of Multiple-Choice and Constructed-Response Items: A Random Effects Synthesis of Correlations*, Journal of Educational Measurement 40(2):163-184, doi 10.1111/j.1745-3984.2003.tb01102.x. **Abstract** (Crossref).
  - «Of the 67 studies identified, 29 studies included 56 correlations between items in both formats. These 56 correlations were corrected for attenuation and synthesized to establish evidence for a common estimate of correlation (true-score correlations). The 56 disattenuated correlations were highly heterogeneous.»
  - «When items are constructed in both formats using the same stem (stem equivalent), the mean correlation between the two formats approaches unity and is significantly higher than when using non-stem-equivalent items (particularly when using essay-type items). Construct equivalence, in part, appears to be a function of the item design method or the item writer's intent.»
- Lukhele, R., Thissen, D. y Wainer, H. (1994), *On the Relative Value of Multiple-Choice, Constructed Response, and Examinee-Selected Items on Two Achievement Tests*, Journal of Educational Measurement 31(3):234-250, doi 10.1111/j.1745-3984.1994.tb00445.x. **Abstract** (Crossref; hay una versión previa como ETS Research Report de 1993).
  - «Using analyses based on fitting item response models to data from the College Board's Advanced Placement exams in chemistry and United States history, we found that the constructed response portion of the tests yielded little information over and above that provided by the multiple-choice sections.»
- Adesope et al. (2017): ver punto 1; el dato del formato más eficaz sigue sin verificar. La URL pasa al DOI.

**Qué se cambió**: una sección nueva, «Elegir y producir», con Rodriguez y Lukhele et al., antes de «Para practicar y para acreditar». El aviso se achicó.

**Sigue faltando**: las dos fuentes enteras y una comparación entre opción múltiple y tareas de producción en habilidades prácticas como programar.

## 7. Acuerdo absoluto (`Fundamentos/glosario-de-evaluacion-educativa.md` y `Instrumentos/autoevaluacion-y-evaluacion-entre-pares.md`)

**Faltaba**: una fuente de medición para la definición.

**Se encontró**:

- Koo, T. K. y Li, M. Y. (2016), *A Guideline of Selecting and Reporting Intraclass Correlation Coefficients for Reliability Research*, Journal of Chiropractic Medicine 15(2):155-163, doi 10.1016/j.jcm.2016.02.012. https://pmc.ncbi.nlm.nih.gov/articles/PMC4913118/. **Texto completo** en PMC, leído con un lector que corta las citas largas; los fragmentos van tal cual.
  - «Absolute agreement concerns if different raters assign the same score to the same subject.»
  - «…Conversely, consistency definition concerns if raters' scores to the same group of subjects are correlated…»
  - «…(ie, y = x + c), whereas absolute agreement concerns about the extent to which y equals x.»
  - «…Pearson correlation coefficient is only a measure of correlation, and hence, they are nonideal measures of reliability.»
- Stemler (2004), *A Comparison of Consensus, Consistency, and Measurement Approaches to Estimating Interrater Reliability*, Practical Assessment, Research and Evaluation 9(4), doi 10.7275/96jp-xz07: la página de PARE pide un control antibots (Anubis) y ScholarWorks devolvió HTML. No se leyó.

**Qué se cambió**: la definición del glosario ahora dice «Que dos correctores pongan la misma nota al mismo trabajo, no solo que sus notas se correlacionen (que ordenen parecido los trabajos)» y nombra la definición de «consistencia» del coeficiente intraclase. La nota de pares cita a Koo y Li. Las dos notas suman la fuente.

**Sigue faltando**: nada para la definición. Stemler (2004) sería la fuente de evaluación educativa, si se consigue.

## Fuera del lote o del tema

- `Ingles/Adquisicion/repeticion-espaciada.md` da para Adesope et al. (2017) g = 0,70, «no verificado». Esta búsqueda tampoco lo pudo verificar; el buscador devuelve cifras distintas (0,50 a 0,61, 0,67, 0,70).
- `Evaluacion-educativa/Fundamentos/fuentes-de-evaluacion-educativa.md` lista Jönsson y Svingby y Panadero y Jönsson como la referencia de rúbricas; podría sumar el metaanálisis de Panadero et al. (2023).
- Otras notas que citan Adesope con la URL de WSU que ya no sirve: se buscaron con grep y solo estaban en este lote.

## Después del cotejo

El cotejo contra los extractos llevó a recortar, sin fuente nueva: en rúbrica, «el primer metaanálisis» y los ejemplos de moderadores no significativos; el bloque de disputa ahora suma el resumen de Jönsson y Svingby y dice que no se puede saber qué beneficio tiene más respaldo. En tareas de desempeño, el reanálisis de 1999 se atribuye a Shavelson, Wiley y Ruiz-Primo (no a «los mismos autores») y la conclusión práctica va como inferencia; Indriasari et al. dan ejemplos de beneficios y barreras, no «el más citado». En evaluación como aprendizaje, el párrafo de Pan y Rickard ya no dice «al corregir por sesgo de publicación». En opción múltiple, se recuperó el «in part» de Rodriguez.
