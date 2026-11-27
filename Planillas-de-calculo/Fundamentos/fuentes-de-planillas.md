---
resumen: >-
  Bibliografía del tema Planillas de cálculo: los estándares de diseño (ICAEW, FAST), la
  investigación sobre errores (Panko, EuSpRIG), los papers sobre datos en planillas (Broman y Woo,
  Wickham), la documentación de Microsoft y Google, un sitio de practicantes y el examen de Excel
  de Microsoft, con qué leer de cada uno y en qué fijarse.
estado: borrador
estabilidad: semi
fuentes:
  - "ICAEW, Financial Modelling Code (2018, ed. 2024): https://www.icaew.com/-/media/corporate/files/technical/technology/excel-community/financial-modelling-code.ashx"
  - "FAST Standard Organisation, The FAST Standard: https://www.fast-standard.org/the-fast-standard/"
  - "Raymond R. Panko, Spreadsheet Errors: What We Know. What We Think We Can Do, EuSpRIG 2000: https://arxiv.org/pdf/0802.3457"
  - "Raymond R. Panko, What We Don't Know About Spreadsheet Errors Today, EuSpRIG 2015: https://arxiv.org/pdf/1602.02601"
  - "EuSpRIG, horror stories: https://eusprig.org/research-info/horror-stories/"
  - "Karl W. Broman y Kara H. Woo, Data Organization in Spreadsheets, The American Statistician 72(1): 2-10, 2018: https://kbroman.org/Paper_DataOrg/manuscript.html"
  - "Hadley Wickham, Tidy Data, Journal of Statistical Software 59(10), 2014: https://vita.had.co.nz/papers/tidy-data.html"
  - "Exceljet (practicante): https://exceljet.net/functions/xlookup-function"
  - "Microsoft Learn, Exam MO-211: Microsoft Excel Expert (Microsoft 365 Apps) (2026-07-01): https://learn.microsoft.com/certifications/exams/mo-211"
  - "Planillas-de-calculo/.investigacion/ (informes del 2026-11-27)"
aliases: [bibliografía de planillas, recursos de Excel, recursos de Google Sheets, spreadsheet references]
creado: 2026-11-27
revisado:
---

# Fuentes de planillas

Bibliografía del tema Planillas de cálculo: los estándares de diseño (ICAEW, FAST), la investigación sobre errores (Panko, EuSpRIG), los papers sobre datos en planillas (Broman y Woo, Wickham), la documentación de Microsoft y Google, un sitio de practicantes y el examen de Excel de Microsoft, con qué leer de cada uno y en qué fijarse.

Casi todo es gratuito y está en línea. Las ideas de cada fuente están repartidas en las notas del tema; acá se dice qué leer si se quiere ir a la fuente.

## Para diseñar una planilla que dure

**ICAEW, *Financial Modelling Code*** (2018, edición 2024). [PDF gratuito](https://www.icaew.com/-/media/corporate/files/technical/technology/excel-community/financial-modelling-code.ashx). Es la referencia principal de [entradas, cálculo y salidas](../Diseno-de-planillas/entradas-calculo-salidas.md) y de [revisar una planilla](../Diseno-de-planillas/revisar-una-planilla.md). Leer los principios #9 (separar entradas, cálculos y salidas), #12 (fórmulas consistentes), #14 (sin números fijos en las fórmulas), #15 (un solo lugar por dato), #17 (controles) y #18 (revisar y probar). Fijarse en que está escrito para modelos financieros: hay que traducir cada principio a una planilla de costos o de stock. Se apoya en los «Twenty principles for good spreadsheet practice» del mismo instituto, cuya lista completa la investigación no abrió.

**FAST Standard.** [Página del estándar](https://www.fast-standard.org/the-fast-standard/). La segunda referencia de diseño, más detallada en reglas de construcción. La versión enlazada es la 02c de julio de 2019, según el nombre del archivo. Leer el PDF de reglas, que la investigación no leyó; fijarse en si hay una edición posterior.

## Para saber cuánto fallan las planillas

**Raymond Panko, «What We Don't Know About Spreadsheet Errors Today»** (EuSpRIG 2015). [arXiv](https://arxiv.org/pdf/1602.02601). La revisión más reciente y la que explica qué mide cada cifra. Leer el resumen y la sección de evidencia, con sus tablas. Fijarse en la diferencia entre el porcentaje de planillas auditadas con errores y la tasa de error por celda, que es la base de [errores en planillas](../Diseno-de-planillas/errores-en-planillas.md).

**Raymond Panko, «Spreadsheet Errors: What We Know. What We Think We Can Do»** (EuSpRIG 2000). [arXiv](https://arxiv.org/pdf/0802.3457). La edición anterior, con las tablas de auditorías y experimentos por estudio, la sobreconfianza y las cifras de trabajo en parejas y grupos. Fijarse en que sus totales mezclan estudios viejos y nuevos, y en que los experimentos son con estudiantes sobre planillas chicas.

**Powell, Baker y Lawson, «A critical review of the literature on spreadsheet errors»** (Decision Support Systems, 2008). [Enlace](https://unpaywall.org/10.1016%2Fj.dss.2008.06.001). La crítica metodológica a trasladar las tasas de laboratorio a planillas reales. Solo se vio su resumen.

**EuSpRIG** (European Spreadsheet Risks Interest Group). [Lista de casos](https://eusprig.org/research-info/horror-stories/) y actas de sus conferencias, muchas en arXiv. La lista de casos públicos de errores se lleva desde 1995; respondió 403 durante la investigación. Fijarse en su sesgo: solo están los errores que se hicieron públicos.

## Para ordenar los datos en la planilla

**Karl Broman y Kara Woo, «Data Organization in Spreadsheets»** (*The American Statistician* 72(1): 2-10, 2018). [Manuscrito de los autores](https://kbroman.org/Paper_DataOrg/manuscript.html). La guía práctica más clara sobre cómo cargar datos: una cosa por celda, un solo rectángulo, sin celdas combinadas, fechas como AAAA-MM-DD. Leer las secciones «Put just one thing in a cell», «Make it a rectangle», «No empty cells» y «Write dates like YYYY-MM-DD». Fijarse en que los ejemplos son de laboratorio y hay que traducirlos a ventas y stock. Es la fuente de [datos ordenados](../Datos-en-la-planilla/datos-ordenados.md).

**Hadley Wickham, «Tidy Data»** (*Journal of Statistical Software* 59(10), 2014). [Página del paper](https://vita.had.co.nz/papers/tidy-data.html). La teoría detrás: "Each variable is a column, each observation is a row, and each type of observational unit is a table." Fijarse en que define un modelo de datos para analizar, no reglas de carga en la hoja; se lee después de Broman y Woo.

## La documentación de cada aplicación

**Microsoft Support y Microsoft Learn.** La documentación de Excel va por función, y cada página lista las versiones en que existe: es la forma de saber si una función anda en Excel 2019 o solo en Microsoft 365. La página de [especificaciones y límites](https://support.microsoft.com/en-us/office/excel-specifications-and-limits-1672b34d-7043-467e-8e27-269d656771c3) da los topes de tamaño. Las páginas en castellano (support.microsoft.com/es-es) dan los nombres de las funciones y los errores como aparecen en la interfaz. Fijarse en que a veces una misma página se contradice sobre las versiones, como pasa con BUSCARX.

**Ayuda de Google Docs Editors y guías de Apps Script.** La ayuda de Sheets va por función, sin lista de versiones. Las novedades y sus fechas están en el blog [Google Workspace Updates](https://workspaceupdates.googleblog.com/), que es donde se anunció el aumento a 20 millones de celdas. Para automatizar, las guías de [funciones personalizadas](https://developers.google.com/apps-script/guides/sheets/functions) y de [cuotas](https://developers.google.com/apps-script/guides/services/quotas) de Apps Script.

Lo que cambia de estas fuentes (versiones, límites, cuotas) está en la [ficha de aplicaciones](../aplicaciones-de-planillas.md) y en la [ficha de equivalencias](../Formulas/equivalencias-de-funciones.md).

## Un sitio de practicantes

**Exceljet.** [exceljet.net](https://exceljet.net/). Explicaciones por función con ejemplos resueltos, escritas por practicantes, no por Microsoft. Útil para ver cómo se usa una función en un caso real (por ejemplo, [BUSCARX](https://exceljet.net/functions/xlookup-function) o [INDICE](https://exceljet.net/functions/index-function)) y para las advertencias que la documentación oficial no da. Fijarse en que sus fechas de versión cambian: verificarlas contra Microsoft.

## El examen de Excel de Microsoft como lista de temas

**MO-211, Microsoft Excel Expert (Microsoft 365 Apps).** [Página del examen](https://learn.microsoft.com/certifications/exams/mo-211), actualizada el 2026-07-01. Sus cuatro dominios y pesos son: gestionar opciones y ajustes del libro (10-15 %), gestionar y dar formato a los datos (30-35 %), crear fórmulas avanzadas y macros (25-30 %) y gestionar gráficos y tablas avanzados (25-30 %). Sirve como lista de lo que Microsoft considera nivel experto, no como programa de estudio para un negocio chico. El PDF con los objetivos detallados no se pudo abrir.

> [!NOTE] Sin fuente todavía: libros y cursos canónicos de Excel y Google Sheets para un negocio chico; la investigación no los buscó. *M is for (Data) Monkey*, de Ken Puls y Miguel Escobar, aparece como referencia de practicantes para Power Query, sin año confirmado.
