---
resumen: >-
  La cotización y la licitación son las maneras de pedirles ofertas a varios proveedores y compararlas: el pedido de información sondea el mercado, el pedido de cotización pide precio y condiciones por algo bien especificado y el pedido de propuesta pide una solución. La oferta elegida se convierte en una orden de compra o en un contrato marco.
estado: borrador
estabilidad: semi
fuentes:
  - "CIPS, The thirteen steps of the procurement process, pasos 4 a 8: https://1prd-dxp.cips.org/intelligence-hub/procurement/procurement-process"
  - "APQC, Process Classification Framework 7.4 (2024), 4.2.3.3 «Solicit supplier quotes» y 4.2.2.2 «Certify and validate suppliers»: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "UK Government, The Sourcing Playbook, sección 10: https://www.gov.uk/government/publications/the-sourcing-and-consultancy-playbooks/the-sourcing-playbook-html"
  - "ERPNext, Request for Quotation (práctica de un sistema abierto): https://docs.frappe.io/erpnext/user/manual/en/request-for-quotation"
  - "Wikipedia, Request for quotation (consultada 2026-11-27): https://en.wikipedia.org/wiki/Request_for_quotation"
  - "Wikipedia, Reverse auction (consultada 2026-11-27): https://en.wikipedia.org/wiki/Reverse_auction"
  - "MIT Sloan Management Review, resumen del working paper de Sandy Jap (julio de 2001) sobre subastas inversas en línea: https://sloanreview.mit.edu/article/ebusiness-potential-pitfalls-of-eauctions (artículo leído completo; el working paper no)"
  - "Compras-y-abastecimiento/.investigacion/abastecimiento-estrategico.md (2026-11-27), secciones 0, 5 y 9"
  - "Compras-y-abastecimiento/.investigacion/fundamentos-y-contraria.md (2026-11-27), sección 2.4"
aliases: [cotización, licitación, pedido de cotización, solicitud de cotización, request for quotation, RFQ, pedido de propuesta, request for proposal, RFP, pedido de información, request for information, RFI, llamado a ofertas, invitation to tender, ITT, tender, RFx, concurso de precios, cuadro comparativo, comparativo de ofertas, cotización del proveedor, supplier quotation, subasta inversa, reverse auction, e-auction]
creado: 2026-11-27
revisado:
---

# Cotización y licitación

La cotización y la licitación son las maneras de pedirles ofertas a varios proveedores y compararlas: el pedido de información sondea el mercado, el pedido de cotización pide precio y condiciones por algo bien especificado y el pedido de propuesta pide una solución. La oferta elegida se convierte en una orden de compra o en un contrato marco.

Dentro de [Abastecimiento estratégico](abastecimiento-estrategico.md) es el paso en que la estrategia que salió de la [matriz de Kraljic](matriz-de-kraljic.md) se encuentra con el mercado. Le pide ofertas a proveedores que [Proveedores](../Proveedores/proveedores.md) tiene registrados o que se van a dar de alta, las compara por [costo total de adquisición](costo-total-de-adquisicion.md) y deja el terreno para la [negociación](negociacion-de-compras.md). Las compras del Estado, con la licitación pública como régimen legal, quedan fuera del tema.

## Una actividad partida entre lo transaccional y lo estratégico

El campo no se pone de acuerdo sobre dónde va este paso. APQC 7.4 pone «Solicit supplier quotes» (4.2.3.3) dentro de ordenar materiales y servicios, entre aprobar la [solicitud de compra](../Orden-de-compra/solicitud-de-compra.md) y emitir la [orden de compra](../Orden-de-compra/orden-de-compra.md). CIPS lo pone en la licitación, del paso 4 al 8 de su ciclo, antes de adjudicar un contrato.

Las dos lecturas describen casos distintos. Pedirle precio a un par de proveedores por cincuenta sillas es parte del trámite de una orden. Llamar a ofertas por todo el transporte del año es una decisión de categoría, con criterios fijados antes y un contrato al final (ejemplos de la base). La base trata los dos acá porque el objeto es el mismo (un pedido a varios proveedores y sus ofertas) y cambia solo el peso de la decisión.

## Información, cotización y propuesta

Los tres pedidos se distinguen por lo que se sabe de antemano:

| Pedido | Qué pide | Cuándo |
|---|---|---|
| Pedido de información (RFI) | Quiénes pueden abastecer y cómo, sin compromiso | Antes de decidir a quién invitar |
| Pedido de cotización (RFQ) | Precio y condiciones por algo bien especificado | La necesidad está definida: se compara sobre todo el costo |
| Pedido de propuesta (RFP) | Una solución y su precio | La necesidad está definida por el resultado, no por la especificación |

La tabla es criterio de la base. Las fuentes leídas sostienen partes: en CIPS, el sondeo del mercado y la selección de quién participa (pasos 4 y 6) van antes de emitir los documentos de la licitación (paso 7). Una definición secundaria llama al pedido de cotización «a business process in which a company or public entity requests a quote from a supplier», dice que «generally means the same thing as» el llamado a ofertas, y advierte que a menudo se usa uno donde correspondía otro tipo de pedido.

> [!NOTE] Sin fuente todavía: una definición primaria (CIPS, ISM o un libro de texto) que distinga el pedido de información, el de cotización y el de propuesta.

## El recorrido de una licitación

Los pasos de CIPS van de preparar a evaluar. Los nombres entre comillas son literales; las descripciones resumen la página:

1. «Pre-procurement market test and engagement»: sondear el mercado antes de comprometerse.
2. «Develop documentation PPQ and detailed spec»: la especificación detallada y el cuestionario previo (PPQ) para precalificar proveedores, que es una forma de homologación (APQC 4.2.2.2). La homologación también puede hacerse después de elegir, antes de la primera orden, y está en [alta de proveedor](../Proveedores/alta-de-proveedor.md).
3. «Supplier selection to participate in tender»: decidir quién recibe el pedido.
4. «Issue tender documents»: los pedidos de cotización y los documentos, con fecha límite.
5. «Bid and tender evaluation and validation»: evaluar contra criterios fijados antes, de forma transparente, mirando el costo de vida completa y con posibilidad de negociar.

Un sistema abierto muestra cómo se registra. El pedido de cotización nace de una solicitud de material y va a varios proveedores; «A submitted RFQ remains an invitation, not an order». Cada respuesta se carga como una cotización del proveedor, un comparador pone lado a lado el mismo artículo y cantidad, y la orden de compra se crea desde la cotización elegida. Son tres documentos distintos (pedido, cotización, orden) unidos por referencias.

## Cómo se comparan las ofertas

El error que señalan las fuentes es elegir por el precio. El comparador del mismo sistema aconseja pesar impuestos, flete, plazo de entrega, vigencia de la oferta, garantías, condiciones de pago y cumplimiento de la especificación. La guía de compras del gobierno británico es más tajante: el objetivo es «the most economically advantageous tender», «the key factor is whole life cost, not lowest purchase price», y en una tercerización compleja el costo «will be secondary to quality».

La misma guía advierte contra competir solo por precio, por las falsas economías que trae, y pide mandar a revisar las ofertas que estén más de un «10% lower than either the average of all bids or the Should Cost Model Estimate». Es una regla del sector público británico, útil como ejemplo de control. CIPS, por su parte, pide evaluar contra criterios fijados antes; cambiarlos después vuelve la comparación arbitraria, que es lectura de la base.

## La subasta inversa

En la subasta inversa, un comprador recibe ofertas de muchos proveedores que compiten bajando el precio. El estudio con método que se leyó es el de Jap, según el resumen de Sloan (no el working paper): seis subastas en línea, tres cerradas de una ronda y tres abiertas, de un fabricante de componentes automotrices, por USD 100 millones en contratos, entre 1999 y 2000. Las cerradas y las abiertas dieron ahorros potenciales parecidos, medidos contra el costo histórico y no contra el costo total. En las abiertas, los proveedores coincidieron más con que el proceso «will reduce my chances of earning a fair margin on the business», y hubo más desconfianza, menos información compartida y menos cooperación.

El mismo resumen recoge efectos en los dos sentidos. Un proveedor nuevo más barato puede subir el costo total a corto plazo, mientras el comprador aprende a trabajar con él. Y los proveedores se mostraron más dispuestos a invertir a medida del comprador; Jap concluye que las subastas pueden ser «a good wake-up call to your supply base» si no se abusa. Es una sola empresa y hace más de veinte años. La reducción de precio de 18 a 20 % que circula la informan los vendedores de la tecnología y no está verificada.

## Cuántas cotizaciones pedir

> [!NOTE] Sin fuente todavía: cuántas cotizaciones pedir según el monto, y a partir de qué monto se pasa de una compra directa a un pedido de cotización o a una licitación. La regla de «tres cotizaciones» que circula no tiene fuente leída. Los tramos de aprobación por monto están en [autorizaciones](../../Contabilidad/Control-interno/autorizaciones.md).
