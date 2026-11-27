---
resumen: >-
  El plan de inspección dice, para cada producto, qué características se controlan, en qué punto del recorrido, contra qué especificación, con qué método y cada cuánto. Cuando no se revisa todo, el muestreo de aceptación decide si un lote entero se acepta o se rechaza mirando una muestra.
estado: borrador
estabilidad: semi
fuentes:
  - "MIL-STD-105E, «Sampling procedures and tables for inspection by attributes», 10 de mayo de 1989, cancelada (PDF escaneado con OCR; tablas leídas en la imagen): https://everyspec.com/MIL-STD/MIL-STD-0100-0299/download.php?spec=MIL-STD-105E.011675.PDF"
  - "EverySpec, ficha de MIL-STD-105E y aviso de cancelación de 1995 que remite a ANSI/ASQC Z1.4-1993 (según el buscador): https://everyspec.com/MIL-STD/MIL-STD-0100-0299/MIL-STD-105E_11675/"
  - "ISO 2859-1:2026, ficha (según el buscador; la página da 403): https://www.iso.org/standard/2859-1"
  - "NIST/SEMATECH e-Handbook of Statistical Methods, 6.2 «Lot Acceptance Sampling» y 6.2.1: https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc2.htm y https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc21.htm"
  - "Documentación de un sistema abierto, Quality control points (v17.0): https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/quality/quality_management/quality_control_points.html"
  - "Documentación de otro sistema abierto, Quality Inspection: https://docs.frappe.io/erpnext/user/manual/en/quality-inspection"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 4.3.3: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Produccion/.investigacion/calidad.md (sección 2) y calidad-2.md (sección 1), 2026-11-27"
aliases: [plan de inspección, plan de control, inspection plan, control plan, punto de control de calidad, quality control point, inspección, inspection, inspección en proceso, in-process inspection, inspección final, final inspection, primera pieza, first article inspection, first piece, muestreo de aceptación, acceptance sampling, lot acceptance sampling, AQL, nivel de calidad aceptable, acceptable quality level, límite de calidad de aceptación, acceptance quality limit, letra código, sample size code letter, inspección normal, rigurosa y reducida, normal, tightened and reduced inspection, reglas de cambio, switching rules, MIL-STD-105E, ANSI/ASQ Z1.4, ISO 2859-1]
creado: 2026-11-27
revisado:
---

# Plan de inspección

El plan de inspección dice, para cada producto, qué características se controlan, en qué punto del recorrido, contra qué especificación, con qué método y cada cuánto. Cuando no se revisa todo, el muestreo de aceptación decide si un lote entero se acepta o se rechaza mirando una muestra.

Es la pieza de control de producto de [Calidad](calidad.md). Lo que no cumple pasa a [no conformidad](no-conformidad.md); las mediciones que se repiten alimentan el [control estadístico de procesos](control-estadistico-de-procesos.md), que vigila el proceso y no el lote. APQC 7.4 lo ubica en 4.3.3 «Perform quality testing», con cuatro actividades que el plan tiene que prever: calibrar el equipo de ensayo, ensayar según el procedimiento estándar, gestionar las muestras y registrar los resultados.

## Los cuatro puntos donde se controla

El plan nombra el momento del recorrido en que se mira cada característica. Los puntos son corte de la base; los sistemas leídos distinguen al menos la entrada, el proceso y la salida.

| Punto | Qué se mira | De quién es |
|---|---|---|
| Recepción | el material que llega del proveedor, antes de usarlo | de Inventario: [recepción](../../Inventario-y-depositos/Operacion-del-deposito/recepcion.md); el estado del material en espera, en [estados del stock](../../Inventario-y-depositos/Existencias/estados-del-stock.md) |
| Primera pieza | la primera unidad después de preparar la máquina o cambiar de producto, antes de seguir con el lote | de acá |
| En proceso | una operación de la [ruta de fabricación](../Producto-y-proceso/ruta-de-fabricacion.md), mientras corre la [orden de producción](../Ejecucion-en-planta/orden-de-produccion.md) | de acá |
| Final | el producto terminado, antes de declararlo bueno y pasarlo al depósito | de acá; la liberación es la cláusula 8.6 de ISO 9001, que mantiene el número en la edición 2026 y según una consultora no cambió (ver [Calidad](calidad.md#iso-9001-como-sistema-de-gestión)) |

La primera pieza se controla porque un error de preparación se repite en todas las unidades que siguen (criterio de la base).

> [!NOTE] Sin fuente todavía: una definición canónica de inspección de primera pieza (first article inspection) y de inspección en proceso.

## Qué dice cada línea del plan

Cada línea es una característica en un punto. Un ejemplo de la base, para una pieza torneada:

| Característica | Especificación | Método | Punto | Frecuencia | Si falla |
|---|---|---|---|---|---|
| Diámetro exterior | 20,00 ± 0,05 mm | micrómetro | primera pieza y en proceso | 5 piezas cada hora | parar la máquina y abrir no conformidad |
| Rugosidad | Ra ≤ 1,6 µm | rugosímetro | final | muestreo por lote | retener el lote |
| Rebabas | sin rebabas | visual, pasa o no pasa | final | todas las piezas | separar la pieza |

La especificación viene del plano o la ficha técnica del producto, que es de [Producto y proceso](../Producto-y-proceso/producto-y-proceso.md). La característica puede ser una variable, que se mide con un número, o un atributo, que cumple o no cumple. La diferencia importa: con variables se puede hacer un gráfico de control y calcular la capacidad; con atributos se cuenta defectuosos (criterio de la base).

En papel, el plan es una planilla por producto con estas columnas, y cada inspección, una hoja con fecha, orden, lote y lecturas.

## Cómo lo modelan dos sistemas abiertos

Los dos sistemas leídos separan el plan de su resultado.

- El punto de control como configuración. Un sistema abierto define puntos de control que disparan un chequeo: «In the Type field, specify the type of quality check that should be performed». Los tipos son instrucciones, foto, registrar producción, pasa o no pasa, medición y planilla. Se dispara por operación (fabricación, recepción), por producto o por categoría, y la frecuencia puede ser siempre, un porcentaje al azar o cada cierto período. Un mensaje para el caso de falla guía qué hacer, y puede pedir una alerta de calidad. El punto no guarda resultados.
- La inspección como registro. Otro sistema abierto guarda cada inspección con su tipo (entrante, saliente o en proceso), el documento de referencia (el recibo o la tarjeta de trabajo), el artículo, el tamaño de la muestra y una plantilla tomada de la ficha del artículo. Hay una fila de lectura por chequeo; si el chequeo es numérico y queda fuera de rango, la fila se marca rechazada sola al guardar.

## El muestreo de aceptación por atributos

El muestreo de aceptación decide sobre un lote entero a partir de una muestra. NIST lo define así: «This process is called Lot Acceptance Sampling or just Acceptance Sampling», y «In general, the decision is either to accept or reject the lot» (según el resumen del lector).

La única versión pública de la tabla es la MIL-STD-105E, una norma militar de los Estados Unidos de 1989. Está cancelada. Según el buscador, un aviso de 1995 manda a referir las compras futuras a una norma no gubernamental, la ANSI/ASQC Z1.4-1993. La base la usa por ser el texto abierto; que ANSI/ASQ Z1.4 e ISO 2859-1 desciendan de ella no está escrito en ningún texto leído, salvo el aviso de 1995. La norma vigente es la ISO 2859-1:2026. Según la ficha de ISO que mostró el buscador, es la tercera edición, se publicó en enero de 2026 y suma por primera vez procedimientos de salteo de lotes (skip-lot). Es de pago y no se leyó.

Aviso sobre las citas. La 105E se leyó en un PDF escaneado con OCR. Las citas en inglés están limpiadas solo de espacios y letras evidentes, y los números de las tablas se leyeron en la imagen de la página. Conviene recotejarlas con el PDF.

### El AQL no es un permiso para entregar defectos

La 105E define el AQL (Acceptable Quality Level) como el nivel de calidad que, «for the purposes of sampling inspection, is the limit of a satisfactory process average». Es un valor de porcentaje defectuoso, o de defectos por cien unidades, «for which lots will be accepted most of the time». La misma nota advierte: «The AQL alone does not identify the chances of accepting or rejecting individual lots or batches». Y la cláusula 4.4.2 lo cierra: «The selection or use of an AQL shall not imply that the contractor has the right to supply any defective unit of product».

El AQL es una propiedad de la serie de lotes, no de un lote. Se puede fijar uno distinto por clase de defecto (crítico, mayor, menor). La ISO 2859-1 lo llama «acceptance quality limit»; cuándo cambió el nombre no se pudo documentar.

### Nivel de inspección y letra código

La 105E da tres niveles generales y cuatro especiales: «Normally, Inspection Level II is used. However, Inspection Level I may be used when less discrimination is needed, or Level III may be used for greater discrimination». Los especiales, S-1 a S-4, sirven «where relatively small sample sizes are necessary and large sampling risks can or must be tolerated».

El tamaño del lote y el nivel dan una letra código, y la letra con el AQL ubica el plan en la tabla. La norma define el plan como el número de unidades que se inspeccionan de cada lote y «the criteria for determining the acceptability of the lot or batch (acceptance and rejection numbers)». La muestra se elige «at random without regard to their quality».

### Un plan leído en la tabla

Un lote de 2000 unidades, nivel general II y AQL 1,0 %:

1. Tabla I de la 105E: el lote cae en la fila «1201 to 3200»; con nivel II, la letra es K (con nivel I sería H; con nivel III, L).
2. Tabla II-A, muestreo simple con inspección normal: la letra K da una muestra de 125 unidades.
3. En la columna de AQL 1,0, la tabla da Ac 3, Re 4.
4. Se sacan 125 unidades al azar. Con 3 defectuosas o menos, el lote se acepta; con 4 o más, se rechaza. La regla es la 4.10.1.1: «If the number of defectives is equal to or greater than the rejection number, the lot or batch shall be rejected».

En la misma fila, AQL 0,65 da 2 y 3; AQL 1,5 da 5 y 6; AQL 2,5 da 7 y 8. Cuando la celda tiene una flecha, la tabla manda a usar el primer plan debajo o encima de ella, y si la muestra iguala o supera el lote, se inspecciona el 100 %.

Hay también planes dobles y múltiples, que según la 4.9.4 piden en promedio muestras más chicas que el simple.

### Las reglas de cambio

Las reglas de cambio son lo que presiona al proveedor o a la línea: si los lotes empeoran, la inspección se endurece. Se aplican por separado a cada clase de defecto, y siempre se empieza en normal (4.6).

| De | A | Cuándo, según la 105E |
|---|---|---|
| Normal | Rigurosa | 2 de 2, 3, 4 o 5 lotes consecutivos rechazados en la inspección original (4.7.1) |
| Rigurosa | Normal | 5 lotes consecutivos aceptados en la inspección original (4.7.2) |
| Normal | Reducida | se cumplen todas: los 10 lotes anteriores aceptados en normal; defectuosos totales dentro del límite de la Tabla VIII; producción a ritmo estable; y la reducida «is considered desirable» (4.7.3) |
| Reducida | Normal | basta una: un lote rechazado; un lote entre aceptación y rechazo; «Production becomes irregular or delayed»; u otra condición que lo justifique (4.7.4) |
| Rigurosa | Suspensión | cinco lotes no aceptados acumulados en la secuencia rigurosa; no se reanuda sin [acción correctiva](accion-correctiva.md) (4.8, parcialmente ilegible) |

La Tabla VIII, con los números límite para pasar a reducida, no se leyó. Para la teoría (la curva característica, los planes secuenciales) sirve el capítulo 6.2 de NIST, que no trae la tabla y nombra la «MIL Standard 105D», la edición anterior.

## Qué guarda un plan de inspección

- El plan, por producto y punto: característica, tipo (variable o atributo), especificación con límites y objetivo, método o instrumento, frecuencia o porcentaje, y qué hacer si falla.
- El plan de muestreo, si lo hay: nivel de inspección, AQL por clase de defecto, tipo de plan (simple, doble, múltiple) y el estado vigente (normal, rigurosa, reducida), con la historia de los últimos lotes para poder aplicar las reglas de cambio.
- Cada inspección: punto, referencia (orden de producción, operación o recibo), lote, tamaño del lote, letra código, tamaño de muestra, lecturas por característica, defectuosos encontrados, números de aceptación y rechazo, decisión, inspector y fecha.
- El equipo de medición, con su calibración vigente, porque APQC la pone como primer paso del ensayo. Su mantenimiento es de [Activos y mantenimiento](../../Activos-y-mantenimiento/activos-y-mantenimiento.md).

Un rechazo no se resuelve en la inspección: abre una [no conformidad](no-conformidad.md).
