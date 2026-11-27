---
resumen: >-
  El error de pronóstico es la diferencia entre lo que pasó y lo que se había pronosticado, y se resume con medidas como el sesgo, el MAE, el MAPE y el MASE. Cada medida castiga cosas distintas; se mide para elegir el método, para detectar un sesgo y para dimensionar el stock de seguridad.
estado: borrador
estabilidad: semi
fuentes:
  - "Hyndman y Athanasopoulos, FPP3, «Evaluating point forecast accuracy»: https://otexts.com/fpp3/accuracy.html (según el resumen del lector, con citas literales)"
  - "Wikipedia, Tracking signal (secundaria; fórmulas de la señal y de Trigg 1964): https://en.wikipedia.org/wiki/Tracking_signal"
  - "Fildes, Goodwin, Lawrence y Nikolopoulos (2009), IJF 25(1):3-23, abstract: https://eprints.lancs.ac.uk/id/eprint/45487/ (según el resumen)"
  - "Makridakis, Spiliotis y Assimakopoulos (2018), The M4 Competition: Results, findings, conclusion and way forward, IJF 34(4), abstract: https://doi.org/10.1016/j.ijforecast.2018.06.001 (según el resumen)"
  - "APQC, Process Classification Framework 7.4 (2024), 4.1.2.7 «Measure demand forecast accuracy»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Gilliland, The Business Forecasting Deal, cap. 4 «Forecast Value Added Analysis», y Vandeput, Data Science for Supply Chain Forecasting (2021), cap. 27: solo registros bibliográficos, DOI 10.1002/9781119199885.ch4 y 10.1515/9783110671124-027"
  - "Cadena-de-suministro-y-logistica/.investigacion/planificacion.md (sección 3) y planificacion-2.md (sección 4)"
aliases: [error de pronóstico, forecast error, exactitud del pronóstico, forecast accuracy, precisión del pronóstico, sesgo, bias, MAE, MAD, desvío absoluto medio, MAPE, MASE, WAPE, RMSE, señal de seguimiento, tracking signal, FVA, forecast value added, valor agregado del pronóstico]
creado: 2026-11-27
revisado:
---

# Error de pronóstico

El error de pronóstico es la diferencia entre lo que pasó y lo que se había pronosticado, y se resume con medidas como el sesgo, el MAE, el MAPE y el MASE. Cada medida castiga cosas distintas; se mide para elegir el método, para detectar un sesgo y para dimensionar el stock de seguridad.

Es la otra mitad del [pronóstico de demanda](pronostico-de-demanda.md): no hay pronóstico sin error, y lo que se puede hacer es saber cuánto. APQC lo pone dentro de la gestión de la demanda, como 4.1.2.7 «Measure demand forecast accuracy». Está en [Planificación](planificacion.md).

## Las medidas

FPP3 llama e_t al error del período t, lo real menos lo pronosticado, y define las medidas a partir de él:

| Medida | Cómo se calcula | Qué dice | En qué unidad |
|---|---|---|---|
| Sesgo | promedio de e_t con su signo | si el pronóstico se pasa o se queda corto de forma sistemática | la del artículo |
| MAE | promedio de \|e_t\| | cuánto se equivoca, sin importar el lado | la del artículo |
| MAPE | promedio de \|p_t\|, con p_t = 100 e_t / y_t | el error como porcentaje de lo real | porcentaje |
| MASE | promedio de \|q_j\|, con q_j = el error dividido por el MAE del ingenuo sobre los datos de entrenamiento | cuánto mejora al [método ingenuo](pronostico-de-demanda.md#los-métodos-de-referencia-el-piso) | sin unidad |

La fila del sesgo es definición corriente que la base no leyó en FPP3; la fuente leída lo trata a través de la señal de seguimiento (abajo). La fuente de la señal de seguimiento llama MAD (desvío absoluto medio) a la misma cuenta que el MAE.

El MASE se lee contra 1: según FPP3, «A scaled error is less than one if it arises from a better forecast» que el ingenuo promedio. Si la serie tiene estación, se escala con el ingenuo estacional. Como no depende de la unidad, sirve para comparar artículos que se venden por unidad con otros que se venden por kilo.

> [!NOTE] Sin fuente todavía: el WAPE (suma de errores absolutos sobre suma de lo real), que se usa mucho en la práctica para agregar muchos artículos.

## Por qué el MAPE engaña

El MAPE es la medida más pedida porque se entiende como porcentaje, y FPP3 le marca cuatro problemas:

- Es «infinite or undefined if y_t = 0 for any t in the period of interest». Con [demanda intermitente](pronostico-de-demanda.md#demanda-intermitente), que tiene muchos ceros, no se puede calcular.
- Tiene «extreme values if any y_t is close to zero». Un artículo que vendió 1 unidad cuando se esperaban 3 da 200 %.
- Pone «a heavier penalty on negative errors than on positive errors»: no es simétrico.
- Supone que «the unit of measurement has a meaningful zero». Sirve para unidades vendidas; no para una temperatura.

Las competencias M lo siguen usando en versión simétrica (sMAPE): el ganador de M4 fue, según el resumen, «close to 10% more accurate» en sMAPE que el método de comparación. Que una competencia lo use no lo vuelve apto para cualquier serie.

## Cómo se mide bien

- Sobre datos que no se usaron para ajustar: FPP3 mide la exactitud sobre un tramo de prueba, separado del de entrenamiento. Medir sobre lo mismo con que se ajustó el método da un error demasiado optimista.
- Al rezago en que se decide: si el pedido sale con dos meses de anticipación, importa el error del pronóstico hecho dos meses antes, no el del mes anterior (criterio de la base).
- Contra una referencia: un error del 30 % puede ser bueno o malo; el MASE lo dice comparando contra el ingenuo.
- Por artículo y agregado: el total puede tener poco error y cada artículo mucho, porque los errores se compensan al sumar (inferencia de la base).

## La señal de seguimiento

La señal de seguimiento vigila el sesgo período a período. Según una fuente secundaria, «monitors any forecasts that have been made in comparison with actuals, and warns when there are unexpected departures of the outcomes from the forecasts». La forma simple divide la suma de los errores con signo por el MAD:

señal = Σ(real − pronóstico) / MAD

Si el pronóstico es parejo, los errores se cancelan y la señal queda cerca de cero; si siempre se pasa o siempre se queda corto, crece. Trigg (1964) propuso una versión suavizada que no acumula toda la historia. Sirve para detectar lo que encontraron Fildes y otros en los ajustes por juicio: un sesgo hacia el optimismo.

> [!NOTE] Sin fuente todavía: el umbral a partir del cual la señal indica un sesgo. La fuente leída solo da un ejemplo para la versión de Trigg con β = 0,1 («a value of Tt greater than .51 indicates nonrandom errors»); los límites de ±4 a ±6 que circulan no se leyeron.

## Para qué sirve medir

1. Elegir el método: entre dos métodos gana el de menor error sobre el tramo de prueba, y un método que no le gana al ingenuo no se justifica.
2. Detectar el sesgo: un pronóstico que siempre se pasa infla el stock; uno que siempre se queda corto genera faltantes. El sesgo se corrige; el error al azar, no.
3. Saber si el ajuste ayudó: Fildes y otros encontraron que los ajustes chicos «often damaged accuracy». Midiendo el error antes y después de cada ajuste se sabe si el paso suma.
4. Dimensionar el colchón: el stock de seguridad se calcula con el desvío del error del pronóstico en el plazo de reposición, como explica [stock de seguridad](../../Inventario-y-depositos/Reposicion/stock-de-seguridad.md), en Inventario. Ahí la medida es el desvío (la raíz del error cuadrático medio), no el MAPE.

El tercer punto tiene nombre en la práctica, valor agregado del pronóstico (FVA): comparar el error de cada paso del proceso (el estadístico, el ajuste del planificador, el consenso) contra el de un pronóstico ingenuo.

> [!NOTE] Sin fuente todavía: la definición de FVA en un texto leído. Existen el capítulo 4 de Gilliland, *The Business Forecasting Deal*, y el 27 de Vandeput (2021), pero solo se vieron sus registros bibliográficos.

## Qué tiene que guardar un sistema para medir el error

Ninguno de los ERP abiertos consultados mostró un registro del error. Lo que hace falta, por inferencia de FPP3 y de la señal de seguimiento:

- Cada pronóstico congelado, con la fecha en que se hizo y el período al que apunta, para medir a cualquier rezago.
- El real con signo, de la misma serie que se pronosticó (venta, pedido o despacho).
- Cada versión (estadística, ajustada, de consenso), para medir el aporte de cada paso.
- La medida usada junto al número, porque MAPE, MASE y WAPE no son intercambiables.
- Los acumulados de la señal (o los valores suavizados de Trigg), por artículo.

Para leer más: FPP3, «Evaluating point forecast accuracy», entera; fijarse en la lista de problemas del MAPE y en la lectura del MASE contra 1.
