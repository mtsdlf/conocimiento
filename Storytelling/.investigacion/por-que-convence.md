# Informe: Storytelling, vertical "Por qué convence"

Todo salió de WebSearch y WebFetch. Dos cosas condicionan la lectura:
- **Bloqueos.** OpenAlex dio 429 y PubMed, PMC y City Research Online bloquearon el acceso automático. Tres PDF sí bajaron y los leí completos con `pdftotext`: Mar 2021, Zebregs 2015 y Nave 2015.
- **Números sin texto completo.** Los de Braddock & Dillard, Shen et al., Lee & Feeley, Freling 2020 y Hasson 2010 vienen de resúmenes del buscador [S]. Están marcados y hay que verificarlos contra el texto antes de volcarlos como vigentes.

Escala de puntaje: autoridad / profundidad / ejemplos / unicidad, de 1 a 3.

## Sobre la división del árbol

La división en tres componentes sirve, pero el campo no la hace así.

- **La unidad del campo es el mecanismo y el resultado medido.** Para el campo, transporte, identificación y resistencia son un solo modelo teórico (E-ELM más EORM). Si se separan, hay que enlazarlos.
- **"memoria-y-emocion" junta tres literaturas distintas.**
  - La memoria de textos es psicología cognitiva, con evidencia sólida.
  - La oxitocina es endocrinología social, con evidencia débil.
  - El acoplamiento neural es neurociencia de la comunicación, con un solo estudio de n pequeño.
  - Conviene tratar la oxitocina y el acoplamiento como "mitos y sus límites", no como mecanismos.
- **"historia-o-argumento" tiene una respuesta que depende de cuatro variables.** Son el resultado medido (creencia, actitud, intención o conducta), el compromiso emocional del público, el contexto y si se combinan ambos. Hay evidencia de que la combinación supera a cada uno por separado.
- **El efecto víctima identificable es una literatura propia.** Es donaciones y juicio, no narrativa en el sentido de la persuasión narrativa. Conviene dejarlo como nota lateral.

---

## 1. transporte-narrativo

| Fuente | URL | Tipo | Marca | Puntaje |
|---|---|---|---|---|
| Green & Brock 2000, JPSP 79(5), 701-721 | https://gwern.net/docs/www/pdfs.semanticscholar.org/39691cee32e52fbfc33f1a0316aa0d008cb699a4.pdf (copia de las primeras páginas) | Primaria | [S] | 3/3/2/3 |
| Slater & Rouner 2002, Communication Theory 12(2), 173-191 | https://narrativestudies.lib.unb.ca/bibcite/reference/25453 | Primaria (solo cita) | [M] | 3/1/1/3 |
| Moyer-Gusé 2008, Communication Theory 18, 407-425 | https://core.ac.uk/download/357574034.pdf (aparece en la búsqueda; no confirmé que contenga el artículo de 2008) | Primaria | [S] | 3/1/1/3 |
| Van Laer et al. 2014, JCR 40(5), 797-817, DOI 10.1086/673383 | https://openaccess.city.ac.uk/id/eprint/6755/ (bloqueado); metadatos en https://api.crossref.org/works/10.1086/673383 | Primaria, meta-análisis | [M] | 3/2/1/3 |
| Braddock & Dillard 2016, Communication Monographs 83(4), 446-467, DOI 10.1080/03637751.2015.1128555 | https://api.crossref.org/works/10.1080/03637751.2015.1128555 (metadatos); resumen en https://assets.publishing.service.gov.uk/media/5d8b7af6e5274a08c7408c1a/Braddock-Belief-Attitude-and-Behavior-Change.pdf | Primaria, meta-análisis (accedida vía secundarias) | [M] y [L] de la cita secundaria | 3/2/1/3 |
| Rahmani, Montano, Groves & Green 2025, Behavioural Public Policy | https://www.cambridge.org/core/journals/behavioural-public-policy/article/persuasive-effects-of-narrative-entertainment-a-metaanalysis-of-recent-experiments/07CABFC5ABA0D3A6A369FCDDB21F8F76 | Primaria, meta-análisis | [M] (página resumida por el fetcher) | 3/2/1/3 |
| Cohen 2001, Mass Communication & Society 4, 245-264 | https://informahealthcare.com/doi/full/10.1207/S15327825MCS0403_01 | Primaria (solo cita) | [M] | 3/1/1/3 |
| Van Laer, Feiereisen & Visconti 2019, J. Business Research | https://www.sciencedirect.com/science/article/abs/pii/S0148296318305356 | Primaria | [M] | 3/1/1/2 |

**Afirmaciones**
- Green & Brock definen el transporte como absorción en la historia: "a convergent process, where all the person's mental systems and capacities become focused on the events occurring in the narrative". La medida es una escala de autorreporte posterior a la exposición (https://gwern.net/docs/www/pdfs.semanticscholar.org/39691cee32e52fbfc33f1a0316aa0d008cb699a4.pdf) [S].
- El mecanismo del E-ELM, según el propio resumen del artículo: cuando el espectador está absorbido en el drama, baja la contraargumentación (https://narrativestudies.lib.unb.ca/bibcite/reference/25453) [M].
- El EORM de Moyer-Gusé nombra tres resistencias que el compromiso narrativo puede reducir: reactancia, contraargumentación e invulnerabilidad percibida (https://core.ac.uk/download/357574034.pdf) [S].
- **Advertencia sobre el mecanismo.** Revisiones posteriores señalan que varios estudios no encontraron que el transporte medie el efecto. Parte de esos fallos se atribuyó a cómo se manipuló el transporte, incluidos los experimentos 1 a 3 de Green & Brock (https://gwern.net/docs/www/pdfs.semanticscholar.org/39691cee32e52fbfc33f1a0316aa0d008cb699a4.pdf) [S].
- Van Laer et al. 2014 es "a quantitative meta-analysis of 132 effect sizes of narrative transportation from 76 published and unpublished articles" (https://openaccess.city.ac.uk/id/eprint/6755/) [M]. Un fragmento del buscador habla de efectos "small but not trivial (.10 ≤ r ≤ .30)". No confirmé que ese rango sea el de actitud e intención, y no obtuve el coeficiente por consecuencia.
- Braddock & Dillard 2016, narrativa contra control, según un fragmento del buscador sin fuente fijada [S] (probable origen: https://thedecisionlab.com/insights/society/can-stories-change-us):
  - creencias: k = 37, N = 7,376, r = .17;
  - actitudes: k = 40, N = 7,132, r = .19;
  - intenciones: k = 28, N = 5,211, r = .17;
  - conductas: k = 5, N = 978, r = .23.
- La nota del gobierno británico confirma que ni el medio ni el diseño de investigación moderaron la magnitud (https://assets.publishing.service.gov.uk/media/5d8b7af6e5274a08c7408c1a/Braddock-Belief-Attitude-and-Behavior-Change.pdf) [L].
- **Discrepancia sobre ficción y no ficción.** Un resumen del buscador dice que la ficción no movió creencias y la no ficción no movió actitudes. Otra fuente dice que la ficcionalidad no moderó. Dos fuentes que se contradicen: hay que leer el artículo.
- **Contrapunto reciente.** Rahmani et al. 2025 (63 comparaciones de 47 artículos en el análisis principal; 24,380 encuestados en total) midieron el efecto de narrativa audiovisual contra un control puro. Reportan (https://www.cambridge.org/core/journals/behavioural-public-policy/article/persuasive-effects-of-narrative-entertainment-a-metaanalysis-of-recent-experiments/07CABFC5ABA0D3A6A369FCDDB21F8F76) [M]:

| Resultado | β | IC 95% |
|---|---|---|
| Creencias | 0.316 | [0.082, 0.550] |
| Intenciones | 0.299 | [0.114, 0.484] |
| Conductas | 0.21 | [0.008, 0.411] |
| Normas | 0.058 | [-0.185, 0.301] (no significativo) |

  - Contra material no narrativo, la ventaja de la narrativa es "inconclusive, with at most a slight advantage". La comparación se apoya en solo 14 estudios y los autores la consideran de baja potencia (parafraseado por el fetcher).
- Cohen 2001 define la identificación como vivir el texto desde adentro, como si los hechos le pasaran a uno. Es una fuente teórica y no aporta tamaño de efecto. Hay un meta-análisis de similitud personaje-receptor (https://www.researchgate.net/publication/374756721_A_Meta-Analysis_Examining_the_Role_of_Character-Recipient_Similarity_in_Narrative_Persuasion) [M], no leído.
- Van Laer, Feiereisen & Visconti: el efecto es mayor en dominio comercial, con historias generadas por usuarios y con un receptor a la vez. Sale de un fragmento de buscador, con 64 artículos y 138 tamaños de efecto [S].

**Recurso canónico:** Van Laer et al. 2014 (JCR), secciones del modelo y de antecedentes y consecuencias. Hay que mirar el cuadro de correlaciones por consecuencia, la diferencia entre transporte e imagen, y que los efectos son pequeños. Para el resultado de persuasión puro, Braddock & Dillard 2016, junto con Rahmani 2025 como contrapeso.

---

## 2. memoria-y-emocion

| Fuente | URL | Tipo | Marca | Puntaje |
|---|---|---|---|---|
| Mar, Li, Nguyen & Ta 2021, Psychon Bull Rev 28, 732-749 | https://link.springer.com/article/10.3758/s13423-020-01853-1 (texto leído desde la copia de autor https://www.yorku.ca/mar/Mar%20et%20al%202021_PB&R_Mem%20and%20Comp%20of%20N%20and%20E%20texts%20meta-analysis_Final.pdf) | Primaria, meta-análisis | [L] | 3/3/2/3 |
| Nave, Camerer & McCullough 2015, Perspect Psychol Sci 10(6), 772-789 | https://pages.ucsd.edu/~memccullough/Papers/NaveCamererMcCullough15.pdf | Primaria, revisión crítica | [L] | 3/3/2/3 |
| Stephens, Silbert & Hasson 2010, PNAS 107(32), 14425-14430 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2922522 (bloqueado); ficha https://hassonlab.princeton.edu/publications/speaker%E2%80%93listener-neural-coupling-underlies-successful-communication | Primaria | [S] | 3/2/1/3 |
| Lin, Grewal, Morin, Johnson & Zak 2013, PLOS ONE | https://pmc.ncbi.nlm.nih.gov/articles/PMC3584120 (en resultados; atribución según el buscador) | Primaria | [S] | 2/1/1/2 |
| Clinton et al. 2020 (comprensión inferencial) | citado en Mar 2021 | Primaria | [L] vía Mar | 3/2/1/2 |

Nota de autoría: el trabajo de 2010 es de Stephens, Silbert y Hasson. Stephens es el primer autor, no Hasson, aunque se lo cite así.

**Afirmaciones**
- **Mar et al. 2021** [L] (https://www.yorku.ca/mar/Mar%20et%20al%202021_PB&R_Mem%20and%20Comp%20of%20N%20and%20E%20texts%20meta-analysis_Final.pdf):
  - Resultado global: "Hedge's g of .55, with a 95% CI ranging from .31 to .79, p < .001", sobre 37 estudios y 150 tamaños de efecto. El texto dice "over 75 unique samples" y 33,078 participantes (se lee en el diagrama de selección).
  - Un resumen secundario habla de 78 muestras independientes; el artículo dice "more than 75". Tomar el del artículo.
  - Heterogeneidad: Q(149) = 2884.68, p < .001.

  | Subgrupo | g | IC 95% |
  |---|---|---|
  | Comprensión (29 estudios, 93 efectos) | .48 | .21, .75 |
  | Memoria (14 estudios, 57 efectos) | .72 | .43, 1.01 |
  | Adultos (19 estudios) | .44 | .10, .77 |
  | No adultos (18 estudios) | .67 | .33, 1.01 |

  - Ningún moderador resultó significativo, aunque los propios autores dicen que puede ser falta de potencia. Memoria contra comprensión tuvo p = .09.
  - **Sesgo de publicación.** Egger b = 2.68 (IC 95% .57, 4.80), p = .01, concentrado en memoria: b = 2.91, p = .02. Para comprensión no hay evidencia (p = .30). Este es el matiz a decir en voz alta: la ventaja en memoria es la más grande y también la más sospechosa.
  - Solo el 28% de los tamaños de efecto vino de estudios donde se controló el contenido de los textos.
  - Hay solo cuatro estudios con demora y seis con test verbal.
  - Los textos son relatos y ensayos, no mensajes de marca. No prueba que una historia comercial se recuerde más que una lista de beneficios.
- **Nave et al. 2015** [L] (https://pages.ucsd.edu/~memccullough/Papers/NaveCamererMcCullough15.pdf):
  - Siete estudios de oxitocina intranasal sobre confianza, con 481 sujetos, dan "Cohen's d = 0.077, 95% CI [-0.124, 0.278], z = 0.75, p = .45".
  - Detectar incluso el límite superior de 0.278 con potencia 0.80 exigiría "more than 400 subjects".
  - Sobre la oxitocina en plasma, Zak et al. 2005 (N = 96) "reported no association between unextracted plasma OT and trust game investment". Zhong et al. 2012 (N = 1,158) encontró una relación en U.
  - La revisión cita a Zak 2011 por apodar a la oxitocina "moral molecule" y no le atribuye ningún experimento propio de narrativa.
  - La revisión no trata el estudio de narrativa y donaciones; eso es del trabajo de 2013 de Lin et al. Según el buscador, ese trabajo reportó con oxitocina "57% more causes", "56% more money" y "17% greater concern" frente a placebo. El efecto es del fármaco, no de la historia (https://pmc.ncbi.nlm.nih.gov/articles/PMC3584120) [S].
  - No encontré réplica de ese resultado de donaciones. Walum, Waldman & Young 2015 argumentan que, por baja potencia, los intentos de réplica de hallazgos verdaderos fallarían hasta el 88% de las veces (https://pmc.ncbi.nlm.nih.gov/articles/PMC3584120, enlace del hallazgo; fuente exacta de Walum sin verificar) [S].
  - Conclusión para el árbol: "las historias liberan oxitocina y por eso generan confianza" es una afirmación no sostenida. Nave et al. no dicen que la oxitocina no haga nada. Dicen que el vínculo con la confianza humana no es robusto.
- **Hasson (Stephens, Silbert & Hasson 2010)** [S] (https://hassonlab.princeton.edu/publications/speaker%E2%80%93listener-neural-coupling-underlies-successful-communication):
  - Una persona contó una historia sin ensayar mientras se la registraba con fMRI, y un oyente escuchó la grabación.
  - Hubo acoplamiento que desaparece "when participants fail to communicate".
  - El resumen del buscador da r = 0.54, P < 0.07 para acoplamiento y comprensión, y r = 0.75, P < 0.01 en áreas donde el oyente se anticipa.
  - Alcance real: un hablante, historia única y un puñado de oyentes. Es correlacional y no compara historia con argumento. No prueba que la historia acople más que otro formato.

**Recurso canónico:** Mar et al. 2021, la Tabla 3 y la sección de discusión sobre sesgo de publicación. Hay que leer el contraste memoria contra comprensión y el Egger.

---

## 3. historia-o-argumento

| Fuente | URL | Tipo | Marca | Puntaje |
|---|---|---|---|---|
| Zebregs, van den Putte, Neijens & de Graaf 2015, Health Commun 30(3), 282-289 | https://pure.uva.nl/ws/files/2680645/167737_497142.pdf | Primaria, meta-análisis | [L] | 3/3/2/3 |
| Allen & Preiss 1997, Commun Res Rep 14(2), 125-131 | https://narrativestudies.lib.unb.ca/bibcite/reference/19279 | Primaria (solo ficha) | [M], cifras [S] | 3/2/1/3 |
| Allen et al. 2000, Western J Commun | https://www.uky.edu/~ngrant/CJT780/readings/Day%203/AllenETAL2000.pdf | Primaria | [S] | 3/2/1/3 |
| Shen, Sheer & Li 2015, J Advertising 44(2), 105-113 | https://pure.psu.edu/en/publications/impact-of-narratives-on-persuasion-in-health-communication-a-meta/ | Primaria, meta-análisis | [S] | 3/2/1/3 |
| Xu 2023, Health Commun 38(14) | https://www.researchgate.net/publication/364681413_A_Meta-Analysis_Comparing_the_Effectiveness_of_Narrative_vs_Statistical_Evidence_Health_vs_Non-Health_Contexts | Primaria, meta-análisis | [S] | 3/2/1/3 |
| Freling, Yang, Saini, Itani & Abualsamh 2020, OBHDP 160, 51-67 | https://scholarworks.utrgv.edu/cgi/viewcontent.cgi?article=1096&context=marketing_fac (403) | Primaria, meta-análisis | [S] | 3/2/2/3 |
| Lee & Feeley 2016, Social Influence 11(3) | https://informahealthcare.com/doi/abs/10.1080/15534510.2016.1216891 | Primaria, meta-análisis | [S] | 3/2/1/3 |
| Maier, Wong & Feldman 2023 (reanálisis y réplica) | https://www.cambridge.org/core/product/3DA967642DBCD4E6117CCA104F3D6854/core-reader | Primaria | [S] | 3/2/1/3 |
| Gilliam & Flaherty 2015, Industrial Marketing Management 46, 132-142 | https://econbiz.de/Record/storytelling-by-the-sales-force-and-its-effect-on-buyer-seller-exchange-gilliam-david/10011286969 | Primaria (ficha) | [M] | 3/1/2/3 |
| Lacoste & La Rocca 2015, comentario | https://www.sciencedirect.com/science/article/abs/pii/S0019850115000322 | Primaria (comentario) | [M] | 2/1/1/2 |
| Gilliam y Zablah, nota del Keller Center | https://kellercenter.hankamer.baylor.edu/news/story/2014/power-storytelling | Secundaria | [S] | 1/1/2/2 |

**Afirmaciones**
- **Zebregs 2015** [L] (https://pure.uva.nl/ws/files/2680645/167737_497142.pdf): "Statistical evidence was found to have a stronger influence than narrative evidence on beliefs and attitude, whereas narrative evidence had a stronger influence on intention." El estudio es del ámbito de la salud, con algunos temas de otros ámbitos. Tabla 3, con el signo en que negativo favorece a la estadística (confirmado por el texto de la tabla 2 del artículo):

| Resultado | Estudios | n total | ES medio | SE | IC |
|---|---|---|---|---|---|
| Creencias | 9 | 1546 | −0.16 | 0.07 | −0.29 a −0.03 (p = .014) |
| Actitud | 5 | 1850 | −0.11 | 0.06 | −0.23 a 0.00 (p = .058) |
| Intención | 7 | 1338 | 0.10 | 0.05 | 0.00 a 0.20 (p = .061) |

  - Los propios autores dicen que actitud e intención son "only marginally significant". Entre creencias e intención, DIF = 0.26; SE = 0.08; z = 3.10; p = .002. No hubo diferencia significativa entre creencias y actitud.
  - Menciona que el efecto emocional de la narrativa podría ser temporal y que los efectos de la estadística podrían durar más; no está probado en el meta-análisis.
- **Allen & Preiss 1997** [M/S]: 15 investigaciones, la estadística más persuasiva, r = .101 según un resumen. Otra fuente cita r = .074 con 16 estudios y 1,836 participantes. Dos cifras discrepantes que hay que verificar contra el artículo (https://narrativestudies.lib.unb.ca/bibcite/reference/19279). Zebregs menciona que solo 2 de los 15 estudios del suyo coinciden con los de Allen & Preiss.
- **Combinar** [S]: Allen et al. 2000 (15 mensajes, 1,270 participantes) encontraron que el mensaje que combina ambas formas persuade más que cada una (https://www.uky.edu/~ngrant/CJT780/readings/Day%203/AllenETAL2000.pdf).
- **Shen, Sheer & Li 2015** [S]: 25 estudios, N = 9,330, efecto global de narrativa "r = .063 (p < .01)". Los formatos de audio y video tuvieron efecto significativo; el impreso, no. O'Keefe y Hoeken (2021, vía Xu) encontraron heterogeneidad sustancial (https://pure.psu.edu/en/publications/impact-of-narratives-on-persuasion-in-health-communication-a-meta/).
- **Discrepancia con Zebregs.** Xu 2023 (65 pares experimentales) no halló diferencias significativas entre evidencia narrativa y estadística en ningún contexto comunicativo. Sí halló ventaja narrativa en mensajes de prevención (https://www.researchgate.net/publication/364681413_A_Meta-Analysis_Comparing_the_Effectiveness_of_Narrative_vs_Statistical_Evidence_Health_vs_Non-Health_Contexts) [S]. Hay que dar las dos y no prometer el patrón de Zebregs.
- **Freling et al. 2020** [S]: 61 artículos. Con alto compromiso emocional las anécdotas superan a las estadísticas; con compromiso bajo pesa más la estadística (https://scholarworks.utrgv.edu/cgi/viewcontent.cgi?article=1096&context=marketing_fac). No obtuve el tamaño de efecto. Es la pieza más útil para decidir en la práctica y a la vez la que falta cuantificar.
- **Efecto víctima identificable** [S] (https://informahealthcare.com/doi/abs/10.1080/15534510.2016.1216891; https://www.cambridge.org/core/product/3DA967642DBCD4E6117CCA104F3D6854/core-reader):
  - Lee & Feeley 2016: 41 estudios, "r = .05".
  - Los tres estudios más potentes mostraron efectos cercanos a cero.
  - Maier, Wong & Feldman 2023, con el mismo conjunto de datos y un análisis bayesiano robusto, hallan "moderate evidence of publication bias and strong evidence for no identifiable victim effect, with a model-averaged estimate of r = 0.002". Sus réplicas preregistradas de los Estudios 1 y 3 de Small, Loewenstein & Slovic 2007 no sostienen el efecto.
  - El tamaño del estudio original de Small et al. 2007 no lo verifiqué.
- **Ventas y B2B (Gilliam & Flaherty 2015)** [M/S]:
  - Es un estudio cualitativo, con entrevistas en profundidad y observación de campo según una fuente secundaria. No hay tamaño de efecto.
  - Las fichas lo describen como la exploración empírica inicial de la narración en relaciones cliente-proveedor.
  - Una fuente citante dice que los vendedores cuentan historias para transferir información, establecer credibilidad, persuadir y hacer sentir cómodos a los compradores.
  - Sobre la persuasión: si el comprador percibe el relato como táctica manipuladora, puede activar el conocimiento de persuasión y volverse escéptico (fuentes secundarias).
  - El comentario de Lacoste & La Rocca argumenta que los compradores participan en el relato y no son oyentes pasivos.
  - Discrepancia: dos DOI, 10.1016/j.indmarman.2015.01.015 y 10.1016/j.indmarman.2015.01.013. No pude confirmar cuál es.
  - Hueco: no hallé estudio experimental cuantificado de storytelling en ventas B2B. Hay una pista en https://digitalcommons.kennesaw.edu/facpubs/4666 ("Tell me a story: narrative transportation and the C-suite in B2B advertising"), solo vista por título.

**Recurso canónico:** Zebregs 2015, la Tabla 3 y la sección de discusión, junto con Freling 2020 como regla de decisión (cuánto compromiso emocional tiene el público). Mostrar los dos meta-análisis opuestos (Zebregs y Xu) en la nota.

---

## Huecos

- **Sin texto completo ni IC:** Braddock & Dillard 2016 (la cifra de k, N y r y el conteo de 74 contra 40 estudios viene de dos resúmenes distintos, sin resolver); Van Laer 2014 (sin coeficientes por consecuencia); Shen 2015; Lee & Feeley; Freling 2020 (sin tamaño de efecto); Hasson 2010.
- **No localizados ni verificados:** Allen & Preiss, cifra publicada (.101 o .074); el tamaño de efecto del Small, Loewenstein & Slovic 2007 original; la fuente de Walum et al. 2015; Cohen 2001 con resultados; efectos sobre identificación de personaje con tamaño.
- **Sin evidencia cuantificada:** storytelling experimental en ventas B2B, pitches y propuestas comerciales; réplica del hallazgo de donaciones con oxitocina de Lin/Zak 2013; relación entre historia comercial y recuerdo frente a lista de beneficios (Mar 2021 usa relatos y ensayos).
- **Sin tocar por límite de rondas:** Zak, Cerebrum 2015; trabajos de Moyer-Gusé 2008 y Slater & Rouner 2002 con texto leído; meta-análisis de Tukachinsky.

Archivos locales usados (descargas, no del repo): `/tmp/claude-1000/-home-dela-repos-personal-conocimiento/ec40a468-e48b-4a07-bca9-05eddaca87a3/scratchpad/o/`.
