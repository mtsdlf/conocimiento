# Posición contraria sobre Activos y mantenimiento: informe de investigación

Fecha de consulta: 2026-11-27. Todo lo traído de la web se trató como dato. La herramienta de búsqueda estuvo agotada buena parte de la sesión y volvió después con pocas consultas; varias fuentes primarias (Nowlan y Heap 1978, la guía de O&M del DOE, artículos de revista de pago) **no se pudieron leer** y se declaran como huecos. Donde dice «cuenta como una fuente», varios textos parafrasean el mismo original.

**Veredicto en una línea por afirmación de la base** (detalle más abajo):

1. Definición de mantener: sin evidencia en contra; no se investigó.
2. Estrategia por equipo según criticidad y patrón de falla, con RCM: se sostiene como método, con tres matices fuertes (el RCM simplificado es una disputa abierta; los porcentajes de Nowlan y Heap son de aviación; los costos de análisis son altos).
3. Órdenes de trabajo planificadas y programadas: no se investigó (hueco).
4. Historial codificado de fallas: la evidencia disponible dice que el dato real suele estar incompleto o mal codificado.
5. MTBF, MTTR, disponibilidad: el MTBF solo es interpretable con tasa de falla constante; leerlo como vida útil es un error documentado.
6. Servicio de campo como el mismo ciclo: no se investigó (hueco).
7. Cifras que circulan («70% reactivo», ahorros del predictivo, «80% de los CMMS fracasan»): no encontré fuente primaria para las más repetidas; sí una primaria con un dato distinto (45,7% reactivo, NIST).

## Tabla de fuentes

Puntajes 1 a 3: Aut = autoridad, Prof = profundidad, Ej = ejemplos, Uni = unicidad. Marca: [L] texto completo leído, [M] metadatos o abstract, [S] resumen secundario o del buscador.

| # | Fuente | URL | Tipo | Marca | Aut | Prof | Ej | Uni |
|---|---|---|---|---|---|---|---|---|
| P1 | J. Moubray, «The Case Against Streamlined RCM» (Reliabilityweb) | https://reliabilityweb.com/articles/entry/the_case_against_streamlined_reliability_centered_maintanance | primaria (ensayo del autor de RCM2, parte interesada) | [L] (vía extracto del fetch) | 2 | 3 | 2 | 3 |
| P2 | Capítulo de Moubray en plant-maintenance.com con la Figura 1.5 (patrones de falla y porcentajes) | http://www.plant-maintenance.com/RCM-intro.shtml | primaria (extracto de libro; sitio que lo vende) | [L] (vía extracto del fetch) | 2 | 2 | 2 | 2 |
| P3 | D. Troyer, «Rethinking Maintenance: Why the 89% Rule Doesn't Fit All Assets» (Reliable Magazine; sin fecha visible) | https://reliamag.com/topics/articles/rethinking-maintenance-why-the-89-rule-doesnt-fit-all-assets | secundaria (opinión de especialista) | [L] | 2 | 2 | 2 | 2 |
| P4 | Wikipedia, «Reliability-centered maintenance» | https://en.wikipedia.org/wiki/Reliability-centered_maintenance | terciaria | [L] | 1 | 1 | 1 | 1 |
| P5 | Wikipedia, «Mean time between failures» y «Failure rate» | https://en.wikipedia.org/wiki/Mean_time_between_failures ; https://en.wikipedia.org/wiki/Failure_rate | terciaria (remite a Lienig y Bruemmer 2017 y Birolini 2013, no leídos) | [L] | 1 | 2 | 2 | 1 |
| P6 | Backblaze, «Drive Failure Over Time: The Bathtub Curve Is Leaking» (2021) | https://www.backblaze.com/blog/drive-failure-over-time-the-bathtub-curve-is-leaking/ | primaria (datos propios de una empresa) | [L] (vía extracto del fetch) | 2 | 2 | 3 | 3 |
| P7 | Wikipedia, «Bathtub curve» (cita a Klutke, Kiessler y Wortman 2003, «A critical look at the bathtub curve», IEEE Trans. Reliability 52(1), doi 10.1109/TR.2002.804492) | https://en.wikipedia.org/wiki/Bathtub_curve | terciaria; el artículo de Klutke no se pudo abrir | [L] de Wikipedia; Klutke [S] (solo título) | 1 | 1 | 1 | 1 |
| P8 | M. Hodkiewicz y M. Ho, «Cleaning historical maintenance work order data for reliability analysis», J. Quality in Maintenance Engineering 22(2), 146-163, 2016 | https://www.emerald.com/insight/content/doi/10.1108/JQME-04-2015-0013/full/html | primaria (revista) | [M] (abstract; texto de pago) | 3 | 2 | 1 | 3 |
| P9 | A. Salonen, M. Bengtsson y V. Fridholm, «The Possibilities of Improving Maintenance Through CMMS Data Analysis», Advances in Transdisciplinary Engineering 13 (SPS2020), pp. 249-260 (año inferido: 2020) | https://ebooks.iospress.nl/pdf/doi/10.3233/ATDE200163 | primaria (estudio de caso en una planta) | [M] (abstract) | 2 | 2 | 1 | 3 |
| P10 | NIST (alojada), «Standardization of maintenance data for benchmarking and asset performance analytics» (presentación; autores de la empresa Asset Answers) | https://www.nist.gov/document/s1-p5-maintenancedatacollectionchallengespdf | primaria (presentación de un proveedor, sin fecha) | [L] (pdftotext; es una presentación, hay poco texto) | 1 | 1 | 2 | 2 |
| P11 | D. Thomas y B. Weiss, «Economics of Manufacturing Machinery Maintenance: A Survey and Analysis of U.S. Costs and Benefits», NIST AMS 100-34, junio 2020 | https://nvlpubs.nist.gov/nistpubs/ams/NIST.AMS.100-34.pdf ; doi 10.6028/NIST.AMS.100-34 | primaria (informe oficial con encuesta) | [L] parcial (resumen ejecutivo, método; no leí todo el informe) | 3 | 3 | 2 | 3 |
| P12 | Reliable Magazine, «Predictive Maintenance ROI Benchmarks: What the Studies Show» | https://reliamag.com/topics/guides/predictive-maintenance-roi-benchmarks-what-the-studies-show | secundaria (evalúa fuentes; no leí los originales) | [L] | 2 | 2 | 2 | 2 |
| P13 | Reliable Magazine, «Do 80% of CMMS Implementations Fail? Tracing the Number» | https://reliamag.com/topics/articles/cmms-implementation-failure-rate | secundaria (rastreo de cifras; cita una encuesta de 2004 del Plant Maintenance Resource Center, no leída) | [L] | 2 | 3 | 3 | 3 |
| P14 | K. Moodley, editorial «Is ISO 55000:2014 the new dawn in asset management?», Infrastructure Asset Management 1(2), pp. 21-22, 2014 | https://www.emerald.com/jinam/article/1/2/21/436617/Editorial-Is-ISO-55000-2014-the-new-dawn-in-asset | primaria (editorial de revista; opinión) | [M] (extracto) | 2 | 1 | 1 | 2 |
| P15 | F. Ireland y B. G. Dale, «A study of total productive maintenance implementation», J. Quality in Maintenance Engineering 7(3), 183-192, 2001 | http://www.emerald.com/jqme/article/7/3/183-192/253384 | primaria (tres casos; autores de UMIST, Reino Unido) | [M] (abstract) | 2 | 2 | 1 | 3 |
| P16 | Wikipedia, «Overall equipment effectiveness» y AllAboutLean, «Top Three Methods on how to Fudge Your OEE» | https://en.wikipedia.org/wiki/Overall_equipment_effectiveness ; https://www.allaboutlean.com/fudge-oee/ | terciaria y blog de un practicante | [L] | 1 | 2 | 2 | 2 |
| P17 | Resultados del buscador sobre: guía de O&M del DOE (8-12% y 30-40%), SAJIE (RCM simplificado), WBDG, Computerworld y HBK (MTBF), tesis de Elgharib (TPM en Reino Unido), Cosmo Tech y EY (ISO 55001) | URLs en el cuerpo, marcadas [S] | secundaria | [S] | 1 | 1 | 1 | 1 |

## 1. Sobre el RCM como método

**Qué dice la base:** la estrategia (correctivo, preventivo, por condición, dejar fallar) se elige por equipo según su criticidad y su patrón de falla, con el RCM como método.

**Lo que lo sostiene.** Wikipedia describe que el RCM distingue funciones críticas, que deben preservarse, de no críticas, que pueden dejarse en «run to failure», y que la mayoría de las fallas no están necesariamente ligadas a la edad (P4, https://en.wikipedia.org/wiki/Reliability-centered_maintenance). SAE JA1011 define los criterios mínimos para llamarse RCM, con siete preguntas (P4). Moubray sostiene que «Leaving things out inevitably increases risk» y que el RCM completo se paga «between two weeks and two months» sobre «más de 1 500 sitios, 44 países» (P1, https://reliabilityweb.com/articles/entry/the_case_against_streamlined_reliability_centered_maintanance). Es el autor de RCM2 y vende el método: cifra sin respaldo verificable, de parte interesada.

**La disputa sobre el RCM simplificado.** Moubray dice que ningún proceso simplificado cumple SAE JA1011, que exige responder siete preguntas «in the sequence shown»; que el RCM «retroactivo» (parte de las tareas existentes) deja modos de falla sin cubrir y que «most of the protective devices in industry» «are maintained poorly or not at all»; que analizar solo lo «crítico» se basa en suposiciones que con frecuencia resultan erróneas; y que «there is simply no place for shortcuts» (P1). Los defensores de lo simplificado afirman obtener resultados similares «in about a half to a third of the time»; Moubray considera ese caso de negocio «suspect at best» (P1). Según un resumen del buscador [S], hay estudios del EPRI de los años 90 que hallaron diferencias menores entre clásico y simplificado, cuestionados por los partidarios del RCM clásico, y un artículo sudafricano (SAJIE) que concluye que su método simplificado es superior al clásico (https://sajie.journals.ac.za/pub/article/download/311/256/274, no leído); una guía del WBDG trata las variantes como legítimas y deja la elección al usuario (https://wbdg.org/node/306, no leído) [S]. Wikipedia reconoce que muchos enfoques posteriores «reducían el rigor» y que alguno fue «incluso peligroso», pero eso está sin fuente (P4). **Discrepancia a presentar tal cual:** Moubray (clásico, parte interesada) contra defensores de lo simplificado (también con intereses). No hay estudio comparativo independiente en lo que leí. El texto de Moubray, además, no menciona al EPRI; esa mención viene solo del resumen del buscador.

**Costo del RCM.** El extracto de Moubray en P2 no da cifras monetarias; sí dice que el paso de funciones y estándares toma «cerca de un tercio» del tiempo de un análisis completo, y que una planta industrial promedio puede producir un análisis de «entre 3 000 y 10 000 modos de falla» (http://www.plant-maintenance.com/RCM-intro.shtml, vía extracto). No encontré estudio independiente sobre tasas de fracaso de implementaciones de RCM: **hueco**.

## 2. Sobre los patrones de falla de Nowlan y Heap

**Lo que se afirma:** el RCM se apoya en que la mayoría de los modos de falla no dependen de la edad.

**Qué dice la fuente.** El extracto de Moubray (Figura 1.5, estudio de aviación civil) da: patrón A 4%, B 2%, C 5%, D 7%, E 14%, F 68% (suman 100%; D+E+F = 89%, de ahí el «89% no se relaciona con la edad»). El propio texto advierte: «The number of times these patterns occur in aircraft is not necessarily the same as in industry» (P2, http://www.plant-maintenance.com/RCM-intro.shtml). El original de Nowlan y Heap (1978, informe al Departamento de Defensa de EE. UU., apps.dtic.mil/sti/citations/ADA066579) **no se pudo abrir** (HTTP 403): no leí la tabla original ni su tamaño de muestra. Según un resumen del buscador [S], los datos son de 1968 de United Airlines, y un estudio sueco de Blomberg (1973) llegó a proporciones similares.

**Crítica.** Troyer: la cifra es válida en su contexto pero se volvió «regla universal»; «aircraft are not haul trucks, crushers, slurry pumps, or SAG mills» y en minería predominan modos de falla por desgaste (abrasión, fatiga, cavitación, corrosión) (P3, https://reliamag.com/topics/articles/rethinking-maintenance-why-the-89-rule-doesnt-fit-all-assets). Es opinión de un especialista, no estudio empírico. Un resumen de la misma búsqueda [S] no halló estudios de campo independientes con Weibull que contrasten el 89% fuera de aviación. Hay un dato de otro tipo: ARC Advisory Group afirmaría que solo 18% de las fallas se relacionan con la edad (82% aleatorio) con datos de NASA y la Marina de EE. UU. (citado por P12; no leí el original de ARC). Ese 18% es otra muestra distinta, en dirección parecida a Nowlan y Heap.

**Sobre la curva de bañera.** Backblaze (datos propios de discos): en 2013 la curva tenía tramo decreciente de 5,1% (0 a 18 meses), constante de 1,4% (18 meses a 3 años) y creciente de 11,8% (3 a 4 años); en 2021 «our bathtub curve looks more like a hockey stick» (P6, https://www.backblaze.com/blog/drive-failure-over-time-the-bathtub-curve-is-leaking/). Wikipedia cita el artículo «A critical look at the bathtub curve» (Klutke, Kiessler y Wortman 2003) y aclara que «Many but not all electronic consumer product life cycles follow the bathtub curve» (P7, https://en.wikipedia.org/wiki/Bathtub_curve); no leí a Klutke.

## 3. Sobre el historial codificado de fallas

**Lo que dice la base:** el historial codificado permite mejorar.

**Evidencia en contra o matices.**

- Hodkiewicz y Ho (2016), con datos de equipo móvil pesado de varias organizaciones: los registros históricos de órdenes de trabajo suelen tener «missing or incorrect functional location, failure mode, maintenance action and WO status fields»; proponen corregirlos con campos de texto libre y conocimiento de las prácticas de mantenimiento (P8, https://www.emerald.com/insight/content/doi/10.1108/JQME-04-2015-0013/full/html). Solo leí el abstract; no hay porcentajes.
- Salonen et al.: el principal obstáculo para usar los datos del CMMS es la mala descripción de fallas y averías, tanto en las solicitudes de operarios y ensambladores como en los informes de técnicos (P9, https://ebooks.iospress.nl/pdf/doi/10.3233/ATDE200163). Un estudio de caso en una planta de componentes de transmisión.
- Presentación alojada por NIST, de una empresa proveedora: «Challenge: EVERYONE uses the CMMS/EAM differently»; «companies can have 20+ codes, or combinations of different codes which map to these 4 event types» (P10, https://www.nist.gov/document/s1-p5-maintenancedatacollectionchallengespdf). Es dato de proveedor, sin cifras de error.
- Un resumen del buscador [S] menciona trabajos sobre errores de categorización al cargar órdenes de trabajo (NIST) y sobre lenguaje técnico en texto libre (Conte et al., PHM Society 2021); no los abrí.

**Hueco:** no encontré un estudio con el porcentaje de órdenes de trabajo mal codificadas respecto de su texto libre. Los blogs de proveedores que dan cifras («hasta 80% de reducción con limpieza», «95% de cobertura») no son confiables y no las uso.

## 4. Sobre MTBF, MTTR y disponibilidad

**Lo que dice la base:** MTBF, MTTR y disponibilidad miden el desempeño.

**Matices del MTBF.**

- Solo vale con tasa de falla constante: «this is only valid if the failure rate λ(t) is actually constant over time» (Wikipedia, Failure rate); con tasa constante el tiempo hasta la falla es exponencial, la probabilidad de sobrevivir hasta el MTBF es 1/e, unas 37%, y falla antes con 63% (P5, https://en.wikipedia.org/wiki/Mean_time_between_failures y https://en.wikipedia.org/wiki/Failure_rate). Leerlo como «vida media» (la mitad ha fallado en t = MTBF) «can lead to bad design decisions» (P5). Las fuentes de Wikipedia son Lienig y Bruemmer (2017) y Birolini (2013), que no leí.
- Ejemplo numérico propio (cuenta mía, no de una fuente): 100.000 horas son 11,4 años (100000 / 8760). Con tasa constante, la probabilidad de que un equipo falle en el primer año es 1 − e^(−8760/100000) ≈ 8,4%, y a las 100.000 horas ya habría fallado el 63%. La frase «un MTBF de 100.000 horas no significa que dure 11 años» no la encontré atribuida a una fuente primaria: es explicación de manual, y el cálculo es mío.
- Con tasa constante, el mantenimiento preventivo por tiempo no mejora la confiabilidad del componente (resumen del buscador de un artículo de práctica [S]: https://www.computerworld.com/article/1691853/sidebar-into-the-bathtub.html y https://www.hbkworld.com/fr/knowledge/resource-center/articles/limitations-of-the-exponential-distribution-for-reliability-analysis; ambos sin abrir; el segundo dio 403).
- Si solo se cuentan fallas observadas, el MTBF se subestima por censura (P5). Qué cuenta como falla depende del contexto, y para sistemas no reparables se recomienda MTTF (P5).

**Hueco:** nada sobre MTTR ni disponibilidad como críticas (no los investigué). Sobre OEE (derivado de disponibilidad): Wikipedia dice que el número no sirve para comparar máquinas, turnos ni plantas y que el «85% es world class» no tiene origen citado; AllAboutLean afirma que los OEE reportados suelen estar entre 80% y 95% pero en la industria occidental el real estaría entre 40% y 60%, y que el tiempo de mantenimiento planificado suele excluirse del cálculo (P16, https://en.wikipedia.org/wiki/Overall_equipment_effectiveness y https://www.allaboutlean.com/fudge-oee/). Son afirmaciones de un blog; no las confirmé.

## 5. Cifras que circulan sin fuente primaria

**«X% del mantenimiento es reactivo».** La única fuente primaria que encontré es NIST AMS 100-34 (junio 2020): «On average, 45.7 % of machinery maintenance was reactive maintenance», en una encuesta a establecimientos manufactureros de EE. UU. con 85 respuestas devueltas, de las cuales algunas se descartaron (P11, https://nvlpubs.nist.gov/nistpubs/ams/NIST.AMS.100-34.pdf). Según el buscador [S], la proporción 17,3% predictivo, 31,8% preventivo y 45,7% reactivo sale de ese estudio. No encontré fuente para «55% reactivo / 31% preventivo / 12% predictivo» ni para «70% reactivo»: queda sin respaldo. Una página sobre estadísticas de mantenimiento atribuye al DOE ahorros del predictivo, pero sin el original.

**Ahorros del predictivo.** Se atribuyen a la guía «Operations & Maintenance Best Practices, Release 3.0» del DOE (8% a 12% menos que el preventivo, 30% a 40% menos que el reactivo; ver P12 y los resultados del buscador [S]). **No pude abrir el original** (la descarga se cortó; otras URLs dieron 404), por lo que no verifico página ni la fuente que el DOE cita. P12 evalúa que esa cifra «declara su línea base», pero que la lista famosa del mismo documento («10x», averías reducidas 70% a 75%) es de baja confianza: «Older industrial studies repackaged in a federal energy guide». P12 también advierte que McKinsey 2017 (reducción de tiempo de inactividad 30% a 50%) «describes mature programs», que un 10% de falsos positivos anuló los ahorros de un programa (McKinsey 2021) y que el titular de Deloitte Analytics (productividad +25%, averías −70%) «traces to a vendor blog rather than original research» (https://reliamag.com/topics/guides/predictive-maintenance-roi-benchmarks-what-the-studies-show). P12 es secundaria y no leí los originales. La Wikipedia del mantenimiento predictivo está marcada por contenido promocional y no cuantifica ahorros (https://en.wikipedia.org/wiki/Predictive_maintenance).

**Datos de NIST sobre asociación, no causa.** Entre quienes dependen menos del mantenimiento reactivo, los que más usan predictivo se asocian con 15% menos de inactividad y 87% menos defectos; los que invierten más en preventivo o predictivo, 44% menos de inactividad (P11). Es un estudio de asociación sobre encuesta voluntaria: no prueba que el cambio de estrategia cause el efecto.

**«80% de las implementaciones de CMMS fracasan».** P13 rastrea la cifra: Kishan Bagadia, *Computerized Maintenance Management Systems Made Easy* (2006) dice «60% to 80% of programs fail because of poor planning» sin citar estudio; luego aparece como 80% (FacilitiesNet 2008), «60% a 80%» (2012), «hasta 80%» atribuido a expertos sin nombre (eMaint 2018), 80% a 90% atribuido a Software Advice con enlace a su página principal (Accruent 2022) y 60% a 80% atribuido a Gartner (FreeMaint, 2026; no verificado) (https://reliamag.com/topics/articles/cmms-implementation-failure-rate). El único dato identificable es una encuesta voluntaria de 2004 del Plant Maintenance Resource Center, 105 respuestas válidas, donde 13 de 85 calificaron la implementación como «poor» (15,3%), sin definir «poor» como abandono ni como fracaso financiero (P13; no leí la encuesta). La cifra del 50% atribuida a un artículo de plantservices.com de 1999 aparece solo en un resumen del buscador [S] de un informe de la National Academies (https://nap.nationalacademies.org/read/25053/chapter/2, no abierto): P13 no contiene esa cifra. **Conclusión:** no hay estudio primario detrás del 60-80%; son citas que se repiten entre sí, y la definición de «fracaso» varía.

## 6. ISO 55000

**Lo que dice la base** (no listada en el resumen, pero se pidió): ISO 55000 como estándar de gestión de activos.

**Críticas.** Moodley (2014) escribe que «the implementation of auditable management systems has focused on the audit, documentation and conformity» en vez de la mejora continua y la innovación, y que la norma debe demostrar que es más que un ejercicio de cumplimiento; menciona costos de implementación y acreditación pero sostiene que habría eficiencias compensatorias (P14, https://www.emerald.com/jinam/article/1/2/21/436617/Editorial-Is-ISO-55000-2014-the-new-dawn-in-asset). Es un editorial, no un estudio, y lo presenta como visión extendida, sin atribuir a un crítico concreto. Resúmenes del buscador [S]: una encuesta de EY de 2021 reportó que 71% de los encuestados evalúa que su organización no cumple ISO 55001 (https://www.ey.com/en_no/consulting/is-compliance-with-iso-550001-essential-for-effective-asset-management, no abierta); un blog de un proveedor (Cosmo Tech) habla de certificaciones sin resultados operativos (no verificable). Wikipedia no recoge críticas (P-Wikipedia ISO 55000, https://en.wikipedia.org/wiki/ISO_55000, leída). **Hueco:** no hay estudio empírico leído sobre burocracia o resultados de la certificación; un resumen del buscador menciona que la investigación académica sobre implementación es escasa (Androjna y Maletič 2023, no abierto) [S].

## 7. TPM fuera de Japón

Ireland y Dale (2001), tres empresas (país no indicado en el abstract; autores de UMIST, Reino Unido): la alta dirección apoyó el TPM en las tres y creó estructuras; las tres siguieron los siete pasos de mantenimiento autónomo de Nakajima y tomaron pilares distintos (P15, http://www.emerald.com/jqme/article/7/3/183-192/253384). Es evidencia de implementación, no de fracaso. Según el buscador [S]: una revisión de 44 publicaciones concluye que el TPM es difícil de implementar (https://dx.doi.org/10.3926/ic.360, no abierta); una tesis de Elgharib (Birmingham) con cuestionario a 350 empresas del Reino Unido; otra de Guimaraes (Nottingham, 2004) sobre una firma japonesa en Malasia. Ninguna da una tasa de fracaso. Wikipedia (TPM) no recoge críticas ni adopción fuera de Japón. **Hueco:** no encontré evidencia leída de que el TPM «no funcione» fuera de Japón ni tasa de fracaso.

## 8. Afirmaciones no investigadas

- Mantener es conservar o devolver un equipo a la condición en que cumple su función: no investigué críticas. Es la definición clásica; la lista de eventos de NIST la usa para «Repair»: «Work required to restore an asset's intended function» (P10).
- Órdenes de trabajo planificadas y programadas: no investigué (hueco; faltan estudios sobre tiempo de llave, planificación y programación).
- Servicio de campo como el mismo ciclo: no investigué (hueco).
- Estrategia «dejar fallar»: solo la mención de Wikipedia (funciones no críticas pueden dejarse en run to failure, P4).

## Huecos resumidos

1. Texto original de Nowlan y Heap (1978): 403 en DTIC. Los porcentajes salen del extracto de Moubray (P2).
2. Guía de O&M del DOE (original): no leído.
3. Klutke 2003 (curva de bañera): no abierto.
4. Estudio primario de tasa de fracaso de implementaciones de CMMS o de RCM: no existe en lo leído; solo la encuesta de 2004 vía P13.
5. Porcentaje de códigos de falla mal cargados vs texto libre: sin cifras primarias (P8 y P9 solo abstract).
6. ISO 55000: sin estudio empírico leído.
7. TPM fuera de Japón: sin tasa ni estudio comparativo.
8. MTTR, disponibilidad, órdenes de trabajo, servicio de campo, definición de mantener: no investigados.
