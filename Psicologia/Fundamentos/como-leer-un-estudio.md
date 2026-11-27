---
resumen: >-
  Leer un estudio de psicología es decidir cuánto creerle a un hallazgo mirando cinco cosas: si el diseño permite hablar de causa, qué tan grande es el efecto, qué tan grande y de dónde es la muestra, si el análisis se fijó antes de ver los datos y si otros lo repitieron. El p-valor solo no alcanza.
estado: borrador
estabilidad: estable
fuentes:
  - "Wasserstein y Lazar (2016), ASA Statement on p-Values (texto completo): https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf (DOI https://doi.org/10.1080/00031305.2016.1154108)"
  - "Lakens (2021), The Practical Alternative to the p Value Is the Correctly Used p Value, Perspectives on Psychological Science (abstract): https://doi.org/10.1177/1745691620958012"
  - "Funder y Ozer (2019), Evaluating effect size in psychological research, AMPPS (abstract): https://doi.org/10.1177/2515245919847202"
  - "Button et al. (2013), Nature Reviews Neuroscience (abstract): https://doi.org/10.1038/nrn3475"
  - "Henrich, Heine y Norenzayan (2010), The weirdest people in the world?, BBS (abstract): https://doi.org/10.1017/S0140525X0999152X"
  - "Thalmayer, Toscanelli y Arnett (2021), The neglected 95% revisited, American Psychologist (abstract): https://doi.org/10.1037/amp0000622"
  - "Rad, Martingano y Ginges (2018), PNAS (abstract): https://doi.org/10.1073/pnas.1721165115"
  - "Schäfer y Schwarz (2019), Frontiers in Psychology (abstract): https://doi.org/10.3389/fpsyg.2019.00813"
  - "Scheel, Schijen y Lakens (2021), AMPPS (abstract): https://doi.org/10.1177/25152459211007467"
  - "Klein et al. (2018), Many Labs 2, AMPPS (abstract): https://doi.org/10.1177/2515245918810225"
  - "Sisk et al. (2018), metaanálisis de mentalidad de crecimiento, Psychological Science (abstract): https://doi.org/10.1177/0956797617739704"
  - "Liu, Ein, Gervasio y Vickers (2019), metaanálisis de reevaluación del estrés, PLOS ONE (lectura parcial): https://pmc.ncbi.nlm.nih.gov/articles/PMC6392321"
  - "Mertens et al. (2022), The effectiveness of nudging, PNAS (abstract): https://doi.org/10.1073/pnas.2107346118"
  - "Moffitt et al. (2011), PNAS (abstract): https://doi.org/10.1073/pnas.1010076108"
  - "Keller et al. (2012), Health Psychology (abstract): https://doi.org/10.1037/a0026743"
  - "Doyen et al. (2012), PLOS ONE (abstract): https://doi.org/10.1371/journal.pone.0029081"
  - "Flake y Fried (2020), Measurement schmeasurement, AMPPS (abstract): https://doi.org/10.1177/2515245920952393"
  - "Stieger et al. (2021), PNAS (abstract): https://pmc.ncbi.nlm.nih.gov/articles/PMC7923371"
  - "Psicologia/.investigacion/fundamentos.md, secciones 3 y 4"
  - "Psicologia/.investigacion/posicion-contraria.md, sección 1"
aliases: [cómo leer un paper, how to read a study, lectura crítica de estudios, tamaño de efecto, p-valor, metaanálisis, preregistro, WEIRD]
creado: 2026-11-27
revisado:
---

# Cómo leer un estudio

Leer un estudio de psicología es decidir cuánto creerle a un hallazgo mirando cinco cosas: si el diseño permite hablar de causa, qué tan grande es el efecto, qué tan grande y de dónde es la muestra, si el análisis se fijó antes de ver los datos y si otros lo repitieron. El p-valor solo no alcanza.

La [crisis de replicación](crisis-de-replicacion.md) mostró por qué hace falta: en Many Labs 2, el tamaño de efecto mediano de 28 hallazgos clásicos bajó de d = 0,60 en los originales a d = 0,15 en las réplicas. Las preguntas que siguen sirven para un paper, para un libro de divulgación que lo cita y para una charla que lo cuenta.

## Correlación o experimento

Un experimento asigna al azar quién recibe qué; un estudio observacional mide lo que ya pasa. Solo el primero permite hablar de causa con cierta seguridad, y aun así puede fallar.

Dos ejemplos de este tema muestran el límite de lo observacional. Moffitt et al. (2011) siguieron a 1.000 niños hasta los 32 años y hallaron que el autocontrol infantil predice salud, finanzas y delitos, aun separando inteligencia y clase social; sigue siendo una asociación en una cohorte. Keller et al. (2012) hallaron un 43 % más de riesgo de muerte prematura en quienes tenían mucho estrés y creían que los afectaba mucho, pero quien ya está enfermo puede percibir más daño: la dirección causal es incierta.

Un experimento también puede engañar. En Doyen et al. (2012), el efecto de priming de caminar más lento apareció solo cuando los experimentadores esperaban verlo: la expectativa de los experimentadores actuaba como factor de confusión.

> [!NOTE]
> Sin fuente todavía: una fuente didáctica sobre correlación y causalidad. OpenStax Psychology 2e, capítulo 2, la tiene, pero no se leyó.

## Qué dice y qué no dice un p

El p-valor mide cuán incompatibles son los datos con un modelo, típicamente el de «no hay efecto». La declaración de la American Statistical Association (2016), leída entera, da seis principios. Tres de ellos:

- «P-values do not measure the probability that the studied hypothesis is true, or the probability that the data were produced by random chance alone.»
- «Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold.»
- «A p-value, or statistical significance, does not measure the size of an effect or the importance of a result.»

Lakens (2021) defiende no abandonar el p sino usarlo mejor, con pruebas de efecto mínimo y de equivalencia. Es una postura, no un consenso.

## Cuánto es grande: el tamaño de efecto

El tamaño de efecto dice cuánto, no solo si hay algo. Los dos que más aparecen en el tema son r, una correlación entre −1 y 1, y d de Cohen, la diferencia entre dos grupos expresada en desvíos estándar. Funder y Ozer (2019) proponen esta escala para r en psicología:

| r | Cómo leerlo (Funder y Ozer) |
|---|---|
| 0,05 | Muy chico para un hecho aislado, pero puede pesar a la larga |
| 0,10 | Chico en un hecho aislado, con más consecuencias a la larga |
| 0,20 | Mediano, de alguna utilidad práctica aun en el corto plazo |
| 0,30 | Grande, potente en el corto y en el largo plazo |
| 0,40 o más | «likely to be a gross overestimate that will rarely be found in a large sample or in a replication» |

También advierten contra los umbrales arbitrarios y contra elevar r al cuadrado para juzgarlo. Un ejemplo de este tema: la responsabilidad, el rasgo que mejor predice el desempeño laboral, lo hace con ρ = 0,19 ([Cinco Grandes](../Personalidad/cinco-grandes.md)).

> [!NOTE]
> Sin fuente todavía: los umbrales clásicos de Cohen para d (0,2, 0,5 y 0,8, de 1988). Circulan mucho, pero el informe no los verificó.

## Por qué el efecto publicado suele ser más grande que el real

Un tamaño publicado es, en promedio, mayor que el real. Schäfer y Schwarz (2019) hallaron una mediana de r = 0,36 en efectos sin preregistro y de 0,16 con preregistro, y Many Labs 2 vio caer los efectos a una cuarta parte. Conviene descontar el número de un estudio único que nadie repitió.

La muestra chica empeora las cosas. Button et al. (2013) muestran que un estudio con poco poder no solo tiene menos chances de detectar un efecto verdadero: «low power also reduces the likelihood that a statistically significant result reflects a true effect». Sus datos son de neurociencia, no de psicología, así que vale como paralelo.

## Preregistro y registered reports

Preregistrar es dejar escritas la hipótesis, la muestra y el análisis antes de juntar los datos, para que no se ajusten después. Un informe registrado (*registered report*) va más lejos: la revista acepta el estudio por su diseño, antes de ver los resultados. Scheel, Schijen y Lakens (2021) hallaron 96 % de resultados positivos en artículos estándar y 44 % en informes registrados.

Un estudio preregistrado no es automáticamente verdadero, pero su p-valor significa lo que dice. Uno que no lo está pudo haber probado varios análisis y reportado el que dio.

## Metaanálisis: el promedio de muchos estudios

Un metaanálisis combina los resultados de muchos estudios sobre la misma pregunta. Hereda el sesgo de publicación de lo que junta, y por eso importa si lo corrige.

Tres casos del tema lo muestran. Sisk et al. (2018) hicieron dos metaanálisis sobre mentalidad de crecimiento, uno de su relación con el rendimiento (k = 273) y otro de las intervenciones (k = 43), y concluyeron «Overall effects were weak for both meta-analyses». Según una lectura parcial del metaanálisis de Liu et al. (2019) sobre reevaluar el estrés, el efecto subjetivo cayó de 0,43 a 0,20 después de corregir el sesgo de publicación. Mertens et al. (2022) hallaron un efecto de los nudges de d = 0,45 con «a moderate publication bias»; la disputa sobre cuánto queda al corregirlo está en [juicio y decisión](../Juicio-y-decision/juicio-y-decision.md#los-nudges-en-la-frontera).

> [!NOTE]
> Sin fuente todavía: cómo funcionan las técnicas para detectar y corregir el sesgo de publicación (funnel plot, trim-and-fill, p-curve).

## Quiénes son los participantes: WEIRD

La mayoría de los estudios usa muestras WEIRD: «Western, Educated, Industrialized, Rich, and Democratic». Henrich, Heine y Norenzayan (2010) muestran que los resultados varían bastante entre poblaciones y que esas muestras son «frequent outliers» respecto del resto de la especie. Thalmayer et al. (2021) hallaron que, en seis revistas de punta, la proporción de muestras de EE. UU. bajó de más del 70 % a «a little over 60 %», con el resto viniendo sobre todo de otros países angloparlantes y de Europa occidental.

Para un lector de Argentina, un hallazgo con estudiantes estadounidenses es una hipótesis sobre otra población.

## Qué se midió y con qué

Muchos constructos se miden con cuestionarios que la persona responde sobre sí misma, el autoinforme. Flake y Fried (2020) sostienen que las prácticas de medición dudosas son comunes: «QMPs are common, hide a stunning source of researcher degrees of freedom». La diferencia entre lo que la persona dice y lo que ven otros puede ser grande: en Stieger et al. (2021), quienes quisieron bajar un rasgo de personalidad reportaron un cambio de d = −0,58, pero los observadores no vieron un cambio significativo ([cambio de personalidad](../Personalidad/cambio-de-personalidad.md)).

## Las preguntas antes de creerle a un hallazgo

1. ¿Es un experimento o una correlación? Si es correlación, buscá la tercera variable que podría explicar las dos.
2. ¿Cuánto es el efecto? Pedí el tamaño, no solo «significativo», y compará con la tabla de Funder y Ozer.
3. ¿Cuántas personas y de dónde? Una muestra chica y WEIRD es una pista, no una conclusión.
4. ¿Estaba preregistrado? Si no, descontá el número.
5. ¿Alguien lo repitió? Buscá el efecto en [crisis de replicación](crisis-de-replicacion.md) o en la nota del mecanismo, que dice su estado.
6. ¿Se midió conducta o autoinforme? Si es autoinforme, preguntá qué vería un tercero.

## Qué leer para aprender a leer estudios

Funder y Ozer (2019), la tabla de referencias para r; la declaración de la ASA, dos páginas con los seis principios; y Henrich et al. (2010), el abstract y la comparación entre poblaciones. Para correlación y causalidad, OpenStax Psychology 2e, capítulo 2, todavía sin leer para esta base.
