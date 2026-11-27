---
resumen: >-
  La inferencia estadística saca conclusiones sobre una población a partir de una muestra, y dice
  cuánta incertidumbre tienen: con intervalos de confianza, con p-valores y con un tamaño de muestra
  elegido de antemano para tener potencia.
estado: borrador
estabilidad: estable
fuentes:
  - "ASA, Statement on Statistical Significance and P-Values (7 de marzo de 2016): https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf"
  - "Ronald Wasserstein y Nicole Lazar, The ASA's Statement on p-Values: Context, Process, and Purpose, The American Statistician 70(2), 129-133, 2016, doi 10.1080/00031305.2016.1154108; copia de lectura: https://www.stat.berkeley.edu/~aldous/Real_World/ASA_statement.pdf"
  - "Ronald Wasserstein, Allen Schirm y Nicole Lazar, Moving to a World Beyond 'p < 0.05', The American Statistician 73(sup1), 2019, doi 10.1080/00031305.2019.1583913 (según su resumen)"
  - "NIST/SEMATECH e-Handbook, 7.1.4, intervalos de confianza (según su resumen): https://www.itl.nist.gov/div898/handbook/prc/section1/prc14.htm"
  - "NIST/SEMATECH e-Handbook, 7.2.2.2, tamaño de muestra (según su resumen): https://www.itl.nist.gov/div898/handbook/prc/section2/prc222.htm"
  - "OpenIntro Statistics, caps. 5 a 7 (solo la página del libro): https://www.openintro.org/book/os/"
  - "Datos/.investigacion/estadistica.md"
  - "Datos/.investigacion/posicion-contraria.md (sección 4)"
aliases: [inferencia estadística, inferencia, muestreo, p-valor, p-value, valor p, intervalo de confianza, potencia estadística, tamaño de muestra]
creado: 2026-11-27
revisado:
---

# Muestreo e inferencia

La inferencia estadística saca conclusiones sobre una población a partir de una muestra, y dice cuánta incertidumbre tienen: con intervalos de confianza, con p-valores y con un tamaño de muestra elegido de antemano para tener potencia.

La [estadística descriptiva](estadistica-descriptiva.md) resume los datos que se tienen. La inferencia pregunta si lo que se ve ahí vale más allá: si la tasa de conversión de esta semana dice algo de la de siempre, o si la diferencia entre dos variantes es real o salió del azar.

## Por qué se infiere aunque se tengan todas las ventas

Una muestra es una parte de la población que se estudia. Si se encuesta a 200 clientes de 5.000, los 200 son la muestra. Pero en un comercio que tiene registradas todas sus ventas, la inferencia también hace falta. Lo que interesa casi nunca son las ventas pasadas, sino el proceso que las genera: el mes que viene, los clientes que todavía no llegaron. Los datos de un período son una muestra de ese proceso, y otro período habría dado otros números (lectura de la base).

Por eso dos semanas con tasas de conversión de 2,1 % y 2,4 % pueden no ser distintas en nada que importe. La inferencia mide cuánto puede variar un número solo por azar.

## Qué dice un intervalo de confianza

Un intervalo de confianza, según el NIST, «provides a range of values which is likely to contain the population parameter of interest». El 95 % no es la probabilidad de que el valor verdadero esté en este intervalo concreto. Describe al método: de muchos intervalos calculados igual, alrededor del 95 % contendrían el valor verdadero.

El ancho del intervalo depende de la dispersión de los datos y del tamaño de la muestra, que entra bajo una raíz cuadrada en la fórmula del NIST. Consecuencia práctica: para achicar el intervalo a la mitad hay que cuadruplicar la muestra (deducción de la fórmula, no cita). Un intervalo que va de una baja del 3 % a una suba del 8 % dice más que «no significativo»: dice que el efecto puede ser cualquier cosa en ese rango.

## Qué es un p-valor y qué no es

La definición de la ASA, en el artículo de Wasserstein y Lazar (2016): «Informally, a p-value is the probability under a specified statistical model that a statistical summary of the data (e.g., the sample mean difference between two compared groups) would be equal to or more extreme than its observed value.»

Dicho en criollo: si no hubiera ninguna diferencia real, ¿qué tan raro sería ver una diferencia como la observada o mayor? Un p-valor chico dice que los datos encajan mal con el supuesto de «no hay diferencia». No dice cuánto vale la diferencia ni si es verdad la hipótesis contraria.

La ASA publicó en 2016 seis principios, la referencia de lo que el p-valor no significa:

1. «P-values can indicate how incompatible the data are with a specified statistical model.»
2. «P-values do not measure the probability that the studied hypothesis is true, or the probability that the data were produced by random chance alone.»
3. «Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold.»
4. «Proper inference requires full reporting and transparency.»
5. «A p-value, or statistical significance, does not measure the size of an effect or the importance of a result.»
6. «By itself, a p-value does not provide a good measure of evidence regarding a model or hypothesis.»

El artículo lo resume así: se quiere convertir el p-valor en una afirmación sobre la verdad de la hipótesis nula o sobre el azar, y «The p-value is neither». La declaración propone complementarlo con intervalos de confianza, de credibilidad o de predicción, métodos bayesianos y tasas de falsos descubrimientos.

> [!IMPORTANT]
> El editorial de 2019 de la misma revista (Wasserstein, Schirm y Lazar) fue más lejos: según su resumen, recomienda dejar de decir «estadísticamente significativo», un paso que la declaración de 2016 no dio. Argumenta que un umbral fijo fomenta el reporte selectivo y que «no significativo» no implica «sin efecto». Es un editorial y no una declaración de la asociación; en la práctica, el término se sigue usando (lectura de la base). El texto no se leyó entero.

## Tamaño de muestra y potencia

La potencia es la probabilidad de detectar un efecto que existe; se escribe 1 − β, donde β es la probabilidad de no verlo. El nivel α es la probabilidad aceptada de declarar un efecto que no existe, casi siempre 5 %. El tamaño de muestra se elige antes de mirar datos, a partir de α, de la potencia, de la dispersión y del efecto más chico que importa detectar.

El NIST da una tabla para una prueba sobre la media con α = 0,05 y β = 0,10 (potencia del 90 %). Para detectar un desplazamiento de 0,5 desvíos hacen falta 43 casos; de 1 desvío, 11; de 1,5 desvíos, 5. La lección es la proporción: un efecto la mitad de grande pide cerca de cuatro veces más muestra.

Con poco volumen, el cálculo se da vuelta. En lugar de preguntar cuánta muestra hace falta, se pregunta cuál es el efecto más chico que la muestra disponible puede detectar. En un comercio chico suele ser un efecto enorme (lectura de la base), y por eso un experimento con poco tráfico no ve mejoras realistas. Cómo afecta eso a un experimento está en [significancia](significancia.md#por-qué-el-tráfico-bajo-exagera-los-efectos).

## Cómo falla la inferencia

- Una muestra que no representa: si los que responden la encuesta son los clientes más contentos, ningún intervalo lo corrige. Es [sesgo de selección](sesgos.md#sesgo-de-selección).
- Leer el p-valor como probabilidad de que sea cierto: lo prohíbe el principio 2.
- Confundir significativo con importante: con muchos datos, una diferencia ínfima da un p-valor chico (principio 5).
- Leer «no significativo» como «no hay efecto»: con poca muestra, el intervalo es tan ancho que no descarta casi nada.
- Elegir el análisis después de ver los datos: es una forma de hacer muchas pruebas y quedarse con la que da, tratada en [significancia](significancia.md#comparaciones-múltiples).

## Leer la declaración de la ASA

La declaración de 2016 son cuatro páginas, y es la fuente de qué no significa un p-valor. Conviene leer la definición y fijarse en los principios 2, 3 y 5. Para el cálculo, OpenIntro Statistics trata los fundamentos de la inferencia y la inferencia para proporciones y medias en los capítulos 5 a 7, y el capítulo 7 del manual del NIST tiene las fórmulas con tablas.
