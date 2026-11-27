---
resumen: >-
  Reparar o reemplazar es la decisión de seguir manteniendo un equipo o darlo de baja y poner otro, y se toma comparando cuánto cuesta por año cada camino a lo largo de su vida. Las herramientas son el costo del ciclo de vida, que suma todo lo que cuesta tener el equipo, y el costo anual equivalente, que pone en la misma unidad opciones de vidas distintas.
estado: borrador
estabilidad: estable
fuentes:
  - "Wikipedia, Whole-life cost (resumen): https://en.wikipedia.org/wiki/Whole-life_cost"
  - "Wikipedia, Equivalent annual cost (resumen): https://en.wikipedia.org/wiki/Equivalent_annual_cost"
  - "NIST, Life-Cycle Costing Manual for the Federal Energy Management Program, NIST Handbook 135 (1995), cap. 1, pp. 1-1 y 1-2 (PDF escaneado, leído como imagen; el resto no): https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=907459 ; ficha: https://www.nist.gov/publications/life-cycle-costing-manual-federal-energy-management-program-nist-handbook-135-1995"
  - "A Multi-Criteria Decision-Making Framework for Fleet Sizing and Replacement Age of Critical Medical Equipment (artículo de acceso abierto, 2026), sobre el costo anual equivalente: https://pmc.ncbi.nlm.nih.gov/articles/PMC13763394/"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 10.2.3.5 y 10.4.1, pp. 27-28: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "ERPNext, Asset Repair (como evidencia de práctica, resumen): https://docs.frappe.io/erpnext/user/manual/en/asset-repair"
  - "Activos-y-mantenimiento/.investigacion/registro-y-desempeno.md (2026-11-27), componente 2 y segunda ronda, sección 5"
  - "Activos-y-mantenimiento/.investigacion/apqc-10.md (2026-11-27)"
  - "Activos-y-mantenimiento/.investigacion/verificacion-registro-y-desempeno.md (2026-11-27)"
aliases: [reparar o reemplazar, repair or replace, decisión de reemplazo, replacement decision, costo del ciclo de vida, life cycle cost, LCC, costo total de propiedad, whole-life cost, total cost of ownership, TCO, costo anual equivalente, equivalent annual cost, EAC, vida económica, economic life, fin de vida del activo, asset end-of-life]
creado: 2026-11-27
revisado:
---

# Reparar o reemplazar

Reparar o reemplazar es la decisión de seguir manteniendo un equipo o darlo de baja y poner otro, y se toma comparando cuánto cuesta por año cada camino a lo largo de su vida. Las herramientas son el costo del ciclo de vida, que suma todo lo que cuesta tener el equipo, y el costo anual equivalente, que pone en la misma unidad opciones de vidas distintas.

Es la decisión más grande de la vertical [Desempeño de los activos](desempeno-de-los-activos.md) y la que cierra la vida del equipo en el [registro de activos](../Registro-de-activos/registro-de-activos.md). APQC 7.4 la pone al principio del fin de vida, en 10.4.1 «Develop exit strategy», con dos procesos: 10.4.1.1 «Monitor useful life of assets» y 10.4.1.2 «Perform cost vs. benefit analysis for replacement». La ejecución del reemplazo cae en otro grupo, 10.2.3.5 «Renew/Replace assets», dentro de construir activos.

## Lo que suma el costo del ciclo de vida

El costo del ciclo de vida es el costo total de tener un activo durante toda su vida, no solo el precio de compra. Según el resumen de Wikipedia, es el «total cost of ownership over the life of an asset» y suma «planning, design, construction and acquisition, operations, maintenance», además de «renewal and rehabilitation, depreciation and cost of finance and replacement or disposal».

Esa lista mete la amortización y el costo financiero, y otras definiciones lo tratan distinto. La referencia pública del método es el Handbook 135 del NIST (1995), la guía de costo del ciclo de vida para proyectos de energía, agua y renovables en edificios federales de Estados Unidos. Su capítulo 1 define el costo del ciclo de vida de un sistema como «the total cost of owning, operating, maintaining, and (eventually) disposing of» él «over a given study period (usually related to the life of the project), with all costs adjusted (discounted) to reflect the time-value of money». No nombra la amortización contable: lo que entra es lo que cuesta tener el equipo, descontado en el tiempo. El manual agrega que ese número «has little value by itself» y sirve para comparar alternativas que cumplen la misma función, a las que llama «mutually exclusive». Su ejemplo central son alternativas de diseño de un edificio, que pueden tener «possibly different lives»; el manual aclara que no trae datos de costos ni «expected lives» de los sistemas. Del resto del manual no se leyó nada, y no consta si trata el reemplazo de un equipo en uso.

Como criterio de la base, de todo eso el mantenimiento aporta lo que más cambia año a año: lo que costó cada [orden de trabajo](../Orden-de-trabajo/orden-de-trabajo.md) sobre el equipo, que queda sumado en el [historial del equipo](../Registro-de-activos/historial-del-equipo.md). Sin órdenes cerradas con su costo, la decisión se apoya en la memoria de quien mantiene.

## El costo anual equivalente

Dos equipos con vidas distintas no se comparan por su costo total: el que dura más siempre suma más. El costo anual equivalente (EAC) lo resuelve convirtiendo todo en una cuota anual. Según Wikipedia, es «the cost per year of owning and operating an asset over its entire lifespan», y supone que las opciones tienen el mismo riesgo. El Handbook 135 del NIST llama a esto valor anual: «the cost resulting from amortizing all project costs evenly over the study period, taking into account the time-value of money».

La fórmula es EAC = −VAN / A(t, r), donde VAN es el valor actual neto de la opción, r la tasa anual y t los años, y A(t, r) = (1 − 1/(1 + r)^t) / r es el factor de anualidad. Con un costo de mantenimiento parejo cada año, como en el ejemplo siguiente, queda la inversión dividida por el factor, más el mantenimiento anual.

El ejemplo de Wikipedia compara dos máquinas a una tasa del 5 %:

| | Máquina A | Máquina B |
|---|---|---|
| Inversión | 50.000 | 150.000 |
| Vida | 3 años | 8 años |
| Mantenimiento anual | 13.000 | 7.500 |
| Factor A(t; 5 %), calculado con la fórmula | 2,7232 | 6,4632 |
| Costo anual equivalente | 50.000 / 2,7232 + 13.000 = 31.360 | 150.000 / 6,4632 + 7.500 = 30.708 |

La máquina B cuesta el triple y sale más barata por año, y la fuente concluye invertir en ella. Las cuentas se rehicieron y cierran. El ejemplo compara dos compras nuevas; no es todavía la decisión de reparar o reemplazar un equipo que ya está andando. Un artículo de acceso abierto sobre la edad de reemplazo de una flota de equipos médicos marca el límite: el costo anual equivalente trata cada política como un ciclo que se repite y «disregards the initial age» de la flota, así que «is more representative of a steady state than of a transient state, or a one-off decision accounting for a pre-existing situation». Para un equipo ya instalado hace falta mirar también la edad que tiene.

## La vida económica

La vida económica de un equipo es la edad hasta la que conviene tenerlo: la que hace mínimo su costo anual equivalente. Con los años la inversión se reparte en más cuotas y la cuota baja, pero el mantenimiento sube con el desgaste; en algún año la suma deja de bajar. Wikipedia lista entre las aplicaciones del costo anual equivalente «determining the optimum economic life of an asset» y «determining the cost of continuing with existing equipment»; la definición de vida económica como el mínimo de ese costo anual, y la idea de comparar el equipo actual contra el que lo reemplazaría, no se encontraron en una fuente leída: quedan como criterio de la base.

La vida económica no es la vida útil contable. La vida útil es una estimación para repartir el costo como amortización, se fija al dar de alta el bien y se revisa como cambio de estimación, según [activos fijos y amortización](../../Contabilidad/Operaciones/activos-fijos-y-amortizacion.md). La vida económica sale de los costos reales del equipo y puede ser más corta o más larga. Como criterio de la base, a veces conviene seguir usando años un equipo totalmente amortizado, y a veces conviene reemplazar mañana uno a mitad de amortizar.

> [!NOTE] Sin fuente todavía: la vida económica como mínimo del costo anual equivalente, el método del defensor y el retador, los criterios de baja y un ejemplo numérico de reemplazo de un equipo en uso. Las normas que lo tratan (IEC 60300-3-3, ISO 15663) son de pago y no se leyeron, y el Handbook 135 se leyó solo en su capítulo 1; tampoco se encontró un libro de ingeniería económica de acceso abierto.

## Qué mira el mantenimiento antes de decidir

El proceso 10.4.1.1 de APQC se llama «Monitor useful life of assets». Como criterio de la base, eso se hace mientras el equipo anda y no cuando se rompe del todo, y las señales salen de los [indicadores de mantenimiento](indicadores-de-mantenimiento.md) y del historial: el costo anual de mantenimiento del equipo que sube, el MTBF que baja, los repuestos que el fabricante deja de vender y una [criticidad](../Registro-de-activos/criticidad.md) alta que hace cara cada parada.

Entre reparar y reemplazar hay un camino del medio: una reparación grande que alarga la vida, como cambiar el motor de una máquina. Un ERP abierto la registra en la reparación con un campo para el aumento de vida, «Increase in asset life», y un interruptor para capitalizar su costo, con la regla general «Routine repair is normally an expense». Lo que el [cierre de la orden](../Orden-de-trabajo/cierre-de-la-orden.md) tiene que dejar para esa decisión está explicado allí.

## Dónde empieza el lado contable

Como criterio de la base, reemplazar un equipo deja dos registros que se cierran por separado: el operativo, en el registro de activos, y el contable, en el bien de uso. Dar de baja el equipo en uno no lo da de baja en el otro. La baja contable, con el valor en libros que queda y el resultado de la venta, está en [activos fijos y amortización](../../Contabilidad/Operaciones/activos-fijos-y-amortizacion.md).

Para la decisión, el valor en libros del equipo viejo no es un costo de seguir usándolo: es plata que ya salió cuando se compró. Lo que cuenta es lo que se puede cobrar si se vende hoy y lo que cuesta mantenerlo de acá en adelante. Esta separación, central en la ingeniería económica, no se encontró en una fuente leída y queda como criterio de la base; la idea de que la amortización no aparta plata sí está sostenida en la nota contable.
