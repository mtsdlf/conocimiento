---
resumen: >-
  Lo transversal del tema Inventario y depósitos: de dónde vienen sus ideas, las escuelas que discuten si conviene tener stock (colchón, desperdicio y DDMRP), la evidencia contra las fórmulas y los supuestos más repetidos, y dónde se produce el saber del campo.
estado: borrador
estabilidad: estable
fuentes:
  - "Harris (1913), How many parts to make at once, Factory, The Magazine of Management; reimpreso en Operations Research 38(6), 947-950, 1990: https://doi.org/10.1287/opre.38.6.947 (según el resumen)"
  - "Ford Whitman Harris and the Economic Order Quantity Model, Operations Research 38(6), 937-946, 1990: https://doi.org/10.1287/opre.38.6.937 (según el resumen)"
  - "Wikipedia, Economic order quantity: https://en.wikipedia.org/wiki/Economic_order_quantity (secundaria)"
  - "Wikipedia, Kardex Group: https://en.wikipedia.org/wiki/Kardex_Group (secundaria; solo para el origen del nombre)"
  - "Wikipedia, Material requirements planning: https://en.wikipedia.org/wiki/Material_requirements_planning (secundaria)"
  - "Wikipedia, Muda (Japanese term): https://en.wikipedia.org/wiki/Muda_(Japanese_term) (secundaria)"
  - "Hopp y Spearman (2004), To Pull or Not to Pull: What Is the Question?, Manufacturing & Service Operations Management 6(2): https://doi.org/10.1287/msom.1030.0028 (según el resumen)"
  - "Demand Driven Institute, DDMRP: https://www.demanddriveninstitute.com/ddmrp (la descripción de quien difunde el método)"
  - "DeHoratius y Raman (2008), Inventory Record Inaccuracy: An Empirical Analysis, Management Science 54(4), 627-641: https://doi.org/10.1287/mnsc.1070.0789 (según el resumen)"
  - "Eppen y Martin (1988), Determining Safety Stock in the Presence of Stochastic Lead Time and Demand, Management Science 34(11): https://doi.org/10.1287/mnsc.34.11.1380 (según el resumen)"
  - "Chopra, Reinhardt y Dada (2004), The Effect of Lead Time Uncertainty on Safety Stocks, Decision Sciences 35(1): https://doi.org/10.1111/j.1540-5414.2004.02332.x (según el resumen)"
  - "Teunter, Babai y Syntetos (2010), ABC Classification: Service Levels and Inventory Costs, Production and Operations Management 19(3): https://doi.org/10.1111/j.1937-5956.2009.01098.x (según el resumen)"
  - "Bartholdi y Hackman, Warehouse & Distribution Science, versión 0.98.1: https://www.warehouse-science.com/"
  - "Inventario-y-depositos/.investigacion/fundamentos-y-contraria.md (2026-11-27)"
aliases: [fundamentos de inventario, historia del inventario, escuelas de inventario, lean e inventario, DDMRP, mitos del inventario]
creado: 2026-11-27
revisado:
---

# Fundamentos de inventario y depósitos

Lo transversal del tema Inventario y depósitos: de dónde vienen sus ideas, las escuelas que discuten si conviene tener stock (colchón, desperdicio y DDMRP), la evidencia contra las fórmulas y los supuestos más repetidos, y dónde se produce el saber del campo.

## De la ficha de stock al sistema de depósito

La teoría de inventarios arranca con una pregunta de fábrica. En 1913, Ford Whitman Harris publicó «How many parts to make at once»: según el resumen de su reimpresión, el costo del capital inmovilizado limita cuántas piezas conviene hacer por tanda, y el costo de preparar la máquina fija el otro extremo. De ahí sale el [lote económico](../Reposicion/lote-economico.md). El trabajo pasó inadvertido hasta que se lo redescubrió en 1988. Por eso circuló durante décadas atribuido a R. H. Wilson, que lo difundió en 1934 en la *Harvard Business Review* (este último dato tiene una sola fuente secundaria).

Antes de las computadoras, la cantidad de cada artículo se llevaba en fichas, una por artículo, con las entradas, las salidas y el saldo: el kardex de la contabilidad latinoamericana (esta descripción es de la base, sin fuente leída). El nombre viene de una marca de fichas visibles de principios del siglo XX (según una fuente secundaria sobre la empresa); no se encontró una fuente que diga cuándo se empezó a usar para el stock. La lógica de la ficha es la misma que la del [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md).

En los años sesenta llegó el MRP. Según una fuente secundaria, Joseph Orlicky lo desarrolló en 1964 y su libro es de 1975; antes de él, lo común eran los métodos de [punto de pedido](../Reposicion/punto-de-pedido.md). El MRP calcula los materiales a partir del plan de producción, y en esta base es del tema Producción (todavía no armado). Los sistemas de gestión de depósitos (WMS) vinieron después; no se encontró una fuente fechada de su origen.

## Tres escuelas sobre para qué tener stock

| Escuela | Qué es el stock | Qué propone | Quién la sostiene |
|---|---|---|---|
| Colchón (teoría clásica) | Una protección contra la incertidumbre de la demanda y del plazo, con funciones distintas (ciclo, seguridad, anticipación, tránsito, desacople) | Calcular cuánto conviene tener equilibrando el costo de pedir, el de mantener y el de quedarse sin stock: [lote económico](../Reposicion/lote-economico.md), [punto de pedido](../Reposicion/punto-de-pedido.md), [stock de seguridad](../Reposicion/stock-de-seguridad.md) | Los libros de texto de operaciones (Silver, Pyke y Thomas; Nahmias) y los cuerpos de certificación de ASCM |
| Desperdicio (lean, justo a tiempo) | Uno de los siete desperdicios de Ohno: capital inmovilizado que todavía no genera ingreso y que esconde problemas | Bajar el stock para que los problemas salgan a la luz, y achicar el costo de preparar en vez de tomarlo como dato (lectura de la base: la fuente leída solo lista el stock como desperdicio) | El sistema de producción de Toyota, según la difusión de Ohno (1988) |
| DDMRP | Un amortiguador que se ubica solo en algunos puntos de la cadena | Poner stock en puntos de desacople elegidos y dimensionarlo según la demanda real; su lema es «Position, Protect, Pull and Adapt» | Carol Ptak y Chad Smith, según el instituto que difunde el método |

Las dos primeras discuten menos de lo que parece. Hopp y Spearman (2004), según el resumen de su artículo, definen lean como un sistema «fundamentally about minimizing the cost of buffering variability»: lean no elimina el colchón, busca que cueste menos. Las dos escuelas responden a la misma variabilidad, una calculando el colchón y la otra atacando sus causas.

DDMRP se presenta como un método de planificación y ejecución en varios niveles. La única fuente leída es la de quien lo difunde, sin fórmulas de los amortiguadores ni comparación independiente; se nombra como escuela y no como evidencia.

> [!NOTE] Sin fuente todavía: un estudio independiente que compare DDMRP con el MRP o con las políticas clásicas.

## Lo que la evidencia discute de las ideas más repetidas

| Idea | Qué dice la evidencia | Fuente |
|---|---|---|
| «Si el sistema dice que hay 10, hay 10» | En 37 tiendas de un minorista, el 65 % de los registros de stock no coincidía con lo que había; la categoría de producto explica más que la tienda | DeHoratius y Raman (2008), según el resumen; un solo minorista |
| «La fórmula del stock de seguridad da el número» | Supone demanda normal, independiente y estable; una fuente secundaria lo resume así: «No universal formula exists for safety stock, and application of the one above can cause serious damage.» Eppen y Martin (1988) mostraron que un procedimiento estándar podía dar resultados lejos del buscado | Wikipedia, Safety stock; Eppen y Martin (1988), según el resumen |
| «Achicar la variabilidad del plazo siempre baja el stock» | Según el resumen de Chopra, Reinhardt y Dada (2004), depende del nivel de servicio; a veces conviene acortar el plazo en lugar de hacerlo más parejo | Chopra y otros (2004), según el resumen |
| «Clasificar por valor alcanza para fijar el servicio de cada clase» | En tres conjuntos de datos reales, ordenar por valor o por volumen con un nivel de servicio fijo por clase dio costos lejos del óptimo | Teunter, Babai y Syntetos (2010), según el resumen |
| «Lean es no tener stock» | Lean busca bajar el costo de amortiguar la variabilidad | Hopp y Spearman (2004), según el resumen |
| «El lote económico lo inventó Wilson» | Es de Harris, 1913; Wilson lo difundió | Harris (1913) y su reimpresión de 1990 |

El caso de la inexactitud pesa sobre todo el tema: [disponible para prometer](../Existencias/disponible-para-prometer.md), [reserva](../Operacion-del-deposito/reserva.md) y [punto de pedido](../Reposicion/punto-de-pedido.md) calculan sobre un número que probablemente está mal. Qué hacer con eso está en [control del stock](../Control-del-stock/control-del-stock.md). Ninguno de los artículos de esta tabla se leyó entero.

## Dónde se produce el saber del campo

- **Investigación de operaciones**: *Management Science*, *Operations Research*, *Manufacturing & Service Operations Management*, *Production and Operations Management*. Ahí están los modelos de reposición y la evidencia sobre la exactitud de los registros.
- **Libros de texto**: Silver, Pyke y Thomas, *Inventory and Production Management in Supply Chains* (4.ª ed.), y Nahmias, *Production and Operations Analysis*, para la reposición; Bartholdi y Hackman, *Warehouse & Distribution Science*, de descarga libre, para la operación del depósito (capítulo 3 y secciones 2.4 y 4.2). Solo el último se leyó para este tema.
- **Cuerpos de certificación**: ASCM (ex APICS), con su diccionario y el programa CPIM; definen el disponible para prometer y el vocabulario de la planificación.
- **Marcos de procesos**: el Process Classification Framework de APQC, proceso 4.4.3 (Operate warehousing), que reparte el depósito en recibir, guardar, controlar la exactitud, preparar y transferir.
- **Documentación de sistemas abiertos y de proveedores**: la mejor fuente sobre qué datos y estados lleva cada objeto; sirve como evidencia de que un patrón es común, no como norma.
- **Divulgación de práctica**: guías de consultoras y blogs del rubro, útiles para la práctica y flojos en cifras.

## Lo que hay en Fundamentos

- [Glosario de inventario y depósitos](glosario-de-inventario-y-depositos.md): los términos del tema con su nombre en inglés y la nota donde viven.
