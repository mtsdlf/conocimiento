---
resumen: >-
  Conciliar el BI es comprobar, antes de mostrar un número, que lo que llegó al BI coincide con lo
  que salió del sistema de gestión, con los reportes que el sistema emite y con el balance de sumas
  y saldos del período. Si no coincide, manda el sistema y el BI tiene que explicar la diferencia.
estado: borrador
estabilidad: estable
fuentes:
  - "Joy Mundy, Design Tip #134, Data Warehouse Testing Recommendations (Kimball Group, 2011): https://www.kimballgroup.com/2011/05/design-tip-134-data-warehouse-testing-recommendations/"
  - "Kimball Group, Audit Dimension y Error Event Schemas: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/audit-dimension/"
  - "Ralph Kimball, An Architecture for Data Quality (white paper, 2007), leído por páginas: https://www.kimballgroup.com/2007/10/white-paper-an-architecture-for-data-quality/"
  - "Bob Becker, The Subsystems of ETL Revisited (Kimball Group, 2007): https://www.kimballgroup.com/2007/10/subsystems-of-etl-revisited/"
  - "OpenStax, Principles of Accounting, Volume 1, 7.4 Prepare a Subsidiary Ledger: https://openstax.org/books/principles-financial-accounting/pages/7-4-prepare-a-subsidiary-ledger"
  - "Datos/.investigacion/bi-gestion-conciliacion-moneda.md y bi-gestion-modelado.md (2026-11-27)"
aliases: [conciliar el BI, cuadrar el BI, conciliación del data warehouse, reconciliation, tie-out, cuadre contra el mayor, totales de control, control totals, dimensión de auditoría]
creado: 2026-11-27
revisado:
---

# Conciliar el BI

Conciliar el BI es comprobar, antes de mostrar un número, que lo que llegó al BI coincide con lo que salió del sistema de gestión, con los reportes que el sistema emite y con el balance de sumas y saldos del período. Si no coincide, manda el sistema y el BI tiene que explicar la diferencia.

Es el último paso del [BI sobre el software de gestión](bi-sobre-software-de-gestion.md) antes del [tablero](../tablero.md). Los controles generales sobre un dato (completitud, unicidad, validez) están en [calidad de datos](../../Gobierno-y-calidad/calidad-de-datos.md), y el camino de cada número, en [metadatos y linaje](../../Gobierno-y-calidad/metadatos-y-linaje.md). Un sistema de gestión agrega un número oficial contra el cual comparar, y eso es lo que permite conciliar.

## Por qué el sistema manda

Un BI de gestión que no cuadra con el balance no se usa, porque la reunión discute el número en lugar de la decisión (lectura de esta base). Becker (2007) lo pone como expectativa: el almacén «is expected to provide an accurate picture of the data as it was captured by the organization's production systems». Alguien firmó y presentó el balance; el BI lo puede cortar de otras formas, pero el total tiene que ser el mismo.

## Tres niveles de cuadre

| Nivel | Contra qué | Qué compara | Qué detecta |
|---|---|---|---|
| Extracción | lo que salió del sistema | cantidad de filas e importes por tabla y por período | filas perdidas o duplicadas en la [extracción](extraer-de-un-sistema-de-gestion.md) |
| Reportes del sistema | los listados y libros que emite el sistema | el total de ventas contra el libro de IVA ventas; el saldo por antigüedad contra el listado de deudores | reglas mal copiadas: anuladas que se cuentan, signos, monedas |
| Balance | el balance de sumas y saldos del período | el saldo de cada cuenta en el BI contra el del sistema; el total de cada auxiliar contra su cuenta de control | asientos que no pasaron por los auxiliares, períodos reabiertos, cuentas mal mapeadas |

La tabla es lectura de esta base. El primer nivel tiene respaldo en Kimball: Mundy (2011) recomienda correr la misma consulta en el origen y en el almacén, y busca «row counts and amounts to match up». No se encontró un texto de Kimball que trate con nombre propio el cuadre contra el balance de sumas y saldos; el *Toolkit* tiene una sección «Period Close» en su capítulo de contabilidad que no se leyó.

El tercer nivel aplica al BI una regla que la contabilidad ya usa. OpenStax: el total del auxiliar de clientes «must agree with the balance shown in the accounts receivable general ledger account», y eso «helps us find mistakes». La conciliación del auxiliar contra su cuenta de control está en [conciliaciones](../../../Contabilidad/Control-interno/conciliaciones.md#el-auxiliar-contra-su-cuenta-de-control), y qué errores encuentra el balance de sumas y saldos, en [asiento y libros](../../../Contabilidad/Registro/asiento-y-libros.md#el-balance-de-sumas-y-saldos). En el BI, el hecho de cuentas a cobrar es el auxiliar y la foto del mayor es la cuenta de control: si no coinciden en el BI pero sí en el sistema, el error es del BI.

## Por qué no coinciden

Las diferencias tienen pocas causas, y conviene buscarlas en este orden (lectura de esta base):

1. El corte. El BI se extrajo a las seis de la mañana y el balance se emitió a las diez, con asientos cargados en el medio. Se resuelve comparando a la misma fecha de registro.
2. El filtro. El BI excluye documentos anulados que el sistema muestra con su anulación, o al revés.
3. El movimiento con fecha pasada. Un asiento de un mes ya extraído llegó después; es el caso de [los cambios que llegan después](extraer-de-un-sistema-de-gestion.md#los-cambios-que-llegan-después).
4. La moneda. El BI convirtió con su propia tabla lo que el sistema ya había convertido ([multiempresa y moneda en el BI](multiempresa-y-moneda-en-el-bi.md#dos-columnas-por-importe)).
5. El mapeo. Una cuenta nueva del plan de cuentas no está en la tabla que la lleva a un renglón del estado de resultados.
6. La dimensión vacía. El resultado por centro de costo no suma el total porque hay gastos sin centro, como avisa [reportes operativos y legales](../../../Software-de-gestion/Columnas-tecnicas/reportes-operativos-y-legales.md#las-dimensiones-existen-para-el-reporte).

En la Argentina se suma una séptima: el BI y el balance reexpresados con índices o meses de origen distintos ([BI de gestión en la Argentina](bi-de-gestion-en-argentina.md)).

## Dónde queda registrado que un número cuadró

Kimball propone dos piezas para que la calidad quede a la vista. La primera es un conjunto de filtros que prueban el dato mientras viaja: «a comprehensive system of data quality screens or filters that test the data as it flows from the source systems to the BI platform». Cada falla se guarda en un esquema de eventos de error. El *white paper* de 2007 distingue filtros de columna, de estructura y de reglas de negocio, y entre estos últimos incluye los controles de umbrales agregados.

La segunda es la dimensión de auditoría, que se pega a cada fila de hechos con lo que se sabía al cargarla: indicadores de calidad, la versión del proceso de carga y la hora de ejecución. Con ella, el BI muestra junto al número si pasó los controles.

Para un BI de gestión, en lectura de esta base, eso se traduce en una tabla chica: por período y por cuenta o total, el valor del sistema, el del BI, la diferencia y si se explicó. El tablero puede mostrar una marca en los períodos que no cuadraron. Mundy (2011) recuerda que los usuarios del negocio tienen que ayudar a definir esas pruebas («How do we know the data is correct?»), y el *white paper* de Kimball, que «relatively few data errors can be fixed in the data warehouse»: el arreglo va en el sistema, no en el BI.

## Cuándo se concilia

Cada carga concilia el primer nivel. El segundo y el tercero se concilian en el cierre de cada período, después de que el sistema lo cierra con su fecha de bloqueo y antes de que el informe de gestión salga del BI (lectura de esta base). El cierre contable, con el informe de gestión como uno de sus pasos y los días de cierre como medida, está en [del registro al balance](../../../Procesos-de-negocio/del-registro-al-balance.md). Una vez conciliado, el período queda guardado como foto de lo informado, como explica [lo que se informó y lo que es](historia-en-el-bi-de-gestion.md#lo-que-se-informó-y-lo-que-es).

> [!NOTE]
> Sin fuente todavía: un texto primario sobre el cuadre de un almacén de datos contra el balance de sumas y saldos, y una norma o manual de auditoría de sistemas sobre totales de control. El capítulo de contabilidad del *Toolkit* y el manual de la FFIEC no se pudieron leer.

## Cómo falla

- Conciliar solo filas. La cantidad de filas coincide y los importes no, porque una columna cambió de signo.
- El BI corregido a mano. Alguien ajusta el BI para que cuadre y la diferencia vuelve en la carga siguiente.
- El período que se mueve solo. Octubre cuadraba en noviembre y no cuadra en enero, porque alguien reabrió el período.
- La diferencia aceptada. Una diferencia chica que nadie explica se vuelve permanente y esconde otra más grande.
