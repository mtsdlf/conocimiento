---
resumen: >-
  El control estadístico de procesos vigila un proceso con mediciones tomadas en el tiempo, para separar la variación propia del proceso de la que tiene una causa que se puede encontrar y corregir. Sus herramientas son el gráfico de control, con sus límites y reglas, y los índices de capacidad, que comparan el proceso con la especificación.
estado: vigente
estabilidad: estable
fuentes:
  - "NIST/SEMATECH e-Handbook of Statistical Methods, 6.3.1 «What are Control Charts?» (leído por el lector): https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc31.htm"
  - "NIST/SEMATECH e-Handbook, 6.3.2 «What are Shewhart Control Charts?»: https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc32.htm"
  - "NIST/SEMATECH e-Handbook, 6.3.2.1 gráficos X-barra y R: https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc321.htm"
  - "NIST/SEMATECH e-Handbook, 6.3.3.2 gráfico p: https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc332.htm"
  - "NIST/SEMATECH e-Handbook, 6.1.6 «What is Process Capability?»: https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm"
  - "Best, M. y Neuhauser, D., «Walter A Shewhart, 1924, and the Hawthorne factory», Qual Saf Health Care 2006;15(2):142-143: https://pmc.ncbi.nlm.nih.gov/articles/PMC2464836"
  - "Deming, W. E., Out of the Crisis, cap. 11, vía extractos de la Universidad de Oklahoma (secundaria): https://ou.edu/faculty/M/Jorge.L.Mendoza-1/DEMIN.htm"
  - "LeanBlog, «Two kinds of mistakes and the wisdom of Shewhart, 100 years later» (2025, paráfrasis): https://www.leanblog.org/2025/06/two-kinds-of-mistakes-and-the-wisdom-of-shewhart-100-years-later/"
  - "Produccion/.investigacion/calidad.md (sección 3) y calidad-2.md (sección 3), 2026-11-27"
aliases: [control estadístico de procesos, control estadístico del proceso, CEP, statistical process control, SPC, gráfico de control, carta de control, control chart, gráfico de Shewhart, Shewhart chart, X-barra y R, X-bar and R chart, gráfico p, p chart, límites de control, control limits, causa asignable, assignable cause, causa por azar, chance cause, causa común, common cause, causa especial, special cause, reglas de Western Electric, Western Electric rules, capacidad del proceso, process capability, Cp, Cpk, Cpm]
creado: 2026-11-27
revisado: 2026-11-27
---

# Control estadístico de procesos

El control estadístico de procesos vigila un proceso con mediciones tomadas en el tiempo, para separar la variación propia del proceso de la que tiene una causa que se puede encontrar y corregir. Sus herramientas son el gráfico de control, con sus límites y reglas, y los índices de capacidad, que comparan el proceso con la especificación.

Es la pieza de [Calidad](calidad.md) que mira el proceso y no el lote. Toma las mediciones que prevé el [plan de inspección](plan-de-inspeccion.md), pero no decide si una pieza se acepta: dice si la máquina o la operación cambió. Cuando una señal tiene causa, lo que se hace con las piezas ya fabricadas es una [no conformidad](no-conformidad.md), y lo que se hace con la causa, una [acción correctiva](accion-correctiva.md).

## Causas por azar y causas asignables

Shewhart separó la variación en dos clases. Según un artículo de 2006 sobre su trabajo (Best y Neuhauser), «identified two categories of variation which he called 'assignable-cause' and 'chance-cause' variation», y «He devised the control chart as a tool for distinguishing between the two». El libro de Shewhart (1931) no se leyó.

El manual de NIST usa las mismas palabras. Un punto fuera de los límites es motivo para buscar: «We would be searching for an assignable cause if a point would fall outside these limits». Mientras solo actúan las causas por azar, el proceso está bajo control, y estar bajo control «implies that all points are between the control limits and they form a random pattern».

En la planta, una causa asignable es algo con nombre: una herramienta gastada, un lote de material distinto, un operario nuevo, un cambio de turno. La variación por azar es la suma de muchas causas chicas que no se pueden separar una por una (ejemplos de la base).

## Causas comunes y especiales: la versión de Deming

Deming habló de causas comunes y especiales. En los extractos de *Out of the Crisis* que publica una universidad: «Variations on performance are due to common causes (system) and special causes (out side the system)», y «most troubles with service or production are due to the system». Es una fuente secundaria; el libro no se leyó.

El artículo de 2006 dice que otros llaman a las dos clases de Shewhart «'special-cause' and 'common-cause' variation, respectively», sin atribuírselo a Deming. Según un resumen de un blog, Deming advertía dos errores: tratar como especial una variación común, que lleva a sobreajustar el proceso, y tratar como común una causa especial, que lleva a no actuar.

> [!IMPORTANT] Dos puntos sin resolver. Algunas fuentes secundarias toman «asignable» y «especial» como sinónimos; otras dicen que Deming entiende la causa especial como externa al sistema o efímera, y que no es lo mismo. Y la proporción de problemas que Deming atribuye al sistema circula con dos cifras: los extractos de la universidad dan 94 % comunes y 6 % especiales; otro resumen da 85 % y 15 %. Ninguna se verificó en el libro.

## Los límites de control no son la especificación

El modelo de Shewhart pone la línea central en la media del estadístico y los límites a k desvíos de ella. NIST: «Historically, k = 3 has become an accepted standard in industry». Con un proceso normal, un punto cae fuera de ±3σ cerca del 0,3 % de las veces.

Los límites salen de los datos del proceso; la especificación sale del cliente o del plano. Un proceso puede estar bajo control y fabricar piezas fuera de especificación, o fuera de control y todavía dentro de ella. Los dos límites se calculan con datos distintos: ninguna fórmula de la tabla usa la especificación (lectura de la base).

| Gráfico | Para qué | Límites, según NIST |
|---|---|---|
| X-barra | la media de subgrupos de una variable | x̿ ± A2·R̄, con A2 = 3/(d2·√n) |
| R | el rango de esos subgrupos | superior R̄·D4, inferior R̄·D3, con D3 = 1 − 3d3/d2 y D4 = 1 + 3d3/d2 |
| p | la proporción de defectuosos de un atributo | p ± 3√(p(1−p)/n); con p desconocido, p̄ = ΣDi/(m·n) |

En el gráfico p, Di es la cantidad de defectuosos del subgrupo i, m la cantidad de subgrupos y n su tamaño. Los gráficos de variables piden medir; el p solo pide contar, y por eso es el que se puede armar con los rechazos que ya declara la planta (inferencia de la base).

## Las reglas para leer un gráfico

Un punto fuera de los límites no es la única señal. NIST, en la página de Shewhart, lista reglas del tipo Western Electric, como las devolvió el lector:

1. Un punto más allá de 3σ.
2. Dos de tres puntos más allá de 2σ, del mismo lado.
3. Cuatro de cinco puntos más allá de 1σ, del mismo lado.
4. Ocho puntos seguidos del mismo lado de la línea central.
5. Una tendencia de seis puntos.
6. Catorce puntos alternando arriba y abajo.

Cada regla agrega sensibilidad y también falsas alarmas. Según la misma lectura, sumar las reglas lleva las falsas alarmas de una cada 371 puntos a una cada 91,75. La lista y los números vienen de una lectura automática de la página y falta recotejarlos con el texto de NIST.

## La capacidad del proceso: Cp y Cpk

La capacidad compara el ancho natural del proceso con el ancho que permite la especificación. Solo tiene sentido con el proceso bajo control: si no, la σ estimada no describe nada estable (criterio de la base). Las fórmulas, según NIST:

| Índice | Fórmula | Qué mide |
|---|---|---|
| Cp | (USL − LSL) / 6σ | si el proceso entra en la tolerancia, sin mirar dónde está centrado |
| Cpk | mín[(USL − μ) / 3σ, (μ − LSL) / 3σ] | lo mismo, contra el límite más cercano a la media |
| Cpm | (USL − LSL) / 6√(σ² + (μ − T)²) | penaliza la distancia al objetivo T |

USL y LSL son los límites superior e inferior de la especificación, μ la media del proceso y σ su desvío.

El ejemplo de NIST. La especificación va de 8 a 20, el desvío es 2 y la media 16. Entonces Cp = 12/12 = 1,0: el proceso entra justo en la tolerancia. Pero la media está corrida hacia arriba: Cpu = (20 − 16)/6 = 0,6667 y Cpl = (16 − 8)/6 = 1,3333, así que Cpk = 0,6667. NIST concluye: «We would like to have Ĉpk at least 1.0, so this is not a good process». La página escribe la media como «≥ 16», que parece una errata; las cuentas cierran con 16 (verificado por la base).

La diferencia entre Cp y Cpk dice qué hacer. Un Cp bueno con Cpk malo pide centrar el proceso, que suele ser un ajuste; un Cp malo pide reducir la variación, que suele ser un cambio de máquina, método o material, y puede terminar en un [cambio de ingeniería](../Producto-y-proceso/cambios-de-ingenieria.md) (lectura de la base).

## Qué guarda un gráfico de control

- La característica, con su unidad y su especificación (LSL, USL, objetivo).
- Cada subgrupo: tamaño, fecha y hora, orden de producción, lote, máquina y operario; los valores o el conteo de defectuosos.
- El estadístico del subgrupo (media, rango, proporción).
- Los límites de control, con el período de datos con que se calcularon, y cuándo se recalcularon.
- Las señales: qué regla se violó, en qué punto, y la causa encontrada o la [no conformidad](no-conformidad.md) que abrió.
- Los índices de capacidad, con la fecha y los datos que los respaldan.

Los dos sistemas abiertos leídos registran la medición pero no dibujan el gráfico. En una planilla alcanza con una tabla de subgrupos, dos columnas calculadas (media y rango), los límites fijos y un gráfico de línea con tres líneas horizontales. El texto de referencia para profundizar es el capítulo 6 del manual de NIST, secciones 6.1.6 y 6.3; Montgomery, *Introduction to Statistical Quality Control*, es el libro de texto habitual y no se leyó.
