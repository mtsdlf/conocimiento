---
resumen: >-
  Búsqueda de fuentes para los avisos «Sin fuente todavía» de Evaluacion-educativa/Evaluar-un-programa (issue #153).
creado: 2026-11-27
---

# Fuentes para los avisos de Evaluar un programa (issue #153)

Cuatro avisos en cuatro notas. Ninguno se cerró del todo y los cuatro se achicaron: los candados de la EEF, el texto de Kirkpatrick, una crítica académica del ROI y el texto de Baldwin y Ford se leyeron. Siguen faltando los coeficientes de Alliger et al. (1997), los tamaños de efecto de Blume et al. (2010), los libros de Phillips y el contenido de las guías de evaluación de la EEF.

Los extractos en inglés son literales de lo que se leyó. Los PDF se bajaron con curl y se pasaron a texto con `pdftotext`; Baldwin y Ford (1988) y Kirkpatrick son escaneos con OCR, y algún extracto puede traer cortes de columna.

## 1. Evaluación con grupo de comparación (`Evaluar-un-programa/evaluacion-con-grupo-de-comparacion.md`)

**Faltaba**: cómo califica la EEF la solidez de la evidencia (sus candados) y su guía de evaluación; las páginas habían dado error 403.

**Se encontró** (el sitio de la EEF respondió con curl y un User-Agent de navegador; WebFetch seguía dando 403):

- EEF (julio de 2019), *Classification of the security of findings from EEF evaluations*, versión 2.0, 28 págs. https://d2tic4wvo1iusb.cloudfront.net/production/documents/evaluation/peer-review-process/Classifying_the_security_of_EEF_findings_2019.pdf. **Texto completo** (se leyeron las secciones A a C y el apéndice 1 hasta el inicio del criterio 4). Enlazado desde la página Evaluation design.
  - «The ratings are from 5 padlocks ( ), the most robust evidence that could be expected from a single study, to 0 padlocks ( ) which denotes a study that adds little to the evidence base. The ratings take no account of whether the intervention itself was successful in achieving an impact.»
  - «The padlock ratings largely refer to the internal rather than external validity of the findings.»
  - «Padlock ratings are assigned to the primary outcome only.»
  - Proceso: «1. Two peer reviewers will use this guidance to provide a security rating, 2. The EEF arbitrates between peer reviewer ratings and presents this to the author, 3. The author has an opportunity to respond, 4. The EEF assigns the final security rating».
  - «Step 1: The first three criteria – Design, MDES, and Attrition – are awarded a rating on a scale from 0 to 5. Step 2: An interim padlock rating is determined by the lowest of these three ratings. Step 3: The interim padlock rating can be adjusted downwards by assessing Threats to internal validity.»
  - Diseño: «5 Randomised design. 4 Design for comparison that considers some type of selection on unobservable characteristics (e.g. Regression Discontinuity Designs, Difference-in-Differences, Matched Difference-in-Differences). 3 Design for comparison that considers selection on all relevant observable confounders (e.g. Matching/Weighting or Regression Analysis with variables descriptive of the selection mechanism). 2 Design for comparison that considers selection only on some relevant confounders. 1 Design for comparison that does not consider selection on any relevant confounders. 0 No comparator.»
  - MDES (plantilla de la fig. 1): «<= 0.2», «0.21 - 0.29», «0.30 - 0.39», «0.40 - 0.49», «0.50 - 0.59», «>=0.6». «MDES is highly dependent upon the sample size».
  - Desgaste: «0-10%», «11-20%», «21-30%», «31-40%», «41-50%», «>50%». «EEF has decided to develop its own attrition scale based purely on overall attrition, rather than relying on that created by the WWC», que usa «overall and differential attrition».
  - Amenazas: «Threat 1: Confounding», «Threat 2: Concurrent Interventions», «Threat 3: Experimental effects», «Threat 4: Implementation fidelity», «Threat 5: Missing Data», «Threat 6: Measurement of Outcomes», «Threat 7: Selective reporting». «Adjustments of up to two padlocks can be made according to the following table».
- EEF, *Teaching and Learning / Early Years Toolkit guide*. https://d2tic4wvo1iusb.cloudfront.net/production/documents/toolkit/toolkit_guide_2025_v3.0.0.pdf (enlazado desde https://educationendowmentfoundation.org.uk/education-evidence/using-the-toolkits). **Texto completo de la sección Evidence strength** (págs. 7-8). La portada dice «February 2023», aunque el nombre del archivo dice 2025 v3.0.0; la nota lo cita como 2023.
  - «Topics are awarded padlocks based on the number of studies that meet the Toolkit inclusion criteria. Additional padlocks are then lost due to a number of potential threats to security.»
  - «Studies included in the Toolkit all take place in schools rather than lab-studies, involve a comparison group (rather than simply testing pupils before and after intervention), and meet the definition of each topic.»
  - Niveles iniciales: «= Very limited evidence: Between 11 and 39 studies», «= Limited evidence: Between 40 and 59 studies», «= Moderate evidence: Between 60 and 79 studies», «= Extensive evidence: Between 80 and 119 studies», «= Very Extensive evidence: 120 or more studies». Los íconos no salen en el texto extraído, así que la nota no dice cuántos candados es cada nivel.
  - «Where there are fewer than 11 studies that meet the inclusion criteria a 0 padlock security rating is awarded, and months’ progress are not communicated.»
  - Pérdidas: «Only a small percentage of the studies have taken place recently», «A large percentage of the studies included are not randomised controlled trials», «A large percentage of the studies took place in conditions distinct from regular school practice», «A large percentage of the studies were not independently evaluated», «There is a large amount of unexplained variation between the results included in the topic».
- EEF, *Evaluation design*. https://educationendowmentfoundation.org.uk/projects-and-evaluation/evaluation/evaluation-guidance-and-resources/evaluation-design. **Solo la lista**: «EEF statistical analysis guidance (2022)», «Classifying the security of EEF findings (2019)», «EEF IPE guidance (2022)», «Guidance for EEF pilot evaluations (2023)», «EEF cost evaluation guidance (2023)», entre otras.

**Qué se cambió**: sección nueva «Los candados de la EEF», con la tabla de los tres criterios, el ajuste por amenazas y la escala del Toolkit; tres fuentes nuevas. El aviso se achicó.

**Sigue faltando**: el contenido de las guías de evaluación de la EEF (análisis, implementación, costos, pilotos).

## 2. Niveles de Kirkpatrick (`Evaluar-un-programa/niveles-de-kirkpatrick.md`)

**Faltaba**: los coeficientes de Alliger et al. (1997) leídos en el original y el texto de Kirkpatrick.

**Se encontró**:

- Kirkpatrick, D. L. (junio de 1979), *Techniques for evaluating training programs*, Training and Development Journal, págs. 78-92. https://assets.td.org/m/4a306d561507658e/original/TECHNIQUES-FOR-EVALUATING-TRAINING-PROGRAMS.pdf. **Texto completo** de la reimpresión de las cuatro partes. Bajo el autor dice «(JUNE, 1960)».
  - «Each of these four articles will discuss one of the evaluation steps which can be summarized as follows: Step 1 - REACTION Step 2 - LEARNING Step 3 - BEHAVIOR Step 4 - RESULTS».
  - «Reaction may best be defined as how well the trainees liked a particular training program. […] It is important to emphasize that it does not include a measurement of any learning that takes place.»
  - «Even though he/she has done a masterful job of measuring the reaction of the group, there is still no assurance that any learning has taken place. Neither is there any indication that the behavior of the participants will change because of the training program. And still farther away is any indication of the results that can be attributed to the training program.»
  - «2. The more favorable the reaction to the program, the more likely the conferees are to pay attention and learn the principles, facts, and techniques that are discussed.»
  - Aprendizaje: «2. A before-and-after approach should be used», «4. Where practical, a control group (not receiving the training) should be used to compare with the experimental group which receives the training.»
  - Resultados, citando a Keachie: «Difficulties in the evaluation of training are evident at the outset in the problem technically called 'the separation of variables;' that is, how much of the improvement is due to training as compared to other factors?»
- Kirkpatrick, D. L. (enero de 1960), *Techniques for evaluating training programs, Part 3 – Behavior*. https://assets.td.org/m/486fb05fce23e065/original/Techniques-For-Evaluating-Training-Programs-January-1960.pdf. **Texto completo**. «The Third in a Series of Four Articles»; pie de página «Training Directors». «At this time I began to realize there may be a big difference between knowing principles and techniques and using them on the job.»
- *Kirkpatrick Then and Now* (extracto, Kirkpatrick Partners). https://www.kirkpatrickpartners.com/wp-content/uploads/2021/09/Kirkpatrick-Then-and-Now-peek-inside-10-09.pdf. Solo índice y la primera página de la parte 1, fechada «November 1959». Sostiene el «entre 1959 y 1960».
- Alliger et al. (1997): no se consiguió el texto. El PDF del informe técnico de la Fuerza Aérea (https://apps.dtic.mil/sti/tr/pdf/ADA368508.pdf) dio 403; la copia de SciSpace vino vacía; OpenAlex la marca «closed». Se releyó el abstract en OpenAlex (https://api.openalex.org/works/doi:10.1111/j.1744-6570.1997.tb00911.x), que confirma «A total of 34 studies yielding 115 correlations» y la cita que ya tenía la nota.

**Qué se cambió**: el párrafo de «Los cuatro niveles» ya no dice que el original no se leyó; da la serie, la reimpresión de 1979 y la definición de reacción. En «La cadena que no está», un párrafo nuevo con lo que dice el propio Kirkpatrick: una reacción favorable hace más probable aprender, pero no asegura aprendizaje ni cambio de conducta, y recomienda grupo de control. Dos fuentes nuevas. El aviso se achicó a los coeficientes de Alliger.

**Matiz** (no contradice la nota, que atribuye la cadena causal a la lectura de Colquitt et al.): en su texto, Kirkpatrick no afirma una cadena causal.

**Sigue faltando**: los coeficientes de Alliger et al. (1997).

## 3. Retorno de la capacitación (`Evaluar-un-programa/retorno-de-la-capacitacion.md`)

**Faltaba**: los libros de Phillips y una crítica académica independiente de la metodología.

**Se encontró**:

- Russ-Eft, D. y Preskill, H. (2005), *In search of the Holy Grail: return on investment evaluation in human resource development*, Advances in Developing Human Resources 7(1):71-85, doi 10.1177/1523422304272169. https://study.sagepub.com/sites/default/files/7.1%20Advances%20in%20Developing%20Human%20Resources-2005-Russ-Eft-71-85.pdf. **Texto completo** (copia de SAGE).
  - «This article argues that, in many cases, ROI does not provide the kind of information needed by decision makers. What is needed is a systems model that examines the effect of organizational and environmental factors on the intended outcomes of an HRD initiative or program.»
  - «The four-level taxonomy continues to be bolstered by others in the field, such as Phillips’s (2003) work on return on investment (ROI)».
  - «A major problem with the Kirkpatrick approach […] is that it makes evaluation clients and stakeholders believe that the best evaluations are those that examine the ROI of some intervention».
  - «Translating employee or customer satisfaction into dollars, or measuring the financial effect of coaching, is very difficult to accomplish in any valid or credible way.» Antes: «linking employee satisfaction with the financial success of an organization is difficult if not impossible to establish, and so is the relationship between many training programs and the bottom line.»
  - «(a) when conducting ROI within an HRD context, it is critical to consider what effect other organizational variables have on the outcome measure (or bottom line) and (b) most of the time, ROI is not necessarily what the client wants or needs».
  - «many of these requests for ROI tend to be “knee-jerk” reactions, based on a lack of understanding and misconceptions about evaluation.» «Although ROI is certainly one method, it is only one of many approaches to determining a program’s success.»
  - Autoras: «Darlene Russ-Eft is an assistant professor of adult education and higher education leadership at Oregon State University»; «Hallie Preskill is a professor of organizational learning and instructional technologies at the University of New Mexico».
- No se buscaron los libros de Phillips: no hay copia abierta y no entraban en tres rondas.

**Qué se cambió**: sección nueva «La crítica desde la evaluación». La frase «No se encontró una crítica académica independiente que la cuantifique» pasó a «No se encontró un estudio que cuantifique esa incertidumbre», porque la crítica existe pero es conceptual. El aviso se achicó.

**Sigue faltando**: los libros de Phillips y un estudio que mida cuánto se equivocan las estimaciones de los participantes.

## 4. Transferencia de la capacitación (`Evaluar-un-programa/transferencia-de-la-capacitacion.md`)

**Faltaba**: los tamaños de efecto de Blume et al. (2010) y el texto de Baldwin y Ford (1988).

**Se encontró**:

- Baldwin, T. T. y Ford, J. K. (1988), *Transfer of training: A review and directions for future research*, Personnel Psychology 41:63-105. https://gwern.net/doc/psychology/1988-baldwin.pdf. **Texto completo**: la copia tiene capa de OCR (el informe anterior decía que no).
  - «The conditions of transfer include both the (1) generalization of material learned in training to the job context and (2) maintenance of the learned material over a period of time on the job.»
  - «Training-input factors include training design, trainee characteristics, and work-environment characteristics.» «Trainee characteristics consist of ability or skill, motivation, and personality factors. Work-environment characteristics include climatic factors such as supervisory or peer support as well as constraints and opportunities to perform learned behaviors on the job.»
  - «These effects are specified in terms of six linkages […] training outcomes of learning and retention are seen as having direct effects on conditions of transfer (Linkage 6).» «Trainee characteristics and work-environment characteristics are also hypothesized to have direct effects on transfer regardless of initial learning during the training program or retention of the training material (Linkages 4 and 5, respectively). For example, well-learned skills may not be maintained on the job due to lack of motivation or lack of supervisory support.» «training outcomes (learning and retention) are viewed as directly affected by the three training inputs of training design, trainee characteristics, and the work-environment characteristics (Linkages 1, 2, and 3 respectively). These three training inputs, therefore, have an indirect effect on transfer through their impact on training outcomes.»
  - Sobre el 10 %: «It is estimated that while American industries annually spend up to $100 billion on training and development, not more than 10% of these expenditures actually result in transfer to the job (Georgenson, 1982).» Bibliografía: «Georgenson DL. (1982). The problem of transfer calls for partnership. Training and Development Journal, 36( lo), 75-78.» (el OCR lee «lo»; sería el número 10)
- Blume, Ford, Baldwin y Huang (2010): sin texto completo. OpenAlex la marca «closed» y «any_repository_has_fulltext: False»; las copias de CiteSeerX dieron 404. El abstract de OpenAlex coincide con lo que ya dice la nota (89 estudios, habilidades abiertas y cerradas, «consistently inflated»).

**Qué se cambió**:

- La fuente de Baldwin y Ford pasó de «vía Wikipedia» a texto completo.
- La definición se cita del original. Wikipedia queda solo para «the most commonly cited model».
- **Corrección**: el diagrama mostraba los tres insumos llegando a la transferencia solo a través del aprendizaje, y la nota decía que no se sabía qué efecto directo tenía cada uno. El original suma dos efectos directos sobre la transferencia: el de quien aprende (vínculo 4) y el del ambiente (vínculo 5). El diseño llega solo en forma indirecta. Se rehízo el diagrama con los seis vínculos numerados como en el artículo. Era un hueco de la nota, no una afirmación contraria, así que no lleva `[!IMPORTANT]`.
- El 10 %: la nota decía que no se encontró una fuente primaria. Ahora dice que Baldwin y Ford ya la presentan como estimación, citando a Georgenson (1982), y que no se encontró un estudio que la mida. La conclusión (esta base no la usa) sigue igual.
- El aviso se achicó.

**Sigue faltando**: los tamaños de efecto de Blume et al. (2010) y el artículo de Georgenson (1982).

## Fuera del lote

- `Evaluacion-educativa/Fundamentos/fundamentos-de-evaluacion-educativa.md`, línea 54: la tabla de mitos dice, sobre «Solo el 10 % de una capacitación se transfiere», «No se encontró fuente primaria». Se podría precisar: la cifra viene de una estimación de Georgenson (1982) que citan Baldwin y Ford (1988), y no de una medición. No se editó.

## Después del cotejo

Recortes: Russ-Eft y Preskill dicen que los pedidos de ROI son reacciones «knee-jerk» «based on a lack of understanding and misconceptions about evaluation»; se sacó «de quien quiere algo que suene a resultados». El MDES ya no se define en la nota (el extracto solo dice que depende de la muestra). El documento de la EEF de 2019 figura como leído en las secciones A a C y el apéndice 1. Kirkpatrick: la revista se nombra por el pie «Training Directors», y *Kirkpatrick Then and Now* pasa a `fuentes:` por la fecha de 1959. En `fundamentos-de-evaluacion-educativa.md`, el 10 % es «una estimación que Baldwin y Ford atribuyen a Georgenson (1982)».
