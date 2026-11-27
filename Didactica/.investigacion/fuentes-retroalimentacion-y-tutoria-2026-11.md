---
resumen: >-
  Búsqueda de fuentes para los avisos «Sin fuente todavía» de escalera de pistas, niveles de retroalimentación, tutoría y mentoría (issue #151).
creado: 2026-11-27
---

# Fuentes para los avisos de retroalimentación y tutoría (issue #151)

Cuatro avisos en cuatro notas. Ninguno se cerró del todo; los cuatro se achicaron a lo que sigue faltando. Ninguna fuente contradice lo que las notas ya afirmaban.

Los extractos en inglés son literales de lo que se leyó. Los PDF se pasaron a texto con `pdftotext`; el de Kram e Isabella es un escaneo sin texto y se leyó como imagen.

## 1. Enseñar a pedir ayuda (`Retroalimentacion/escalera-de-pistas.md`)

**Faltaba**: si enseñar a pedir ayuda mejora el aprendizaje; Aleven, Roll, McLaren y Koedinger (2016) sin verificar.

**Se encontró**:

- Roll, I., Aleven, V., McLaren, B. M. y Koedinger, K. R. (2011), *Improving students' help-seeking skills using metacognitive feedback in an intelligent tutoring system*, Learning and Instruction 21(2):267-280, DOI 10.1016/j.learninstruc.2010.07.004 (datos de Crossref). https://www.cs.cmu.edu/~bmclaren/pubs/RollEtAl-ImprovingMetacogSkillsWithITS-LandI2010.pdf. **Texto completo**, versión de autor (sin la paginación de la revista).
  - Abstract: «The Help Tutor, an intelligent tutor agent for help seeking, was integrated into a commercial tutoring system for geometry, the Geometry Cognitive Tutor. Study 1, with 58 students, found that […] the Help Tutor improved students' help-seeking behavior while learning Geometry». «Study 2, with 67 students, evaluated more elaborated support that included, in addition to the Help Tutor, also help-seeking instruction and support for self assessment. The study replicated the effect found in Study 1. It was also found that the improved help-seeking skills transferred to learning new domain-level content during the month following the intervention, while the help-seeking support was no longer in effect.»
  - Estudio 1: «All students were in Grades 10-11 (15-17 years old).» Estudio 2: «Participants were 67 students, 10th and 11th graders (15-17 years old)».
  - Estudio 1, aprendizaje: «while students in both conditions improved significantly from pre- to posttest, there was no effect of the Help Tutor on students' learning gains».
  - Estudio 2, aprendizaje: «Study 2 found no effect of the help-seeking support on domain learning during Months 1 and 3». «Learning gains were not evaluated during Months 2 and 4.»
  - Transferencia solo tras dos unidades: «The significant improvement in students' behavior in the unsupported environment was found only during Month 4, and not during Month 2.» «students could extract the domain-independent nature of help-seeking skills only after they received support for their help-seeking behavior across two different instructional units (angles and quadrilaterals)».
- Aleven, V., Roll, I., McLaren, B. M. y Koedinger, K. R. (2016), *Help Helps, But Only So Much: Research on Help Seeking with Intelligent Tutoring Systems*, International Journal of Artificial Intelligence in Education 26(1):205-223, DOI 10.1007/s40593-015-0089-1 (datos de Crossref). https://cris.iucc.ac.il/en/publications/help-helps-but-only-so-much-research-on-help-seeking-with-intelli/. **Abstract**:
  - «In a classroom study, feedback on help seeking helped students to use on-demand help more deliberately, even after the feedback was no longer given, but not to achieve better learning outcomes.»
  - «Although we do not view on-demand, principle-based help during tutored problem solving as being as important as we once did, we still view it as helpful under certain circumstances, and recommend that it be included in ITSs.»

**Corrección del cotejo**: la nota generalizaba «no cambió» a los dos estudios. Ahora separa el estudio 1 («there was no effect of the Help Tutor on students' learning gains») del 2 («no effect of the help-seeking support on domain learning during Months 1 and 3»; «Learning gains were not evaluated during Months 2 and 4»).

**Qué se cambió**: sección nueva «Enseñar a pedir ayuda» con los dos estudios, su población y el resultado nulo sobre el aprendizaje; las dos fuentes al frontmatter. El aviso se achicó.

**Sigue faltando**: un estudio con adultos o con un tutor humano. El artículo de 2016 entero.

**Fuera de este archivo**: `Tecnologia-educativa/Tutores-inteligentes/pistas-de-un-tutor-inteligente.md` (línea 33) tiene un aviso «el trabajo de Aleven et al. sobre enseñar a pedir ayuda. Ninguno se verificó». Estas dos fuentes lo cubren; no se editó porque no es de este encargo.

## 2. Comparar los cuatro niveles (`Retroalimentacion/niveles-de-retroalimentacion.md`)

**Faltaba**: un análisis que compare los cuatro niveles por separado; Hattie y Timperley leído solo en parte.

**Se encontró**:

- Hattie, J. y Timperley, H. (2007), *The Power of Feedback*, Review of Educational Research 77(1):81-112. https://www.uky.edu/~gmswan3/575/Hattie_Timperly_2007.pdf. **Texto completo**. No trae un metaanálisis por nivel; el orden de los niveles es su argumento.
  - p. 90-91: «We argue that FS is the least effective, FR and FP are powerful in terms of deep processing and mastery of tasks, and FT is powerful when the task information subsequently is useful for improving strategy processing or enhancing self-regulation (which it too rarely does).»
  - p. 91, la tarea: «By itself, corrective feedback can be powerful. From various meta-analyses, Lysakowski and Walberg (1982) reported an effect size of 1.13, Walberg (1982) reported 0.82, and Tenenbaum and Goldring (1989) reported 0.74».
  - p. 91: «FT is more powerful when it is about faulty interpretations, not lack of information. If students lack necessary knowledge, further instruction is more powerful than feedback information.»
  - p. 91: «Feedback aimed to move students from task to processing and then from processing to regulation is most effective.»
  - p. 92: «feedback that mixes FS with FT is less effective than FT by itself.»
  - p. 96, la persona (confirma las cifras que la nota ya tenía): «Wilkinson (1981) […] (overall effect = 0.12). Kluger and DeNisi (1998) also reported a similarly low effect size for praise (0.09)». En la tabla de p. 84: «Praise […] 0.14».
  - Para proceso y autorregulación no se encontró un tamaño de efecto propio en el texto.
- Wisniewski, Zierer y Hattie (2020), https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.03087/full (se leyó hasta el carácter 100.000 de 119.000). Confirma que no separa los niveles: los usa para describir sus tipos. Métodos: «the study features for our coding scheme are orientated toward Hattie's and Timperley's (2007) coding features»; los refuerzos y castigos «provide a minimum amount of information on task level and no information on the levels of process or self-regulation». Discusión: «High-information feedback contains information on task, process and (sometimes) self-regulation level.»
- Harks, B., Rakoczy, K., Hattie, J., Besser, M. y Klieme, E. (2014), *The effects of feedback on achievement, interest and self-evaluation: The role of feedback's perceived usefulness*, Educational Psychology 34(3):269-290, DOI 10.1080/01443410.2013.785384. https://fis.leuphana.de/en/publications/the-effects-of-feedback-on-achievement-interest-and-self-evaluati/. **Abstract**:
  - «The impact of two types of written feedback (process-oriented, grade-oriented) on changes in mathematics achievement, interest and self-evaluation was compared».
  - «Participants, 146 ninth graders (aged 14 to 17 years), were assigned to either a process-oriented or a grade-oriented experimental feedback condition.»
  - «process-oriented feedback was perceived as more useful than grade-oriented feedback and that feedback's perceived usefulness had a positive effect on changes in achievement and interest. Consistent with this, process-oriented feedback had a greater positive indirect effect than grade-oriented feedback on changes in mathematics achievement and interest via its perceived usefulness. There were no such effects on changes in self-evaluation.»
  - Hattie es coautor; la nota lo muestra en la lista de autores.

**Qué se cambió**: Hattie y Timperley pasa a «texto completo» en `fuentes:`. Sección nueva «Cómo ordenan los niveles Hattie y Timperley», con la tesis, las cifras de la tarea, los tres matices y el experimento de Harks et al. El aviso se achicó: ahora pide solo el metaanálisis por nivel.

**Sigue faltando**: un metaanálisis con un efecto para cada nivel. Una búsqueda («meta-analysis feedback "task level" "process level" "self-regulation level"») no lo encontró. Harks et al. entero.

## 3. Tutoría con adultos en habilidades técnicas (`Tutoria-y-mentoria/tutoria.md`)

**Faltaba**: evidencia de tutoría con adultos en habilidades técnicas.

**Se encontró**:

- VanLehn, K., Graesser, A. C., Jackson, G. T., Jordan, P., Olney, A. y Rosé, C. P. (2007), *When are tutorial dialogues more effective than reading?*, Cognitive Science 31(1):3-62, DOI 10.1080/03640210709336984. https://pubmed.ncbi.nlm.nih.gov/21635287/. **Abstract** (el PDF del autor en public.asu.edu no se pudo bajar):
  - «In 7 experiments, we tested the interaction hypothesis under the constraint that (a) all students covered the same content during instruction, (b) the task domain was qualitative physics».
  - «we compared 2 kinds of human tutoring (spoken and computer mediated) with 2 kinds of natural-language-based computer tutoring (Why2-Atlas and Why2-AutoTutor) and 3 control conditions that involved studying texts.»
  - «When novices (students who had not taken college physics) studied content that was written for intermediates (students who had taken college physics), then tutorial dialogue was reliably more beneficial than less interactive instruction, with large effect sizes. When novices studied material written for novices or intermediates studied material written for intermediates, then tutorial dialogue was not reliably more effective than the text-based control conditions.»
- Fossati, D., Di Eugenio, B., Ohlsson, S., Brown, C. y Chen, L. (2015), *Data Driven Automatic Feedback Generation in the iList Intelligent Tutoring System*, Technology, Instruction, Cognition and Learning 10:5-26. https://www.oldcitypublishing.com/wp-content/uploads/2016/02/TICLv10n1p5-26Fossati.pdf. **Texto completo**.
  - Tema y población: «iList, an ITS that helps students learn linked list, a fundamental Computer Science concept taught in introductory undergraduate curricula».
  - Diseño: «We compared the 5 versions of iList with a control group of students that did not receive any form of instruction between the tests, and another group of students that interacted with a human tutor.»
  - Resultado: «ANOVA revealed an overall significant difference among the seven groups (F (6, 319) = 3.04, P = .007). Tukey post-hoc tests revealed significant differences only between the control group and the human tutored group (P = .004), and between the control group and iList-5 (P = 0.021).»
  - Tabla 3 (pre, post, ganancia, medias): «None 53 .34 […] .35 […] .01»; «iList-5 30 .37 […] .51 […] .14»; «Human 54 .40 […] .54 […] .14». El artículo no dice la escala de la prueba; la nota da los puntajes sin escala.
- Descartado: el Digital Tutor de DARPA para técnicos de IT de la Armada de EE. UU. (Fletcher y Morrison, IDA D-5358, 2014) es un tutor por computadora, no tutoría humana, y el informe de DTIC devolvió 403.

**Corrección del cotejo**: la nota decía que en los dos estudios la tutoría humana «gana a no hacer nada» y «no siempre a materiales bien hechos». VanLehn et al. comparan con textos («3 control conditions that involved studying texts»), y solo Fossati et al. con un grupo sin instrucción. Ninguno prueba la tutoría contra materiales juzgados «bien hechos». Se recortó a qué compara cada uno.

**Qué se cambió**: la sección «Lo que falta para adultos» ahora describe los dos estudios con universitarios y cierra con una inferencia marcada como tal. Dos fuentes nuevas al frontmatter. El aviso se achicó a adultos fuera de la universidad.

**Sigue faltando**: tutoría humana con adultos que trabajan o se forman en un oficio técnico (formación profesional, bootcamps, empresas); un metaanálisis. Si VanLehn (2011) incluye adultos no se pudo ver: el artículo está cerrado (OpenAlex: «oa_status: closed») y solo se tiene el abstract.

## 4. Kram (`Tutoria-y-mentoria/mentoria.md`)

**Faltaba**: el texto de Kram (1983), con las cuatro fases y el contenido de cada función.

**Se encontró**:

- Kram (1983), *Phases of the Mentor Relationship*: AOM devolvió 403, Semantic Scholar tiene el abstract retirado por la editorial («the following paper fields have been elided by the publisher: {'abstract'}») y OpenAlex no lo tiene. No se leyó. Crossref confirma Academy of Management Journal 26(4):608-625, diciembre de 1983.
- Kram, K. E. e Isabella, L. A. (1985), *Mentoring Alternatives: The Role of Peer Relationships in Career Development*, Academy of Management Journal 28(1):110-132. https://bu.edu/sph/files/2012/01/Kram_Mentoring-Alternatives.pdf (copia de JSTOR). **Texto completo**; se leyeron la portada y las pp. 110-111.
  - p. 111: «Mentors provide young adults with career-enhancing functions,¹ such as sponsorship, coaching, facilitating exposure and visibility, and offering challenging work or protection, all of which help the younger person to establish a role in the organization, learn the ropes, and prepare for advancement. In the psychosocial sphere, the mentor offers role modeling, counseling, confirmation, and friendship, which help the young adult to develop a sense of professional identity and competence.»
  - Nota 1: «Career-enhancing functions in this paper are the same as the Career Functions discussed in earlier work (Kram, 1980, 1983, 1985).»
  - p. 111: «Complementarity of needs solidifies a mentor relationship during the initiation phase, and propels it forward to the cultivation phase when the range of functions provided by the relationship expands to its maximum (Kram, 1983). Eventually, changes in organizational circumstances or in the individuals' needs cause the relationship to move to a new phase. For example, organizational changes like transfers, promotions, and demotions, as well as individual changes like a sense of increased confidence or a growing need for independence, have been found to alter the context of the mentoring relationship.» «As a mentoring relationship moves into the separation and redefinition phases, it ceases to provide many of the central functions that previously gave it such importance.»
  - Las funciones psicosociales se citan ahí a «Clawson, 1979; Kram, 1985; Phillips, 1977», no a 1983.

**Corrección del cotejo**: la nota decía que los cambios «llevan a la separación»; el extracto dice «cause the relationship to move to a new phase», sin nombrar cuál. Se recortó a esa frase.

**Qué se cambió**: tabla con las dos funciones y su contenido, y un párrafo con las cuatro fases, ambos atribuidos a Kram e Isabella (1985). La fuente al frontmatter. El aviso se achicó a lo que solo da el artículo de 1983.

**Sigue faltando**: Kram (1983) mismo: cómo se pasa de una fase a otra, cuánto dura cada una, y su muestra.
