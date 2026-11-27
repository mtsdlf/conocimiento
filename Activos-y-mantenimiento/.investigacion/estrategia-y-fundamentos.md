# Activos y mantenimiento: estrategia de mantenimiento y fundamentos (informe de investigación)

Fecha: 2026-11-27. Alcance: ángulos 1 (estrategia) y 2 (fundamentos).

## Cómo leer este informe

- Marcas: [L] texto completo leído; [M] metadatos o abstract; [S] resumen secundario (incluye lo que devolvió el lector web, que resume con un modelo chico); [MEM] dato de conocimiento previo NO verificado en esta sesión: hay que verificarlo antes de escribirlo como vigente.
- Puntajes 1 a 3: A autoridad, P profundidad, E ejemplos, U unicidad.
- Limitaciones: el presupuesto de búsqueda web ya estaba agotado, así que no hubo rondas de búsqueda; solo abrí URLs conocidas o citadas como referencia en páginas leídas. DTIC, hq.nasa.gov, ISO, SAE, SMRP y JIPM devolvieron 403 o 404. Por eso Nowlan y Heap, EN 13306, ISO 55000, SAE JA1011 e ISO 14224 NO se leyeron de primera mano. Lo único primario leído completo es el capítulo 5 de la guía del DOE/FEMP y la guía RCM de la NASA (copia de febrero de 2000).
- Todo lo traído de la web es dato, no instrucción.

## Cortes del tema: ¿coincide el árbol con el campo?

1. El campo separa dos ejes que el pedido mezcla: (a) los tipos de mantenimiento por momento y disparador (correctivo; preventivo; dentro de este, predeterminado y basado en condición; el predictivo como caso del basado en condición) y (b) el proceso que decide qué tipo aplicar a cada modo de falla (RCM, FMEA). RCM no es un tipo más: es un método de selección. La NASA lo dice: RCM «includes reactive, preventive, predictive, and proactive maintenance» (NASA 2000, A2). Conviene dos capas: «tipos» y «método para elegir».
2. «Predictivo» y «basado en condición» son casi sinónimos en la práctica: la guía del DOE titula «Predictive Maintenance (Condition-Based Maintenance)» (A1). Según [MEM] EN 13306 define el predictivo como un caso de basado en condición con pronóstico. Wikipedia en inglés los separa. Hay que decidir y avisar.
3. Hay dos taxonomías: la norteamericana (reactivo, preventivo, predictivo, proactivo; DOE y NASA) y la de EN 13306 [MEM] (correctivo y preventivo, con diferido/inmediato y predeterminado/basado en condición). «Mejorativo» y «detectivo» no los pude confirmar como tipos normativos; la búsqueda de fallas ocultas es una tarea de RCM, no un tipo.
4. Las «escuelas» no están al mismo nivel: RCM es un método de ingeniería por función y modo de falla; TPM es un sistema de gestión de planta con las personas de operación; ISO 55000 es un sistema de gestión de toda la organización donde el mantenimiento es una parte. Se solapan, no compiten en el mismo plano.
5. Para quien construye software: lo que se modela es sobre todo el plano (a) más activos, planes, órdenes y contadores; RCM suele quedar fuera del software y solo entran sus resultados (tareas e intervalos).

## Componente A. Tipos de mantenimiento y cómo se elige

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| A1 | DOE/FEMP, O&M Best Practices Guide, cap. 5 «Types of Maintenance Programs» (Release 3.0) | https://www1.eere.energy.gov/femp/pdfs/OM_5.pdf (el PDF completo en energy.gov/sites/prod/files/2013/10/f3/omguide_complete.pdf dio 404) | primaria, organismo público | 2 | 2 | 2 | 2 | [L] |
| A2 | NASA, RCM Guide for Facilities and Collateral Equipment, copia de feb. 2000 (existe edición 2008 que no pude abrir) | https://everyspec.com/NASA/NASA-General/download.php?spec=NASA_RCM_GUIDE_2000.030306.pdf (ficha: http://everyspec.com/NASA/NASA-General/NASA_RCM_GUIDE_2000_267/) | primaria, organismo público | 3 | 3 | 3 | 2 | [L] |
| A3 | Wikipedia, Maintenance, repair, and operations (sección Types) | https://en.wikipedia.org/wiki/Maintenance,_repair,_and_operations | secundaria | 1 | 1 | 1 | 1 | [S] |
| A4 | Wikipedia, Predictive maintenance | https://en.wikipedia.org/wiki/Predictive_maintenance | secundaria, con aviso de contenido promocional | 1 | 1 | 1 | 1 | [S] |
| A5 | EN 13306 «Maintenance terminology», ficha comercial (el vendedor la marca como no vigente en su edición 2018) | https://www.en-standard.eu/csn-en-13306-maintenance-maintenance-terminology/ | metadatos de la primaria | 3 | 1 | 1 | 3 | [M] (la ficha no mostró las definiciones) |

Afirmaciones:

- El DOE distingue reactivo, preventivo, predictivo y RCM. El reactivo es «basically the “run it till it breaks” maintenance mode» (A1, sec. 5.2).
- Preventivo: «Actions performed on a time- or machine-run-based schedule that detect, preclude, or mitigate degradation of a component or system with the aim of sustaining or extending its useful life through controlling degradation to an acceptable level» (A1, sec. 5.3).
- Predictivo: «differs from preventive maintenance by basing maintenance need on the actual condition of the machine rather than on some preset schedule». Ejemplo del documento: cambiar el aceite cada 3.000 a 5.000 millas (por uso) frente a analizarlo y extender hasta 10.000 (A1, sec. 5.4).
- Desventajas del preventivo según el DOE, que es la forma oficial del riesgo de sobremantener: «Includes performance of unneeded maintenance» y «Potential for incidental damage to components in conducting unneeded maintenance» (A1, sec. 5.3).
- Distribución en una instalación promedio: «>55% Reactive, 31% Preventive, 12% Predictive, 2% Other», de «Studies as recent as the winter of 2000», sin citar el estudio (A1, sec. 5.2).
- La NASA ubica cuándo conviene cada familia: reactivo para elementos pequeños, no críticos, sin consecuencia, improbables de fallar o redundantes; preventivo para los sujetos a desgaste, consumibles o con patrón de falla conocido; predictivo para fallas aleatorias, sin desgaste, o fallas inducidas por el propio preventivo; proactivo con análisis de causa raíz, exploración de edad y FMEA (A2, fig. 1-1).
- Generación de órdenes: el preventivo se dispara por calendario o por tiempo de marcha del equipo (A1, sec. 5.4: «like calendar time or equipment run time»). No hallé en lo leído nada sobre rutas, hojas de ruta o cómo se generan las órdenes (hueco 11).

Recurso canónico: A1 (diez páginas; mirar las tablas de ventajas y desventajas y la comparación de cuatro programas) para el mapa de tipos; A2, caps. 1 a 3, fig. 1-1, para cómo se elige; EN 13306 para la definición normativa (paga, no leída).

## Componente B. Mantenimiento preventivo

Fuentes: A1 y A2.

- Ahorro del preventivo sobre el reactivo: «Estimated 12% to 18% cost savings over reactive maintenance program» (A1, sec. 5.3), sin fuente en el texto.
- Costos por caballo de fuerza por año: reactivo 18 dólares, preventivo 13, predictivo 9, de Piotrowski (2001), «Pro-Active Maintenance for Pumps», Pump-Zone.com (A1, «Comparison of Four Maintenance Programs (Piotrowski 2001)» y sec. 5.7). Es un artículo de revista comercial sobre bombas que el DOE generaliza a maquinaria. Autoridad baja.
- Sobremantener: «In many cases scheduled overhaul increases the overall failure rate by introducing a high infant mortality rate into an otherwise stable system» (A2, sec. 2.4.5).
- Cuándo la edad sí sirve: «Single-piece and simple items frequently demonstrate a direct relationship between reliability and age... an age limit based on operating time or stress cycles may be effective» (A2, sec. 2.4.5).

Recurso canónico: A2 sec. 2.4 (patrones de falla y qué implican para las tareas por tiempo); atender a la distinción entre elementos simples y complejos.

## Componente C. Mantenimiento por condición y curva P-F

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| C1 | A1 sec. 5.4 | ver A1 | primaria | 2 | 2 | 2 | 2 | [L] |
| C2 | A2: glosario y esquema de PT&I (no leí las tecnologías del cap. 4) | ver A2 | primaria | 3 | 3 | 3 | 2 | [L] parcial |
| C3 | Moubray, Reliability-centred Maintenance (RCM II), 1997 | https://books.google.com/books?id=bNCVF0B7vpIC (citado por Wikipedia; no abierto) | primaria, libro de texto | 3 | 3 | 3 | 3 | [M] |

- «Potential Failure: An identifiable condition that indicates a failure is imminent» (A2, glosario). Es el punto P de la curva P-F.
- Ni A1 ni A2 usan «curva P-F» ni «intervalo P-F» en el texto que extraje (busqué la cadena sin resultados). Cuándo la condición es viable técnica y económicamente no tiene fuente primaria leída (hueco 6).
- El DOE condiciona el predictivo: «Increased investment in diagnostic equipment», «Increased investment in staff training», «Savings potential not readily seen by management» (A1, sec. 5.4); funciona «very well if personnel have adequate knowledge, skills, and time» (A1, comparación de programas).
- A4 no menciona P-F y su aviso de mayo de 2024 marca contenido promocional; sus afirmaciones de ahorro no tienen fuente.

Recurso canónico propuesto: Moubray RCM II, capítulo de tareas a condición (on-condition), fijándose en la definición del intervalo P-F y en que el intervalo de inspección debe ser una fracción del P-F [MEM, a verificar].

## Componente D. RCM

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| D1 | Nowlan y Heap, Reliability-Centered Maintenance, United Airlines, 1978, AD-A066579 | https://apps.dtic.mil/sti/citations/ADA066579 (403; el número sale de Wikipedia) | primaria | 3 | 3 | 3 | 3 | NO leída; solo citada por A2 y D3 |
| D2 | NASA RCM Guide | ver A2 | primaria | 3 | 3 | 3 | 2 | [L] |
| D3 | Wikipedia, Reliability-centered maintenance | https://en.wikipedia.org/wiki/Reliability-centered_maintenance | secundaria | 1 | 1 | 1 | 1 | [S] |
| D4 | SAE JA1011, Evaluation Criteria for RCM Processes | http://standards.sae.org/ja1011_200908 (la página no mostró contenido) | primaria paga | 3 | 1 | 1 | 3 | [M] indirecto |
| D5 | Wikipedia, Failure mode and effects analysis | https://en.wikipedia.org/wiki/Failure_mode_and_effects_analysis | secundaria | 1 | 1 | 1 | 1 | [S] |
| D6 | Klutke, Kiessler, Wortman (2003), «A critical look at the bathtub curve», IEEE Trans. Reliability | http://ieeexplore.ieee.org/document/1179819/ | primaria académica | 3 | 2 | 1 | 3 | [M] solo como referencia citada; no leída |

Historia y definición:

- NASA: «Analysis of maintenance policy in the airline industry in the late 1960's and early 1970's led to the development of Reliability Centered Maintenance (RCM) concepts... The work demonstrated that a strong correlation between age and failure rate did not exist and the basic premise of time based maintenance was false for the majority of equipment. Additional studies performed by the Department of Defense (DOD) and several nuclear utilities confirmed Nowlan and Heap's work» (A2, sec. 1.2). Nota al pie: «F. Stanley Nowlan and Howard F. Heap. Reliability-Centered Maintenance. United Airlines and Dolby Press, sponsored and published by the Office of Assistant Secretary of Defense, 1978».
- Wikipedia [S]: un texto de UAL y un informe de RAND, ambos de 1978 (cita DTIC ADA066579); adopción militar de EE.UU. a mediados de los 70 y nuclear comercial en los 80; Moubray encabezó RCM2 desde fines de los 80; Disney lo adoptó en 1997; la atribución del término a Matteson, Nowlan y Heap figura como disputada (D3).
- JA1011 fija «the minimum criteria that any process should meet before it can be called RCM», con fecha 1 de agosto de 1998 según Wikipedia (D3); la URL citada es de la edición 2009. [MEM] otras fuentes dicen 1999: verificar.
- Siete preguntas de RCM (de JA1011, paráfrasis de D3 [S]): función y estándar; cómo falla; qué causa cada falla; qué pasa al ocurrir; por qué importa; qué tarea proactiva previene o reduce las consecuencias; qué hacer si no hay tarea adecuada. Sin texto literal de la norma.
- FMEA (D5 [S]): MIL-P-1629 en 1949 (luego MIL-STD-1629A, 1980); uso por contratistas de NASA a comienzos de los 60; SAE ARP926 en 1967; automotriz a mediados de los 70; primera norma AIAG en 1993; SAE J1739 en 1994; el manual AIAG/VDA de 2019 reemplazó el RPN por «Action Priority». IEC 60812 no confirmada.

### Los seis patrones de falla y sus porcentajes

Dato primario leído en la NASA (A2, sec. 2.4.5, fig. 2-4). Los porcentajes de la figura, con las filas identificadas por la forma de curva que la NASA describe en el texto:

| Forma de curva | UAL 1968 | Broberg 1973 (la NASA escribe «Bromberg») | U.S. Navy 1982 |
|---|---|---|---|
| Bañera: mortalidad infantil, constante, desgaste | 4% | 3% | 3% |
| Constante o creciente y luego desgaste marcado | 2% | 1% | 17% |
| Aumento gradual, sin edad de desgaste | 5% | 4% | 3% |
| Baja probabilidad al inicio, sube rápido a un nivel constante | 7% | 11% | 6% |
| Probabilidad constante a toda edad | 14% | 15% | 42% |
| Mortalidad infantil y luego constante o creciente | 68% | 66% | 29% |

- Cada columna suma 100%.
- Advertencia de transcripción: reconstruí la correspondencia fila-valor desde el orden de la figura en el texto extraído; hay que confirmarla mirando el gráfico del PDF. La NASA rotula las curvas con letras distintas de las que, según [MEM], usan Moubray y la mayoría de la literatura (A a F con la bañera en A y la mortalidad infantil en F); en la NASA la bañera es «Type E» y la mortalidad infantil «Type B». No cruzar letras entre fuentes sin chequear.
- La Marina figura como «1982» en la figura y como «1983» en el texto de la misma guía. Que la fuente sea el programa MSP de la Marina o SUBMEPP, como menciona el pedido, es [MEM] y no lo verifiqué: la NASA no usa esos nombres.
- La NASA resume: «In these three studies, random failures accounted for 77-92% of the total failures and age related failure characteristics for the remaining 8-23%» (A2, sec. 2.4.5). No logré reproducir ese rango agrupando las columnas de la tabla; no repetirlo sin fuente.
- «Types A and E are typical of single-piece and simple items such as tires, compressor blades, brake pads, and structural members. Most complex items have conditional probability curves of types B, C, D, and F» (A2).
- Discrepancia entre estudios, que son dos fuentes dando distinto: UAL 1968 pone 68% en mortalidad infantil y 14% en constante; la Marina 1982 pone 29% y 42%, y 17% en desgaste tras vida constante contra 2% de UAL (A2). El reparto depende del tipo de equipo y de la fuente de datos.
- Crítica a las cifras: no encontré en esta corrida ninguna crítica verificable. Existe literatura académica sobre la curva de bañera (D6) que no leí.

Recurso canónico: Nowlan y Heap (D1), capítulos sobre patrones de falla y la lógica de decisión (NO leído; abrirlo desde un navegador). Público y leído: A2, cap. 2. Norma: SAE JA1011 (qué puede llamarse RCM) e IEC 60300-3-11 [MEM].

## Componente E. Historia, escuelas y dónde se produce el saber

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| E1 | Wikipedia, Total productive maintenance | https://en.wikipedia.org/wiki/Total_productive_maintenance | secundaria | 1 | 1 | 1 | 1 | [S] |
| E2 | Wikipedia, Asset management | https://en.wikipedia.org/wiki/Asset_management | secundaria | 1 | 1 | 1 | 1 | [S] |
| E3 | ISO 55000:2014 | https://www.iso.org/standard/55088.html (403) | primaria paga | 3 | 1 | 1 | 3 | [M] indirecto |
| E4 | IAM, conocimiento | https://theiam.org/knowledge/ | primaria, sociedad profesional | 2 | 1 | 1 | 2 | [S] |
| E5 | GFMAM | https://gfmam.org/ | primaria | 2 | 1 | 1 | 2 | [S] |
| E6 | Moubray, RCM II, sobre las generaciones | https://books.google.com/books?id=bNCVF0B7vpIC | primaria, libro | 3 | 3 | 3 | 3 | [M] no abierto |

- TPM (E1 [S]): Seiichi Nakajima lo desarrolló en Japón entre 1950 y 1970 y se aplicó en 1971; Nippondenso, proveedora de Toyota, fue la primera ganadora del premio PM; JIPM lo amplió a una versión de toda la empresa con ocho actividades. Ocho pilares: mantenimiento autónomo, mejora enfocada, mantenimiento planificado, mantenimiento de la calidad, gestión temprana del equipo, educación y entrenamiento, TPM administrativo, seguridad salud y ambiente. OEE: «Performance × Availability × Quality = OEE»; el 85% de clase mundial no está en esa fuente y queda sin verificar. Referencias de E1 para abrir: https://web.archive.org/web/20190605091909/https://www.cetpm.de/downloads/nakajima/index.htm y https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2246601.
- Gestión de activos (E2 [S]): ISO «published its management system standard for asset management in 2014»; ISO 55000 es de TC 251; ISO 55001 especifica requisitos y 55002 da lineamientos; activo: «item, thing or entity that has potential or actual value to an organization». E2 no menciona PAS 55. El IAM agrupa el tema en 39 materias bajo seis grupos (E4 [S]). GFMAM es una organización sin fines de lucro cuyos miembros visibles incluyen IAM, JIPM, EFNMS, Abraman, AEMA, PEMAC, SAAMA, IPWEA e IFRAMI (E5 [S]); SMRP no apareció en la lista visible.
- Las «generaciones» de Moubray, PAS 55 (2004, BSI) y la historia del correctivo al preventivo de posguerra: [MEM], sin verificar. Revista confirmada como referencia: IEEE Transactions on Reliability (D6). Reliability Engineering & System Safety y Journal of Quality in Maintenance Engineering: [MEM].

Mitos documentados:

- «La mayoría de los equipos fallan por edad»: la NASA lo refuta (A2, sec. 1.2) y con la salvedad de elementos simples, con desgaste o consumibles (A2, sec. 2.4.5).
- «Más preventivo es mejor»: A2 sec. 2.4.5 (la revisión programada puede subir la tasa de falla) y A1 sec. 5.3 (incluye mantenimiento innecesario).
- «El predictivo siempre conviene»: el DOE lo condiciona a inversión y personal (A1). Además la cifra de 8% a 12% no trae fuente: «Past studies have estimated that a properly functioning predictive maintenance program can provide a savings of 8% to 12% over a program utilizing preventive maintenance alone» (A1, sec. 5.4).
- Cifras de ahorro del DOE, literales: «independent surveys indicate the following industrial average savings resultant from initiation of a functional predictive maintenance program: Return on investment: 10 times; Reduction in maintenance costs: 25% to 30%; Elimination of breakdowns: 70% to 75%; Reduction in downtime: 35% to 45%; Increase in production: 20% to 25%» (A1, sec. 5.4). Procedencia: el texto dice solo «independent surveys»; la lista de referencias del capítulo (sec. 5.7) trae únicamente NASA 2000 y Piotrowski 2001. No son rastreables y no deben presentarse como dato duro. También: «could easily recognize savings opportunities exceeding 30% to 40%» (A1). No busqué si esas cifras están en la NASA.

Recurso canónico: para ISO 55000, la norma o la vista previa de ISO, más «Asset Management – An Anatomy» (IAM) y «The Asset Management Landscape» (GFMAM), mirando las 39 materias y el lugar del mantenimiento; para TPM, Nakajima, Introduction to TPM [MEM], pilares y OEE; para historia, Moubray RCM II cap. 1.

## Huecos

1. Nowlan y Heap 1978 no se leyó (DTIC 403): faltan porcentajes en la primaria, número de figura, lógica de decisión, definiciones de on-condition, hard-time y failure-finding.
2. EN 13306: sin definiciones literales de preventivo, predeterminado, basado en condición, predictivo, diferido e inmediato; vigencia de edición sin confirmar.
3. SAE JA1011 e IEC 60300-3-11: sin texto; siete preguntas literales sin ver; fecha 1998 contra 1999 sin resolver.
4. ISO 14224: no se buscó.
5. ISO 55000 y PAS 55: sin lectura ni fecha verificada de PAS 55.
6. Curva P-F e intervalo P-F y su viabilidad técnica y económica: sin fuente primaria leída; Moubray no se abrió.
7. Correspondencia exacta de letras y filas de los patrones de falla entre la NASA, Moubray y Nowlan y Heap: a confirmar con el gráfico.
8. Origen de «MSP» y «SUBMEPP» y cita original de Broberg: no verificados.
9. Crítica o discrepancia sobre los porcentajes 4/2/5/7/14/68: no encontrada.
10. Origen de las cifras de ahorro del DOE (8-12%, 25-30%, 70-75%, 35-45%, 20-25%, 10 veces) y del 12-18%: sin fuente en el documento y sin cotejo independiente.
11. Rutas, hojas de ruta, generación de órdenes por calendario y por contador, y sobremantenimiento medido: no hay fuente leída; es el hueco más relevante para quien construye el software.
12. Generaciones de Moubray, Nakajima 1988, JIPM, SMRP Body of Knowledge y las revistas del campo: sin verificar (SMRP y JIPM dieron 404).
13. «Mejorativo» y «detectivo» como tipos: sin confirmar en ninguna norma.
14. Se leyó la guía de la NASA de febrero de 2000, no la de 2008; las secciones corresponden a esa copia.
15. Fecha y autoría de la Release 3.0 de la guía del DOE: no verificadas en la página leída.

## Segunda ronda

Fecha: 2026-11-27. Solo WebFetch. Resúmenes de modelo chico: reabrir antes de citar literal.

### TPM y OEE (hueco 7)
- Wikipedia, Total productive maintenance [S; A1 P1 E1 U1] https://en.wikipedia.org/wiki/Total_productive_maintenance. Ocho pilares: "Autonomous maintenance", "Focused improvement", "Planned maintenance", "Quality maintenance", "Early/equipment management", "Education and training", "Administrative & office TPM", "Safety health environmental conditions". Discrepancia dentro de esa página: la introducción nombra "Development management" en vez de "Early/equipment management". Origen: Seiichi Nakajima lo desarrolló en Japón entre 1950 y 1970 y se aplicó por primera vez en 1971; es "regarded as the father of TPM"; Nippondenso fue el primer ganador del premio PM.
- Wikipedia, Overall equipment effectiveness [S] https://en.wikipedia.org/wiki/Overall_equipment_effectiveness. OEE = Disponibilidad × Rendimiento × Calidad; ejemplo de la página: 86,6% × 93% × 91,3% = 73,6%. Rendimiento = piezas producidas × tiempo de ciclo ideal / tiempo operativo. Origen: "The term OEE was first mentioned in Seiichi Nakajima's book 'TPM Tenkai' in 1982" (la relación con Harrington Emerson está marcada "citation needed"). El 85% de clase mundial, sin verificar en la primera ronda: la página lo discute: "To assume that 85% OEE is a 'world Class' target value is in many cases incorrect"; el 100% es una referencia teórica.

### Tipos de mantenimiento y EN 13306 (hueco 5, parcial)
- Wikipedia, Preventive maintenance [S] https://en.wikipedia.org/wiki/Preventive_maintenance: planificado "can be date-based, based on equipment running hours, or on distance travelled"; ítems con intervalo fijo (TCI); basado en condición cuando surge la necesidad, con monitoreo; predictivo = forma de basado en condición con sensores y tendencias. No cita EN 13306.
- Wikipedia, Corrective maintenance [S] https://en.wikipedia.org/wiki/Corrective_maintenance: cita NF EN 13306: correctivo = "maintenance which is carried out after failure detection"; inmediato "starts immediately after a failure"; diferido "delayed in conformance to a given set of maintenance rules". Cubre en parte el hueco 2, de segunda mano.
- Wikipedia, Predictive maintenance y RCM: no mencionan P-F ni patrones A a F; el hueco 6 sigue abierto.

### Nowlan y Heap y patrones de falla
DTIC (https://apps.dtic.mil/sti/citations/ADA066579 y https://apps.dtic.mil/sti/pdfs/ADA066579.pdf) devolvió 403 otra vez. La guía NASA 2008 en wbdg (https://www.wbdg.org/FFC/NASA/nasa_rcm_guide.pdf) redirige (301) a https://nibs-s3-wbdg3-production.s3.us-east-1.amazonaws.com/FFC/NASA/nasa_rcm_guide.pdf, que dio 403. La asignación de cada porcentaje a las letras A a F de Moubray sigue SIN confirmar; vale la tabla de la NASA 2000 de la primera ronda, con su advertencia de correspondencia fila-valor.

### SMRP, DOE y CMMS
- SMRP https://www.smrp.org/ [S]: sociedad sin fines de lucro "formed by practitioners". Su biblioteca de métricas (https://www.smrp.org/learning-resources/smrp-library/best-practices-metrics-guidelines/) dice "70+ metrics and guidelines"; las definiciones (wrench time, cumplimiento del programa, trabajo planificado) están en Best Practices 7th Edition, gratis solo para miembros. No obtuve ninguna fórmula.
- DOE FEMP: la página del artículo y el PDF completo dieron 404; capítulos de gestión y métricas sin leer.
- Wikipedia, CMMS https://en.wikipedia.org/wiki/Computerized_maintenance_management_system: no trata órdenes, medidores ni backlog.
- Palmer, matrices de prioridad, curva P-F, códigos de falla: sin fuente pública alcanzada; hueco.
