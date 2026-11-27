---
resumen: >-
  La estadística, en el análisis de negocio, es lo que dice qué se puede concluir de un número: cómo
  resumir muchos valores sin esconder lo importante, cuánto se puede generalizar desde una muestra,
  cuándo una relación es causa y qué sesgos hacen que un dato mienta.
estado: vigente
estabilidad: estable
fuentes:
  - "OpenIntro Statistics, índice de capítulos (solo la página del libro): https://www.openintro.org/book/os/"
  - "ASA, Statement on Statistical Significance and P-Values (7 de marzo de 2016): https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf"
  - "Stanford Encyclopedia of Philosophy, Simpson's Paradox (rev. 2026; según su resumen): https://plato.stanford.edu/entries/paradox-simpson/"
  - "Andrew Gelman y John Carlin, Beyond Power Calculations, Perspectives on Psychological Science 9(6), 641-651, 2014 (según su resumen): https://sites.stat.columbia.edu/gelman/research/published/PPS551642_REV2.pdf"
  - "Datos/.investigacion/estadistica.md"
  - "Datos/.investigacion/posicion-contraria.md (secciones 4, 7 y 8)"
aliases: [estadística para análisis, estadística aplicada, statistics, inferencia estadística]
creado: 2026-11-27
revisado: 2026-11-27
---

# Estadística

La estadística, en el análisis de negocio, es lo que dice qué se puede concluir de un número: cómo resumir muchos valores sin esconder lo importante, cuánto se puede generalizar desde una muestra, cuándo una relación es causa y qué sesgos hacen que un dato mienta.

No es una etapa del recorrido del dato. El dato se guarda, se transforma, se analiza y se muestra, y la estadística atraviesa el [análisis](../Analisis/analisis.md) y los experimentos sin agregar un tramo. Está como vertical porque es lo que más se estudia por separado. Le da al análisis el criterio para leer un resultado, a la [analítica de producto](../Analitica-de-producto/analitica-de-producto.md) la forma de comparar cohortes y embudos sin engañarse, y a [Visualización y BI](../Visualizacion-y-BI/visualizacion-y-bi.md) el límite de lo que un tablero puede afirmar.

El enfoque es el de quien analiza un comercio o un producto digital, no el de la estadística matemática: importa qué pregunta contesta cada herramienta y cómo falla, más que la demostración.

## Cuatro preguntas antes de creerle a un número

Casi todo error de lectura cae en una de cuatro preguntas. Cada una tiene su nota:

| Pregunta | Qué la contesta | Dónde |
|---|---|---|
| ¿Este número representa a los datos? | El centro, la dispersión y la forma de la distribución | [Estadística descriptiva](estadistica-descriptiva.md) |
| ¿Vale más allá de los casos que miré? | El intervalo, el p-valor, el tamaño de muestra | [Muestreo e inferencia](muestreo-e-inferencia.md) |
| ¿Esto causó aquello? | El contrafactual, el grupo de control, los confusores | [Correlación y causalidad](correlacion-y-causalidad.md) |
| ¿Los datos que tengo dicen lo que parece? | Simpson, supervivencia, selección, regresión a la media | [Sesgos](sesgos.md) |

La quinta nota, [significancia](significancia.md), junta la inferencia con un diseño: cuándo una diferencia entre dos variantes de un experimento es real, y por qué mirar el resultado antes de tiempo o con poco tráfico lo arruina.

El orden de las notas es el de los libros de texto. OpenIntro Statistics, el libro abierto que sirve de referencia, va de resumir datos a los fundamentos de la inferencia y de ahí a la inferencia sobre proporciones y medias. Los sesgos no son un capítulo aparte en el campo. Según la lectura de Pearl que recoge la Stanford Encyclopedia, son casos de inferencia causal: si hay que partir o no una población «depende del modelo causal». Por eso [sesgos](sesgos.md) se lee junto con [correlación y causalidad](correlacion-y-causalidad.md).

## Cómo falla la lectura estadística en un negocio

Las fallas típicas son pocas y se repiten. El promedio esconde a un cliente grande que lo arrastra. Un agregado esconde que, por segmento, la relación es la contraria. Una suba que siguió a una promoción se toma como efecto de la promoción. Un experimento con pocos visitantes «da ganador» y el efecto resulta mucho menor, o del otro signo.

La declaración de la Asociación Estadística de los Estados Unidos (ASA) de 2016 nombra a los negocios en uno de sus seis principios: «Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold». La regla práctica que se desprende es mirar el tamaño del efecto y su incertidumbre, no solo si cruzó un umbral (lectura de la base). Con tráfico bajo, como en la mayoría de los comercios chicos, el problema se agrava: Según su resumen, Gelman y Carlin muestran que un resultado significativo con poca potencia tiende a exagerar el efecto, y a veces tiene el signo equivocado.

La otra falla es la contraria: exigir estadística donde no hace falta. Un tablero de ventas del mes es descriptivo; no necesita un p-valor, necesita una [métrica bien definida](../Analitica-de-producto/definicion-de-metrica.md) y una distribución mirada antes que un promedio.

## Dónde termina la estadística de este tema

Diseñar y decidir un experimento A/B (qué probar, métricas de guarda, cuándo no conviene) es de Producto, en [experimento A/B](../../Producto/Medicion/experimento-ab.md); acá queda el cálculo y su lectura. Medir si un canal causa ventas es [incrementalidad](../../Marketing/Medicion/incrementalidad.md), en Marketing, que usa la misma lógica de grupo de control. Los modelos predictivos y el machine learning quedan fuera del tema.

## Lo que hay adentro de la estadística

- [Estadística descriptiva](estadistica-descriptiva.md) — media, mediana, dispersión y forma de la distribución; el ticket promedio contra la mediana. Se lee primero.
- [Muestreo e inferencia](muestreo-e-inferencia.md) — de una muestra a una población: qué es y qué no es un p-valor según la ASA, intervalos de confianza, tamaño de muestra y potencia.
- [Correlación y causalidad](correlacion-y-causalidad.md) — por qué una relación no prueba una causa, el contrafactual, diferencias en diferencias y el caso de las ventas que suben después de una promoción.
- [Sesgos](sesgos.md) — la paradoja de Simpson con el caso Berkeley, el sesgo de supervivencia, el de selección y la regresión a la media.
- [Significancia](significancia.md) — leer un experimento: frecuentista y bayesiana, mirar antes de tiempo, comparaciones múltiples y tráfico bajo.
