---
resumen: >-
  La limpieza de datos es dejar una tabla en condiciones de analizarla: ordenarla para que cada
  columna sea una variable y cada fila una observación, y decidir qué hacer con los faltantes, los
  duplicados, los atípicos y los formatos.
estado: borrador
estabilidad: estable
fuentes:
  - "Hadley Wickham, Tidy Data, Journal of Statistical Software 59(10), 2014, secciones 2 y 3: https://www.jstatsoft.org/article/view/v059i10 (PDF: https://vita.had.co.nz/papers/tidy-data.pdf)"
  - "Donald B. Rubin, Inference and missing data, Biometrika 63(3):581-592, 1976 (según resumen): https://dash.harvard.edu/entities/publication/73120378-8764-6bd4-e053-0100007fdf3b"
  - "Universidad de Melbourne, Statistical Consulting Centre, Missing data (según resumen): https://scc.ms.unimelb.edu.au/resources/preparing-your-data/missing-data"
  - "NIST/SEMATECH e-Handbook of Statistical Methods, 7.1.6 What are outliers in the data?: https://itl.nist.gov/div898/handbook/prc/section1/prc16.htm"
  - "Microsoft, Study guide for Exam PL-300, Profile and clean the data: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300"
  - "Datos/.investigacion/analisis.md"
aliases: [data cleaning, limpiar datos, preparación de datos, datos ordenados, tidy data, valores faltantes, missing values, outliers, atípicos]
creado: 2026-11-27
revisado:
---

# Limpieza de datos

La limpieza de datos es dejar una tabla en condiciones de analizarla: ordenarla para que cada
columna sea una variable y cada fila una observación, y decidir qué hacer con los faltantes, los
duplicados, los atípicos y los formatos.

Es la fase del [análisis](analisis.md) que viene después de conseguir los datos y antes de
consultarlos. Wickham advierte en el resumen de su artículo de 2014: «A huge amount of effort is
spent cleaning data to get it ready for analysis». Esta nota trata la limpieza que hace el analista
sobre su propia tabla. La calidad como disciplina de la organización, con reglas y controles para
que el dato llegue bien desde el origen, es [calidad de datos](../Gobierno-y-calidad/calidad-de-datos.md),
y la limpieza que se automatiza en un pipeline es parte de
[ETL y ELT](../Ingesta-y-transformacion/etl-y-elt.md).

## Datos ordenados: una variable, una columna

Wickham define los datos ordenados («tidy data») con tres reglas: «each variable is a column, each
observation is a row, and each type of observational unit is a table». Una tabla así se filtra,
agrupa y grafica sin pasos intermedios. Su frase sobre las otras: «tidy datasets are all alike but
every messy dataset is messy in its own way».

Los cinco problemas más comunes, en sus palabras, con un ejemplo de comercio:

| Problema según Wickham | En una planilla de ventas | Cómo se ordena |
|---|---|---|
| «Column headers are values, not variable names» | Una columna por mes: «oct», «nov», «dic» | Pasar a dos columnas, mes y ventas |
| «Multiple variables are stored in one column» | «Remera-M-Negra» en una sola celda | Separar en producto, talle y color |
| «Variables are stored in both rows and columns» | Una fila «total» y otra «unidades» por producto, con meses en columnas | Pasar los meses a filas y «total» y «unidades» a columnas |
| «Multiple types of observational units are stored in the same table» | Datos del cliente repetidos en cada venta | Una tabla de clientes y otra de ventas |
| «A single observational unit is stored in multiple tables» | Una hoja de ventas por mes | Unir las hojas en una tabla con columna de mes |

Ordenar es la parte de la limpieza que tiene un criterio claro. Lo que sigue son decisiones que
cambian la respuesta y dependen de la [pregunta](pregunta-de-analisis.md).

## Por qué falta un dato importa más que cuántos faltan

Rubin (1976) formalizó cómo faltan los datos, según su resumen. Hoy se usan tres nombres, aunque
Rubin solo introdujo el segundo:

- Faltante completamente al azar (MCAR): que falte no depende de ningún valor. Borrar esas filas achica la muestra pero no debería sesgar el resultado (lectura de la base).
- Faltante al azar (MAR): depende de otra columna que sí se ve. Por ejemplo, la tienda online no pide el teléfono y el local sí.
- Faltante no al azar (MNAR): depende del valor que falta. Por ejemplo, los clientes que más gastan no completan la encuesta de satisfacción.

La consecuencia práctica es que borrar o completar no es neutro. Borrar las filas sin canal está
bien si el canal falta al azar; si falta en las ventas de un sistema viejo, borrarlas saca un
período entero. Antes de tocar un faltante, la pregunta es por qué falta.

Un faltante no es igual a otro, así que compararlo con `=` no lo encuentra. En SQL es NULL y se
pregunta con `IS NULL`, como explica
[SQL para análisis](sql-para-analisis.md#null-el-valor-que-no-es-igual-a-nada). Las funciones de
pandas para detectarlo, borrarlo o completarlo están en la ficha
[herramientas del analista](herramientas-del-analista.md#faltantes-en-pandas).

## Duplicados y formatos

Un duplicado es, en la lectura de la base, una fila que representa la misma observación que otra. El caso fácil son dos filas
idénticas; el difícil, dos filas del mismo cliente con el nombre escrito distinto, que es un
problema de [datos maestros](../Gobierno-y-calidad/datos-maestros.md). Para decidir qué es un
duplicado hay que saber qué es una fila en esa tabla: su
[grano](sql-para-analisis.md#el-grano-qué-es-una-fila).

Los formatos son el resto: fechas escritas de tres maneras, números con coma o punto decimal,
importes en pesos y dólares mezclados, texto con espacios de más. El programa del examen PL-300
de Microsoft pone en «Profile and clean the data» tareas como «Resolve inconsistencies, unexpected
or null values, and data quality issues», y elegir el tipo de dato de cada columna en la etapa
siguiente.

> [!NOTE]
> Sin fuente todavía: una fuente primaria con criterios para detectar duplicados y para normalizar
> formatos (fechas, texto, unidades), y una introducción a la imputación de faltantes para este
> nivel.

## Un atípico se investiga antes de sacarlo

NIST define un atípico como «an observation that lies an abnormal distance from other values in a
random sample from a population», y pide: «Outliers should be investigated carefully». La regla
habitual para marcarlos usa el rango intercuartílico (IQ, la distancia entre el primer y el tercer
cuartil):

| Valla | Fórmula según NIST | Lo que queda afuera |
|---|---|---|
| Interna inferior y superior | Q1 − 1,5·IQ y Q3 + 1,5·IQ | Atípico leve |
| Externa inferior y superior | Q1 − 3·IQ y Q3 + 3·IQ | Atípico extremo |

Los cuartiles y la dispersión se explican en
[estadística descriptiva](../Estadistica/estadistica-descriptiva.md). Una venta de 50 veces el
ticket promedio puede ser un error de tipeo, una compra mayorista o el cliente más valioso del año.
Sacarla sin mirar cambia el promedio y puede borrar justo lo que la pregunta buscaba.

## Cómo limpiar una tabla de ventas

1. Escribí qué es una fila y verificá que no haya dos filas con la misma clave.
2. Ordená la tabla con las tres reglas de Wickham.
3. Contá faltantes por columna y, para cada columna con faltantes, anotá por qué faltan.
4. Normalizá fechas, números y texto, y fijá el tipo de cada columna.
5. Marcá los atípicos con las vallas y mirá cada uno antes de decidir.
6. Anotá cada decisión (qué borraste, qué completaste, por qué), para que otra persona llegue al mismo número.

El último paso es el que separa una limpieza de un arreglo a mano que nadie puede repetir. Mirar
la tabla con gráficos antes y después de limpiar es parte del
[análisis exploratorio](analisis-exploratorio.md).
