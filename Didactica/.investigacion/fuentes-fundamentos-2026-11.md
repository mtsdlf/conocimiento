---
resumen: >-
  Búsqueda de fuentes para los avisos «Sin fuente todavía» de Didactica/Fundamentos (issue #151): candados y meses de la EEF, estándares del WWC, Slavin, el 0,40 de Hattie, Bergeron, libros de la didáctica europea y latinoamericana y evidencia sobre capacitar adultos.
creado: 2026-11-27
---

# Fuentes para los avisos de Fundamentos de Didáctica (issue #151)

Tres avisos en tres notas. Ninguno se cerró del todo; los tres se achicaron. En `evidencia-en-educacion.md` se resolvieron los candados, los estándares del WWC, Slavin, la autoría y el año de Bergeron y, en parte, el 0,40. En `historia-de-la-didactica.md` se leyeron Litwin (cap. 2), un extracto de Chevallard, Dewey (cap. 2) y la portada de la traducción de Comenio. En `fundamentos-de-didactica.md` se sumaron dos fuentes sobre capacitar adultos.

Hay dos correcciones: la guía de la EEF contradice dos cifras que la nota tenía («0,2 desviaciones por mes» y «90 estudios para cinco candados»), y Bergeron no tiene coautor: Rivard es la traductora.

Los extractos en inglés, francés y castellano son literales de lo que se leyó. Los PDF se bajaron y se pasaron a texto con `pdftotext`; las páginas web se leyeron con un lector que corta las citas en fragmentos, y los fragmentos se citan tal cual.

## 1. Evidencia en educación (`Fundamentos/evidencia-en-educacion.md`)

**Faltaba**: los umbrales de candados de la guía 2025 de la EEF, los estándares del What Works Clearinghouse, el texto de Slavin «John Hattie is Wrong», el 0,40 de Hattie y la coautoría y el año de Bergeron.

### 1.1 Guía del Toolkit de la EEF

**Se encontró**: EEF, *Teaching and Learning / Early Years Toolkit guide*, https://d2tic4wvo1iusb.cloudfront.net/production/documents/toolkit/toolkit_guide_2025_v3.0.0.pdf. **Texto completo** (10 páginas). La portada dice «February 2023», pero los metadatos del PDF dicen «Keywords: v3.0.0 - October 2025» y «ModDate: Mon Oct 27 09:05:30 2025». La nota la cita como versión 3.0.0, de octubre de 2025.

- Tabla de meses: «Months' progress / Effect size from... / to...»: «0 -0.04 0.04 Very low or no impact»; «+1 0.05 0.09 Low impact»; «+6 0.45 0.52 High impact»; «+12 0.96 1.00 Very high impact».
- Candados: «Topics are awarded padlocks based on the number of studies that meet the Toolkit inclusion criteria. Additional padlocks are then lost due to a number of potential threats to security.»
- Umbrales: «Very limited evidence: Between 11 and 39 studies»; «Limited evidence: Between 40 and 59 studies»; «Moderate evidence: Between 60 and 79 studies»; «Extensive evidence: Between 80 and 119 studies»; «Very Extensive evidence: 120 or more studies». Los íconos de candado no salen en el texto extraído; se verificaron mirando la p. 7 como imagen: «Very limited evidence» lleva un candado lleno y cuatro vacíos, «Limited» dos, «Moderate» tres, «Extensive» cuatro y «Very Extensive» cinco.
- «Where there are fewer than 11 studies that meet the inclusion criteria a 0 padlock security rating is awarded, and months' progress are not communicated.»
- Pérdida de candados: «Only a small percentage of the studies have taken place recently»; «A large percentage of the studies included are not randomised controlled trials»; «A large percentage of the studies took place in conditions distinct from regular school practice»; «A large percentage of the studies were not independently evaluated»; «There is a large amount of unexplained variation between the results».
- «Studies included in the Toolkit all take place in schools rather than lab-studies, involve a comparison group».
- Deberes: «Homework in secondary school is estimated to deliver 5 months' additional progress. However, the evidence strength is very low».

**Contradicciones con la nota**: la nota decía que un mes son «unas 0,2 desviaciones por mes en primaria» (fuente sin identificar del informe `fundamentos-del-area.md`) y que una página de un Research School pedía «90 estudios o más para cinco candados». La guía da 0,05 a 0,09 por un mes y 120 o más estudios para cinco candados. No se borraron: quedaron en un `[!IMPORTANT]` con las dos posiciones. La guía no distingue primaria de secundaria.

### 1.2 What Works Clearinghouse

**Se encontró**:

- La página https://ies.ed.gov/ncee/wwc/handbooks/ dice: «The current version of the Handbook, What Works Clearinghouse Procedures and Standards Handbook, Version 5.0, contains the most up-to-date procedures and standards» y «Current Standards Version 5.0, August 2022 (Revised December 2022)».
- What Works Clearinghouse (2022), *Procedures and Standards Handbook, Version 5.0*, https://ies.ed.gov/ncee/WWC/Docs/referenceresources/Final_WWC-HandbookVer5_0-0-508.pdf. 234 páginas; se leyeron la tabla 3, el resumen de la fase 3 y la tabla 23.
  - «eligible findings from the study will receive one of three research ratings: Meets WWC Standards Without Reservations, Meets WWC Standards With Reservations, or Does Not Meet WWC Standards.»
  - «The effectiveness ratings include strong evidence (Tier 1), moderate evidence (Tier 2), promising evidence (Tier 3), uncertain effects, and negative effects.»
  - Guías de práctica: «The WWC assigns effectiveness ratings to practice guide recommendations as supported by strong evidence (Tier 1), moderate evidence (Tier 2), promising evidence (Tier 3), or notes when evidence demonstrates a rationale for a recommendation (Tier 4).»
  - Tabla 23, evidencia fuerte: «More than 50 percent of the meta-analytic weight […] is based on finding(s) that are rated Meets WWC Standards Without Reservations; AND The analytic sample includes multiple sites […]; AND The analytic sample includes 350+ unique individuals».
  - «Individual-level RCTs with low attrition are eligible to be rated Meets WWC Standards Without Reservations».
- What Works Clearinghouse, *Procedures Handbook, Version 4.1*, https://ies.ed.gov/ncee/WWC/Docs/referenceresources/WWC-Procedures-Handbook-v4-1-508.pdf. Solo la tabla IV.5: «Levels of evidence for practice guide recommendations»: «Strong evidence base», «Moderate evidence base», «Minimal evidence base».

**Qué cambió**: la fila del WWC en la tabla ya no dice «fuerte, moderada o mínima». Ahora da las tres calificaciones de estudios y los niveles de la versión 5.0, y aclara que «mínimo» era el nivel de antes de esa versión. El informe no encontró la fecha de la versión 4.1.

### 1.3 Slavin, «John Hattie is Wrong»

**Se encontró**: Slavin, R., «John Hattie is Wrong», *Robert Slavin's Blog*, 21 de junio de 2018 (actualizado el 30 de noviembre de 2018), https://robertslavinsblog.wordpress.com/2018/06/21/john-hattie-is-wrong/. **Texto completo**.

- «Yet many, perhaps most meta-analyses accept all sorts of individual studies of widely varying standards of quality.»
- «A meta-analysis cannot be any better than the studies that go into it.»
- «there is now overwhelming evidence that effect sizes are significantly inflated in studies with small sample sizes,» «brief durations, use measures made by researchers or developers, are published (vs. unpublished), or use quasi-experiments» «(vs. randomized experiments) (Cheung & Slavin, 2016).»
- «Hattie makes a big deal of the magical effect size +0.40, the "hinge point," recommending that educators essentially ignore factors» «or programs below that point».
- Entre las «core claims» de Hattie que discute: «Any effect size less than +0.40 is ignorable».
- «He is merely shoveling meta-analyses containing massive bias into meta-meta-analyses that reflect the same biases.»
- Contra el umbral (segunda lectura, a pedido del cotejo): «individual studies, except for studies of one-to-one tutoring, almost never have effect sizes as large as +0.40»; «So an effect size of, say, +0.15 or +0.25 could be very important.» Slavin no ataca el 0,40 con esas palabras; la nota cita estas dos frases en lugar de decir que «rechaza» el umbral.

**Qué cambió**: Slavin ya no figura «según un resumen secundario»; la nota cita su texto.

### 1.4 El 0,40 de Hattie

**Se encontró**:

- Hattie, J. y Timperley, H. (2007), «The Power of Feedback», *Review of Educational Research* 77(1):81-112, https://www.uky.edu/~gmswan3/575/Hattie_Timperly_2007.pdf. **Texto completo**. P. 83: «Hattie (1999) reported a synthesis of over 500 meta-analyses, involving 450,000 effect sizes from 180,000 studies»; «The average or typical effect of schooling was 0.40 (SE = 0.05), and this provided a benchmark figure or "standard" from which to judge the various influences on achievement, such as that of feedback.»
- Slavin (2018), arriba: el «hinge point».
- Bergeron (2017), abajo, sobre *Visible Learning*: «Above 0.4 represents the desired effect zone.» «Between 0 and 0.4 we go from "developmental" effects to "teacher" effects.»
- Routledge, ficha de *Visible Learning: A Synthesis of Over 800 Meta-Analyses Relating to Achievement*, https://www.routledge.com/Visible-Learning-A-Synthesis-of-Over-800-Meta-Analyses-Relating-to-Achievement/Hattie/p/book/9780415476188: «1st Edition», «Copyright 2009», «392 Pages»; índice de once capítulos más «Appendix A: The 800 meta-analyses» y «Appendix B: The meta-analyses by rank order». Open Library da para el ISBN 9780415476188 «publish_date: 2008» y 378 páginas.

**Qué cambió**: un párrafo nuevo, «El 0,40», con la cita de Hattie y Timperley y las de Slavin y Bergeron. La tabla aclara que la editorial pone copyright 2009 al libro de 2008.

**Sigue faltando**: el 0,40 en el texto de *Visible Learning*. No se pudo bajar el libro, el artículo de Hattie de 2003 para ACER (403) ni *Visible Learning for Teachers* (2012, bloqueado).

### 1.5 Bergeron: autoría y año

**Se encontró**:

- Ficha en inglés, https://mje.mcgill.ca/article/view/9475: autor «Pierre-Jérôme Bergeron (University of Ottawa)»; «Lysanne Rivard (trans.)»; título completo «HOW TO ENGAGE IN PSEUDOSCIENCE WITH REAL DATA: A CRITICISM OF JOHN HATTIE'S ARGUMENTS IN VISIBLE LEARNING FROM THE PERSPECTIVE OF A STATISTICIAN»; «Vol. 52 No. 1 (2017)»; publicado el 2017-07-07; sección «The MJE Forum». Resumen: «This paper is a forum contribution that appeared in issue 51-2 in French.»
- Ficha en francés, https://mje.mcgill.ca/article/view/9394: «COMMENT FAIRE DE LA PSEUDOSCIENCE AVEC DES DONNÉES RÉELLES : UNE CRITIQUE DES ARGUMENTS STATISTIQUES DE JOHN HATTIE DANS VISIBLE LEARNING PAR UN STATISTICIEN», vol. 51, núm. 2, 2016, publicado el 2016-11-25, solo Bergeron.
- Texto en inglés, https://mje.mcgill.ca/article/download/9475/7229?inline=1 (**lectura parcial**, por búsquedas dentro del texto):
  - «His most blatant calculation error is the case of the common language effects (CLE), which take the form of a probability.»
  - «Noticed in 2012 by Norwegian researchers (Topphol, 2012), it is flagrant» «to the point of giving negative probabilities or probabilities superior to 100%».
  - «The effect size is large (0.59)»; «the socio-economic effect would be -0.59, the most negative of all, if nothing else is changed.»
  - «We must therefore absolutely qualify Hattie's methodology as pseudoscience.»
  - «Visible Learning (Hattie, 2008)»; «over 800 meta-analyses, comprising over 50,000 studies and millions of individuals».
  - No aparecen «admit», «acknowledg» ni «recogni».

**Corrección**: no hay coautor. Rivard es la traductora; el original es de 2016 y la traducción de 2017. Además, la nota atribuía a Bergeron que «Hattie admitió que esos valores estaban mal calculados», y el artículo no lo dice. Esa frase viene del informe `fundamentos-del-area.md` (§3.3), sin fuente nombrada (probablemente Wikipedia). Como el artículo se leyó en parte, la nota ahora dice que la admisión no aparece en lo que se leyó y que no se encontró una fuente que la diga.

**Qué cambió en la nota**: entradas nuevas en `fuentes` (Bergeron 2017 con traductora, Bergeron 2016, Slavin, Hattie y Timperley, ficha de Routledge, WWC v5.0 y v4.1); la guía de la EEF pasa de «según resumen» a texto completo. Dos párrafos nuevos (meses y candados), un `[!IMPORTANT]` con las dos cifras que no coinciden, el párrafo del 0,40 y el bloque de críticas reescrito con Bergeron y Slavin de sus textos.

**Sigue faltando**: el texto de *Visible Learning*; de dónde sale la admisión de Hattie sobre el CLE; los umbrales de deserción y equivalencia del WWC (no se leyeron).

## 2. Historia de la didáctica (`Fundamentos/historia-de-la-didactica.md`)

**Faltaba**: las obras de Comenio, Klafki, Dewey, Camilloni y Litwin; la tradición francesa más allá de Houssaye; una historia de la didáctica en castellano que no sea enciclopedia.

**Se encontró**:

- **Comenio**: *The Great Didactic of John Amos Comenius*, trad. y ed. de M. W. Keatinge, Londres, Adam and Charles Black, 1907, parte II, texto; https://archive.org/details/cu31924031053709 (texto OCR de archive.org). En el colofón: «Published as one Volume in May 189[6]» (OCR cortado) y «Second Part reissued April 1907». Se leyeron la portada, el objetivo y la cronología de obras:
  - Portada: «The Great Didactic Setting forth The whole Art of Teaching all Things to all Men».
  - «Let the main object of this, our Didactic, be as follows: To seek and to find a method of instruction, by which teachers may teach less, but learners may learn more».
  - Cronología: «19. 1628-32. The Didactic of John Amos Comenius. Prague, 1849. [C]» («[C] signifies that the work was written in Czech»); «The Latin version, under the title Didactica Magna, was published at Amsterdam in 1657.»
  - Litwin (1997, cap. 2) da lo mismo: «escribió, entre 1628 y 1632, la Didáctica Magna».
  - La nota mantiene el 1627-1638 de la Wikipedia y suma el 1628-1632 de la versión checa. No es contradicción: la Wikipedia parece contar la versión latina.
  - Ediciones en castellano, por Open Library (sin verificar en el libro): Porrúa (1976) y Akal (1986, ISBN 84-7600-098-7).
- **Klafki**: capítulo «Didaktik analysis as the core of the preparation of instruction», en *Rethinking Schooling*, Routledge, 2006, https://www.taylorfrancis.com/chapters/oa-edit/10.4324/9780203963180-15/didaktik-analysis-core-preparation-instruction-wolfgang-klafki. **Solo el resumen**: el texto salió primero en la revista *Die Deutsche Schule* en 1958, y luego en compilaciones y en su libro *Studien zur Bildungstheorie und Didaktik* (1963). «The concept I developed was used for about two decades in pre-service teacher education»; «It is still in use in places today.» Crossref: traducción previa en *Journal of Curriculum Studies* 27(1):13-30, 1995, doi 10.1080/0022027950270103.
  - **Qué resuelve**: la discrepancia 1958/1963 de la nota y del informe `fundamentos-del-area-2.md`. 1958 es el artículo; 1963 es el libro que lo recoge.
- **Dewey**: *Experience and Education*, Nueva York, Macmillan, reimpresión de 1953; https://archive.org/details/dli.ernet.285395 (texto OCR). «THE KAPPA DELTA PI LECTURE SERIES»; «Copyright, 1938, By KAPPA DELTA PI»; «Published February, 1938». Índice: I Traditional vs. Progressive Education; II The Need of a Theory of Experience; III Criteria of Experience; IV Social Control; V The Nature of Freedom; VI The Meaning of Purpose; VII Progressive Organization of Subject-Matter; VIII Experience—The Means and Goal of Education. Cap. II, p. 13: «For some experiences are mis-educative. Any experience is mis-educative that has the effect of arresting or distorting the growth of further experience.»
- **Litwin**: *Las configuraciones didácticas: una nueva agenda para la enseñanza superior*, Buenos Aires, Paidós, «1a. edición, 1997», «2a. reimpresión, 2000», «ISBN 950-12-2126-1». Sumario y capítulo 2 («Las prácticas de la enseñanza en la agenda de la didáctica», pp. 35-68) en https://www.amsafe.org.ar/wp-content/uploads/Litwin-Las_Configuraciones_Didacticas-Cap2.pdf. **Texto completo del capítulo**. Extractos:
  - «Contenidos y método constituyen dos dimensiones clásicas e indisociables de la agenda de la didáctica para analizar el problema del conocimiento en las aulas.»
  - Sobre Camilloni (1994): «se podría definir a la didáctica, al menos potencialmente, como una ciencia social» (cita de Camilloni, «págs. 35-36»); «Camilloni entiende que la teoría didáctica es una teoría de encrucijada en la que confluyen diferentes aportes que, aunque se consideren imprescindibles, deben ser leídos desde el objeto de la didáctica, esto es la enseñanza».
  - La palabra «multireferencial» no aparece en el capítulo 2; esa cita sigue saliendo de la Wikipedia.
- **Camilloni**: *El saber didáctico*. En un fragmento del libro que publicó un instituto de formación docente (https://inscastelli-cha.infd.edu.ar/sitio/wp-content/uploads/2019/06/ÁREA-PEDAGÓGICA-La-enseñanza.-Basabe-Camillioni-pages-112-19.pdf) dice: «El saber didáctico / Alicia R. W. de Camilloni (et.al) / Editorial Paidós / 1ª ed., Buenos Aires, 2007 / Colección: Cuestiones de educación / ISBN 978-950-12-6154-7». Hay un resumen del capítulo 1 («Justificación de la didáctica») hecho por un profesorado, no por la autora (https://des-for.infd.edu.ar/sitio/profesorado-de-educacion-inicial/upload/CAMILLONI_A..docx): «la didáctica es una disciplina teórica que estudia la acción pedagógica desde su descripción, explicación y fundamentación». Coincide con la cita de la Wikipedia, pero es un resumen y no el libro.
- **Chevallard**: *La transposición didáctica: del saber sabio al saber enseñado*, Aique Grupo Editor. «Título original: La transposition didactique. Du savoir savant au savoir enseigné»; «Primera edición 1997 / Segunda edición 1997 / Tercera edición 1998». Extracto de 28 páginas en https://des-tuc.infd.edu.ar/sitio/wp-content/uploads/2023/10/Chevallard-La-transposicion-didactica.-Del-saber-sabio-al-saber-ensenado.pdf (índice, prefacio y cap. 1). Extractos:
  - Origen: «notas preparatorias a un curso que dicté en ocasión de la Primera Escuela de Verano de didáctica de las matemáticas, llevada a cabo en Chamrousse del 7 al 19 de julio de 1980».
  - Cap. 1, 1.3: «Un contenido de saber que ha sido designado como saber a enseñar, sufre a partir de entonces un conjunto de transformaciones adaptativas que van a hacerlo apto para ocupar un lugar entre los objetos de enseñanza. El "trabajo" que transforma de un objeto de saber a enseñar en un objeto de enseñanza, es denominado la transposición didáctica.»
  - El índice trae «Prefacio a la segunda edición» y «Posfacio a la segunda edición»: se tradujo la segunda edición francesa. Según el buscador, la primera francesa es de 1985 y la segunda de 1991; no se verificó, y la nota no lo dice.
- **Historia de la didáctica en castellano**: no se encontró una que se pudiera leer. *Corrientes didácticas contemporáneas* (Paidós, 1996), con el capítulo de Camilloni «De herencias, deudas y legados», no tiene copia accesible. El PDF de CLACSO *Lecciones maestras*, que la trata, dio 403. El capítulo 2 de Litwin repasa el campo desde Comenio, pero mirando la universidad argentina.

**Qué cambió**: siete fuentes nuevas en `fuentes` y aliases nuevos (Chevallard, transposición didáctica). Comenio: suma la fecha de Keatinge y la cita del objetivo. Un párrafo sobre Chevallard después de Houssaye. Klafki: la fecha queda explicada. Litwin: la cita sale del libro, y se suma su lectura de Camilloni. Dewey: la cita de «mis-educative» sale del libro. La frase final del párrafo latinoamericano dice qué se leyó de cada uno. El aviso se achicó.

**Sigue faltando**: la *Didactica Magna* y el artículo de Klafki enteros; *El saber didáctico* en su texto; el resto de la tradición francesa; una historia de la didáctica en castellano que no sea enciclopedia.

## 3. Fundamentos de didáctica (`Fundamentos/fundamentos-de-didactica.md`)

**Faltaba**: una síntesis de la didáctica latinoamericana leída en sus libros, y una revisión de la evidencia sobre enseñar a adultos fuera de la escuela.

**Se encontró**:

- Litwin y Camilloni: ver §2 (ISBN y capítulo 2 de Litwin; datos de edición de Camilloni). Davini, *Métodos de enseñanza* (2008): no se buscó.
- Arthur, W., Bennett, W., Edens, P. S. y Bell, S. T. (2003), «Effectiveness of training in organizations: A meta-analysis of design and evaluation features», *Journal of Applied Psychology* 88(2):234-245, doi 10.1037/0021-9010.88.2.234 (Crossref). **Resumen** (OpenAlex): «Results of the meta-analysis revealed training effectiveness sample-weighted mean ds of 0.60 (k = 15, N = 936) for reaction criteria, 0.63 (k = 234, N = 15,014) for learning criteria, 0.62 (k = 122, N = 15,627) for behavioral criteria, and 0.62 (k = 26, N = 1,748) for results criteria. These results suggest a medium to large effect size for organizational training. In addition, the training method used, the skill or task characteristic trained, and the choice of evaluation criteria were related to the effectiveness of training programs.»
- Salas, E., Tannenbaum, S. I., Kraiger, K. y Smith-Jentsch, K. A. (2012), «The Science of Training and Development in Organizations: What Matters in Practice», *Psychological Science in the Public Interest* 13(2):74-101, doi 10.1177/1529100612436661 (Crossref). **Resumen** (OpenAlex): «The research on training clearly shows two things: (a) training works, and (b) the way training is designed, delivered, and implemented matters.» «we argue that training is a systematic process, and we explain what matters before, during, and after training.»

El resumen dice «were related to»: la nota habla de asociación («se asociaron con cuánto rindió»), no de causa.

**Qué cambió**: el párrafo de los textos en castellano ya no dice «Ninguno se leyó»; dice qué se leyó de cada uno, con editorial. Una sección nueva, «Enseñar a adultos en el trabajo», con las dos fuentes y una lectura propia, marcada como tal: miden aprendizaje y conducta en el trabajo, así que sus cifras no se comparan directo con las escolares. El aviso se achicó.

**Sigue faltando**: la síntesis latinoamericana leída en libros; Arthur et al. y Salas et al. enteros.

## Fuera de estos archivos

- `Evaluacion-educativa/Evaluar-un-programa/evaluacion-con-grupo-de-comparacion.md:47` tiene un aviso «cómo califica la EEF la solidez de la evidencia (sus "candados")»: se puede cerrar con §1.1.
- `Didactica/.investigacion/fundamentos-del-area.md` (§3.1 y §3.3) repite el «0,2 por mes», los «90 estudios», «Bergeron (y Rivard…)» y la admisión de Hattie atribuida sin fuente. Es un informe y no se edita; este lo corrige.
- Davini y *Corrientes didácticas contemporáneas* (corregido en `historia-de-la-didactica.md`). La ficha de la biblioteca de la UNQ (https://biblio.unq.edu.ar/qfind/Record/16109/Description) dice: «Other Authors: Camilloni, Alicia W. de; Davini, María Cristina; Edelstein, Gloria; Litwin, Edith; Souto, Marta; Barco, Susana»; «Buenos Aires: Paidós, 1998»; «1a. ed., 2a. reimpr.»; «167 p.»; «ISBN: 9501261131». Open Library da para ese ISBN «first_publish_year: 1996». La nota ahora dice que Davini es coautora de un libro colectivo. No se encontró el índice, así que no se sabe qué capítulo escribió.
- `revisar.py` de `documentar` 0.6.0 se cae al correr sobre `Didactica/` («File name too long»): toma como ruta una entrada de `fuentes` de otra nota (Bernard et al. 2004). No se pudo correr el lint sobre estas notas.
