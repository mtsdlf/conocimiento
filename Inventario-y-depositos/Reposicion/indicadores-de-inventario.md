---
resumen: >-
  Los indicadores de inventario miden si el stock cumple su función sin costar de más: cuántas veces rota en el año, cuántos días de venta cubre, qué parte de la demanda se atiende a tiempo y cuánto coincide el registro con el estante. Se calculan sobre el costo de lo vendido y el valor promedio del stock, y varios tienen definiciones que cambian según la fuente.
estado: borrador
estabilidad: semi
fuentes:
  - "Hammond y Western Technical College, Operations Management, §6.8 Measuring Supply Chain Performance (CC BY 4.0; leído por resumen): https://biz.libretexts.org/Courses/Western_Technical_College/Operations_Management_(Hammond)/06%3A_Supply_Chain_and_Inventory_Management/6.08%3A_Measuring_Supply_Chain_Performance"
  - "Caplice, C. (MIT CTL), Inventory Management: Probabilistic Demand, ESD.260 lección 11, octubre de 2006, diapositivas 10-24: https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/8b53c45fd26ffff706d815131e8d177e_lect11.pdf"
  - "APQC, Process Classification Framework 7.4, 4.4.3.5 «Track inventory accuracy»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "DeHoratius y Raman (2008), Inventory Record Inaccuracy: An Empirical Analysis, Management Science 54(4):627-641 (según el resumen): https://doi.org/10.1287/mnsc.1070.0789"
  - "Inventario-y-depositos/.investigacion/reposicion.md (sección 6)"
aliases: [indicadores de inventario, KPI de inventario, inventory KPIs, rotación de inventario, rotación de stock, inventory turnover, inventory turns, días de inventario, días de stock, days of supply, days of inventory, DIO, cobertura, cobertura de stock, nivel de servicio, exactitud de inventario, inventory accuracy, obsolescencia, stock obsoleto]
creado: 2026-11-27
revisado:
---

# Indicadores de inventario

Los indicadores de inventario miden si el stock cumple su función sin costar de más: cuántas veces rota en el año, cuántos días de venta cubre, qué parte de la demanda se atiende a tiempo y cuánto coincide el registro con el estante. Se calculan sobre el costo de lo vendido y el valor promedio del stock, y varios tienen definiciones que cambian según la fuente.

Son la vuelta de control de [reposición](reposicion.md): la política fija un [punto de pedido](punto-de-pedido.md), un [lote](lote-economico.md) y un [stock de seguridad](stock-de-seguridad.md), y los indicadores dicen después qué pasó. Unos miden el costo del stock (rotación, días), otros el servicio (nivel de servicio) y otro la confianza en el número (exactitud).

## Los indicadores y sus fórmulas

| Indicador | Qué mide | Fórmula | Fuente |
|---|---|---|---|
| Rotación | cuántas veces se renueva el stock en el año | costo de lo vendido / valor promedio del stock | libro abierto de operaciones |
| Días de inventario | cuántos días de costo de lo vendido hay guardados | valor promedio del stock / costo de lo vendido anual × 365 | ídem |
| Nivel de servicio | qué parte de los ciclos o de la demanda se atiende sin faltar | CSL o fill rate | clases del MIT |
| Exactitud | cuánto coincide el registro con el estante | sin fuente | APQC solo nombra la tarea |
| Cobertura | cuántos días de demanda futura cubre el stock | sin fuente | |
| Obsolescencia | cuánto stock ya no se va a vender | sin fuente | |

## Rotación y días de inventario

Según el resumen de la fuente, la rotación es, literal: «cost of goods sold divided by average aggregate inventory value». Los ejemplos de la fuente: 17.550.000 / 1.650.000 = 10,64 vueltas al año, y 16.255.000 / 1.763.350 = 9,22.

Los días de inventario, también según el resumen: «average aggregate inventory value divided by annual cost of goods sold, the sum of which is multiplied by 365». El ejemplo: 3.025.600 / 45.000.000 × 365 = 24,54 días.

Las dos son la misma información dada vuelta: días = 365 / rotación. Una rotación de 10,64 equivale a unos 34 días. La equivalencia y la cuenta son de la base; los ejemplos de la fuente no encajan entre sí (inferencia de la base: son de empresas distintas).

Las dos van al costo, no al precio de venta: el numerador es el [costo de lo vendido](../../Contabilidad/Operaciones/costo-de-lo-vendido.md) y el stock se valúa al costo, con el método que fija Contabilidad. Mezclar ventas a precio con stock a costo infla la rotación por el margen (inferencia de la base). Cambiar de método de valuación también mueve el indicador sin que cambie una sola unidad.

Una rotación alta no es buena por sí sola. Puede venir de un stock tan bajo que se falta seguido, y por eso se lee junto con el nivel de servicio (criterio de la base).

## Nivel de servicio

El nivel de servicio tiene dos definiciones de uso corriente, y el MIT avisa que «Definitions in practice are fuzzy». El nivel de servicio por ciclo (CSL) es la probabilidad de no faltar en un ciclo de reposición; el fill rate es la «Fraction of demand filled from IOH». Para el mismo stock, el fill rate suele dar un porcentaje mucho más alto. Las definiciones literales y la tabla que lo muestra están en [stock de seguridad](stock-de-seguridad.md).

Medido después, el nivel de servicio real es el que dice si el stock de seguridad alcanza. Un tablero que lo muestra tiene que decir cuál de los dos es (criterio de la base).

## Exactitud del registro

APQC 7.4 tiene una tarea propia, 4.4.3.5 «Track inventory accuracy». DeHoratius y Raman midieron la inexactitud en un minorista y encontraron inexacto el 65 % de los registros (según el resumen). Es el indicador del que dependen los demás: si el registro miente, la rotación y la cobertura se calculan sobre un número falso. Cómo se cuenta y se corrige está en [control del stock](../Control-del-stock/control-del-stock.md) y [conteo cíclico](../Control-del-stock/conteo-ciclico.md).

> [!NOTE] Sin fuente todavía: la fórmula de la exactitud de registros (por artículo, por valor, con o sin tolerancia), la cobertura medida sobre la demanda futura y la obsolescencia. Tampoco se leyó de primera mano cómo define SCOR los días de inventario: según fuentes secundarias, hay quien la calcula sobre el costo de lo vendido y quien sobre la demanda pronosticada.

## Dónde discrepan las definiciones

Los días de inventario de este tema se calculan hacia atrás, sobre el costo de lo vendido del año. La cobertura se calcula hacia adelante, sobre la demanda que se espera. Con demanda estable dan parecido; con estacionalidad, no: antes de la temporada alta, el stock parece excesivo mirando atrás y escaso mirando adelante. La distinción es de la base, y es la razón por la que un tablero tiene que decir cuál de las dos muestra.
