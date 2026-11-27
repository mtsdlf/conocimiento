---
resumen: >-
  Centralizar el stock es atender desde menos lugares la demanda que antes se atendía desde muchos, para que las variaciones de cada zona se compensen entre sí y haga falta menos stock de seguridad con el mismo nivel de servicio del stock. La ley de la raíz cuadrada estima ese ahorro, pero solo vale bajo supuestos que la mayoría de las empresas no cumplen.
estado: borrador
estabilidad: estable
fuentes:
  - "Caplice, C. (MIT CTL), Transportation Management: Network & Hubs, ESD.260 Logistics Systems, archivo lect25, diciembre de 2006, diapositivas 28 a 33 («Location Pooling» y «Lead Time Pooling», esta última adaptada de Cachon y Terwiesch, 2005): https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/421e474d22fae64f415aea445a34a254_lect25.pdf"
  - "Caplice, C. (MIT CTL), ESD.260 Logistics Systems, archivo lect17, diapositiva 11: https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/"
  - "Chopra, S., Designing the Distribution Network in a Supply Chain, Kellogg School of Management, Northwestern University (PDF de noviembre de 2002), secciones 2.1 y 4: https://transportation.tech.northwestern.edu/docs/research/core-topics/logistics-and-supply-chain-management/Chopra_DistributionSupplyChain.pdf"
  - "Maister, D. H. (1976), Centralisation of Inventories and the «Square Root Law», International Journal of Physical Distribution 6(3):124-134 (según el resumen): https://doi.org/10.1108/eb014366"
  - "Das, C. (1978), sobre la ley de la raíz cuadrada de Maister (según el resultado del buscador): https://emerald.com/insight/content/doi/10.1108/eb014428/full/html"
  - "Eppen, G. D. (1979), Effects of Centralization on Expected Costs in a Multi-Location Newsboy Problem, Management Science 25(5):498-501 (según el resumen): https://doi.org/10.1287/mnsc.25.5.498"
  - "Oeser, G. y Romano, P. (2016), International Journal of Production Research 54(8):2298-2319 (según el resumen): https://ideas.repec.org/a/taf/tprsxx/v54y2016i8p2298-2319.html"
  - "Oeser, G. (2019), International Journal of Retail & Distribution Management 47(3):292-310 (según el resumen): https://doi.org/10.1108/ijrdm-05-2017-0108"
  - "Bimpikis, K. y Markakis, M. G. (2016), Inventory Pooling Under Heavy-Tailed Demand, Management Science 62(6):1800-1813 (según el resumen): https://ideas.repec.org/a/inm/ormnsc/v62y2016i6p1800-1813.html"
  - "Fleischmann, B. (2016), OR Spectrum 38(4) (según el resultado del buscador): https://ideas.repec.org/a/spr/orspec/v38y2016i4d10.1007_s00291-016-0442-2.html"
  - "Cadena-de-suministro-y-logistica/.investigacion/red-de-distribucion.md (sección 3)"
  - "Cadena-de-suministro-y-logistica/.investigacion/red-de-distribucion-2.md (sección 3) y fundamentos-y-contraria-2.md (sección 7)"
aliases: [centralización del stock, centralización de inventarios, agrupar el riesgo, agrupación del riesgo, risk pooling, inventory pooling, location pooling, agrupación por ubicación, lead time pooling, ley de la raíz cuadrada, square root law, SRL, stock centralizado, stock descentralizado]
creado: 2026-11-27
revisado:
---

# Centralización del stock

Centralizar el stock es atender desde menos lugares la demanda que antes se atendía desde muchos, para que las variaciones de cada zona se compensen entre sí y haga falta menos stock de seguridad con el mismo nivel de servicio del stock. La ley de la raíz cuadrada estima ese ahorro, pero solo vale bajo supuestos que la mayoría de las empresas no cumplen.

Es la curva de inventario del [diseño de la red](diseno-de-la-red.md): explica por qué el stock total sube cuando se suman depósitos. El cálculo del colchón de cada lugar es el del [stock de seguridad](../../Inventario-y-depositos/Reposicion/stock-de-seguridad.md), de Inventario; acá se mira qué pasa con la suma cuando cambia la cantidad de lugares.

## Por qué agrupar baja el colchón

Cuando cada zona tiene su propio stock, cada una necesita un colchón para su propia variación. Si las demandas no se mueven juntas, un día flojo en una zona compensa uno fuerte en otra, y un solo stock común necesita menos colchón que la suma de los separados. Eppen (1979), según el resumen de su artículo, lo demostró para varias ubicaciones con demanda normal y costos iguales: los costos esperados de mantener y de faltar son mayores descentralizados que centralizados, y el ahorro depende de la correlación entre las demandas.

Chopra lo usa como argumento a favor de dos diseños de la [red de distribución](red-de-distribucion.md). Del envío directo dice que «A manufacturer can aggregate demand and provide a high level of product availability with lower levels of inventory than individual retailers»; del distribuidor, que «aggregates safety inventory rather than disaggregating at each retailer».

## La ley de la raíz cuadrada

Maister (1976) la enunció así: «the total inventory in a system is proportional to the square root of the number of locations at which a product is stocked». Pasar de n depósitos iguales a uno solo divide el stock de seguridad total por √n; pasar de uno a n lo multiplica por √n. Según el resumen de Eppen, con demandas idénticas e independientes el costo crece con la raíz cuadrada de la cantidad de demandas que se agrupan.

Maister quiso extenderla también al stock de ciclo, y Das (1978) cuestionó esa extensión (según el resultado del buscador).

## El ejemplo del MIT

Las clases del MIT (Caplice, archivo lect25, diapositiva 28) plantean este caso:

- «Region has 3 sales/delivery teams»
- «Each team has its own inventory site»
- «Daily demand ~N(15, 4) within each territory»
- «Lead time to each territory site = 2 days»
- «Cycle service level set at 99.9%»

Y preguntan: «How much safety stock should be in each territory? What if they pool to a common site?».

La diapositiva 29 grafica los días de cobertura contra la cantidad de puntos de stock, de 1 a 10, y concluye: «Note declining marginal benefit of pooling. Going from 1 to 3 – reduced SS by 42%. Going from 7 to 9 – reduced SS by 12%». Las dos cifras son las de la raíz cuadrada: 1 − 1/√3 = 42,3 % y 1 − √7/√9 = 11,8 % (cuenta de la base).

La fuente no publica los valores en unidades. Con la fórmula de [stock de seguridad](../../Inventario-y-depositos/Reposicion/stock-de-seguridad.md) y suponiendo que el 4 es el desvío diario, quedan así (cuenta de la base, ilustrativa):

| Escenario | Desvío en el plazo de 2 días | Stock de seguridad (k = 3,09) |
|---|---|---|
| Cada sitio por separado | 4 × √2 ≈ 5,7 | ≈ 17,5 por sitio |
| Los tres sitios separados | | ≈ 52,4 en total |
| Un sitio común (demanda de 45 por día, varianza triple) | 4 × √6 ≈ 9,8 | ≈ 30,3 |

La reducción, 1 − 30,3/52,4 ≈ 42 %, coincide con la de la diapositiva. Si el 4 fuera la varianza, el porcentaje sería el mismo y las unidades cambiarían.

Lo que muestra el ejemplo es el rendimiento decreciente: juntar los primeros sitios ahorra mucho; juntar el séptimo con el noveno, poco.

## Lo que se paga por centralizar

La diapositiva 30 del MIT agrega el stock de ciclo. Con n sitios que piden cada uno su [lote económico](../../Inventario-y-depositos/Reposicion/lote-economico.md), «qi* = √(2 A Di / v r) = √(2 A D / (v r n))», y el costo total de reponer queda en «TRC* = √(2 n D A v r)»: √n veces el de un sitio común. Separar también encarece los pedidos. La diapositiva deja abierto qué pasa con la reposición del centro común: «Impact on replenishment to the DC location. Other impacts?».

Del otro lado, Chopra marca lo que se pierde. El tiempo de respuesta: «Response times tend to be large when drop shipping is used ... shipping distances are on average longer from the manufacturer's centralized site». Y el transporte de salida: «Transportation costs are high with drop shipping because the average outbound distance to the end consumer is large and package carriers must be used». Esas son las otras curvas del [diseño de la red](diseno-de-la-red.md#la-curva-de-costo-total).

## Qué artículos conviene centralizar

Chopra da el criterio: «The benefits from centralization are highest for high value, low volume items with unpredictable demand. The inventory benefits of aggregation are small for items with predictable demand and low value». Por eso las redes mezclan diseños: lo que rota poco y es caro va a un solo lugar, y lo que rota mucho y es barato se tiene cerca del cliente. La [clasificación ABC](../../Inventario-y-depositos/Reposicion/clasificacion-abc.md) con XYZ, que ordena por valor y por variabilidad, es una forma de hacer esa separación (inferencia de la base).

## Agrupar en el plazo y no en el lugar

El stock puede quedar cerca del cliente y aun así agruparse. El MIT (diapositivas 31 a 33, adaptadas de Cachon y Terwiesch) separa tres incertidumbres: «Total demand uncertainty», «Allocation demand uncertainty» y «Product mix uncertainty». Un centro de distribución intermedio protege contra la segunda: «Consolidated Distribution: Keep inventory near customers; Hedge against allocation uncertainty». Se decide tarde a qué local va cada unidad.

El caso de la clase: un proveedor que abastece directo a 100 tiendas, con plazo de 4 semanas, revisión cada 4 semanas, «Weekly demand in each store is iid ~N(75, 20)» y «IFR = 99.5%». La alternativa pone un centro regional: 4 semanas del proveedor al centro y 1 del centro a las tiendas. La diapositiva no da el resultado; pregunta «What is the safety stock on hand in the system?» y «Who owns the pipeline inventory?». Cuánto mandar desde el centro a cada tienda es la [planificación de la distribución](../Planificacion/planificacion-de-la-distribucion.md).

## Dónde falla la ley

La ley es un resultado de modelo, y la evidencia dice que pocas empresas cumplen el modelo.

> [!IMPORTANT] Cuánto vale la ley de la raíz cuadrada en la práctica está discutido.
> - **A favor**: Eppen la deduce para demandas normales, idénticas e independientes, y las clases del MIT la usan como regla de cálculo.
> - **En contra, con datos**: Oeser y Romano (2016) derivan las condiciones para el stock de ciclo, el de seguridad y el total, y las prueban con cuatro casos y una encuesta a 280 empresas alemanas. Según su resumen: «Most companies do not fulfil the assumptions of the SRL and therefore cannot apply it with accurate results». Las comerciales cumplen más supuestos que las manufactureras, los minoristas más que los mayoristas, y los supuestos se ajustan mejor al stock de ciclo que al de seguridad, al revés de como se la suele usar.
> - **En contra, midiendo el error**: Oeser (2019), según su resumen, comparó la estimación de la ley con lo que pasó en 26 casos de empresas que redujeron depósitos. El error medio para el inventario total fue del 27,85 %, con mucha variación entre casos, y la ley «seems to mostly overestimate inventory savings from centralisation».
> - **En contra, por la forma de la demanda**: Bimpikis y Markakis (2016), según su resumen, muestran que con demanda de cola pesada (parámetro alfa entre 1 y 2) el beneficio de agrupar crece más lento que la raíz cuadrada.
> - **En contra, por el transporte**: Fleischmann (2016), según el resultado del buscador, encuentra que si los depósitos se reponen en camión completo con un nivel de servicio dado, la ley «is not valid».

Los supuestos que se rompen más seguido, a juicio de la base: demandas correlacionadas entre zonas (una promoción nacional o el clima mueven a todas juntas, y el ahorro se achica), zonas de tamaños muy distintos, y plazos que cambian al centralizar. Eppen ya pone la correlación como condición; la fórmula con correlación no se leyó.

Las clases del MIT agregan, para redes de varios escalones, que el control descentralizado con lote y punto de pedido puede «Create and amplify "lumpy" demand» y llevar a «mal-distribution of available stock, hoarding of stock, and unnecessary stock outs» (archivo lect17). Es uno de los motivos para planificar la reposición entre escalones en vez de dejar que cada depósito pida solo.

> [!NOTE] Sin fuente todavía: la crítica de Evers y Beier a la ley de la raíz cuadrada (no se encontró la obra), la fórmula con demandas correlacionadas y un ejemplo publicado con valores absolutos.

## Qué guarda un sistema para calcularlo

La agrupación no es un objeto del sistema: es una consecuencia de la relación de abastecimiento, que dice qué ubicación atiende a cuál (ver [red de distribución](red-de-distribucion.md#qué-tiene-que-poder-representar-un-sistema-de-la-red)). Para recalcular el colchón cuando esa relación cambia, el ejemplo del MIT necesita, por ubicación y artículo:

- la media y el desvío de la demanda que atiende, en la misma unidad de tiempo;
- el plazo de reposición desde quien la abastece;
- el nivel de servicio del stock buscado (en el ejemplo, por ciclo).

Si dos zonas pasan a abastecerse de un mismo depósito, el sistema tiene que sumar sus demandas antes de calcular, y no sumar los colchones (inferencia de la base). Guardar el historial de demanda por zona, y no solo por depósito, permite simular la centralización antes de hacerla.

Para leer más: Caplice, archivo lect25, diapositivas 28 a 30, tiene el ejemplo y el rendimiento decreciente; Oeser y Romano (2016), la lista de supuestos y cuántas empresas los cumplen.
