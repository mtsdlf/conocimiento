---
resumen: >-
  El test de usabilidad es el método en que un facilitador pide tareas realistas a un participante parecido al usuario real y observa dónde se traba. Con pocos participantes sirve para encontrar y corregir los problemas más frecuentes de un grupo homogéneo, no para garantizar que se encontraron todos.
estado: vigente
estabilidad: semi
fuentes:
  - "NN/g, Usability Testing 101: https://www.nngroup.com/articles/usability-testing-101/ (leída a través del resumen de una herramienta)"
  - "Jakob Nielsen (2000), Why You Only Need to Test with 5 Users: https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/ (leída a través del resumen de una herramienta)"
  - "NN/g (2012), How Many Test Users in a Usability Study?: https://www.nngroup.com/articles/how-many-test-users/ (leída a través del resumen de una herramienta)"
  - "Nielsen y Landauer (1993), A mathematical model of the finding of usability problems, INTERCHI (leído a través de NN/g y del buscador; el PDF dio 404)"
  - "Spool y Schroeder (2001), Testing web sites: five users is nowhere near enough, CHI EA, pp. 285-286: https://dblp.uni-trier.de/rec/conf/chi/SpoolS01.html (solo metadatos y resúmenes)"
  - "Faulkner (2003), Beyond the five-user assumption, Behav Res Methods Instrum Comput 35(3):379-383: https://pubmed.ncbi.nlm.nih.gov/14587545/ (cifras vía resúmenes)"
  - "Hwang y Salvendy (2010), Number of People Required for Usability Evaluation: The 10±2 Rule, CACM (vía resúmenes): https://cacm.acm.org/research/number-of-people-required-for-usability-evaluation"
  - "Baymard Institute, metodología: https://baymard.com/research/methodology"
  - "UX/.investigacion/investigacion-y-evaluacion.md y UX/.investigacion/posicion-contraria.md"
aliases: [test de usuarios, prueba de usabilidad, usability testing, test con usuarios]
creado: 2026-11-22
revisado: 2026-11-22
---

# Test de usabilidad

El test de usabilidad es el método en que un facilitador pide tareas realistas a un participante parecido al usuario real y observa dónde se traba. Con pocos participantes sirve para encontrar y corregir los problemas más frecuentes de un grupo homogéneo, no para garantizar que se encontraron todos.

Es una técnica de la [evaluación](evaluacion.md). NN/g lo ubica en la fase de diseño, como método formativo, y es a la vez de [investigación](../Investigacion/metodos-de-investigacion.md). Sus métricas habituales parten de ISO 9241-11: eficacia, eficiencia y satisfacción.

## Qué tiene un test

Según NN/g, un test tiene tres componentes. El facilitador conduce la sesión. Las tareas son "realistic activities". El participante es "a realistic user… or someone with a similar background or needs". El facilitador observa la conducta y escucha. En la variante think-aloud, se pide al participante que narre sus acciones y pensamientos mientras trabaja (NN/g; la fuente primaria no se leyó).

Hay dos formatos remotos. En el moderado, facilitador y participante están en lugares distintos pero conectados en vivo. En el no moderado, una herramienta entrega las tareas por escrito y el investigador revisa después las grabaciones y métricas como éxito de tarea. Lo que se mide en un test está en [métricas de UX](metricas-de-ux.md).

## De dónde sale la regla de los cinco usuarios

Según el buscador (el paper de 1993 no se leyó), Nielsen y Landauer modelaron el hallazgo de problemas como un proceso de Poisson sobre 11 estudios, con independencia entre tests. La fórmula que NN/g da es N × (1 − (1 − L)^n): N es el total de problemas, L la proporción que descubre un usuario y n la cantidad de usuarios. El valor típico de L, promediado entre proyectos, es 31%. Con L = 31% y n = 5, la fórmula da 1 − 0,69^5, cerca de 84% (cálculo de esta base). El buscador atribuye al artículo de 2000 una cifra de 85% con cinco usuarios, y NN/g (2012) la atribuye a un modelo de 11 estudios; esa cifra no se leyó en la página.

La recomendación de Nielsen (2000, 18 de marzo) dice, según el resumen de NN/g: "The best results come from testing no more than 5 users and running as many small tests as you can afford." Con grupos distintos propone de 3 a 4 por categoría si son dos grupos, y 3 por categoría si son tres o más. Y agrega: "Spend this budget on 3 studies with 5 users each!" El modelo supone usuarios comparables que usan el producto de manera parecida.

> [!IMPORTANT]
> Cuántos participantes hacen falta es una discusión abierta.
>
> A favor de cinco para iterar: Nielsen (2000) sostiene que, tras cinco usuarios, los problemas empiezan a repetirse y que rinde más correr varios tests chicos con rediseño en el medio. La defensa habitual agrega que los problemas graves y frecuentes aparecen antes que los raros.
>
> En contra de que alcancen como garantía de cobertura: Spool y Schroeder (2001) pidieron la misma tarea a 49 usuarios en cuatro sitios en producción y, según los resúmenes (solo metadatos leídos), los sitios necesitarían bastante más de cinco usuarios para llegar a 85%. Faulkner (2003) tomó 60 usuarios y submuestras al azar: algunos grupos de cinco encontraron 99% de los problemas y otros solo 55%; con 20 usuarios el peor grupo llegó a 95% (cifras de resúmenes, sin verificar en el original). Hwang y Salvendy (2010), en un metaanálisis de 36 puntos de 27 experimentos, proponen 10±2 para 80% de descubrimiento (según el resumen); un artículo posterior de CACM, también según un resumen, la critica y propone 16 para 80% en un conjunto de datos de referencia.
>
> Otras instituciones usan otro número. Baymard no usa cinco: justifica 20 participantes con un cálculo binomial, "20 participants will uncover about 95% of problems with an occurrence rate of 14% or higher", y admite que lo que ocurre en menos de 14% de los casos puede perderse.
>
> Las fuentes secundarias discrepan sobre el piso con 10 usuarios en Faulkner (80% según el abstract, 82% según un boletín). La lectura prudente: cinco es una regla de iteración sobre problemas frecuentes de un grupo homogéneo, no una garantía.

## Cuándo se necesitan más de cinco

Para métricas cuantitativas, NN/g (2012) recomienda "test at least 20 users to get statistically significant numbers", y 39 para mapas de calor estables en eyetracking. El card sorting pide 15 por grupo. Para un estudio cualitativo mantiene: "test 5 users in a qualitative usability study". El rango de 20 a 40 que circula para estudios cuantitativos no figura en esa página y queda sin confirmar.

La regla de cinco tampoco se traslada a las [entrevistas de usuario](../Investigacion/entrevista-de-usuario.md), que tienen otra cifra y otro objetivo.

## Cómo se combina con la heurística

NN/g aconseja alternar con la [evaluación heurística](evaluacion-heuristica.md), empezando por ella. Las fuentes leídas no registran el porqué de ese orden. La heurística no reemplaza al test.

## Qué leer

Para el cómo, NN/g, [Usability Testing 101](https://www.nngroup.com/articles/usability-testing-101/). Para el debate de la cantidad, Nielsen, [Why You Only Need to Test with 5 Users](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/), junto con Faulkner (2003) como contrapeso: conviene fijarse en el valor de L, en que varía entre estudios y en el rango de 55 a 100% de los grupos de cinco. Para tamaños cuantitativos, Sauro y Lewis, Quantifying the User Experience (no leído).

> [!NOTE]
> Sin fuente todavía: la fuente primaria del think-aloud; la cifra de 35% de problemas con los primeros cinco usuarios de Spool y Schroeder, que circula en listas y no se verificó; y el tamaño de muestra de estudios cuantitativos de MeasuringU, cuya página no estuvo disponible. Las cifras y citas de NN/g salen de un resumen que una herramienta hizo de cada página: conviene cotejarlas en el original antes de entrecomillarlas.
