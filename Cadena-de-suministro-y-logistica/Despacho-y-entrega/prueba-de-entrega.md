---
resumen: >-
  La prueba de entrega es la constancia de que la mercadería llegó a su destinatario: quién la recibió, cuándo, y si la recibió conforme o con observaciones. Cierra el despacho, abre el reclamo cuando llegó menos, dañado o tarde, y en el transporte por carretera entre países del CMR fija plazos cortos para dejar las reservas.
estado: vigente
estabilidad: estable
fuentes:
  - "Wikipedia, Proof of delivery (según el resumen): https://en.wikipedia.org/wiki/Proof_of_delivery"
  - "Naciones Unidas, United Nations Treaty Series vol. 399, n.º 5742: Convention on the Contract for the International Carriage of Goods by Road (CMR), Ginebra, 19 de mayo de 1956, texto oficial en inglés, capítulo V (arts. 30 a 33) y arts. 17, 19 y 23: https://treaties.un.org/doc/Publication/UNTS/Volume%20399/volume-399-I-5742-English.pdf"
  - "Facultad de Derecho de la Universidad de Oslo, CMR consolidado con el Protocolo de 1978 (transcripción del mismo texto), arts. 17, 19, 23, 30 a 32: https://jus.uio.no/english/services/library/treaties/07/7-02/cmr-consolidated.html"
  - "UN Treaty Collection, estado del CMR (58 partes al 27-11-2026; según el resumen): https://treaties.un.org/pages/ViewDetails.aspx?src=TREATY&mtdsg_no=XI-B-11&chapter=11"
  - "UN Treaty Collection, Protocolo Adicional sobre la carta de porte electrónica (e-CMR), Ginebra, 20 de febrero de 2008, estado y entrada en vigor (según el resumen): https://treaties.un.org/pages/ViewDetails.aspx?src=TREATY&mtdsg_no=XI-B-11-b&chapter=11"
  - "Odoo 17.0, modelo de transferencias (campos de firma, fechas, entrega pendiente y devolución): https://raw.githubusercontent.com/odoo/odoo/17.0/addons/stock/models/stock_picking.py"
  - "ERPNext, definición de Delivery Stop: https://raw.githubusercontent.com/frappe/erpnext/develop/erpnext/stock/doctype/delivery_stop/delivery_stop.json"
  - "Apache OFBiz, datos semilla de producto, motivos de rechazo al recibir (RejectionReason): https://raw.githubusercontent.com/apache/ofbiz-framework/trunk/applications/datamodel/data/seed/ProductSeedData.xml"
  - "Cadena-de-suministro-y-logistica/.investigacion/despacho-y-entrega.md (componente prueba-de-entrega)"
  - "Cadena-de-suministro-y-logistica/.investigacion/despacho-y-entrega-2.md (componente prueba-de-entrega)"
aliases: [prueba de entrega, POD, proof of delivery, prueba de entrega electrónica, ePOD, conformidad, remito conformado, entrega conformada, firma de conformidad, recibí conforme, entrega fallida, failed delivery, diferencia en destino, faltante, daño en tránsito, reservas al recibir, reserva del destinatario, CMR, carta de porte, consignment note, e-CMR]
creado: 2026-11-27
revisado: 2026-11-27
---

# Prueba de entrega

La prueba de entrega es la constancia de que la mercadería llegó a su destinatario: quién la recibió, cuándo, y si la recibió conforme o con observaciones. Cierra el despacho, abre el reclamo cuando llegó menos, dañado o tarde, y en el transporte por carretera entre países del CMR fija plazos cortos para dejar las reservas.

Es el último paso de [Despacho y entrega](despacho-y-entrega.md): el [despacho](despacho.md) se cierra con ella. Lo que el destinatario rechaza o devuelve sigue por [logística inversa](logistica-inversa.md), y la fecha y la cantidad que registra son las que usa el [nivel de servicio logístico](nivel-de-servicio-logistico.md) para decir si se entregó a tiempo y completo.

## Qué prueba la constancia

Una fuente secundaria la define como «a document that substantiates that goods have been delivered to their intended recipient». La misma fuente menciona la firma del destinatario y la prueba electrónica (ePOD), que puede intercambiar correcciones. En la Argentina, el documento que viaja con la mercadería es el remito, y la base lee el remito firmado como la constancia corriente; las reglas del remito están en [Inventario y depósitos en la Argentina](../../Inventario-y-depositos/inventario-y-depositos-en-argentina.md).

La constancia sirve para dos cosas distintas (lectura de la base). Frente al cliente, prueba que se cumplió la entrega y habilita a facturar o a cobrar. Frente al transportista, fija en qué estado llegó la carga, y de eso depende si se le puede reclamar.

## Tres resultados posibles

Cada intento de entrega termina en uno de tres resultados. La clasificación es de la base; las fuentes leídas no traen una.

| Resultado | Qué pasa | Qué deja registrado |
|---|---|---|
| Entrega conforme | el destinatario recibe todo y firma sin observaciones | quién, cuándo, la firma |
| Entrega con diferencia | recibe, pero falta algo, llegó dañado o sobra | lo anterior, más la diferencia por renglón y bulto, el motivo y las reservas |
| Entrega fallida | no se entregó: no había nadie, la dirección estaba mal, el destinatario rechazó la carga | el motivo, la fecha del intento y qué sigue (reintento, devolución al origen) |

Un sistema abierto trae como motivos de rechazo al recibir «Damaged», «Not Ordered» y «Over Shipped», entre otros. Lo que se rechaza vuelve por [logística inversa](logistica-inversa.md); lo que falta se reclama al transportista o se repone con otra entrega.

> [!NOTE] Sin fuente todavía: cómo se manejan la entrega fallida y los reintentos (cuántos, en qué plazo, quién paga), y una clasificación de motivos de diferencia con su responsable. Ninguno de los sistemas abiertos consultados tiene un estado de entrega fallida.

## Las reservas en el CMR

Reserva, acá, es la observación que deja quien recibe sobre un faltante, un daño o una demora. No es la [reserva](../../Inventario-y-depositos/Operacion-del-deposito/reserva.md) de stock de Inventario.

El CMR (Convention on the Contract for the International Carriage of Goods by Road, Ginebra, 19 de mayo de 1956) es el convenio que rige el contrato de transporte internacional de mercadería por carretera entre los países que lo ratificaron. Tiene 58 partes según la colección de tratados de las Naciones Unidas, consultada el 27 de noviembre de 2026. No rige el transporte dentro de un país ni los otros modos: el aéreo y el marítimo tienen sus propios plazos, que no se investigaron. Es útil como ejemplo de cómo una norma convierte la firma de conformidad en prueba.

Hay una sola fuente independiente: el texto oficial en la colección de tratados de las Naciones Unidas, capítulo V, que es lo que hay que leer. Una transcripción universitaria da las mismas palabras, pero es una copia del mismo instrumento. Lo que sigue no es asesoramiento legal; para un caso real, hay que leer el texto vigente y consultar a quien sepa del derecho aplicable.

El artículo 30 pone la carga sobre quien recibe. Si no deja reservas a tiempo, recibir vale como prueba de que todo llegó bien:

> «If the consignee takes delivery of the goods without duly checking their condition with the carrier or without sending him reservations giving a general indication of the loss or damage, not later than the time of delivery in the case of apparent loss or damage and within seven days of delivery, Sundays and public holidays excepted, in the case of loss or damage which is not apparent, the fact of his taking delivery shall be prima facie evidence that he has received the goods in the condition described in the consignment note. In the case of loss or damage which is not apparent the reservations referred to shall be made in writing.» (art. 30, párr. 1)

Para la demora el plazo es otro: «No compensation shall be payable for delay in delivery unless a reservation has been sent in writing to the carrier, within twenty-one days from the time that the goods were placed at the disposal of the consignee.» (art. 30, párr. 3). Y el día de la entrega no se cuenta: «In calculating the time-limits provided for in this article the date of delivery, or the date of checking, or the date when the goods were placed at the disposal of the consignee, as the case may be, shall not be included.» (art. 30, párr. 4).

| Qué pasó | Cuándo dejar la reserva | Cómo |
|---|---|---|
| Pérdida o daño aparente | a más tardar en el momento de la entrega | el texto no exige forma escrita |
| Pérdida o daño no aparente | dentro de los siete días de la entrega, sin domingos ni feriados | por escrito |
| Demora | dentro de los veintiún días desde que la mercadería quedó a disposición | por escrito |

La tabla resume el artículo 30; el texto literal manda.

## Cuándo prescribe el reclamo

El artículo 32 fija el plazo para demandar: «The period of limitation for an action arising out of carriage under this Convention shall be one year. Nevertheless, in the case of wilful misconduct, or such default as in accordance with the law of the court or tribunal seised of the case, is considered as equivalent to wilful misconduct, the period of limitation shall be three years.» (art. 32, párr. 1).

El plazo empieza a correr según el caso: «(a) In the case of partial loss, damage or delay in delivery, from the date of delivery; (b) In the case of total loss, from the thirtieth day after the expiry of the agreed time-limit or where there is no agreed time-limit from the sixtieth day from the date on which the goods were taken over by the carrier; (c) In all other cases, on the expiry of a period of three months after the making of the contract of carriage.» Un reclamo escrito lo suspende: «A written claim shall suspend the period of limitation until such date as the carrier rejects the claim by notification in writing and returns the documents attached thereto.» (art. 32, párr. 2). Otro reclamo por lo mismo no lo vuelve a suspender.

El transportista responde, según el artículo 17, por la pérdida y el daño «occurring between the time when he takes over the goods and the time of delivery, as well as for any delay in delivery». La prueba de entrega marca el final de ese tramo.

## Firma, foto y posición

La firma en papel o en una pantalla es la prueba que registran los sistemas. Uno de los sistemas abiertos guarda en el documento de salida una firma como imagen, con una marca derivada de si está firmada, y la fecha en que se hizo la transferencia. Otro guarda en cada parada del viaje la latitud y la longitud, pero son las de la parada planificada; su definición no dice que se capturen al entregar.

Para la carta de porte electrónica en el CMR existe el Protocolo Adicional de Ginebra del 20 de febrero de 2008 (e-CMR), en vigor desde el 5 de junio de 2011 según el registro de las Naciones Unidas; su texto no se leyó.

> [!NOTE] Sin fuente todavía: una fuente que no sea de un vendedor sobre la foto y la geolocalización como prueba de entrega, y sobre su valor como evidencia. Tampoco se leyeron el texto del e-CMR ni la norma europea de firma electrónica.

## Lo que se guarda de cada entrega

Del texto del CMR se deduce qué hace falta para reclamar; el esquema es inferencia de la base, no un modelo publicado:

- El intento: fecha y hora, resultado (conforme, con diferencia, fallida) y, si falló, el motivo.
- Quién recibió: nombre, documento o relación con el destinatario, y la firma.
- La puesta a disposición: la fecha en que la mercadería quedó a disposición del destinatario, de donde corren los veintiún días por demora y la prescripción.
- Las reservas: si hubo, su texto, su fecha, si fueron por escrito y si se verificó la carga junto con el transportista.
- La diferencia: por renglón y por bulto (el SSCC del [despacho](despacho.md)), la cantidad, el tipo (faltante, daño, sobrante) y el motivo.
- Lo que sigue: un vínculo al despacho pendiente por lo que faltó o a la devolución por lo rechazado. En un sistema abierto, el documento de salida guarda los dos vínculos: uno al pendiente de lo no enviado y otro a la devolución.

La constancia, como el despacho, es un hecho que no se edita: una corrección es otro registro (criterio de la base).
