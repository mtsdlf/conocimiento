---
resumen: >-
  El pronóstico de demanda es la estimación de cuánto van a pedir los clientes de cada artículo, en cada lugar y en cada período futuro. Se hace con métodos estadísticos sobre la historia, con juicio o con los dos, y siempre se compara contra un método simple de referencia.
estado: borrador
estabilidad: estable
fuentes:
  - "Hyndman y Athanasopoulos, Forecasting: Principles and Practice, 3.ª ed. (FPP3), «Simple forecasting methods»: https://otexts.com/fpp3/simple-methods.html (según el resumen del lector)"
  - "FPP3, «Exponential smoothing» y «Estimation and model selection»: https://otexts.com/fpp3/expsmooth.html y https://otexts.com/fpp3/ets.html (según el resumen del lector)"
  - "FPP3, «Forecasting count time series» (Croston): https://otexts.com/fpp3/counts.html (según el resumen del lector)"
  - "FPP3, «Forecasting hierarchical and grouped time series»: https://otexts.com/fpp3/hierarchical.html (según el resumen del lector)"
  - "FPP3, «Judgmental forecasts»: https://otexts.com/fpp3/judgmental.html (según el resumen del lector)"
  - "Fildes, Goodwin, Lawrence y Nikolopoulos (2009), Effective forecasting and judgmental adjustments, International Journal of Forecasting 25(1):3-23, abstract: https://eprints.lancs.ac.uk/id/eprint/45487/ (según el resumen)"
  - "Syntetos, Boylan y Croston (2005), On the categorization of demand patterns, JORS 56(5):495-503, abstract: https://ideas.repec.org/a/pal/jorsoc/v56y2005i5d10.1057_palgrave.jors.2601841.html (según el resumen)"
  - "Syntetos y Boylan (2005), The accuracy of intermittent demand estimates, IJF 21(2):303-314, solo metadatos: https://ideas.repec.org/a/eee/intfor/v21y2005i2p303-314.html"
  - "Documentación de statsforecast, CrostonSBA (secundaria, para el factor de corrección): https://nixtlaverse.nixtla.io/statsforecast/docs/models/crostonsba.html"
  - "Makridakis, Spiliotis y Assimakopoulos (2018), The M4 Competition: Results, findings, conclusion and way forward, IJF 34(4), abstract: https://doi.org/10.1016/j.ijforecast.2018.06.001 (según el resumen)"
  - "Makridakis, Spiliotis y Assimakopoulos, The M5 Accuracy competition: Results, findings and conclusions, preprint, sección 6: https://statmodeling.stat.columbia.edu/wp-content/uploads/2021/10/M5_accuracy_competition.pdf"
  - "CSCMP, Supply Chain Management Terms and Glossary (2013), entradas forecast y demand planning: https://www.cisco-eagle.com/uploads/cscmp/cscmp-glossary.pdf"
  - "Documentación de un ERP abierto, Master production schedule (rama 19.0): https://github.com/odoo/documentation/blob/19.0/content/applications/inventory_and_mrp/manufacturing/workflows/use_mps.rst"
  - "Campos de Sales Forecast de otro ERP abierto (rama develop): https://github.com/frappe/erpnext/tree/develop/erpnext/manufacturing/doctype"
  - "Cadena-de-suministro-y-logistica/.investigacion/planificacion.md (sección 2), planificacion-2.md (sección 3) y fundamentos-y-contraria-2.md (secciones 5 y 10)"
aliases: [pronóstico, pronóstico de demanda, previsión de demanda, demand forecast, forecasting, forecast, planificación de la demanda, demand planning, suavizado exponencial, exponential smoothing, ETS, método ingenuo, naive, Croston, SBA, demanda intermitente, intermittent demand, pronóstico jerárquico, hierarchical forecasting, reconciliación, MinT, ajuste por juicio, judgmental adjustment, Delphi, competencias M]
creado: 2026-11-27
revisado:
---

# Pronóstico de demanda

El pronóstico de demanda es la estimación de cuánto van a pedir los clientes de cada artículo, en cada lugar y en cada período futuro. Se hace con métodos estadísticos sobre la historia, con juicio o con los dos, y siempre se compara contra un método simple de referencia.

Es el número del que parten todos los planes de [Planificación](planificacion.md): el [plan de ventas y operaciones](plan-de-ventas-y-operaciones.md) lo agrega por familia, y la [planificación de la distribución](planificacion-de-la-distribucion.md) lo usa por artículo y depósito. En Inventario, el [punto de pedido](../../Inventario-y-depositos/Reposicion/punto-de-pedido.md) lo usa sin hacerlo. Cuánto se equivoca está en [error de pronóstico](error-de-pronostico.md). El glosario del CSCMP define el pronóstico como «An estimate of future customer demand».

## Los métodos de referencia, el piso

FPP3, el libro abierto de Hyndman y Athanasopoulos, empieza por cuatro métodos simples, que sirven para comparar a los demás:

| Método | Regla, literal de FPP3 | Para qué serie |
|---|---|---|
| Media | «the forecasts of all future values are equal to the average (or "mean") of the historical data» | sin tendencia ni estación |
| Ingenuo | «we simply set all forecasts to be the value of the last observation» | que se mueve sin patrón |
| Ingenuo estacional | «we set each forecast to be equal to the last observed value from the same season» | con estación marcada |
| Deriva | «the amount of change over time (called the drift) is set to be the average change seen in the historical data» | con tendencia |

La columna de la derecha es lectura de la base. Un método más elaborado vale si le gana a estos; si no, sobra. El [MASE](error-de-pronostico.md) mide justamente contra el ingenuo.

## Suavizado exponencial

El suavizado exponencial pondera más lo reciente y es el caballo de batalla del pronóstico por artículo. FPP3 lo arma por capas:

- El simple tiene un pronóstico «"flat"»: el mismo número para todos los períodos futuros.
- Holt agrega la tendencia: el pronóstico queda «no longer flat but trending».
- La tendencia amortiguada hace que «short-run forecasts are trended while long-run forecasts are constant».
- Holt-Winters agrega la estación, aditiva o multiplicativa.

FPP3 los junta en el marco ETS (error, tendencia, estación). Cruzando tendencia (ninguna, aditiva, amortiguada) con estación (ninguna, aditiva, multiplicativa) salen nueve métodos. Como son modelos estadísticos, dan intervalos de predicción y se eligen por un criterio: «We let the ETS() function select the model by minimising the AICc».

## Qué dicen las competencias M

Las competencias de Makridakis comparan métodos sobre miles de series reales, y su conclusión cambió con el tiempo. Según las conclusiones del artículo de M5:

- M1 dio el triunfo a «a simple exponential smoothing method rather than the statistically sophisticated Box-Jenkins methodology».
- En M3, «simple methods outperformed the relatively more complex ones».
- En M4 (100.000 series), según su abstract de 2018, «Out Of the 17 most accurate methods, 12 were "combinations" of mostly statistical approaches», ganó un híbrido estadístico y de aprendizaje automático, y «The six pure ML methods performed poorly».
- En M5, con 42.840 series jerárquicas de ventas de una cadena minorista, la mayoría intermitentes, ganó el aprendizaje automático: «the 50 top-performing ones achieving a superior performance of more than 14% over the most accurate statistical benchmark».

Lo que no cambió en las cinco: «combining improves forecasting accuracy». La lectura de la base: el método simple es el piso de comparación, no el techo, y qué método rinde depende de cuántas series hay, de si hay variables externas (precio, eventos) y de la jerarquía.

## Pronóstico por juicio y su ajuste

FPP3 avisa que «Judgmental forecasts are subjective, and therefore do not come free of bias or limitations». El sesgo típico es el anclaje: los pronósticos siguientes «tend to converge or be close to an initial familiar reference point». Para un grupo de expertos propone Delphi, que busca «consensus forecasts from a group of experts in a structured iterative manner», anónimo y en dos o tres rondas. Y pide separar roles: «Forecasters and users should be clearly segregated».

La práctica común es otra: el sistema genera un pronóstico estadístico y el planificador lo corrige. Fildes, Goodwin, Lawrence y Nikolopoulos estudiaron más de 60.000 pronósticos de cuatro empresas, según el resumen de su artículo:

- «In three of the companies, on average, judgmental adjustments increased accuracy.»
- Pero «the smaller adjustments often damaged accuracy», y los grandes mejoraron más.
- Los ajustes hacia arriba «were much less likely to improve accuracy than negative adjustments», lo que sugiere «a general bias towards optimism».

No dice que ajustar empeore: dice que los ajustes chicos y los optimistas suelen restar. Para saberlo en una empresa hay que guardar el pronóstico antes y después del ajuste (inferencia de la base).

## Demanda intermitente

Un artículo es intermitente cuando muchos períodos tienen demanda cero: repuestos, artículos de cola. El suavizado común lo pronostica mal. Croston (1972), según FPP3, separa dos series, el tamaño de las demandas no nulas y el tiempo entre ellas, las suaviza por separado y pronostica su cociente. FPP3 marca dos límites: «Forecasts obtained from Croston's method are also known to be biased», y el método «does not correspond to any statistical model», así que no da intervalos.

Para el sesgo hay una corrección, SBA, de Syntetos y Boylan (2005). Su fórmula se verificó solo en la documentación de un paquete de pronóstico, que multiplica el cociente de Croston por (1 − α/2), con α la constante de suavizado.

Para decidir qué artículo es intermitente, Syntetos, Boylan y Croston (2005) proponen clasificar la demanda con dos variables, según su resumen: «the average inter-demand interval and the squared coefficient of variation of demand sizes» (el ADI y el CV²). Lo validaron con 3.000 series del sector automotor.

> [!NOTE] Sin fuente todavía: los umbrales de ADI y CV² que separan los cuatro patrones de demanda (los valores que circulan, 1,32 y 0,49, no se leyeron en la fuente).

## Pronosticar en jerarquía

Las ventas se suman por artículo, familia, región y total, y los pronósticos de cada nivel tienen que cerrar entre sí. FPP3 distingue series jerárquicas (anidadas, como sucursal dentro de región) de agrupadas, que cruzan atributos y no se desarman «in a unique hierarchical manner». Los enfoques:

| Enfoque | Cómo hace cerrar los niveles |
|---|---|
| Abajo-arriba | pronostica cada serie de la base y suma |
| Arriba-abajo | pronostica el total y lo reparte con proporciones |
| Del medio hacia afuera | parte de un nivel intermedio; solo en estructuras estrictamente jerárquicas |
| Reconciliación óptima (MinT) | pronostica todos los niveles y los ajusta: «minimises the total forecast variance of the set of coherent forecasts» |

En los ejemplos de FPP3, MinT fue más preciso que abajo-arriba. Que «lo agregado se pronostica mejor que lo detallado» se repite mucho, pero FPP3 no lo dice; el agrupamiento reduce la variabilidad relativa, como explica [centralización del stock](../Red-de-distribucion/centralizacion-del-stock.md).

## La venta no es la demanda

La historia que se pronostica casi nunca es la demanda: es lo que se vendió, se pidió o se despachó. Si un artículo estuvo sin stock, la venta registrada queda por debajo de lo que se hubiera vendido, y pronosticar sobre esa venta repite el faltante (inferencia de la base). Lo mismo pasa al revés con una promoción, que infla un período. El CSCMP define la planificación de la demanda como identificar «all sources of demand», no solo las ventas.

> [!NOTE] Sin fuente todavía: el tratamiento de la demanda censurada por faltantes (corregir la historia cuando hubo quiebre de stock) en una fuente leída.

## Qué guarda un sistema del pronóstico

Un ERP abierto guarda el pronóstico como documento con cabecera y partidas: almacén, fecha de inicio, frecuencia («Weekly» o «Monthly»), número de períodos y un estado («Planned», «MPS Generated», «Cancelled»); por partida, artículo, unidad, fecha y cantidad. El estado «MPS Generated» muestra que el pronóstico se consume al generar el plan maestro. Otro sugiere la demanda a partir de la historia («Previous Year», «Last 3 Months», «Last 12 Months») con un factor de escala, y deja editarla a mano por período.

Lo que la base agrega como criterio, porque ninguno de los sistemas leídos lo mostró:

- La serie con su origen: venta, pedido o despacho, por artículo, lugar y período, con marcas de quiebre de stock y de promoción para corregirla.
- La jerarquía de agregación como estructura propia, no como un filtro de informe.
- Versiones del pronóstico (estadístico, ajustado, de consenso), cada una con autor y fecha, para medir si el ajuste ayudó.
- El método y sus parámetros con que se generó cada versión, y la clase de demanda del artículo (intermitente o no).

Para leer más: FPP3 en <https://otexts.com/fpp3/>, los capítulos de métodos simples, suavizado exponencial, series jerárquicas y pronóstico por juicio.
