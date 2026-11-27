---
resumen: >-
  Búsqueda de fuentes para los avisos «Sin fuente todavía» de Evaluacion-educativa/Evaluacion-adaptativa (issue #153).
creado: 2026-11-27
---

# Fuentes para los avisos de Evaluación adaptativa (issue #153)

Tres avisos en tres notas. Se cerró el de seguimiento del conocimiento: Corbett y Anderson leído en el original y las cifras de Khajah et al. verificadas. Quedó un aviso nuevo, más chico. Se achicaron los otros dos: espacios de conocimiento y teoría de respuesta al ítem. Se corrigió una fecha con `[!WARNING]`: el artículo de Corbett y Anderson es de 1995, no de 1994.

Los extractos en inglés son literales de lo que se leyó; en los PDF escaneados con OCR se corrigieron solo errores de reconocimiento evidentes (letras y símbolos). Los PDF con capa de texto se extrajeron con `pdftotext`. El de Corbett y Anderson es un escaneo sin texto: se leyeron las imágenes de las págs. 253-262.

## 1. Seguimiento del conocimiento (`Evaluacion-adaptativa/seguimiento-del-conocimiento.md`)

**Faltaba**: Corbett y Anderson leído en el original, y las cifras de AUC de Khajah et al. (2016) verificadas en el artículo.

**Se encontró**:

- Corbett, A. T. y Anderson, J. R., *Knowledge Tracing: Modeling the Acquisition of Procedural Knowledge*, User Modeling and User-Adapted Interaction 4:253-278, doi 10.1007/BF01099821. PDF escaneado en el sitio de ACT-R (Carnegie Mellon): http://act-r.psy.cmu.edu/wordpress/wp-content/uploads/2012/12/893CorbettAnderson1995.pdf. **Texto completo; se leyeron las págs. 253-262** (resumen, modelo y procedimiento).
  - Encabezado: «User Modeling and User-Adapted Interaction 4: 253-278, 1995. © 1995 Kluwer Academic Publishers.» «(Received 1 December 1994; in final form 13 March 1995)».
  - Resumen: «Students in this research are learning to write short programs with the ACT Programming Tutor (APT).» «As the student works, the tutor also maintains an estimate of the probability that the student has learned each of the rules in the ideal model, in a process called knowledge tracing.»
  - Pág. 260: «Knowledge tracing assumes a two-state learning model. Each coding rule is either in the learned state or in the unlearned state.» «There is no forgetting; rules do not make the transition in the other direction.» «If a rule is in the learned state, the student may nevertheless slip and make a mistake. If the rule is in the unlearned state, there is some chance the student will guess correctly.»
  - Fig. 4, pág. 261: «p(L0) Initial Learning: the probability a rule is in the learned state prior to the first opportunity to apply the rule (i.e., from reading the text). p(T) Acquisition: the probability a rule will make the transition from the unlearned to the learned state following an opportunity to apply the rule. p(G) Guess: the probability a student will guess correctly if a rule is in the unlearned state. p(S) Slip: the probability a student will slip (make a mistake) if a rule is in the learned state».
  - Pág. 261: «That mastery criterion in the tutor is a knowledge probability of 0.95.»
  - La pág. 262 sitúa el currículo: «Each of the four studies focuses on the first chapter in the Lisp Tutor curriculum.»
  - Un resumen del buscador atribuye el año 1994 a la cita de Springer. Semantic Scholar y Wikipedia dan 1995, según la nota anterior; OpenAlex también da 1995.
- Khajah, M., Lindsey, R. V. y Mozer, M. C. (2016), *How Deep is Knowledge Tracing?*, arXiv:1604.02416v2 (21 de junio de 2016). https://arxiv.org/abs/1604.02416. **Texto completo** (PDF de arXiv).
  - Resumen: «We demonstrate that when BKT is extended to allow it more flexibility in modeling statistical regularities—using extensions previously proposed in the literature—BKT achieves a level of performance indistinguishable from that of DKT.»
  - Leyenda de la fig. 2: «BKT+A= BKT with inference of latent student abilities; BKT+F= BKT with forgetting; BKT+S= BKT with skill discovery; BKT+FSA= BKT with all three extensions».
  - «On Assistments, classic BKT obtains an AUC of 0.73, better than the 0.67 reported for BKT by Piech et al.» «BKT+F obtains an AUC of 0.83, not quite as good as the 0.86 value reported for DKT by Piech et al.»
  - «To summarize the comparison of BKT and DKT, 31.6% of difference in performance reported in [22] appears to be due to the use of a biased procedure for computing the AUC for BTK. Another 50.6% of the difference in performance reported vanishes if BKT is augmented to allow for forgetting.»
  - «The full model, BKT+FSA, obtains an AUC of 0.75 and our implementation of DKT obtains a nearly identical AUC of 0.76. On Spanish, the BKT extensions obtain very little benefit. The full model, BKT+FSA, obtains an AUC of 0.846 and again, DKT obtains a nearly identical AUC of 0.836.»
  - El artículo no menciona a Xiong et al. ni a Wilson et al. (2016).

**Qué se cambió**:

- La tabla de BKT sale ahora del artículo, con los nombres originales (p(L0), p(T), p(G), p(S)), en lugar de Wikipedia.
- Se sumaron los dos estados, el «no forgetting» y el criterio de dominio de 0,95. Las extensiones de Khajah se nombran como en su figura.
- Se sumaron los porcentajes 31,6 y 50,6, y se sacó «hay que verificarlas».
- `[!WARNING]` por la fecha: la base usaba 1994 y el artículo impreso dice 1995. La nota pasa a citar 1995.

El aviso original se cerró. Quedó uno nuevo con lo que sigue faltando.

**Sigue faltando**: Xiong et al. (2016) y Wilson et al. (2016), que siguen «según el buscador»; las págs. 263-278 de Corbett y Anderson, con los cuatro estudios empíricos.

## 2. Teoría de respuesta al ítem (`Evaluacion-adaptativa/teoria-de-respuesta-al-item.md`)

**Faltaba**: un manual leído (Embretson y Reise, 2000; Wainer, 2000) y el contraste de Hambleton y Jones (1993).

**Se encontró**: Hambleton, R. K. y Jones, R. W. (1993), *Comparison of Classical Test Theory and Item Response Theory and Their Applications to Test Development*, Educational Measurement: Issues and Practice 12(3):38-47, doi 10.1111/j.1745-3992.1993.tb00543.x (volumen, número y páginas según Crossref). Módulo ITEMS de NCME: https://ncme.org/wp-content/uploads/2025/10/Module-16-Comparison-of-CTT-and-IRT-Hambleton-J-1.pdf. **Texto completo.** Extractos:

- «The intent of this module is to provide a nontechnical comparison of classical test theory and item response theory.»
- Tabla comparativa, teoría clásica: «Weak (i.e., easy to meet with test data)»; «No-item and person parameters are sample dependent»; «Sample size (for item parameter estimation) 200 to 500 (in general)».
- Misma tabla, IRT: «Strong (i.e., more difficult to meet with test data)»; «Yes-item and person parameters are sample independent, if model fits the test data»; «Depends on the IRT model but larger samples, i.e., over 500, in general, are needed».
- «one main shortcoming is that they are sample dependent»; «Another limitation of classical test theory is that scores obtained by classical test theory applications are entirely test dependent. Consequently, test difficulty directly affects the resultant test scores.»
- «in computer adaptive testing, in which examinees may see tests of substantially different difficulties, test-dependent scores such as estimated true scores would be of no value in comparing examinees.»
- Ventajas de la teoría clásica: «1. Smaller sample sizes required for analyses (a particularly valuable advantage for field testing). 2. Simpler mathematical analyses compared to item response theory.»
- «The item parameters, b, a, and c, are correspondingly referred to as the item difficulty, item discrimination, and pseudoguessing parameters.» «Simpler logistic test models can be obtained by setting ci = 0 (the two-parameter model) or setting ci = 0 and ai = 1 (the one-parameter model).»
- «Model fit too can be a problem».

Embretson y Reise (2000) y Wainer (2000) son libros sin copia libre; no se buscaron más.

**Qué se cambió**:

- Dos párrafos con el contraste de Hambleton y Jones en «En qué se diferencia de la teoría clásica».
- Un párrafo bajo la tabla de modelos, con los nombres de los parámetros.
- Una fila nueva en la tabla de tamaños de muestra.

El aviso se achicó.

**Sigue faltando**: un manual leído.

## 3. Espacios de conocimiento (`Evaluacion-adaptativa/espacios-de-conocimiento.md`)

**Faltaba**: Doignon y Falmagne (1985 y 1999) leídos en el original, y una aplicación validada fuera de la matemática.

**Se encontró**:

- Falmagne, J.-C., Koppen, M., Villano, M., Doignon, J.-P. y Johannesen, L. (1990), *Introduction to Knowledge Spaces: How to Build, Test, and Search Them*, Psychological Review 97(2):201-224. Copia en un curso de Carnegie Mellon: https://stat.cmu.edu/~brian/nynke/726-2021/project%20HCI%20Prereqs%20(Elaine,%20Smeet%20&%20Zhou)/2021-02-23/Falmagne90.pdf. **Texto completo.** Es de los mismos autores y resume su trabajo previo, incluido el de 1985: «Most of the results presented summarize previous articles published in various technical journals.» Extractos:
  - «the knowledge state of a subject with regard to a specified field of information can be represented by a particular subset of questions or problems that the subject is capable of solving. The family of all knowledge states forms the knowledge space. It is assumed that if 2 subsets K and K' of questions are assumed to be states in a knowledge space K, then K ∪ K' is also assumed to be a state».
  - «Such a theory is consistent with the idea that at least some of the notions in the field may be acquired from different sets of prerequisites.»
  - «A first sketch of the knowledge space can be obtained by consulting expert teachers in the field.» «This preliminary construction can then be tested and refined on the basis of empirical data.»
  - Pregunta al experto: «[Q1] Suppose that a student under examination has just provided a wrong response to problem q. Is it practically certain that this student will then also fail problem q'?»
  - «a subject might make a careless error in a computation or might guess the correct response»; «correct responses resulting from lucky guesses».
  - «An exemplary application of this probabilistic theory to a high school mathematics test is described, based on a sample of several hundred students. By standard likelihood ratio methods, it is shown how the preliminary knowledge space can be gradually refined, and the number of possible knowledge states substantially reduced.»
- Stefanutti, L. y Cristante, F., *Empirical validation of a knowledge structure for assessment and learning of psychometrics at university level*, ponencia (4 págs.) en el repositorio de IASE, carpeta de la 54.ª sesión del ISI: https://fpce.uc.pt/iase-web/documents/papers/isi54/3440.pdf. **Texto completo.** El texto no trae el año. Extractos:
  - «courses of statistics, psychometrics and data analysis of the Faculty of Psychology of the University of Padova, Italy».
  - «their topic is "basic probability theory", "contingency tables" and "log-linear analysis"».
  - «A knowledge space was obtained for the above-mentioned set of items through a computerized query of five experts of the domain of knowledge.»
  - «A test Q containing the 10 selected items was administered to a group of 400 Italian students».
  - Primera mitad: «a likelihood ratio of 23.46 that with 32 − 10 − 5 − 1 = 16 degrees of freedom has a probability of .102, thus the model is accepted.» Segunda: «a likelihood ratio of 23.84 was obtained. With 16 degrees of freedom also this value is not significant, suggesting that the model can be accepted.»
  - «the lucky guess probability γ8 is very high (0.78)»; «Taking into account that item 8 was a multiple choice item with 5 different alternatives, this result would suggest that either the model is not correct or the data for this item are unreliable.»
- Doignon y Falmagne (1985), *Spaces for the assessment of knowledge*, International Journal of Man-Machine Studies 23(2):175-196 (datos de la bibliografía de Stefanutti y Cristante y de un resumen del buscador). No se consiguió el texto.

**Qué se cambió**:

- La definición de espacio pasa de Wikipedia al artículo de 1990.
- Un párrafo nuevo sobre cómo se arma y se pone a prueba el grafo.
- En «Cómo falla», un párrafo con la aplicación de Padua y su límite: un problema dio una probabilidad de acierto por suerte de 0,78.

El aviso se achicó: la aplicación encontrada es de estadística para psicología, cerca todavía de la matemática.

**Sigue faltando**: Doignon y Falmagne (1985 y 1999) leídos en el original, y una aplicación validada lejos de la matemática y la estadística. Un resumen del buscador menciona otras, sin verificar: Spoto, Stefanutti y Vidotto (2010), en *Behavior Research Methods*, sobre evaluación psicológica; y ALEKS en química.

## Fuera del lote

- `Evaluacion-educativa/Fundamentos/fundamentos-de-evaluacion-educativa.md`, línea 34: fecha a Corbett y Anderson en 1994. El artículo impreso dice 1995.
- `Evaluacion-educativa/Evaluacion-adaptativa/evaluacion-adaptativa.md`, línea 9: cita «Corbett y Anderson (1994)» en `fuentes:`.
- `Evaluacion-educativa/.investigacion/adaptativa-calificacion-programa.md`, líneas 86, 91 y 296: usan 1994.

## Después del cotejo

Recortes: en seguimiento del conocimiento, el criterio de 0,95 se dice como en el extracto («mastery criterion in the tutor is a knowledge probability of 0.95») y se sacó que el tutor actualiza la probabilidad «en cada oportunidad»; el aviso de 1994 ya no dice que otras notas lo repiten (se corrigieron `evaluacion-adaptativa.md` y la tabla de `fundamentos-de-evaluacion-educativa.md`). Crossref (https://api.crossref.org/works/10.1007/BF01099821) da «issued» 1995, volumen 4, número 4, págs. 253-278. En IRT, «sample dependent» se dice de los parámetros de pregunta y persona, como en la tabla de Hambleton y Jones.
