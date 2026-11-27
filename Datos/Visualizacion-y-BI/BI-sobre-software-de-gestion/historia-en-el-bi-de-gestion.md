---
resumen: >-
  La historia en el BI de gestión es lo que el BI guarda y el sistema de gestión pisa o no tiene:
  qué vendedor, zona o centro de costo tenía cada cosa en su momento, los saldos de cada cierre,
  lo que ya se informó de un período y los años que quedaron en el sistema anterior. Con eso un
  reporte puede mostrar el dato como era o como es hoy, y decir cuál de los dos muestra.
estado: borrador
estabilidad: estable
fuentes:
  - "Kimball Group, Type 0 a Type 7 (dimensiones lentamente cambiantes): https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/type-2/"
  - "Kimball Group, Late Arriving Fact y Late Arriving Dimension: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/late-arriving-dimension/"
  - "Kimball Group, Natural, Durable, and Supernatural Keys: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/natural-durable-supernatural-key/"
  - "Kimball y Ross, The Data Warehouse Toolkit, 3.ª ed. (Wiley, 2013), cap. 1, extracto oficial: https://media.wiley.com/product_data/excerpt/02/11185308/1118530802-32.pdf"
  - "W. H. Inmon, What Is a Data Warehouse?, Prism Tech Topic 1(1), 1995 (copia en archive.org): https://web.archive.org/web/20010424175209/http://www.cait.wustl.edu:80/cait/papers/prism/vol1_no1/"
  - "Golfarelli y Rizzi, Managing Late Measurements in Data Warehouses, IJDWM 3(4), 2007 (solo el resumen): https://ideas.repec.org/a/igg/jdwm00/v3y2007i4p51-67.html"
  - "Datos/.investigacion/bi-gestion-modelado.md y bi-gestion-extraccion.md (2026-11-27)"
aliases: [historia en el BI, as-was y as-is, como era y como es, SCD en gestión, dimensión lentamente cambiante en el ERP, hecho tardío, late arriving fact, reorganización de centros de costo]
creado: 2026-11-27
revisado:
---

# Historia en el BI de gestión

La historia en el BI de gestión es lo que el BI guarda y el sistema de gestión pisa o no tiene: qué vendedor, zona o centro de costo tenía cada cosa en su momento, los saldos de cada cierre, lo que ya se informó de un período y los años que quedaron en el sistema anterior. Con eso un reporte puede mostrar el dato como era o como es hoy, y decir cuál de los dos muestra.

Es la razón más fuerte para que el [BI sobre el software de gestión](bi-sobre-software-de-gestion.md) no sea una copia de la base. Kimball y Ross: los sistemas operativos «typically do not maintain history, but rather update data to reflect the most current state», y un buen almacén «can relieve the source systems of much of the responsibility for representing the past». Inmon pone el horizonte del almacén en cinco a diez años. Las técnicas generales, empezando por las dimensiones lentamente cambiantes, están en [modelado dimensional](../../Modelado-y-almacenamiento/modelado-dimensional.md#cuando-el-contexto-cambia-en-el-tiempo).

## Lo que el sistema guarda y lo que pisa

Un sistema de gestión bien hecho conserva la historia de los hechos, porque no edita sus movimientos, y suele pisar el contexto (lectura de esta base):

| Cambia | Qué guarda el sistema | Qué pregunta queda sin respuesta |
|---|---|---|
| El vendedor asignado a un cliente | el vendedor de hoy en la ficha del cliente | cuánto vendió cada vendedor con la cartera que tenía cada mes |
| La zona o la categoría de un cliente | la de hoy | cómo evolucionó cada zona tal como estaba armada |
| La categoría de un artículo | la de hoy | ventas por categoría con la categoría que tenía en su momento |
| La jerarquía de centros de costo | la estructura nueva | el gasto de un área que se partió en dos |
| El saldo de un cliente | el saldo de hoy, calculado de los movimientos | el saldo y su antigüedad al cierre de cada mes, sin recalcular |

Algunos datos sí traen su vigencia en el sistema: la lista de precios, la alícuota, el sueldo, como explica [vigencias](../../../Software-de-gestion/Columnas-tecnicas/fechas-vigencias-y-cierre.md#vigencias-datos-que-valen-desde-y-hasta). Un documento confirmado también copia datos del maestro, como el domicilio o la condición de IVA. En esos casos el BI no reconstruye nada y lee el valor del documento.

## Como era o como es hoy

La misma pregunta tiene dos respuestas legítimas. Las ventas de la zona norte del año pasado pueden ser las de los clientes que eran de la zona norte el año pasado (como era) o las de los clientes que hoy son de la zona norte (como es hoy). La comisión de un vendedor se calcula como era; la proyección de su cartera para el año que viene, como es (lectura de esta base).

Kimball tiene un tipo de dimensión lentamente cambiante para cada caso:

| Tipo | Qué hace | Para qué en gestión |
|---|---|---|
| 1, sobrescribir | el valor nuevo pisa al viejo; «this technique destroys history» | corregir un error de carga, como un nombre mal escrito |
| 2, fila nueva | agrega una fila con los valores nuevos y fechas de vigencia; los hechos nuevos apuntan a ella | ver como era: la zona del cliente en el momento de cada venta |
| 6, tipo 1 dentro del 2 | cada fila guarda el valor de su momento y además el actual, para agrupar «by either the type 2 attribute value in effect when the measurement occurred or the attribute's current value» | ver como era y como es hoy en la misma dimensión |
| 7, dos claves en el hecho | el hecho guarda la clave de la fila de su momento y la clave durable de la entidad, para «both as-was and as-is reporting» | lo mismo, con más flexibilidad para quien consulta |

La decisión se toma por atributo. En el cliente, el nombre puede ser tipo 1, la zona tipo 2 y el vendedor tipo 6. El reporte tiene que decir cuál muestra; dos tableros que no lo dicen dan dos números para «ventas de la zona norte» (lectura de esta base).

## Las reorganizaciones

Una reorganización cambia una jerarquía entera: el área comercial se parte en dos, dos sucursales se fusionan, el plan de cuentas agrega un nivel. Para comparar con años anteriores hay dos caminos (lectura de esta base). Uno es rehacer el pasado con la estructura nueva, con una tabla de equivalencias entre el centro viejo y el nuevo, y avisar que el pasado se rehízo. El otro es mostrar cada período con la estructura que tenía y aceptar que no se comparan línea por línea. El *Toolkit* trata las jerarquías que cambian en el tiempo en su capítulo de contabilidad, en secciones como «Time Varying Ragged Hierarchies» y «Modifying Ragged Hierarchies», según su índice; el texto no se leyó.

## Lo que se informó y lo que es

Un sistema de gestión tiene dos fechas para cada hecho: cuándo pasó y cuándo se registró, como explica [la fecha del hecho y la fecha de registro](../../../Software-de-gestion/Columnas-tecnicas/fechas-vigencias-y-cierre.md#la-fecha-del-hecho-y-la-fecha-de-registro). Con las dos, el BI contesta dos preguntas: cuánto se vendió en octubre, según lo que se sabe hoy, y cuánto se informó en noviembre que se había vendido en octubre. Golfarelli y Rizzi (2007) sostienen que con mediciones que llegan tarde las soluciones tradicionales «fail in preserving accountability and query consistency», y proponen separar el tiempo de transacción del tiempo válido; solo se leyó su resumen.

Kimball trata el mismo problema como hecho tardío: cuando una fila llega después de que cambió su contexto, se buscan las claves de dimensión «that were effective when the late arriving measurement event occurred». Si lo que llega tarde es un cambio retroactivo de la dimensión, hay que agregar la fila nueva y además «the associated fact rows must be restated».

En la práctica (lectura de esta base):

- Mientras el período está abierto, el BI muestra lo que se sabe hoy y cambia cada día.
- Cuando el período se cierra con la [fecha de bloqueo](../../../Software-de-gestion/Columnas-tecnicas/fechas-vigencias-y-cierre.md#la-fecha-de-bloqueo), el BI guarda una foto de lo informado: los saldos y los totales de ese cierre. Esa foto es la que tiene que coincidir con el balance presentado.
- Un hecho de octubre que llega en diciembre entra en octubre con su fecha del hecho, y queda marcado con su fecha de registro para explicar la diferencia con la foto.

## La historia que quedó en el sistema anterior

Cuando una empresa cambia de sistema, la [migración](../../../Software-de-gestion/Implementacion/migracion-de-datos.md#qué-se-migra-y-qué-se-deja) suele cargar maestros, saldos y documentos abiertos, y dejar la historia en el sistema viejo. El análisis de varios años queda partido en dos fuentes con claves distintas. El BI es el único lugar donde se vuelven a unir: los clientes y artículos del sistema viejo se mapean a la [clave durable](dimensiones-conformadas.md#las-dimensiones-que-comparten-los-dominios) del nuevo, y los hechos de los dos sistemas van a la misma tabla con una marca de origen (lectura de esta base). Kimball justifica la clave durable con un caso parecido: el número de empleado cambia si alguien renuncia y vuelve a entrar, pero «the durable key never changes».

## Cómo falla

- La comisión recalculada con la cartera de hoy. El cliente que pasó a otro vendedor se lleva sus ventas pasadas.
- La reorganización silenciosa. Un área nueva aparece con gasto cero en los años anteriores, porque nadie mapeó los centros viejos.
- El balance que ya no coincide. El BI muestra octubre con lo que se sabe hoy, y el balance presentado se hizo con lo que se sabía al cierre.
- El año del cambio de sistema. El tablero de cinco años muestra una caída en el año en que se cambió de sistema, porque la mitad de los clientes tiene clave nueva.
