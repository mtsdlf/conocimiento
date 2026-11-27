# Calidad (vertical de Producción): informe de investigación

Marcas: [L] texto leído (por el fetcher o extraído de PDF), [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1-3 en: autoridad / profundidad / ejemplos / unicidad.

Aviso de método: la herramienta de lectura devuelve resúmenes de la página y no citas largas; solo las dos normas extraídas de PDF (Reglamento 178/2002 y el Federal Register del QMSR) tienen texto literal verificado. Lo demás que figura entre comillas lo devolvió el lector, pero conviene recotejarlo antes de publicar.
Muchas fuentes primarias pagas o bloqueadas (ISO 9001, ISO 2859-1, ISO 22005, Juran, Montgomery) NO se pudieron leer: ver Huecos. Nada de eso se completó de memoria.

## 0. Hallazgos que cambian el borrador del tema

- ISO 9001:2015 no tiene cláusula de "acción preventiva". Confirmado solo con fuentes secundarias (ver 5); falta el texto del Anexo A.3 (hueco).
- La acción preventiva sigue viva en otros marcos: ISO 13485:2016 tiene la cláusula 8.5.3 (preventiva) separada de la 8.5.2 (correctiva), según el Federal Register 2024-01709.
- 21 CFR 820.100 (CAPA) deja de ser el texto vigente desde el 2 de febrero de 2026: el QMSR incorpora ISO 13485:2016 por referencia. Hoy es 2026-11-27, así que "QMSR 2026 si aplica" aplica, pero solo para dispositivos médicos.
- Hay indicios de una edición ISO 2859-1:2026 (tercera edición, enero 2026) y de una ISO 9001:2026 [S]. No verificado en ISO. Antes de citar "ISO 9001:2015" como vigente, chequear si hay edición nueva (hueco).
- División del árbol: el campo separa la calidad en control (SPC, muestreo), aseguramiento (sistema, ISO 9001) y mejora (CAPA). El árbol del brief las junta en una vertical, y sirve. La trazabilidad y el retiro de producto vienen de la inocuidad alimentaria y de los dispositivos médicos, no de la teoría de calidad; conviene decirlo en la nota.

## 1. Entrada: control, aseguramiento y gestión; Juran; costo de la calidad; ISO 9001

| Fuente | Tipo | Marca | Puntaje | Nota |
|---|---|---|---|---|
| ISO 9001:2015, https://www.iso.org/standard/62085.html | primaria | no accesible (403) | 3/3/2/3 | No leída |
| ISO OBP, https://www.iso.org/obp/ui/en/#iso:std:iso:9001:ed-5:v1:en | primaria | no accesible (403) | | No leída |
| iso-9001-checklist.co.uk, cláusula 8.7, https://www.iso-9001-checklist.co.uk/8.7-control-of-nonconforming-process-outputs-products-and-services.htm | secundaria | [S] | 1/2/1/1 | Resume 8.7; la página trata la edición 2026, no la 2015 |
| Búsquedas sobre 8.7 (isms.online, thecoresolution, etc.) | secundarias | [S] | 1/1/1/1 | Parafrasean la misma norma: cuentan como una sola fuente |

Afirmaciones (todas [S], sin texto de la norma):
- 8.7.1: las salidas no conformes se identifican y controlan para que no se usen ni entreguen por error ("the nonconforming output must be quickly identified and controlled so that it is not used or delivered by mistake", cita que da el lector del sitio checklist). Las respuestas son: corrección; segregación, contención, devolución o suspensión; informar al cliente; autorización de aceptación bajo concesión. Lo reprocesado se verifica contra los requisitos antes de liberar. 8.7.2: se conserva información documentada con la no conformidad, las acciones, las concesiones y la autoridad que decidió. URL arriba.
- Qué cláusulas tocan producción (8.5 producción y provisión del servicio, 8.5.2 identificación y trazabilidad, 8.6 liberación, 8.7, 10.2): sin evidencia directa leída. Solo 8.7 y 10.2 aparecen en fuentes secundarias.

Recurso canónico propuesto: ISO 9001:2015 (de pago); el texto de la norma se cita desde ISO y no desde terceros. Qué mirar: 8.5.2, 8.6, 8.7 y 10.2.

Hueco fuerte: Juran (trilogía de la calidad), las definiciones de control, aseguramiento y gestión (ISO 9000:2015) y el costo de la calidad no se investigaron: no se consiguió fuente primaria abierta en las rondas usadas.

Qué registra un sistema (nivel sistema de gestión): documento controlado y su revisión, no conformidades, acciones correctivas, auditorías. Sin evidencia de sistema abierto leída.

## 2. Plan de inspección, puntos de control y muestreo de aceptación

| Fuente | Tipo | Marca | Puntaje |
|---|---|---|---|
| Odoo 17, "Quality control points" (un sistema abierto), https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/quality/quality_management/quality_control_points.html | primaria de sistema | [L] | 2/2/2/2 |
| ERPNext, "Quality Inspection" (un sistema abierto), https://docs.frappe.io/erpnext/user/manual/en/quality-inspection | primaria de sistema | [L] | 2/2/2/2 |
| NIST/SEMATECH e-Handbook, "Lot Acceptance Sampling", https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc2.htm | primaria | [M] | 3/2/1/2 |
| ISO 2859-1: ficha ISO https://www.iso.org/standard/2859-1 y vista previa ANSI https://webstore.ansi.org/preview-pages/ISO/preview_ISO+2859-1-2026.pdf | primaria | no accesible (403) | |
| Resumen del buscador sobre ISO 2859-1 | secundaria | [S] | 1/1/1/1 |

Afirmaciones:
- Un sistema abierto (Odoo) modela el punto de control como configuración que dispara chequeos: "In the Type field, specify the type of quality check that should be performed." Tipos: instrucciones, foto, registrar producción, pasa/no pasa, medición, planilla. Se dispara por operación (fabricación, recepción), producto o categoría. La frecuencia puede ser todas las veces ("All"), un porcentaje al azar o un período. "Message If Failure" guía qué hacer al fallar (puede pedir una alerta de calidad). El punto no registra resultados.
- Un sistema abierto (ERPNext) registra una inspección con: tipo (entrante/compra, saliente/venta, en proceso/fabricación), documento de referencia (recibo de compra, tarjeta de trabajo), ítem, tamaño de muestra, plantilla de inspección tomada del maestro de ítem, lecturas (una fila por chequeo; si es numérico hay rango y la fila queda "Rejected" automáticamente al guardar si está fuera de rango; también hay chequeos no numéricos y por fórmula), inspector, verificador, observaciones y estado general. Con "Manual Inspection" el estado se fija a mano.
- NIST trata el muestreo de aceptación de lotes y lista "Choosing a Sampling Plan: MIL Standard 105D". En esa página no aparecen AQL ni ISO 2859.
- ISO 2859-1 [S, a verificar]: planes simples, dobles y múltiples indexados por AQL; tres niveles generales (I, II, III) y cuatro especiales (S-1 a S-4); nivel II por defecto; reglas de cambio entre inspección normal, rigurosa y reducida; tercera edición de enero de 2026. No se obtuvo ninguna tabla.

Recurso canónico propuesto: ISO 2859-1 (o ANSI/ASQ Z1.4) para la tabla; NIST cap. 6 para la teoría de la curva característica de operación. Qué mirar: letra código por tamaño de lote y nivel, luego AQL, y los criterios de cambio.

Hueco: no hay tabla literal pública (ni de 2859-1 ni de Z1.4). No armar una tabla de memoria. Alternativa no probada: MIL-STD-105E en un archivo del gobierno de EE. UU., con aviso de que está retirada.

Qué registra un sistema: plan por producto y operación (característica, tipo de chequeo, especificación o rango, método, frecuencia o porcentaje de muestreo); inspección (referencia, muestra, lecturas, resultado por línea, resultado global, quién).

## 3. Control estadístico de procesos y capacidad

| Fuente | Tipo | Marca | Puntaje |
|---|---|---|---|
| NIST 6.3.1, https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc31.htm | primaria | no leída (redirige a la portada) | |
| NIST 6.3.2 Shewhart, https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc32.htm | primaria | [L] | 3/2/2/2 |
| NIST 6.3.2.1 X-barra y R, https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc321.htm | primaria | [L] | 3/3/2/2 |
| NIST 6.3.3 y 6.3.3.2 (p), https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc33.htm y https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc332.htm | primaria | [L] | 3/2/1/2 |
| NIST 6.1.6 capacidad, https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm | primaria | [L] | 3/3/3/2 |

Afirmaciones:
- Modelo de Shewhart: la línea central está en la media del estadístico y los límites a k desvíos. "Historically, k = 3 has become an accepted standard in industry." Con proceso normal, un punto fuera de ±3σ ocurre cerca del 0,3% de las veces (pmc32).
- Reglas tipo Western Electric (pmc32, como las listó el lector): un punto más allá de 3σ; 2 de 3 más allá de 2σ del mismo lado; 4 de 5 más allá de 1σ del mismo lado; 8 seguidos del mismo lado de la línea central; tendencia de 6; alternancia de 14. Agregarlas sube las falsas alarmas de una cada 371 puntos a una cada 91,75. Recotejar los números con la página.
- X-barra: UCL = x̿ + A2·R̄; LCL = x̿ − A2·R̄; A2 = 3/(d2·√n). R: UCL = R̄·D4; LCL = R̄·D3; D3 = 1 − 3d3/d2, D4 = 1 + 3d3/d2 (pmc321).
- p: UCL = p + 3√(p(1−p)/n), LCL = p − 3√(p(1−p)/n); con p desconocido, p̄ = ΣDi/(mn) (pmc332).
- Capacidad: Cp = (USL − LSL)/(6σ); Cpk = min[(USL − μ)/(3σ), (μ − LSL)/(3σ)]; Cpm = (USL − LSL)/(6√(σ² + (μ − T)²)). Ejemplo NIST: USL = 20, LSL = 8, s = 2, media 16 (la página dice "≥ 16", parece errata): Cp = 1,0; Cpk = 0,6667 (Cpu = 0,6667, Cpl = 1,3333). "We would like to have Ĉpk at least 1.0, so this is not a good process." (pmc16).
- Causas comunes y especiales: no están en las páginas leídas (hueco).

Recurso canónico: NIST/SEMATECH e-Handbook, capítulo 6 (Process or Product Monitoring and Control), secciones 6.1.6 y 6.3. Para profundidad, Montgomery, Introduction to Statistical Quality Control (no leído).

Qué registra un sistema: característica medida, subgrupo (tamaño n, fecha y hora, lote u orden), valores, estadístico (media, rango, proporción), límites de control y regla violada, especificaciones (LSL, USL, objetivo), índice de capacidad. No hay evidencia de sistema abierto que haga gráficos de control: Odoo y ERPNext registran la medición, no el gráfico.

## 4. No conformidad y su disposición

Fuentes: ISO 9001 8.7 (sección 1, [S]) y lo de Odoo (sección 2).

Afirmaciones: las acciones de 8.7.1 y los registros de 8.7.2 están en la sección 1. Las disposiciones "reprocesar, reparar, usar como está, reclasificar, desechar" y el comité de revisión de material (MRB) NO tienen fuente leída. "Concesión" (concession) es término de ISO 9001 [S].

Qué registra un sistema: no conformidad (producto, lote u orden, cantidad, defecto, punto de detección, fecha), estado (abierta, retenida, en disposición, cerrada), disposición y quién la autorizó, concesión, costo. Sin evidencia de sistema abierto leída.

## 5. Acción correctiva, preventiva, CAPA, 8D

| Fuente | Tipo | Marca | Puntaje |
|---|---|---|---|
| 21 CFR 820.100, eCFR, https://www.ecfr.gov/api/versioner/v1/full/2026-01-01/title-21.xml?part=820&section=820.100 | primaria | [L] por el lector | 3/3/1/3 |
| FDA, Federal Register 2024-01709, "Medical Devices; Quality System Regulation Amendments", https://www.federalregister.gov/documents/2024/02/02/2024-01709/medical-devices-quality-system-regulation-amendments (texto extraído del PDF https://www.fda.gov/media/177022/download) | primaria | [L] | 3/3/1/3 |
| FDA, FAQ del QMSR, https://www.fda.gov/medical-devices/quality-management-system-regulation-qmsr/quality-management-system-regulation-frequently-asked-questions | primaria | [L] | 3/1/1/2 |
| Acción preventiva e ISO 9001 (BSI, Advisera, Quality Magazine, Ideagen; ISO/TC 176 N1284, https://www.slideshare.net/slideshow/iso9001-2015-andrisk/102654266) | secundarias | [S] | 1/1/1/1 |

Afirmaciones:
- 21 CFR 820.100, texto que mostró el lector (sin aviso de reemplazo): los procedimientos de CAPA cubren siete puntos. Análisis de procesos, quejas, producto devuelto y otros datos de calidad, con métodos estadísticos; investigación de la causa; identificación de la acción; verificación o validación de que la acción es eficaz y no perjudica al producto terminado; implementación y registro de los cambios; comunicación a los responsables; entrada a la revisión por la dirección. El apartado (b) exige documentar todo y sus resultados. Recotejar con el eCFR.
- QMSR: "This rule is effective February 2, 2026." (Federal Register 89 FR, p. 7496, DATES). FAQ de la FDA: "The rule became effective, February 2, 2026, two years after publication in the Federal Register." Incorpora ISO 13485:2016 por referencia.
- En el mismo Federal Register la FDA responde que ISO 13485 "has one Clause outlining expectations regarding corrective action (Clause 8.5.2) and has another Clause outlining the expectations regarding preventive action (Clause 8.5.3)". Y que 820.100(a)(6) y (7) (comunicar problemas y elevarlos a revisión por la dirección) no figuran en ISO 13485, pero su sustancia está cubierta por las cláusulas 8.2.2, 8.5.2 y 8.3.1.
- Acción preventiva en ISO 9001:2015 [S, confirmar con Anexo A.3]: Quality Magazine dice que la referencia a "preventive action" fue reemplazada por "actions to address risks and opportunities"; ISO/TC 176 dice que la acción preventiva queda incorporada cuando el sistema es basado en riesgo. Dos lecturas: "reemplazada" (BSI, Advisera) y "absorbida" (ISO/TC 176).
- 8D, 5 porqués, Ishikawa y el error de cerrar sin verificar eficacia: sin fuente leída. Lo verificado: la verificación de eficacia es un requisito explícito de 820.100(a)(4).

Recurso canónico: para producción general, ISO 9001:2015 cláusula 10.2 (de pago); para el patrón de siete pasos, 21 CFR 820.100 (abierto, histórico) más la FAQ del QMSR. Qué mirar: la verificación de eficacia y la entrada a la revisión por la dirección.

Qué registra un sistema (CAPA): origen (no conformidad, queja, auditoría), descripción, corrección inmediata, causa raíz y método, acción correctiva o preventiva, responsable, fecha límite, verificación de eficacia (fecha y resultado), estado y cierre. Sin evidencia de sistema abierto leída.

## 6. Trazabilidad de lotes (genealogía) y retiro

| Fuente | Tipo | Marca | Puntaje |
|---|---|---|---|
| Reglamento (CE) 178/2002, versión ES del DOCE L 31 de 1.2.2002, https://www.boe.es/doue/2002/031/L00001-00024.pdf | primaria | [L] (texto extraído del PDF) | 3/3/1/3 |
| AESAN, "Trazabilidad", https://www.aesan.gob.es/AECOSAN/web/seguridad_alimentaria/detalle/trazabilidad.htm | secundaria oficial | [L] | 2/1/1/1 |
| ISO 22005:2007, https://www.iso.org/standard/36297.html | primaria | ficha 403; datos del buscador [S] | 3/1/1/3 |
| Odoo y ERPNext: trazabilidad de lotes | | no investigado | |

Afirmaciones (literales del DOCE, salvo indicación):
- Art. 3.15: «Trazabilidad», la posibilidad de encontrar y seguir el rastro, a través de todas las etapas de producción, transformación y distribución, de un alimento, un pienso, un animal destinado a la producción de alimentos o una sustancia destinada a ser incorporada en un alimento o un pienso.
- Art. 18.1: "En todas las etapas de la producción, la transformación y la distribución deberá asegurarse la trazabilidad de los alimentos, los piensos, los animales destinados a la producción de alimentos y de cualquier otra sustancia destinada a ser incorporada en un alimento o un pienso, o con probabilidad de serlo."
- Art. 18.2: los explotadores "deberán poder identificar a cualquier persona que les haya suministrado un alimento, un pienso, un animal destinado a la producción de alimentos, o cualquier sustancia destinada a ser incorporada en un alimento o un pienso", con sistemas y procedimientos para ponerlo a disposición de las autoridades si lo piden.
- Art. 18.3: "deberán poner en práctica sistemas y procedimientos para identificar a las empresas a las que hayan suministrado sus productos."
- Art. 18.4: los productos "deberán estar adecuadamente etiquetados o identificados para facilitar su trazabilidad mediante documentación o información pertinentes".
- El texto NO pide genealogía interna (qué lote de ingrediente entró en qué lote de producto): exige identificar proveedor inmediato y cliente inmediato. La expresión "un paso atrás y un paso adelante" no está en el artículo; la usa la AESAN. AESAN: los explotadores "contarán con un sistema que les permita identificar a sus proveedores inmediatos y a sus clientes inmediatos", salvo cuando el cliente es consumidor final.
- Art. 19.1 (retiro): si el explotador considera o tiene motivos para pensar que un alimento que ha importado, producido, transformado, fabricado o distribuido no cumple los requisitos de seguridad, iniciará inmediatamente los procedimientos para retirarlo del mercado, informará a las autoridades y, si puede haber llegado al consumidor, lo informará y recuperará los productos. Parafraseado de una extracción de PDF parcialmente ilegible: recotejar.
- ISO 22005:2007 [S]: principios y requisitos mínimos para diseñar e implantar un sistema de trazabilidad en la cadena de piensos y alimentos; usa la misma definición que el Codex; confirmada en 2022.
- Dispositivos médicos: el Federal Register del QMSR trata la trazabilidad (p. ej. de implantables, 820.10(d)); no se leyó en detalle.

Recurso canónico: Reglamento 178/2002, arts. 3.15, 18 y 19 (abierto). Para la genealogía interna, ISO 22005 (de pago, sin leer). Qué mirar: 18.2 y 18.3 son el mínimo legal; la genealogía de fabricación es una decisión de diseño de la empresa.

Qué registra un sistema (genealogía): lote de producto (orden de producción, fecha, cantidad); lotes de componentes consumidos por orden (lote, proveedor, cantidad); lotes de salida; despachos a clientes por lote. Consultas hacia atrás (de un lote de producto a los lotes de componente y sus proveedores) y hacia adelante (de un lote de componente a los lotes de producto y a los clientes). Sin evidencia de sistema abierto leída.

## 7. Huecos (consolidado)

1. Texto de ISO 9001:2015 (8.5.2, 8.6, 8.7, 10.2 y Anexo A.3): bloqueado (403). Todo lo de la norma está en [S].
2. Si existe ISO 9001:2026 y qué cambia: no verificado; solo una pista indirecta.
3. Tabla literal de ISO 2859-1 o Z1.4 (letras código, tamaños, aceptación y rechazo, reglas de cambio): no obtenida.
4. Juran (trilogía), diferencias control, aseguramiento y gestión, costo de la calidad: sin fuente.
5. Causas comunes y especiales: no confirmadas en NIST (pmc31 no se pudo leer).
6. Disposición de no conformidad (reprocesar, reparar, MRB), 8D, 5 porqués, Ishikawa y el error de cierre sin eficacia: sin fuente.
7. ISO 22005 y Codex CAC/GL 60-2006: sin leer (403 y redirección a la portada).
8. Evidencia de un sistema abierto sobre no conformidad, CAPA y genealogía de lotes: no investigada.
9. Estado vigente exacto de la sección 820.100 tras el QMSR: el lector devolvió el texto sin aviso; falta confirmar si fue derogada o reemplazada en el CFR.
10. Art. 19 del Reglamento 178/2002: texto parcialmente ilegible en el PDF extraído.
