---
resumen: >-
  Una pregunta de análisis es un pedido de información reformulado para que los datos puedan
  contestarlo: nombra la métrica, la población y el período, y dice qué decisión cambia con la
  respuesta.
estado: vigente
estabilidad: semi
fuentes:
  - "Coursera, Ask Questions to Make Data-Driven Decisions (curso 2 del certificado de Google, programa del curso): https://www.coursera.org/learn/ask-questions-make-decisions"
  - "Trusted Institute, SMART questions methodology (guía de terceros sobre el curso 2, según resumen): https://trustedinstitute.com/concept/google-data-analytics/ask-questions-data-driven-decisions/smart-questions-methodology/"
  - "Foster Provost y Tom Fawcett, Data Science for Business, cap. 2 Business Problems and Data Science Solutions (O'Reilly, 2013), por índice y resúmenes: https://oreilly.com/library/view/data-science-for/9781449374273"
  - "IBM, CRISP-DM guide, Business Understanding: determine business objectives (según resumen): https://www.ibm.com/docs/SS3RA7_sub/modeler_crispdm_ddita/clementine/crisp_help/crisp_business_objectives.html"
  - "Purdue CS 49000, CRISP-DM phase 1: business understanding (diapositivas, según resumen): https://www.cs.purdue.edu/homes/jhonorio/22spring-cs49000dsc-phase1-business-understanding.pdf"
  - "Microsoft, The advanced analytics solution building process: business problem formulation (archivo del blog de Machine Learning, según resumen): https://docs.microsoft.com/en-us/archive/blogs/machinelearning/the-advanced-analytics-solution-building-process-business-problem-formulation"
  - "Datos/.investigacion/analisis.md"
aliases: [preguntas SMART, SMART questions, pregunta de negocio, formular la pregunta, business understanding, ask]
creado: 2026-11-27
revisado: 2026-11-27
---

# Pregunta de análisis

Una pregunta de análisis es un pedido de información reformulado para que los datos puedan
contestarlo: nombra la métrica, la población y el período, y dice qué decisión cambia con la
respuesta.

Es la primera fase del [análisis](analisis.md) y, en la lectura de la base, la que más se saltea. Los pedidos llegan como
«¿cómo venimos?» o «quiero un tablero de ventas», y ninguno de los dos se puede contestar con una
consulta. Lo que lo convierte en pregunta es acordar con quien pide qué va a hacer con la
respuesta.

## De un pedido vago a una pregunta contestable

Provost y Fawcett dedican una sección de su capítulo 2 a pasar «from business problems to data
mining tasks». Su punto, según el índice y los resúmenes: los problemas de negocio casi nunca
llegan formulados como una tarea de datos, y alguien tiene que reformularlos. CRISP-DM hace lo
mismo en su primera fase, donde según unas diapositivas de curso separa los objetivos de negocio, en palabras del negocio, de los
objetivos del análisis, en términos técnicos.

| Pedido | Pregunta de análisis | Decisión que cambia |
|---|---|---|
| «¿Cómo venimos?» | ¿Cuánto vendimos en noviembre por canal, comparado con noviembre del año pasado? | Dónde poner el presupuesto de diciembre |
| «Quiero un tablero de ventas» | ¿Qué tres números miramos cada lunes para decidir reposición y promociones? | Qué reponer y qué liquidar |
| «¿La promo funcionó?» | ¿Los clientes que usaron el cupón compraron más en los 60 días siguientes que los que no, y es atribuible al cupón? | Si se repite la promoción |
| «¿Los clientes vuelven?» | ¿Qué parte de los que compraron por primera vez en agosto volvió a comprar en 90 días? | Si conviene invertir en recompra |

Lo que tienen en común las fuentes, como síntesis de esta base: la pregunta nombra la métrica, la
población y el período, y dice qué decisión cambia. Cada número que aparece en ella necesita una
[definición de métrica](../Analitica-de-producto/definicion-de-metrica.md) para que dos personas lo
calculen igual. La tercera pregunta ya pide una causa, y eso cambia el método: ver
[correlación y causalidad](../Estadistica/correlacion-y-causalidad.md). La cuarta es una pregunta de
[retención](../Analitica-de-producto/Retencion-y-churn/retencion.md) y se contesta con
[análisis de cohortes](../Analitica-de-producto/Cohortes/analisis-de-cohortes.md).

## Las preguntas SMART del certificado de Google

El curso 2 del certificado de Google, «Ask Questions to Make Data-Driven Decisions», enseña las
«SMART questions» en su primer módulo; la página del curso no las define. Según una guía de
terceros, las letras son specific, measurable, action-oriented, relevant y time-bound. Su ejemplo:
«Is our website good?» no es SMART; «What was the average session duration and bounce rate for our
homepage during the last quarter?» sí.

La sigla se confunde con SMART de metas, donde la A es «achievable». En las preguntas la A es
«action-oriented»: la respuesta tiene que poder llevar a una acción. Esa es la letra que más
importa, porque es la que ata la pregunta a una decisión.

> [!NOTE]
> Sin fuente todavía: un texto oficial y abierto de Google que defina las preguntas SMART. La
> definición sale de una guía de terceros.

## Predecir o explicar

Antes de elegir el método conviene saber si la pregunta pide predecir o explicar. Microsoft lo
plantea así en su guía de formulación de problemas, según un resumen. «¿Qué clientes van a dejar de
comprar?» pide una predicción: importa acertar, no entender por qué. «¿Por qué dejan de comprar?»
pide una explicación, y es más difícil, porque roza la causa (lectura de la base). La clase de respuesta que se busca es
el vocabulario de los [tipos de analítica](tipos-de-analitica.md).

## Cómo se arma la pregunta con quien la pide

1. Preguntá qué va a decidir con la respuesta. Si no hay decisión, anotá el pedido y no lo analices todavía.
2. Escribí la pregunta con métrica, población y período: «ventas netas», «clientes con al menos una compra», «noviembre de 2026».
3. Escribí cómo se vería una respuesta que cambia la decisión y una que no la cambia. Si las dos llevan a lo mismo, la pregunta sobra.
4. Decidí si pide describir, explicar, predecir o recomendar, y si pide una causa.
5. Revisá que los datos existan: qué tabla tiene esa métrica y qué es [una fila](sql-para-analisis.md#el-grano-qué-es-una-fila) en ella.
6. Mandá la pregunta por escrito a quien la pidió y esperá su acuerdo antes de consultar.

## Cómo falla una pregunta

La falla que más se ve, en la lectura de la base, es una pregunta sin decisión: se contesta, nadie hace nada con la respuesta, y
el tablero que la muestra deja de mirarse. La segunda es una pregunta que cambia de métrica en el
camino («ventas» que al principio eran pedidos y al final facturación). La tercera es una pregunta
causal contestada con datos descriptivos, que es el error que separa la
[analítica diagnóstica](tipos-de-analitica.md#la-diagnóstica-no-prueba-causas) de un experimento.

En producto, una buena pregunta debería colgar de la métrica principal del equipo: la
[North Star](../../Producto/Medicion/north-star.md) o la [activación](../../Producto/Medicion/activacion.md).
En una empresa nueva, de la [métrica que importa](../../Marketing/Medicion/metrica-que-importa.md)
en su etapa.
