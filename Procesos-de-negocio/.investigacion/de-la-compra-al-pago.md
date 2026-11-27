# Informe crudo: de la compra al pago (procure-to-pay)

Sesión 13 de 16 (issue #120), 2026-11-27. Ángulo: el recorrido de la necesidad al pago conciliado, cruzando Compras, Inventario, Contabilidad, Tesorería e Impuestos. Límites de #98 y #99: Compras termina cuando lo recibido coincide con lo pedido; Inventario cuenta y ubica; la factura, el cruce y la cuenta a pagar son de Contabilidad; el pago, de Tesorería.

Marcas: [L] texto completo leído; [M] metadatos, resumen o parte; [S] resumen secundario o del buscador.

## 1. Lo que ya dicen los temas de dominio (leído entero, [L])

| Nota | Lo que aporta al recorrido | Término que usa |
|---|---|---|
| `Compras-y-abastecimiento/Orden-de-compra/solicitud-de-compra.md` | Primer documento; aprobación por quien responde por el gasto; la compra fuera del circuito (APQC: peor desempeño «2.5 percent or more of their total purchases»; «16 hours more to issue a purchase order»; USD 2,58 más por cada USD 1.000, según el resumen del artículo de APQC de 2019); «no PO, no pay»; tarjeta de compra (GAO-08-333) | solicitud de compra; compra fuera del circuito (maverick spending) |
| `Compras-y-abastecimiento/Orden-de-compra/tipos-de-orden.md` | Orden puntual, orden abierta, orden contra contrato, orden de servicios con hoja de aceptación de servicios («before the vendor can send an invoice, you need to accept the service», según el resumen de la documentación de un ERP grande), consignación | hoja de aceptación de servicios; orden contra contrato |
| `Compras-y-abastecimiento/Seguimiento-de-la-orden/recepcion-contra-lo-pedido.md` | Compras compara el conteo de Inventario con la orden; tolerancia de recepción; saldo pendiente; cerrar el renglón; APQC 4.2.3.6 | recepción contra lo pedido; tolerancia de recepción; saldo pendiente |
| `Compras-y-abastecimiento/Seguimiento-de-la-orden/diferencias-y-devoluciones.md` | Faltante, sobrante, rechazo; devolución al proveedor; nota de débito del comprador y nota de crédito del proveedor; «rechazar no es devolver» | devolución al proveedor; nota de débito |
| `Inventario-y-depositos/Operacion-del-deposito/recepcion.md` | Descargar, contar, inspeccionar, decidir estado, guardar; APQC 4.4.3.2; Bartholdi y Hackman: la recepción dispara el pago al proveedor | recepción; cuarentena |
| `Produccion/Calidad/plan-de-inspeccion.md` | La inspección de recepción es uno de los cuatro puntos de control | plan de inspección |
| `Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md` | Cuenta a pagar; cruce de tres vías con tolerancia; factura retenida; recepciones no facturadas; asientos de OpenStax 6.3 | cruce de tres vías; recepciones no facturadas (recibido sin facturar) |
| `Contabilidad/Control-interno/separacion-de-funciones.md`, `autorizaciones.md`, `conciliaciones.md` | Quién no puede hacer dos pasos; matriz de aprobación; conciliación bancaria | separación de funciones; matriz de autorizaciones |
| `Contabilidad/Operaciones/gastos-y-rendiciones.md` | Fondo fijo (caja chica), reintegro, anticipo a rendir | fondo fijo; rendición |
| `Tesoreria/Pagos-a-proveedores/*.md` | Programar, correr, cuidar; corrida de pagos en siete pasos (síntesis de esa base); APQC 9.6.1.4, 9.6.1.8, 9.7.2.3, 9.6.1.1; correo comprometido (FBI 2025: USD 3.046.598.558) | programación de pagos; corrida de pagos; descuento por pronto pago |
| `Tesoreria/Caja-y-liquidez/capital-de-trabajo.md` | Días de pago (payables deferral period, DPO): costo de ventas ÷ cuentas a pagar promedio | días de pago |
| `Compras-y-abastecimiento/Fundamentos/fundamentos-de-compras-y-abastecimiento.md` | Costo por orden de compra: USD 14 a USD 54,50 entre percentiles 25 y 75 (APQC, según buscador) | costo por orden de compra |

Conclusión de términos: la base dice «cruce de tres vías» (no «control de tres vías»), «hoja de aceptación de servicios» (no «certificado de servicio»), «compra fuera del circuito» para maverick spending, «días de pago» para DPO, «corrida de pagos» y «programación de pagos». La nota de proceso usa esos términos y pone los otros como alias.

## 2. Códigos APQC PCF 7.4 (leído en el texto bajado, [L])

URL: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf

- 4.2.3 «Order materials and services»: 4.2.3.1 «Process/Review requisitions»; 4.2.3.2 «Approve requisitions»; 4.2.3.3 «Solicit supplier quotes»; 4.2.3.4 «Create/Distribute purchase orders»; 4.2.3.5 «Expedite orders and satisfy inquiries»; 4.2.3.6 «Reconcile purchase orders»; 4.2.3.7 «Research/Resolve order exceptions».
- 4.2.1 «Provide sourcing governance and perform category management» y 4.2.2 «Select suppliers and develop/maintain contracts»: lo que suma el source-to-pay.
- 4.4.3.2 «Receive, inspect, and store inbound deliveries» (citado por Inventario).
- 9.6.1 «Process accounts payable (AP)»: 9.6.1.1 «Verify AP pay file with purchase order vendor master file»; 9.6.1.3 «Audit invoices and key data in AP system»; 9.6.1.4 «Approve payments»; 9.6.1.5 «Process financial accruals and reversals»; 9.6.1.6 «Process payables taxes»; 9.6.1.7 «Research/Resolve payable exceptions»; 9.6.1.8 «Process payments».
- 9.6.2 «Process expense reimbursements»; 9.6.3 «Manage corporate credit cards».
- 9.7.2.3 «Process and oversee electronic fund transfers».

El PCF Cross Industry 7.4 no tiene un proceso «procure-to-pay»: el recorrido se arma con piezas de 4.2, 4.4 y 9.6–9.7 (consistente con el ALCANCE).

## 3. Fuentes nuevas

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| APQC, medida «Cycle time in days from receipt of invoice until payment is transmitted» | https://www.apqc.org/resources/benchmarking/open-standards-benchmarking/measures/cycle-time-days-receipt-invoice-until | primaria | 3/1/1/3 | [S] (403; resumen del buscador) |
| APQC, medida «Percentage of invoice line items that are matched the first time» | https://www.apqc.org/resources/benchmarking/open-standards-benchmarking/measures/percentage-invoice-line-items-are | primaria | 3/1/1/3 | [S] (403; solo título por buscador) |
| Wiggins (APQC), «Hidden delays that slow payments and strain cash flow», CFO.com, 3-dic-2025 | https://www.cfo.com/news/hidden-delays-that-slow-payments-and-strain-cash-flow-metric-of-the-month/806681/ | secundaria con datos de APQC | 2/2/2/3 | [L] |
| Wiggins (APQC), métrica «cycle time to approve and schedule a payment for AP», CFO.com, 3-ago-2022 | https://www.cfo.com/technology/payments/2022/08/accounts-payable-process-invoice-payment-apqc | secundaria con datos de APQC | 2/2/2/2 | [L] |
| Oracle Payables, «Two-, Three-, and Four-way Matching» (documentación de proveedor) | https://docs.oracle.com/cd/A60725_05/html/comnls/us/ap/point04.htm | práctica de proveedor | 2/2/2/3 | [L] |
| GAO, AIMD-95-68R (23-ene-1995), pagar sin factura | https://gao.gov/products/aimd-95-68r | primaria (auditoría pública) | 3/1/1/2 | [M] (resumen oficial) |
| Curso de sistemas de información contable, Bradley University, unidad «Expenditure Cycle» | https://personalpages.bradley.edu/~simonp/atg383/expenditure/expenditure.html | apuntes de curso | 2/1/1/2 | [L] |
| Romney, Steinbart y otros, Accounting Information Systems, capítulo del ciclo de egresos | https://pearson.com/en-au/media/2628245/9781292353364-toc.PDF | libro de texto | 3/–/–/3 | [S] (índice y resúmenes de terceros) |
| APQC, Open Standards Benchmarking Measure List (16/11/2013), 203 páginas | https://www.apqc.org/sites/default/files/APQC%20Benchmarking%20Measures%20List.pdf | primaria | 3/2/1/3 | [L] (bajado con curl y leído por búsqueda en las secciones de cuentas a pagar, compras y activos fijos) |
| IBM, «What is source to pay (S2P)?» | https://www.ibm.com/think/topics/source-to-pay | práctica de proveedor | 1/1/1/2 | [L] |

## 4. Afirmaciones

### Definición y bordes
- Source-to-pay es «an integrated procurement process that connects procurement activities from start to finish», que suma abastecimiento y gestión de contratos; «P2P is a subset of S2P and focuses exclusively on the operational aspects of purchasing». IBM [L]. Fuente de proveedor; ninguna fuente de CIPS o APQC apareció con la distinción. En la base, lo que suma S2P es la vertical Abastecimiento estratégico (APQC 4.2.1 y 4.2.2).
- Los libros de sistemas de información contable cuentan el recorrido como «ciclo de egresos» (expenditure cycle). Un curso de Bradley lo lista como «identifying a need», «issuing a purchase order», «receiving the goods», «establishing a payable» y «making payment for the goods» [L]. Romney y Steinbart lo dividen en tres, cuatro o cinco actividades según la edición (pedir, recibir, aprobar la factura del proveedor, pagar) [S]; no se leyó el capítulo.
- El mismo curso da el control: «Invoice should be compared to PR, PO, and RR to be sure that goods requisitioned, ordered, and received» [L]. Es una fuente académica (apuntes) para el cruce que Contabilidad dejó «sin fuente todavía» (ver huecos).

### Cruce de dos, tres y cuatro vías
- Oracle [L]: «2-way matching verifies that purchase order and invoice information match within your tolerances»: cantidad facturada ≤ cantidad pedida y precio de factura ≤ precio de la orden. «3-way matching adds a third criterion»: cantidad facturada ≤ cantidad recibida. «4-way matching adds a fourth criterion»: cantidad facturada ≤ cantidad aceptada (en la inspección). El nivel se elige por proveedor, sitio y renglón de entrega de la orden.
- Para servicios, la factura se controla contra la hoja de aceptación de servicios (tipos-de-orden.md, fuente de un ERP grande según resumen). Que eso equivale a la tercera vía es lectura de la base.
- GAO AIMD-95-68R [M]: se puede autorizar un pago sin factura si hay controles; entre los esenciales, «matching the types and quantities of goods received with those of the purchase order or contract» y evitar pagos duplicados y anticipados.

### Dónde se traba
- APQC por Wiggins (2025) [L]: causas de demora entre la factura y el pago: facturas mal dirigidas; facturas con «wrong tax treatment, incorrect pricing or mismatched quantities» que no avanzan hasta corregirse; y demora deliberada por manejo de caja, que «reflects strategy, not inefficiency».
- APQC por Wiggins (2022) [L]: facturas que llegan tarde a cuentas a pagar, facturas sin imputación (centro, ubicación), facturas que «still require approval», sistemas viejos.
- Bartholdi y Hackman (vía Inventario): una recepción mal registrada hace pagar lo que no llegó [inferencia de esa base].
- Compra fuera del circuito: no hay orden contra la cual cruzar la factura (solicitud-de-compra.md, criterio de esa base).
- Rechazo sin devolución: la deuda no baja (diferencias-y-devoluciones.md, inferencia de esa base).
- Pago a cuenta cambiada por correo comprometido; pago duplicado (seguridad-de-los-pagos.md).
- Factura que llega antes que la mercadería, o mercadería sin factura: recepciones no facturadas (compras-y-cuentas-a-pagar.md).

### Medidas
- APQC Measure List 2013 [L], literal: 103094 «Procure to pay cycle time in days» = «[Time in days required to pay suppliers from purchase order placement until payment complete]». 100639 «Cycle time in hours to place a purchase order» = «[Cycle time in hours from the receipt of a purchase requisition line item to the purchase order's transmission to the vendor/contractor]». 100575 «Cycle time in days from receipt of invoice until payment is transmitted» = «[Cycle time in calendar days from receipt of an invoice until payment is transmitted]». 100632 «Cycle time in days to resolve an invoice error». 102149 «Percentage of invoice line items that are matched the first time» = «([Number of invoice line items that are matched the first time] / [Number of invoice line items processed]) * 100». 102136 «Percentage of invoice line items matched with a purchase order». 100451 «Total cost to perform the process "process accounts payable" per invoice processed». 101947 «Percentage of discounts available that are taken». 102139 «Percentage of invoice line items paid on time». 104004 «Total cost to perform the procurement process group per purchase order». La lista no trae valores.
- Tiempo de la solicitud al pago = 100639 + 103094: criterio de la base.
- Tiempo de la factura al pago: APQC «cycle time in days from receipt of invoice until payment is transmitted»: percentil 25, 12 días; mediana, 15; cuartil superior, 24 (Wiggins 2025 [L]). Wiggins la distingue de los días de pago (DPO), que empiezan cuando se incurre el gasto.
- Tiempo de aprobar y programar: 2,8 días o menos en el mejor cuartil; una semana o más en el peor (Wiggins 2022 [L]).
- Porcentaje de renglones de factura que coinciden la primera vez: la página de la medida da 403 [S]; la fórmula sale de la lista de 2013 [L].
- Costo por factura procesada: las cifras atribuidas a APQC en blogs (USD 2,05 / 5,78 / 10,00) no se pudieron verificar en APQC [S]: no entran a la nota.
- Compra fuera del circuito y costo por orden: definidas en Compras; días de pago: en Tesorería. Se enlazan.

## 5. Recurso canónico

Oracle Payables, la página de las tres formas del cruce (corta, con las desigualdades). Para el recorrido entero, el capítulo del ciclo de egresos de Romney y Steinbart, no leído.

## 6. Huecos

- APQC Open Standards Benchmarking da 403 en sus páginas de medidas: las fórmulas salen de la lista de 2013, pero los valores de referencia (salvo la factura al pago, por CFO.com) quedan sin leer.
- El capítulo del ciclo de egresos de Romney y Steinbart no se consiguió; tampoco una guía de auditoría completa (FAM del GAO no se leyó en su parte de egresos).
- Ninguna fuente define el tiempo de la solicitud al pago como una sola medida; APQC lo parte en dos.
- Evaluated receipt settlement (pagar desde la recepción, sin factura): solo aparece la idea en GAO 1995 [M]; no entra en la nota.

## 7. Problemas encontrados en los temas de dominio

- `Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md:21`: dice que Compras y Tesorería están «todavía sin escribir»; ya existen. Línea 42: Impuestos «todavía no escrito».
- `Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md:50`: «Sin fuente todavía» para el cruce de tres vías; hay un apunte académico (Bradley) y la guía de Oracle con las tres vías.
- `Compras-y-abastecimiento/compras-y-abastecimiento.md:22`, `:67` y `:68`: Cadena de suministro y Tesorería «todavía no armado»; ya existen (`Cadena-de-suministro-y-logistica/Comercio-exterior/comercio-exterior.md`).
- `Compras-y-abastecimiento/Orden-de-compra/solicitud-de-compra.md:31` y `:48`: Producción «todavía no armado».
- `Compras-y-abastecimiento/Orden-de-compra/tipos-de-orden.md:134`: Producción y Activos y mantenimiento «todavía no armado».
- `Compras-y-abastecimiento/compras-y-abastecimiento-en-argentina.md:51`, `:58`, `:62`, `:87`: Impuestos y Tesorería «todavía no armado(s)»; ya existen `Impuestos/Recaudacion-en-la-fuente/retenciones-y-percepciones-en-argentina.md` y `Tesoreria/tesoreria-en-argentina.md`.
- `Inventario-y-depositos/Operacion-del-deposito/recepcion.md:24`: dice que Compras compara lo recibido «con la orden de compra y con la factura del proveedor»; contradice #98 y `compras-y-cuentas-a-pagar.md` (la factura es de Contabilidad). Además, Compras «todavía no armado». Línea 58: Cadena «todavía no armado».
- `Tesoreria/Pagos-a-proveedores/pagos-a-proveedores.md:26`: Compras «un tema todavía no escrito». Línea 36: «Compras decide que la factura se debe»; en el resto de la base el cruce y la deuda son de Contabilidad.
- `Tesoreria/Pagos-a-proveedores/programacion-de-pagos.md:125`: Administración de personal e Impuestos «todavía no escritos».
- Término: el ALCANCE de Procesos de negocio (pregunta 2) dice «control de tres vías»; la base dice «cruce de tres vías» (Compras, Contabilidad). Conviene unificar a «cruce».
- Cifra: `solicitud-de-compra.md:62` da «2.5 percent or more» para las de peor desempeño; `fundamentos-de-compras-y-abastecimiento.md:74` compara «2 % o más» frente a «menos de 1 %». Puede ser el mismo artículo con dos cortes; conviene cotejarlo.

## Borrador para la nota de Argentina

Apartado «De la compra al pago». En la Argentina el recorrido suma tres cosas que no cambian su orden pero sí lo que se controla en cada traspaso.

- **Al recibir la factura del proveedor**: constatar el CAE en ARCA antes del cruce, y mirar la letra y la leyenda del comprobante (la A con «OPERACIÓN SUJETA A RETENCIÓN» que reemplazó a la M). Está en [Compras y abastecimiento en la Argentina](../Compras-y-abastecimiento/compras-y-abastecimiento-en-argentina.md#qué-se-controla-cuando-llega-la-factura) y la factura electrónica en sí, en [factura electrónica de ARCA](../Comercio-electronico/Normativa/factura-electronica-de-arca.md). El crédito fiscal que deja la factura, en [IVA en Argentina](../Impuestos/Impuestos-al-consumo/iva-en-argentina.md).
- **Factura de crédito electrónica MiPyME**: si la empresa es grande y el proveedor una pyme, la factura se acepta o se rechaza en un plazo de 21 días corridos, o queda aceptada tácitamente. El cruce de tres vías tiene que terminar antes de ese plazo, porque rechazar por diferencias pide tener registrada la recepción. Detalle en [Compras y abastecimiento en la Argentina](../Compras-y-abastecimiento/compras-y-abastecimiento-en-argentina.md#la-factura-de-crédito-electrónica-mipyme-del-lado-del-que-compra).
- **Al pagar**: quien paga, si es agente, retiene IVA, Ganancias e Ingresos Brutos y entrega el certificado de retención; el proveedor con certificado de exclusión no sufre la retención. Los regímenes, en [retenciones y percepciones en Argentina](../Impuestos/Recaudacion-en-la-fuente/retenciones-y-percepciones-en-argentina.md); qué hace el agente y qué guarda, en [agente de recaudación](../Impuestos/Recaudacion-en-la-fuente/agente-de-recaudacion.md). La corrida de pagos tiene que calcular la retención sobre cada pago, no sobre la factura, y descontarla del neto (lectura de la base sobre la regla «deducciones con su cuenta» de [corrida de pagos](../Tesoreria/Pagos-a-proveedores/corrida-de-pagos.md)).
- **El medio de pago**: el ECHEQ y las transferencias inmediatas, en [Tesorería en Argentina](../Tesoreria/tesoreria-en-argentina.md#lo-que-cambia-con-el-echeq); la leyenda «PAGO EN CBU INFORMADA» obliga a pagar a la CBU informada a ARCA ([Compras y abastecimiento en la Argentina](../Compras-y-abastecimiento/compras-y-abastecimiento-en-argentina.md#qué-factura-tiene-que-mandar-el-proveedor)).
- **La importación**: los tributos y percepciones de la aduana están en [comercio exterior en Argentina](../Impuestos/comercio-exterior-en-argentina.md).
