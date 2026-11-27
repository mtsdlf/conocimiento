---
resumen: >-
  La teoría de respuesta al ítem (IRT) modela la probabilidad de acertar una pregunta según la habilidad de la persona y los rasgos de la pregunta. Es la base de los tests adaptativos computarizados, que eligen cada pregunta según las anteriores, y necesita un banco de preguntas calibrado con muchas personas.
estado: vigente
estabilidad: estable
fuentes:
  - "Hambleton y Jones (1993), Comparison of classical test theory and item response theory and their applications to test development, Educational Measurement: Issues and Practice 12(3):38-47 (texto completo, módulo ITEMS de NCME): https://ncme.org/wp-content/uploads/2025/10/Module-16-Comparison-of-CTT-and-IRT-Hambleton-J-1.pdf"
  - "Wikipedia, Item response theory: https://en.wikipedia.org/wiki/Item_response_theory"
  - "Wikipedia, Computerized adaptive testing: https://en.wikipedia.org/wiki/Computerized_adaptive_testing"
  - "König, Spoden y Frey (2019), Applied Psychological Measurement (abstract): https://doi.org/10.1177/0146621619893786"
  - "Şahin y Weiss (2015), Educational Sciences: Theory & Practice (abstract): https://doi.org/10.12738/estp.2015.6.0102"
  - "Ree (1981), Applied Psychological Measurement (abstract): https://doi.org/10.1177/014662168100500102"
  - "Linacre (1994), Sample size and item calibration stability, Rasch Measurement Transactions 7(4) (resumen de herramienta): https://www.rasch.org/rmt/rmt74m.htm"
  - "Weiss y Kingsbury (1984), Application of computerized adaptive testing to educational problems, Journal of Educational Measurement (abstract): https://doi.org/10.1111/j.1745-3984.1984.tb01040.x"
  - "Evaluacion-educativa/.investigacion/adaptativa-calificacion-programa.md"
  - "Evaluacion-educativa/.investigacion/fuentes-adaptativa-2026-11.md"
aliases: [IRT, item response theory, TRI, modelo de Rasch, Rasch, teoría clásica de los tests, CTT, test adaptativo computarizado, CAT, computerized adaptive testing]
creado: 2026-11-27
revisado: 2026-11-27
---

# Teoría de respuesta al ítem

La teoría de respuesta al ítem (IRT) modela la probabilidad de acertar una pregunta según la habilidad de la persona y los rasgos de la pregunta. Es la base de los tests adaptativos computarizados, que eligen cada pregunta según las anteriores, y necesita un banco de preguntas calibrado con muchas personas.

Es la rama psicométrica de la [evaluación adaptativa](evaluacion-adaptativa.md). Devuelve un número, la habilidad estimada en una escala, a diferencia de los [espacios de conocimiento](espacios-de-conocimiento.md), que devuelven qué temas se dominan.

## En qué se diferencia de la teoría clásica

La teoría clásica de los tests suma aciertos y estima el error para el test entero. La IRT, según Wikipedia, se diferencia en tres cosas: no supone que todas las preguntas sean igual de difíciles, deja que el error de medición varíe entre personas y sus parámetros, en teoría, no dependen de la muestra ni del test.

Hambleton y Jones (1993) hacen el mismo contraste. En la teoría clásica, los parámetros de la pregunta y de la persona dependen del grupo que la respondió, y el puntaje depende de qué tan difícil fue el test. En la IRT, los parámetros de la pregunta y de la persona son independientes de la muestra, «if model fits the test data». Por eso la IRT sirve para comparar a personas que rindieron tests distintos, como en un test adaptativo.

La teoría clásica tiene otras ventajas, según los mismos autores. Necesita muestras más chicas y cálculos más simples, y sus supuestos son «weak», fáciles de cumplir con datos reales. Los de la IRT son «strong», más difíciles de cumplir, y el ajuste del modelo puede fallar.

Los modelos se distinguen por cuántos rasgos de la pregunta estiman:

| Modelo | Rasgos de la pregunta |
|---|---|
| 1PL o Rasch | Dificultad |
| 2PL | Dificultad y discriminación (cuánto separa a los que saben de los que no) |
| 3PL | Lo anterior más el acierto por azar; en una pregunta de cuatro opciones ronda 0,25 |

Hambleton y Jones llaman a los tres parámetros «item difficulty, item discrimination, and pseudoguessing». El 2PL sale de fijar en cero el acierto por azar, y el 1PL, de fijar además la discriminación.

La escuela de Rasch no ve su modelo como un caso particular de la IRT sino como otro enfoque: prioriza la medición fundamental y trata los datos que no encajan como un problema a diagnosticar, no a absorber con más parámetros.

## Cuánta gente hace falta

Para calibrar las preguntas hacen falta respuestas de muchas personas, y las fuentes no coinciden en cuántas:

| Fuente | Qué dice |
|---|---|
| Hambleton y Jones (1993), comparación general | Teoría clásica: «200 to 500 (in general)». IRT: depende del modelo, pero «over 500, in general, are needed» |
| Linacre (1994), Rasch | De 16 a 36 personas para que la dificultad quede estable dentro de ±1 logit; 30 como mínimo recomendado; 50 bien apuntadas, «conservative»; 250 para decisiones de alto riesgo |
| Şahin y Weiss (2015), simulación de un test adaptativo | Con una muestra de calibración de 150 se obtienen «accurate ability parameter estimates» con un banco de 500 preguntas |
| Ree (1981), simulación 3PL | Reducir el error «required at least 200 items calibrated on 2,000 subjects» |
| König, Spoden y Frey (2019), 2PL | La recomendación habitual es una muestra grande; proponen un método bayesiano para achicarla (las cifras no figuran en el abstract) |

Una cifra de «150 a 500 personas» que se menciona es una simplificación. Para un grupo chico, el cuello de botella no es solo la gente sino el banco: cientos de preguntas ya calibradas. Esto último es inferencia del informe de esta base a partir de Ree y de Şahin y Weiss.

## El test adaptativo computarizado

Un test adaptativo computarizado (CAT) arranca suponiendo una habilidad media, elige la pregunta más informativa para la estimación actual, actualiza la estimación con cada respuesta y corta cuando el error baja de un umbral. Según Wikipedia, existe desde los años 70, se usa en pruebas de admisión y de gran escala y acorta el test «typically by 50%» con más precisión que la versión fija. Tiene límites: no se puede lanzar con preguntas sin calibrar, expone las preguntas del banco, no deja volver atrás y, con tiempo límite, no sirve para decisiones de alto riesgo.

Weiss y Kingsbury (1984) describen tres usos escolares: decidir si se dominó un contenido, calificar y medir el cambio. Según el abstract, para decidir el dominio el test adaptativo clasificó con más exactitud que el convencional y con menos preguntas.

## Cuándo vale la pena

Un CAT paga cuando hay muchos examinados, un banco grande ya calibrado y consecuencias que justifican el costo. Con un curso o una mentoría de decenas de personas, armar y calibrar el banco no se recupera. Lo que se lleva es el principio: no gastar preguntas muy fáciles ni muy difíciles para esa persona. A mano alcanza con 5 a 10 preguntas ordenadas por dificultad y un corte simple, sin IRT. Las dos conclusiones son inferencias del informe, no resultados medidos.

> [!NOTE] Sin fuente todavía: un manual leído (Embretson y Reise, 2000; Wainer, 2000). Salvo Hambleton y Jones (1993), leído entero, lo de esta nota viene de abstracts y de Wikipedia.
