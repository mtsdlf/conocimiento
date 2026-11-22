---
resumen: >-
  La evaluación competitiva compara la usabilidad del producto propio con la de dos a cuatro rivales, con las mismas tareas y las mismas métricas. Se hace como revisión de un experto o como test con usuarios, y su fin es mejorar el diseño propio, no declarar un ganador ni copiar al líder.
estado: borrador
estabilidad: semi
fuentes:
  - "Tim Neusesser, NN/g (5-ene-2024), Competitive Usability Evaluations: https://www.nngroup.com/articles/competitive-usability-evaluations/ (leída a través del resumen de una herramienta)"
  - "Kate Moran, NN/g (3-may-2020), 7 Steps to Benchmark Your Product's UX: https://www.nngroup.com/articles/benchmarking-ux/ (leída a través del resumen de una herramienta)"
  - "MeasuringU, Competitive & Benchmark UX Evaluation (página de servicio): https://measuringu.com/?p=8464 (leída a través del resumen de una herramienta)"
  - "MeasuringU, SUPR-Q: https://measuringu.com/suprq/ (leída a través del resumen de una herramienta); Sauro (2015), SUPR-Q: A Comprehensive Measure of the Quality of the Website User Experience, Journal of Usability Studies, pp. 68-86: https://uxpajournal.org/?p=2506 (según resumen del buscador)"
  - "Lewis y Sauro (11-feb-2026), Sample Sizes for Comparing UX-Lite Scores: https://measuringu.com/sample-sizes-for-comparison-of-ux-lite-scores/ (leída a través del resumen de una herramienta)"
  - "Sauro y Lewis, Quantifying the User Experience, 2.ª ed. (2016), caps. 5 y 6 (según índice y resumen; el texto no se leyó)"
  - "Jakob Nielsen, NN/g (21-ago-1999), Do Interface Standards Stifle Design Creativity?: https://www.nngroup.com/articles/do-interface-standards-stifle-design-creativity/ (leída a través del resumen de una herramienta); Jakob's Law of Internet User Experience (video, 2017): https://www.nngroup.com/videos/jakobs-law-internet-ux/ (según resumen)"
  - "UX/.investigacion/evaluacion-competitiva-y-cambio.md"
aliases: [competitive usability evaluation, evaluación competitiva de usabilidad, test competitivo, competitive usability test, revisión competitiva, competitive review, benchmark competitivo, competitive benchmarking, SUPR-Q]
creado: 2026-11-22
revisado:
---

# Evaluación competitiva

La evaluación competitiva compara la usabilidad del producto propio con la de dos a cuatro rivales, con las mismas tareas y las mismas métricas. Se hace como revisión de un experto o como test con usuarios, y su fin es mejorar el diseño propio, no declarar un ganador ni copiar al líder.

Es la mirada de UX del catálogo de [perspectivas de análisis](../../Estrategia-competitiva/Analisis-de-competidores/perspectivas-de-analisis.md) de Estrategia competitiva. El [desarme de producto](../../Estrategia-competitiva/Analisis-de-competidores/desarme-de-producto.md) mira qué hace el rival; esta evaluación mide qué tan fácil se hace una tarea en cada producto. Qué rivales entran sale de la [identificación de competidores](../../Estrategia-competitiva/Analisis-de-competidores/identificacion-de-competidores.md).

## Revisión de experto o test con usuarios

NN/g la define como "Comparing your product against several competing designs" y distingue dos formas (Neusesser, 2024). Las dos usan métodos que ya tienen nota; lo propio de la comparación es repetir el mismo protocolo en varios productos.

| Forma | Quién evalúa | Método base | Qué entrega |
|---|---|---|---|
| Revisión competitiva | un experto, sin usuarios | [evaluación heurística](evaluacion-heuristica.md) o recorrido de tareas | fortalezas, debilidades, tendencias y patrones de cada producto |
| Test competitivo | participantes haciendo tareas | [test de usabilidad](test-de-usabilidad.md) sobre el producto propio y los ajenos | dónde se traba la gente en cada uno y, con métricas, cuál rinde mejor |

La guía pone el foco "typically" en 2 a 4 rivales. Si hay muchos, una revisión inicial elige los de contenido parecido, buena UX, diseño innovador o más clientes en común. También sugiere mirar fuera de los rivales directos, hacia empresas chicas o de rubros vecinos.

## Cómo se arma el test competitivo

Cada participante prueba dos o tres productos. NN/g advierte que "Testing more than 3 sites with any given participant can overwhelm the study participants." Las tareas son las mismas en todos y representan lo que el cliente hace de verdad.

El orden importa porque el segundo producto se beneficia de lo aprendido en el primero. Por eso la guía pide alternar: "Alternate which sites are paired together and which is tested first for each user." Al final de la sesión, el participante compara los productos que usó.

En una plataforma de tiendas online, las tareas podrían ser publicar el primer producto, configurar el envío y cobrar la primera venta, en la propia y en dos rivales (ejemplo de esta base).

## Las métricas que se pueden comparar

NN/g nombra cuatro formas de decidir quién rinde mejor: tasa de éxito, tiempo en tarea, valoraciones subjetivas o una tarjeta de puntaje propia. Las tres primeras se definen en [métricas de UX](metricas-de-ux.md#métricas-de-un-test-con-personas), junto con el SUS. Lo que agrega la comparación es una referencia: según Moran (NN/g, 2020), "A single number is meaningless, since you have no idea whether it's good or bad". Su ejemplo es literal: "Our success rate for application completion is 86%, while our competitor's is 62%."

Para sitios web, MeasuringU propone el SUPR-Q, "an 8 item questionnaire for measuring the quality of the website user experience". Mide usabilidad, confianza, lealtad y apariencia, y da el puntaje como percentil: 50 es el promedio y 75 supera al 75% de los sitios de su base. La base de comparación es de MeasuringU y su tamaño varía en la propia página, entre 150 y 200 sitios. Según el resumen de un buscador, el paper de Sauro (2015) parte de unas 4.000 respuestas sobre más de 100 sitios.

El benchmark competitivo es investigación sumativa. Moran lo dice así: "Benchmarking is not formative; it is a summative evaluation." Mide al final de un ciclo de diseño; el test formativo con pocos usuarios sirve, en cambio, para encontrar problemas mientras se diseña.

## Cuántos participantes hacen falta para comparar

Encontrar problemas pide pocos participantes; afirmar que un producto rinde más que otro pide muchos más. El debate de los cinco usuarios vale para lo primero y está en el [test de usabilidad](test-de-usabilidad.md#de-dónde-sale-la-regla-de-los-cinco-usuarios). Para lo segundo hace falta estadística: Sauro y Lewis dedican el capítulo 5 de *Quantifying the User Experience* a si hay diferencia entre dos diseños y el 6 al tamaño de muestra (según su índice; el texto no se leyó).

El piso de unos 20 participantes que da el [test de usabilidad](test-de-usabilidad.md) para métricas sirve para medir un producto solo; comparar dos pide más, porque hay que distinguir una diferencia del ruido de cada medición (lectura de esta base a partir de las dos notas). El diseño del estudio cambia mucho la cuenta. Si los mismos participantes usan los dos productos (intra-sujetos), alcanza con menos gente que si cada grupo usa uno (entre-sujetos). Lewis y Sauro (2026) lo calculan para el cuestionario UX-Lite, con potencia del 80%:

| Diferencia a detectar (puntos de 100) | Intra-sujetos, 90% / 95% de confianza | Entre-sujetos, 90% / 95% |
|---|---|---|
| 15 | 12 / 15 | 44 / 56 |
| 10 | 25 / 32 | 94 / 120 |
| 5 | 94 / 119 | 372 / 470 |

La regla que dan es que el estudio entre-sujetos pide "about four times" la muestra del intra-sujetos. La tabla es de UX-Lite; para SUS o SUPR-Q no se leyó una tabla equivalente, aunque el método es el mismo.

> [!NOTE] Sin fuente todavía: una tabla de tamaño de muestra para comparar SUS, SUPR-Q, tasa de éxito o tiempo entre dos productos. La de arriba ilustra el orden de magnitud con otro cuestionario.

## Cuándo conviene y cuánto cuesta

NN/g la recomienda como actividad temprana de investigación, y sirve incluso con prototipos en papel de variantes propias. Repetida en el tiempo, "these evaluations tend to be expensive" y conviene a organizaciones con madurez de UX y presupuesto.

La única cifra de costo leída es de un proveedor, sobre su propio servicio. MeasuringU da un precio típico de US$20.000 a 80.000 y de 5 a 8 semanas por encargo. Según la misma página, la mayoría de sus benchmarks no moderados tienen entre 100 y 200 participantes, con un margen de error de cerca de 5 a 7%. En un estudio competitivo la muestra es "usually twice the size of a standalone study". Es una sola fuente, interesada, y su precio probablemente refleja el mercado de EE.UU. (inferencia de esta base).

## Las convenciones se adoptan, la ventaja se busca en otro lado

La guía de NN/g cierra con "You want to beat the competition, not copy them." Copiar la interfaz del líder tiene un argumento a favor y uno en contra, y los dos son de Nielsen. A favor, la Ley de Jakob: "Users spend most of their time on other sites", así que esperan que un producto funcione como los que ya usan.

En contra, el mismo Nielsen (1999) separa el vocabulario de la historia. Un estándar asegura que se entienda cada elemento, y apartarse de él cuesta "major usability problems" salvo "a very, very good reason". Pero "the most important design elements are those that cannot be specified by a standard": la estructura, el flujo y el ajuste al [modelo mental](../Percepcion-y-decision/modelo-mental.md) del usuario.

De ahí sale una regla de esta base para leer una evaluación competitiva. Lo que todos los rivales resuelven igual (el carrito arriba a la derecha, el botón de pagar al final) es convención y se adopta. Lo que el líder resuelve distinto y mejor es una pista sobre la tarea, no un diseño para calcar. La diferenciación que importa al cliente se piensa en [distintividad o diferenciación](../../Marketing/Propuesta/distintividad-o-diferenciacion.md), y el riesgo de construir lo que el rival tiene porque lo tiene está en [desarme de producto](../../Estrategia-competitiva/Analisis-de-competidores/desarme-de-producto.md).

## Qué leer

Neusesser, [Competitive Usability Evaluations](https://www.nngroup.com/articles/competitive-usability-evaluations/), de NN/g: fijarse en elegir de 2 a 4 rivales con criterio, alternar el orden y medir tareas. Para la estadística, Sauro y Lewis, *Quantifying the User Experience*, capítulos 5 y 6: qué prueba usar según la métrica sea binaria o continua, y según los mismos usuarios estén o no en los dos grupos.

> [!NOTE] Las citas de NN/g y MeasuringU salen de un resumen que una herramienta hizo de cada página; el paper de SUPR-Q y el libro de Sauro y Lewis no se leyeron. Conviene cotejarlos antes de pasar la nota a vigente.
