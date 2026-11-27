---
resumen: >-
  El costo del flete es lo que el cargador paga por mover una carga. Se arma con una parte fija por envío o por parada y una variable por distancia, peso o unidad, más recargos, y su precio depende de cómo se contrató: por contrato, en el mercado spot o por licitación.
estado: vigente
estabilidad: semi
fuentes:
  - "Rodrigue y Notteboom, 3.2 Transport Costs, en Rodrigue, The Geography of Transport Systems (tarifa frente a costo, costo de servicio y valor de servicio, costos de terminal y de línea, recargos): https://transportgeography.org/contents/chapter3/transport-costs/"
  - "Rodrigue, 5.1 Transportation Modes, Modal Competition and Modal Shift (ajuste por combustible según el modo): https://transportgeography.org/contents/chapter5/transportation-modes-modal-competition-modal-shift/"
  - "Caplice, C. (MIT), Transportation Management: Fundamental Concepts, ESD.260, noviembre de 2006 (lect20; funciones de costo del transporte y Transport vs. Inventory Costs; las curvas no están en el texto extraído): https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/06ab054739b3882c4bda862570c7266b_lect20.pdf"
  - "Caplice, C. (MIT), Transportation Management: Operational Networks, ESD.260, noviembre de 2006 (lect21, diapositivas 17 y 19: continuo de relaciones y costo por envío): https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/3a09fc7ee1175120b31399b1ce06b175_lect21.pdf"
  - "Caplice y Sheffi (2003), Optimization-based procurement for transportation services, Journal of Business Logistics 24(2):109-128 (según el resumen): https://api.crossref.org/works/10.1002/j.2158-1592.2003.tb00048.x"
  - "Sheffi (2004), Combinatorial Auctions in the Procurement of Transportation Services, Interfaces 34(4):245-252 (según el resumen): https://api.crossref.org/works/10.1287/inte.1040.0075"
  - "Caplice (2007), Electronic Markets for Truckload Transportation, Production and Operations Management 16(4):423-436 (según el resumen): https://api.crossref.org/works/10.1111/j.1937-5956.2007.tb00270.x"
  - "Li, Bolumole y Miller (2022), Antecedents of Spot and Contract Freight Mix in the Truckload Sector, Transportation Journal 61(4):331-368 (según el resumen): https://doi.org/10.5325/transportationj.61.4.0331"
  - "Wikipedia, Dimensional weight (secundaria; solo la regla del mayor entre peso real y volumétrico; según el resumen): https://en.wikipedia.org/wiki/Dimensional_weight"
  - "Wikipedia, Freight audit (secundaria, marcada como falta de citas; según el resumen): https://en.wikipedia.org/wiki/Freight_audit"
  - "Documentación de un ERP abierto, Shipping Rule (según el resumen): https://docs.frappe.io/erpnext/user/manual/en/shipping-rule"
  - "Documentación de otro ERP abierto, envío con proveedor externo (versión 17.0, leída): https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper.html"
  - "Modelo de datos de un tercer ERP abierto, entidades de envío (costos y peso facturable por tramo; según el resumen): https://raw.githubusercontent.com/apache/ofbiz-framework/trunk/applications/datamodel/entitydef/shipment-entitymodel.xml"
  - "Cadena-de-suministro-y-logistica/.investigacion/transporte.md (sección 3) y transporte-2.md (sección 3)"
aliases: [costo del flete, flete, tarifa de flete, freight rate, freight cost, costo de transporte, transport cost, tarifa, rate, peso facturable, billable weight, chargeable weight, peso volumétrico, recargo, surcharge, recargo por combustible, fuel surcharge, flete por contrato, contract rate, flete spot, spot rate, licitación de fletes, transportation procurement, freight tender, subasta combinatoria, combinatorial auction, guía de ruteo, routing guide, auditoría de fletes, freight audit, liquidación de fletes, freight payment]
creado: 2026-11-27
revisado: 2026-11-27
---

# Costo del flete

El costo del flete es lo que el cargador paga por mover una carga. Se arma con una parte fija por envío o por parada y una variable por distancia, peso o unidad, más recargos, y su precio depende de cómo se contrató: por contrato, en el mercado spot o por licitación.

Es la segunda decisión del cargador en [Transporte](transporte.md), después del [modo](modos-de-transporte.md). El costo del envío de una tienda online, paquete por paquete, está en [costo del envío](../../Comercio-electronico/Operaciones-del-comercio/Envios-y-logistica/costo-del-envio.md), de Comercio electrónico; acá va la carga entre empresas. Quién paga el flete en una venta internacional lo fija el [Incoterm](../Comercio-exterior/incoterms.md). Cómo entra el flete en el costo de la mercadería es de Contabilidad, en [costo de lo vendido](../../Contabilidad/Operaciones/costo-de-lo-vendido.md); si se paga en otra moneda, [moneda extranjera](../../Contabilidad/Operaciones/moneda-extranjera.md).

## La tarifa no es el costo

Rodrigue separa lo que cuesta mover la carga de lo que se cobra: «Rates are the price of transportation services paid by their users... They may not necessarily express the real transport costs». En carga hay dos lógicas para fijar la tarifa: «cost-of-service», que refleja el costo directo, y «value-of-service», que cobra según el valor de la mercadería. El cargador ve la tarifa; el costo es del transportista. A juicio de la base, entender la estructura del costo sirve para leer la tarifa y negociarla.

## De qué se arma

Rodrigue reparte el costo en dos partes:

- De terminal: «loading, transshipment, and unloading». Los de origen y destino son inevitables; los intermedios, los del transbordo, se pueden evitar.
- De línea (linehaul): «Costs that are a function of the distance over which a unit of freight or passenger is carried. Weight is also a cost function when freight is involved».

Caplice lo escribe como costo por envío con una parte fija y una variable: «c_f = c_s(1 + n_s) + c_d d» y «c_v = c_vs + c_vd d». La parte fija suma un costo por parada y otro por distancia; la variable, un costo por ítem y otro por ítem y distancia (lectura de la base sobre los términos de la fuente).

Las tarifas toman cinco formas, según las funciones de costo que muestra Caplice:

| Forma | Cómo se cobra |
|---|---|
| Variable | un monto por unidad (kilo, pallet, kilómetro) |
| Fija | un monto por envío, sin importar cuánto lleve |
| Mixta | un fijo por envío más un variable por unidad |
| Variable con mínimo | «Variable Cost / Unit with a Minimum»: por unidad, pero nunca menos de un piso |
| Con descuentos por escala | «Incremental Discounts»: el precio por unidad baja por tramos de cantidad |

El tamaño del envío entra en la elección del modo. Caplice suma al flete el costo del stock que viaja, «cf + cv + r·v·tm» (fijo, variable y el costo de tener el valor v inmovilizado durante el tiempo de viaje tm), y grafica tres modos contra el tamaño del envío; la lectura de la base es que cada modo resulta el más barato en un rango de tamaños. Es la misma cuenta del costo total de [Transporte](transporte.md#el-transporte-entra-en-el-costo-del-stock).

### El peso que se cobra

En muchas tarifas se cobra el mayor entre el peso real y el volumétrico, que sale del volumen dividido por un divisor. Según el resumen de Wikipedia, «The shipping fee is based upon the dimensional weight or the actual weight, whichever is greater». El divisor lo fija cada transportista o cada tarifa; no hay uno universal. Los divisores de la paquetería y cómo se aplican están en [costo del envío](../../Comercio-electronico/Operaciones-del-comercio/Envios-y-logistica/costo-del-envio.md).

> [!NOTE] Sin fuente todavía: el divisor del peso volumétrico en la carga aérea, en la terrestre y en la marítima entre empresas. Lo leído es de paquetería.

### Recargos

Rodrigue los define como «an array of fees, often set arbitrarily, that reflect temporary conditions that may affect the costs assumed by the transporter». Los más comunes son «Fuel surcharges, security fees, geopolitical risk premiums». El combustible se traslada distinto según el modo: el marítimo hace «direct rate adjustments», y el aéreo se apoya en «fuel surcharges when energy prices are increasing».

> [!NOTE] Sin fuente todavía: el mecanismo contractual del recargo por combustible (la tabla atada a un índice, cada cuánto se actualiza) y los recargos de temporada alta.

## Cómo se contrata el flete

La relación con el transportista va del viaje suelto a la flota propia; el continuo de Caplice está en [Transporte](transporte.md#del-mercado-spot-a-la-flota-propia). Para la carga que se compra afuera, el precio sale de tres maneras.

### Contrato y spot

El contrato fija la tarifa por un período; el spot la pacta viaje por viaje. Li, Bolumole y Miller (2022), según su resumen, lo dicen desde el transportista de camión completo en Estados Unidos: «contract freight provides loose volume guarantees but lower linehaul rates, whereas spot freight commands higher linehaul rates while being more stochastic in nature». Caplice coincide en el signo: el spot es para el tráfico aleatorio o de urgencia, el contrato para los flujos estables. Las dos fuentes son de Estados Unidos y de camión completo; no es un dato universal.

### Licitación

La tarifa de contrato sale de una licitación. Según el resumen de Sheffi (2004), «Most shippers use annual auctions to procure transportation services, leading to annual contracts». Se licita por carril (lane, un par de origen y destino): Sheffi habla de decidir «which carrier should serve what lane».

Tres ideas de la literatura, todas de Caplice y Sheffi, dos autores, y leídas como resumen:

- Asignar es un problema combinatorio. Caplice y Sheffi (2003): «the shipper's assignment problem involves a combinatorial number of choices and cannot be easily executed manually», y por eso la licitación se beneficia de la optimización.
- Ofertar por paquetes de carriles. En una subasta combinatoria el transportista oferta por un conjunto de carriles que le cierra en su red. Sheffi dice que así el cargador baja costos «while protecting carriers from winning lanes that do not fit their networks», porque tiene en cuenta las economías de alcance, «which many consider more important than economies of scale in transportation operations».
- El precio no alcanza. Según Sheffi, el nivel de servicio del transportista y otras variables «are as important as price in determining which carrier should serve what lane».

El resultado se guarda en una guía de ruteo (routing guide). Caplice (2007) dice que las subastas se usan para llenar estos catálogos «with pricing, assignments, and priority logic», y que los mercados electrónicos los complementan «in cases where the catalog fails». En la práctica, cuando el transportista asignado rechaza la carga, se pasa al siguiente de la guía o al spot (lectura de la base).

> [!NOTE] Sin fuente todavía: cómo se arma un pliego de licitación, sus plazos y los criterios con que se puntúa en la práctica.

## Liquidación y auditoría de fletes

Después del viaje, el transportista factura y el cargador controla. Según el resumen de Wikipedia (fuente débil, marcada por falta de citas), la auditoría de fletes es «the process of examining, adjusting, and verifying freight bills for accuracy». Se hace a mano, con software o tercerizada, a menudo cobrando un porcentaje de lo recuperado; se audita envío por envío o factura por factura, y la auditoría posterior al pago puede recuperar pagos de más. El control de fondo, como inferencia de la base, es comparar el flete facturado con el que da la tarifa vigente para ese envío.

> [!NOTE] Sin fuente todavía: los pasos de la liquidación, los errores más comunes en las facturas de flete y sus estados. No hay fuente académica ni de asociación leída.

## Qué guarda un sistema de la tarifa

Los sistemas abiertos consultados muestran tres maneras de calcular el flete:

- Regla por tramos. Un ERP abierto, según el resumen de su documentación, calcula un cargo fijo o por tramos del total neto o del peso neto, con una tabla «desde, hasta, monto», los países donde aplica y la cuenta contable. El cargo puede bajar cuando sube el valor del pedido.
- Cotización al transportista. Otro pide la tarifa al transportista («Get Rate») o, además, crea el envío y la etiqueta. Le suma un «Margin on Rate» para cubrir «handling fees, packaging materials, exchange rates», ofrece envío gratis sobre un monto y un porcentaje de seguro, y guarda cada cotización pedida. Su ejemplo muestra que el transportista puede informar un peso distinto del cargado: 6 kilos contra 7.
- Costo real por tramo. Un tercero guarda, en cada tramo, el peso facturable y el costo real separado en transporte, servicio y otros, con su moneda; en el envío, un costo estimado y un cargo adicional con su descripción (según el resumen de su modelo de datos).

Las dos primeras son de paquetería y comercio electrónico: muestran que la tarifa se calcula con peso, distancia y reglas, y no cómo se tarifa la carga entre empresas.

De las fuentes del tema sale, como inferencia de la base, la ficha de una tarifa de carga: transportista, carril o zonas de origen y destino, modo y servicio, unidad de cobro (peso, volumen, pallet, contenedor, kilómetro), forma (de las cinco de arriba), escalas, mínimo, moneda, vigencia y recargos. La guía de ruteo suma la asignación y la prioridad por carril. Junto al cálculo van el peso real, el volumétrico y el facturable, y del lado del control, la factura del transportista con la diferencia entre lo esperado y lo cobrado.

> [!NOTE] Sin fuente todavía: los campos de una tarifa de contrato en un sistema (vigencia, recargos, mínimos) y los estados de la auditoría y del pago.
