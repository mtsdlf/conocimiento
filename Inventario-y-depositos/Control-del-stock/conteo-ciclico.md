---
resumen: >-
  El conteo cíclico cuenta una parte chica del stock por vez, según un calendario fijo, para que todo el depósito se cuente a lo largo del año sin frenar la operación. Reemplaza o complementa el inventario físico anual, y su decisión central es qué contar más seguido: por clase de artículo o por ubicación.
estado: vigente
estabilidad: semi
fuentes:
  - "Wikipedia, Cycle count: https://en.wikipedia.org/wiki/Cycle_count (según su resumen)"
  - "Wikipedia, Cycle counting (ventajas y desventajas del ABC; cita a Muller, Essentials of Inventory Management, AMACOM, no leído): https://en.wikipedia.org/wiki/Cycle_counting"
  - "Odoo 17, Cycle counts: https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/cycle_counts.html (según su resumen)"
  - "ERPNext, Stock Reconciliation: https://docs.frappe.io/erpnext/user/manual/en/stock-reconciliation (según su resumen)"
  - "Teunter, Babai y Syntetos (2010), ABC Classification: Service Levels and Inventory Costs, POM 19(3), 343-352: https://doi.org/10.1111/j.1937-5956.2009.01098.x (según su resumen)"
  - "DeHoratius y Raman (2008), Inventory Record Inaccuracy: An Empirical Analysis, Management Science 54(4), 627-641: https://doi.org/10.1287/mnsc.1070.0789 (según su resumen)"
  - "Kök y Shang (2007), Inspection and Replenishment Policies for Systems with Inventory Record Inaccuracy, MSOM 9(2), 185-205: https://doi.org/10.1287/msom.1060.0136 (según su resumen)"
  - "Inventario-y-depositos/.investigacion/existencias-y-control.md (componente 2) y fundamentos-y-contraria.md (secciones 4.1 y 4.4), 2026-11-27"
aliases: [conteo cíclico, cycle count, cycle counting, inventario rotativo, conteo rotativo, inventario físico, conteo físico, physical inventory, inventario anual, toma de inventario, recuento]
creado: 2026-11-27
revisado: 2026-11-27
---

# Conteo cíclico

El conteo cíclico cuenta una parte chica del stock por vez, según un calendario fijo, para que todo el depósito se cuente a lo largo del año sin frenar la operación. Reemplaza o complementa el inventario físico anual, y su decisión central es qué contar más seguido: por clase de artículo o por ubicación.

Es la herramienta principal de [Control del stock](control-del-stock.md): el conteo encuentra la diferencia entre el registro y el estante, y [ajustes y mermas](ajustes-y-mermas.md) la registra.

## Del inventario anual al conteo de a partes

El inventario físico tradicional cuenta todo de una vez, una vez por año. La práctica de software lo conserva como punto de partida: un sistema abierto trae por defecto un conteo completo anual al 31 de diciembre, y otro describe su conciliación de stock como el conteo de los productos «periodically at the year-end» (las dos, según su resumen). Contar todo junto suele pedir cerrar el depósito o congelar los movimientos mientras dura; eso es criterio de la base, sin fuente leída.

El conteo cíclico, según el resumen de la enciclopedia, cuenta un subconjunto chico del stock de manera repetida y según un calendario, y no frena la operación. Además de evitar el cierre, encuentra las diferencias cerca de cuando se produjeron. Un error del lunes que se descubre el martes deja rastros (el pedido, el remito, la persona del turno); el mismo error descubierto en diciembre no deja ninguno. Esto último es inferencia de la base.

Kök y Shang (2007) dan el respaldo de modelo: con registros que se saben inexactos, un conteo cíclico con niveles que dependen del estado rinde casi igual que la política de inspección que proponen (según su resumen).

## Qué se cuenta más seguido: por clase o por ubicación

En la práctica hay dos diseños, y un sistema puede ofrecer uno u otro:

| Diseño | Cómo reparte los conteos | Dónde aparece |
|---|---|---|
| Por clase de artículo | Los artículos se agrupan con la [clasificación ABC](../Reposicion/clasificacion-abc.md) por el método de Pareto, y los de mayor valor se cuentan más seguido | La mayoría de las implementaciones, según la enciclopedia |
| Por ubicación | Cada [ubicación](../Operacion-del-deposito/ubicaciones.md) tiene una frecuencia en días; al aplicar los ajustes de un conteo, el sistema programa el siguiente | Un sistema abierto (la frecuencia por defecto es 0) |

Contar por ubicación tiene una ventaja que no da el ABC: el contador recorre un pasillo y cuenta todo lo que hay, así que encuentra también lo que está donde no debía. Contar por clase obliga a buscar cada artículo en todas sus ubicaciones. Esta comparación es criterio de la base.

> [!NOTE] Sin fuente todavía: frecuencias por clase, tolerancias de diferencia y una meta de exactitud con fuente primaria. Una guía de un proveedor que solo se vio en el resumen de un buscador da A semanal o mensual, B trimestral y C anual, con 98 a 99 % de exactitud como meta; no se usa hasta tener una fuente mejor.

## Dónde falla el ABC por valor

Ordenar por valor es el diseño más común y el más discutido. La enciclopedia lista sus desventajas: por valor se dejan de lado artículos baratos que pueden frenar una línea, por uso se sesga contra lo caro, y los conteos hechos por gente sin capacitar pueden empeorar el inventario.

Teunter, Babai y Syntetos (2010) probaron en tres conjuntos de datos reales que ordenar los artículos por valor o por volumen, con un nivel de servicio fijo por clase, da costos lejos del óptimo, y proponen un criterio mejor que puede incluir la criticidad (según su resumen). El trabajo trata de niveles de servicio por clase, no de frecuencia de conteo: llevar la crítica al conteo es inferencia de la base.

DeHoratius y Raman (2008) apuntan en la misma dirección por otro camino. Si la categoría de producto explica el 26,4 % de la varianza de la inexactitud y la tienda solo el 2,7 %, conviene contar más seguido lo que más se equivoca, y no solo lo que más vale. Esa conclusión es inferencia de la base sobre su resumen. En la práctica se traduce en sumarle al ABC un criterio de propensión al error: los artículos con diferencias en los últimos conteos suben de frecuencia.

## Los errores que mete el propio conteo

Contar también puede introducir errores. La enciclopedia nombra tres causas: un artículo guardado en varias ubicaciones, el trabajo en curso y las demoras en cargar los papeles. Las tres tienen la misma forma, que es lectura de la base: el registro y el estante se comparan en momentos distintos o sobre lugares distintos.

De ahí salen las reglas de un conteo bien hecho, que son criterio de la base:

1. Fijá el corte: qué movimientos entraron al registro antes de contar. Lo que se recibió, se preparó o se movió durante el conteo se trata aparte.
2. Contá por ubicación y registrá la ubicación junto con la cantidad, aunque el diseño sea por clase.
3. Antes de ajustar una diferencia, buscá el artículo en sus otras ubicaciones y en los movimientos pendientes de carga; si sigue, recontá.
4. Recién ahí pasá la diferencia a [ajustes y mermas](ajustes-y-mermas.md), con el motivo.

> [!NOTE] Sin fuente todavía: si conviene que quien cuenta vea la cantidad que espera el sistema (conteo a ciegas) y qué hacer con los movimientos durante el conteo; ninguna fuente leída lo trata.
