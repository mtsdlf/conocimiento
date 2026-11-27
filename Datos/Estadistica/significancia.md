---
resumen: >-
  La significancia, en un experimento, es el criterio para decidir si la diferencia entre dos
  variantes es real o salió del azar. Funciona solo si el tamaño de muestra y la regla de parada se
  fijan antes de mirar, y con poco tráfico exagera los efectos que encuentra.
estado: vigente
estabilidad: semi
fuentes:
  - "Evan Miller, How Not To Run an A/B Test (18-abr-2010): https://www.evanmiller.org/how-not-to-run-an-ab-test.html"
  - "Ramesh Johari, Leo Pekelis y David Walsh, Always Valid Inference: Bringing Sequential Analysis to A/B Testing, arXiv 1512.04922 (v3, 2019; abstract): https://arxiv.org/abs/1512.04922"
  - "Ron Kohavi, Diane Tang y Ya Xu, Trustworthy Online Controlled Experiments (Cambridge UP, 2020), cap. 3, p. 42, según el índice: https://assets.cambridge.org/97811087/24265/index/9781108724265_index.pdf"
  - "Confidence by Spotify, Why not Bayes? (proveedor; sin fecha, © 2026): https://confidence.spotify.com/why-not-bayes"
  - "R-bloggers, Is Bayesian A/B Testing Immune to Peeking? Not Exactly (2015; según el resumen del buscador): https://www.r-bloggers.com/2015/08/is-bayesian-ab-testing-immune-to-peeking-not-exactly/"
  - "Alex Molas, Bayesian A/B test peeking (2025; según el resumen del buscador): https://www.alexmolas.com/2025/10/30/bayesian-ab-test-peeking.html"
  - "Andrew Gelman y John Carlin, Beyond Power Calculations: Assessing Type S (Sign) and Type M (Magnitude) Errors, Perspectives on Psychological Science 9(6), 641-651, 2014 (según su resumen): https://sites.stat.columbia.edu/gelman/research/published/PPS551642_REV2.pdf"
  - "Twitter Engineering, Power, minimal detectable effect, and bucket size estimation in A/B tests (2016; según el resumen del buscador): https://blog.twitter.com/2016/power-minimal-detectable-effect-and-bucket-size-estimation-in-ab-tests"
  - "Gelman y Loken, jardín de los senderos que se bifurcan; Simmons et al. (2011); Rubin (2023); Murayama et al. (2013), según resúmenes del buscador: https://philarchive.org/archive/RUBTIE y https://confidence.spotify.com/glossary/garden-of-forking-paths"
  - "Datos/.investigacion/estadistica.md (sección 5)"
  - "Datos/.investigacion/posicion-contraria.md (sección 4)"
aliases: [significancia estadística, statistical significance, significación estadística, peeking, mirar antes de tiempo, comparaciones múltiples, multiple comparisons, error tipo M, error tipo S, efecto mínimo detectable, MDE]
creado: 2026-11-27
revisado: 2026-11-27
---

# Significancia

La significancia, en un experimento, es el criterio para decidir si la diferencia entre dos variantes es real o salió del azar. Funciona solo si el tamaño de muestra y la regla de parada se fijan antes de mirar, y con poco tráfico exagera los efectos que encuentra.

Es la [inferencia](muestreo-e-inferencia.md) (p-valor, potencia, intervalos) aplicada a un diseño. El diseño y la decisión del experimento, qué probar, qué métricas de guarda poner y cuándo no conviene, están en [experimento A/B](../../Producto/Medicion/experimento-ab.md), en Producto. Acá queda cómo se lee el resultado y cómo se arruina la lectura.

## Frecuentista y bayesiana, dos formas de leer el mismo experimento

La lectura frecuentista, la más común, calcula un p-valor: qué tan raro sería ver esta diferencia si las variantes fueran iguales. Si baja de un umbral fijado antes, casi siempre 5 %, se declara significativa. Qué dice y qué no dice ese número lo fija la declaración de la ASA de 2016, en [muestreo e inferencia](muestreo-e-inferencia.md#qué-es-un-p-valor-y-qué-no-es).

La lectura bayesiana parte de una creencia previa (el prior) y la actualiza con los datos. Da una respuesta que suena más directa: la probabilidad de que B sea mejor que A, o cuánto se pierde si se elige B y era peor. Según la página de Spotify, con un prior plano, parar cuando la probabilidad de que B supere a A pasa de 0,95 equivale a parar cuando el p-valor baja de 0,05. La misma página concede que el enfoque bayesiano se justifica cuando hay un prior bien calibrado o costos de decisión explícitos.

Elegir una u otra cambia el vocabulario más que el problema: las dos se rompen si se mira el resultado sin una regla.

## Mirar antes de tiempo

Mirar el resultado mientras corre el experimento y pararlo cuando da significativo (peeking) multiplica los falsos positivos. Miller lo dice así: «Repeated significance testing always increases the rate of false positives». Cada mirada es una prueba más, y basta que una cruce el umbral por azar para declarar un ganador que no existe.

Miller da un ejemplo simulado: conversión del 50 %, un cambio que no hace nada, y una revisión después de cada observación hasta un máximo de 150. La tasa de falsos positivos llega a 26,1 %, más de cinco veces el 5 % que se cree estar aceptando. También da cuánto hay que exigir en cada mirada para que el error total siga en 5 %:

| Miradas | Umbral por mirada |
|---|---|
| 1 | 2,9 % |
| 2 | 2,2 % |
| 3 | 1,8 % |
| 5 | 1,4 % |
| 10 | 1,0 % |

Las cifras vienen de la página de Miller, leída por un sistema que la resume; otra lectura no pudo confirmar el 26,1 %. Su regla es fijar el tamaño de muestra antes de empezar y no mirar la significancia hasta llegar: n = 16σ²/δ² por variante, donde δ es el efecto más chico que importa detectar y σ² = p(1 − p) para una tasa de conversión. Corresponde aproximadamente a potencia del 80 % y α del 5 % (lectura de la base).

La salida para quien necesita mirar es la inferencia secuencial. Johari, Pekelis y Walsh muestran que los p-valores y los intervalos clásicos «are wholly unreliable if users endogenously choose samples sizes», y proponen p-valores «always valid», que se pueden mirar cuantas veces se quiera. Los autores estarían ligados a una plataforma comercial de experimentos (no verificado).

> [!IMPORTANT]
> Si la lectura bayesiana resiste el peeking está en disputa. Miller sostiene que un diseño bayesiano permite parar cuando se quiera. Spotify, un proveedor, publica simulaciones propias: parar por probabilidad de superioridad bajo monitoreo continuo da 30,3 % de falsos positivos, parar por pérdida esperada alrededor de 50 %, y parar por factor de Bayes como mucho 5 %. Un análisis de 2015 en R-bloggers y un post de 2025 sostienen que el bayesiano común tampoco es inmune. No apareció una comparación independiente: las cifras son de proveedores y practicantes.

## Comparaciones múltiples

Probar muchas métricas, muchos segmentos o muchas variantes a la vez tiene el mismo efecto que mirar muchas veces. Con 20 comparaciones al 5 %, se espera alrededor de un falso positivo aunque nada funcione (cálculo de la base). El libro de Kohavi, Tang y Xu trata el problema en el capítulo 3, sobre la ley de Twyman, según su índice.

El mismo riesgo aparece sin intención, cuando el análisis se decide después de ver los datos: qué segmento mirar, qué período cortar, qué valores atípicos sacar. Gelman y Loken lo llaman el jardín de los senderos que se bifurcan. Simmons y otros (2011) sostienen que esa flexibilidad «dramatically increases actual false-positive rates»; Rubin (2023) y Murayama y otros (2013) dicen que la inflación está exagerada. Las dos posiciones se leyeron por resúmenes.

La defensa práctica es declarar antes una métrica principal y tratar lo demás como exploración que pide otro experimento (lectura de la base). Según diapositivas de terceros sobre los materiales de Kohavi, sin verificar en el libro, el riesgo de que un resultado con p = 0,05 sea falso depende de cuántas ideas funcionan en general: si funciona el 15 %, ese riesgo ronda el 15 % y no el 5 %.

## Por qué el tráfico bajo exagera los efectos

Con poco tráfico, un experimento solo puede detectar efectos enormes. Para un tamaño de muestra y una varianza dados, se puede calcular el menor efecto que el experimento detecta con 80 % de potencia, el efecto mínimo detectable, como explica el blog de ingeniería de Twitter.

Un cálculo de la base con la regla de Miller: una tienda convierte el 2 % y quiere detectar una suba a 2,4 %, una mejora relativa del 20 %. Hacen falta unos 19.600 visitantes por variante, 39.200 en total. Con 500 visitas diarias, son casi 80 días sin tocar nada más.

Esperar no es el único costo. Gelman y Carlin definen dos errores que aparecen cuando un experimento con poca potencia da significativo. El error de tipo S es que el efecto tenga el signo equivocado; el de tipo M, cuánto se sobreestima su tamaño. En un ejemplo del paper, leído por resumen, con potencia del 13 % el efecto significativo exagera el real 3,11 veces en promedio, y el 2 % de las veces tiene el signo cambiado. Un experimento chico que «da ganador» con una suba del 30 % probablemente esconde una mucho menor (lectura de la base).

Para un comercio chico se desprende (lectura de la base):

- Probar cambios grandes, no ajustes de color: son los únicos que el experimento puede ver.
- Probar pocas variantes a la vez; cada una divide el tráfico.
- Leer el intervalo y desconfiar de efectos grandes con pocos datos.
- Cuando no hay volumen, cambiar de método, como dice [experimento A/B](../../Producto/Medicion/experimento-ab.md#cuándo-un-experimento-no-sirve), o comparar contra un grupo que no recibió el cambio con [diferencias en diferencias](correlacion-y-causalidad.md#diferencias-en-diferencias-cuando-no-se-puede-sortear).

> [!NOTE]
> Sin fuente todavía: un tráfico mínimo de referencia para correr un experimento. Según un practicante, no existe una regla universal; lo que dice el libro de Kohavi sobre productos chicos no se leyó.

## Leer a Miller y a Gelman y Carlin

Para el peeking, la página de Miller (2010) es corta y tiene los números; fijarse en la tabla de umbrales y en la regla de tamaño de muestra. Para el tráfico bajo, el paper de Gelman y Carlin (2014), en las secciones sobre los errores de tipo S y M y sobre diseñar con efectos realistas. Para lo demás, el capítulo 3 de Kohavi, Tang y Xu.
