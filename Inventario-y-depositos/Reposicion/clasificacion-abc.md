---
resumen: >-
  La clasificación ABC ordena los artículos por su valor anual de consumo y los parte en tres clases, para darles control fino a los pocos que pesan mucho (A) y control simple a los muchos que pesan poco (C). Decide qué política de reposición y qué frecuencia de conteo lleva cada artículo; sus cortes no son fijos, y XYZ le suma una segunda mirada por variabilidad de la demanda.
estado: borrador
estabilidad: estable
fuentes:
  - "Wikipedia, ABC analysis (Pareto, clases, ejemplos de cortes, método en cinco pasos): https://en.wikipedia.org/wiki/ABC_analysis"
  - "Caplice, C. (MIT CTL), Inventory Management: Probabilistic Demand, ESD.260 lección 11, octubre de 2006, diapositivas 4 y 8: https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/8b53c45fd26ffff706d815131e8d177e_lect11.pdf"
  - "Wikipedia, Cycle counting (ABC para la frecuencia de conteo y sus desventajas): https://en.wikipedia.org/wiki/Cycle_counting"
  - "Teunter, Babai y Syntetos (2010), ABC Classification: Service Levels and Inventory Costs, Production and Operations Management 19(3):343-352 (según el resumen): https://doi.org/10.1111/j.1937-5956.2009.01098.x"
  - "DeHoratius y Raman (2008), Inventory Record Inaccuracy: An Empirical Analysis, Management Science 54(4):627-641 (según el resumen): https://doi.org/10.1287/mnsc.1070.0789"
  - "Mecalux Interlake, ABC XYZ analysis (umbrales XYZ; solo por el buscador): https://www.interlakemecalux.com/blog/abc-xyz"
  - "SCM Dojo, guía ABC-XYZ (umbrales XYZ; solo por el buscador): https://www.scmdojo.com/blog/abc-xyz-analysis-complete-guide/"
  - "Material de curso IEOR sobre XYZ (umbrales; solo por el buscador): https://neoprimate.github.io/IEOR/supply-chain/classification/xyz/index.html"
  - "Inventario-y-depositos/.investigacion/reposicion.md (sección 5)"
  - "Inventario-y-depositos/.investigacion/fundamentos-y-contraria.md (sección 4.4)"
aliases: [clasificación ABC, análisis ABC, ABC analysis, ABC classification, curva ABC, ley de Pareto, Pareto, 80-20, clasificación XYZ, análisis XYZ, ABC-XYZ, segmentación de artículos, SKU segmentation]
creado: 2026-11-27
revisado:
---

# Clasificación ABC

La clasificación ABC ordena los artículos por su valor anual de consumo y los parte en tres clases, para darles control fino a los pocos que pesan mucho (A) y control simple a los muchos que pesan poco (C). Decide qué política de reposición y qué frecuencia de conteo lleva cada artículo; sus cortes no son fijos, y XYZ le suma una segunda mirada por variabilidad de la demanda.

Dentro de [reposición](reposicion.md), dice a qué artículos dedicarles la política más fina de [punto de pedido](punto-de-pedido.md) y de [stock de seguridad](stock-de-seguridad.md). Fuera de ella, fija cada cuánto se cuenta cada artículo en el [conteo cíclico](../Control-del-stock/conteo-ciclico.md). Vive acá porque nace como política de atención; el conteo la usa.

## Cómo se arma

«The ABC concept is based on Pareto's law»: pocos artículos concentran la mayor parte del valor. El método, en cinco pasos:

1. Calcular el valor anual de consumo de cada artículo: unidades al año por costo unitario.
2. Ordenar los artículos de mayor a menor valor.
3. Acumular los valores.
4. Pasar el acumulado a porcentaje del total.
5. Graficar y cortar las clases.

El corte no tiene regla: «There are no fixed thresholds for each class». Wikipedia da dos ejemplos de reparto:

| Clase | Ejemplo 1: artículos | Ejemplo 1: valor | Ejemplo 2: artículos | Ejemplo 2: valor |
|---|---|---|---|---|
| A | 20 % | ~70 % | 10 % | 66,6 % |
| B | 30 % | ~25 % | 20 % | 23,3 % |
| C | 50 % | ~5 % | 70 % | 10,1 % |

## Qué cambia según la clase

Cada clase recibe un control distinto. Según Wikipedia, la A lleva «very tight control and accurate records»; la B, «less tightly controlled and with moderate records»; la C, «the simplest controls possible and minimal records». El MIT lo dice parecido: la A «Require the most managerial attention and review», y para la C «Control systems should be as simple as possible».

En reposición, eso se traduce en la política. El MIT da como regla práctica (s, S) o (R, s, S) para la A, (s, Q) o (R, S) para la B, y una revisión manual parecida a (R, S) para la C; la tabla está en [punto de pedido](punto-de-pedido.md).

En el conteo, se traduce en la frecuencia: los A se cuentan más seguido que los C. Wikipedia lo describe como práctica común: «Most cycle counting applications use ABC analysis, which sorts items into count frequencies using the Pareto method». Las frecuencias y las tolerancias de cada clase están en [conteo cíclico](../Control-del-stock/conteo-ciclico.md).

## XYZ: la variabilidad de la demanda

ABC mira cuánto vale un artículo; no mira cuán previsible es. XYZ lo agrega, con el coeficiente de variación de la demanda (desvío dividido por media): X es la demanda estable, Y la que varía algo, Z la errática. Cruzadas, las dos clasificaciones separan un A estable (fácil de reponer con fórmula) de un A errático (que pide seguimiento). Esto último es lectura de la base.

Los cortes de XYZ discrepan entre fuentes y ninguna es un libro de texto:

| Fuente | X | Y | Z |
|---|---|---|---|
| Un fabricante de estanterías | ≤ 10 % | 10-25 % | > 25 % |
| Un material de curso | < 0,5 | < 1,0 | ≥ 1,0 |
| Una guía de cadena de suministro | < 0,5 | 0,5-1,0 | sin dato |

El fabricante aclara que los cortes se adaptan a cada empresa. Las tres se leyeron solo por el resumen del buscador.

> [!NOTE] Sin fuente todavía: XYZ en un texto de libro o de un organismo del campo. La página de ASCM sobre XYZ vino vacía.

## Dónde falla la clasificación por valor

El MIT lo advierte en la misma diapositiva: «But – these are arbitrary classifications». La crítica tiene evidencia:

- **Para el nivel de servicio.** Teunter, Babai y Syntetos (2010), según su resumen, probaron con tres conjuntos de datos reales que ordenar por valor o por volumen y fijar un nivel de servicio por clase da costos lejos del óptimo. Proponen otro criterio, que puede incluir la criticidad del artículo.
- **Para el conteo.** Wikipedia lista desventajas: por valor se ignoran artículos baratos que pueden frenar una línea, y por uso se sesga contra lo caro. DeHoratius y Raman, según su resumen, encontraron que la categoría de producto explica la inexactitud del registro más que la tienda. Que eso apunte a contar según la propensión al error y no solo según el valor es inferencia de la base; Teunter y sus coautores no hablan del conteo.

En la práctica (criterio de la base), ABC es un buen primer corte y un mal criterio único. Un tornillo barato que para una línea de producción merece trato de A aunque su valor sea de C.

Para leer más: la entrada de Wikipedia sobre ABC analysis tiene el método y los ejemplos; para la crítica, el artículo de Teunter, Babai y Syntetos (2010).
