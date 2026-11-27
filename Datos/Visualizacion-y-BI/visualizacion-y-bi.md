---
resumen: >-
  Visualización y BI es la parte de Datos que pone los números delante de quien decide: elige la
  forma gráfica de cada comparación, arma los tableros, fija cada métrica en un solo lugar y cuenta
  los hallazgos.
estado: vigente
estabilidad: estable
fuentes:
  - "Stephen Few, Dashboard Confusion (Intelligent Enterprise, 2004), reimpresión (según su resumen): https://www.informationweek.com/government/dashboard-confusion-2"
  - "Stephen Few, Information Dashboard Design (O'Reilly, 2006), según la reseña de UXmatters: https://www.uxmatters.com/mt/archives/2007/04/book-review-information-dashboard-design.php"
  - "Financial Times, Visual Vocabulary (según su resumen): https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary"
  - "dbt Docs, Semantic Layer (según su resumen): https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl"
  - "Brynjolfsson, Hitt y Kim, Strength in Numbers (2011), solo el abstract: https://papers.ssrn.com/abstract=1819486"
  - "Datos/.investigacion/metricas-y-visualizacion.md (secciones 3 a 7)"
  - "Datos/.investigacion/posicion-contraria.md (secciones 1 y 3)"
aliases: [BI, business intelligence, inteligencia de negocios, visualización de datos, data visualization, dataviz]
creado: 2026-11-27
revisado: 2026-11-27
---

# Visualización y BI

Visualización y BI es la parte de Datos que pone los números delante de quien decide: elige la
forma gráfica de cada comparación, arma los tableros, fija cada métrica en un solo lugar y cuenta
los hallazgos.

Es el último tramo del recorrido del dato en [Datos](../datos.md). Recibe los resultados de
[Análisis](../Analisis/analisis.md) y de [Analítica de producto](../Analitica-de-producto/analitica-de-producto.md),
y lee las tablas que deja [Modelado y almacenamiento](../Modelado-y-almacenamiento/modelado-y-almacenamiento.md).
BI (business intelligence) es el nombre de la práctica y de las herramientas de reportes y tableros
de una empresa. Lo que un tablero deja ver también vuelve hacia atrás: el dato que falta o el número
que no cierra es un pedido para las verticales de ingeniería.

Cuando la fuente es un sistema de gestión (un ERP, el sistema de un comercio), el tramo tiene una
parte propia: [BI sobre el software de gestión](BI-sobre-software-de-gestion/bi-sobre-software-de-gestion.md),
que dice dónde termina el reporte que el sistema emite y cómo se sacan, modelan, juntan y concilian
sus datos para decidir.

## Tres usos de un gráfico: vigilar, explorar y contar

Few separa el tablero, que sirve para vigilar algo de un vistazo, de lo que llama "faceted
analytical display": varios gráficos interactivos en una pantalla para analizar (según un resumen,
de un texto de 2007). A esos dos usos se suma un tercero, presentar un hallazgo a alguien. Cada uso
pide una forma distinta (lectura de la base):

| Uso | Quién mira y para qué | Forma | Nota |
|---|---|---|---|
| Vigilar | Alguien que decide, todos los días o todas las semanas, si algo se salió de lo normal | Un tablero de una pantalla, con pocas métricas comparadas contra algo | [Tablero](tablero.md) |
| Explorar | El analista, buscando un patrón | Gráficos que se filtran y se cruzan, sin forma fija | [Análisis exploratorio](../Analisis/analisis-exploratorio.md) |
| Contar | Alguien que no hizo el análisis y tiene que actuar | Una idea, un gráfico que la muestra, lo justo de contexto | [Contar con datos](contar-con-datos.md) |

Gran parte de lo que se llama tablero en las herramientas de BI es la segunda forma (lectura de la
base a partir del resumen del texto de Few). Mezclarlas es la falla más común: un tablero de vigilancia con treinta
filtros o una presentación que muestra todo lo explorado.

## Dónde se rompe un número antes de llegar al gráfico

El error más caro de esta vertical aparece antes del gráfico. Si dos tableros calculan «clientes activos» con
filtros distintos, muestran números distintos y nadie confía en ninguno. Por eso la vertical tiene
dos piezas que no son gráficas: la [definición de métrica](../Analitica-de-producto/definicion-de-metrica.md),
que fija qué se cuenta, y la [capa semántica](capa-semantica.md), que la escribe una sola vez para
que todas las herramientas la usen. La documentación de un proveedor la ubica en la capa de modelado y no en
la de BI, justamente para que todas las herramientas lean la misma definición.

Después viene la forma. Un gráfico codifica cada número con una marca (una posición, una longitud,
un ángulo, un color), y el ojo compara unas mejor que otras. Qué gráfico corresponde a qué relación
y qué errores deforman la lectura está en [elegir un gráfico](elegir-un-grafico.md); cómo se arma
cada gráfico dentro de Excel o Sheets, en
[gráficos en la planilla](../../Planillas-de-calculo/Analisis/graficos-en-la-planilla.md).

## Qué se sabe de si un tablero mejora las decisiones

Poco, y no para comercios chicos. El estudio que la base encontró a favor de decidir con datos, el de
Brynjolfsson, Hitt y Kim (2011), es una asociación medida por encuesta en grandes empresas que
cotizan en bolsa; sus cifras y sus límites están en
[Análisis](../Analisis/analisis.md#cómo-falla-un-análisis). Contra los
tableros que nadie mira y las métricas de vanidad tampoco hay estudios con método, solo opinión de
practicantes, según el informe de posición contraria.

Lo que queda es un criterio de diseño, no un hallazgo: cada número de un tablero tiene que tener una
decisión asociada. Cómo se aplica está en [tablero](tablero.md).

> [!NOTE]
> Sin fuente todavía: evidencia sobre el uso de tableros y BI en pymes o comercios chicos.

## Lo que hay adentro de visualización y BI

- [Elegir un gráfico](elegir-un-grafico.md) — qué relación se quiere mostrar, qué marca se lee mejor y cuándo el eje tiene que empezar en cero.
- [Tablero](tablero.md) — el tablero de una pantalla para vigilar: para qué decisión, qué comparación y qué es excepción.
- [Capa semántica](capa-semantica.md) — donde cada métrica se define una sola vez para todas las herramientas.
- [Contar con datos](contar-con-datos.md) — cómo se presenta un hallazgo a quien tiene que actuar, y qué afirma el número.
- [BI sobre el software de gestión](BI-sobre-software-de-gestion/bi-sobre-software-de-gestion.md) — el BI que se arma con los datos de un sistema de gestión: extraer, hechos y dimensiones de gestión, historia, varias fuentes, empresas y monedas, la Argentina y la conciliación con el balance.
- [Herramientas de BI](herramientas-de-bi.md) — ficha: licencias y precios públicos de cinco herramientas de BI, copiados el 2026-11-27.
