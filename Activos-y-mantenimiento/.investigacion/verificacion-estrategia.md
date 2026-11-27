# Verificación con fuentes, ángulo estrategia

Fecha: 2026-11-27. Notas: Estrategia-de-mantenimiento/ y Fundamentos/. Marcas: [L] leído en el original o en una copia fiel; [M] leído vía herramienta de resumen o ficha oficial sin el texto; [S] secundaria. El cupo de búsqueda web se agotó a mitad de la pasada; no se hicieron búsquedas más allá de las primeras.

## Nowlan y Heap (1978), DTIC ADA066579 [L]

- URL original (apps.dtic.mil/sti/pdfs/ADA066579.pdf y /citations/): 403 a curl con cualquier User-Agent. Copia que sí sirvió: https://web.archive.org/web/2020/https://apps.dtic.mil/sti/pdfs/ADA066579.pdf (PDF escaneado de 515 páginas, 26 MB; se extrajo con pdftotext y se miró la página 67 como imagen).
- Fecha: la hoja «Report Documentation Page» dice «December 29, 1978». Confirma la nota.
- Exhibit 2.13 (pág. 67 del PDF): seis curvas, A a F. Texto del cuerpo (sec. 2.8): «Some 89 percent of the items analyzed had no wearout zone; therefore their performance could not be improved by the imposition of an age limit... curves D, E, and F», «Another 5 percent had no well-defined wearout zone (curve C)», «Only 6 percent of the items studied showed pronounced wearout characteristics (curves A and B)», «just 4 percent of the items fell into this pattern (curve A)». En la figura: «11% might benefit from a limit on operating age» y «89% cannot benefit from a limit on operating age». Confirma 4, 6 (así B = 2), 5 y 89. El reparto D 7, E 14, F 68 no está escrito en el informe (la barra solo muestra proporciones): sale de Moubray y de la NASA.
- Rótulos de la figura: B «characteristic of aircraft reciprocating engines», C «characteristic of aircraft turbine engines», F «particularly applicable to electronic equipment». Los porcentajes son «United Airlines».
- «In fact, in many cases scheduled overhaul actually increases the overall failure rate by introducing a high infant-mortality rate in an otherwise stable system» y «unless there is a dominant failure mode, an age limit does little or nothing to improve the overall reliability of a complex item». Confirma la atribución de la NASA.
- Lógica de decisión (sec. 1.2, 2.2, 2.4, cap. 3): cuatro categorías de consecuencia (seguridad, operativas, no operativas, falla oculta); cuatro tareas (inspección para fallas potenciales, reparación a edad límite, descarte a vida límite, inspección de función oculta para fallas funcionales); aplicabilidad y efectividad; respuestas por defecto en el diagrama de decisión; exploración de edad. Definiciones literales de falla funcional («the inability of an item (or the equipment containing it) to meet a specified performance standard»), falla potencial («an identifiable physical condition which indicates a functional failure is imminent») y función oculta. Tres criterios de aplicabilidad de la tarea a condición (sec. 3.1; el tercero, un intervalo de edad razonablemente consistente entre la falla potencial y la funcional, sale cortado en el OCR). Tarea de búsqueda de fallas (sec. 3.4): «scheduled inspection of a hidden-function item to find any functional failures» (el OCR del resumen de la sec. 3 la rompe; el texto de la 3.4 dice «scheduled inspections for hidden failures»). Cierra el NOTE de la lógica de decisión y el de fallas ocultas.
- «P-F»: la sigla no aparece en el informe.

## NASA RCM Guide (febrero de 2000) [L]

- Releída. Fig. 2-4: UAL 1968 / «BROMBERG 1973» / U.S. Navy 1982 = tipo E (bañera) 4/3/3, A 2/1/17, F 5/4/3, C 7/11/6, D 14/15/42, B 68/66/29. Confirma la tabla de la nota. El texto dice «U.S. Navy in 1983». Letras de la NASA: A motores alternativos, E bañera, F turbinas.
- PNNL (https://www.pnnl.gov/projects/om-best-practices/advanced-maintenance-approach-reliability-centered-maintenance) [M]: titula las columnas «Nowlan 1978, Broberg 1973, MSDP 1993» y cita «Broberg, Broberg's report 1973. Cited in Failure Diagnosis & Performance Monitoring, Vol. 11 edited by LF Pau, Marcel-Dekker, 1981». Entonces «Broberg» es la grafía de la nota; la NASA escribe «Bromberg». Año del estudio de la Marina, 1982 (NASA, figura), 1983 (NASA, texto) o 1993 (PNNL): sin resolver.

## SAE JA1011 [M]

- Ficha oficial (copia de la Wayback Machine, https://web.archive.org/web/2023/https://www.sae.org/standards/content/ja1011_200908/; sae.org en vivo no carga sin JavaScript): «JA1011_200908 Current REVISED 2009-08-26»; «JA1011_199908 1999-08-01 Historical Issued»; 12 páginas; «This SAE Standard for Reliability Centered Maintenance (RCM) is intended for use by any organization that has or makes use of physical assets or systems that it wishes to manage responsibly»; rationale de 2009: «The overall technical process remains unchanged». Corrige a Wikipedia (1 de agosto de 1998): la primera edición es de 1999.
- Las siete preguntas: Moubray, «The Case Against Streamlined RCM», https://reliabilityweb.com/articles/entry/the_case_against_streamlined_reliability_centered_maintanance, leído vía herramienta de resumen, cita la sec. 5 de JA1011: «What are the functions and associated desired standards of performance of the asset in its present operating context»; «In what ways can it fail to fulfil its functions (functional failures)?»; «What causes each functional failure (failure modes)?»; «What happens when each failure occurs (failure effects)?»; «In what way does each failure matter (failure consequences)?»; «What should be done to predict or prevent each failure (proactive tasks and task intervals)?»; «What should be done if a suitable proactive task cannot be found (default actions)?». La paráfrasis de Wikipedia de la nota era aproximada (la 6 no menciona «prevent or diminish consequences»; hay que ver el texto con cuidado). Cita también «This standard presents criteria against which a process may be compared» y «Leaving things out inevitably increases risk»; atribuye lo de «about half to a third of the time» a los defensores del RCM abreviado.
- Texto completo de la norma: pago, no leído.

## EN 13306 [sin verificar]

- Ficha del organismo checo (https://www.en-standard.eu/csn-en-13306-maintenance-maintenance-terminology/) [M]: edición de 2018, 98 páginas, alcance: «specifies generic terms and definitions for the technical, administrative and managerial areas of maintenance». Sin definiciones. iteh, aenor y sis: no cargaron o dieron 403/404.
- Wikipedia, Corrective maintenance [S]: cita NF EN 13306 X 60-319 (AFNOR, junio de 2010) para «carried out after failure detection»; las frases de inmediato y diferido son de Wikipedia y no tienen cita en línea a la norma. Wikipedia, Predictive maintenance [S]: lo trata como «condition-based maintenance carried out as suggested by estimations of the degradation state of an item» y no cita EN 13306. Sigue abierto: definiciones literales de la norma; la base trata predictivo como sinónimo de por condición, pero esa frase de Wikipedia sugiere que es un caso de por condición (la nota ya lo dice).

## ISO 55000 [M]

- Ficha ISO 55000:2014 (Wayback, https://web.archive.org/web/2024/https://www.iso.org/standard/55088.html): «Edition 1 2014-01 Withdrawn... New version available: ISO 55000:2024». Ficha ISO 55000:2024 (Wayback, https://web.archive.org/web/2025/https://www.iso.org/standard/83053.html): «Asset management — Vocabulary, overview and principles», Edition 2, 2024-07. Las notas hablaban solo de 2014: corregido. OBP (iso.org/obp) y iso.org en vivo: 403.
- IAM, https://theiam.org/what-is-asset-management/ [M]: «Asset management: the coordinated activity of an organisation to realize value from assets. (ISO 55000, 2014, 3.3.1)»; «An asset is an item, thing or entity that has potential or actual value to an organisation (ISO 55000, 2014, 3.2.1)». Confirma la definición de activo que antes venía de Wikipedia. Las definiciones de la edición 2024 no se leyeron.
- IAM, https://theiam.org/knowledge/ [M]: 39 materias agrupadas en seis grupos; las describen «Asset Management — an anatomy» y The Asset Management Landscape de GFMAM.
- Para Registro-de-activos (no tocada): su fuente es Wikipedia, ISO 55000 (resumen secundario), y no menciona que la edición de 2014 está retirada.

## Moubray, generaciones y patrones [M]

- Extracto del capítulo 1 de RCM II en http://www.plant-maintenance.com/RCM-intro.shtml: «Since the 1930's, the evolution of maintenance can be traced through three generations»; primera hasta la Segunda Guerra Mundial («downtime did not matter much»); segunda hasta los sesenta («equipment overhauls done at fixed intervals»); tercera desde mediados de los setenta. Figura 1.5: «4% of the items conformed to pattern A, 2% to B, 5% to C, 7% to D, 14% to E and no fewer than 68% to pattern F»; «The number of times these patterns occur in aircraft is not necessarily the same as in industry». El libro no se abrió.

## Curva P-F

- Nowlan y Heap fundan falla potencial y falla funcional con las definiciones literales de arriba y el criterio del intervalo consistente; no usan la sigla. La regla de inspeccionar a la mitad del intervalo no está en N&H y sigue sin fuente primaria (Moubray no se abrió).

## PAS 55 [S]

- Wikipedia, PAS 55: BSI, 2004, bajo el liderazgo del IAM; PAS 55:2008 en diciembre de 2008; predecesora de la serie ISO 55000. La página de la BSI (knowledge.bsigroup.com) dio «Product not found».

## TPM [S]

- Wikipedia, Total productive maintenance: Nakajima 1950 a 1970, aplicación en 1971, Nippondenso primera ganadora del premio PM, ocho pilares (con inconsistencias de nombre entre el encabezado y la sección). Sus fuentes son una página web sin año y un artículo de plant-maintenance.com. JIPM: las páginas probadas dieron 404. Ireland y Dale (Emerald): el abstract dice «a study of total productive maintenance (TPM) in three companies» y «Nakajima's seven steps of autonomous maintenance»; no define ni da la historia del TPM. Sigue abierto: una fuente de JIPM o Nakajima.

## DOE FEMP, O&M Best Practices Guide, cap. 5 [L]

- PDF bajado de https://www1.eere.energy.gov/femp/pdfs/OM_5.pdf y leído. Confirmadas las cifras literales: «Estimated 12% to 18% cost savings over reactive», «Estimated 8% to 12% cost savings over preventive», «independent surveys indicate the following savings: Return on investment: 10 times; Reduction in maintenance costs: 25% to 30%; Elimination of breakdowns: 70% to 75%; Reduction in downtime: 35% to 45%; Increase in production: 20% to 25%»; «Studies as recent as the winter of 2000... >55% Reactive» (la guía no cita los estudios); aceite de 3,000 a 5,000 millas, extendido a 10,000; desventajas citadas. Sin cambios en la nota.

## Sin resolver

- EN 13306: definiciones literales (inmediato, diferido, preventivo, por condición, predictivo).
- Letras y años de los tres estudios de la NASA: la fecha del estudio de la Marina.
- TPM: fuente primaria o de JIPM; historia 1971.
- PAS 55: página de la BSI.
- FMEA (MIL-P-1629, 1949; ARP926; manual AIAG/VDA de 2019) y Klutke, Kiessler y Wortman (2003): no se intentaron en esta pasada; siguen como estaban.
- Oxmaint y AvWeb sobre otros repartos del 89 %: sin leer.
