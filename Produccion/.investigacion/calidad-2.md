# Calidad (vertical de Producción): informe de la segunda ronda

Marcas: [L] texto leído; [M] metadatos o abstract; [S] resumen secundario o del buscador. Puntajes 1-3 en: autoridad / profundidad / ejemplos / unicidad.

Aviso de método. Las dos normas de dominio público (MIL-STD-105E y MIL-STD-1520C) se bajaron de everyspec.com como PDF escaneado con OCR. El OCR de 105E es muy ruidoso en el texto corrido: lo que va entre comillas está limpiado solo de espacios y de letras evidentes, y se marca "(OCR)". Los números de las tablas de 105E se leyeron mirando la imagen de la página, no el OCR. Conviene recotejar con el PDF antes de publicar una cita. iso.org (todas las páginas, incluido el visor OBP) devuelve 403 al bajarlo directo: lo de ISO sale del buscador o de las páginas espejo de ISO que sí abrieron.

## 0. Lo que cambia respecto de la primera ronda

1. ISO 9001:2026 ESTÁ PUBLICADA. Fecha y estado literales abajo (sección 1). El borrador del tema no puede decir "ISO 9001:2015 vigente": la 2015 sigue siendo la edición contra la que están certificadas las empresas hasta el 30 de septiembre de 2029, pero la edición vigente es la 2026.
2. ISO 2859-1:2026 existe, tercera edición, publicada en enero de 2026 [S, de la ficha de ISO vista por el buscador].
3. Se cerró con texto literal el muestreo de aceptación (MIL-STD-105E), las definiciones de reproceso, reparación, descarte y MRB (MIL-STD-1520C), y la trilogía de Juran (página del Juran Institute).
4. NO se cerró el texto literal de ISO 9001 (2015 ni 2026): sigue bloqueado y pago. Lo que hay es de segunda mano.
5. Corrección a la primera ronda: el apartado 6.3.1 de NIST ("What are Control Charts?") está en https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc31.htm (la URL de la primera ronda, section1/pmc31.htm, redirige a la portada). Ahí sí aparecen causas por azar y asignables, pero NO "comunes" ni "especiales".

## 1. Muestreo de aceptación

### Fuentes

| Fuente | Tipo | Marca | Puntaje |
|---|---|---|---|
| MIL-STD-105E, "Sampling procedures and tables for inspection by attributes", 10 May 1989 (supersede a 105D, 29 April 1963). Ficha https://everyspec.com/MIL-STD/MIL-STD-0100-0299/MIL-STD-105E_11675/ ; PDF https://everyspec.com/MIL-STD/MIL-STD-0100-0299/download.php?spec=MIL-STD-105E.011675.PDF | primaria (norma de dominio público, cancelada) | [L] (OCR; tablas vistas en imagen) | 3/3/3/2 |
| NIST/SEMATECH e-Handbook 6.2, https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc2.htm y 6.2.1 https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc21.htm | primaria | [L] por el lector (resumen de página) | 3/1/1/2 |
| ISO 2859-1:2026, https://www.iso.org/standard/2859-1 | primaria | 403 directo; datos del buscador, que cita la ficha de ISO [S] | 3/1/1/3 |
| The ANSI Blog, "ISO 2859-1:2026", https://blog.ansi.org/ansi/iso-2859-1-2026-aql-sampling/ | secundaria | 403; solo vía buscador [S] | 1/1/1/1 |
| EverySpec, avisos sobre la cancelación (notice 1, 1995), https://everyspec.com/MIL-STD/MIL-STD-0100-0299/MIL-STD-105E_NOTICE-1_11679/ | primaria (aviso) | [S] del buscador | 2/1/1/1 |

### Afirmaciones con cita

Estado de MIL-STD-105E. Está cancelada: EverySpec la lista como "Cancelled" y un aviso de 1995 dice que las compras futuras deben referirse a una norma no gubernamental, ANSI/ASQC Z1.4-1993 [S] (https://everyspec.com/MIL-STD/MIL-STD-0100-0299/MIL-STD-105E_11675/). Es el antecedente directo de ANSI/ASQ Z1.4 e ISO 2859-1: esa relación no está escrita en el propio 105E y no se pudo verificar con texto en esta ronda; solo el aviso de 1995 que menciona Z1.4 [S]. No presentarla como cita literal.

AQL (105E, 3.1, OCR limpiado): "Acceptable Quality Level (AQL). When a continuous series of lots is considered, the AQL is the quality level which, for the purposes of sampling inspection, is the limit of a satisfactory process average". Nota del mismo párrafo (OCR): el AQL "is a designated value of percent defective (or defects per hundred units) for which lots will be accepted most of the time by the sampling procedure being used", y "The AQL alone does not identify the chances of accepting or rejecting individual lots or batches". Es decir: el AQL no es un porcentaje que se acepta de defectuosos ni un derecho del proveedor; 4.4.2: "The selection or use of an AQL shall not imply that the contractor has the right to supply any defective unit of product" (OCR). Fuente: https://everyspec.com/MIL-STD/MIL-STD-0100-0299/MIL-STD-105E_11675/ (PDF arriba).

Otras definiciones de 105E (OCR limpiado): 3.21 "The sample size code letter is a device used along with the AQL for locating a sampling plan on a table of sampling plans." 3.22 "A sampling plan indicates the number of units of product from each lot or batch which are to be inspected (sample size or series of sample sizes) and the criteria for determining the acceptability of the lot or batch (acceptance and rejection numbers)." 3.20: la muestra se elige "at random without regard to their quality". Defecto (3.7): "any nonconformance of the unit of product with specified requirements". Defectuoso (3.8): unidad con uno o más defectos. 4.4.3: el AQL puede darse por grupos de defectos (críticos, mayores, menores) y los valores de 10,0 o menos pueden expresarse en porcentaje defectuoso o en defectos por cien unidades.

Niveles de inspección (105E, 4.9.1, OCR): "Three inspection levels: I, II, and III, are given in Table I for general use. Normally, Inspection Level II is used. However, Inspection Level I may be used when less discrimination is needed, or Level III may be used for greater discrimination. Four additional special levels: S-1, S-2, S-3, and S-4, are given in the same table and may be used where relatively small sample sizes are necessary and large sampling risks can or must be tolerated." (idem fuente).

Inspección normal, rigurosa y reducida y reglas de cambio (105E, 4.6 y 4.7, OCR):
- 4.6: "Normal inspection will be used at the start of inspection." Normal, rigurosa o reducida sigue sin cambios hasta que las reglas de cambio lo exijan, y las reglas se aplican "to each class of defects or defective independently".
- 4.7.1, de normal a rigurosa: "tightened inspection shall be instituted when 2 out of 2, 3, 4, or 5 consecutive lots or batches have been rejected on original inspection (i.e., ignoring resubmitted lots or batches for this procedure)".
- 4.7.2, de rigurosa a normal: "normal inspection shall be instituted when 5 consecutive lots or batches have been considered acceptable on original inspection".
- 4.7.3, de normal a reducida, deben cumplirse todas: (a) "the preceding 10 lots or batches (or more, as indicated by the note to Table VIII) have been on normal inspection and all have been accepted on original inspection"; (b) el total de defectuosos en las muestras de esos lotes es igual o menor al número límite de la Tabla VIII; (c) "Production is at a steady rate"; (d) "Reduced inspection is considered desirable".
- 4.7.4, de reducida a normal, si ocurre cualquiera: un lote es rechazado; un lote queda en la zona intermedia entre aceptación y rechazo; "Production becomes irregular or delayed"; "Other conditions warrant that normal inspection shall be instituted".
- 4.8, suspensión: si el número acumulado de lotes no aceptados en una secuencia de lotes consecutivos bajo inspección rigurosa llega a cinco, se suspende el procedimiento de aceptación y no se reanuda hasta que se tome acción correctiva (OCR; 4.8 está parcialmente ilegible).
- Tabla VIII (números límite para reducida): NO leída (hueco menor).

Cómo se decide un lote (105E, 4.10.1.1, OCR): en el plan simple, "If the number of defectives found in the sample is equal to or less than the acceptance number, the lot or batch shall be considered acceptable. If the number of defectives is equal to or greater than the rejection number, the lot or batch shall be rejected."

Tipos de plan: simple (Tabla II), doble (III) y múltiple (IV), y "The average sample size of multiple plans is less than for double ... and both of these are always less than a single sample size" (4.9.4, OCR).

EJEMPLO LITERAL (lote, letra, muestra, aceptación, rechazo), leído de las imágenes de las tablas de 105E (no del OCR):
1. Tabla I, "Sample size code letters" (página 13 del documento, PDF p. 18): fila de tamaño de lote "1201 to 3200", niveles generales I = H, II = K, III = L.
2. Tabla II-A, "Single sampling plans for normal inspection (Master table)" (página 14, PDF p. 19): letra K, tamaño de muestra 125. Columna AQL 1,0: Ac 3, Re 4. En la misma fila: AQL 0,65 → 2 y 3; AQL 1,5 → 5 y 6; AQL 2,5 → 7 y 8. Letra L (muestra 200), AQL 1,0 → 5 y 6.
3. Lectura: un lote de 2000 unidades, nivel general II y AQL 1,0 % → letra código K → muestra de 125 unidades, al azar → se acepta el lote si hay 3 defectuosos o menos y se rechaza si hay 4 o más.
Cada celda con flecha (por ejemplo AQL 0,10 con letra K) remite a otra letra: la tabla dice (OCR) "Use first sampling plan below arrow. If sample size equals, or exceeds, lot or batch size, do 100 percent inspection" y "Use first sampling plan above arrow."

Qué NO dice NIST. La sección 6.2 (https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc2.htm) describe el muestreo de aceptación de lotes y lista "Choosing a Sampling Plan: MIL Standard 105D" (así, 105D, no 105E), pero el texto leído no menciona AQL, riesgo del productor ni del consumidor, ni da tabla. Definición de 6.2.1: "This process is called Lot Acceptance Sampling or just Acceptance Sampling." y "In general, the decision is either to accept or reject the lot." Fuente: https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc21.htm [S, resumen del lector]. NIST sirve para la teoría (curva característica, plan doble, múltiple, secuencial, skip-lot), no para la tabla.

ISO 2859-1:2026 (ficha de ISO vista por el buscador, https://www.iso.org/standard/2859-1) [S]: título "Sampling procedures for inspection by attributes — Part 1: Sampling schemes indexed by acceptance quality limit (AQL) for lot-by-lot inspection"; tercera edición, publicada en enero de 2026, reemplaza la de 1999 y su enmienda; estado "published" (el catálogo muestra el código de etapa 60.60); planes simples, dobles y múltiples; incluye por primera vez procedimientos opcionales de inspección por salteo de lotes (skip-lot); inspección normal, rigurosa, reducida y skip-lot en la cláusula 9, y las tablas en la cláusula 15; se usa junto con ISO 2859-0 para ejemplos. El texto y las tablas son de pago: no se leyeron.

Nota de terminología (verificada en 105E contra lo que dijo la primera ronda de 2859-1 [S]): 105E dice "AQL = Acceptable Quality Level"; la ficha de ISO 2859-1 dice "acceptance quality limit". El cambio de nombre es de ISO; no se pudo documentar con texto en esta ronda cuándo se hizo.

### Recurso canónico
Para la tabla y las reglas: MIL-STD-105E (abierta, aunque cancelada), partes 4.6 a 4.10 y tablas I, II-A, II-B y II-C. Para la norma vigente: ISO 2859-1:2026 (de pago). Fijarse en que el AQL es una propiedad de la serie de lotes y no de un lote, y en que las reglas de cambio son lo que hace presión sobre el proveedor.

### Qué registra un sistema
Plan de muestreo por producto o proveedor (nivel de inspección, AQL por clase de defecto, tipo de plan), estado de inspección vigente (normal, rigurosa, reducida) con el historial de los últimos lotes para poder aplicar las reglas de cambio, y por lote: tamaño del lote, letra código, tamaño de muestra, defectuosos encontrados, número de aceptación y de rechazo, decisión. Sin evidencia de un sistema abierto en esta ronda.

## 2. ISO 9001: estado de la edición y cláusulas 8.5.2, 8.6, 8.7 y 10.2

### Fuentes

| Fuente | Tipo | Marca | Puntaje |
|---|---|---|---|
| ISO, comunicado de prensa, 16 September 2026, https://committee.iso.org/files/live/sites/isoorg/files/news/News_archive/2026/09/MediaRelease_9001-2026-en.pdf | primaria | [L] | 3/2/1/3 |
| ISO/TC 176, "ISO 9001:2026 has been released!", https://committee.iso.org/sites/tc176/home/news/content-left-area/news-and-updates/news.html | primaria | [L] por el lector | 3/2/1/2 |
| ISO, ficha "ISO 9001:2026", https://www.iso.org/standard/9001 | primaria | 403 directo; datos del buscador [S] | 3/1/1/3 |
| NSAI (organismo nacional de Irlanda), presentación "Overview 9001:2015", https://www.nsai.ie/download/certification/Overview-9001-2015-presentation-23-Sep-15-Web-Compatibility-Mode.pdf | secundaria, de un organismo de normalización | [L] | 2/1/1/1 |
| ISO 9001:2015 texto, https://www.iso.org/standard/62085.html y OBP | primaria | 403: NO leída | |
| iso-9001-checklist.co.uk, isms.online, thecoresolution, certbetter y otros sobre 8.7 | secundarias | [S] | 1/1/1/1 (cuentan como una sola) |

### Estado de ISO 9001:2026 (cerrado)
- Comunicado de ISO: "Geneva, Switzerland, 16 September 2026 – Today, the International Organization for Standardization (ISO) announced the launch of ISO 9001:2026, Quality management systems – Requirements, the new edition of the world's leading quality management system standard." (https://committee.iso.org/files/live/sites/isoorg/files/news/News_archive/2026/09/MediaRelease_9001-2026-en.pdf)
- Comité ISO/TC 176: "ISO 9001:2026 was published on 16 September 2026!!" (entrada del 23 de septiembre de 2026). Transición (literal): "Accreditation bodies to be ready to assess ISO 9001:2026 no later than 31 March 2027"; "From 31 March 2028, new and initial accredited certifications may only be issued to ISO 9001:2026"; "Organisations already certified to ISO 9001:2015 will have until 30 September 2029 to complete their transition." (https://committee.iso.org/sites/tc176/home/news/content-left-area/news-and-updates/news.html, leído por el lector, no verificado en el HTML.)
- Estado según el buscador, citando la ficha de ISO: "Published", edición 6, fecha de publicación 2026-09 (https://www.iso.org/standard/9001) [S].
- Qué cambia (comunicado): "It places greater emphasis on leadership, a culture of quality and ethical behaviour, while providing greater clarity on the consideration of risks and opportunities", "A new section also helps users better understand the intent of the requirements", y "The standard also adopts the latest Harmonized Structure for ISO management system standards". Lo que la primera ronda tomó como borrador (FDIS) ya quedó superado.
- Qué NO se sabe: si cambió la numeración o el texto de 8.5.2, 8.6, 8.7 y 10.2 en la edición 2026. Ninguna fuente leída lo dice. Las notas de producción que citen cláusulas deben decir "ISO 9001:2015, y verificar la numeración en la 2026".

### Cláusulas de ISO 9001:2015: lo que hay (todo [S])
No se consiguió el texto de la norma. Esto es lo que dice un organismo de normalización nacional (NSAI, presentación de 23 sep. 2015, texto literal de la diapositiva, https://www.nsai.ie/download/certification/Overview-9001-2015-presentation-23-Sep-15-Web-Compatibility-Mode.pdf):
- 8.5.2: "Identification and traceability: No new requirements."
- 8.6: "Release of products and services: Replaces 'Monitoring and measurement of product'. No new requirements."
- 8.7: "Control of nonconforming outputs: Replaces 'Control of nonconforming product'. No requirement for a documented procedure. But there is a requirement to maintain documented information. When dealing with nonconforming product or service, the organisation needs to consider: segregation, containment, return or suspension; informing the customer; authorise re-provision of the products and services."
- 10.2: "Does not include a clause on Preventive action as an emphasis on risk-based thinking throughout the standard supersedes a single clause on preventive action." Y: "taking action to control and correct nonconformity and address the consequences, determining if similar nonconformities exist or could happen, making changes to QMS if necessary."
Atención: la diapositiva dice "authorise re-provision", mientras que la lista de 8.7.1 que circula por los sitios secundarios dice "obtaining authorization for acceptance under concession". No se pudo dirimir cuál es el texto de la norma. Cuando dos fuentes discrepan hay que dar las dos y no inventar una tercera.

Lo que circula (secundario, sin verificar contra ISO): 8.7.1 "The organization shall ensure that outputs that do not conform to their requirements are identified and controlled to prevent their unintended use or delivery" (reproducido por un sitio de consultoría; fuente: https://www.isms.online/iso-9001/clause-8-7-control-of-nonconforming-outputs , buscador [S]); y 8.7.2, registros: "a) describes the nonconformity; b) describes the actions taken; c) describes the concessions obtained; d) identifies the authority deciding the action in respect of the nonconformity" (blog, [S]). Las cuatro acciones (corrección; segregación, contención, devolución o suspensión de la provisión; informar al cliente; autorización para aceptación bajo concesión) están en la primera ronda y en varias páginas, pero ninguna es la norma. Una sola fuente en realidad: todas parafrasean el mismo documento.

8.5.1 (control de la producción) y su mención del NSAI: "Includes the requirements of ISO 9001:2008 Clauses '7.5.1 Control of production and service provision' and '7.5.2 Validation of processes for production and service provision'. The requirement for work instructions has been replaced by Documented information." (mismo PDF).

### Recurso canónico
ISO 9001:2015 (y su sucesora 2026), cláusulas 8.5.2, 8.6, 8.7 y 10.2; de pago. Mientras no haya texto literal, la nota debe citar la cláusula por número y atribuir la paráfrasis a "organismo de normalización" o "consultoras", no a ISO. Alternativa abierta no encontrada.

### Qué registra un sistema
Idéntico a la primera ronda: no conformidad con su descripción, acciones, concesiones y autoridad que decidió (8.7.2), lo cual sí coincide con lo que listan las fuentes secundarias.

## 3. Shewhart y Deming: causas por azar, asignables, comunes y especiales

### Fuentes

| Fuente | Tipo | Marca | Puntaje |
|---|---|---|---|
| NIST 6.3.1 "What are Control Charts?", https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc31.htm | primaria (manual abierto) | [L] por el lector | 3/2/1/2 |
| Best M, Neuhauser D, "Walter A Shewhart, 1924, and the Hawthorne factory", Qual Saf Health Care 2006;15(2):142-143, https://pmc.ncbi.nlm.nih.gov/articles/PMC2464836 | secundaria (artículo revisado) | [L] por el lector | 2/1/1/1 |
| Deming, Out of the Crisis (cap. 11 "Common Causes and Special Causes of Improvement. Stable System", p. 309 según el índice), vía extractos de la U. de Oklahoma https://ou.edu/faculty/M/Jorge.L.Mendoza-1/DEMIN.htm | secundaria (extractos) | [L] | 1/1/1/1 |
| Shewhart, Economic Control of Quality of Manufactured Product (1931) | primaria | NO leída | |

### Afirmaciones con cita
- NIST 6.3.1 (literal, citado por el lector): "We would be searching for an assignable cause if a point would fall outside these limits"; "if chance causes alone were present"; "if the system of chance causes generates a variation in X"; "'in control' implies that all points are between the control limits and they form a random pattern". Las palabras "common cause" y "special cause" no aparecen, y Shewhart aparece solo en el nombre de una imagen. Es decir: NIST 6.3.1 sirve para "azar" y "asignable", no para Deming.
- Best y Neuhauser (2006): Shewhart "identified two categories of variation which he called 'assignable-cause' and 'chance-cause' variation"; "He devised the control chart as a tool for distinguishing between the two."; "Others call the two categories 'special-cause' and 'common-cause' variation, respectively." No atribuyen la terminología de común/especial a Deming. https://pmc.ncbi.nlm.nih.gov/articles/PMC2464836
- Deming, extractos de Oklahoma: "The fact is that most troubles with service or production are due to the system." y "Variations on performance are due to common causes (system) and special causes (out side the system)." La página da "94% common" y "6% special" (sección III.d), mientras que otro resumen da 85% y 15% (SlideShare, [S]): las dos cifras figuran y no coinciden. Cita que circula, "We shall speak of faults of the system as common causes of trouble, and faults from fleeting events as special causes", no se halló en ninguna fuente leída: NO citarla literal.
- LeanBlog (https://www.leanblog.org/2025/06/two-kinds-of-mistakes-and-the-wisdom-of-shewhart-100-years-later/) resume los dos errores de Deming: tratar variación común como especial (sobreajustar) y tratar una causa especial como común (no actuar). Es paráfrasis, sin página.
- Discrepancia a mencionar: algunas fuentes dicen que "causa asignable" de Shewhart y "causa especial" de Deming no son lo mismo (Deming la entiende como externa al sistema o efímera); otras las toman como sinónimos [S]. No se resolvió con texto primario.

### Hueco
Citas literales de Shewhart 1931 y de Deming de los libros: no obtenidas. La definición de "estado de control" de Shewhart que citan los secundarios (efectos de azar de un sistema constante de causas, sin una predominante) no se verificó.

## 4. Juran: la trilogía, y el costo de la calidad

### Fuentes

| Fuente | Tipo | Marca | Puntaje |
|---|---|---|---|
| Juran Institute, "More About the Juran Trilogy" (M. Goldman, 15 abr. 2019, actualizada 5 ago. 2025), https://www.juran.com/blog/the-juran-trilogy/ | primaria institucional (organización que lleva su nombre) | [L] | 2/2/2/2 |
| ASQ, J.M. Juran, "The Quality Trilogy", Quality Progress 19(8), August 1986, pp. 19-24, https://asq.org/-/media/ASQ-Supplemental-Media-Import/E/F/7/9/D/7188.pdf | primaria (el paper original) | [M] solo el abstract: el texto está detrás de membresía | 3/3/2/3 |
| U. de Alberta (Y. Reshef), https://sites.ualberta.ca/~yreshef/orga432/print/jurantrilolgy.html | secundaria | [L] | 1/1/1/1 |
| ASQ, "About: A. V. Feigenbaum", https://asq.org/about-asq/honorary-members/feigenbaum | primaria institucional | 403 directo; texto del buscador [S] | 2/1/1/2 |
| ASQ, "What is Cost of Quality (COQ)?", https://asq.org/quality-resources/cost-of-quality | primaria institucional | 403 directo; solo buscador [S] | 2/2/1/1 |

### Afirmaciones con cita
- Referencia: Juran, "The Quality Trilogy", Quality Progress, August 1986, vol. 19, issue 8, pp. 19-24. Abstract (ASQ, [M]): "In response to a crisis in quality, the author argues for a new direction in managing for quality." (https://asq.org/-/media/ASQ-Supplemental-Media-Import/E/F/7/9/D/7188.pdf).
- Juran Institute (literal): "The Juran Trilogy, also called Quality Management Trilogy, was presented by Dr. Joseph M. Juran as a means to manage for quality." "The underlying concept is that organizations must use three universal processes: Quality Planning (Quality by Design); Quality Control (Process Control & Regulatory); Quality Improvement (Lean Six Sigma)." El diagrama muestra "time on the horizontal axis and cost of poor quality (what goes up is bad) on the vertical axis". Sobre el control: "to prevent things from getting worse"; el pico esporádico se corrige "to restore the status quo". Sobre la mejora: "In effect, it was seen that the chronic waste was an opportunity for improvement". Y: "'breakthrough' means 'the organized creation of beneficial change and the attainment of unprecedented levels of performance.'" (https://www.juran.com/blog/the-juran-trilogy/). Juran Institute fecha la presentación en 1986 en el metadato de la página ("presented by Dr. Joseph M. Juran in 1986").
- Definiciones abreviadas de una universidad (secundaria, atribuidas a Juran sin cita de página): planificación: "Create a process that will be able to meet established goals and do so under operating conditions"; control: "Keep the waste from getting worse; meet quality goals during operations"; mejora: "Breaking through to unprecedented levels of performance" (https://sites.ualberta.ca/~yreshef/orga432/print/jurantrilolgy.html).
- Costo de la calidad (ASQ, vía buscador, no verificado en la página [S]): la biografía de Feigenbaum en ASQ dice "His was the first text to characterize quality costs as the costs of prevention, appraisal, and internal and external failure." La definición de ASQ de COQ es una forma de medir cuántos recursos van a prevenir la mala calidad, evaluar el producto o servicio y atender fallas internas y externas. Fallas internas: defectos detectados antes de entregar; externas: defectos que encuentra el cliente. Las cuatro categorías: prevención, evaluación, fallas internas, fallas externas.
- Debate en el mismo resultado de búsqueda (ASQ CMQ/OE BoK, [S]): la teoría tradicional supone un nivel óptimo de esfuerzo de calidad que minimiza el costo total; los defensores de TQM dicen que prevención y evaluación cuestan menos y las fallas más de lo que supone ese modelo.

### Hueco
Texto del paper de Juran (1986) y de Feigenbaum (Total Quality Control, 1951; Harvard Business Review, 1956): no leídos. ASQ devuelve 403. No se halló una definición literal de ASQ de las cuatro categorías.

### Recurso canónico
Para la trilogía: el paper de Juran de 1986 (ASQ, de membresía) y, como lectura abierta, la página del Juran Institute. Para el costo de la calidad: ASQ, página "Cost of Quality". Fijarse en que el control apaga picos esporádicos y no baja el nivel crónico: eso es mejora.

## 5. Disposición de no conformidades y comité de revisión de material (MRB)

### Fuente

| Fuente | Tipo | Marca | Puntaje |
|---|---|---|---|
| MIL-STD-1520C, "Corrective Action and Disposition System for Nonconforming Material", 27 June 1986 (supersede a 1520B, 3 July 1980), https://everyspec.com/MIL-STD/MIL-STD-1500-1599/MIL_STD_1520C_1489/ ; PDF https://everyspec.com/MIL-STD/MIL-STD-1500-1599/download.php?spec=MIL_STD_1520C.1489.pdf | primaria (norma de dominio público, cancelada) | [L] (OCR, algo ruidoso pero legible) | 3/3/2/3 |

Estado: EverySpec la lista como cancelada, con avisos hasta 1995 y 2003, y el listado comercial da una fecha de retiro de 27-02-1995 y la remite a SAE AS7106/2B [S, buscador]. Es una norma de contratos con el gobierno de los EE. UU. ("the Government" aprueba ciertas disposiciones): lo que sirve a un tema agnóstico son las definiciones y la lógica de dos niveles (revisión preliminar y comité).

### Definiciones literales (3.x, OCR limpiado)
- 3.5 Material Review Board (MRB): "A board consisting of representatives of contractor departments necessary to review, evaluate, and determine or recommend disposition of nonconforming material referred to it."
- 3.6 Nonconformance: "The failure of a characteristic to conform to the requirements specified in the contract, drawings, specifications, or other approved product description." 3.6.1 menor: la que no afecta "Health or safety", "Performance", "Interchangeability, reliability, or maintainability", "Effective use or operation", "Weight or appearance (when a factor)"; "Multiple minor nonconformances, when considered collectively, may raise the category to a major/critical nonconformance." 3.6.2 mayor o crítica: "A nonconformance other than minor that cannot be completely eliminated by rework or reduced to a minor nonconformance by repair."
- 3.7 Nonconforming material: "Any item, part, supplies, or product containing one or more nonconformances."
- 3.10 Preliminary Review (PR): "An evaluation by contractor-appointed Quality personnel ... to determine the disposition of nonconforming material after its initial discovery and prior to referral to the MRB. PR may result in an authorized disposition of the nonconforming material without referral to the MRB for final disposition."
- 3.12 Repair (reparación): "A procedure which reduces but not completely eliminates a nonconformance and which has been reviewed and concurred in by the MRB and approved for use by the Government. The purpose of repair is to reduce the effect of the nonconformance. Repair is distinguished from rework in that the characteristic after repair still does not completely conform to the applicable drawings, specifications, or contract requirements."
- 3.13 Rework (reproceso): "A procedure applied to a nonconformance that will completely eliminate it and result in a characteristic that conforms completely to the drawings, specifications, or contract requirements."
- 3.14 Scrap (descarte): "Nonconforming material that is not usable for its intended purpose and which cannot be economically reworked or cannot be repaired in a manner acceptable to the Government."
- 3.15 Standard Repair Procedure (SRP): "A documented technique for repair of a type of nonconformance which has been demonstrated to be an adequate and cost-effective method for repair when properly applied", con "an expiration date or a finite limit on the number of applications".
- "Use as is": NO tiene definición propia en 3.x. Aparece como disposición (5.3 f y 5.4, abajo).

### Quién y cómo decide
- 4.5: el MRB "shall be chaired by a representative of the contractor's Quality organization and shall include, as required, personnel representing other contractor organizations necessary to determine appropriate disposition of nonconforming material. As a minimum, the MRB shall include the chairman and a representative of the contractor's engineering organization responsible for product design."
- 5.2, revisión preliminar: si la no conformidad "Requires scrapping of the material because it is obviously unfit for use and cannot be economically reworked or repaired", "Can be eliminated by rework", "Requires return of the material to the supplier", o "Can be repaired using SRPs which have been concurred in by the MRB and approved by the Government", se dispone en PR; lo demás se envía al MRB. Y: "PR action does not negate the requirement for identification, documentation, and corrective action associated with nonconformances."
- 5.3, el MRB dispone: "Scrap. Rework. Return to supplier. Repair by an approved SRP. Recommend to the Government for repair by other than an SRP. Recommend to the Government for use-as-is. Request a waiver from the contracting officer."
- 4.5.1(b): "The MRB shall review and concur in all proposed use-as-is and repair dispositions prior to submission to the Government for approval." 5.4: "All use-as-is dispositions must be approved by the Government. Until the use-as-is disposition has been approved, the nonconforming material shall not be further processed nor used without prior Government authorization".
- Relación con ISO 9001 (inferencia mía, no de una fuente): la "concesión" de 8.7 y el "use as is con aprobación del cliente" de 1520C describen lo mismo en contratos con un cliente que aprueba. En una empresa sin cliente que apruebe, la autorización es interna y queda en 8.7.2.

### Qué registra un sistema
No conformidad (artículo, lote u orden, cantidad, característica, clasificación menor o mayor o crítica); quién la detectó y dónde; disposición de revisión preliminar o enviada al comité; disposición del comité (descartar, reprocesar, devolver al proveedor, reparar con un procedimiento estándar o no, usar como está, pedir una desviación); quién autorizó, y si requirió la aprobación del cliente; bloqueo del material hasta la disposición; costo; referencia a la acción correctiva. Sin evidencia de un sistema abierto en esta ronda.

### Recurso canónico
MIL-STD-1520C, 3.5 a 3.15 y 5.2 a 5.4 (abierta). Fijarse en la diferencia entre reproceso (queda conforme) y reparación (sigue sin conformar del todo) y en que "usar como está" requiere una autoridad por encima de la planta.

## 6. 8D, 5 porqués, Ishikawa y sus críticas

### Fuentes

| Fuente | Tipo | Marca | Puntaje |
|---|---|---|---|
| Wikipedia, "Eight disciplines problem solving", https://en.wikipedia.org/wiki/Eight_disciplines_problem_solving | secundaria (cita a Ford) | [L] por el lector | 1/2/1/1 |
| AllAboutLean, "The History of the Eight Disciplines Problem Solving (8D)", https://www.allaboutlean.com/8d-history/ | secundaria | [L] por el lector | 1/2/1/2 |
| Ford, "Team Oriented Problem Solving" (TOPS), 1987, y "8-D Problem Solving Overview" | primaria | NO leída (no hay copia pública oficial hallada) | |
| Ohno, T., Toyota Production System: Beyond Large-Scale Production, Productivity Press, 1988, ISBN 0-915299-14-3 | primaria | NO leída | |
| Wikipedia, "Five whys", https://en.wikipedia.org/wiki/Five_whys | secundaria | [L] por el lector | 1/2/1/1 |
| Card AJ, "The problem with '5 whys'", BMJ Qual Saf 2017;26(8):671-677, doi 10.1136/bmjqs-2016-005849, PMID 27590189 | primaria (el paper) | [M] (PubMed y Europe PMC dan solo la ficha: sin abstract; el texto da 403) | 3/3/1/3 |
| PSNet, https://psnet.ahrq.gov/issue/problem-5-whys | secundaria | [S] del buscador (403 directo) | 2/1/1/1 |
| ASQ, "Fishbone", https://asq.org/quality-resources/fishbone y ASQ "About: Kaoru Ishikawa", https://asq.org/about-asq/honorary-members/ishikawa | primaria institucional | [S] del buscador (403 directo) | 2/1/1/1 |

### 8D: origen y las ocho disciplinas
- Origen. Wikipedia (relato de Ford): en 1986 se encargó un manual y un curso; el manual, "Team Oriented Problem Solving" (TOPS), fue "first published in 1987" y se probó en la sede de Dearborn; los ejecutivos de la Powertrain Organization "wanted a methodology where teams" pudieran trabajar problemas crónicos. La variante vigente de Ford es G8D (Global 8D), revisada a fines de los años 90. https://en.wikipedia.org/wiki/Eight_disciplines_problem_solving
- AllAboutLean: "The results of this work, the Team Oriented Problem Solving Manual by Ford was first published in 1987." https://www.allaboutlean.com/8d-history/
- Discrepancia sobre el origen: AllAboutLean escribe sobre MIL-STD-1520C que, como proveedor militar, Ford "was probably heavily influenced" por ella (conjetura, no hecho); otro resultado del buscador la llama "disputed" y un documento de Scribd afirma que nunca se basó en una norma militar; TWI dice que sigue un enfoque original de Kepner-Tregoe [S]. No hay una fuente primaria que lo resuelva. Lo único documentado en esta ronda es que 1520C (1986) existe, es anterior a TOPS (1987) y trata acción correctiva con un comité de revisión: la influencia no está probada. No afirmarla.
- Las disciplinas, tal como las lista la fuente (Wikipedia y AllAboutLean coinciden, con variantes de nombre; ninguna es el manual de Ford):
  - D0: "Preparation and Emergency Response Actions" ("Plan for solving the problem and determine the prerequisites. Provide emergency response actions."); agregada después (mediados de los 90, según un resultado de buscador sobre Mindtools [S]).
  - D1: "Establish a Team" / "Use a Team" ("Establish a team of people with product/process knowledge").
  - D2: "Describe the Problem" (en términos cuantificables: "the who, what, where, when, why, how, and how many (5W2H)").
  - D3: "Develop Interim Containment Plan" ("Define and implement containment actions to isolate the problem from any customer").
  - D4: "Root Cause Analysis and Escape Points" (Wikipedia: "Determine and Verify Root Causes and Escape Points"; también por qué pasó inadvertido).
  - D5: "Develop Permanent Solution" (Wikipedia: "Verify Permanent Corrections (PCs) ... that will resolve the problem for the customer"; confirmar cuantitativamente con programas de preproducción).
  - D6: "Implement Permanent Solution" (Wikipedia: "Define and Implement Corrective Actions").
  - D7: "Prevent Recurrence" ("Modify the management systems, operation systems, practices, and procedures").
  - D8: "Close Problem and Recognize Contributors" (Wikipedia: "Congratulate the Main Contributors to your Team").
  Dos fuentes secundarias dan nombres distintos para D5 y D6: se muestran las dos. El orden original de 1987 tenía ocho pasos sin D0.

### 5 porqués
- Ohno, citado por Wikipedia: el método es "the basis of Toyota's scientific approach by repeating why five times" y así "the nature of the problem as well as its solution becomes clear". Cita de libro: Ohno, Taiichi (1988), Toyota Production System: Beyond Large-Scale Production, Portland, OR: Productivity Press, ISBN 0-915299-14-3. La frase exacta del libro NO se verificó: las versiones en línea varían. https://en.wikipedia.org/wiki/Five_whys
- Origen según Wikipedia: "originally developed by Sakichi Toyoda"; fue "initially developed to understand why new product features or manufacturing techniques were needed", y no fue diseñado como análisis de causa raíz [S].
- Card, 2017 (via Wikipedia, [S]): "The arbitrary depth of the fifth why is unlikely to correlate with the root cause." Sostiene que el método se basa en "a misguided reuse of a strategy to understand why new features should be added to products" y propone diagrama de espina de pescado u otros. Del buscador (PSNet, [S]): es uno de los enfoques más enseñados en salud; Card concede su valor pedagógico, pero lo desaconseja para investigaciones reales; una cadena de porqués da una vista estrecha de la vía causal y otro equipo puede armar otras cinco cadenas igualmente válidas.
- Críticas generales (Wikipedia, [S]): se detiene en síntomas, depende del conocimiento del investigador, no es repetible entre investigadores y aísla una única causa raíz. Teruyuki Minoura (ex Toyota) lo calificó de demasiado básico para analizar causas raíz con la profundidad necesaria.
- Nota de un blog (LeanBlog, 2026, opinión): el famoso ejemplo de Ohno tiene más de cinco pasos causales. No es fuente primaria.

### Ishikawa
ASQ (buscador, [S]): se llama diagrama de Ishikawa "because Kaoru Ishikawa developed it" y diagrama de espina de pescado por su forma; "illustrates the main causes and subcauses leading to an effect (symptom)"; la versión de Ishikawa usó seis categorías, las "6 M" (materiales, maquinaria, métodos, medición, mano de obra, medio ambiente). No se halló el año ni el libro de origen: NO fechar. https://asq.org/quality-resources/fishbone

### Recurso canónico
Para el 8D: el manual de Ford TOPS/G8D (no hallado) y, mientras tanto, Wikipedia con su bibliografía (Pruitt, W. F., "A Disciplined Approach", Quality Progress 52(5), mayo 2019). Para la crítica de los 5 porqués: Card (2017). Fijarse en D3 (contención) y D7 (prevenir la recurrencia) como los pasos que un sistema suele omitir, y en que el 8D nombra "escape points" (por qué el defecto llegó al cliente).

### Qué registra un sistema (CAPA o 8D)
Número de caso y origen; descripción cuantificada (qué, dónde, cuándo, cuánto); equipo; contención con fecha y alcance (qué lotes, qué stock); causas candidatas, causa raíz y causa de escape, con método y evidencia; acción permanente y su verificación; acción para prevenir recurrencia (documentos o sistemas modificados); cierre y quién. Sin evidencia de un sistema abierto en esta ronda.

## 7. Huecos finales (qué sigue sin cerrar)

1. Texto literal de ISO 9001:2015 8.5.2, 8.6, 8.7 y 10.2, y del Anexo A.3 (acción preventiva): bloqueado (403) y pago. Hay una fuente de organismo nacional (NSAI, diapositivas) y paráfrasis comerciales. No hay una versión abierta hallada. La discrepancia entre "authorise re-provision" (NSAI) y "obtaining authorization for acceptance under concession" (resto) no se resolvió.
2. Texto y numeración de ISO 9001:2026 (qué cambió en 8.x y 10.2): no se leyó. Solo el comunicado de ISO sobre los énfasis (liderazgo, cultura de calidad, riesgos y oportunidades, estructura armonizada, nuevo anexo).
3. Ficha de ISO 9001:2026 y de ISO 2859-1:2026 leídas por la página de ISO: no, 403. El estado "Published" y las fechas salen del buscador (citando la ficha) y de dos páginas de ISO/TC 176 y del comunicado, que sí abrieron.
4. Tabla VIII de 105E (límites para pasar a reducida) y tablas de inspección rigurosa (II-B) y reducida (II-C): no leídas con detalle. La relación Z1.4 e ISO 2859-1 como "descendientes" de 105E no está en un texto leído, salvo el aviso de cancelación de 1995 [S].
5. Primarias de Shewhart (1931), Deming (Out of the Crisis, 1982-86), Juran (1986), Feigenbaum (1951, 1956), Ohno (1988), Ford TOPS (1987), Ishikawa: no leídas. Todo es secundario o institucional.
6. La definición de las cuatro categorías de costo de la calidad según ASQ: solo por el buscador.
7. Card (2017): sin abstract ni texto. Solo la ficha bibliográfica (PubMed) y resúmenes secundarios.
8. Origen del 8D: discrepancia entre fuentes (influencia de 1520C vs. enfoque propio vs. Kepner-Tregoe): sin primaria.
9. Evidencia de un sistema abierto sobre no conformidad, MRB, CAPA y muestreo de aceptación: no investigada esta ronda (la primera ronda cubrió solo la inspección de Odoo y ERPNext).
10. Anotación para la nota: la memoria de las normas MIL (105E y 1520C) tiene un valor histórico y sirve como texto abierto, pero están canceladas. Hay que decirlo cada vez que se las cite.
