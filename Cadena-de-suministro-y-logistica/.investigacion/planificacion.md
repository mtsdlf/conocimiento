# Planificación (vertical): informe de investigación

Alcance: planificacion (entrada), pronostico-de-demanda, error-de-pronostico, plan-de-ventas-y-operaciones, planificacion-de-la-distribucion, efecto-latigo.

## Aviso de cobertura (leer primero)

- El presupuesto de búsqueda web de la sesión se agotó tras la primera ronda. Muchos sitios de editoriales (ScienceDirect, INFORMS, JSTOR) devolvieron 403, y las rutas probadas de MIT OCW dieron 404.
- Quedó verificado y leído lo que figura con [L] o [S] y URL. Todo lo que figura bajo «Sin verificar» es conocimiento previo del investigador: no tiene URL leída en esta sesión y hay que confirmarlo antes de publicarlo como vigente.
- Nada de lo de alto riesgo (ley, plata) cae en este ángulo, así que no hay afirmaciones que exijan doble fuente por esa razón.
- Convención de puntajes: A = autoridad, P = profundidad, E = ejemplos, U = unicidad, de 1 a 3. Marca: [L] texto completo o sección completa leída, [M] metadatos o abstract, [S] resumen secundario o del buscador.

## Fuentes verificadas en esta sesión (tabla general)

| Id | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| F1 | Hyndman y Athanasopoulos, FPP3, «Evaluating point forecast accuracy» | https://otexts.com/fpp3/accuracy.html | primaria (libro de texto abierto) | 3/3/3/2 | [S] (extracto devuelto por el lector, con citas literales) |
| F2 | FPP3, «Forecasting hierarchical and grouped time series» | https://otexts.com/fpp3/hierarchical.html | primaria | 3/3/2/3 | [S] |
| F3 | FPP3, «Judgmental forecasts» | https://otexts.com/fpp3/judgmental.html | primaria | 3/2/2/3 | [S] |
| F4 | FPP3, «Simple forecasting methods» | https://otexts.com/fpp3/simple-methods.html | primaria | 3/2/2/2 | [S] |
| F5 | FPP3, «Exponential smoothing» | https://otexts.com/fpp3/expsmooth.html | primaria | 3/3/2/2 | [S] |
| F6 | FPP3, «Estimation and model selection» (ETS, AICc) | https://otexts.com/fpp3/ets.html | primaria | 3/2/2/2 | [S] |
| F7 | FPP3, «Forecasting count time series» (Croston) | https://otexts.com/fpp3/counts.html | primaria | 3/2/2/3 | [S] |
| F8 | Lee, Padmanabhan y Whang (1997), «Information Distortion in a Supply Chain: The Bullwhip Effect», Management Science 43(4), 546-558 (copia en PDF alojada en un sitio universitario, con la carátula de JSTOR) | https://courses.ie.bilkent.edu.tr/ie102/wp-content/uploads/sites/12/2019/02/Lee-Padmanabhan-Whang-1997-MS.pdf | primaria | 3/3/3/3 | [L] parcial: abstract, introducción y la tabla 1 de causas y contramedidas, extraídos con pdftotext; el cuerpo matemático no se leyó |
| F9 | Mismo paper, registro bibliográfico | https://ideas.repec.org/a/inm/ormnsc/v43y1997i4p546-558.html | secundaria (índice) | 2/1/1/1 | [M] |
| F10 | Bray y Mendelson (2012), «Information Transmission and the Bullwhip Effect: An Empirical Investigation», Management Science 58(5), 860-875 (PDF del sitio de la facultad, versión Articles in Advance) | https://www.kellogg.northwestern.edu/faculty/bray/doc/bw/bw_d.pdf | primaria | 3/3/3/3 | [L] parcial: abstract e introducción |
| F11 | Cachon, Randall y Schmidt (2007), «In Search of the Bullwhip Effect», MSOM 9(4), 457-479, DOI 10.1287/msom.1060.0149 (registro en repositorio de Penn; el abstract no se pudo traer: 403) | https://repository.upenn.edu/oid_papers/137 | primaria | 3/3/3/3 | [S] vía buscador y vía las citas de F10 |
| F12 | APQC Process Classification Framework, Cross Industry, versión 7.4 (2024), categoría 4.1 | https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf | primaria (marco) | 3/2/2/2 | [L] de la categoría 4.1 (pdftotext) |

Nota de corrección de la tabla: F2 es el capítulo sobre series jerárquicas y agrupadas y F3 el de pronósticos de juicio; los números de capítulo exactos de FPP3 no se verificaron, por eso las filas no los afirman (se citan por título y URL).

## 1. planificacion (entrada)

### Afirmaciones verificadas

- APQC 7.4 no usa una «jerarquía de planes» con esos nombres, pero su categoría 4.1 «Plan for and align supply chain resources (10215)» agrupa lo que este tema divide: 4.1.1 «Develop production and materials strategies», 4.1.2 «Manage demand for products», 4.1.3 «Create materials plan», 4.1.4 «Create and manage master production schedule», 4.1.5 «Plan distribution requirements (17042)», 4.1.6 «Establish distribution planning constraints» y 4.1.7 «Review distribution planning policies». [F12, [L]]
- Dentro de 4.1.2 aparecen, en este orden: «Develop baseline demand forecasts», «Collaborate demand with customers», «Develop demand consensus forecast», «Determine available to promise», «Monitor activity against demand forecast», «Evaluate and revise demand forecasting approach» y «Measure demand forecast accuracy». [F12]
- Dentro de 4.1.5 «Plan distribution requirements» (el DRP de este tema): «Maintain master data», «Determine finished goods inventory requirements at destination», «Determine product storage facility requirements», «Calculate requirements at destination», «Calculate consolidation at source», «Manage collaborative replenishment planning», «Calculate and optimize destination dispatch plan», «Manage dispatch plan attainment», «Calculate and optimize destination load plans», «Manage partner load plan», «Manage cost of supply», «Manage capacity utilization». [F12]
- APQC no tiene un proceso llamado S&OP dentro de 4.1: el «consenso de demanda» (4.1.2.3) y las estrategias de producción y materiales (4.1.1) hacen su papel. Esto hay que decirlo en la nota para no inventar una correspondencia.

### Sin verificar (conocimiento previo, a confirmar)

- Jerarquía de planes por horizonte (estratégico a años, S&OP a 18-24 meses por familia y mes, plan maestro semanas a meses por producto, DRP/MRP por semana y artículo, ejecución diaria). Fuentes candidatas: Chopra y Meindl, cap. «Aggregate planning» y «Sales and operations planning»; Simchi-Levi et al., cap. de planificación; diccionario ASCM. Ninguna se leyó.
- Empujar frente a tirar: Chopra y Meindl lo definen por si la ejecución se dispara por un pronóstico o por un pedido real; ASCM tiene la entrada de diccionario. Sin leer.

### Qué registra un sistema

Solo lo que sostiene APQC 4.1 como evidencia de objetos comunes: un pronóstico base y un pronóstico de consenso (dos versiones del mismo pronóstico), disponible para prometer, plan de materiales sin restricciones y con restricciones («unconstrained plan» y «constrained plan», 4.1.3.1 y 4.1.3.5), plan de distribución por destino y datos maestros de planificación («Maintain master data»). No se leyó documentación de sistemas abiertos en esta sesión (hueco).

### Recurso canónico propuesto

APQC PCF 7.4, sección 4.1 completa (las 4 páginas, ~2 por la 4.1) como el mapa de procesos de planificación. Fijarse en la numeración 4.1.2 y 4.1.5, que fijan el vocabulario. Para la jerarquía de planes: Chopra y Meindl, capítulos de planificación (a confirmar en la edición vigente).

## 2. pronostico-de-demanda

### Afirmaciones verificadas

- Métodos de referencia (los que se usan para comparar): «the forecasts of all future values are equal to the average (or "mean") of the historical data» (media); «For naïve forecasts, we simply set all forecasts to be the value of the last observation» (ingenuo); «we set each forecast to be equal to the last observed value from the same season» (ingenuo estacional); «the amount of change over time (called the drift) is set to be the average change seen in the historical data» (deriva). [F4]
- Suavizado exponencial: «Simple exponential smoothing has a "flat" forecast function»; el método de Holt agrega tendencia («no longer flat but trending»); la tendencia amortiguada hace que «short-run forecasts are trended while long-run forecasts are constant»; Holt-Winters agrega estacionalidad aditiva o multiplicativa. [F5]
- Marco ETS: cada método tiene un modelo de espacio de estados «ETS(Error, Trend, Seasonal)»; combinando tendencia (ninguna, aditiva, amortiguada) con estacionalidad (ninguna, aditiva, multiplicativa) salen nueve métodos; al ser modelos estadísticos dan intervalos de predicción y permiten elegir por AICc. [F5, F6]
- Elección por AICc: «We let the ETS() function select the model by minimising the AICc». [F6]
- Demanda intermitente: Croston (1972) construye dos series, los valores de demanda no nulos y el tiempo entre ellos, las suaviza por separado y el pronóstico es su cociente. Croston preveía parámetros fijos de 0,1. FPP3 dice: «Forecasts obtained from Croston's method are also known to be biased», con cita de Syntetos y Boylan (2001), «On the bias of intermittent demand estimates»; y que el método «does not correspond to any statistical model», así que no hay intervalos algebraicos. [F7]
- Pronóstico jerárquico: series jerárquicas son anidadas (región dentro de provincia dentro del total); las agrupadas tienen atributos cruzados y «does not naturally disaggregate in a unique hierarchical manner». Abajo-arriba (pronosticar cada serie de la base y sumar), arriba-abajo (pronosticar el total y repartir con proporciones), del medio hacia afuera (solo estructuras estrictamente jerárquicas) y reconciliación óptima (MinT, de Wickramasuriya et al., 2019: «minimises the total forecast variance of the set of coherent forecasts»). En los ejemplos del capítulo MinT fue más preciso que abajo-arriba. [F2]
- Juicio: «Judgmental forecasts are subjective, and therefore do not come free of bias or limitations»; el anclaje hace que los pronósticos subsiguientes «tend to converge or be close to an initial familiar reference point»; Delphi busca «consensus forecasts from a group of experts in a structured iterative manner», anónimo, con retroalimentación, normalmente dos o tres rondas; pronóstico por analogía; recomendación de separar a quien pronostica de quien usa («Forecasters and users should be clearly segregated») y de evaluar sistemáticamente. [F3]

### Sin verificar (conocimiento previo, a confirmar)

- Syntetos y Boylan (2005), corrección de Croston (SBA, factor 1 − α/2) y clasificación SBC de la demanda en suave, errática, irregular y a golpes con los umbrales ADI = 1,32 y CV² = 0,49: no se leyó la fuente.
- Fildes y Goodwin: ajustes de juicio sobre pronósticos estadísticos; el hallazgo habitual es que los ajustes pequeños y los hacia arriba suelen restar precisión y los grandes y hacia abajo suelen sumar. Hay que leer Fildes, Goodwin, Lawrence y Nikolopoulos (2009) y Fildes y Goodwin (2007, Interfaces) antes de afirmar números.
- Competencias M: M4 (100.000 series, 61 métodos; ganó un híbrido de suavizado exponencial y redes) y M5 (Walmart, datos jerárquicos de ventas diarias, ganaron métodos basados en LightGBM). Las dos páginas de ScienceDirect dieron 403: no hay lectura de ninguna. Fuente a leer: Makridakis, Spiliotis y Assimakopoulos, International Journal of Forecasting 2020 y 2022.
- Demanda censurada por faltantes (las ventas no son la demanda cuando hubo quiebre de stock): concepto estándar de gestión de ingresos y de inventario, sin fuente leída. Candidata: Talluri y van Ryzin, The Theory and Practice of Revenue Management (sobre desrestringir, «unconstraining»).

### Qué registra un sistema

Series históricas por artículo, ubicación y período (con la unidad de tiempo), el origen del dato (venta, pedido, despacho: cuál se toma como «demanda»), un indicador de quiebre o de promoción que permite corregir la demanda, la jerarquía de agregación (artículo, familia, región, total) como estructura propia, versiones del pronóstico (estadístico, ajustado por juicio, consenso) con autor y fecha, y el método y los parámetros con que se generó. Esto se infiere de FPP3 y de APQC 4.1.2 (pronóstico base, consenso). No hay lectura de sistemas abiertos.

### Recurso canónico propuesto

FPP3 (Hyndman y Athanasopoulos, https://otexts.com/fpp3/): capítulos de métodos simples, suavizado exponencial, evaluación de exactitud, jerárquicos y de juicio; fijarse en la idea de que primero se compara contra el ingenuo y el ingenuo estacional. Para lo intermitente, la sección de series de conteo (13.2 según el índice) y, de ahí, Syntetos y Boylan.

## 3. error-de-pronostico

### Afirmaciones verificadas

- MAE = media de |e_t|; el error porcentual es p_t = 100 e_t / y_t y MAPE = media de |p_t|. [F1]
- Problemas del MAPE, literales: «being infinite or undefined if y_t = 0 for any t in the period of interest»; «having extreme values if any y_t is close to zero»; «they put a heavier penalty on negative errors than on positive errors»; «they assume the unit of measurement has a meaningful zero». [F1]
- MASE: el error escalado q_j divide el error de pronóstico por el error absoluto medio del ingenuo de un paso sobre los datos de entrenamiento (con el ingenuo estacional si hay estacionalidad); MASE = media de |q_j|; es independiente de la escala; «A scaled error is less than one if it arises from a better forecast» que el ingenuo promedio. [F1]
- Criterio de evaluación: la exactitud se mide sobre datos de prueba que no se usaron para ajustar el método. [F1] (resumen; el texto literal quedó sin traer)

### Sin verificar (conocimiento previo, a confirmar)

- Sesgo (error medio con signo) y señal de seguimiento (tracking signal = suma acumulada de errores / MAD, con límites habituales de ±4 a ±6): fuente candidata, Chopra y Meindl y Silver, Pyke y Thomas; sin leer.
- WAPE (suma de |e| / suma de y): definición habitual; sin fuente leída.
- Hyndman y Koehler (2006), «Another look at measures of forecast accuracy», International Journal of Forecasting: origen del MASE; solo citado por F1 en forma indirecta, no leído.
- Valor agregado del pronóstico (forecast value added, FVA): proviene de la práctica de Michael Gilliland (SAS); es fuente de práctica y secundaria; no se leyó.
- El uso del error para dimensionar el stock de seguridad vive en Inventario y depósitos: solo se enlaza.

### Qué registra un sistema

Por cada pronóstico, el valor real que se compara y el rezago al que se evalúa (el pronóstico hecho con cuántos períodos de anticipación), el error calculado con una medida elegida, y las agregaciones por artículo, familia y ubicación; la métrica que se usa debe quedar guardada junto al número, porque MAPE, WAPE y MASE no son intercambiables. Inferido de F1; sin lectura de sistemas abiertos.

### Recurso canónico propuesto

FPP3, sección «Evaluating point forecast accuracy» (https://otexts.com/fpp3/accuracy.html): leerla entera; fijarse en la lista de problemas del MAPE y en la lectura del MASE contra 1.

## 4. plan-de-ventas-y-operaciones

### Afirmaciones verificadas

- Solo lo que dice APQC: el consenso de demanda (4.1.2.3) y la «Collaborate demand with customers» (4.1.2.2) son procesos de planificación distintos del plan de materiales y del plan maestro de producción (4.1.4). [F12]

### Sin verificar: esta componente quedó prácticamente sin fuente leída

- Thomé, Scavarda, Fernandez y Scavarda (2012), «Sales and operations planning: A research synthesis», International Journal of Production Economics 138(1), 1-13. La página de ScienceDirect dio 403 y la búsqueda se agotó antes de poder verificar el abstract. Confirmar autores, año y conclusiones antes de citar.
- El ciclo mensual de cinco pasos (datos, demanda, abastecimiento, reunión previa, reunión ejecutiva) es el que difunden Oliver Wight y la bibliografía de ASCM/APICS; no se leyó ninguna fuente que lo diga con esas palabras.
- Estrategias de nivelación (perseguir, nivelar, mixta): Chopra y Meindl y Simchi-Levi et al., en el tema de planificación agregada; sin leer.
- Diferencia con presupuesto anual y plan maestro de producción: sin fuente leída.
- Madurez: modelos de madurez de S&OP (p. ej., los de Grimson y Pyke 2007); sin leer.

### Qué registra un sistema

Sin fuentes leídas para esto. Lo plausible, a confirmar: un plan por familia y por mes con versiones (propuesta de demanda, propuesta de abastecimiento, plan acordado), supuestos, brechas entre demanda y capacidad, y decisiones tomadas en la reunión ejecutiva con responsable. Marcar como inferido en la nota.

### Recurso canónico propuesto

Dos candidatos sin leer: (1) la entrada de S&OP del diccionario de ASCM y su programa CPIM 2026; (2) Thomé et al. (2012) como síntesis de la evidencia. Hay que leerlos antes de escribir la nota.

## 5. planificacion-de-la-distribucion

### Afirmaciones verificadas

- APQC 4.1.5 «Plan distribution requirements» incluye, como pasos, calcular necesidades en el destino, calcular la consolidación en origen, manejar la reposición colaborativa, optimizar el plan de despacho y las cargas, y gestionar la restricción de capacidad (lista completa en la sección de planificacion). [F12]
- APQC 4.1.7.3 «Establish dynamic deployment policies» y 4.1.6 («Establish distribution planning constraints») muestran que los parámetros de la red (capacidad de depósito, restricciones de transporte, de inventario) se tratan como datos de entrada del plan. [F12]
- Lee et al.: el control único de la reposición y el VMI aparecen como contramedidas del «demand signaling» (tabla 1, con P&G y Walmart como práctica citada). [F8]

### Sin verificar: componente casi sin fuente leída

- DRP: André J. Martin, Distribution Resource Planning (1983) es el origen; la tabla por período (necesidades brutas, recepciones programadas, stock proyectado, necesidades netas, pedidos planificados) se parece a la del MRP y se cita en el diccionario de ASCM y en Chopra y Meindl. Nada de esto se leyó.
- Cómo se suman los depósitos hacia el central (la demanda dependiente de los depósitos es la demanda independiente de la red): afirmación estándar de manuales; sin fuente.
- Diferencia con el punto de pedido: contrastar con la nota de Inventario y depósitos, ya escrita en este repo.

### Qué registra un sistema

Por cada depósito y artículo: horizonte en períodos, necesidades brutas (pronóstico y pedidos de clientes), recepciones programadas, stock proyectado a fin de período, necesidades netas y pedidos planificados con fecha de lanzamiento (desfasada por el plazo de transporte), además del origen que abastece a cada depósito (el árbol de la red). Parámetros por artículo y depósito: stock de seguridad, tamaño de lote, plazo. Es la lógica de APQC 4.1.5 («Calculate requirements at destination», «Calculate consolidation at source») más conocimiento previo; sin documentación abierta leída.

### Recurso canónico propuesto

Sin recurso verificado. Candidato: la sección de DRP de Martin (1983) o de un manual de gestión de operaciones; y APQC 4.1.5 como lista de pasos.

## 6. efecto-latigo

### Afirmaciones verificadas

- Definición y alcance: «the bullwhip effect or whiplash effect refers to the phenomenon where orders to the supplier tend to have larger variance than sales to the buyer (i.e., demand distortion), and the distortion often increases as one moves upstream». [F8]
- Las cuatro causas del abstract: «demand signal processing, rationing game, order batching, and price variations»; y «Actions that can be taken to mitigate the detrimental impact of this distortion are also discussed». [F8, F9]
- Tabla 1 del paper (causa, factores, contramedidas): señalización de demanda (sin visibilidad de la demanda final, pronósticos múltiples, plazos largos) con acceso a datos de venta al consumidor, control único de la reposición, VMI y reducción de plazos; agrupación de pedidos (costo alto por pedido, economías de camión completo, pedidos aleatorios o correlacionados) con EDI, descuentos por carga mixta, consolidación por terceros y citas de entrega regulares; precios fluctuantes (alto-bajo) con precio bajo todos los días (EDLP); juego de escasez (racionamiento proporcional, ignorancia de la oferta, pedidos sin restricción) con asignación según ventas pasadas y compartir información de capacidad. [F8, [L]]
- Evidencia agregada a favor y en contra: Cachon, Randall y Schmidt (2007) hallaron en datos mensuales de industrias de EE.UU. que «retail industries generally do not exhibit the effect, nor do most manufacturing industries» (cita literal tomada de F10, que cita las páginas 457 de F11); el efecto aparece sobre todo en el comercio mayorista; y es sensible a la estacionalidad: de 75 industrias, 61 muestran látigo al quitar la estacionalidad y solo 39 sin quitarla (cifras citadas por F10). [F10, F11]
- Evidencia a nivel de empresa: Bray y Mendelson (2012), 4.689 empresas públicas de EE.UU., 1974-2008: «about two-thirds of firms bullwhip»; el látigo medio y el mediano son 15,8 % y 6,7 % de la variabilidad total de la demanda; «From 1974–1994 to 1995–2008, our sample's mean bullwhip dropped by a third»; 35 % de las empresas no muestran látigo; la dispersión es grande: solo 24 % de los látigos de empresa están entre la mitad y el doble del promedio global. También señalan un posible sesgo de publicación en los estudios de caso. [F10, [L] del abstract y la introducción]
- Casos citados por F10 como ilustración (no leídos en origen): Hammond (1994) pastas, Lee et al. (1997) sopa, Fransoo y Wouters (2000), Lai (2005) y Wong et al. (2007). [F10]
- Reconciliación de las dos evidencias: no se contradicen. Cachon et al. miran la industria agregada, Bray y Mendelson miran la empresa; el propio Cachon et al., citado en F10, escribe que «it is possible that firms exhibit the bullwhip effect but the industry does not». [F10]

### Sin verificar (conocimiento previo, a confirmar)

- Forrester (1958), «Industrial Dynamics: A Major Breakthrough for Decision Makers», Harvard Business Review: origen de la idea (amplificación de la demanda en una cadena de cuatro eslabones con demoras). Sin leer.
- Sterman (1989), «Modeling Managerial Behavior: Misperceptions of Feedback in a Dynamic Decision Making Experiment», Management Science 35(3), 321-339: el juego de la cerveza; la explicación por el comportamiento de quien decide (subestima el inventario en camino), sin necesidad de las cuatro causas estructurales de Lee et al. La página de INFORMS dio 403: sin lectura.
- Remedios con nombre propio como CPFR (VICS): sin fuente leída.
- Pedir más chico y más seguido, y precios estables: están en F8 como contramedidas (órdenes pequeñas por EDI y EDLP); no se lee ahí «pedir más seguido» literal, así que no se pone entre comillas.

### Qué registra un sistema

Para detectar o medir el efecto hacen falta dos series por eslabón: ventas (salida) y pedidos de reposición (entrada), a la misma frecuencia, y la varianza o el coeficiente de variación de cada una. Para atacarlo: datos de venta compartidos con el proveedor, parámetros de reposición con el proveedor (VMI), reglas de pedido por calendario (citas de entrega) y el historial de promociones. Fuente: tabla 1 de F8; el resto es inferencia.

### Recurso canónico propuesto

Lee, Padmanabhan y Whang (1997): leer el abstract, la sección 3 (las cuatro causas) y la tabla 1 de causas y contramedidas, que además muestra la práctica de empresas concretas de la época. Para la evidencia: Bray y Mendelson (2012), introducción y abstract (el mejor estado de la discusión con Cachon et al.), y luego Cachon, Randall y Schmidt (2007).

## Huecos

1. S&OP: ninguna fuente leída. Es el hueco principal porque la nota es central. Faltan el ciclo de cinco pasos, quién decide, estrategias de nivelación y madurez. Leer Thomé et al. (2012) y la entrada de S&OP de ASCM.
2. DRP: ninguna fuente leída sobre la tabla y el cálculo. Faltan Martin (1983) y el diccionario de ASCM.
3. Competencias M4 y M5: sin lectura (403 de la editorial); queda por confirmar cuánto aprendizaje automático supera a los métodos de series de tiempo.
4. Fildes y Goodwin: sin lectura; hay que confirmar los números antes de afirmarlos.
5. Syntetos y Boylan 2005: sin lectura; hay que confirmar la corrección SBA y la clasificación de la demanda.
6. Señal de seguimiento, WAPE y FVA: sin fuente leída.
7. Forrester 1958 y Sterman 1989: sin lectura.
8. MIT OCW ESD.260 / 1.260: las URL probadas dieron 404; hay que encontrar la URL vigente del curso.
9. Libros de texto (Chopra y Meindl, Simchi-Levi et al., Silver, Pyke y Thomas): no se leyeron; sostendrían la jerarquía de planes, el empujar y tirar, la planificación agregada y la reposición multinivel.
10. Reaprovisionamiento por el proveedor (VMI) y CPFR: solo aparecen como contramedidas en F8.
11. Documentación de sistemas abiertos: no se leyó nada en esta ronda (agotada la búsqueda); por eso las secciones «Qué registra un sistema» se apoyan sobre todo en APQC y en inferencia.
12. Recencia: las fuentes verificadas son estables (conceptos de 1997-2012 y un libro abierto vigente). FPP3 no se consultó con fecha de edición; APQC es de 2024.

## Discrepancias con el árbol

- La división propuesta (entrada, pronóstico, error, S&OP, DRP, látigo) coincide con APQC 4.1 en lo esencial: 4.1.2 contiene pronóstico, consenso y medición de exactitud; 4.1.5 es el DRP. Se puede mantener.
- Posible ajuste: APQC trata «medir la exactitud del pronóstico» como parte de «Manage demand for products» (4.1.2.7), no como tema aparte. Mantener «error-de-pronostico» como nota propia es válido, pero conviene enlazarla desde pronostico-de-demanda como parte del mismo ciclo.
- APQC no tiene S&OP como proceso nombrado: S&OP viene de los cuerpos de certificación (ASCM, Oliver Wight) y de la bibliografía académica. La nota debe decir que es una práctica, no un proceso del marco.
- El látigo está en Planificación, pero sus remedios (VMI, compartir datos, pedir más chico y seguido) tocan Compras y Transporte; conviene enlazarlos en vez de explicarlos acá.
- Sugerencia menor: la demanda censurada (la venta no es la demanda) puede ser un apartado de pronostico-de-demanda, pero afecta también a Inventario (quiebres); enlazar.
