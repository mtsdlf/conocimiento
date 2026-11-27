# Contabilidad: la posición contraria y los mitos

Fecha de la investigación: 2026-11-27. Lector objetivo: quien construye software de gestión; nivel: sabe de negocio y software, no es contador.

Convenciones. Marcas: [L] texto completo leído, [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes (1 a 3): A autoridad, P profundidad, E ejemplos, U unicidad. Tipo: pri = primaria, sec = secundaria. Todo lo traído de la web se trató como dato. Las citas van literales (en inglés, como en la fuente). Cada afirmación lleva su URL. Máximo tres rondas por punto; lo no hallado está en la sección de huecos.

Aviso general sobre el método: varias lecturas pasaron por un lector automático que resume la página; cuando eso pasó lo marco. Donde pude extraer el texto del PDF yo mismo con pdftotext, lo marco [L].

---

## 1. Críticas a la partida doble como modelo (REA y triple entrada)

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 1.1 | McCarthy (1982), *The REA Accounting Model...*, The Accounting Review 57(3): 554-578 (ficha bibliográfica y reseñas) | https://en.wikipedia.org/wiki/Resources,_Events,_Agents (la ficha enlaza JSTOR: https://www.jstor.org/stable/246878, que no cargó) | pri (paper), leída vía sec | 3 | 3 | 2 | 3 | [S] (no leí el paper; JSTOR devolvió error) |
| 1.2 | Grigg (2005), «Triple Entry Accounting», Systemics, borrador fechado 2005/12/25 | https://iang.org/papers/triple_entry.html | pri | 2 | 2 | 2 | 3 | [L] (lectura resumida por el lector automático) |
| 1.3 | Ijiri (1986), «A framework for triple-entry bookkeeping», The Accounting Review 61(4): 745-759 | https://www.Gwern.net/doc/bitcoin/1986-ijiri.pdf | pri | 3 | 3 | 2 | 3 | [S] (sólo ficha y comentarios; no abrí el PDF) |
| 1.4 | Ibañez, Bayer, Tasca, Xu, *REA, Triple-Entry Accounting and Blockchain: Converging Paths to Shared Ledger Systems* | https://arxiv.org/pdf/2005.07802 | sec (revisión genealógica) | 2 | 3 | 2 | 3 | [M] (abstract leído con pdftotext; cuerpo no) |
| 1.5 | Vandenbossche y Wortmann, en *Proceedings of the 2nd International REA Technology Workshop*, sobre por qué los modelos de datos contables de investigación no están en los ERP | https://www.slideshare.net/slideshow/Proceedings/993485 | pri (workshop) | 1 | 2 | 1 | 3 | [S] |
| 1.6 | Polovina, REA aplicado a SAP HCM (estudio de caso) | https://ceur-ws.org/Vol-1040/paper4.pdf | pri (caso) | 1 | 2 | 2 | 2 | [S] |
| 1.7 | Nikitkov (2020), revisión de 55 artículos REA, JAMIS | https://online-cig.ase.ro/RePEc/ami/articles/19_3_6.pdf | sec | 2 | 3 | 1 | 2 | [S] |
| 1.8 | Wikipedia, «Momentum accounting and triple-entry bookkeeping» | https://en.wikipedia.org/wiki/Momentum_accounting_and_triple-entry_bookkeeping | sec | 1 | 1 | 1 | 1 | [S] |

Nota de independencia: 1.8 y los resúmenes del buscador sobre triple entrada parafrasean la misma literatura (Ijiri, Grigg, 1.4); cuentan como una sola línea secundaria.

### Afirmaciones

- McCarthy 1982 se publicó en The Accounting Review 57(3), julio de 1982, pp. 554-578. El abstract describe un marco para un entorno de datos compartidos «donde contadores y no contadores mantienen información sobre los mismos fenómenos»; su núcleo son conjuntos de recursos económicos, eventos económicos y agentes económicos y sus relaciones. https://en.wikipedia.org/wiki/Resources,_Events,_Agents ; https://synapsesocial.com/papers/W7136181339 (parafraseo del abstract; [S]).
- La AAA le dio en 1996 su primer premio Seminal Contribution to the Accounting Information Systems Literature. https://bps.broad.msu.edu/media/documents/5698309410edd59b5e1c1dc3.pdf ([S], vía buscador).
- Hay una monografía AAA de 2022, «The REA Accounting Model as an Accounting and Economic Ontology» (McCarthy, Geerts, Gal). https://msutoday.msu.edu/news/2026/03/william-mccarthy-accounting-hall-of-fame ([S]).
- Uso real de REA: la evidencia hallada apunta a adopción directa limitada. Vandenbossche y Wortmann sostienen que los ERP siguen tratando la partida doble como modelo de datos contable central y que los modelos contables de investigación no se adoptaron. https://www.slideshare.net/slideshow/Proceedings/993485 ([S]). Polovina reporta que REA agrega valor al modelar procesos en SAP y que no seguir la ontología REA puede hacer que los datos se pierdan o se guarden repetidos. https://ceur-ws.org/Vol-1040/paper4.pdf ([S]). Es evidencia de talleres y casos, de los años 2000; no hay encuesta de adopción (ver huecos).
- Grigg (2005): triple entrada = recibos firmados digitalmente combinados con partida doble; «3 local entries for each of 3 roles»; el recibo firmado es «more powerful than double entry records» como evidencia; sobre partida doble dice «it is a framework that breaks down as soon as the number of parties exceeds one». https://iang.org/papers/triple_entry.html
- Grigg es modesto sobre el uso: «We have operated this system on a small scale.» Lista auditoría y recibos perdidos como «issues for future research». https://iang.org/papers/triple_entry.html
- Hay dos cosas distintas con el mismo nombre. Ijiri (monografía de 1982, paper de 1986) propone una tercera entrada de «momentum» (la variación de la renta) que extiende la partida doble; Grigg lo redefine como recibo criptográfico compartido. Ijiri 1986: The Accounting Review 61(4), 745-759; el trabajo de 1986 se apoya en la monografía de 1982, que mostró que la partida doble «is not an absolute system defying extensions but is logically extendible to triple-entry». https://www.Gwern.net/doc/bitcoin/1986-ijiri.pdf ([S]); https://arxiv.org/pdf/2005.07802 para la distinción histórica ([M]).
- Cuánto se usa cada uno: no hallé cifras de adopción empresarial de ninguno. Una reseña de 60 artículos (2005-2024) citada por un resumen del buscador dice que el 87% de los académicos prefiere la versión tecnológica de Grigg y que la de Ijiri no ganó tracción; es [S] de una fuente que no pude ubicar con certeza, sólo como pista. https://rit.edu/croatia/sites/rit.edu.croatia/files/docs/2%20Schmidt%2C%20Vezjagi%C4%87.pdf
- Ibañez et al. afirman que REA influyó en líneas independientes de investigación de triple entrada y que ese hilo llega al blockchain; dicen también que «correct common misconceptions» sobre esa historia (la atribución popular a Grigg como inventor). https://arxiv.org/pdf/2005.07802 ([M]).

### Dónde le sirve a la base
- Registro / partida doble y Fundamentos: una caja «límites del modelo» para el desarrollador: REA es el modelo de datos que un ingeniero propondría (recursos, eventos, agentes), y los ERP igual guardan asientos de partida doble. Decirlo con cuidado: es lectura de pocas fuentes.
- Registro / asiento y libros: separar el evento económico (el pedido, la entrega) del asiento que lo resume.
- Control interno / conciliaciones: triple entrada de Grigg como idea de por qué las partes conciliarían menos si compartieran un registro firmado; hoy es una propuesta, no práctica.

---

## 2. *Relevance Lost* y la crítica a la contabilidad de costos; adopción de ABC

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 2.1 | Johnson y Kaplan (1987), *Relevance Lost: The Rise and Fall of Management Accounting*, Harvard Business School Press (fichas de catálogo, reseña en Business History Review) | https://libcat.library.tamu.edu/Record/in00000583263/Description ; https://econpapers.repec.org/RePEc:cup:buhirw:v:62:y:1988:i:01:p:176-178_05 | pri (libro), leído vía fichas | 3 | 3 | 3 | 3 | [M] |
| 2.2 | Quinn, Elafi y Mulgrew (2017), «Reasons for not changing to activity-based costing: a survey of Irish firms», PSU Research Review 1(1): 63-70 | https://www.emerald.com/insight/content/doi/10.1108/prr-12-2016-0017/full/html | pri (encuesta) | 2 | 2 | 2 | 3 | [L] (lectura resumida por el lector automático) |
| 2.3 | Byrne, Stower y Torry (2009), JAMAR, estudio australiano que resume encuestas previas | https://research.usq.edu.au/download/34b0423e7ec72de2f77f6d732ba7ffadbe727eeec69e2c23fe5683ec2182a8b6/76722/Byrne_Stower_Torry_JAMAR_2009_PV.pdf | pri/sec | 2 | 2 | 2 | 2 | [S] |
| 2.4 | Askarany y Yazdifar (2012), Int. J. Production Economics 135(1): 430-439 | https://econpapers.repec.org/RePEc:eee:proeco:v:135:y:2012:i:1:p:430-439 | pri | 2 | 2 | 1 | 2 | [S] |
| 2.5 | Kaplan y Anderson (2004), «Time-Driven Activity-Based Costing», Harvard Business Review (nov. 2004) | https://papers.ssrn.com/abstract=485443 ; resumen HBS: https://www.library.hbs.edu/working-knowledge/adding-time-to-activity-based-costing | pri (de los defensores de ABC) | 2 | 2 | 2 | 2 | [S] |

Los resultados de 2.3 y 2.2 citan las mismas encuestas anteriores (p. ej. 20,3% en Nueva Zelanda, 18% en EE.UU.); tratar 2.3 como una sola línea con las que cita.

### Afirmaciones

- *Relevance Lost*: Harvard Business School Press, 1987; xiii + 269 pp.; ISBN 0875841384. https://libcat.library.tamu.edu/Record/in00000583263/Description ([M]).
- Tesis, según un resumen: casi todo lo significativo de la contabilidad gerencial estadounidense ya se conocía hacia 1925 y seis décadas después había perdido relevancia; es una crítica a cómo se enseñaba, investigaba y usaba. https://econpapers.repec.org/RePEc:cup:buhirw:v:62:y:1988:i:01:p:176-178_05 ([S]; no leí el libro). Una nota de discrepancia: la formulación «todo se sabía en 1925» es la del resumen del buscador; verificar contra el texto antes de usarla como cita.
- Johnson y Kaplan se separaron después: Kaplan desarrolló el Balanced Scorecard (con Norton); Johnson pasó a criticar la gestión por mediciones. https://libcat.library.tamu.edu/Record/in00000583263/Description ([S], resumen del buscador).
- Adopción de ABC, Irlanda: 18,7% (32 de 171 empresas; muestra de 821 empresas medianas y grandes, 20,75% de respuesta). Costeo directo 41,5%; costeo tradicional 33,9%. Razón principal para no adoptarlo: satisfechos con el método actual (20,6% en la tabla de razones; 84,6% de acuerdo con «satisfied with the current method» en otra tabla). El artículo se publicó el 13/4/2017; no dice el año de la encuesta; el texto dice «just under 94 per cent» y no coincide con la tabla. https://www.emerald.com/insight/content/doi/10.1108/prr-12-2016-0017/full/html
- Comparaciones: el estudio irlandés cita 11,8% (Clarke et al., 1999). https://www.emerald.com/insight/content/doi/10.1108/prr-12-2016-0017/full/html . El estudio australiano (Byrne et al., 2009) cita 20,3% en una encuesta neozelandesa a contadores y 18% en una encuesta estadounidense, y que hay «some evidence that worldwide adoption rates for ABC have peaked at around 20%». https://research.usq.edu.au/download/34b0423e7ec72de2f77f6d732ba7ffadbe727eeec69e2c23fe5683ec2182a8b6/76722/Byrne_Stower_Torry_JAMAR_2009_PV.pdf ([S]).
- Askarany y Yazdifar (2012) comparan tasas de ABC de Australia, Nueva Zelanda y Reino Unido con una encuesta a más de 2.000 miembros de CIMA; concluyen que la tasa reportada depende de cómo se mida la difusión. https://econpapers.repec.org/RePEc:eee:proeco:v:135:y:2012:i:1:p:430-439 ([S]).
- Kaplan y Anderson (2004): muchas empresas dejaron ABC porque «did not capture the complexity of their operations, took too long to implement, and was too expensive to build and maintain»; proponen el ABC basado en tiempo con dos parámetros (costo unitario de la capacidad y tiempo por actividad). Es la defensa de los propios autores, con casos de sus clientes. https://www.library.hbs.edu/working-knowledge/adding-time-to-activity-based-costing ([S]). Discrepancia: una tesis de Oklahoma State (2009) señala que TDABC no simplifica la etapa 2 de asignación. https://shareok.org/bitstream/handle/11244/7139/School%20of%20Accounting_06.pdf?sequence=1 ([S]).

### Dónde le sirve a la base
- Contabilidad de gestión / costos y costeo: sección «por qué el costeo tradicional distorsiona» (la crítica de 1987) y «qué se hace de verdad»: pocas empresas usan ABC completo (cifras alrededor del 20%, de países y años distintos, no extrapolar a Argentina).
- Costo de lo vendido (Operaciones): aviso de que prorratear gastos indirectos por una base única distorsiona el margen por producto; en software, es un argumento para guardar el driver de cada gasto.

---

## 3. Presupuesto anual: Beyond Budgeting y la evidencia

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 3.1 | Libby y Lindsay (2010), «Beyond budgeting or budgeting reconsidered? A survey of North-American budgeting practice», Management Accounting Research 21(1): 56-75. DOI 10.1016/j.mar.2009.10.003 | https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/8/36875/files/2016/12/Libby-Lindsay_budgeting_survey-17bvsph.pdf | pri (encuesta) | 3 | 3 | 2 | 3 | [M]: abstract y metodología leídos con pdftotext; no leí el cuerpo completo |
| 3.2 | Hope y Fraser, crítica del presupuesto (Beyond Budgeting) vía resumen HBS | https://www.library.hbs.edu/working-knowledge/why-budgeting-kills-your-company | pri/sec | 2 | 1 | 2 | 2 | [S] |
| 3.3 | Tesis/paper de Oxford (ORA) que cita a Becker (2014) y Libby y Lindsay | https://ora.ox.ac.uk/objects/uuid:35c45299-832b-4602-95c1-c12e659a8868/files/rfj236339p | sec | 2 | 2 | 1 | 2 | [S] |
| 3.4 | Tesis de Aalborg sobre el presupuesto | https://projekter.aau.dk/projekter/files/281135355/20133268.pdf | sec | 1 | 1 | 1 | 1 | [S] |
| 3.5 | ACCA, artículo técnico «Beyond budgeting» | https://www.accaglobal.com/gb/en/student/exam-support-resources/professional-exams-study-resources/p5/technical-articles/beyond-budgeting.html | sec (didáctica) | 2 | 1 | 1 | 1 | [S] |

### Afirmaciones

- Libby y Lindsay, abstract literal: «Overall, we find for the majority of firms that budgets continue to be used for control purposes and are perceived to be value-added. While problems exist with budgets, organizations are adapting their use to account for these problems rather than abandoning budgets altogether.» https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/8/36875/files/2016/12/Libby-Lindsay_budgeting_survey-17bvsph.pdf
- Método (leído en el PDF): dos encuestas a organizaciones medianas y grandes de Norteamérica; en una, la tasa de respuesta fue 13,6%; en la otra, de miembros de IMA, 1,5% (212 respuestas); cargos más frecuentes: Controller 44,6% y CFO 26,6%; 21% dijo que no usaba el presupuesto (la frase está cortada en la extracción; verificar el contexto antes de citarla). Los cuatro reproches que se ponen a prueba: tiempo de preparación, adaptabilidad, desconexión con la estrategia y contratos de desempeño fijos. https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/8/36875/files/2016/12/Libby-Lindsay_budgeting_survey-17bvsph.pdf
- Los números exactos de uso del presupuesto anual y de abandono no los pude confirmar del cuerpo; lo que dicen trabajos posteriores (estudios posteriores lo leen como que la mayoría sigue con presupuesto anual y pocos planean abandonarlo) es [S]. https://ora.ox.ac.uk/objects/uuid:35c45299-832b-4602-95c1-c12e659a8868/files/rfj236339p
- La crítica de Hope y Fraser: depender demasiado del presupuesto «acordado» afecta el comportamiento gerencial; la mayoría de los presupuestos no se basan en un modelo causal del consumo de recursos sino en negociaciones internas prolongadas. Su alternativa: metas basadas en benchmarks y contratos de mejora relativa a dos o tres años. https://www.library.hbs.edu/working-knowledge/why-budgeting-kills-your-company ([S]; es la posición de los proponentes, sin prueba independiente en lo que leí).
- Discrepancia: el trabajo de Oxford sostiene que incluso organizaciones que eliminaron el presupuesto anual parecen haberlo restablecido (Becker, 2014), y que la persistencia del presupuesto «bulwarks talk of its abandonment» (Hope y Fraser 2003a; Libby y Lindsay 2010). https://ora.ox.ac.uk/objects/uuid:35c45299-832b-4602-95c1-c12e659a8868/files/rfj236339p ([S]).
- Trabajos posteriores: un estudio IMA modelado sobre Libby y Lindsay (720 respuestas, empresas con fines de lucro) y un trabajo de 2024 que se presenta como actualización a más de una década. Ver las citas en el buscador: https://www.imanet.org/-/media/c72ba62b78e5476caa06d2cc2ddc40c0.ashx ; https://researchonline.lse.ac.uk/id/eprint/125940/1/Bhimani_et_al_2024_accepted.pdf ([S], no abiertos).

### Dónde le sirve a la base
- Contabilidad de gestión / presupuesto: contraposición honesta: el presupuesto anual tiene críticas serias (gaming, rigidez) pero la evidencia dice que se adapta (forecasts rodantes, usos más flexibles) más que se abandona. Para software: soportar versiones, forecasts rodantes y comparación contra presupuesto sin atar a un único ciclo anual.

---

## 4. Límites de la información contable

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 4.1 | Laux y Leuz (2009), «Did Fair-Value Accounting Contribute to the Financial Crisis?», NBER WP 15515 | https://www.nber.org/papers/w15515 | pri | 3 | 3 | 2 | 3 | [M] (abstract leído) |
| 4.2 | Laux y Leuz (2010), «The crisis of fair-value accounting: Making sense of the recent debate», AOS | ver el resumen en https://www.ecgi.global/sites/default/files/working_papers/documents/SSRN-id1487905.pdf (la versión de trabajo) | pri | 3 | 3 | 2 | 2 | [S] |
| 4.3 | Lev y Gu (2016), *The End of Accounting and the Path Forward for Investors and Managers*, Wiley | https://www.stern.nyu.edu/experience-stern/faculty-research/baruch-lev-book-end-of-accounting | pri (libro) | 3 | 3 | 2 | 3 | [M] (ficha de editor) |
| 4.4 | Reseñas y réplicas sobre Lev y Gu: CFA Institute, Fortune, trabajos sobre la relevancia valorativa | https://blogs.cfainstitute.org/blog/2018/02/01/the-end-of-accounting-not-so-sure/ ; https://fortune.com/2016/09/22/accounting-broken-baruch-lev/ | sec | 2 | 2 | 2 | 2 | [S] |
| 4.5 | Ocean Tomo, Intangible Asset Market Value Study | https://oceantomo.com/insights/ocean-tomo-releases-intangible-asset-market-value-study-interim-results-for-2020/ | pri de una consultora | 1 | 1 | 1 | 2 | [S] |
| 4.6 | Penman, valor y estados contables (reseñas y comentarios; el libro *Accounting for Value*, 2011) | https://blogs.cfainstitute.org/?p=26536 | sec | 2 | 2 | 1 | 2 | [S] |
| 4.7 | Barth (a favor del valor razonable), vía Stanford GSB | https://www.gsb.stanford.edu/index%2Ephp/insights/case-fair-value-accounting | sec | 2 | 1 | 1 | 2 | [S] |

### Afirmaciones

- Valor razonable y crisis, Laux y Leuz (NBER, noviembre 2009), literal: «it is unlikely that fair-value accounting added to the severity of the current financial crisis in a major way»; «While there may have been downward spirals or asset-fire sales in certain markets, we find little evidence that these effects are the result of fair-value accounting»; «If anything, empirical evidence to date points in the opposite direction, that is, towards overvaluation of bank assets.» https://www.nber.org/papers/w15515
- La versión publicada en AOS (2010): la controversia nace en parte de la confusión sobre qué es nuevo en el valor razonable; hay preocupaciones legítimas sobre «marking to market» puro en crisis, y el costo histórico tampoco es el remedio. https://www.ecgi.global/sites/default/files/working_papers/documents/SSRN-id1487905.pdf ([S]; verificar que coincida con la versión publicada).
- Posición opuesta de la defensa de costo histórico: Penman sostiene que el valor razonable pone valores inciertos en el balance y puede alimentar la especulación (la burbuja punto com); Barth sostiene que el costo histórico sólo coincide por accidente con el valor subyacente de la empresa. https://blogs.cfainstitute.org/?p=26536 ; https://www.gsb.stanford.edu/index%2Ephp/insights/case-fair-value-accounting ([S] ambas). Le doy las dos posiciones; no hay consenso.
- Lev y Gu: según la ficha del editor, sus informes financieros «have become useless in capital market decisions» y el análisis de grandes muestras muestra que los documentos financieros han perdido relevancia para los inversores; proponen un «Value Creation Report». https://www.stern.nyu.edu/experience-stern/faculty-research/baruch-lev-book-end-of-accounting
- Cifras del libro, sólo de resúmenes: el poder explicativo de las ganancias sobre el valor de mercado habría pasado de 80-90% de R cuadrado en los años 1950 a 45-55% en los 2010. https://fortune.com/2016/09/22/accounting-broken-baruch-lev/ y un resumen del libro ([S]; sin la tabla original. NO citar como cifra del libro sin verificar).
- Réplicas: CFA Institute dice que la evidencia lleva a inferencias «perhaps premature»; Sadka, Sadka y Tseng sostienen que los estudios mal retratan la relación ganancias-retornos; un estudio asociado a Stanford halla que la relevancia valorativa aumentó entre 1962 y 2014 y que los R cuadrado de MCO la sobreestiman. https://blogs.cfainstitute.org/blog/2018/02/01/the-end-of-accounting-not-so-sure/ ([S]). Dos fuentes que discrepan: Lev y Gu (pérdida de relevancia) contra esas réplicas (no se perdió, o se midió mal).
- Intangibles: Ocean Tomo calcula el valor intangible como capitalización menos valor tangible neto; en el S&P 500 sería 17% en 1975, 68% en 1995, 84% en 2015, alrededor del 90% en 2020-2025. https://oceantomo.com/insights/ocean-tomo-releases-intangible-asset-market-value-study-interim-results-for-2020/ ; https://oceantomo.com/?p=15611 ([S]). Es un residuo (todo lo que no es activo tangible neto), no una medición de intangibles, y la fuente es una consultora que vende servicios de propiedad intelectual: autoridad baja.

### Dónde le sirve a la base
- Estados contables / balance y normas: aclarar que el balance sigue reglas de reconocimiento (costo, valor razonable en algunos instrumentos) y que gran parte del valor de una empresa de software (código, marca, clientes, datos propios) no figura. Para quien vende gestión: el balance no es una tasación.
- Fundamentos: la contabilidad como lenguaje convencional con límites; debate costo histórico frente a valor razonable con las dos posiciones.

---

## 5. Mitos y confusiones frecuentes de no contadores

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 5.1 | AccountingCoach, «Debits and credits: additional explanations» | https://accountingcoach.com/debits-and-credits-additional-explanations/explanation | sec (didáctica) | 2 | 2 | 2 | 2 | [L] (lector automático) |
| 5.2 | BlackLine, glosario «Debits & Credits» | https://www.blackline.com/resources/glossaries/debits-and-credits/ | sec | 1 | 1 | 2 | 1 | [S] |
| 5.3 | W. Patrick Brady, apunte docente (Univ. de Illinois) | https://publish.illinois.edu/jennifer-johnson/debits-and-credits-first-thing/ | sec (docente) | 2 | 1 | 1 | 2 | [S] |
| 5.4 | UCT Graduate School of Business, «Four basic accounting misconceptions» | https://www.howwemadeitinafrica.com/four-basic-accounting-misconceptions-holding-business-back/57612/ | sec | 2 | 1 | 1 | 2 | [S] |
| 5.5 | OpenStax, *Principles of Financial Accounting*, cap. 11.3 (depreciación) | https://openstax.org/books/principles-financial-accounting/pages/11-3-explain-and-apply-depreciation-methods-to-allocate-capitalized-costs | pri (libro de texto abierto) | 3 | 2 | 2 | 2 | [L] (lector automático) |
| 5.6 | Yale, «Teaching the Cash Flow Statement Concepts» (material docente) | https://learning-accounting.yale.edu/sites/default/files/files/For-profit/Documents/20190912-Teaching-the-Cash-Flow-Statement-Concepts.pdf | sec | 2 | 2 | 2 | 2 | [S] |
| 5.7 | AccountingCoach, «Net cash flow vs net income» | https://www.accountingcoach.com/blog/net-cash-flow-net-income | sec | 2 | 1 | 2 | 1 | [S] |
| 5.8 | Washington State Auditor, manual BARS sobre conciliaciones bancarias | https://sao.wa.gov/bars-annual-filing/bars-gaap-manual/accounting/accounting-principles-and-internal-control/bank-reconciliations | pri (manual de un organismo de control) | 2 | 2 | 2 | 2 | [S] |
| 5.9 | UNC School of Government, «The Bank Reconciliation: A Key Internal Control...» (Badgett, 2024) | https://canons.sog.unc.edu/2024/04/the-bank-reconciliation-a-key-internal-control-in-financial-management | sec | 2 | 2 | 2 | 2 | [S] |
| 5.10 | COSO, *Internal Control: Integrated Framework* (2013), vía copias alojadas en AAA | https://aaahq.org/node/35067 | pri | 3 | 3 | 1 | 3 | [S] |

### Mito 1: «débito es bueno, crédito es malo» (o débito = disminuye, crédito = aumenta)
- AccountingCoach: «Debit means left side» y «Do not think of debit as good, bad, or anything else»; lo mismo para crédito. https://accountingcoach.com/debits-and-credits-additional-explanations/explanation
- BlackLine nombra la confusión: «It is a common misconception to equate debits with decreases and credits with increases. The actual effect of a debit or credit depends entirely on the type of account being modified.» Un débito a una cuenta de gasto la aumenta. https://www.blackline.com/resources/glossaries/debits-and-credits/ ([S])
- Brady (docente): muchos estudiantes de habla inglesa traen la idea de que crédito es positivo y débito negativo, y «they are right...half of the time». https://publish.illinois.edu/jennifer-johnson/debits-and-credits-first-thing/ ([S])
- UCT lista «a debit is a bad thing» como concepción errónea. https://www.howwemadeitinafrica.com/four-basic-accounting-misconceptions-holding-business-back/57612/ ([S])
- Para software: no mostrar «débito/crédito» al usuario final sin traducir al efecto según la naturaleza de la cuenta (y el idioma banco-cliente: para el banco, el depósito del cliente es un crédito, lo contrario de lo que ve el cliente en su cuenta; ese punto no lo verifiqué, queda como hipótesis).

### Mito 2: «ganancia = caja»
- Material docente: los estudiantes confunden resultado neto con flujo de efectivo operativo; «net income and cash flow from operations are seldom the same number» (cita del curso de finanzas y contabilidad, vía lynda.com). https://www.lynda.com/Finance-Accounting-tutorials/Accrual-accounting/565365/637007-4.html ([S]). Mecánica: una venta de diciembre sube la ganancia en diciembre y la caja en enero. https://www.accountingcoach.com/blog/net-cash-flow-net-income ([S])
- Un estudio en American Journal of Business Education: los estudiantes entienden mejor la base caja si primero ven la base devengado y luego ajustan. https://core.ac.uk/download/268108926.pdf ([S])
- OpenStax (Principles of Finance): el momento de los flujos de caja difiere del de registrar ingresos y gastos. Es de otro libro del mismo proyecto. [S], vía buscador: https://openstax.org/books/principles-finance/pages/4-4-when-should-a-company-capitalize-or-expense-an-item
- Que una empresa rentable se quede sin caja: sólo hallé un artículo general (https://www.lawtimesnews.com/news/general/accounting-misconceptions/259162 [S]); no hay fuente fuerte. Hueco.

### Mito 3: «la amortización es plata que se guarda»
- OpenStax: la depreciación «is based on the allocation of the cost of owning the asset over the period of its useful life»; valor en libros es «the amount of the asset that has not been allocated to expense through depreciation»; no se basa en cambios de valor de mercado. https://openstax.org/books/principles-financial-accounting/pages/11-3-explain-and-apply-depreciation-methods-to-allocate-capitalized-costs [L por lector automático]. El pasaje leído no dice nada sobre que la depreciación no aparta efectivo: ese vacío lo cubre el hecho de que es un asiento de ajuste con la cuenta de depreciación acumulada. Nadie en lo hallado nombra el mito con esas palabras; fuente que lo nombra: hueco.
- Que la depreciación no es una salida de caja pero sí un ajuste que se suma de vuelta en el flujo de efectivo indirecto: https://openstax.org/books/principles-finance/pages/5-key-terms ([S]).

### Mito 4: «el balance dice cuánto vale la empresa»
- Base: el valor en libros es costo no asignado (OpenStax arriba). Penman: el valor puede leerse en balance y en estado de resultados, y el valor en libros es un ancla del modelo de resultado residual, no una tasación. https://blogs.cfainstitute.org/?p=26536 ([S]).
- Fuente que nombre el mito con estas palabras para no contadores: no la hallé (el buscador devolvió «not found»). Hueco. Se apoya en los puntos 4 (intangibles, 90% del S&P 500 según Ocean Tomo) y en Lev y Gu.

### Mito 5: «el control interno evita el fraude»
- COSO: el control interno da «reasonable but not absolute assurance»; limitaciones nombradas: colusión y elusión por la dirección (management override). https://aaahq.org/node/35067 ([S]; verificar contra el marco 2013).
- ACFE 2024, datos de la sección 6: los controles correlacionan con pérdidas menores y detección más rápida, y aun así «override of existing internal controls» fue la segunda debilidad más citada (19%). https://anchin.com/wp-content/uploads/2024/08/2024-ACFE-Occupational-Fraud-Report.pdf

### Mito 6: «la conciliación bancaria es para encontrar errores del banco»
- Los manuales la presentan como control: «to safeguard cash against fraud and losses, and to ensure the accuracy of accounting records»; la mayoría de las partidas conciliatorias son de tiempo (depósitos en tránsito, cheques pendientes) o movimientos del banco no registrados (intereses, comisiones, cheques sin fondos); los errores propios se corrigen en los libros, los del banco se reclaman al banco. https://canons.sog.unc.edu/2024/04/the-bank-reconciliation-a-key-internal-control-in-financial-management ; https://sao.wa.gov/bars-annual-filing/bars-gaap-manual/accounting/accounting-principles-and-internal-control/bank-reconciliations ([S] ambas, vía buscador).
- Nadie nombra el mito como tal; lo inferido: el propósito dominante es detectar errores y fraude propios. ACFE 2024: la conciliación de cuentas detectó el 5% de los casos. https://anchin.com/wp-content/uploads/2024/08/2024-ACFE-Occupational-Fraud-Report.pdf

### Dónde le sirve a la base
- Fundamentos y Registro: sección «malentendidos habituales» con estos seis, en lenguaje llano (rutas: partida doble, devengado, activos fijos y amortización, balance, control interno, conciliaciones).
- Estados contables / flujo de efectivo: ejemplo de empresa rentable y sin caja (ver hueco: buscar un caso documentado).
- Para quien vende o implementa: los clientes preguntan por «plata guardada para reponer» (amortización) y por «cuánto vale» (balance); respuestas cortas.

---

## 6. Cuánto fallan los controles y cuánto detecta la auditoría externa (ACFE 2024)

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 6.1 | ACFE, *Occupational Fraud 2024: A Report to the Nations* (a través del resumen de Anchin, CPA) | https://anchin.com/wp-content/uploads/2024/08/2024-ACFE-Occupational-Fraud-Report.pdf | sec (resumen profesional del informe; el informe original es primario) | 2 | 2 | 2 | 1 | [L] del resumen (pdftotext propio); el informe completo de ACFE no lo leí (pesaba más de 10 MB y falló la descarga) |
| 6.2 | ACFE, informe completo (copia en Ivey) | https://www.ivey.uwo.ca/media/kjljj5cy/2024-report-to-the-nations.pdf | pri | 3 | 3 | 3 | 3 | no leído (límite de tamaño) |
| 6.3 | CAQ, «Fighting fraud: a shared responsibility» | https://www.thecaq.org/aia-fighting-fraud-a-shared-responsibility | sec (asociación de auditores; con interés) | 2 | 2 | 1 | 2 | [L] (lector automático) |

### Afirmaciones (del resumen de Anchin, que reporta el informe ACFE 2024)
- Muestra: 1.921 casos reales de fraude ocupacional, enero de 2022 en adelante; pérdida mediana de $145,000; 22% de los casos con pérdidas de $1 millón o más; pérdidas totales identificadas por encima de $3.1 billion; duración mediana del esquema, 12 meses; una organización típica pierde 5% de sus ingresos al año. https://anchin.com/wp-content/uploads/2024/08/2024-ACFE-Occupational-Fraud-Report.pdf
- Detección, literal de la tabla: Tip 43%; Internal Audit 14%; Management Review 13%; Document Examination 6%; Account Reconciliation 5%; By Accident 5%; External Audit 3%; Automated Transaction/Data Monitoring 3%. https://anchin.com/wp-content/uploads/2024/08/2024-ACFE-Occupational-Fraud-Report.pdf
- «only 3% of cases were discovered by external audits». Y al mismo tiempo, las auditorías externas de estados financieros estaban presentes en el 84% de los casos (con pérdida mediana de $121,000 frente a $250,000 sin ellas; la columna se leyó en una tabla extraída y el contraste es de esa tabla); también había códigos de conducta (85%) y auditoría interna (80%). https://anchin.com/wp-content/uploads/2024/08/2024-ACFE-Occupational-Fraud-Report.pdf
- Debilidades: «The most cited organizational weakness was a lack of internal controls (32% of cases), while override of existing internal controls (19%) was found to be the second most common weakness.» https://anchin.com/wp-content/uploads/2024/08/2024-ACFE-Occupational-Fraud-Report.pdf
- Los controles de detección activa y los demás correlacionan con pérdidas menores y detección más rápida (reducción de la duración de entre 14% y 50%). https://anchin.com/wp-content/uploads/2024/08/2024-ACFE-Occupational-Fraud-Report.pdf
- Lectura del CAQ, con interés (los auditores): «External auditors detected fraud in 3% of the cases in the ACFE's study»; sostienen que refleja un sistema de controles que funciona, y que un porcentaje mucho mayor sugeriría que las empresas no toman medidas proactivas y en capas; del 3%, 58% se descubrió por procedimientos estándar de auditoría. https://www.thecaq.org/aia-fighting-fraud-a-shared-responsibility . Discrepancia entre lecturas: el mismo 3% se usa como crítica a la auditoría externa (por quien lo lee como falla) y como prueba de que los controles funcionan (CAQ). Hay que decir ambas; ACFE no pretende que la auditoría externa esté diseñada para detectar fraude ocupacional (no verificado en el texto; el informe completo no se leyó).
- Una fuente con fecha inconsistente: la página actual de ACFE ya muestra la edición 2026 (2.402 casos, 10.276 respuestas); las cifras de 2024 se citan con su edición. https://www.acfe.com/fraud-resources/report-to-the-nations

### Dónde le sirve a la base
- Control interno / auditoría y fraude: afirmar que la auditoría externa no es el mecanismo principal de detección (3%) y que lo es el aviso de alguien (43%); implica canales de denuncia en el diseño del sistema.
- Control interno / separación de funciones y autorizaciones: la elusión por parte de quien tiene autoridad (19%) y la falta de controles (32%) como argumento de diseño: registro de auditoría inalterable, aprobaciones que también alcancen a administradores.
- Control interno / conciliaciones: la conciliación detecta, pero poco (5%).

---

## Huecos

1. McCarthy 1982: no leí el paper (JSTOR falló); sólo ficha y reseñas. Falta el texto original y su crítica explícita a la partida doble (qué dice sobre ella, no sólo su definición).
2. Uso real de REA y de triple entrada: no hay encuesta de adopción; sólo casos y talleres. Mi conclusión de adopción limitada es inferencia de poca evidencia. Tampoco hay cifras de uso de blockchain contable en empresas.
3. Ijiri 1986 y Ibañez et al. 2020: sólo ficha y abstract; no leí el cuerpo.
4. *Relevance Lost*: no leí el libro; falta una fuente primaria sobre su argumento central, y cualquier cita textual del libro. La frase «todo se sabía en 1925» es de un resumen secundario.
5. ABC: no hallé encuestas recientes (después de 2017) ni de América Latina o Argentina; las cifras (11,8% a 20,3%) son de países y años distintos y sin año de la encuesta en el caso irlandés. No encontré Drury y Tayles ni Bjørnenak (la búsqueda devolvió resultados irrelevantes).
6. Presupuesto: no obtuve los números exactos de Libby y Lindsay (porcentaje que usa presupuesto anual, que planea abandonarlo, que usa rolling forecasts). Faltan Hope y Fraser primarios y estudios empíricos de Beyond Budgeting con resultados (Becker 2014 sólo citado). Evidencia causal sobre mejora de desempeño: no hallé.
7. Valor razonable: leí sólo el abstract de Laux y Leuz; no verifiqué la versión publicada en AOS ni los argumentos de Penman y Barth en su texto original (sólo reseñas).
8. Lev y Gu: cifras de R cuadrado de resúmenes; falta la tabla original y la fuente primaria para los datos sobre intangibles (Ocean Tomo es una consultora, residuo contable). Falta Corrado, Hulten y Sichel o equivalente académico sobre capitalización de intangibles.
9. Mitos: ninguna fuente nombra «el balance dice cuánto vale la empresa», «la amortización es plata que se guarda» ni «la conciliación es para errores del banco» con esas palabras; los tres se sostienen por inferencia a partir de textos que explican el concepto correcto. Falta literatura de educación contable sobre concepciones erróneas (p. ej. artículos de Issues in Accounting Education) y un ejemplo documentado de empresa rentable sin caja. La relación débito/crédito vista por el banco quedó sin verificar.
10. ACFE 2024: no leí el informe completo (más de 10 MB); trabajé con el resumen de Anchin. Faltan la mediana de pérdida de los casos detectados por auditoría externa y la tasa de auditorías externas que consideran el fraude parte de su objetivo (ISA 240 / AS 2401 sin consultar). Tampoco consulté el marco COSO original: copias en AAA, resúmenes.
11. Todo lo de Argentina quedó fuera por consigna; esta investigación es agnóstica.
12. Nota de método: gran parte de las lecturas pasó por un resumidor automático; las citas literales entre comillas provienen de él y deberían verificarse contra la página antes de publicar en la base.
