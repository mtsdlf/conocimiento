---
resumen: >-
  Un sesgo es una forma sistemática en que los datos llevan a una conclusión equivocada aunque los
  cálculos estén bien: por cómo se agregan (paradoja de Simpson), por quiénes quedaron en la muestra
  (supervivencia y selección) o por haber elegido los casos extremos (regresión a la media).
estado: vigente
estabilidad: estable
fuentes:
  - "Peter Bickel, Eugene Hammel y J. William O'Connell, Sex Bias in Graduate Admissions: Data from Berkeley, Science 187(4175), 398-404, 1975, doi 10.1126/science.187.4175.398 (según su resumen): https://www.science.org/doi/10.1126/science.187.4175.398"
  - "David Freedman, Robert Pisani y Roger Purves, Statistics, 3ª ed. (Norton, 1998), tabla de admisiones de Berkeley reproducida en: https://condor.depaul.edu/sjost/it223/documents/admissions.htm"
  - "Wikipedia, Simpson's paradox, tabla de los seis departamentos más grandes (consultada el 2026-11-27): https://en.wikipedia.org/wiki/Simpson%27s_paradox"
  - "Alex Reinhart, Simpson's Paradox and Statistical Urban Legends: Gender Bias at Berkeley (2016): https://www.refsmmat.com/posts/2016-05-08-simpsons-paradox-berkeley.html"
  - "Stanford Encyclopedia of Philosophy, Simpson's Paradox (rev. 6-jun-2026; según su resumen): https://plato.stanford.edu/entries/paradox-simpson/"
  - "Marc Mangel y Francisco Samaniego, Abraham Wald's Work on Aircraft Survivability, JASA 79(386), 259-267, 1984, doi 10.1080/01621459.1984.10478038 (no se leyó)"
  - "AMS Feature Column, The Legend of Abraham Wald (2016; según el resumen del buscador): https://www.ams.org/samplings/feature-column/fc-2016-06"
  - "Adrian Barnett, Jolieke van der Pols y Annette Dobson, Regression to the mean: what it is and how to deal with it, Int J Epidemiol 34(1), 215-220, 2005 (abstract): https://pubmed.ncbi.nlm.nih.gov/15333621/"
  - "OpenIntro Statistics, cap. 1, Intro to Data (solo la página del libro): https://www.openintro.org/book/os/"
  - "Datos/.investigacion/estadistica.md"
  - "Datos/.investigacion/posicion-contraria.md (sección 7)"
aliases: [sesgos estadísticos, paradoja de Simpson, Simpson's paradox, sesgo de supervivencia, survivorship bias, sesgo de selección, selection bias, regresión a la media, regression to the mean]
creado: 2026-11-27
revisado: 2026-11-27
---

# Sesgos

Un sesgo es una forma sistemática en que los datos llevan a una conclusión equivocada aunque los cálculos estén bien: por cómo se agregan (paradoja de Simpson), por quiénes quedaron en la muestra (supervivencia y selección) o por haber elegido los casos extremos (regresión a la media).

A diferencia del azar, que la [inferencia](muestreo-e-inferencia.md) mide con intervalos, un sesgo no se achica con más datos: un conjunto grande y mal elegido sigue sesgado. Casi todos se explican por una variable que no se miró, y por eso esta nota se lee con [correlación y causalidad](correlacion-y-causalidad.md).

## Paradoja de Simpson

La paradoja de Simpson es cuando una relación entre dos variables aparece, desaparece o se invierte al partir la población en grupos; la Stanford Encyclopedia dice que la asociación «emerges, disappears or reverses». El nombre viene de un trabajo de Simpson de 1951, con antecedentes en Pearson (1899) y Yule (1903).

El caso canónico son las admisiones a posgrado de la Universidad de California en Berkeley, otoño de 1973. Postularon 8.442 hombres y 4.321 mujeres; fue admitido el 44 % de los hombres y el 35 % de las mujeres. Parecía discriminación. La tabla de los seis departamentos más grandes, en Freedman, Pisani y Purves:

| Departamento | Hombres: postulantes | Hombres: admitidos | Mujeres: postulantes | Mujeres: admitidas |
|---|---|---|---|---|
| A | 825 | 62 % | 108 | 82 % |
| B | 560 | 63 % | 25 | 68 % |
| C | 325 | 37 % | 593 | 34 % |
| D | 417 | 33 % | 375 | 35 % |
| E | 191 | 28 % | 393 | 24 % |
| F | 373 | 6 % | 341 | 7 % |

Dentro de cada departamento las tasas son parecidas o favorecen a las mujeres, salvo en C y E. La diferencia del total sale de otro lado: casi todas las mujeres postularon a departamentos que admiten poco, y pocas a A y B, los que más admiten, mientras que más de la mitad de los hombres de la tabla postuló a esos dos (cálculo de la base). Según el resumen del artículo de Bickel, Hammel y O'Connell (1975), al ponderar por departamento aparece «a small but statistically significant bias in favor of women».

> [!WARNING]
> Tres salvedades. El artículo analiza 85 departamentos; los seis de la tabla son la versión de un libro de texto, cotejada con la que reproduce Wikipedia («Simpson's paradox», consultada el 2026-11-27) y no con el libro impreso, y la conclusión del artículo se leyó solo por resumen. Muchos textos dicen que Berkeley fue demandada; Reinhart, citando una entrevista a Bickel, sostiene que nunca hubo demanda, solo el temor a una. Y la lectura causal de la paradoja es de Pearl: la Stanford Encyclopedia recoge también explicaciones no causales.

Lo que enseña el caso: si conviene mirar el total o los grupos lo decide cómo se causan las cosas, no los números. En Berkeley, el departamento influye en la admisión y en a dónde postula cada uno, así que hay que partir por departamento. En un comercio pasa lo mismo con la tasa de conversión por canal y dispositivo: un canal puede convertir mejor en cada dispositivo y peor en el total si trae más tráfico de celular, que convierte menos (ilustración de la base).

## Sesgo de supervivencia

El sesgo de supervivencia es sacar conclusiones solo de los casos que pasaron un filtro, sin ver los que no lo pasaron. La versión que circula es la de Abraham Wald en la Segunda Guerra: los aviones que volvían tenían impactos en ciertas zonas, y Wald habría recomendado blindar las otras, porque los aviones tocados ahí no volvían.

> [!WARNING]
> La Feature Column de la AMS llama «legend» a ese relato y dice que la única fuente fiable son los escritos técnicos de Wald, sus memorias de 1943 para el Statistical Research Group de Columbia. Los detalles populares (motores, el dibujo de impactos) no se verificaron en esas memorias ni en Mangel y Samaniego (1984). Hay una sola fuente de peso, leída por resumen.

En negocio aparece cuando se estudia a los clientes que se quedaron para saber qué hace volver a la gente, sin mirar a los que se fueron, o cuando se copian las prácticas de los comercios exitosos sin saber cuántos hicieron lo mismo y cerraron (ilustración de la base). El [análisis de cohortes](../Analitica-de-producto/Cohortes/analisis-de-cohortes.md) lo evita porque sigue a todos los que entraron juntos, también a los que se fueron.

## Sesgo de selección

El sesgo de selección aparece cuando la forma en que se eligió la muestra la hace distinta de la población sobre la que se quiere concluir. El de supervivencia es un caso particular. Ejemplos de comercio: una encuesta de satisfacción que responden sobre todo los clientes muy contentos o muy enojados; reseñas que deja una minoría; un análisis de comportamiento hecho solo con usuarios logueados (ilustraciones de la base). OpenIntro trata el muestreo sesgado en su capítulo 1.

> [!NOTE]
> Sin fuente todavía: una fuente de referencia sobre sesgo de selección (un texto de epidemiología o el capítulo 1 de OpenIntro, leído).

## Regresión a la media

La regresión a la media, según el abstract de Barnett, van der Pols y Dobson (2005), «is a statistical phenomenon that can make natural variation in repeated data look like real change. It happens when unusually large or small measurements tend to be followed by measurements that are closer to the mean». Se nota más cuando hay mucho ruido y cuando se sigue a un grupo elegido por su valor inicial. Los autores concluyen que «should always be considered as a possible cause of an observed change».

En negocio, la trampa es elegir lo extremo y actuar. Se toman las tres sucursales con peor mes, se les cambia el encargado, y al mes siguiente mejoran. Parte de la mejora habría ocurrido igual, porque un mes muy malo suele tener una parte de mala suerte que no se repite (ilustración de la base). La defensa es la de siempre: un grupo de comparación igual de malo que no recibió el cambio. Es también una de las explicaciones a descartar antes de atribuirle una suba a una promoción, en [correlación y causalidad](correlacion-y-causalidad.md#las-ventas-subieron-después-de-una-promoción-la-causó).

Según un resumen secundario (Bohrium, no leído), hay una corrección de 2015 al artículo por un error en la fórmula del efecto esperado; quien use la fórmula, que la tome de la versión corregida.

## Leer el caso Berkeley

Para Simpson, conviene la tabla de los seis departamentos con el aviso de Reinhart sobre la demanda que nunca existió, y después la entrada de la Stanford Encyclopedia para la discusión sobre si la paradoja es causal. En los dos, fijarse en que la explicación siempre es una tercera variable y en que partir o no partir depende de la causa.
