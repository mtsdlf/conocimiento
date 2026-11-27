# Del pedido al cobro (order-to-cash): informe de investigación

Fecha: 2026-11-27. Sesión 13 de 16 (issue #120). Alcance: el recorrido de punta a punta del pedido de venta aceptado al cobro aplicado y conciliado (decisión de #99), sus traspasos entre dominios, dónde se traba y qué se mide del recorrido entero. El detalle de cada paso ya está en los temas de dominio; este informe junta lo que no es de ningún dominio y verifica qué fuentes de dominio se reusan.

Marcas: [L] texto completo leído (o la tabla/página entera), [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntaje 1-3 en autoridad / profundidad / ejemplos / unicidad (A/P/E/U).

## Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| APQC, PCF Cross Industry 7.4 (agosto 2024), copia de la IFRC | https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf | primaria | 3/2/1/3 | [L] (texto bajado al scratchpad, grep por código) |
| APQC, Open Standards Benchmarking Measure List (2013, 203 págs.) | https://www.apqc.org/sites/default/files/APQC%20Benchmarking%20Measures%20List.pdf | primaria | 3/1/1/3 | [L] de las filas citadas (nombre, fórmula en inglés, ID) |
| APQC, OSB Measure List «Accounts Receivable» (2012) | https://www.apqc.org/sites/default/files/files/OSB/measureLists/20120812/Measures%20List%20-%20Accounts%20Receivable.pdf | primaria | 3/1/1/2 | [L] |
| APQC, OSB Measure List «Customer Credit and Invoicing» (2018) | https://www.apqc.org/sites/default/files/osb/259%20-%20Customer%20Credit%20and%20Invoicing%20Measure%20List_0.pdf | primaria | 3/1/1/2 | [L] |
| APQC, OSB Measure List «Sales and Order Management» (2015) | https://www.apqc.org/sites/default/files/osb/233%20-%20Sales%20and%20Order%20Management%20Measure%20List_0.pdf | primaria | 3/1/1/2 | [L] |
| APQC, medida «Cycle time in days to perform the order-to-cash (O2C) processes» | https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/cycle-time-days-perform-order-cash-o2c | primaria | 3/1/1/3 | [S] (403; solo el fragmento del buscador) |
| APQC, «What is the order-to-cash process» (blog) y «End-to-End Processes» | https://www.apqc.org/blog/what-order-cash-process ; https://www.apqc.org/expertise/end-to-end-processes | primaria | 3/1/1/2 | [S] (403; resumen del buscador) |
| Romney y Steinbart (atribuido), *Accounting Information Systems*, cap. 12 «The Revenue Cycle: Sales to Cash Collections», diapositivas de Pearson (2012) | https://docs.google.com/presentation/d/1PJd1Bx3TA6fdXV6Rb7I1A62ffB9AT02d/htmlpresent | primaria (material del libro) | 3/2/1/3 | [L] de las diapositivas; la autoría es [S]: las diapositivas solo dicen «Pearson Education, publishing as Prentice Hall», y el buscador las asocia al libro de Romney y Steinbart |
| Notas de dominio de la base (Relación con clientes, Inventario, Cadena, Contabilidad, Impuestos, Tesorería, Comercio electrónico) | rutas abajo | secundaria interna | — | [L] |

Las fuentes de dominio que ya citan las notas enlazadas (OpenStax, NIIF 15, CRF, KPMG, CASRAI, GS1) no se volvieron a leer: se enlazan las notas.

## Afirmaciones

### Borde y piezas APQC

- APQC define los procesos de punta a punta como procesos que cruzan funciones y comprenden todos los pasos para lograr un resultado; según su resumen, el O2C se centra en recibir, procesar y facturar los pedidos e incluye «manage sales orders» y «perform revenue accounting». También dice que «Order-to-Cash» puede significar cosas distintas según dónde cada organización pone el borde. [S] https://www.apqc.org/blog/what-order-cash-process ; https://www.apqc.org/expertise/end-to-end-processes
- Según el fragmento del buscador, la medida de ciclo O2C de APQC abarca gestionar pedidos, entregar, crédito, facturar y cobrar. [S] https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/cycle-time-days-perform-order-cash-o2c
- Piezas del PCF 7.4, literales [L]:
  - 3.5.4 «Manage sales orders» (10185): 3.5.4.1 «Accept and validate sales orders», 3.5.4.3 «Determine availability», 3.5.4.5 «Process back orders and updates», 3.5.4.6 «Handle sales order inquiries including post-order fulfillment transactions».
  - 9.2.1 «Process customer credit» (10742).
  - 4.4.3.4 «Pick, pack, and ship product for delivery» (10356), dentro de 4.4.3 «Operate warehousing».
  - 4.4.4.1 «Plan, transport, and deliver outbound product» (10360), dentro de 4.4.4 «Operate outbound transportation».
  - 9.2.2 «Invoice customer» (10743): 9.2.2.2 «Generate customer billing data», 9.2.2.3 «Transmit billing data to customers», 9.2.2.4 «Post receivable entries», 9.2.2.5 «Resolve customer billing inquiries».
  - 9.2.3 «Process accounts receivable (AR)» (10744): 9.2.3.2 «Receive/Deposit customer payments», 9.2.3.3 «Apply cash remittances», 9.2.3.5 «Post AR activity to the general ledger».
  - 9.2.4 «Manage and process collections» (10745); 9.2.5 «Manage and process adjustments/deductions» (10746).
  - 9.3.2.6 «Reconcile general ledger accounts» (10824); 9.7.2.1 «Manage and reconcile cash positions» (10893).
- Observación: el PCF reparte el recorrido en cuatro categorías (3, 4, 9.2, 9.7). Ninguna sola lo contiene: es el argumento para tratarlo como recorrido (lectura propia).

### Ciclo de ingresos en los libros de sistemas contables

- El ciclo de ingresos «Provides goods and services to customers» y «Collects cash in payment for those sales»; actividades básicas: «Sales order entry», «Shipping», «Billing», «Cash collections». [L] diapositivas Pearson 2012.
- Documentos que nombra: sales order, picking list (picking ticket), packing slip, bill of lading, invoice, credit memo, customer statements. [L]
- Amenazas por actividad [L]: pedido: «Incomplete/inaccurate orders», «Invalid orders», «Uncollectible accounts», «Stockouts or excess inventory»; despacho: «Picking the wrong items or the wrong quantity», «Shipping errors»; facturación: «Failure to bill», «Billing errors», «Posting errors in accounts receivable», «Inaccurate or invalid credit memos»; cobro: «Theft of cash», «Cash flow problems».
- Controles que son traspasos [L]: «Credit limits»; «Specific authorization to approve sales to new customers or sales that exceed a customer's credit limit»; «Reconciliation of picking lists to sales order details»; «Reconciliation of shipping documents with sales orders, picking lists, and packing slips»; «Separation of billing and shipping functions»; «Periodic reconciliation of invoices with sales orders, picking tickets, and shipping documents»; «Configuration of system to automatically enter pricing data»; «Mailing of monthly statements to customers»; «Reconciliation of subsidiary accounts to general ledger»; «Segregation of duties of credit memo authorization from both sales order entry and customer account maintenance»; «Use of EFT, FEDI, and lockboxes to minimize handling of customer payments by employees».

### Medidas del recorrido entero (APQC OSB)

- 100496 «Customer order cycle time in days»: «Cycle time in days from a customer's placing a primary product/service order to the product/service's delivery». [L] lista 2013 y lista Sales and Order Management 2015.
- 100558 «Cycle time in days between transmission of invoice and shipment of goods or delivery of services»: «Cycle time in calendar days from the transmission of an invoice/bill to shipping/providing the good/service». [L] lista 2013 y Customer Credit and Invoicing 2018.
- 100581 «Cycle time in days from transmission of invoice to receipt of payment»: «Cycle time in calendar days from invoicing a customer to the receipt of payment». KPI de 9.2.3. [L] listas 2012 y 2013.
- 100178 «Days sales outstanding». [L] (la fórmula la da la CRF en la nota de Tesorería).
- 100164 «Cycle time in days to generate complete and correct billing data». [L] 2018.
- 100561 «Cycle time in days for credit approval». [L] 2018.
- 102142 «Percentage of invoice line items processed error free the first time». [L] 2018.
- 102264 «Percentage of billed/invoiced line items paid on time to the business entity». [L] 2018.
- 102155 «Percentage of invoice line items that are adjusted by the customer prior to payment». [L] 2012.
- 102463 «Percentage of receipts automatically matched to open items in the accounts receivable sub ledger». [L] 2012.
- 100628 «Cycle time in days to resolve adjustments». [L] 2012.
- 101741 «Perfect order performance»: en la lista de 2015 la fórmula impresa es la de otra medida («Number of total annual inbound contacts outsourced...»), un error de la lista; en la de 2013 la fórmula es solo «[Perfect order performance]». La definición con componentes está en la nota de Cadena (fragmento del buscador). [L]
- Ninguna lista abierta da la fórmula de la medida O2C de punta a punta ni valores de referencia: son solo para socios. Hueco.

### Lo que ya está en los dominios (verificado leyendo las notas)

- Pedido con dos ejes (entregado, facturado) y qué dispara aguas abajo: `../Relacion-con-clientes/Pedido-de-venta/pedido-de-venta.md` [L].
- Bloqueo por crédito, de entrega y de facturación: `../Relacion-con-clientes/Pedido-de-venta/cambios-y-cancelaciones.md#bloquear-un-pedido` [L]. Límite y exposición (suma pedidos sin facturar y cheques sin acreditar): `../Tesoreria/Credito-y-cobranzas/credito-a-clientes.md` [L].
- Fecha prometida y ATP: `../Relacion-con-clientes/Pedido-de-venta/fecha-prometida.md`, `../Inventario-y-depositos/Existencias/disponible-para-prometer.md`; reserva: `../Inventario-y-depositos/Operacion-del-deposito/reserva.md` [L de títulos y resumen].
- Preparación (picking, embalaje, control): `../Inventario-y-depositos/Operacion-del-deposito/preparacion-de-pedidos.md`; despacho: `../Cadena-de-suministro-y-logistica/Despacho-y-entrega/despacho.md`; prueba de entrega y sus tres resultados: `prueba-de-entrega.md` [L de títulos y resumen].
- Pedido perfecto, OTIF, tiempo de ciclo del pedido: `../Cadena-de-suministro-y-logistica/Despacho-y-entrega/nivel-de-servicio-logistico.md` [L].
- Factura y nota de crédito como comprobante fiscal: `../Impuestos/Cumplimiento/comprobante-fiscal.md` [L]; registro del ingreso al transferir el control (NIIF 15), cuenta a cobrar, nota de crédito, anticipos: `../Contabilidad/Operaciones/ingresos-y-cuentas-a-cobrar.md` [L].
- Auxiliar de clientes y antigüedad: `../Contabilidad/Registro/cuentas-corrientes.md`; conciliación bancaria y del auxiliar contra la cuenta de control: `../Contabilidad/Control-interno/conciliaciones.md` [L de títulos].
- Gestión de la cobranza, disputas y deducciones, DSO: `../Tesoreria/Credito-y-cobranzas/gestion-de-la-cobranza.md` [L]; aplicación de cobros y sus casos: `aplicacion-de-cobros.md` [L].
- Ciclo de conversión del efectivo: `../Tesoreria/Caja-y-liquidez/capital-de-trabajo.md#el-ciclo-de-conversión-del-efectivo` [L].
- Variantes: tienda (`../Comercio-electronico/Pagos/pagos.md`, `../Comercio-electronico/Checkout-y-conversion/checkout-y-conversion.md`, `../Comercio-electronico/Pagos/fraude-y-contracargos.md`); mayorista (`../Comercio-electronico/Comercio-B2B/comercio-b2b.md`, `cuenta-corriente-y-credito.md`, `pedido-b2b.md`); suscripción (`../Relacion-con-clientes/Pedido-de-venta/tipos-de-pedido.md#el-pedido-recurrente`, `../Emprender/Modelo-de-negocio/saas.md`, anticipos e ingresos diferidos en Contabilidad). No hay nota de facturación recurrente propia; `../Servicios-profesionales-y-proyectos/Facturacion-del-proyecto/abono-y-bolsa-de-horas.md` trata el abono de servicios y va con el proyecto al cobro.

### Inferencias propias (marcadas así en la nota)

- Los traspasos que más fallan son los que cambian de dueño el documento: pedido a reserva (cantidad y fecha), entrega a factura (lo entregado contra lo facturado), factura a cuenta a cobrar, cobro a factura (aplicación). Los controles de Romney y Steinbart son conciliaciones de esos mismos pares; la lectura de que «cada control es un traspaso» es propia.
- La deducción del cliente al pagar suele nacer aguas arriba (entrega incompleta, precio distinto, devolución): es la vuelta del recorrido sobre sí mismo. Apoyo: CRF cuenta las deducciones como componente del DSO (en la nota de Tesorería) y APQC tiene 102155; la causalidad es lectura propia.
- El tiempo de punta a punta se puede partir en tres tramos medibles con medidas de APQC: pedido a entrega (100496), entrega a factura (100558, con signo), factura a cobro (100581). La suma como descomposición es propia.

## Recursos canónicos

- APQC PCF 7.4, categorías 3.5.4, 4.4.3-4.4.4 y 9.2: para ver que ningún dominio solo contiene el recorrido.
- Romney y Steinbart, capítulo del ciclo de ingresos: la tabla de amenazas y controles por actividad.

## Huecos

1. La fórmula y los valores de referencia de la medida O2C de APQC (403; solo socios).
2. El texto de SCOR para el tiempo de ciclo del cumplimiento del pedido (RS.1.1) no se leyó; la nota de Cadena ya lo marca.
3. El libro de Romney y Steinbart no se leyó: solo las diapositivas del editor. La autoría se asigna por el buscador.
4. Ninguna fuente neutral sobre la facturación recurrente (estados de una suscripción, renovación); la nota de Relación con clientes ya lo marca.
5. Una fuente que cuantifique dónde se pierden días en el recorrido (qué tramo pesa más) no apareció.

## Borrador para la nota de Argentina

### Del pedido al cobro

- **El pedido no es factura.** La nota de pedido lleva la leyenda de documento no válido como factura: [la leyenda de lo que no es factura](../Relacion-con-clientes/relacion-con-clientes-en-argentina.md#la-leyenda-de-lo-que-no-es-factura).
- **El despacho lleva remito.** Todo traslado de mercadería va con remito, y desde abril de 2025 puede ser digital; en la provincia de Buenos Aires, además, el COT: [inventario y depósitos en la Argentina](../Inventario-y-depositos/inventario-y-depositos-en-argentina.md) y [el remito](../Cadena-de-suministro-y-logistica/Despacho-y-entrega/despacho.md#en-la-argentina-el-remito).
- **La factura necesita CAE.** La factura electrónica (letra A, B, C o E) se emite con el código de autorización que ARCA da por comprobante; sin CAE no produce efectos: [factura electrónica de ARCA](../Comercio-electronico/Normativa/factura-electronica-de-arca.md). La misma regla rige la nota de crédito, que solo emite quien emitió la factura.
- **Al facturar se perciben; al cobrar, se sufren retenciones.** Un vendedor agente de percepción suma IVA o Ingresos Brutos a la factura ([factura entre empresas](../Comercio-electronico/Comercio-B2B/factura-entre-empresas.md#percepciones-el-impuesto-que-el-mayorista-cobra-por-adelantado)); un cliente agente de retención paga neto y entrega el certificado, que se aplica junto con la plata ([retenciones y percepciones en Argentina](../Impuestos/Recaudacion-en-la-fuente/retenciones-y-percepciones-en-argentina.md), [las retenciones sufridas](../Tesoreria/Credito-y-cobranzas/aplicacion-de-cobros.md#las-retenciones-sufridas)). Los cobros bancarios pueden sufrir SIRCREB o SIRTAC ([normativa argentina](../Comercio-electronico/Normativa/normativa-argentina.md#sirtac-ingresos-brutos-sobre-los-cobros)).
- **El cobro llega en cheque o ECHEQ.** El cheque a fecha es cobro, crédito y garantía, y obliga a decidir si cancela la factura al recibirse o al acreditarse: [tesorería en Argentina](../Tesoreria/tesoreria-en-argentina.md#lo-que-cambia-con-el-echeq).
- **Entre una pyme y una empresa grande, FCE MiPyME.** Por encima de un monto, la factura es de crédito electrónica, el comprador la acepta o la rechaza en un plazo, y se puede negociar: [la Factura de Crédito Electrónica MiPyME](../Comercio-electronico/Comercio-B2B/factura-entre-empresas.md#la-factura-de-crédito-electrónica-mipyme) y [cómo se financia una pyme con sus cheques y sus facturas](../Tesoreria/tesoreria-en-argentina.md#cómo-se-financia-una-pyme-con-sus-cheques-y-sus-facturas).
