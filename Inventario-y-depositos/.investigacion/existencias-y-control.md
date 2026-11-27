# Existencias y Control del stock: informe de investigación

Fecha de lectura: 2026-11-27. Marcas: [L] texto completo, [M] metadatos o abstract, [S] resumen secundario o del buscador. Las páginas se leyeron a través de WebFetch (un modelo chico que resume la página), así que ninguna cuenta como [L] estricta salvo donde se aclara. Puntajes 1 a 3: autoridad / profundidad / ejemplos / unicidad.

## Tabla de fuentes

| # | Fuente | URL | Tipo | Aut/Prof/Ej/Uni | Marca |
|---|---|---|---|---|---|
| 1 | DeHoratius y Raman (2008), *Inventory Record Inaccuracy: An Empirical Analysis*, Management Science 54(4), 627-641 | https://ideas.repec.org/a/inm/ormnsc/v54y2008i4p627-641.html (DOI 10.1287/mnsc.1070.0789; la página de INFORMS devolvió 403) | primaria | 3/3/2/3 | [M] abstract |
| 2 | Chicago Booth Review, «First Measure, Then Manage» (divulgación del mismo estudio) | https://www.chicagobooth.edu/review/first-measure-then-manage | secundaria (del mismo paper: no cuenta como fuente aparte) | 2/1/2/1 | [S] |
| 3 | Microsoft Learn, Inventory Visibility: on-hand change schedule y ATP | https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-available-to-promise | primaria (documentación de práctica en software) | 2/3/3/2 | [L] con ejemplo numérico completo |
| 4 | Odoo, Cycle counts (v17) | https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/cycle_counts.html | primaria (práctica) | 2/1/1/1 | [S] |
| 5 | Odoo, Lots (v17) | https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/product_management/product_tracking/lots.html | primaria (práctica) | 2/1/1/1 | [S] |
| 6 | Frappe/ERPNext, Stock Reconciliation | https://docs.frappe.io/erpnext/user/manual/en/stock-reconciliation | primaria (práctica) | 2/1/1/1 | [S] |
| 7 | Frappe/ERPNext, Serial No | https://docs.frappe.io/erpnext/user/manual/en/serial-no | primaria (práctica) | 2/1/1/1 | [S] |
| 8 | Wikipedia, Cycle count | https://en.wikipedia.org/wiki/Cycle_count | secundaria | 1/2/1/1 | [S] |
| 9 | Odoo, Inventory valuation (v19), periódico frente a permanente | https://www.odoo.com/documentation/19.0/applications/finance/accounting/get_started/inventory_valuation.html | primaria (práctica) | 2/1/1/1 | [S] del buscador (no abierta) |
| 10 | NRF, National Retail Security Survey 2023 (vía LPRC y prensa) | https://nrf.com/research/national-retail-security-survey-2023 ; https://lpresearch.org/2023-nrss-release-9-26-23/ | primaria (encuesta) accedida por secundarias | 2/2/1/2 | [S] del buscador |
| 11 | Extracto CPIM ya bajado (ATP discreto) | /tmp/claude-1000/-home-dela-repos-personal-conocimiento/8f0c0cb6-2f82-41a4-8ebf-4fbe94e03c21/scratchpad/inv/cpim.txt | primaria (certificación ASCM) | 3/2/3/2 | [L] |

No se pudo abrir: APICS Dictionary (entradas de cycle counting, lot, serial number, ATP, inventory record accuracy), los libros de texto (Silver-Pyke-Thomas, Nahmias, Bartholdi-Hackman, Frazelle, Muller, Wild), el texto del paper en INFORMS, Dynamics 365 sobre estados de inventario, SAP EWM, y la página de Oracle sobre cycle counting (la URL devolvió la portada). Ver huecos.

## Componente 1: Existencias

### Artículo, unidad de medida
- Hueco: no hay fuente leída sobre ítem, SKU, unidad de medida y conversión, ni sobre stockeable frente a servicio o consumible. Se espera encontrarlo en el APICS Dictionary y en la documentación de ERPNext (Item) y Odoo (Units of measure). Para el modelo Shopify ya existe Comercio-electronico/Operaciones-del-comercio/catalogo-y-stock.md.

### Lote y número de serie
- Un lote agrupa lo que se recibió, almacenó, envió o fabricó junto, para rastrearlo como grupo: «Lots are one of the two ways to identify and track products in Odoo» y sirven «particularly for product recalls or expiration dates». [5] https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/product_management/product_tracking/lots.html
- El lote elegido para una entrega depende de la estrategia de salida: «(FIFO, LIFO, or FEFO)». La página no explica cada una. [5]
- Un artículo serializado tiene un registro único por unidad, con garantía y vencimiento, estado actual, y vínculo con el proveedor, el cliente y el documento de origen; solo una unidad «Available» se puede entregar. [7] https://docs.frappe.io/erpnext/user/manual/en/serial-no
- Hay una fuente de práctica por lado (Odoo y ERPNext, independientes entre sí) y ninguna de definición; las definiciones canónicas (lote frente a serie, FEFO) quedan sin cubrir.

### Estados del stock
- Evidencia de que la práctica separa cantidades por estado: la fórmula de disponible de Dynamics suma como oferta «PhysicalInvent + OnHand + Unrestricted + QualityInspection + Inbound» y resta como demanda «ReservPhysical + SoftReservePhysical + Outbound». Muestra que calidad en inspección, reserva blanda y reserva física son cantidades distintas y que qué se incluye es una decisión de configuración («The default ATP calculated formula is for reference»). [3]
- Hueco: nada leído sobre en tránsito, bloqueado, consignación ni cuarentena como definición.

### Disponible para prometer (ATP) como cálculo
- Dos fuentes con enfoques distintos; conviene presentar las dos.
- Método discreto (CPIM): «First Period ATP = Beginning Inventory − [pedidos de cliente]», ejemplo «70 units − 48 units = 22 units»; períodos con MPS: «ATP for Periods Containing MPS = Scheduled MPS Receipt − Sum of Customer Orders Before the next MPS»; ejemplo «100 units − 66 units = 34 units». Regla adicional: si el ATP de un período da negativo, se resta del ATP del período anterior y se suma al negativo (ejemplo semana 3: 100 − (57 + 62) = −19; semana 2 queda 100 − 66 − 19 = 15; semana 3 queda 0). [11] cpim.txt, líneas 118-206.
- Variante con ventana hacia adelante (Dynamics): «ATP quantity – The minimum projected on-hand quantity that's available from the specified date through the end of the schedule period... It's the maximum quantity that can be promised on the current date». Ejemplo literal: on-hand 20, demanda programada 3 hoy, oferta 10 el 3 de febrero, demanda 15 el 4 de febrero, oferta 1 el 5 y 3 el 6: ATP del 1 al 4 de febrero = 12 (el mínimo del proyectado: 17, 17, 27, 12), el 5 = 13, el 6 = 16. Y si la oferta de 10 programada para el 3 no llega, el ATP del 4 cae a 2. [3]
- Esa segunda forma coincide con el método acumulado de la literatura (mínimo de lo proyectado hacia adelante), pero acá solo se confirma por [3], no por una fuente de libro. Hallazgo de una sola fuente.
- Diferencia a notar: el ATP de [11] parte de un plan maestro (producción); el de [3] parte de existencias más programación de entradas y salidas de un depósito. Para un tema agnóstico, el cálculo común es oferta confirmada menos demanda comprometida, sin descontar dos veces. La fecha prometida ya está en Relacion-con-clientes/Pedido-de-venta/fecha-prometida.md.

### Recurso canónico
- ATP: [11] (CPIM, módulo de planificación maestra), parte «Calculating Available-to-Promise»: fijarse en la regla de arrastre del negativo; complementar con [3] por el ejemplo de la oferta que se atrasa.
- Lote, serie, FEFO y estados: sin recurso canónico confirmado; proponer el APICS Dictionary y el CPIM (módulo de inventario) para verificar.

## Componente 2: Control del stock

### Exactitud de los registros: cuán mal anda en la realidad
- En 37 tiendas de un minorista, con casi 370.000 registros, 65 % de los registros eran inexactos (abstract, parafraseado por el lector; la única cita literal obtenida es «Traditional inventory models, with a few exceptions, do not account for the existence of inventory record inaccuracy»). La auditoría reduce el error; la complejidad del local y la estructura de distribución lo aumentan; 26,4 % de la varianza está entre categorías y 2,7 % entre tiendas. [1] https://ideas.repec.org/a/inm/ormnsc/v54y2008i4p627-641.html
- Discrepancia de cifras entre lecturas del mismo estudio: [2] habla de «nearly 240,000 items across 37 stores» con registros distintos del físico y de una caída de ganancias de más del 10 por ciento; [1] habla de casi 370.000 registros. Probablemente son universos distintos (registros evaluados frente a ítems con diferencia), pero no se pudo verificar en el texto completo. https://www.chicagobooth.edu/review/first-measure-then-manage
- Causas citadas en [2]: errores de escaneo en caja, devoluciones y cambios mal tratados, envíos erróneos desde el centro de distribución, mercadería que llega sin inspeccionar, mayor variedad de producto y locales saturados; los envíos directos del proveedor tuvieron registros más exactos que los del centro de distribución del propio minorista. Es un solo estudio y un solo minorista de EE.UU.; no generalizar el 65 %.

### Inventario permanente frente a periódico
- La documentación de Odoo los trata como regla contable: el periódico actualiza el valor del inventario solo al cierre; el permanente, a medida que ocurren las transacciones; el periódico se asocia a la norma continental y el permanente a la anglosajona. [9] https://www.odoo.com/documentation/19.0/applications/finance/accounting/get_started/inventory_valuation.html (solo vía buscador).
- Cuidado con la frontera: eso es valuación (Contabilidad). Lo que le toca a este tema es la regla de negocio de cuándo se actualiza la cantidad (al instante frente a en el conteo). Sin fuente de libro leída; la definición de «perpetual inventory» del APICS Dictionary queda como hueco.

### Conteo físico y cíclico
- Cycle count: «a perpetual inventory audit in which a small subset of stock is counted repeatedly on a set schedule» (paráfrasis del lector); no frena la operación; la mayoría de las implementaciones usan ABC por el método Pareto, y los ítems de mayor valor se cuentan más seguido; el conteo mal hecho introduce errores (varias ubicaciones por ítem, trabajo en curso, demoras de papeles). [8] https://en.wikipedia.org/wiki/Cycle_count (secundaria).
- Práctica en software: Odoo permite fijar por ubicación una frecuencia en días (por defecto 0), con conteo completo anual por defecto al 31 de diciembre; una vez aplicados los ajustes de un conteo se programa el siguiente. [4] https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/cycle_counts.html Nota: Odoo cuenta por ubicación, no por clase ABC. Hay dos diseños en la práctica (por clase y por lugar).
- Una guía de proveedor citada por el buscador da A semanal o mensual, B trimestral, C anual, y 98-99 % de exactitud como meta «world-class» (resumen del buscador, sin URL abierta; no usar sin fuente mejor).
- Frecuencias, tolerancias y meta de exactitud: ninguna fuente primaria leída. Hueco importante.

### Ajustes y mermas
- ERPNext: la reconciliación de stock es «the process of counting and evaluating material/products, periodically at the year-end»; se cambia la cantidad al valor contado y al validar la diferencia se asienta contra una cuenta de diferencia, por defecto «Stock Adjustment» (y «Temporary Opening» para stock inicial). [6] https://docs.frappe.io/erpnext/user/manual/en/stock-reconciliation
- Composición de la merma en comercio minorista de EE.UU. (NRSS 2023, ejercicio 2022): tasa promedio 1,6 % (1,4 % el año anterior); hurto externo 36,15 %, hurto interno 28,85 %, errores administrativos o de proceso 27,29 %, desconocido 6 %, otros 1 %. [10] https://lpresearch.org/2023-nrss-release-9-26-23/ y https://nrf.com/research/national-retail-security-survey-2023. Cifras vía resumen del buscador; es retail, no depósito general; en Argentina no hay equivalente verificado. Los decimales difieren entre fuentes (la prensa redondea).
- Hueco: separación de funciones, aprobación de ajustes y umbrales. Sin fuente leída. Es regla de control interno (Contabilidad/auditoría); marcar la frontera.

### Recurso canónico
- Exactitud y por qué importa: [1] DeHoratius y Raman (2008), el abstract y el modelo de factores; para el texto completo hay que pedirlo por el DOI o una biblioteca.
- Conteo cíclico: sin recurso canónico confirmado; proponer APICS Dictionary (cycle counting, inventory record accuracy) y el CPIM de inventario; como lectura abierta, Bartholdi y Hackman (warehouse-science.com) para conteo en depósito (no verificado).

## ¿El árbol coincide con cómo el campo divide esto?
Probablemente sí en lo grueso. Dos ajustes a considerar:
1. «Estados del stock» y «ATP» se cruzan: lo que cuenta como comprometido es una decisión de configuración (ver [3]); conviene definir los estados en Existencias y que el cálculo de ATP cite esa lista.
2. Permanente frente a periódico figura en la práctica de software como método de valuación contable [9], no de control de cantidad. Para este tema solo vale como regla de cuándo se actualiza la cantidad; el resto es de Contabilidad.

## Huecos
- APICS Dictionary completo (nada abierto): definiciones de cycle counting, lot, serial number, ATP discreto y acumulado, inventory record accuracy.
- Texto completo de DeHoratius y Raman (403); ahí están los hallazgos sobre auditoría y las cifras exactas.
- Ningún libro de texto leído: Silver-Pyke-Thomas y Bartholdi-Hackman para ABC y conteo.
- ATP acumulado: sin fuente de libro, solo la variante de [3].
- Estados en tránsito, bloqueado, consignación, cuarentena: sin definición leída.
- Frecuencias de conteo, tolerancias, metas de exactitud, aprobación y separación de funciones: sin fuente primaria.
- Unidad de medida y conversión, servicio frente a artículo con stock.
- Sin cobertura de Argentina en este ángulo (la norma es otro componente).
