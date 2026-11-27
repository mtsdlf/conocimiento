---
resumen: >-
  La jerarquía de activos ordena los equipos de una empresa de lo general a lo particular: la planta, sus sistemas, los lugares donde se instala un equipo, el equipo y sus componentes. Su decisión central es separar la ubicación técnica, que queda, del equipo, que se puede mover, para que cada uno guarde su propia historia.
estado: borrador
estabilidad: estable
fuentes:
  - "Reliable Media (Reliamag), How to build an asset hierarchy in a CMMS, cita la figura 3 de ISO 14224:2016 vía un paper de OTC (resumen): https://reliamag.com/topics/guides/how-to-build-asset-hierarchy-cmms"
  - "Wikipedia, ISO 14224 (resumen): https://en.wikipedia.org/wiki/ISO_14224"
  - "SAP Help 4.6C, Equipment at Functional Locations (como evidencia de práctica, resumen): https://help.sap.com/saphelp_46c/helpdata/en/01/d546244ab311d189740000e8322d00/content.htm"
  - "SAP Help 4.6C, Installing/Dismantling Equipment from the Functional Location Master Record (resumen): https://help.sap.com/saphelp_46c/helpdata/en/01/d546314ab311d189740000e8322d00/content.htm"
  - "SAP Help 4.6C, Installing/Dismantling from the Equipment Master Record (resumen): https://help.sap.com/saphelp_46c/helpdata/en/01/d546654ab311d189740000e8322d00/content.htm"
  - "SAP Help 4.6C, Replacing Equipment (resumen): https://help.sap.com/saphelp_46C/helpdata/EN/01/d546584ab311d189740000e8322d00/content.htm"
  - "SAP KBA 3582809 (solo extracto del buscador, no leído): https://userapps.support.sap.com/sap/support/knowledge/en/3582809"
  - "ERPNext, Asset Movement (como evidencia de práctica, resumen): https://docs.frappe.io/erpnext/user/manual/en/asset-movement"
  - "Activos-y-mantenimiento/.investigacion/registro-y-desempeno.md (2026-11-27), primera y segunda ronda"
aliases: [jerarquía de equipos, asset hierarchy, ubicación técnica, functional location, ubicación funcional, taxonomía de equipos, equipment taxonomy, ISO 14224, lista de repuestos del equipo, lista de materiales de mantenimiento, maintenance BOM, equipment BOM, componente mantenible, maintainable item]
creado: 2026-11-27
revisado:
---

# Jerarquía de activos

La jerarquía de activos ordena los equipos de una empresa de lo general a lo particular: la planta, sus sistemas, los lugares donde se instala un equipo, el equipo y sus componentes. Su decisión central es separar la ubicación técnica, que queda, del equipo, que se puede mover, para que cada uno guarde su propia historia.

Es la forma del [registro de activos](registro-de-activos.md). Sobre ella se calcula la [criticidad](criticidad.md), se cuelga el [plan preventivo](../Estrategia-de-mantenimiento/mantenimiento-preventivo.md) y se suman las fallas del [historial del equipo](historial-del-equipo.md). Sin software, es el árbol de la planta dibujado en una hoja y las chapitas con el código de cada posición.

## Los nueve niveles de la ISO 14224

La ISO 14224:2016 propone una taxonomía de nueve niveles. Según una guía secundaria que cita la figura 3 de la norma (la norma no se leyó):

| Nivel | Nombre en la norma | Qué es |
|---|---|---|
| 1 | Industry | la industria |
| 2 | Business category | la categoría de negocio |
| 3 | Installation | la instalación |
| 4 | Plant/Unit | la planta o unidad |
| 5 | Section/System | la sección o sistema |
| 6 | Equipment unit | el equipo |
| 7 | Subunit | el subconjunto |
| 8 | Component/Maintainable item | el componente mantenible |
| 9 | Part | la pieza |

Los niveles 1 a 5 describen el uso y la ubicación; los 6 a 9 subdividen el equipo. El nivel 6 es, en la cita de la misma guía, «the common reporting level for merging and assessment», y «a failure of a component is also counted as a failure of its parent equipment». Es decir: la falla de un rodamiento (nivel 8) cuenta también como falla de la bomba (nivel 6), y los indicadores se comparan a nivel de equipo.

Según un resultado del buscador, la norma es del petróleo, el gas natural y la petroquímica; para otras industrias es un modelo de referencia y no un requisito. Según la misma guía, la última edición cubre «108 equipment classes, with 46 in focus», cifra de un paper que no se verificó contra la norma. La guía aconseja no usar los nueve niveles el primer día. Como criterio de la base, una planta chica puede arrancar con planta, sistema, equipo y componente.

## Ubicación técnica y equipo

La ubicación técnica es el lugar donde se instala un equipo: «bomba de alimentación de la caldera 2». El equipo es el objeto físico, con su número de serie, que hoy ocupa ese lugar. La ubicación queda aunque el equipo se cambie; el equipo puede pasar por varias ubicaciones, estar sin instalar o en el depósito.

Un sistema de mantenimiento de referencia lo modela así, según resúmenes de su ayuda (versión 4.6C, antigua):

- La ubicación define dónde se puede instalar un equipo, y se configura para admitir ninguno, uno o varios.
- El equipo tiene que existir como registro antes de instalarlo. Si hay equipos dentro de equipos, solo el de más arriba se instala en la ubicación.
- Instalar abre una entrada en una lista de uso del equipo; desmontar la cierra con fecha y hora, y abre otra con los datos nuevos. Las fechas se pueden cargar hacia atrás.
- Reemplazar es desmontar uno e instalar otro, y queda un registro de qué salió y qué entró.

Un sistema abierto más simple no tiene ubicación técnica: la ubicación es un campo del activo, y cada traslado es un movimiento propio. Según su documentación, el movimiento «records every transfer, issue, and receipt as a separate event»: el más nuevo fija la posición actual y los anteriores quedan como historial.

## Qué pasa con el historial cuando el equipo cambia de lugar

Cuando la bomba de la posición 2 se saca para repararla y se pone una de repuesto, hay dos historias que interesan. La de la posición dice cuántas veces falló la bomba de alimentación de la caldera 2, sea cual sea la bomba: sirve para ver si el problema es del servicio (la instalación, el fluido, la operación). La del equipo dice cuántas veces falló esa bomba con ese número de serie, esté donde esté: sirve para ver si el problema es del aparato.

Las fuentes no coinciden en dónde queda la historia. La ayuda del sistema de referencia la guarda en el equipo, con su lista de uso. Publicaciones citadas por el buscador sostienen que el historial queda con la ubicación aunque se reemplace el activo, y el mismo buscador lo calificó de convención de modelado, no de regla. No se verificó.

> [!IMPORTANT]
> Un problema conocido del sistema de referencia muestra el riesgo, según un extracto del buscador de una nota de soporte no leída: al desmontar un equipo, la ubicación se blanquea en las órdenes cerradas y en curso. Si la orden guarda solo dónde está el equipo hoy, mover el equipo reescribe el pasado.

Como inferencia desde esas fuentes, el modelo que conserva las dos historias guarda la relación entre ubicación y equipo como intervalos con inicio y fin, igual que la lista de uso, y cada [orden de trabajo](../Orden-de-trabajo/orden-de-trabajo.md) guarda la ubicación y el equipo del momento en que se abrió. Así se reconstruye qué equipo estaba dónde en cada fecha. Es la idea que el [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md) aplica al stock: guardar cada cambio como un hecho que no se edita, en vez de sobrescribir el estado.

## Componentes y lista de repuestos del equipo

Debajo del equipo están los subconjuntos, los componentes mantenibles y las piezas (niveles 7 a 9). Como criterio de la base, un componente entra al registro como algo propio cuando se le hace mantenimiento por separado o cuando se lo quiere seguir: un motor que se saca, se repara en el taller y se instala en otra máquina es un equipo dentro de otro, con su número de serie. Un rodamiento que se tira al cambiarlo, en cambio, es una pieza.

La lista de repuestos del equipo dice qué piezas lleva cada equipo y en qué cantidad, para que la orden sepa qué pedir sin que el planificador lo busque cada vez. Qué repuestos reserva una orden y cuáles son críticos está en [repuestos y materiales](../Orden-de-trabajo/repuestos-y-materiales.md); cuántos hay en el depósito es del tema [Inventario y depósitos](../../Inventario-y-depositos/inventario-y-depositos.md).

> [!NOTE] Sin fuente todavía: cómo se arma la lista de repuestos del equipo (maintenance BOM), si es propia de cada equipo o de su clase, y cómo se relaciona con la lista de materiales de producción. La guía de jerarquía leída dice explícitamente que no trata repuestos, y no se alcanzó ninguna página de un sistema sobre el tema.
