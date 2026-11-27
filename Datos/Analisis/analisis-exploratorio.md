---
resumen: >-
  El análisis exploratorio es mirar los datos, sobre todo con gráficos, antes de resumirlos o de
  imponerles un modelo, para encontrar su forma, sus errores y las hipótesis que vale la pena
  probar.
estado: borrador
estabilidad: estable
fuentes:
  - "NIST/SEMATECH e-Handbook of Statistical Methods, 1.1.1 What is EDA?: https://www.itl.nist.gov/div898/handbook/eda/section1/eda11.htm"
  - "NIST/SEMATECH e-Handbook of Statistical Methods, 1.1.2 How does Exploratory Data Analysis differ from Classical Data Analysis?: https://www.itl.nist.gov/div898/handbook/eda/section1/eda12.htm"
  - "Hadley Wickham, Mine Çetinkaya-Rundel y Garrett Grolemund, R for Data Science, 2.ª ed., cap. Exploratory data analysis: https://r4ds.hadley.nz/EDA.html"
  - "John W. Tukey, Exploratory Data Analysis (Addison-Wesley, 1977), p. 1, citado por fuentes secundarias"
  - "SAGE Encyclopedia of Research Design, Exploratory data analysis (según resumen): https://methods.sagepub.com/ency/edvol/embed/encyc-of-research-design/chpt/exploratory-data-analysis"
  - "F. J. Anscombe, Graphs in Statistical Analysis, The American Statistician 27(1):17-21, 1973, vía Wikipedia: https://en.wikipedia.org/wiki/Anscombe%27s_quartet"
  - "Andrew Gelman y Eric Loken, The garden of forking paths, vía https://confidence.spotify.com/glossary/garden-of-forking-paths (según resumen)"
  - "Bickel, Hammel y O'Connell (1975), Sex Bias in Graduate Admissions: Data from Berkeley, Science, vía https://en.wikipedia.org/wiki/Simpson%27s_paradox (según resumen)"
  - "Datos/.investigacion/analisis.md"
  - "Datos/.investigacion/posicion-contraria.md (sección 7)"
aliases: [EDA, exploratory data analysis, exploración de datos, análisis exploratorio de datos]
creado: 2026-11-27
revisado:
---

# Análisis exploratorio

El análisis exploratorio es mirar los datos, sobre todo con gráficos, antes de resumirlos o de
imponerles un modelo, para encontrar su forma, sus errores y las hipótesis que vale la pena
probar.

Está en la fase de analizar del [análisis](analisis.md), pero empieza antes: mirar la tabla es como
se descubre qué hay que [limpiar](limpieza-de-datos.md). NIST lo define como «an approach/philosophy
for data analysis that employs a variety of techniques (mostly graphical)». Es más una actitud que
una técnica: mirar antes de concluir.

## Mirar primero, modelar después

NIST compara tres enfoques por el orden de los pasos. En el análisis clásico, a los datos les sigue
«the imposition of a model». En el exploratorio, la recolección «is followed immediately by
analysis with a goal of inferring what model would be appropriate». En el bayesiano, antes de mirar
se impone una distribución sobre los parámetros del modelo.

Tukey es el autor del texto fundacional del enfoque, de 1977. Según una revisión histórica, la primera página dice:
«Exploratory data analysis is detective work». Fuentes secundarias le atribuyen la contraposición
con el análisis confirmatorio: el exploratorio busca pistas, el confirmatorio juzga la evidencia, y
los dos avanzan en paralelo. El libro no se leyó; es denso y no es para quien empieza.

## Por qué los resúmenes no alcanzan

Anscombe publicó en 1973 cuatro conjuntos de 11 pares de puntos con medias, varianzas, correlación
y recta de regresión casi idénticas. Graficados, uno es una nube con tendencia, otro una curva, otro
una recta perfecta con un punto suelto y otro una columna con un único valor lejano. Su objetivo,
según Wikipedia, era rebatir la idea de que «numerical calculations are exact, but graphs are
rough».

La lección para un comercio: un ticket promedio no dice si todos gastan parecido o si unos pocos
clientes gastan mucho y el resto poco. Cuándo usar media o mediana, y cómo describir la
dispersión, es [estadística descriptiva](../Estadistica/estadistica-descriptiva.md). Qué gráfico
muestra cada forma está en [elegir un gráfico](../Visualizacion-y-BI/elegir-un-grafico.md).

## Dos preguntas para explorar una tabla

R for Data Science dice que el exploratorio «is not a formal process with a strict set of rules»,
sino «more a state of mind», y propone dos preguntas que guían:

- «What type of variation occurs within my variables?» Cómo se reparte cada columna: qué
  valores son comunes, cuáles raros, si hay huecos o valores imposibles.
- «What type of covariation occurs between my variables?» Cómo se mueven dos columnas juntas:
  si el ticket cambia con el canal, si las ventas cambian con el día de la semana.

Para una tabla de ventas, eso se traduce en pasos concretos:

1. Contá filas, fechas mínima y máxima, y valores distintos de cada columna categórica (canal, producto, provincia).
2. Graficá la distribución del total de cada venta con un histograma y marcá los [atípicos](limpieza-de-datos.md#un-atípico-se-investiga-antes-de-sacarlo).
3. Graficá las ventas por día o por semana: buscá huecos, picos y la estacionalidad.
4. Cruzá el total con cada categoría: ticket por canal, por medio de pago, por primera compra o recompra.
5. Desagregá cada número que te sorprenda un nivel más (por canal, por producto, por [segmento](segmentacion-de-clientes.md)) antes de explicarlo.
6. Anotá cada patrón como hipótesis, con lo que haría falta para confirmarlo.

Las consultas para cada paso son agregaciones y funciones de ventana de
[SQL para análisis](sql-para-analisis.md).

## Un patrón encontrado es una hipótesis

El exploratorio genera hipótesis; no las prueba. Mirar muchos cortes hasta que uno muestre algo es
la forma más rápida de encontrar una coincidencia. Gelman y Loken lo llaman «garden of forking
paths»: los falsos positivos aparecen aun sin pescar a propósito, por decisiones de análisis
tomadas después de ver los datos, según el informe de posición contraria. El riesgo y su
discusión están en [significancia](../Estadistica/significancia.md).

Desagregar también puede dar vuelta una conclusión: en los datos de admisión de Berkeley de 1973 el
total sugería un sesgo contra las mujeres y por departamento la relación cambiaba. Es la paradoja
de Simpson, en [sesgos](../Estadistica/sesgos.md).

Que un grupo compre más no prueba que algo lo haya causado. Para pasar de un patrón a una causa hace
falta un diseño: [correlación y causalidad](../Estadistica/correlacion-y-causalidad.md) da el
razonamiento; el [experimento A/B](../../Producto/Medicion/experimento-ab.md) y la
[incrementalidad](../../Marketing/Medicion/incrementalidad.md), la prueba. La lectura de esta base
es que el exploratorio decide qué vale la pena probar, y el experimento decide si es cierto.

## Qué leer

NIST 1.1.1 y 1.1.2 para la idea, cortas. El capítulo de exploratorio de R for Data Science para la
práctica: fijarse en cómo cada gráfico contesta una de las dos preguntas. Anscombe (1973) tiene
cuatro páginas; lo que importa es la figura con los cuatro conjuntos.
