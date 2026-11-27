---
resumen: >-
  Un tablero (dashboard) es una pantalla que reúne la información más importante para seguir uno o más
  objetivos, ordenada para que quien la mira vea de un vistazo si algo se salió de lo normal.
estado: borrador
estabilidad: semi
fuentes:
  - "Stephen Few, Dashboard Confusion (Intelligent Enterprise, 2004), reimpresión (según su resumen): https://www.informationweek.com/government/dashboard-confusion-2"
  - "Stephen Few, Information Dashboard Design (O'Reilly, 2006), según la reseña de UXmatters (2007): https://www.uxmatters.com/mt/archives/2007/04/book-review-information-dashboard-design.php"
  - "Tableau, What the heck is a dashboard anyways (según el buscador): https://www.tableau.com/sites/default/files/webinars/what_the_heck_is_a_dashboard_anyways.pdf"
  - "Stephen Few, Why Most Dashboards Fail (solo la ficha; el PDF no se leyó): https://blogs.ischool.berkeley.edu/i247s13/files/2013/02/WhyMostDashboardsFail.pdf"
  - "Datos/.investigacion/metricas-y-visualizacion.md (sección 4)"
  - "Datos/.investigacion/posicion-contraria.md (sección 3)"
aliases: [dashboard, tablero de control, panel, cuadro de mando]
creado: 2026-11-27
revisado:
---

# Tablero

Un tablero (dashboard) es una pantalla que reúne la información más importante para seguir uno o más
objetivos, ordenada para que quien la mira vea de un vistazo si algo se salió de lo normal.

Es la forma de vigilar dentro de [Visualización y BI](visualizacion-y-bi.md). Cada número que
muestra es una [métrica definida](../Analitica-de-producto/definicion-de-metrica.md), idealmente
tomada de la [capa semántica](capa-semantica.md), y cada gráfico sale de
[elegir un gráfico](elegir-un-grafico.md). Para presentar un hallazgo una vez, la forma es otra:
[contar con datos](contar-con-datos.md).

## La definición de Few: una pantalla, de un vistazo

Stephen Few escribió en 2004: "A dashboard is a visual display of the most important information
needed to achieve one or more objectives". El resto de su definición, que lo acomoda en una sola
pantalla para vigilarlo de un vistazo, llegó por resumen. Según la reseña de su libro de 2006, Few
sostiene que "A dashboard fits on a single computer screen" y que "Dashboards are used to monitor
information at a glance".

La pantalla única obliga a elegir. Si no entra, sobra algo, o son dos
tableros para dos personas distintas (lectura de la base). Few separa el tablero de las pantallas de
análisis con muchos gráficos interactivos, que él llama "faceted analytical display", según un
resumen de un texto de 2007. Gran parte de lo que las herramientas de BI llaman dashboard es esto
segundo (lectura de la base).

## Estratégico, analítico u operativo

Según la reseña, Few clasifica los tableros por el papel que cumplen, y ese papel es lo que más
condiciona su diseño.

| Papel | Quién lo mira y cada cuánto | Ejemplo en un comercio |
|---|---|---|
| Estratégico | La dirección, cada mes, para ver la marcha general | ventas, margen y clientes que vuelven, contra el año anterior |
| Analítico | Quien analiza, para entender una tendencia | ventas por canal y por categoría, con filtros |
| Operativo | Quien opera, todos los días, para actuar en el momento | pedidos sin despachar, stock por debajo del mínimo |

Los ejemplos son de la base. Otras fuentes agregan un cuarto tipo, el táctico, que no es de Few.

## Cada número con una decisión

Contra los tableros que nadie mira no hay estudios con método, según el informe de posición
contraria; hay opinión de practicantes. Lo que se puede sostener es un criterio de diseño: cada
número del tablero tiene que tener una decisión asociada. Si sube o baja, alguien hace algo. Un
número que no cambia ninguna decisión es decoración, y suele ser una
[métrica de vanidad](../Analitica-de-producto/definicion-de-metrica.md#métricas-de-vanidad).

Few propone, según la reseña, simplicidad y dos formas de condensar: el resumen (mostrar el total,
no cada fila) y la excepción (mostrar lo que se salió de lo normal). Un número suelto no dice si
está bien o mal; dice algo comparado contra una meta, contra el mismo período anterior o contra un
rango esperado.

## Cómo se arma un tablero

1. Escribí quién lo va a mirar, cada cuánto y qué decisiones toma con él. Si son dos personas con
   decisiones distintas, son dos tableros.
2. Para cada decisión, elegí el número que la dispara y escribí su
   [definición](../Analitica-de-producto/definicion-de-metrica.md) completa.
3. Fijá contra qué se compara cada número: meta, período anterior o rango normal.
4. Elegí el gráfico por la comparación que hay que hacer, con [elegir un gráfico](elegir-un-grafico.md).
5. Ordená la pantalla: lo que pide acción primero, arriba a la izquierda; el contexto después.
6. Marcá las excepciones (un color, una señal) y dejá el resto en gris.
7. Revisá que entre en una pantalla. Si no entra, sacá lo que no dispara ninguna decisión.
8. Al mes, preguntá qué decisiones se tomaron mirándolo. Lo que nadie usó, sacalo.

Los pasos son de la base, a partir del criterio de Few (una pantalla, resumen y excepción) y del
criterio de decisión asociada. Un comercio que pide «un tablero de ventas» casi siempre necesita
primero el paso 1: acordar qué tiene que contestar, con una [pregunta de análisis](../Analisis/pregunta-de-analisis.md).

## Cómo falla un tablero

- Muestra todo lo que hay en vez de lo que hace falta, y nadie encuentra lo importante.
- Mezcla vigilar y analizar: treinta filtros en un tablero que tendría que leerse en diez segundos.
- Sus números no coinciden con los de otro tablero, porque cada uno calcula la métrica a su manera.
  Lo resuelve la [capa semántica](capa-semantica.md).
- Muestra números sin comparación, y nadie sabe si está bien o mal.
- Invita a leer causas en una serie: que las ventas suban la semana de una promoción no prueba que
  la promoción las causó. Eso es tema de [correlación y causalidad](../Estadistica/correlacion-y-causalidad.md).

La lista es de la base. El texto de Few sobre por qué fallan los tableros no se pudo leer.

> [!NOTE]
> Sin fuente todavía: "Why Most Dashboards Fail" de Few y los capítulos de *Information Dashboard
> Design* sobre errores de diseño, leídos en el original.

La referencia es *Information Dashboard Design* (2006) de Few, en los capítulos de definición y de
errores de diseño, junto con "Dashboard Confusion" para la definición. Conviene fijarse en tres
cosas: una pantalla, para qué decisión y qué es excepción. Las herramientas para armarlo están en la
[ficha de herramientas de BI](herramientas-de-bi.md).
