---
resumen: >-
  Los errores en planillas son celdas con fórmulas o datos mal hechos que dan un resultado
  equivocado sin avisar. La investigación los mide de dos maneras distintas (cuántas planillas
  auditadas tienen al menos uno y qué proporción de celdas con fórmula está mal), y las dos dicen que
  en una planilla grande es muy probable que algún resultado final esté mal.
estado: borrador
estabilidad: semi
fuentes:
  - "Raymond R. Panko, Spreadsheet Errors: What We Know. What We Think We Can Do, EuSpRIG 2000: https://arxiv.org/pdf/0802.3457"
  - "Raymond R. Panko, What We Don't Know About Spreadsheet Errors Today, EuSpRIG 2015: https://arxiv.org/pdf/1602.02601"
  - "Powell, Baker y Lawson, A critical review of the literature on spreadsheet errors, Decision Support Systems, 2008 (solo según el buscador): https://unpaywall.org/10.1016%2Fj.dss.2008.06.001"
  - "Ziemann, Eren y El-Osta, Gene name errors are widespread in the scientific literature, Genome Biology 2016 (cifras según resúmenes; el texto pidió autenticación): https://link.springer.com/10.1186/s13059-016-1044-7"
  - "Seguimiento 2014-2020 de errores de nombres de genes (según resumen): https://pmc.ncbi.nlm.nih.gov/articles/PMC8357140"
  - "Tweedie et al., Genenames.org: the HGNC and VGNC resources in 2021, Nucleic Acids Research: https://pmc.ncbi.nlm.nih.gov/articles/PMC7779007"
  - "Public Health England, comunicado sobre la demora en reportar casos (según resumen): https://gov.uk/government/news/phe-statement-on-delayed-reporting-of-covid-19-cases"
  - "The Register, Excel England coronavirus contact error (2020-10-05): https://www.theregister.com/2020/10/05/excel_england_coronavirus_contact_error/"
  - "Retraction Watch sobre Herndon, Ash y Pollin (2013-04-18; reseña): https://retractionwatch.com/2013/04/18/influential-reinhart-rogoff-economics-paper-suffers-database-error/"
  - "Rogoff, FAQ (respuesta de los autores; según resumen): https://rogoff.scholars.harvard.edu/resource/faq"
  - "Senado de EE. UU., PSI, JPMorgan Chase Whale Trades (2013-03-15; no leído): https://www.hsgac.senate.gov/wp-content/uploads/imo/media/doc/REPORT%20-%20JPMorgan%20Chase%20Whale%20Trades%20%283-15-13%29.pdf"
  - "IFRE, JPM report unveils VaR errors (prensa; según resumen): https://www.ifre.com/story/1744757/derivatives-jpm-report-unveils-var-errors"
  - "EuSpRIG, horror stories (respondió 403; vista en espejo): https://eusprig.org/research-info/horror-stories/"
  - "Planillas-de-calculo/.investigacion/diseno-automatizacion-y-limites.md"
  - "Planillas-de-calculo/.investigacion/posicion-contraria-y-fundamentos.md"
aliases: [spreadsheet errors, spreadsheet risk, errores de Excel, cell error rate, CER, tasa de error por celda, horror stories]
creado: 2026-11-27
revisado:
---

# Errores en planillas

Los errores en planillas son celdas con fórmulas o datos mal hechos que dan un resultado equivocado sin avisar. La investigación los mide de dos maneras distintas (cuántas planillas auditadas tienen al menos uno y qué proporción de celdas con fórmula está mal), y las dos dicen que en una planilla grande es muy probable que algún resultado final esté mal.

Casi todo lo que se sabe viene de Raymond Panko, de la Universidad de Hawái, que reunió auditorías y experimentos en dos revisiones publicadas por EuSpRIG (el grupo europeo de riesgo en planillas), una de 2000 y otra de 2015. Su conclusión de 2015 es "spreadsheet errors are rare on a per-cell basis, but in large programs, at least one incorrect bottom-line value is very likely to be present". Y sobre a quién culpar: "spreadsheet programs are not error-prone. People are error prone."

## Las dos cifras que mide Panko

Las cifras de errores en planillas que circulan mezclan dos magnitudes distintas. Conviene separarlas antes de citar cualquiera.

**El porcentaje de planillas con al menos un error.** Sale de auditorías: alguien revisa una planilla entera y cuenta si encontró algo. En 2015 Panko reúne 85 planillas inspeccionadas a fondo en seis trabajos (Hicks 1995, Coopers & Lybrand 1997, KPMG 1998, Lukasic 1998, Butler 2000, Lawrence y Lee 2001) y da un 94 % con errores. La edición de 2000 da 91 % para las 54 planillas de los estudios de 1997 en adelante (Coopers & Lybrand 1997: 91 % de 23; KPMG 1997: 91 % de 22; Butler 2000: 86 % de 7).

**La tasa de error por celda** (*cell error rate*, CER). Es la proporción de celdas con fórmula que tienen un error original. En 2015 Panko da un promedio de 3,9 % en los experimentos de laboratorio y dice que lo esperable es de 1 % a 5 % "based on human error research". En las auditorías de 2000, las CER fueron 1,2 %, 2,2 % y 2,5 %, y 0,38 % para las celdas con fórmula en el estudio de Butler.

Las dos se conectan así: si cada celda con fórmula tiene una chance chica de estar mal, una planilla con cientos de fórmulas encadenadas tiene una chance alta de que algún resultado final herede un error. Panko lo muestra en un gráfico de su texto de 2015.

> [!IMPORTANT]
> El 94 % no es la proporción de todas las planillas que tienen errores. Es la de planillas que alguien eligió auditar, revisadas en su mayoría por firmas comerciales en auditorías de varios días por planilla. Son muestras chicas y no aleatorias. La edición de 2000 da otra cifra, 24 % de 367 planillas, porque mezcla esas auditorías con estudios más viejos y menos rigurosos (Davies e Ikin 1987: 21 % de 19; Butler 1992: 11 % de 273). Las dos cifras son ciertas para su muestra y no se pueden comparar entre sí.

## De dónde sale el «88 %»

La frase «el 88 % de las planillas tiene errores» circula mucho y no tiene una fuente rastreable. Las cifras de Panko son 24 %, 86 %, 91 % y 94 %; en ninguna de sus dos revisiones aparece un 88 %. Un artículo de divulgación la da como "it was estimated that 88 percent of existing spreadsheets contain errors", sin fuente. Un resumen secundario la explica como «94 % de 88 planillas auditadas en 7 estudios», lo que choca con las 85 planillas en seis trabajos que cuenta Panko en 2015; esa discrepancia quedó sin resolver.

Para citar algo, lo verificable es: «en las auditorías intensivas que reunió Panko, el 94 % de 85 planillas tenía al menos un error», con la aclaración de que la muestra no representa a todas las planillas.

## Tres tipos de error

Panko y Halverson clasifican los errores en tres tipos, y la diferencia importa porque no se detectan igual:

| Tipo | Qué es | En una planilla de stock |
|---|---|---|
| Mecánico | Apuntar a la celda equivocada, tipear mal un número | La fórmula del stock de azúcar resta las ventas de la fila de la harina |
| Lógico | La fórmula hace lo que se escribió, pero lo que se escribió está mal pensado | El stock se calcula restando ventas, pero nunca se suman las compras |
| De omisión | Falta algo que tendría que estar | La merma no figura en ningún lado |

En un experimento, el reparto fue 45 % lógicos, 23 % mecánicos y 31 % de omisión. En otro, 44 %, 3 % y 53 %, y Panko atribuye ese 53 % a "an anomaly of the task statement wording". Los de omisión son los más difíciles de encontrar, porque no hay ninguna celda mal para mirar.

## Quien hizo la planilla cree que está bien

El problema de fondo es la sobreconfianza. En los estudios que reúne Panko en 2000, quienes habían armado las planillas estimaron, en la mediana, que había un 10 % de chance de que la suya tuviera errores (18 % en promedio). El 86 % de esas planillas tenía errores.

La detección tampoco es fácil cuando alguien busca. En el experimento de Galletta y colegas que cita Panko, ninguno de 14 errores sembrados fue encontrado por todos los participantes: tres los encontró menos del 10 % y la mitad, menos del 40 %. Panko pone el techo de las revisiones celda por celda en encontrar alrededor del 90 % de los errores. Cómo se organiza esa revisión está en [revisar una planilla](revisar-una-planilla.md).

## Casos que se hicieron públicos

EuSpRIG lleva desde 1995 una lista de casos públicos (*horror stories*), con 89 contados en 2007. Tiene un sesgo obvio: solo entran los errores que alguien hizo públicos. Los cuatro casos que más se citan, con lo que está verificado y lo que viene de la prensa:

**Nombres de genes convertidos en fechas.** Excel convierte automáticamente textos como `SEPT2` o `MARCH1` en fechas. El comité que nombra los genes humanos (HGNC) terminó renombrando los genes: MARCH# pasó a MARCHF#, SEPT# a SEPTIN#, MARC# a MTARC# y DEC1 a DELEC1, porque se "auto-converted to dates when entered in Microsoft Excel". El comité concluyó que pedir a los usuarios que cambiaran la configuración de Excel no resolvía el problema. Ziemann, Eren y El-Osta revisaron archivos suplementarios de 18 revistas entre 2005 y 2015, y según los resúmenes de su trabajo, el 19,6 % de los artículos con listas de genes en Excel tenía errores; un seguimiento de 2014 a 2020 da 30,9 % (3.436 de 11.117). Son porcentajes de artículos con listas de genes en Excel, no de todos los artículos. La cifra de «27 genes renombrados» viene de la prensa; el artículo del HGNC no da un total. La lección para un negocio es la de [tipos de dato](../Modelo-de-la-planilla/tipos-de-dato.md): un código de producto como `1-3` o `MAR10` puede volverse fecha al cargarlo.

**Public Health England, 2020.** Faltaron 15.841 casos de COVID-19 en los reportes entre el 25 de septiembre y el 2 de octubre de 2020, por un fallo en la carga de datos (según el comunicado oficial, visto por resumen). Según The Register, que cita a la BBC, los resultados se guardaban en el formato .XLS antiguo, con tope de 65.536 filas por hoja; cada caso ocupaba varias filas, así que cada hoja admitía unos 1.400 casos y lo que pasaba el tope se perdía. Hasta 48.000 contactos podrían no haber sido avisados. El comunicado, en lo que se vio, no nombra el formato .XLS: esa atribución viene de la prensa. Las estimaciones de infecciones y muertes adicionales que circularon son modeladas, no medidas. Los límites de filas de cada aplicación están en la [ficha de aplicaciones](../aplicaciones-de-planillas.md).

**Reinhart y Rogoff, 2013.** Herndon, Ash y Pollin encontraron que la planilla de un trabajo influyente sobre deuda pública y crecimiento dejaba fuera de un promedio a Australia, Austria, Bélgica, Canadá y Dinamarca: el rango se cortaba en la fila 44 en lugar de la 49. Según las reseñas, con deuda mayor al 90 % del PIB obtuvieron un crecimiento promedio de 2,2 %, y señalaron además exclusiones de datos y métodos de promedio discutibles. Rogoff respondió que el error de planilla tuvo "relatively limited impact". Las dos lecturas siguen en pie, y la cifra del trabajo original no se verificó en una fuente primaria. Es un error mecánico de libro: un rango que no llega hasta el final de los datos, lo que una [tabla estructurada](../Datos-en-la-planilla/tabla-estructurada.md) evita porque crece sola.

**JPMorgan, la ballena de Londres, 2012.** Según la prensa y los resúmenes del informe interno del banco, el modelo de riesgo (VaR) se armaba a mano copiando y pegando entre planillas, y una fórmula dividía por la suma de dos tasas en lugar de su promedio, lo que reducía la volatilidad calculada. Una revisión interna describió el proceso como "error prone" y "not easily scalable", y al volver al modelo anterior el VaR casi se duplicó, a US$129 millones. Hay dos documentos que se suelen confundir: el informe del grupo de trabajo del propio banco (enero de 2013) y el del Senado de EE. UU. (15 de marzo de 2013). Ninguno de los dos se leyó en su texto; todo lo de este párrafo es de segunda mano.

> [!NOTE] Sin fuente todavía: el texto de los informes del banco y del Senado sobre JPMorgan, el trabajo de Herndon, Ash y Pollin, el artículo completo de Ziemann y la lista oficial de EuSpRIG (que respondió 403). Las cifras de esos casos son las de las reseñas.

## La crítica a las cifras de laboratorio

Powell, Baker y Lawson publicaron en 2008 una revisión crítica de esta literatura. Según su resumen, sostienen que las tasas de error de los experimentos de laboratorio no deberían usarse sin cuidado para inferir cuántos errores hay en las planillas que se usan en las empresas. El punto pesa porque la mayoría de los experimentos se hicieron con estudiantes, sobre planillas de 25 a 50 celdas. Panko responde en 2015 que la evidencia es "substantial, compelling, and unanimous".

> [!IMPORTANT]
> Las dos posiciones no se reconciliaron. Lo que comparten es que las muestras no son aleatorias. Lo que las separa es si las tasas de laboratorio se pueden trasladar a planillas reales. La revisión de 2008 solo se vio por su resumen.

## Por qué no alcanza con sacar las planillas

Que fallen mucho no lleva a dejar de usarlas. La conclusión de Panko es que hace falta "massively more testing", con inspección como la que se hace en el software: el problema que describe es la falta de prueba, no la herramienta. Para un negocio chico, eso se traduce en dos cosas: [diseñar](entradas-calculo-salidas.md) para que los errores sean menos probables y [revisar](revisar-una-planilla.md) antes de confiar en un número. Cuando la planilla falla porque ya no es la herramienta adecuada, la salida es [pasar a una base](../cuando-pasar-a-una-base.md).
