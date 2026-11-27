---
resumen: >-
  La estadística descriptiva resume un conjunto de valores con pocos números (un centro, una
  dispersión) y con la forma de su distribución, sin pretender decir nada más allá de esos datos.
estado: vigente
estabilidad: estable
fuentes:
  - "OpenIntro Statistics, cap. 2, Summarizing Data (solo la página del libro): https://www.openintro.org/book/os/"
  - "Stanford STATS 60, lección 8, When means mislead (2025; según su resumen): https://web.stanford.edu/class/stats60/lectures/08-lecture-robustness.html"
  - "NIST/SEMATECH e-Handbook of Statistical Methods, 1.3.5 Quantitative Techniques (según su resumen): https://www.itl.nist.gov/div898/handbook/eda/section3/eda35.htm"
  - "Lancaster University, Math104, medidas resistentes (según su resumen): https://www.lancaster.ac.uk/~prendivs/accessible/math104/Math104.tex/Ch1.S6.SS6.html"
  - "Duke STA101, diapositivas de la unidad 1 (según su resumen): https://www2.stat.duke.edu/courses/Summer17/sta101.001-2/uploads/slides/u1_deck2H.pdf"
  - "Anscombe, Graphs in Statistical Analysis, The American Statistician 27, 17-21, 1973 (vía Wikipedia): https://en.wikipedia.org/wiki/Anscombe%27s_quartet"
  - "Datos/.investigacion/estadistica.md"
  - "Datos/.investigacion/posicion-contraria.md (sección 7)"
aliases: [estadísticos descriptivos, descriptive statistics, medidas de tendencia central, medidas de dispersión, media y mediana]
creado: 2026-11-27
revisado: 2026-11-27
---

# Estadística descriptiva

La estadística descriptiva resume un conjunto de valores con pocos números (un centro, una dispersión) y con la forma de su distribución, sin pretender decir nada más allá de esos datos.

Es lo que muestra casi todo tablero: ventas del mes, ticket promedio, clientes nuevos. Describe lo que pasó en los datos que se tienen. Si la pregunta es si eso vale para el mes que viene o para todos los clientes, ya es [inferencia](muestreo-e-inferencia.md); si es por qué pasó, es [causalidad](correlacion-y-causalidad.md).

## Centro, dispersión y forma

Un resumen tiene tres partes, y ninguna alcanza sola.

| Qué resume | Medida sensible a extremos | Medida que resiste extremos |
|---|---|---|
| El centro | Media (promedio) | Mediana |
| La dispersión | Desvío estándar | Rango intercuartílico (de Q1 a Q3) |
| La forma | Histograma, sesgo | Diagrama de caja |

La media es la suma de los valores dividida por cuántos son; el NIST la define así para una población. La mediana es el valor del medio cuando se ordenan. Los cuartiles parten los datos ordenados en cuatro partes iguales: Q1 deja abajo un cuarto, Q3 tres cuartos. Los percentiles generalizan la idea: el percentil 90 deja abajo el 90 % de los valores.

La mediana y el rango intercuartílico dependen solo de los valores cerca de Q1, la mediana y Q3; la media y el desvío cambian mucho con un solo extremo. Según el curso de Lancaster eso las hace resistentes, y el de Duke recomienda mediana e intercuartílico para datos sesgados.

## Ticket promedio contra ticket mediano

Las ventas de un comercio casi nunca son simétricas: muchas compras chicas y unas pocas muy grandes. Con ese sesgo a la derecha, la mediana queda por debajo de la media, y la diferencia entre las dos mide cuánto sesgo hay, según la lección de Stanford. La misma lección trae un caso con cifras: una sola respuesta de 600 minutos subió la media de 85,7 a 93,4 minutos, y la mediana quedó en 60.

Un ejemplo inventado para un comercio, con diez ventas de un día en pesos:

| Venta | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Monto | 8.000 | 9.500 | 10.000 | 11.000 | 12.000 | 12.500 | 13.000 | 14.000 | 15.000 | 185.000 |

La venta 10 es un cliente mayorista. Con ella, el ticket promedio es 29.000 y la mediana 12.250. Sin ella, el promedio baja a 11.667 y la mediana a 12.000. El promedio de 29.000 no describe a ningún cliente: ocho de diez gastaron menos de la mitad. La mediana casi no se movió.

Qué número usar depende de la pregunta (lectura de la base). Para saber cuánto gasta un cliente típico, la mediana. Para proyectar la facturación, la media, porque la plata del mayorista entra igual. Lo prudente es mostrar las dos y separar al mayorista como [segmento](../Analisis/segmentacion-de-clientes.md) si su comportamiento es otro.

## El gráfico antes que el número

Dos conjuntos con el mismo promedio y el mismo desvío pueden ser muy distintos. Lo muestra el cuarteto de Anscombe (1973), contado en [análisis exploratorio](../Analisis/analisis-exploratorio.md#por-qué-los-resúmenes-no-alcanzan).

En la práctica, el histograma y el diagrama de caja van antes que cualquier resumen. Muestran si hay dos grupos mezclados, valores imposibles que vienen de un error de carga o una cola larga que justifica la mediana. Esa mirada es parte del [análisis exploratorio](../Analisis/analisis-exploratorio.md), y los valores raros que salen de un error se tratan en la [limpieza de datos](../Analisis/limpieza-de-datos.md).

## Cómo engaña un resumen

- El promedio de una distribución sesgada: el ticket, el tiempo de entrega o el gasto por cliente arrastrados por pocos casos.
- El promedio de promedios: promediar el ticket de cada sucursal sin pesar por cantidad de ventas da un número que no es el ticket del comercio (lectura de la base).
- El agregado que esconde segmentos: el total puede ir en un sentido y cada segmento en el contrario. Es la paradoja de Simpson, en [sesgos](sesgos.md).
- El resumen sin la dispersión: dos sucursales con el mismo ticket promedio, una estable y otra que oscila mucho, piden decisiones distintas.

## Leer OpenIntro

El capítulo 2 de OpenIntro Statistics, «Summarizing Data», es el recurso abierto del tema (PDF gratis). Conviene fijarse en tres cosas: el histograma antes que cualquier número, cuándo usar media y desvío y cuándo mediana e intercuartílico, y cómo se lee un diagrama de caja. El texto del libro no se leyó para esta nota; se conoce su índice.
