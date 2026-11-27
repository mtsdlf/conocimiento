---
resumen: >-
  El flujo de entrada (inbound) es la parte de la logística que lleva lo comprado desde que sale del proveedor hasta que llega al muelle del comprador: planificar qué va a llegar y cuándo, decidir quién contrata el flete, seguir el viaje, darle turno al camión y medir si las entregas llegan como se pactó. Termina donde empieza la recepción del depósito.
estado: borrador
estabilidad: estable
fuentes:
  - "APQC, Process Classification Framework, Cross Industry, versión 7.4 (© 2024), 4.4.2 «Plan and manage inbound material flow» (ID 20936) y sus actividades 4.4.2.1 a 4.4.2.5, 4.4.3.2, 4.4.4 y 4.2.3.5 a 4.2.3.7 (leído en esas partes): https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "APQC, Process Classification Framework, Cross Industry, versión 8.0, 27/02/2026 (no se pudo leer, error 403; existencia y fecha según el buscador): https://www.apqc.org/resource-library/resource-listing/apqc-process-classification-framework-pcf-cross-industry-pdf-13"
  - "ASCM, SCOR DS / SCOR 12 Comparison Document (© 2025), procesos S2.1 a S2.7 (leído): https://www.ascm.org/globalassets/ascm_website_assets/docs/scor/scor_crosswalk.pdf"
  - "ASCM, SCOR Digital Standard Quick Reference Guide, métricas CO.3.13, CO.3.14, RS.3.8 y RL.2.8 (leído): https://www.ascm.org/globalassets/documents--files/corporate-transformation/scor-ds-digital-guide_final.pdf"
  - "GS1 Germany, EANCOM 2002 S3, perfil DESADV, introducción (leído): https://www.publikationen.gs1-germany.de/Complete/eancom_v9.3/profiles/s3/desadv/en/html/in1.htm"
  - "GS1 UK, ASN Message Implementation Guideline, versión 1.3, marzo de 2012, borrador, copia alojada por el Instituto Superior Técnico de Lisboa (leído): https://disciplinas.tecnico.ulisboa.pt/meic-sei/2013-2014/labs/proj/gs1uk/ASN%20Guidelines.pdf"
  - "U.S. Department of Transportation, Office of Inspector General, Estimates Show Commercial Driver Detention Increases Crash Risks and Costs, but Current Data Limit Further Analysis, ST2018019, 31/01/2018, copia alojada por un tercero (leído): https://www.3plcentral.com/hubfs/FMCSA%20Driver%20Detention%20Final%20Report.pdf"
  - "GAO, Commercial Motor Carriers: More Could Be Done to Determine Impact of Excessive Loading and Unloading Wait Times, GAO-11-198, 2011 (según el resumen): https://www.gao.gov/products/gao-11-198"
  - "ICC, Incoterms 2020, EXW, A4 y B4 (leído): https://library.iccwbo.org/content/tfb/BOOKS/BK_0049/BK_0049_04_RulesAny.htm"
  - "IFRS Foundation, NIC 2 Inventarios, párrafo 11 (leído): https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias2.html"
  - "DP World, glosario, Landed cost (secundaria, leída): https://www.dpworld.com/en/glossary/landed-cost"
  - "Cadena-de-suministro-y-logistica/.investigacion/flujo-de-entrada.md y flujo-de-entrada-2.md (2026-11-27)"
aliases: [flujo de entrada, logística de entrada, inbound logistics, inbound material flow, flujo de materiales de entrada, transporte de entrada, inbound transportation, flete de entrada, inbound freight, arribo esperado, llegada esperada, expected receipt, turno de muelle, turno de descarga, dock appointment, dock appointment scheduling, ventana de descarga, time slot, aviso de despacho, despatch advice, DESADV, ASN, advance ship notice, detención, detention, tiempo de permanencia, dwell time, costo de llegada, landed cost, costo puesto en depósito, desempeño de las entregas entrantes, inbound delivery performance]
creado: 2026-11-27
revisado:
---

# Flujo de entrada

El flujo de entrada (inbound) es la parte de la logística que lleva lo comprado desde que sale del proveedor hasta que llega al muelle del comprador: planificar qué va a llegar y cuándo, decidir quién contrata el flete, seguir el viaje, darle turno al camión y medir si las entregas llegan como se pactó. Termina donde empieza la recepción del depósito.

Es el viaje de ida de lo comprado, dentro de [Transporte](transporte.md). La salida hacia el cliente está en [Despacho y entrega](../Despacho-y-entrega/despacho-y-entrega.md); lo que vuelve del cliente, que el PCF también pone en la entrada, en [logística inversa](../Despacho-y-entrega/logistica-inversa.md). Cuando lo comprado viene del exterior, el flujo de entrada suma la [aduana](../Comercio-exterior/aduana.md) y el recorrido de una importación de [comercio exterior](../Comercio-exterior/comercio-exterior.md#el-recorrido-de-una-importación).

## Lo que el PCF pone en la entrada

En la versión 7.4 del Process Classification Framework de APQC, el proceso es 4.4.2 «Plan and manage inbound material flow», dentro de 4.4 «Manage logistics and warehousing». Tiene cinco actividades:

| Actividad (PCF 7.4) | ID | Dónde va en la base |
|---|---|---|
| 4.4.2.1 Plan inbound material receipts | 10349 | acá: qué va a llegar y cuándo |
| 4.4.2.2 Manage inbound material flow | 10350 | acá: el viaje de entrada |
| 4.4.2.3 Monitor inbound delivery performance | 10351 | acá: el desempeño de las entregas que llegan |
| 4.4.2.4 Manage flow of returned products | 10352 | [logística inversa](../Despacho-y-entrega/logistica-inversa.md) |
| 4.4.2.5 Manage disposition of returned products | 20109 | [logística inversa](../Despacho-y-entrega/logistica-inversa.md) |

El PCF no tiene un proceso de transporte de entrada aparte: el transporte propio está en 4.4.4 «Operate outbound transportation», y 4.4.2 solo planifica, gestiona y monitorea la entrada. Los turnos de descarga y el aviso de despacho no figuran en el PCF; ponerlos acá, y repartir las actividades como en la tabla, es de la base. La recepción física es la actividad siguiente, 4.4.3.2 «Receive, inspect, and store inbound deliveries», que en la base es [recepción](../../Inventario-y-depositos/Operacion-del-deposito/recepcion.md), de Inventario.

APQC publicó la versión 8.0 del PCF el 27 de febrero de 2026, según el buscador. No se pudo leer (la página dio error 403), así que no se sabe si 4.4.2 cambió de número o de nombre. Las páginas de medidas de APQC siguen mostrando 4.4.2.3 «Monitor inbound delivery performance» con el ID 10351, pero no dicen de qué versión son.

> [!NOTE] Sin fuente todavía: el texto de 4.4.2 en el PCF 8.0 y sus definiciones; la base cita la 7.4 en todos los temas. Se probaron el PDF y el Excel de APQC (bloqueados), las copias de archive.org (guardan solo la ficha, sin el documento), una copia en un sitio de documentos (bloqueada) y notas de versión (no se encontraron). Hace falta abrir el PDF de APQC desde un navegador.

SCOR, el otro marco de la cadena, pone la entrada dentro de abastecer. Según la tabla de equivalencias de ASCM de 2025, el SCOR Digital Standard tiene S2.2 «Schedule Product Delivery», S2.3 «Manage Inbound Transport» y S2.4 «Receive Product». El S2.3 es nuevo: la versión 12 pasaba directo de programar la entrega (sS1.1) a recibir (sS1.2). Cómo se reparten los dos marcos en el tema está en [marcos de la cadena de suministro](../Fundamentos/marcos-de-la-cadena-de-suministro.md).

## Dónde corta con Compras y con el depósito

Tres dominios miran la misma entrega desde lados distintos. El reparto es de la base, apoyado en el PCF:

| Dominio | Qué mira | En el PCF 7.4 |
|---|---|---|
| [Compras y abastecimiento](../../Compras-y-abastecimiento/compras-y-abastecimiento.md) | si el proveedor confirmó y cumple la orden: apurarlo, conciliar, resolver excepciones | 4.2.3.5 «Expedite orders and satisfy inquiries», 4.2.3.6 y 4.2.3.7 |
| Este tema | cómo viaja lo pedido y cuándo llega: el flete, el turno, el seguimiento del viaje y el desempeño de la entrega | 4.4.2.1 a 4.4.2.3 |
| [Inventario y depósitos](../../Inventario-y-depositos/inventario-y-depositos.md) | descargar, contar, inspeccionar y guardar | 4.4.3.2 |

La confirmación del proveedor y el aviso de despacho, del lado de la orden, están en [confirmación y seguimiento](../../Compras-y-abastecimiento/Seguimiento-de-la-orden/confirmacion-y-seguimiento.md). La comparación de lo que llegó contra lo pedido es [recepción contra lo pedido](../../Compras-y-abastecimiento/Seguimiento-de-la-orden/recepcion-contra-lo-pedido.md).

## Quién contrata el flete de entrada

Quién contrata y paga el viaje de lo comprado lo dice el contrato, y en una compra al exterior, el [Incoterm](../Comercio-exterior/incoterms.md). En EXW, «The seller has no obligation to the buyer to make a contract of carriage» (A4) y «It is up to the buyer to contract or arrange at its own cost for the carriage of the goods from the named place of delivery» (B4): el comprador maneja todo el flujo de entrada. En el otro extremo, DAP y DDP, el vendedor lleva la carga hasta destino, y en DAP la entrega es lista para descargar, así que la descarga queda del comprador; esas dos reglas no se leyeron en el texto de la ICC, sino en un resumen.

Para el sistema, eso cambia qué tiene que hacer el comprador (lectura de la base). Si el flete es suyo, contrata al transportista, elige el modo y paga el flete: todo lo de [costo del flete](costo-del-flete.md) y [modos de transporte](modos-de-transporte.md) le toca a la compra. Si es del proveedor, el comprador solo planifica la llegada y la sigue. Cuando el comprador junta en un recorrido las compras a varios proveedores cercanos, el viaje es un milk run, una de las formas de [consolidación](consolidacion-y-ruteo.md#las-formas-de-la-red).

## El aviso de despacho: saber antes qué llega

El aviso de despacho (despatch advice, ASN) es el mensaje del proveedor que dice qué mandó. En el estándar EANCOM de GS1 es el DESADV: «A message specifying details for goods despatched or ready for despatch under agreed conditions», y «should always be sent before goods are physically delivered». Según la misma ficha, cada unidad entregada (pallet, caja) «should be uniquely identified», y el mensaje relaciona un vendedor, un comprador y un punto de despacho con uno o varios destinos. En el estándar estadounidense X12 el equivalente es el mensaje 856.

La guía de GS1 UK sobre el aviso enumera lo que gana el que recibe: mejora la recepción, «Increases efficiency of receiving process through selective checking» (permite controlar solo una parte) y da «early notification of any delivery shortfalls». Con el código de cada pallet (el SSCC) informado de antemano, al llegar la carga se escanea la etiqueta y se cruza con lo avisado. El mensaje puede indicar además «a dock number or delivery bay».

Con el aviso, la entrega esperada deja de ser una orden de compra con fecha y pasa a ser un embarque concreto, con bultos y transportista (lectura de la base). Es lo que la base entiende por planificar las llegadas, 4.4.2.1.

## Turnos de descarga y espera de los camiones

El turno de descarga (dock appointment) asigna a cada camión una ventana en un muelle, para que las llegadas no se amontonen. Según Bartholdi y Hackman, no es raro que un depósito le dé al camión una ventana de 30 minutos; el detalle está en [recepción](../../Inventario-y-depositos/Operacion-del-deposito/recepcion.md#los-pasos-de-una-recepción).

La evidencia de que esperar cuesta viene de EE. UU. El inspector general del Departamento de Transporte estimó en 2018, con datos de 2013, que «a 15-minute increase in average dwell time—the total time spent by a truck at a facility—increases the average expected crash rate by 6.2 percent». El tiempo de permanencia medio en los datos que usó fue de 113 minutos, y cerca del 21 % de las paradas pasó las 2 horas. Las pérdidas anuales asociadas a la detención (la espera más allá del plazo pactado) son de «$1.1 billion to $1.3 billion» de ingresos para los choferes de carga completa. El mismo informe advierte que no hay datos confiables de toda la industria, porque casi todos miden solo el tiempo que pasa el límite del contrato (la detención), no el tiempo total en el lugar.

> [!NOTE] Sin fuente todavía: un estudio independiente de cuánto reducen la espera los turnos de descarga en un depósito (lo que se encontró son cifras de proveedores de software, sin método); datos de espera en muelles de la Argentina; cifras de EE. UU. posteriores a 2018.

## Medir el desempeño de la entrada

La actividad 4.4.2.3, «Monitor inbound delivery performance», es según el resumen de APQC «Overseeing the performance of an inbound delivery system». La base la lee como el espejo del [nivel de servicio logístico](../Despacho-y-entrega/nivel-de-servicio-logistico.md) de la salida: la misma pregunta de a tiempo y completo, con el proveedor en el lugar del despachante. SCOR DS tiene métricas para la entrada: RL.2.8 «Supplier Order Perfect Condition» y RS.3.8 «Receive Product Cycle Time».

El dato sale del cruce de tres fechas: la que confirmó el proveedor, la que dio el aviso de despacho y la de llegada real al muelle (lectura de la base). Con eso se separan dos culpas que se suelen mezclar: el proveedor que despachó tarde y el transportista que tardó. La primera alimenta la [evaluación de proveedores](../../Compras-y-abastecimiento/Proveedores/evaluacion-de-proveedores.md), de Compras; la segunda, el seguimiento del transportista, que en la salida el PCF nombra 4.4.4.2 «Track carrier delivery performance».

## El costo de llegada

El costo de llegada (landed cost) es lo que cuesta la mercadería puesta en el depósito: el precio más el flete, el seguro, los derechos y tasas, el despacho y la manipulación en destino. La lista es de un glosario de logística (DP World). La norma contable no usa la expresión; lo más cercano es el costo de compra de la NIC 2, que según el párrafo 11 comprende «the purchase price, import duties and other taxes (other than those subsequently recoverable by the entity from the taxing authorities), and transport, handling and other costs directly attributable to the acquisition». SCOR DS mide la parte logística con CO.3.13 «Inbound Freight and Duties». Los glosarios de logística no coinciden en desde qué lado se mira: algunos lo definen como el costo del vendedor para entregar al cliente; acá se usa el del comprador, como la NIC 2.

Como esos costos llegan en facturas distintas y después de la mercadería (el flete, el despacho, los gastos del banco por una [carta de crédito](../Comercio-exterior/carta-de-credito.md)), el sistema tiene que juntarlos sobre el embarque y repartirlos entre los artículos (lectura de la base). Cómo entran al costo del stock es de Contabilidad, en [costo de lo vendido](../../Contabilidad/Operaciones/costo-de-lo-vendido.md); cuánto se paga de impuestos en la importación, del tema [Impuestos](../../Impuestos/impuestos.md).

> [!NOTE] Sin fuente todavía: con qué criterio se reparten los costos de llegada entre los artículos de un embarque (por valor, por peso, por volumen); la NIC 2 no lo detalla en el párrafo 11.

## Lo que registra un sistema

Como criterio de la base, el flujo de entrada pide un registro que la orden de compra no tiene, la llegada esperada, colgado de una o varias órdenes:

- Qué llega: las líneas de las órdenes que cubre, con cantidades, y si hay aviso de despacho, los bultos con su código.
- Quién lo trae: el transportista, el modo y quién paga el flete según la condición de entrega.
- Cuándo: la fecha confirmada por el proveedor, la estimada de llegada (que se actualiza con el seguimiento), el turno asignado con su muelle y la llegada real.
- Estado: esperada, en tránsito, con turno, arribada, en descarga, recibida.
- Los costos de llegada que se le van sumando, para repartirlos sobre los artículos.

Al pasar a «arribada», la llegada se convierte en la recepción del depósito, que la cuenta y la guarda. Si es una importación, la llegada cuelga además de la [operación de comercio exterior](../Comercio-exterior/comercio-exterior.md#la-operación-de-comercio-exterior-como-registro), que tiene sus propios estados: entre que la operación figura «arribada» al país y la llegada al muelle están la aduana y el último tramo.
