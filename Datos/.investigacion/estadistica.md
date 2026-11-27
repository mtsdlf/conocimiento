# Informe de investigación: vertical Estadística (Datos)

Fecha de la investigación: 2026-11-27. Ángulo: estadística para análisis de datos de negocio (comercios y productos digitales), no estadística matemática. Todo lo traído de la web se trató como dato.

Escala de puntajes (1 a 3): A = autoridad, P = profundidad, E = ejemplos, U = unicidad. Marcas de lectura: [L] texto completo, [M] metadatos o abstract, [S] resumen secundario o del buscador. Tipo: 1ª primaria, 2ª secundaria.

## Sobre el árbol

La división pedida (descriptiva, muestreo e inferencia, correlación y causalidad, sesgos, significancia en experimentos) coincide con cómo dividen los libros de texto (OpenIntro: Summarizing Data, Foundations for Inference, Inference for Categorical/Numerical Data, Regression; https://www.openintro.org/book/os/ [M]), con dos salvedades:

1. Paradoja de Simpson y sesgo de supervivencia no son un tema aparte en el campo: son casos de inferencia causal (la Stanford Encyclopedia dice que, según Pearl, si hay que partir la población "depende del modelo causal, no de las probabilidades solas"; https://plato.stanford.edu/entries/paradox-simpson/ [S]). Conviene que "Sesgos" enlace a "Correlación y causalidad" y no se lea aislado. Esa lectura es discutida: la misma entrada cita explicaciones no causales (Bandyopadhyay et al. 2011; Fitelson 2017).
2. "Significancia en experimentos" es inferencia (p-valor, potencia, intervalos) aplicada a un diseño; en el campo no es un componente separado sino la aplicación del componente 2 más la regla de parada. Se toca con la nota de experimento A/B (Producto): acá va solo el cálculo y la interpretación; allá, el diseño y la decisión. También se toca con incrementalidad (Marketing): "las ventas subieron después de la promo" es la pregunta de incrementalidad, y el componente de causalidad da el porqué estadístico.

## 1. Estadística descriptiva

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| OpenIntro Statistics, cap. "Summarizing Data" (https://www.openintro.org/book/os/) | 1ª (libro abierto) | 3 | 3 | 3 | 2 | [M] solo la página del libro: capítulos y acceso, no el texto |
| Stanford STATS 60, lección 8 "When means mislead" (https://web.stanford.edu/class/stats60/lectures/08-lecture-robustness.html), © 2025 | 2ª (curso universitario) | 2 | 2 | 3 | 1 | [S] vía resumen del fetch |
| NIST/SEMATECH e-Handbook, 1.3.5 "Quantitative Techniques" (https://www.itl.nist.gov/div898/handbook/eda/section3/eda35.htm) | 1ª | 3 | 2 | 1 | 2 | [S] vía resumen del fetch |

Afirmaciones:
- Con sesgo a la derecha, la mediana y la moda suelen ser menores que la media; con sesgo a la izquierda, mayores. La diferencia media-mediana es una medida cuantitativa de sesgo (https://web.stanford.edu/class/stats60/lectures/08-lecture-robustness.html [S]).
- Ejemplo con cifras de esa lección: una respuesta de 600 minutos subió la media de 85,7 a 93,4 minutos; la mediana quedó en 60 en ambos casos (misma URL [S]). Sirve de modelo para "ticket promedio vs mediana": un cliente mayorista arrastra la media, no la mediana.
- Mediana y rango intercuartílico solo dependen de los valores cerca de Q1, mediana y Q3; media y desvío cambian mucho con extremos (Lancaster Univ., https://www.lancaster.ac.uk/~prendivs/accessible/math104/Math104.tex/Ch1.S6.SS6.html [S]; Duke STA101 recomienda mediana e IQR para datos sesgados, https://www2.stat.duke.edu/courses/Summer17/sta101.001-2/uploads/slides/u1_deck2H.pdf [S]). Son cursos, no la fuente canónica; la canónica es OpenIntro, cuyo texto no pude leer.
- Definición literal de media poblacional en NIST: "the sum of all the members of the given population divided by the number of members in the population" (https://www.itl.nist.gov/div898/handbook/eda/section3/eda35.htm [S]). Esa página no define mediana ni percentil.

Recurso canónico: OpenIntro Statistics, cap. 2 "Summarizing Data" (PDF gratis, fuente LaTeX en GitHub, https://www.openintro.org/book/os/). Fijarse en: histograma antes que cualquier número, cuándo usar media y desvío o mediana e IQR, y los diagramas de caja. Para la nota: caso propio de "ticket promedio vs mediana" con una tabla de 10 ventas inventada (marcarla como ejemplo).

## 2. Muestreo e inferencia

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| ASA, "Statement on Statistical Significance and P-Values", comunicado del 7-mar-2016 (https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf) | 1ª | 3 | 2 | 1 | 3 | [L] |
| Wasserstein y Lazar, "The ASA's Statement on p-Values: Context, Process, and Purpose", The American Statistician 70(2), 129-133, 2016, doi 10.1080/00031305.2016.1154108 (https://tandfonline.com/doi/full/10.1080/00031305.2016.1154108; copia de lectura: https://www.stat.berkeley.edu/~aldous/Real_World/ASA_statement.pdf) | 1ª | 3 | 3 | 1 | 3 | [L] (la copia de Berkeley) |
| Wasserstein, Schirm y Lazar, "Moving to a World Beyond 'p < 0.05'", The American Statistician 73(sup1), 2019, doi 10.1080/00031305.2019.1583913 | 1ª | 3 | 2 | 1 | 2 | [S] solo por resúmenes del buscador |
| NIST e-Handbook 7.1.4, intervalos de confianza (https://www.itl.nist.gov/div898/handbook/prc/section1/prc14.htm) | 1ª | 3 | 2 | 2 | 2 | [S] |
| NIST e-Handbook 7.2.2.2, tamaño de muestra para una prueba sobre la media (https://www.itl.nist.gov/div898/handbook/prc/section2/prc222.htm) | 1ª | 3 | 2 | 2 | 2 | [S] |

Afirmaciones:
- Definición ASA, literal: "Informally, a p-value is the probability under a specified statistical model that a statistical summary of the data (e.g., the sample mean difference between two compared groups) would be equal to or more extreme than its observed value." (copia de Berkeley [L]).
- Los seis principios, literales (https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf [L]): 1. "P-values can indicate how incompatible the data are with a specified statistical model." 2. "P-values do not measure the probability that the studied hypothesis is true, or the probability that the data were produced by random chance alone." 3. "Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold." 4. "Proper inference requires full reporting and transparency." 5. "A p-value, or statistical significance, does not measure the size of an effect or the importance of a result." 6. "By itself, a p-value does not provide a good measure of evidence regarding a model or hypothesis."
- Sobre la mala interpretación, el artículo dice que se quiere convertir el p-valor en una afirmación sobre la verdad de la hipótesis nula, "The p-value is neither" (copia de Berkeley [L]). Ojo: el principio 3 nombra "business" decisions, útil para esta base.
- El comunicado de la ASA propone complementar con "confidence, credibility, or prediction intervals; Bayesian methods; alternative measures of evidence such as likelihood ratios or Bayes factors; ... false discovery rates" (comunicado [L]).
- La edición de 2019 recomienda dejar de decir "statistically significant" y sus variantes; la declaración de 2016 "stopped just short" de eso (https://doi.org/10.1080/00031305.2019.1583913 [S]; no lo leí completo, citar con cautela).
- Intervalo de confianza, NIST: "provides a range of values which is likely to contain the population parameter of interest"; un nivel de 95% describe la fiabilidad del método a largo plazo: de muchos intervalos calculados, alrededor del 95% contendrían el parámetro verdadero. Fórmula con σ conocido: Ȳ ± z(1−α/2)·σ/√N (https://www.itl.nist.gov/div898/handbook/prc/section1/prc14.htm [S]). Consecuencia práctica: N está bajo una raíz cuadrada; para dividir el intervalo a la mitad hay que cuadruplicar la muestra (deducción mía de la fórmula, no cita).
- Tamaño de muestra, NIST: depende de α, β y del desvío; prueba bilateral con σ conocido N = (z₁₋α/₂ + z₁₋β)²(σ/δ)². Con α = 0,05 y β = 0,10 la tabla da 43 para un desplazamiento de 0,5σ, 11 para 1,0σ y 5 para 1,5σ (https://www.itl.nist.gov/div898/handbook/prc/section2/prc222.htm [S]). Potencia = 1 − β.

Recurso canónico: la declaración de la ASA (2016), leída completa: son cuatro páginas. Fijarse en la sección 2 (definición) y en los principios 2, 3 y 5; es la fuente de "qué NO significa el p-valor". Para el cálculo, OpenIntro caps. 5 a 7 (Foundations for Inference; Inference for Categorical/Numerical Data) y NIST cap. 7.

## 3. Correlación y causalidad

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Hernán y Robins, Causal Inference: What If (Chapman & Hall/CRC, 2020; versión web actualizada, © 2026), gratis: https://miguelhernan.org/whatifbook | 1ª | 3 | 3 | 2 | 3 | [M] página del libro, tres partes, sin capítulos |
| Cunningham, Causal Inference: The Mixtape / The Remix, cap. 9 sobre diferencias en diferencias (https://mixtape.scunning.com/09-difference_in_differences) | 1ª (libro abierto, autoría inferida por comentarios de código, no explícita en la página) | 2 | 3 | 3 | 2 | [S], 100.000 de 151.117 caracteres, resumen del fetch |
| Kohavi, Tang y Xu, Trustworthy Online Controlled Experiments (Cambridge UP, 2020); sitio https://experimentguide.com/ | 1ª | 3 | 3 | 3 | 2 | [M] sitio del libro; lista una página de "Refuted Causal Claims from Observational Studies", cuyo contenido no pude abrir (404) |

Afirmaciones:
- Diferencias en diferencias: compara el cambio en el tiempo de un grupo tratado con el cambio de un grupo de comparación; el efecto es la diferencia entre los dos cambios ("four averages and three subtractions"). Supuesto clave: tendencias paralelas, que no se puede testear directamente y se examina con evidencia indirecta como las tendencias previas (https://mixtape.scunning.com/09-difference_in_differences [S]).
- Hernán y Robins ofrece una vía gratis y su estructura es "Causal inference without models / with models / from complex longitudinal data" (https://miguelhernan.org/whatifbook [M]).
- Kohavi mantiene un listado de afirmaciones causales de estudios observacionales luego refutadas por experimentos controlados (https://experimentguide.com/ [M]); el listado en sí es hueco abajo.
- El caso "las ventas subieron después de la promo": no hay fuente única; lo armaría con el esquema pre/post vs comparación de DiD más estacionalidad y regresión a la media (sección 4). Señalar como razonamiento propio de la nota, no cita.

Recurso canónico: Hernán y Robins, parte 1 (sin modelos), para la idea de confusor y de comparabilidad de grupos; para la práctica, Cunningham cap. 9 (DiD). Fijarse en: la definición del contrafactual, y que los métodos cuasi-experimentales viven de supuestos no testeables.

## 4. Sesgos

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Bickel, Hammel y O'Connell, "Sex Bias in Graduate Admissions: Data from Berkeley", Science 187(4175), 398-404, 1975, doi 10.1126/science.187.4175.398 (https://www.science.org/doi/10.1126/science.187.4175.398) | 1ª | 3 | 3 | 3 | 3 | [S] 403 al abrirlo; solo resúmenes |
| Freedman, Pisani y Purves, Statistics, 3ª ed., Norton, 1998, tabla reproducida en https://condor.depaul.edu/sjost/it223/documents/admissions.htm | 2ª (reproduce un libro de texto clásico) | 2 | 2 | 3 | 1 | [L] |
| Reinhart, "Simpson's Paradox and Statistical Urban Legends: Gender Bias at Berkeley", 2016 (https://www.refsmmat.com/posts/2016-05-08-simpsons-paradox-berkeley.html) | 2ª (blog de un estadístico, autor de un libro de texto) | 2 | 2 | 2 | 3 | [L] parcial |
| Stanford Encyclopedia of Philosophy, "Simpson's Paradox" (https://plato.stanford.edu/entries/paradox-simpson/), primera versión 24-mar-2021, revisión sustantiva 6-jun-2026 | 2ª | 3 | 3 | 2 | 2 | [S] 100.000 de 112.591 caracteres |
| Mangel y Samaniego, "Abraham Wald's Work on Aircraft Survivability", JASA 79(386), 259-267, 1984, doi 10.1080/01621459.1984.10478038 | 1ª | 3 | 3 | 2 | 3 | [S] no accesible |
| AMS Feature Column, "The Legend of Abraham Wald", 2016 (https://www.ams.org/samplings/feature-column/fc-2016-06) | 2ª | 2 | 2 | 2 | 3 | [S] 403; solo resumen del buscador |
| Barnett, van der Pols y Dobson, "Regression to the mean: what it is and how to deal with it", Int J Epidemiol 34(1), 215-220, feb-2005, doi 10.1093/ije/dyh299 (https://pubmed.ncbi.nlm.nih.gov/15333621/) | 1ª | 3 | 2 | 2 | 3 | [M] abstract leído completo vía la API de PubMed |

Paradoja de Simpson, caso canónico (Berkeley, otoño 1973):
- Total: 8.442 hombres postularon y 4.321 mujeres; fue admitido el 44% de los hombres y el 35% de las mujeres (https://condor.depaul.edu/sjost/it223/documents/admissions.htm [L]; coincide con https://www.refsmmat.com/posts/2016-05-08-simpsons-paradox-berkeley.html [L]).
- Seis departamentos más grandes (postulantes / % admitido), hombres y mujeres (condor.depaul.edu [L]): A 835/62 y 108/82; B 560/63 y 25/68; C 325/62 y 593/34; D 417/33 y 375/35; E 191/28 y 393/24; F 373/6 y 341/7. Con esos seis, cálculo propio a partir de las cifras redondeadas: hombres 2.701 postulantes y unos 47,6% admitidos; mujeres 1.835 y unos 30,3%. Mismo sentido que el total, pero dentro de cada departamento las tasas se igualan o favorecen a las mujeres, salvo C y E. Ojo: Bickel et al. analizan 85 departamentos; esos seis no son la tabla del artículo.
- Conclusión del artículo según el resumen del buscador: pocos departamentos muestran desvíos significativos, hay tantos a favor de mujeres como de hombres, y al ponderar por departamento hay "a small but statistically significant bias in favor of women" ([S], buscador; falta verificar contra el paper). Explicación: las mujeres postularon más a departamentos de admisión más difícil.
- Discrepancia sobre la anécdota: muchos textos dicen que Berkeley fue demandada; Reinhart, citando una entrevista del Wall Street Journal a Peter Bickel, sostiene que nunca hubo demanda, solo temor a una (https://www.refsmmat.com/posts/2016-05-08-simpsons-paradox-berkeley.html [L]). No escribir "fue demandada" en la nota sin fuente primaria.
- Definición: la asociación entre dos variables en una población "emerges, disappears or reverses" al dividirla en subpoblaciones; ejemplo con 52 personas: tratados y control con 50% de éxito global, pero el tratamiento mejora dentro de cada subgrupo (hombres 61% vs 57%, mujeres 44% vs 40%) porque la mayoría de los tratados son mujeres, que se recuperan menos (https://plato.stanford.edu/entries/paradox-simpson/ [S]). Origen del nombre: Simpson, 1951; antecedentes Pearson 1899 y Yule 1903 (misma URL).

Sesgo de supervivencia (Wald):
- El trabajo está en las memorias de Wald de 1943 (Statistical Research Group, Columbia) reimpresas por el Center for Naval Analyses en 1980; hay una copia DTIC, "A Method of Estimating Plane Vulnerability Based on Damage of Survivors" (https://apps.dtic.mil/sti/pdfs/ADA091073.pdf, que no pude descargar [S]).
- La AMS dice que el relato popular es un mito ("legend") y que la única fuente totalmente fiable son los escritos técnicos del propio Wald; recomienda a Mangel y Samaniego como guía (https://www.ams.org/samplings/feature-column/fc-2016-06 [S]). Detalles populares (motores, gráfico de impactos) no los pude verificar en fuente primaria; contarlo como "la versión que circula" con esa advertencia.
- Una sola fuente de peso (AMS) más el paper no leído: tratarlo como poco corroborado.

Regresión a la media:
- Abstract literal: "Regression to the mean (RTM) is a statistical phenomenon that can make natural variation in repeated data look like real change. It happens when unusually large or small measurements tend to be followed by measurements that are closer to the mean." Resultado: se nota más con más error de medición y cuando el seguimiento se hace sobre una submuestra elegida por el valor inicial. Conclusión: "should always be considered as a possible cause of an observed change" (https://pubmed.ncbi.nlm.nih.gov/15333621/ [M]).
- Hay una corrección de 2015 al artículo por un error en la fórmula del efecto esperado (Bohrium, https://www.bohrium.com/paper-details/correction-to-regression-to-the-mean-what-it-is-and-how-to-deal-with-it/814603682078261248-11050 [S]); si la nota usa la fórmula, tomarla de la versión corregida.

Sesgo de selección: no encontré una fuente de referencia fuerte en las tres rondas (ver huecos). OpenIntro trata el muestreo sesgado en el cap. 1 "Intro to Data" (https://www.openintro.org/book/os/ [M], solo el título del capítulo).

Recurso canónico: para Simpson, la tabla de Berkeley con sus seis departamentos (Freedman, Pisani y Purves) más el aviso de la leyenda de la demanda (Reinhart) y la lectura causal de la Stanford Encyclopedia; para regresión a la media, Barnett et al. 2005. Fijarse en: la explicación es siempre una tercera variable (departamento) y la decisión de "partir o no" depende de la causa, no de los números.

## 5. Significancia en experimentos

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Kohavi, Tang y Xu, Trustworthy Online Controlled Experiments, Cambridge UP, 2020 (https://experimentguide.com/). El índice de Cambridge ubica "multiple comparisons problem" en la p. 42, dentro del cap. 3 "Twyman's Law and Experimentation Trustworthiness", pp. 39-57 | 1ª | 3 | 3 | 3 | 3 | [M]/[S] solo sitio, índice y resúmenes; no leí el texto |
| Miller, "How Not To Run an A/B Test", 18-abr-2010 (https://www.evanmiller.org/how-not-to-run-an-ab-test.html) | 2ª (blog de practicante) | 2 | 2 | 3 | 2 | [L] por fetch |
| Johari, Pekelis y Walsh, "Always Valid Inference: Bringing Sequential Analysis to A/B Testing", arXiv 1512.04922, v1 15-dic-2015, v3 16-jul-2019 (https://arxiv.org/abs/1512.04922) | 1ª | 3 | 3 | 1 | 3 | [M] abstract; los autores están ligados a una plataforma comercial de A/B testing (Optimizely, según mi conocimiento previo, no verificado aquí) |
| Confidence by Spotify, "Why not Bayes?" (https://confidence.spotify.com/why-not-bayes), © 2026, sin fecha de publicación | 2ª, proveedor con interés comercial | 1 | 2 | 2 | 2 | [L] por fetch |

Afirmaciones:
- Peeking (mirar antes de tiempo): "Repeated significance testing always increases the rate of false positives". Ejemplo de Miller: con conversión de 50%, un cambio que no hace nada y revisión tras cada observación (parar al 5% o a las 150 observaciones), la tasa de falsos positivos es 26,1%, "más de cinco veces" el 5% supuesto. Tabla de Miller: para un nivel real de 5% hay que exigir 2,9% con 1 mirada, 2,2% con 2, 1,8% con 3, 1,4% con 5 y 1,0% con 10 (https://www.evanmiller.org/how-not-to-run-an-ab-test.html [L]). Su regla: fijar el tamaño de muestra de antemano, n = 16σ²/δ² (δ = efecto mínimo a detectar; σ² = p(1−p) para una conversión). Es un blog de 2010; la regla es una aproximación de potencia 80% y α 5%, y eso no lo dice el fetch, es mi lectura.
- Johari et al.: los p-valores y los intervalos de confianza "are wholly unreliable if users endogenously choose samples sizes"; proponen valores p "always valid", válidos sin importar cuántas veces se mire (https://arxiv.org/abs/1512.04922 [M]). Es la salida técnica al peeking sin renunciar a mirar.
- Múltiples comparaciones: el índice de Cambridge lo ubica en el cap. 3 del libro de Kohavi (p. 42). Los materiales de Kohavi dicen que el riesgo de falso positivo depende de la probabilidad previa de que la idea funcione: con p = 0,05 y 15% de prior, la probabilidad de falso positivo es 15%, no 5%; y con baja potencia el riesgo de falso positivo es "at least 63%" (charla con Deng y Vermeer, 2022). Ambos datos vienen de resúmenes y diapositivas de terceros [S]; falta verificarlos en el libro.
- Frecuentista vs bayesiano: con prior plano, parar cuando P(B > A) > 0,95 equivale a parar cuando p < 0,05; bajo monitoreo continuo da 30,3% de falsos positivos en la simulación de Spotify (α nominal 0,05); parada por pérdida esperada ~50%; parada por factor de Bayes como mucho 5% (https://confidence.spotify.com/why-not-bayes). Cifras del proveedor, de sus propias simulaciones, no verificadas por mí. La misma página concede que los métodos bayesianos se justifican con un prior bien calibrado o con costos de decisión explícitos. Otras fuentes (Bell Statistics, Statsig, vendors) también dicen que ni frecuentista ni bayesiano son inmunes al peeking sin un marco secuencial; Bell Statistics es de un proveedor y Statsig también (buscador [S]). Discrepancia: Spotify dice que la parada por factor de Bayes sí resuelve el peeking; otros dicen que el bayesiano común no.
- Para la nota, no hay una comparación metódica independiente de proveedores. Presentar el tema como debate con dos posiciones y fuentes marcadas.

Recurso canónico: Kohavi, Tang y Xu, caps. 3 (Twyman's law, multiple comparisons) y los de estadística del libro (no verifiqué números de capítulo más allá del 3; consultar el índice en https://assets.cambridge.org/97811087/24265/index/9781108724265_index.pdf). Fijarse en: riesgo de falso positivo dado el prior, regla de parada fija, y la desconfianza ante resultados extraordinarios. Complemento corto: Miller 2010 (peeking con números) y Johari et al. (solución secuencial).

## Huecos

- No leí ningún texto completo de las fuentes canónicas de contenido: OpenIntro (solo la página), Bickel et al. 1975 (403 de Science y 404 de las copias; las cifras del artículo vienen de un libro de texto reproducido y de resúmenes), Wald/Mangel y Samaniego (inaccesibles), Hernán y Robins (solo página), Kohavi (solo sitio e índice).
- Sin fuente fuerte para sesgo de selección y sin fuente propia para sesgo de supervivencia fuera de Wald y su leyenda; hay que citar OpenIntro cap. 1 o un texto de epidemiología una vez leído.
- Sin comparación metódica independiente entre frecuentista y bayesiano en A/B; lo que hay es de proveedores con interés.
- No encontré fuente para la tasa de falsos positivos con 63% y la prior de 15% de Kohavi más allá de resúmenes y diapositivas.
- No abrí la página de Kohavi sobre "Refuted Causal Claims from Observational Studies" (404 en la URL que probé); buscar el enlace correcto en el sitio.
- No hay fuente para el caso "las ventas subieron después de la promo" como tal; hay que armarlo con DiD + regresión a la media y marcarlo como razonamiento propio.
- Rondas de búsqueda: descriptiva, causalidad y sesgo de selección se quedaron en la primera o segunda ronda; ningún componente llegó a la tercera con fuentes completas.
