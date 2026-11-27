---
resumen: >-
  Los tipos de analítica son cuatro clases de pregunta que un análisis puede contestar: qué pasó
  (descriptiva), por qué pasó (diagnóstica), qué va a pasar (predictiva) y qué conviene hacer
  (prescriptiva).
estado: borrador
estabilidad: estable
fuentes:
  - "destinationCRM, Gartner Data & Analytics Summit 2017 Day 2: The Evolution of Analytics (08-03-2017), con Peter Krensky: https://www.destinationcrm.com/Articles/CRM-News/CRM-Featured-Articles/Gartner-Data-and-Analytics-Summit-2017-Day-2-The-Evolution-of-Analytics-116832.aspx"
  - "Lepenioti et al., Prescriptive analytics: Literature review and research challenges, International Journal of Information Management 50 (2020) 57-70, DOI 10.1016/j.ijinfomgt.2019.04.003 (solo abstract): https://ideas.repec.org/a/eee/ininma/v50y2020icp57-70.html"
  - "Gartner, Are You an Analytic Business or Just Using Business Analytics? (2015, según resumen): https://www.gartner.com/en/newsroom/press-releases/2015-02-16-are-you-an-analytic-business-or-just-using-business-analytics"
  - "Playfair Data, 3 Reasons the Analytics Maturity Framework Is Broken (según resumen): https://playfairdata.com/3-reasons-the-analytics-maturity-framework-is-broken-and-whats-better/"
  - "Motio, Rethinking the analytics maturity model (según resumen): https://motio.com/rethinking-the-analytics-maturity-model/"
  - "Datos/.investigacion/analisis.md"
  - "Datos/.investigacion/posicion-contraria.md (sección 6)"
aliases: [analítica descriptiva, analítica diagnóstica, analítica predictiva, analítica prescriptiva, descriptive analytics, predictive analytics, prescriptive analytics, Analytic Ascendancy Model, escalera de la analítica]
creado: 2026-11-27
revisado:
---

# Tipos de analítica

Los tipos de analítica son cuatro clases de pregunta que un análisis puede contestar: qué pasó
(descriptiva), por qué pasó (diagnóstica), qué va a pasar (predictiva) y qué conviene hacer
(prescriptiva).

Sirven para saber qué clase de respuesta se busca antes de empezar el
[análisis](analisis.md), y para no prometer una respuesta de una clase con herramientas de otra.
Son vocabulario, no un método: no dicen cómo se hace cada una ni en qué orden.

## Las cuatro preguntas según Gartner

El marco viene de Gartner. Peter Krensky, analista de la consultora, lo resumió así en su
conferencia de 2017: «descriptive analytics, which identify what happened»; «diagnostic analytics,
which identify how it happened»; «predictive analytics, which identify what will happen»;
«prescriptive analytics, which identify what should be done». Bajo predictiva puso «predictions,
forecasting, and simulation», y bajo prescriptiva, «rules and optimization».

| Tipo | Pregunta | En un comercio | Con qué se contesta |
|---|---|---|---|
| Descriptiva | ¿Qué pasó? | Cuánto se vendió por mes y por canal | Agregaciones y gráficos: [SQL para análisis](sql-para-analisis.md), [tablero](../Visualizacion-y-BI/tablero.md) |
| Diagnóstica | ¿Por qué pasó? | Por qué bajaron las ventas de octubre | Desagregar y comparar: [análisis exploratorio](analisis-exploratorio.md), [segmentación de clientes](segmentacion-de-clientes.md) |
| Predictiva | ¿Qué va a pasar? | Cuánto se va a vender en diciembre | Modelos estadísticos y pronósticos |
| Prescriptiva | ¿Qué conviene hacer? | Cuánto stock pedir de cada producto | Reglas y optimización sobre una predicción |

En la fuente de 2017 la diagnóstica aparece como «how it happened»; otros resúmenes dicen «why».
Esta base usa «por qué pasó» por decisión propia.

## De dónde sale el marco

Se lo conoce como «Analytic Ascendancy Model» de Gartner. Las fuentes de segunda mano lo fechan en
2012 o en 2013; el documento original es de pago y no se leyó, así que la fecha queda abierta. La
literatura académica suele nombrar solo tres tipos. Lepenioti y otros (2020), en una revisión sobre
analítica prescriptiva, la describen como la que «seeks to find the best course of action for the
future» y dicen que el foco académico e industrial sigue en «descriptive and predictive
analytics», según su abstract. La diagnóstica es una categoría del mercado más que de la academia.

> [!NOTE]
> Sin fuente todavía: el documento original de Gartner con las cuatro etapas. Circulan cifras de
> adopción por tipo atribuidas a Gartner en 2017 que ninguna fuente primaria respalda; la base no
> las usa.

## Por qué no es una escalera

El marco se dibuja como una escalera: cada peldaño vale más y cuesta más que el anterior. De ahí
sale la idea de que una organización tiene que «subir» de lo descriptivo a lo prescriptivo.

> [!IMPORTANT]
> Disputado: si los tipos son etapas que se recorren en orden. Playfair Data sostiene que el
> malentendido es suponer que se pasa de un tipo de análisis al siguiente; Motio, que la escalera
> asumió una progresión lineal y la realidad dio una madurez desigual, con organizaciones que llegan
> a lo predictivo sin el gobierno de datos que lo sostenga. Del otro lado, la postura de que las
> etapas se apilan: un caso prescriptivo necesita resueltos los niveles de abajo, y no conviene
> invertir en predicción antes de que lo básico funcione. Las dos posturas son de consultores y
> proveedores, según resúmenes; ningún estudio con método prueba ni refuta que la escalera describa
> cómo se desarrollan las organizaciones.

La lectura de la base tiene tres partes. Primero, las cuatro clases se usan a la vez: un mismo
análisis describe, después busca por qué y a veces proyecta. Segundo, más arriba no es mejor: si
la decisión es cuánta plata entró en noviembre, la respuesta correcta es descriptiva. Tercero, la
escalera tiene un interés comercial, porque quien la propone suele vender lo de arriba.

## La diagnóstica no prueba causas

La analítica diagnóstica busca explicaciones mirando los datos que ya hay: desagrega, compara
grupos y períodos. Eso genera hipótesis, pero no separa causa de coincidencia. Que las ventas de
octubre cayeran en un canal y no en otro sugiere dónde mirar; no prueba qué las bajó.

Para afirmar una causa hace falta otra cosa: un [experimento A/B](../../Producto/Medicion/experimento-ab.md)
con grupos al azar, una prueba de [incrementalidad](../../Marketing/Medicion/incrementalidad.md), o
al menos el razonamiento de [correlación y causalidad](../Estadistica/correlacion-y-causalidad.md).
La predictiva y la prescriptiva dependen de modelos estadísticos, que se apoyan en
[Estadística](../Estadistica/estadistica.md); el machine learning queda fuera de este tema.

## Para un comercio

Lo útil del marco es el orden de las preguntas, no la meta de llegar al final. Un comercio con unos
miles de ventas por mes saca casi todo el valor de contestar bien qué pasó y por qué, con una
[pregunta de análisis](pregunta-de-analisis.md) clara y números bien definidos. Las preguntas
predictivas aparecen con el stock y la estacionalidad, y suelen arrancar con una planilla antes que
con un modelo (lectura de la base).
