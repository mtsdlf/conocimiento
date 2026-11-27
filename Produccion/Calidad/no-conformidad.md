---
resumen: >-
  Una no conformidad es el incumplimiento de un requisito especificado por una característica del producto. Tratarla es registrarla, apartar lo que no cumple para que nadie lo use por error y decidir qué se hace con eso: reprocesar, reparar, usar como está con autorización, desechar o devolver al proveedor.
estado: borrador
estabilidad: estable
fuentes:
  - "MIL-STD-1520C, «Corrective Action and Disposition System for Nonconforming Material», 27 de junio de 1986, cancelada (PDF escaneado con OCR), 3.5 a 3.15, 4.5 y 5.2 a 5.4: https://everyspec.com/MIL-STD/MIL-STD-1500-1599/download.php?spec=MIL_STD_1520C.1489.pdf"
  - "EverySpec, ficha de MIL-STD-1520C (estado cancelado; retiro y reemplazo según el buscador): https://everyspec.com/MIL-STD/MIL-STD-1500-1599/MIL_STD_1520C_1489/"
  - "NSAI, presentación «Overview 9001:2015» (23 de septiembre de 2015), diapositiva sobre 8.7: https://www.nsai.ie/download/certification/Overview-9001-2015-presentation-23-Sep-15-Web-Compatibility-Mode.pdf"
  - "ISMS.online, cláusula 8.7 de ISO 9001 (consultora; según el buscador): https://www.isms.online/iso-9001/clause-8-7-control-of-nonconforming-outputs"
  - "iso-9001-checklist.co.uk, 8.7 Control of nonconforming process outputs (consultora; según el lector): https://www.iso-9001-checklist.co.uk/8.7-control-of-nonconforming-process-outputs-products-and-services.htm"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 4.3.2.4 y 4.3.3.5: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Produccion/.investigacion/calidad.md (secciones 1 y 4) y calidad-2.md (secciones 2 y 5), 2026-11-27"
aliases: [no conformidad, nonconformity, nonconformance, NC, producto no conforme, nonconforming product, salida no conforme, nonconforming output, material no conforme, nonconforming material, disposición, disposition, reproceso, retrabajo, rework, reparación, repair, usar como está, use as is, use-as-is, concesión, concession, desviación, waiver, desecho, descarte, scrap, devolución al proveedor, return to supplier, comité de revisión de material, material review board, MRB, revisión preliminar, preliminary review, retención, hold, segregación, segregation, contención, containment]
creado: 2026-11-27
revisado:
---

# No conformidad

Una no conformidad es el incumplimiento de un requisito especificado por una característica del producto. Tratarla es registrarla, apartar lo que no cumple para que nadie lo use por error y decidir qué se hace con eso: reprocesar, reparar, usar como está con autorización, desechar o devolver al proveedor.

Dentro de [Calidad](calidad.md), es lo que pasa después de que una inspección del [plan de inspección](plan-de-inspeccion.md) o una señal del [control estadístico de procesos](control-estadistico-de-procesos.md) encuentra algo mal. Resuelve las piezas; la causa la ataca la [acción correctiva](accion-correctiva.md). APQC 7.4 la reparte en dos procesos: 4.3.2.4 «Rerun defective items», dentro de producir, y 4.3.3.5 «Track and analyze non-conformance trends», dentro de probar la calidad.

## La definición que sirve para un sistema

La norma abierta más clara es la MIL-STD-1520C, de 1986, una norma militar de los Estados Unidos para el material no conforme de los contratistas. Está cancelada, y la base la usa por sus definiciones; según el buscador, se retiró en 1995 y remite a SAE AS7106/2B. Se leyó en un PDF escaneado con OCR: las citas en inglés conviene recotejarlas.

La norma define la no conformidad (3.6) como «The failure of a characteristic to conform to the requirements specified in the contract, drawings, specifications, or other approved product description». El material no conforme (3.7) es cualquier ítem o producto «containing one or more nonconformances».

Las clasifica en dos grupos. La menor no afecta la salud o la seguridad, el desempeño, la intercambiabilidad, la confiabilidad o el mantenimiento, el uso efectivo, ni el peso o la apariencia cuando importan. La mayor o crítica es la que no es menor y «cannot be completely eliminated by rework or reduced to a minor nonconformance by repair». Y avisa: «Multiple minor nonconformances, when considered collectively, may raise the category to a major/critical nonconformance».

## Registrar y apartar antes de decidir

El primer paso es que lo malo no siga camino. ISO 9001:2015, en la cláusula 8.7.1, pide según una consultora que las salidas que no cumplen «are identified and controlled to prevent their unintended use or delivery». El texto de la norma no se leyó: es de pago.

Apartar tiene dos lados. En la línea, se separan las piezas o se detiene la [orden de producción](../Ejecucion-en-planta/orden-de-produccion.md); los rechazos se declaran como cantidad rechazada en [consumo y declaración](../Ejecucion-en-planta/consumo-y-declaracion.md). En el depósito, lo que ya entró pasa a un estado que no se puede usar. Ese estado (cuarentena o bloqueado) es de Inventario y está en [estados del stock](../../Inventario-y-depositos/Existencias/estados-del-stock.md); acá se decide cuándo se levanta.

Si el problema puede estar en otros lotes, la [trazabilidad de lotes](trazabilidad-de-lotes.md) dice cuáles llevan el mismo componente o salieron de la misma orden, y también se apartan (criterio de la base).

## Las disposiciones posibles

La disposición es la decisión sobre el material no conforme. Las definiciones literales son de la 1520C:

| Disposición | Definición en la 1520C | Qué queda |
|---|---|---|
| Reprocesar (rework) | «A procedure applied to a nonconformance that will completely eliminate it and result in a characteristic that conforms completely» (3.13) | una pieza conforme |
| Reparar (repair) | reduce la no conformidad «but not completely eliminates»; «the characteristic after repair still does not completely conform» (3.12) | una pieza que sigue sin cumplir del todo, pero usable |
| Usar como está (use as is) | no tiene definición propia; es una disposición que necesita aprobación por encima del contratista (5.3 y 5.4) | la pieza tal cual, con autorización |
| Desechar (scrap) | material «not usable for its intended purpose» que no se puede reprocesar ni reparar de manera económica o aceptable (3.14) | una baja |
| Devolver al proveedor | una disposición de la revisión preliminar (5.2) | un reclamo al proveedor |

La diferencia entre reprocesar y reparar es la que más pesa: después de reprocesar la pieza cumple; después de reparar, no del todo. Por eso la reparación pide una autoridad que acepte el desvío, y el reproceso no. La 1520C prevé además un procedimiento estándar de reparación (3.15), una técnica documentada para un tipo de no conformidad, con fecha de vencimiento o un tope de aplicaciones.

Reclasificar, es decir, aceptar la pieza como un producto de menor grado o con otro destino, no aparece en las fuentes leídas.

> [!NOTE] Sin fuente todavía: la reclasificación como disposición, y una lista de disposiciones de una norma vigente.

La devolución al proveedor sigue en Compras, en [diferencias y devoluciones](../../Compras-y-abastecimiento/Seguimiento-de-la-orden/diferencias-y-devoluciones.md), y cuenta en su [evaluación](../../Compras-y-abastecimiento/Proveedores/evaluacion-de-proveedores.md). El material y las horas del desecho y del reproceso quedan registrados en la orden, de donde sale el [costo real de la orden](../Costos-de-produccion/costo-real-de-la-orden.md). Si ese costo queda en la orden, va a la carga fabril o es pérdida del período lo decide [Costos de producción](../Costos-de-produccion/costos-de-produccion.md#mermas-rechazos-y-reproceso-normal-frente-a-anormal).

## Quién decide: revisión preliminar y comité

La 1520C decide en dos niveles. Primero, una revisión preliminar del personal de calidad (3.10) puede disponer sola los casos obvios (5.2): desechar lo que «is obviously unfit for use», reprocesar lo que se elimina con reproceso, devolver al proveedor o reparar con un procedimiento estándar ya aprobado. Lo demás va al comité.

El comité de revisión de material (MRB) es, según 3.5, «A board consisting of representatives of contractor departments necessary to review, evaluate, and determine or recommend disposition of nonconforming material referred to it». Lo preside alguien de calidad y, como mínimo, incluye a un representante de la ingeniería responsable del diseño (4.5). Sus disposiciones son desechar, reprocesar, devolver al proveedor, reparar con un procedimiento estándar, o recomendar al cliente una reparación distinta, el uso como está o una desviación (5.3).

El uso como está tiene un candado: el comité lo revisa y lo aprueba el cliente, y hasta entonces el material «shall not be further processed nor used» (4.5.1 y 5.4). La revisión preliminar tampoco libera de nada: «PR action does not negate the requirement for identification, documentation, and corrective action».

En una fábrica chica, el comité puede ser el jefe de calidad y el de ingeniería en una reunión semanal, con una planilla de no conformidades abiertas (criterio de la base).

## La concesión en ISO 9001

ISO 9001 llama concesión a la autorización para aceptar algo que no cumple. Según la lectura de la base, es lo mismo que el uso como está de la 1520C, pero en una empresa sin un cliente que apruebe la autorización es interna y queda registrada.

> [!IMPORTANT] Las fuentes secundarias no coinciden sobre el texto de 8.7. Las consultoras listan cuatro acciones para la salida no conforme: corrección; segregación, contención, devolución o suspensión; informar al cliente; y obtener la autorización para aceptarla bajo concesión. La presentación de NSAI, un organismo de normalización, lista la segregación, la contención, la devolución o suspensión, informar al cliente y «authorise re-provision of the products and services», sin mencionar la concesión. No se pudo dirimir cuál es el texto de la norma.

Las dos lecturas coinciden en qué se guarda. Según una fuente secundaria, 8.7.2 pide información documentada que «describes the nonconformity», «describes the actions taken», «describes the concessions obtained» e «identifies the authority deciding the action». NSAI agrega que la edición 2015 no exige un procedimiento documentado, pero sí esa información. La numeración es la de 2015; en la edición 2026 no se verificó.

## Cuándo una no conformidad abre una acción correctiva

No toda no conformidad necesita una acción correctiva: una pieza mal sujeta en la máquina se reprocesa y listo. La acción se abre cuando el defecto se repite, cuando es mayor o crítico, o cuando llega del cliente (criterio de la base). Para eso sirve el proceso 4.3.3.5 de APQC, el seguimiento de las tendencias de no conformidad: sin registro, nadie ve que es la quinta vez.

El reclamo del cliente entra por [Servicio al cliente](../../Servicio-al-cliente/Caso/reclamo.md); cuando se confirma un defecto del producto, se abre acá la no conformidad.

## Qué guarda una no conformidad

- Qué: artículo, lote, orden de producción u operación, cantidad afectada, característica que falla y valor encontrado.
- Dónde y quién: punto de detección (recepción, en proceso, final, cliente), quién la detectó y cuándo.
- Clasificación: menor, mayor o crítica.
- Contención: qué se apartó, en qué estado quedó el stock y qué otros lotes se revisaron.
- Disposición: cuál, por cantidad (puede haber 80 reprocesadas y 20 desechadas), si la decidió la revisión preliminar o el comité, quién la autorizó y si hizo falta la aprobación del cliente.
- Concesión o desviación, con su alcance y vencimiento.
- Costo del reproceso, la reparación o el desecho.
- Estado: abierta, retenida, en disposición, cerrada.
- Vínculo con la [acción correctiva](accion-correctiva.md), si se abrió.
