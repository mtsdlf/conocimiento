# Informe de investigación: Planillas de cálculo (Excel y Google Sheets)

Fecha de las lecturas: 2026-11-27. Marcas: [L] leído completo o en la parte útil, [M] solo metadatos, [S] resumen secundario o del buscador. Puntajes A/P/E/U = autoridad/profundidad/ejemplos/unicidad (1 a 3). No escribí archivos; los PDF que bajé al directorio temporal los leí con `pdftotext`.

## Resumen para quien escribe las notas

1. **La cifra "88 % de las planillas tienen errores" no tiene fuente rastreable.** Lo que Panko mide de verdad son dos cosas distintas:
   - El porcentaje de planillas con al menos un error en auditorías intensivas (94 % en 85 planillas, o 91 % en 54, según la edición). Son muestras chicas y sesgadas.
   - La tasa de error por celda (CER, la proporción de celdas con fórmula que tienen un error original), de 0,4 % a 5 %.
   El detalle está en el componente 1.
2. **Dato vigente que cambió: Google Sheets ahora admite 20 millones de celdas, no 10.** Lo anunció Google el 2026-09-10. La ayuda oficial de límites de Drive también dice 20 millones. Con 10 millones se corre el riesgo de dejar una nota desactualizada.
3. **LibreOffice vigente: 26.8.3.** La página de descarga lo dice y también lista la 26.2.7. Hay una 27.2 alpha que no es estable.
4. **Sobre la división del árbol:**
   - "Automatización" junta tres cosas que el campo trata por separado: macros de Excel, Apps Script y compartir y colaborar. Esta última no es automatización. Es un tema de gobernanza que cruza ambas aplicaciones, y conviene sacarla como componente propio, "Compartir y colaborar".
   - "Revisar una planilla" (herramientas y pares) funciona mejor como componente separado de "Errores". Casi toda la bibliografía de práctica las separa: una dice cómo falla, la otra cómo se atrapa.
   - La ficha de aplicaciones y el puente "cuándo pasar a una base de datos" comparten los límites duros. Conviene que los números vivan en la ficha y el puente los enlace.

---

## Componente 1. Diseño de planillas y errores

### Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 1 | ICAEW, *Financial Modelling Code* (2018, edición 2024) | https://www.icaew.com/-/media/corporate/files/technical/technology/excel-community/financial-modelling-code.ashx | primaria (estándar profesional) | 3/3/2/3 | [L] |
| 2 | FAST Standard Organisation, página del estándar | https://www.fast-standard.org/the-fast-standard/ | primaria | 3/1/1/3 | [L] solo la web. El PDF de reglas no lo abrí |
| 3 | Panko, "Spreadsheet Errors: What We Know. What We Think We Can Do" (EuSpRIG, jul. 2000) | https://arxiv.org/pdf/0802.3457 | primaria (académica) | 3/3/3/3 | [L] |
| 4 | Panko, "What We Don't Know About Spreadsheet Errors Today" (EuSpRIG 2015) | https://arxiv.org/pdf/1602.02601 | primaria | 3/3/3/2 | [L] |
| 5 | Panko y Ordway, "Sarbanes-Oxley: What About all the Spreadsheets?" | https://arxiv.org/abs/0804.0797 | primaria | 2/2/1/1 | [M] |
| 6 | EuSpRIG, lista de horror stories | https://eusprig.org/research-info/horror-stories/ | primaria (compilación) | 3/2/3/3 | [M]. Respondió 403, solo vi espejos y reseñas |
| 7 | Ziemann, Eren y El-Osta, Genome Biology 2016 | https://link.springer.com/10.1186/s13059-016-1044-7 | primaria | 3/2/3/3 | [S]. El texto pidió autenticación |
| 8 | Tweedie et al., *Genenames.org: the HGNC and VGNC resources in 2021*, NAR | https://pmc.ncbi.nlm.nih.gov/articles/PMC7779007 | primaria | 3/2/2/3 | [L] |
| 9 | The Register, "Excel England coronavirus contact error" (2020-10-05) | https://www.theregister.com/2020/10/05/excel_england_coronavirus_contact_error/ | secundaria (prensa técnica) | 2/2/2/2 | [L] |
| 10 | PHE, comunicado oficial | https://gov.uk/government/news/phe-statement-on-delayed-reporting-of-covid-19-cases | primaria | 3/1/1/3 | [S] |
| 11 | Senado de EE. UU. (PSI), *JPMorgan Chase Whale Trades: A Case History of Derivatives Risks and Abuses* (2013-03-15) | https://www.hsgac.senate.gov/wp-content/uploads/imo/media/doc/REPORT%20-%20JPMorgan%20Chase%20Whale%20Trades%20%283-15-13%29.pdf | primaria | 3/3/3/3 | [M]. La descarga no devolvió un PDF válido |
| 12 | AccountingWeb, comentario sobre el informe de la tarea | https://www.accountingweb.co.uk/node/114050 | secundaria | 1/1/2/1 | [S]. Respondió 403 |
| 13 | Herndon, Ash y Pollin (2013), reseñas | https://retractionwatch.com/2013/04/18/influential-reinhart-rogoff-economics-paper-suffers-database-error/ y https://rogoff.scholars.harvard.edu/resource/faq | secundaria / primaria de la parte acusada | 2/2/2/2 | [S] |
| 14 | Microsoft, relaciones entre fórmulas y celdas (Rastrear precedentes y dependientes) | https://support.microsoft.com/en-us/office/display-the-relationships-between-formulas-and-cells-a59bef2b-3701-46bf-8ff1-d3518771d507 | primaria | 3/2/1/2 | [S] |
| 15 | Microsoft, Spreadsheet Inquire (Análisis de libro, Compare Files) | https://support.microsoft.com/en-us/office/analyze-a-workbook-with-spreadsheet-inquire-5991e8fa-f1c1-401a-ae3f-469384ae3e3b | primaria | 3/2/1/2 | [S] |

Recencia: el ICAEW Code lleva © 2024 en el pie. La versión de FAST que enlaza la web es "02c, julio 2019", y eso lo infiero del nombre del archivo.

### Afirmaciones

**Estructura entradas, cálculos y salidas**
- El ICAEW Code pide "Segregate inputs (assumptions), calculations and outputs (results)", y que la lógica fluya de las entradas a las salidas. Principio #9. https://www.icaew.com/-/media/corporate/files/technical/technology/excel-community/financial-modelling-code.ashx
- El Code admite una excepción: un tablero puede contener entradas, aunque eso "contradice" la práctica de agruparlas, si la entrada está "very clearly identified". La misma fuente.
- Una ubicación única por cada valor de entrada (principio #15, evitar duplicación). La misma fuente.
- Distinguir las celdas de entrada con color de relleno definido. No identificarlas solo con una etiqueta de texto. La misma fuente.
- Fórmulas consistentes (principio #12): "Make formulas strictly consistent across formula blocks, so the formula can be copied and pasted across the block", y usar anclaje de celdas (`$`) o nombres para las variaciones. Esta es la formulación oficial de "una fórmula por fila/columna". La misma fuente.
- Evitar números fijos en fórmulas (principio #14). Definición literal: "Fixed values embedded into a formula, such as a tax rate entered as 20% within a formula". El Code admite excepciones de bajo riesgo, como 24 horas en un día, y lo prohíbe para valores que puedan cambiar en la vida del modelo. La misma fuente.
- FAST significa "Flexible, Appropriate, Structured & Transparent". La web insiste en "Rigorous consistency in layout and organisation" y en "simple, clear formulas". https://www.fast-standard.org/the-fast-standard/
- Las reglas concretas de FAST (flujo de izquierda a derecha y de arriba abajo, etc.) están en el PDF, que no leí. No afirmo ninguna por FAST. Sí verifiqué el principio equivalente en ICAEW: lógica "from inputs to outputs", pero sin citar "izquierda a derecha" textual. Ver huecos.

**Cuánto fallan las planillas (Panko)**
- Auditorías de campo de 2000: errores en 24 % de 367 planillas, pero ese total mezcla los estudios viejos (Davies e Ikin 1987: 21 % de 19; Butler 1992: 11 % de 273) con los más nuevos. Los estudios de 1997 en adelante: 91 % de 54 planillas (Coopers & Lybrand 1997: 91 % de 23; KPMG 1997: 91 % de 22; Butler 2000: 86 % de 7). https://arxiv.org/pdf/0802.3457
- Cell error rate (CER) en esas auditorías: 1,2 %, 2,2 % y 2,5 %, y 0,38 % para las celdas con fórmula en Butler. La misma fuente.
- En 2015 Panko resume "85 intensive inspection studies" con "94 %" de planillas con errores. Son 85 planillas, no estudios, en 6 trabajos de inspección intensiva (Hicks 1995, Coopers & Lybrand 1997, KPMG 1998, Lukasic 1998, Butler 2000, Lawrence y Lee 2001, que aporta 30 planillas con 100 %). La mayoría eran auditorías comerciales de varios días por planilla. https://arxiv.org/pdf/1602.02601
- El mismo texto dice que el promedio de CER de experimentos de laboratorio es 3,9 %, y esperable de 1 % a 5 % "based on human error research". La misma fuente.
- Experimentos de laboratorio (2000): 51 % de 1.170 planillas de 998 sujetos tenían errores, con planillas de 25 a 50 celdas. https://arxiv.org/pdf/0802.3457
- Panko calcula que con una CER de 1 % a 5 % la probabilidad de un error en el resultado final es muy alta en una planilla grande. Esto se ve en su Figura 1, que no reproduzco. https://arxiv.org/pdf/1602.02601
- Tipos de error, según Panko y Halverson: lógicos, mecánicos (apuntar a la celda equivocada, tipear mal) y de omisión. En un experimento: 45 % lógicos, 23 % mecánicos y 31 % omisión. En otro: 44 %, 3 % y 53 %, y Panko dice que ese 53 % fue "an anomaly of the task statement wording". Los de omisión son los más difíciles de detectar. https://arxiv.org/pdf/1602.02601
- Detección: en inspección de código por celda, el 90 % de los errores es el techo que alcanzan las revisiones. En el experimento de Galletta y colegas, de 14 errores ninguno se detectó por completo: tres tuvieron detección menor a 10 % y la mitad menor a 40 %. La misma fuente.
- Sobreconfianza: la estimación mediana de los propios desarrolladores fue 10 % de error, y la media 18 %, mientras que 86 % de sus planillas tenían errores. https://arxiv.org/pdf/0802.3457
- Panko también cita: "only one technique, cell-by-cell code inspection, has been demonstrated to be effective" (2000). La misma fuente.

**Sobre la cifra "88 %" y similares**
- No encontré a Panko dando "88 %". Las cifras suyas son 24 %, 86 %, 91 % y 94 %. Una de las citas de segunda mano (un artículo de Built In) dice "it was estimated that 88 percent of existing spreadsheets contain errors", sin fuente. Otra dice "80 % a 90 %" atribuido a Panko [2000]. En esa figura la fuente original más cercana es la tabla de 2000. Búsqueda: https://builtin.com/data-science/spreadsheet-cleaning [S].
- Qué miden de verdad: el 91 % o 94 % es un porcentaje de planillas con al menos un error, calculado sobre planillas que alguien eligió auditar, y los auditores son firmas comerciales que cobran por encontrar errores. No es una tasa de la población de planillas. La CER es otra magnitud, por celda con fórmula. Ambas son, en rigor, medidas sobre muestras no aleatorias.
- Hay otra discrepancia entre ediciones. El 24 % de 367 de la edición 2000 mezcla auditorías antiguas con otras más rigurosas. La edición 2015 solo agrega inspecciones intensivas, y por eso da 94 %. Las dos cifras son verdad para su propia muestra, y no se pueden comparar entre sí.

**Casos documentados**
- Genes como fechas: Ziemann et al. revisaron 35.175 archivos Excel suplementarios de 18 revistas, 2005 a 2015. Había 7.467 listas de genes en 3.597 artículos, y el 19,6 % de esos artículos con listas de genes tenía errores. En BMC Bioinformatics fue 13,8 %. Es un porcentaje de artículos que tienen listas de genes en Excel, no de todos los artículos. Un seguimiento posterior (2014 a 2020) da 30,9 % (3.436/11.117). https://link.springer.com/10.1186/s13059-016-1044-7 [S]; seguimiento: https://pmc.ncbi.nlm.nih.gov/articles/PMC8357140 [S].
- HGNC: renombró MARCH# a MARCHF#, MARC# a MTARC#, SEPT# a SEPTIN# y DEC1 a DELEC1 porque se "auto-converted to dates when entered in Microsoft Excel". Concluyeron que pedir a los usuarios cambiar su configuración de Excel "no resolvería" el problema. https://pmc.ncbi.nlm.nih.gov/articles/PMC7779007. La cifra de "27 genes" renombrados viene solo de prensa [S] (por ejemplo https://theprint.in/science/27-genes-in-your-body-now-have-a-new-name-because-microsoft-excel-confused-them-for-dates/477398). El artículo de NAR no da total.
- Public Health England: faltaron 15.841 casos del 25 de septiembre al 2 de octubre de 2020, por un fallo en la carga de datos. https://gov.uk/government/news/phe-statement-on-delayed-reporting-of-covid-19-cases [S]. Según The Register, los resultados de los laboratorios se guardaban en formato .XLS antiguo, con tope de 65.536 filas por hoja, y cada resultado ocupaba varias filas, por lo que cada hoja contenía unos 1.400 casos (cita la BBC). Se perdió lo que excedía el tope. Hasta 48.000 contactos podrían no haber sido avisados. https://www.theregister.com/2020/10/05/excel_england_coronavirus_contact_error/
  - Discrepancia: el comunicado oficial, en lo que vi, no nombra el formato XLS. La atribución al XLS viene de la prensa y del propio gobierno en declaraciones posteriores ("file size"). La estimación de Warwick (más de 125.000 infecciones adicionales y 1.500 muertes) es modelada, no medida. https://uk.news.yahoo.com/data-glitch-may-led-more-161147064.html [S].
- Reinhart-Rogoff: la planilla dejó fuera Australia, Austria, Bélgica, Canadá y Dinamarca de los promedios (el rango se cortaba en la fila 44 en vez de la 49), lo que explica un error de -0,3 puntos porcentuales. Con deuda mayor al 90 % del PIB, Herndon, Ash y Pollin obtienen un crecimiento promedio de 2,2 %, no -0,1 %. Rogoff dice que el error tuvo "relatively limited impact". Hay dos lecturas: HAP lo presenta como un cambio mayor, los autores originales como menor. Y HAP además señala exclusión de datos y métodos de promedio. https://retractionwatch.com/2013/04/18/influential-reinhart-rogoff-economics-paper-suffers-database-error/ y https://rogoff.scholars.harvard.edu/resource/faq [S]. No pude confirmar el "-0,1" original en una fuente primaria.
- JPMorgan, ballena de Londres: el informe de la tarea interna del banco dice que, tras restar la tasa vieja de la nueva, la planilla dividía por la suma en vez del promedio. Se interpreta como que reducía la volatilidad a la mitad. La construcción del modelo, a mano con copiar y pegar, la describe una revisión interna como "error prone" y "not easily scalable". Al volver al modelo anterior, el VaR casi se duplicó a US$129 millones. Todo esto lo tengo de secundarias y de la prensa: https://www.accountingweb.co.uk/node/114050 y https://www.ifre.com/story/1744757/derivatives-jpm-report-unveils-var-errors [S]. El informe del Senado existe (15 de marzo de 2013) pero no pude leer su texto. Cuidado: se lo conoce como "informe de la tarea" pero en rigor son dos documentos distintos, el del banco (Task Force, enero de 2013) y el del Senado (marzo de 2013).
- EuSpRIG mantiene su lista de horror stories desde 1995, con un conteo de 89 en 2007. Es un sesgo conocido: solo cubre errores que se hicieron públicos. Espejo: https://gwern.net/docs/www/www.eusprig.org/555459cfaaf7089b983c09784a489eb2a1e00263.html [S].

**Revisar una planilla**
- Rastrear precedentes y dependientes (pestaña Fórmulas, grupo Auditoría): las flechas son azules para celdas sin error y rojas para las que causan error. No rastrea cuadros de texto, gráficos incrustados, imágenes, tablas dinámicas ni constantes con nombre. https://support.microsoft.com/en-us/office/display-the-relationships-between-formulas-and-cells-a59bef2b-3701-46bf-8ff1-d3518771d507 [S]
- Comprobación de errores y referencias circulares (Fórmulas, Comprobación de errores, Referencias circulares). https://support.microsoft.com/en-us/office/remove-or-allow-a-circular-reference-8540bd0f-6e97-4483-bcf7-1b49cd50d123 [S]
- Spreadsheet Inquire: solo en Excel para Windows, en Microsoft 365 Apps para empresas y ediciones equivalentes. Tiene Análisis de libro, Compare Files (celda por celda, con colores, y hasta cambios de VBA) y diagramas de relación entre hojas y libros. Se habilita en Opciones, Complementos, Complementos COM. https://support.microsoft.com/en-us/office/analyze-a-workbook-with-spreadsheet-inquire-5991e8fa-f1c1-401a-ae3f-469384ae3e3b [S]
- Mostrar fórmulas y Evaluar fórmula: no verifiqué su página oficial (la búsqueda no las devolvió). Ver huecos.
- ICAEW sobre revisión: principio #17 "Include checks" (indicadores visibles cuando una entrada o salida cae fuera de lo esperado) y #18 "Review and test your models" (cambiar entradas y comparar salidas). Es la base de las pruebas de cuadre. https://www.icaew.com/-/media/corporate/files/technical/technology/excel-community/financial-modelling-code.ashx
- Revisión por pares: Panko sostiene que lo único probado es la inspección celda por celda con más de una persona, y que los equipos de dos o cuatro cometen menos errores que individuos (CER 5,6 % solos, 3,8 % en díadas, 1,9 % en tétradas). https://arxiv.org/pdf/0802.3457 (tabla de laboratorio). Son estudiantes en tareas de 25 a 50 celdas.

### Recurso canónico
- **Diseño:** ICAEW *Financial Modelling Code* (20 principios, gratuito, vigente 2024) como referencia principal, con FAST como segunda opción. Tiene el defecto de estar escrito para modelos financieros, y hay que adaptarlo a un negocio chico.
- **Errores:** Panko 2015 (https://arxiv.org/pdf/1602.02601), por ser la edición más reciente y por explicar qué mide cada cifra. Complementar con la lista de EuSpRIG para los casos.
- **Revisión:** las páginas de Microsoft de auditoría de fórmulas, más ICAEW #17 y #18.

---

## Componente 2. Automatización (y compartir y colaborar)

### Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 16 | Microsoft Learn, "Macros from the internet are blocked by default in Office" (actualizada 2026-07-17) | https://learn.microsoft.com/en-us/microsoft-365-apps/security/internet-macros-blocked | primaria | 3/3/2/3 | [L] |
| 17 | Microsoft Learn, "Office Scripts in Excel" (2026-02-26) | https://learn.microsoft.com/en-us/office/dev/scripts/overview/excel | primaria | 3/2/2/3 | [L] |
| 18 | Google, Apps Script: funciones personalizadas | https://developers.google.com/apps-script/guides/sheets/functions | primaria | 3/3/2/3 | [L] |
| 19 | Google, Apps Script: disparadores | https://developers.google.com/apps-script/guides/triggers | primaria | 3/2/1/3 | [L] |
| 20 | Google, Apps Script: cuotas | https://developers.google.com/apps-script/guides/services/quotas | primaria | 3/2/1/3 | [L] |
| 21 | Microsoft, coautoría en Excel | https://support.microsoft.com/en-us/excel/get-started/collaborate-on-excel-workbooks-at-the-same-time-with-co-authoring | primaria | 3/2/1/2 | [S]. La URL con el ID del artículo dio 403 |
| 22 | Google, proteger rangos y hojas | https://support.google.com/docs/answer/1218656 | primaria | 3/2/1/3 | [L] |
| 23 | Google, historial de versiones | https://support.google.com/docs/answer/190843 | primaria | 3/2/1/2 | [S] |

### Afirmaciones

**Macros (VBA)**
- Microsoft cambió el comportamiento por defecto para bloquear macros de archivos de internet: "VBA macros are a common way for malicious actors to gain access to deploy malware and ransomware". Se empezó a desplegar el 2022-04-12 (Current Channel Preview, v2203) y el 2022-07-27 (Current Channel, v2206). Para el canal semestral empresarial, el 2023-01-10. https://learn.microsoft.com/en-us/microsoft-365-apps/security/internet-macros-blocked
- Alcance: solo Office en Windows. "The change doesn't affect Office on a Mac, Office on Android or iOS devices, or Office on the web." La misma fuente. Esto corrige la frase "Microsoft bloquea macros de Internet desde 2022": es Windows, y las versiones perpetuas como LTSC 2021 u Office 2019 conservan su paso previo para documentos de confianza.
- Mecanismo: la marca de la web (Mark of the Web, MOTW) que Windows agrega a archivos descargados o adjuntos. El usuario ve el banner "Security Risk" y no tiene botón "Habilitar contenido". Para desbloquear, se marca "Desbloquear" en Propiedades, pestaña General, o se usa `Unblock-File` en PowerShell. La misma fuente.
- Los archivos abiertos con "Abrir en la aplicación de escritorio" desde OneDrive o SharePoint no llevan MOTW. La misma fuente.
- Las políticas de administrador solo están disponibles en Microsoft 365 Apps for enterprise, no en Apps for business. La misma fuente.
- Excel en la web no ejecuta VBA (se deduce de que el cambio no afecta a Office en la web, pero no leí una afirmación directa de que no lo soporte). Ver huecos.

**Office Scripts y Power Automate**
- Office Scripts: grabadora de acciones y editor de código para automatizar Excel. Se comparten asociándolos al libro, y se pueden poner botones. Los scripts se guardan en OneDrive. https://learn.microsoft.com/en-us/office/dev/scripts/overview/excel
- El lenguaje (TypeScript) y los requisitos de licencia y plataforma no aparecen en la página que leí. Los doy como dato por confirmar.
- Programar scripts: "Script scheduling is temporarily disabled within Office Scripts. Existing scheduled scripts will continue to run". Mientras tanto se recomienda crear un flujo en Power Automate. La misma fuente.
- Power Automate conecta scripts con eventos (por ejemplo, correos). La misma fuente. Su precio no lo verifiqué.

**Apps Script**
- Funciones personalizadas: JavaScript desde Extensiones, Apps Script, con la etiqueta `@customfunction`. "A custom function call must return within 30 seconds." Si no, la celda muestra `#ERROR!`. No pueden usar servicios que requieren autorización, ni modificar otras celdas. https://developers.google.com/apps-script/guides/sheets/functions
- Cada celda con función personalizada hace una llamada al servidor, por lo que para rangos grandes conviene recibir y devolver arreglos 2D. La misma fuente.
- Disparadores simples (`onOpen`, `onEdit`, etc.): no pueden correr más de 30 segundos, no usan servicios con autorización (como Gmail) ni abren otros archivos, y no se activan si el archivo está en modo solo ver o comentar. Los instalables requieren activarse y soportan evento de tiempo, edición, envío de formulario. `onEdit()` encola hasta 2 eventos. https://developers.google.com/apps-script/guides/triggers
- Cuotas (según la tabla): tiempo de ejecución por script 6 min por ejecución en ambas cuentas. Tiempo total de disparadores por día: 90 min en cuentas de consumo, 6 horas en Google Workspace. Función personalizada: 30 s. Destinatarios de correo por día: 100 en consumo, 1.500 en Workspace (la tabla tiene un asterisco cuyo texto no pude ver). https://developers.google.com/apps-script/guides/services/quotas

**Compartir y colaborar**
- Coautoría en Excel: requiere guardar en OneDrive, OneDrive para la Empresa o una biblioteca de SharePoint Online, y cada persona necesita una suscripción de Microsoft 365 y la última versión de Excel. Formatos .xlsx, .xlsm o .xlsb. No admite el formato Strict Open XML. SharePoint local no la admite. AutoSave debe estar activado para que todos vean los cambios y las selecciones en color. No funciona con archivos protegidos con IRM/RMS. Editar macros durante la coautoría puede interrumpir a otros. https://support.microsoft.com/en-us/excel/get-started/collaborate-on-excel-workbooks-at-the-same-time-with-co-authoring [S]
- Hasta 256 usuarios pueden abrir a la vez un libro compartido (ficha de límites de Excel). https://support.microsoft.com/en-us/office/excel-specifications-and-limits-1672b34d-7043-467e-8e27-269d656771c3
- Sheets, rangos y hojas protegidos: se puede limitar la edición a uno mismo, a un dominio o a una lista; los permisos de visor y de comentarista no permiten cambios. "Protection isn't a security measure": pueden imprimir, copiar y pegar, importar y exportar copias, y los visores pueden hacer una copia. La opción "mostrar una advertencia" no bloquea. No hay contraseña. https://support.google.com/docs/answer/1218656
- Historial de versiones de Sheets: solo propietarios y editores lo ven y restauran. Restaurar una versión borra el historial celda por celda previo a esa restauración. Google sugiere hacer una copia si se necesita ese historial. https://support.google.com/docs/answer/190843 [S]
- Permisos en Sheets (ver, comentar, editar): la ayuda "Compartir" respondió 404 y no la pude leer. Los tres niveles se deducen de la página de protección, que menciona editores, visores y comentaristas.
- Riesgo de las copias por correo: no hallé una fuente oficial que cuantifique este riesgo. Sí está implícito en que Panko y ICAEW piden una ubicación única para cada dato (ICAEW #15), y en que la coautoría exige un solo archivo en la nube. Marcar como argumento de práctica, no como dato.

### Recurso canónico
- **Macros:** la página de Microsoft Learn sobre macros bloqueadas de internet, porque explica el porqué y el cómo desbloquear de forma segura.
- **Office Scripts:** la introducción de Microsoft Learn.
- **Apps Script:** la guía oficial de funciones personalizadas, más la página de cuotas.
- **Compartir y colaborar:** no hay un recurso único. Combinar la página de coautoría de Microsoft con la de protección de rangos de Google, y escribir una nota propia de comparación.

---

## Componente 3. Puente: cuándo pasar a una base de datos

### Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 24 | Microsoft, especificaciones y límites de Excel | https://support.microsoft.com/en-us/office/excel-specifications-and-limits-1672b34d-7043-467e-8e27-269d656771c3 | primaria | 3/3/1/3 | [L] |
| 25 | Google, límites de archivos en Drive | https://support.google.com/drive/answer/37603 | primaria | 3/2/1/3 | [L] |
| 26 | Google Workspace Updates, "Doubled cell limits in Google Sheets now generally available" (2026-09-10) | https://workspaceupdates.googleblog.com/2026/09/doubled-cell-limits-in-google-sheets-now-generally-available.html | primaria | 3/2/1/3 | [L] |
| 27 | Google Workspace Updates, 2022-03 ("Ten million cells") | https://workspaceupdates.googleblog.com/2022/03/ten-million-cells-google-sheets.html | primaria | 3/1/1/1 | [M] |
| 28 | Airtable, plans overview | https://support.airtable.com/articles/2277136852-airtable-plans-overview | primaria | 3/2/1/3 | [L] |
| 29 | Microsoft, especificaciones de Access | https://support.microsoft.com/en-us/access/access-specifications | primaria | 3/2/1/3 | [S] |
| 30 | Microsoft, migrar una base de Access a SQL Server | https://support.microsoft.com/en-us/access/migrate-an-access-database-to-sql-server | primaria | 3/2/1/2 | [S] |

### Afirmaciones

- Excel: 1.048.576 filas × 16.384 columnas, 32.767 caracteres por celda, 8.192 caracteres por fórmula, 15 dígitos de precisión, 256 usuarios a la vez en un libro compartido. Otros límites (libros abiertos, hojas) dependen de la memoria. https://support.microsoft.com/en-us/office/excel-specifications-and-limits-1672b34d-7043-467e-8e27-269d656771c3
- Google Sheets: **20 millones de celdas** o 100 MB para planillas creadas o convertidas a Sheets. https://support.google.com/drive/answer/37603. El anuncio del 2026-09-10 confirma el aumento de 10 a 20 millones de celdas, para archivos nuevos, existentes e importados (.xlsx y CSV), sin control de administrador, con despliegue gradual desde el 2026-09-10 (Rapid Release) y el 2026-09-28 (Scheduled Release), y visibilidad de hasta 15 días. https://workspaceupdates.googleblog.com/2026/09/doubled-cell-limits-in-google-sheets-now-generally-available.html. Un aumento de tamaño de archivo importado está "coming soon" sin fecha. La misma fuente.
  - Discrepancia histórica: el brief hablaba de 10 millones, que era el límite desde 2022-03 (https://workspaceupdates.googleblog.com/2022/03/ten-million-cells-google-sheets.html [M]). Hay una beta de abril 2026 (https://workspaceupdates.googleblog.com/2026/04/faster-performance-and-doubled-cell-limits-in-Google-Sheets.html [M]). Ninguna fuente que leí menciona un cambio en el máximo de columnas, y la página de Drive tampoco lo lista.
  - La conversión de Excel a Sheets elimina las celdas con más de 50.000 caracteres. https://support.google.com/drive/answer/37603
- Access: base de hasta 2 GB, menos el espacio de objetos del sistema, y se puede enlazar a tablas de otras bases. Hasta 32.768 objetos. Microsoft indica que no soporta más de 255 usuarios concurrentes y recomienda SQL Server para más volumen. https://support.microsoft.com/en-us/access/access-specifications [S] y https://support.microsoft.com/en-us/access/migrate-an-access-database-to-sql-server [S]
- Airtable (página oficial, sin fecha visible): Free 1.000 registros por base, 1 GB y 1.000 llamadas de API por mes. Team 50.000 registros, 20 GB, 100.000 llamadas, US$24 por usuario por mes facturado mensual o US$20 anual. Business 125.000 registros, 100 GB, llamadas ilimitadas, US$54 mensual o US$45 anual. Los registros cuentan por base, no por tabla. https://support.airtable.com/articles/2277136852-airtable-plans-overview. Precios por arriba vigentes según esa fuente, sin fecha de revisión.
- AppSheet: no investigué (tercera ronda no alcanzó). Ver huecos.
- Señales de pasar a base de datos (varias personas escribiendo a la vez, uno-a-muchos, integridad, auditoría, permisos por fila): no hallé una fuente primaria que las liste como tal. Lo más cercano que verifiqué es indirecto: Panko explica que los errores de omisión y la copia a mano son difíciles de ver, y el límite de usuarios y la documentación de Microsoft sobre Access señalan cuándo falla la herramienta. Esta sección debe marcarse como criterio propio del autor de la nota, apoyado en los límites duros de arriba.

### Recurso canónico
Las dos páginas oficiales de límites (Excel y Drive), más el anuncio de Google del 2026-09-10 como fecha de cambio. Para las señales, no hay recurso: escribir una nota propia, marcada como criterio.

---

## Componente 4. Ficha: aplicaciones de planillas

### Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 31 | Microsoft, ciclo de vida de Office 2024 | https://learn.microsoft.com/lifecycle/products/office-2024 | primaria | 3/2/1/3 | [S] |
| 32 | Microsoft, FAQ de Office 2024 y LTSC 2024 | https://support.microsoft.com/office/office-2024-and-office-ltsc-2024-faq-1c454a7d-3d0a-4139-b1bd-c61725ea436c | primaria | 3/2/1/3 | [S] |
| 33 | LibreOffice, página de descarga | https://www.libreoffice.org/download/download-libreoffice/ | primaria | 3/1/1/3 | [L] |
| 34 | LibreOffice, notas de novedades 25.8 y 26.2 | https://whatsnew.libreoffice.org/26.2/ y https://whatsnew.libreoffice.org/25.8/ | primaria | 3/2/1/2 | [S] |
| 35 | Microsoft, límites de Excel | URL de la fuente 24 | primaria | 3/3/1/3 | [L] |
| 36 | Google, límites de Drive | URL de la fuente 25 | primaria | 3/2/1/3 | [L] |

### Afirmaciones

- **Microsoft 365 (Excel):** recibe mejoras continuas. "Microsoft 365 already has all the features included in Office 2024 and Office LTSC 2024, plus additional collaboration, productivity, and security features." https://support.microsoft.com/office/office-2024-and-office-ltsc-2024-faq-1c454a7d-3d0a-4139-b1bd-c61725ea436c [S]
- **Excel 2024 (perpetua):** fin de soporte el 2029-10-09 (Microsoft Lifecycle). La versión para consumidores sigue la Modern Lifecycle Policy, la comercial LTSC tiene 5 años fijos. Incluye "only a subset of the features" de Microsoft 365. Las apps de Microsoft 365 en Windows 10 reciben actualizaciones de seguridad hasta el 2028-10-10, y Office 2024 en Windows 10 no tiene extensión equivalente. https://learn.microsoft.com/lifecycle/products/office-2024 [S]
- **Excel web:** no soporta el bloqueo de macros de internet (no aplica) ni ejecuta VBA (dato por confirmar), pero sí ejecuta Office Scripts. https://learn.microsoft.com/en-us/office/dev/scripts/overview/excel
- **Google Sheets:** 20 millones de celdas (ver componente 3), tiempo de funciones personalizadas 30 s, Apps Script (JavaScript). Precios de Google Workspace: no verifiqué una fuente oficial, no los incluyo.
- **LibreOffice Calc:** vigente **26.8.3** ("LibreOffice 26.8 is our latest stable release"). También aparece la 26.2.7, y la 27.2.0.0 alpha1 como pre-lanzamiento. https://www.libreoffice.org/download/download-libreoffice/ . Calc 25.8 sumó 14 funciones nuevas y dejó de soportar Windows 7 y 8/8.1; 26.2 agregó conectores en Calc, entre otras cosas. https://whatsnew.libreoffice.org/25.8/ y https://whatsnew.libreoffice.org/26.2/ [S]. Límite de filas y columnas de Calc: la página de ayuda que probé no lo traía. Pendiente.
- **Diferencias clave verificadas:**
  - Excel limita por filas y columnas (1.048.576 × 16.384). Sheets limita por celdas totales (20 millones).
  - Macros: VBA en el escritorio de Excel (con bloqueo por defecto de archivos de internet en Windows), Office Scripts en Excel web, Apps Script en Sheets.
  - Coautoría de Excel: requiere almacenamiento en la nube de Microsoft y suscripción. Sheets la tiene siempre, porque el archivo vive en la nube.
- **Precios:** solo el precio de Airtable tiene fuente oficial verificada (componente 3). No incluyo precios de Microsoft 365 ni de Google Workspace.

### Recurso canónico
Páginas oficiales de especificaciones: Microsoft para Excel y para Office 2024, Google Drive para Sheets, y la descarga y notas de LibreOffice. La ficha debe llevar una línea de "revisado el 2026-11-27" por la volatilidad de las versiones y los límites.

---

## Huecos declarados

- **FAST:** no leí el PDF de reglas (02c, julio 2019). No afirmo reglas concretas atribuidas a FAST, ni "flujo de izquierda a derecha y de arriba abajo". Pendiente leerlo.
- **ICAEW "Twenty principles":** no abrí la lista de los 20 principios (https://www.icaew.com/policy-and-research/thought-leadership/thought-leadership-excel). Solo vi los números de los principios que cita el Code (#4, #5, #7, #8, #9, #11 a #15, #17, #18, #20).
- **Panko:** no encontré la edición 2008 de "What We Know About Spreadsheet Errors" (J. End User Computing, 1998, y actualización posterior) en su sitio. El host de la Universidad de Hawái no resolvió. Trabajé con las versiones de EuSpRIG 2000 y 2015 en arXiv. La cifra "5,2 %" de CER y la de "88 spreadsheets" que circulan de segunda mano no las pude rastrear a una tabla original.
- **Origen de "88 %":** no rastreado a ninguna fuente primaria.
- **EuSpRIG:** la lista oficial respondió 403, y la leí en un espejo y reseñas. Sin mirada propia de los casos.
- **Ziemann 2016:** cifras de segunda mano [S]. Springer pidió autenticación.
- **JPMorgan:** ni el informe del Senado (el PDF no era válido) ni el de la tarea del banco se leyeron en la fuente. La afirmación de "dividir por la suma" viene de prensa y de resúmenes. El informe del banco, en la copia de la OIG de la Fed (https://oig.federalreserve.gov/reports/2015-0030_-_Document_To_Release.pdf), es el candidato para leerlo.
- **Reinhart-Rogoff:** no leí el trabajo de Herndon, Ash y Pollin ni Cambridge Journal of Economics. Las cifras vienen de reseñas.
- **PHE:** el comunicado oficial lo vi solo por resumen del buscador, y no nombra el XLS en lo que vi.
- **Mostrar fórmulas y Evaluar fórmula:** sin página oficial verificada. Tampoco el Verificador de errores en detalle más allá del caso de referencias circulares.
- **Pruebas de cuadre:** no hallé una fuente específica fuera de ICAEW #17 y #18.
- **Office Scripts:** no verifiqué lenguaje (TypeScript), licencias ni plataformas. Power Automate: sin precios ni límites.
- **Excel web y VBA:** sin afirmación directa.
- **Permisos de Sheets (ver, comentar, editar):** la ayuda oficial de compartir respondió 404.
- **Riesgo de copias por correo y señales para pasar a base de datos:** sin fuente primaria. Dejar como criterio marcado.
- **AppSheet y Access:** AppSheet sin investigar. Access solo por buscador [S], sin precios.
- **Límites de LibreOffice Calc (filas, columnas):** no verificados. **Columnas de Sheets:** no verificadas.
- **Precios de Microsoft 365 y de Google Workspace:** no verificados.
- Rondas de búsqueda: usé aproximadamente tres por componente, con los límites de acceso mencionados arriba.
