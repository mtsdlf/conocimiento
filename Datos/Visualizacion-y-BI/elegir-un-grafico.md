---
resumen: >-
  Elegir un gráfico es decidir qué relación entre los datos se quiere mostrar y codificarla con la
  marca visual que el ojo compara con más precisión, sin deformar las proporciones.
estado: borrador
estabilidad: estable
fuentes:
  - "Cleveland y McGill, Graphical Perception, Journal of the American Statistical Association 79 (1984), según resúmenes: https://www.jstor.org/stable/2288400"
  - "Resumen de curso sobre Cleveland y McGill (según el buscador): https://vis.pku.edu.cn/course/visclass_f25/material/Graphical_perception.pdf"
  - "Heer y Bostock, Crowdsourcing Graphical Perception, CHI 2010 (según el buscador): https://idl.cs.washington.edu/files/2010-CrowdsourcingGraphicalPerception-CHI.pdf"
  - "Crítica posterior al ranking (según el buscador): https://arxiv.org/pdf/2212.10533"
  - "Financial Times, Visual Vocabulary (según su resumen): https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary"
  - "Correll et al., Tableau Research, sobre ejes truncados (según su resumen): https://ar5iv.arxiv.org/html/1907.02035"
  - "ONS, Does the axis have to start at zero? Part 1, line charts (2016, según su resumen): https://digitalblog.ons.gov.uk/2016/06/27/does-the-axis-have-to-start-at-zero-part-1-line-charts"
  - "Comisión Europea, Data visualisation guide, Starting bars at zero (según su resumen): https://data.europa.eu/apps/data-visualisation-guide/starting-bars-at-zero"
  - "Datawrapper Academy, Why our column and bar charts start at zero (solo el título): https://www.datawrapper.de/academy/why-our-column-and-bar-charts-start-at-zero"
  - "Datos/.investigacion/metricas-y-visualizacion.md (sección 3)"
aliases: [tipo de gráfico, elegir una visualización, chart choice, percepción gráfica]
creado: 2026-11-27
revisado:
---

# Elegir un gráfico

Elegir un gráfico es decidir qué relación entre los datos se quiere mostrar y codificarla con la
marca visual que el ojo compara con más precisión, sin deformar las proporciones.

Es la primera decisión de forma en [Visualización y BI](visualizacion-y-bi.md), y vale igual para un
[tablero](tablero.md) que para una presentación de [contar con datos](contar-con-datos.md). El
gráfico viene después de la pregunta: si no se sabe qué comparación tiene que hacer quien mira, no
hay gráfico correcto. Cómo se formula esa pregunta está en [pregunta de análisis](../Analisis/pregunta-de-analisis.md).

## Primero la relación, después el gráfico

El Visual Vocabulary del Financial Times agrupa los gráficos por la relación que muestran, no por su
aspecto. Sus nueve categorías, que se apoyan en el Graphic Continuum de Schwabish y Ribecca, son las
de la primera columna. Los ejemplos de la segunda son los casos corrientes (lectura de la base; el
póster trae muchos más).

| Relación | Qué pregunta contesta | Gráficos corrientes |
|---|---|---|
| Desvío (deviation) | ¿Cuánto se aparta de una referencia? | barras divergentes desde una línea de base |
| Correlación | ¿Se mueven juntas dos variables? | dispersión |
| Ranking | ¿Qué orden tienen? | barras ordenadas |
| Distribución | ¿Cómo se reparten los valores? | histograma, diagrama de caja |
| Cambio en el tiempo | ¿Cómo evolucionó? | líneas, barras por período |
| Parte del todo | ¿Qué parte de un total es cada cosa? | barras apiladas, torta con pocas partes |
| Magnitud | ¿Cuánto hay de cada cosa? | barras |
| Espacial | ¿Dónde pasa? | mapa |
| Flujo | ¿De dónde a dónde se mueve? | diagrama de Sankey |

En un comercio, «las ventas de cada mes» es cambio en el tiempo y va en líneas; «qué productos venden
más» es ranking y va en barras ordenadas; «cuánto gasta cada cliente» es distribución y va en un
histograma, que muestra lo que un promedio esconde (ejemplos de la base). Por qué un promedio puede
engañar está en [estadística descriptiva](../Estadistica/estadistica-descriptiva.md).

## Qué marcas se comparan mejor

Cleveland y McGill (1984) estudiaron qué tareas de percepción hace el ojo al leer un gráfico. Según
el resumen de un curso, el orden de precisión va de la posición sobre una escala común, a la
posición sobre escalas no alineadas, a la longitud, la dirección y el ángulo, al área, al volumen y
la curvatura, y al final al sombreado y la saturación del color. Según el buscador, Heer y Bostock repitieron los
experimentos en 2010 con participantes en línea, y el ranking "largely held".

Tres salvedades. El mismo resumen aclara que las diferencias promedio de exactitud a veces son de
uno o dos en cien. Una crítica posterior dice que ese orden es el más común, "by no means universal".
Y el artículo original no se leyó, solo resúmenes.

La consecuencia práctica: lo que hay que comparar con precisión va en posición o en longitud, como
barras o puntos sobre un eje común. El color sirve para separar grupos o destacar un dato, no para
leer cuánto vale.

## El eje de las barras empieza en cero

En un gráfico de barras, la altura de cada barra representa el valor. Si el eje empieza en otro
número, una diferencia chica parece enorme. Correll y otros, de Tableau Research,
describen que truncar el eje rompe la convención de que la diferencia de altura es proporcional a la
diferencia de valores.

En las líneas el caso es otro. La oficina de estadística del Reino Unido (ONS) sostiene que ahí el caso es
más defendible, porque el dato se lee por la posición del punto y no por una longitud.

> [!IMPORTANT]
> Las fuentes no coinciden del todo. La guía de visualización de la Comisión Europea y Datawrapper
> dicen que las barras empiezan en cero siempre. Knaflic discute casos en que no, en un texto del que
> solo se vio el título. Para las líneas, ONS acepta no empezar en cero. Lo que esta base sostiene:
> barras siempre desde cero; líneas desde donde muestre la variación, con el eje rotulado.

## Tortas y doble eje

La torta pide comparar ángulos y áreas, que en el orden de Cleveland y McGill se leen peor que la
posición y la longitud. Por eso cuesta comparar dos porciones parecidas y unas barras lo resuelven
mejor; con dos o tres partes muy distintas, la torta se lee. El gráfico de doble eje superpone dos
escalas elegidas por quien lo arma, y mover una de las dos puede hacer que las líneas parezcan
correlacionadas o no. Las dos cosas son inferencias de la base a partir del orden de percepción.

> [!NOTE]
> Sin fuente todavía: una fuente primaria sobre tortas y gráficos de doble eje.

## Qué leer para elegir mejor

- El póster del [Visual Vocabulary](https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary)
  del Financial Times, para elegir por relación. Fijate en la pregunta que encabeza cada categoría.
- Cleveland y McGill (1984), para el orden de percepción, leído como orientativo y no como regla.

> [!NOTE]
> Sin fuente todavía: *Show Me the Numbers* de Stephen Few, que cubre la elección de gráficos para
> negocios, no se leyó.
