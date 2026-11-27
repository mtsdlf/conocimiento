---
resumen: >-
  La planificación de capacidad compara las horas que pide el plan con las que tiene la planta, en cada nivel de la cascada: los recursos para el plan agregado, la capacidad gruesa para el plan maestro y los requerimientos de capacidad para las órdenes del MRP. El MRP calcula con capacidad infinita; estos controles muestran dónde el plan no entra, y cerrar ese lazo es lo que dio el MRP de lazo cerrado y el MRP II.
estado: borrador
estabilidad: estable
fuentes:
  - "Lymperopoulos, G., Σχεδιασμός και Προγραμματισμός Παραγωγής: MRP (diapositivas, Univ. de Tesalia, 25/11/2015, sobre Hopp y Spearman, Factory Physics, cap. 3), sección 2.2.3, ejemplos de RCCP y CRP (traducción de la base): https://opencourses.uth.gr/modules/document/file.php/MHXB125/MRP.pdf"
  - "Gershwin, S. B., Material Requirements Planning, diapositivas de MIT 2.853/2.854 (MIT OCW, otoño de 2016), diapositivas 34 y 40 a 42: https://ocw.mit.edu/courses/2-854-introduction-to-manufacturing-systems-fall-2016/4eec617bb52d64f4ea1bed6d9905bc00_MIT2_854F16_MatrialRequire.pdf"
  - "Solucionario de preguntas de discusión sobre MRP, curso IE 314, KSU: https://faculty.ksu.edu.sa/sites/default/files/mrp.pdf"
  - "ASCM, CPIM LS 2020 Excerpt (MRP abierto, de lazo cerrado y MRP II): https://learningsystem.ascm.org/wp-content/uploads/2019/11/CPIM_LS_2020_Excerpt.pdf"
  - "ASCM, CPIM Version 6.1, 2019 Edition, módulo 1, sección F (capable-to-promise, del APICS Dictionary, 15.ª ed.): https://learningsystem.ascm.org/wp-content/uploads/2018/11/APICS_CPIM_2019_Excerpt.pdf"
  - "Petropoulos, F. y otros (2025), Operations & Supply Chain Management: Principles and Practice, arXiv:2503.05749v2, pasaje sobre MRP-I y MRP-II: https://arxiv.org/pdf/2503.05749"
  - "Documentación de un sistema comercial, «Finite capacity planning and scheduling»: https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/finite-capacity"
  - "Documentación de «Manufacturing Settings» de un sistema abierto: https://docs.frappe.io/erpnext/user/manual/en/manufacturing-settings"
  - "Produccion/.investigacion/planificacion.md (sección 4) y planificacion-2.md (sección 8), 2026-11-27"
aliases: [planificación de capacidad, capacity planning, planificación de recursos, resource planning, capacidad gruesa, planificación gruesa de la capacidad, rough-cut capacity planning, RCCP, lista de recursos, bill of resources, perfil de recursos, planificación de requerimientos de capacidad, requerimientos de capacidad, capacity requirements planning, CRP, perfil de carga, load profile, carga infinita, infinite loading, carga finita, finite loading, capacidad finita, finite capacity scheduling, MRP de lazo cerrado, closed-loop MRP, MRP II, planificación de los recursos de fabricación, manufacturing resource planning]
creado: 2026-11-27
revisado:
---

# Planificación de capacidad

La planificación de capacidad compara las horas que pide el plan con las que tiene la planta, en cada nivel de la cascada: los recursos para el plan agregado, la capacidad gruesa para el plan maestro y los requerimientos de capacidad para las órdenes del MRP. El MRP calcula con capacidad infinita; estos controles muestran dónde el plan no entra, y cerrar ese lazo es lo que dio el MRP de lazo cerrado y el MRP II.

Es el control que acompaña a cada plan de [Planificación de la producción](planificacion-de-la-produccion.md). Las horas salen de la [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md), que dice cuánto tarda cada operación en cada centro de trabajo; la capacidad del centro (calendario, eficiencia, utilización) está en la misma nota, en [el centro de trabajo](../Producto-y-proceso/ruta-de-fabricacion.md#el-centro-de-trabajo-dónde-se-hace-y-cuánto-puede). La secuencia en que pasan los trabajos por cada máquina ya no es de acá: es de [programación de planta](../Ejecucion-en-planta/programacion-de-planta.md).

## Tres controles, uno por nivel

| Control | Contra qué plan | Qué mira | Con qué |
|---|---|---|---|
| Planificación de recursos | plan agregado | personal, turnos, equipos, por familia y mes | horas o personas por familia |
| Capacidad gruesa (RCCP) | [plan maestro](plan-maestro-de-produccion.md) | unos pocos recursos críticos, por semana | la lista de recursos de cada producto final |
| Requerimientos de capacidad (CRP) | órdenes del [MRP](mrp.md) | cada centro de trabajo, por día | la ruta de cada orden |

La planificación de recursos va con el plan agregado, que es de Cadena: el MIT la pone en el largo plazo, junto al «Aggregate planning — determines rough estimates of production, staffing, etc.». Cómo se decide ahí entre perseguir la demanda o nivelar está en [plan de ventas y operaciones](../../Cadena-de-suministro-y-logistica/Planificacion/plan-de-ventas-y-operaciones.md#perseguir-la-demanda-o-nivelar).

## Capacidad gruesa: el plan maestro contra los recursos críticos

La capacidad gruesa es un control rápido. Las diapositivas de la Universidad de Tesalia, sobre Hopp y Spearman, la definen como un control «of the capacity of a few critical resources, in order to ensure the MPS is feasible». Usa una lista de recursos, que «gives the number of hours required at each critical resource to make one end item» (traducción de la base). La lista de recursos aplana la lista de materiales y la ruta: suma, por producto final, las horas propias y las de sus componentes en ese recurso.

El ejemplo de la fuente tiene dos productos y un centro de trabajo, el 21. El producto A lleva 1 hora en el centro, y sus componentes A1 y A2, media hora y una hora: 2,5 horas por unidad de A. El producto B no tiene componentes y lleva 2 horas. El centro tiene 65 horas por semana.

| Semana | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Plan maestro de A | 10 | 10 | 10 | 20 | 20 | 20 | 20 | 10 |
| Plan maestro de B | 5 | 25 | 5 | 15 | 10 | 25 | 15 | 10 |
| Horas de A | 25 | 25 | 25 | 50 | 50 | 50 | 50 | 25 |
| Horas de B | 10 | 50 | 10 | 30 | 20 | 50 | 30 | 10 |
| Total | 35 | 75 | 35 | 80 | 70 | 100 | 80 | 35 |
| Disponibles | 65 | 65 | 65 | 65 | 65 | 65 | 65 | 65 |
| Sobra o falta | 30 | −10 | 30 | −15 | −5 | −35 | −15 | 30 |

La tabla es la de la fuente. Las cuentas verifican salvo en la semana 8: con 10 unidades de B a 2 horas, las horas de B son 20 y no 10, el total es 45 y sobran 20, no 30 (cuenta de la base). La conclusión no cambia: faltan horas en cinco semanas de ocho y sobran en las otras.

La fuente da dos salidas: cambiar las fechas del plan maestro, o cambiar la capacidad con horas extra o subcontratación. Un solucionario de otro curso agrega partir una orden hacia antes o hacia después y usar un proceso alternativo; si la falta es crónica, «a capital investment to increase capacity, add a shift, or develop an outside source». En el ejemplo, mover producción de la semana 6 a la 1 o la 3, que tienen 30 horas libres cada una, cubre buena parte del faltante (lectura de la base). El precio de adelantar es stock antes de tiempo, y mover dentro de la zona congelada del plan maestro no se puede sin autorización (ver [barreras](plan-maestro-de-produccion.md#barreras-y-zonas-de-tiempo)).

En una planilla, la capacidad gruesa son dos tablas que se multiplican: el plan maestro por la lista de recursos, contra una fila de horas disponibles (criterio de la base).

## Requerimientos de capacidad: las órdenes contra cada centro

El CRP baja al detalle de las órdenes que propuso el MRP. Tesalia lo define así: «provides a more detailed check of the MRP-generated schedules than RCCP». Hace una carga hacia adelante con capacidad infinita: «CRP predicts completion times for each work center using fixed lead times and then calculates a forecast workload over time. The loads are compared with available capacity, but no correction is made for overload situations».

El ejemplo de la fuente: un centro con plazo de 3 días y capacidad de 400 piezas por día. Al empezar el día hay 400 piezas recién llegadas, 500 con un día en el centro y 300 con dos. Los lanzamientos planificados de los días 1 a 5 son 300, 350, 400, 350 y 300. Si alguna vez se prevén más de 400 por día, el centro está sobrecargado. La fuente muestra el resultado en un gráfico; leído como salidas por día con el plazo de 3 días, el perfil de carga es:

| Día | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Piezas que terminan | 300 | 500 | 400 | 300 | 350 | 400 | 350 | 300 |
| Contra 400 por día | | sobrecarga | | | | | | |

La tabla es cuenta de la base: lo que lleva dos días sale el día 1, lo que lleva uno el 2, lo recién llegado el 3, y cada lanzamiento sale tres días después. Coincide con la escala del gráfico, que llega a 500.

Tesalia es dura con el CRP. Aun con el centro sobrecargado, supone que el tiempo de paso no cambia, así que solo sirve en el horizonte muy cercano. Encuentra dónde está el problema, pero no qué lo causó ni cómo arreglarlo. Y concluye que, por esos defectos, cada vez menos empresas lo usan.

## Carga infinita y carga finita

La carga infinita pone el trabajo en la fecha que pide el plan, entre o no; la finita lo corre hasta donde haya capacidad. El MRP y el CRP son de carga infinita. Una revisión abierta de 2025 lo resume: «While MRP-I assumes infinite capacities, MRP-II incorporates capacity constraints». El MIT lo dice como crítica: el MRP se formula sobre un modelo «deterministic, infinite capacity», y «Capacity is actually finite».

La definición más clara leída es de la documentación de un sistema comercial: la capacidad finita es un enfoque para saber «how much work can be produced during a specific period when limitations on different resources are taken into consideration», y produce un programa más realista que el de carga infinita, porque «If there isn't enough capacity on the resources, the delivery date is pushed out, and the job is scheduled when there's enough capacity». El mismo sistema aclara un límite: si la capacidad cambia con los requerimientos, como cuando se agregan turnos, no conviene usar capacidad finita, porque los tiempos calculados no van a ser correctos.

La carga finita es la base del capaz de prometer. El diccionario de ASCM, citado en el CPIM, dice que el CTP «Employs a finite-scheduling model of the manufacturing system to determine when an item can be delivered». Ver [fecha prometida](../../Relacion-con-clientes/Pedido-de-venta/fecha-prometida.md#capable-to-promise-cuando-hay-que-producir).

> [!NOTE] Sin fuente todavía: las definiciones de «finite loading» e «infinite loading» del diccionario de ASCM. La de arriba es de la documentación de un sistema: muestra cómo se implementa, no es una definición de fundamentos.

## Del MRP de lazo cerrado al MRP II

Agregar estos controles cambió el nombre del sistema. Según el material de ASCM, los primeros sistemas eran MRP abiertos, que hacían «a simplifying assumption that there was infinite capacity (thus the open loop)». Después se agregaron «capacity checks at the master scheduling and MRP stages to ensure feasibility», y ese lazo de vuelta «defined the major advancement of these systems, called closed-loop MRP».

El MRP II fue el paso siguiente: un solucionario de un curso dice que «includes or integrates functions within the firm in addition to the management of dependent demand inventories», como «Order entry, invoicing, billing, purchasing, production scheduling, capacity planning, and warehouse management». La revisión de 2025 agrega que el MRP II «requires a step-by-step process to plan materials and capacities, and it is sometimes difficult to generate plans that consider volatility». Quién lo propuso y cuándo, y cómo siguió hasta el ERP, está en [fundamentos de producción](../Fundamentos/fundamentos-de-produccion.md).

## Qué guarda un sistema para la capacidad

- Por centro de trabajo: capacidad por período, calendario con turnos y feriados, eficiencia y utilización (en la [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md#qué-guarda-una-ruta-de-fabricación)).
- Por producto final: la lista de recursos, con horas por recurso crítico, para la capacidad gruesa.
- Por orden y operación: horas cargadas contra un centro y una fecha, y la marca de sobrecarga.
- Por plan: si se calcula con capacidad finita o infinita, y desde qué barrera en días rige la finita, como en el sistema comercial leído.

Un sistema abierto muestra los ajustes mínimos: desactivar la planificación de capacidad, permitir horas extra fuera del horario del centro, cuántos días hacia adelante se planifica («Capacity Planning For (Days)») y el tiempo entre operaciones. Es evidencia de que guarda capacidad y calendario, no de que haga capacidad gruesa ni CRP.
