---
resumen: >-
  El lugar de la operación es la regla que decide qué país (o qué provincia) cobra el impuesto al consumo de una venta que cruza una frontera. Casi todos siguen el principio de destino: la exportación sale sin impuesto, la importación paga en la aduana y el servicio del exterior lo paga el cliente local o un proveedor extranjero inscripto.
estado: borrador
estabilidad: estable
fuentes:
  - "Williams, D., «Value-Added Tax», cap. 6 de Thuronyi (ed.), Tax Law Design and Drafting, vol. 1, FMI, 1996, sec. II (ámbito territorial), sec. VII.D y nota 89: https://www.imf.org/external/pubs/nft/1998/tlaw/eng/ch6.pdf"
  - "Directiva 2006/112/CE del Consejo, texto original (DO L 347, 11/12/2006), arts. 146, 169 y 196, copia del BOE: https://www.boe.es/doue/2006/347/L00001-00118.pdf"
  - "Comisión Europea, One Stop Shop: https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en"
  - "Keen, M., Targeting, Cascading, and Indirect Tax Design, IMF Working Paper WP/13/57, 2013: https://www.imf.org/external/pubs/ft/wp/2013/wp1357.pdf"
  - "South Dakota v. Wayfair, Inc., Corte Suprema de EE. UU., 21/06/2018 (Cornell LII): https://www.law.cornell.edu/supremecourt/text/17-494"
  - "Ley de IVA de Argentina, t.o. 1997, art. 1, texto actualizado en InfoLEG: https://servicios.infoleg.gob.ar/infolegInternet/anexos/40000-44999/42701/texact.htm"
  - "Impuestos/.investigacion/impuestos-al-consumo.md (2026-11-27)"
aliases: [lugar de la operación, lugar de realización, place of supply, principio de destino, principio de origen, destination principle, origin principle, exportación a tasa cero, IVA de importación, inversión del sujeto pasivo, reverse charge, autoliquidación, servicios digitales, proveedor extranjero, registro simplificado, OSS, ventanilla única, plataformas, deemed supplier, proveedor presunto]
creado: 2026-11-27
revisado:
---

# Lugar de la operación

El lugar de la operación es la regla que decide qué país (o qué provincia) cobra el impuesto al consumo de una venta que cruza una frontera. Casi todos siguen el principio de destino: la exportación sale sin impuesto, la importación paga en la aduana y el servicio del exterior lo paga el cliente local o un proveedor extranjero inscripto.

Es parte del mecanismo del [IVA](iva.md), pero la misma pregunta aparece en el [impuesto a las ventas](impuesto-a-las-ventas.md) (qué estado puede exigir que se cobre) y en [Ingresos Brutos](ingresos-brutos.md) (qué provincia se queda con qué parte). Quién es contribuyente y qué es la residencia está en [sujetos del impuesto](../Obligacion-tributaria/sujetos-del-impuesto.md).

## Destino u origen

El capítulo del FMI sobre el IVA presenta los dos principios: el de origen grava la operación «if the transaction originates or is created within the state», y el de destino «if it is destined for consumption in the state». Si un país exporta a otro, con origen cobra el que vende y con destino cobra el que consume.

Si dos países usan principios distintos, la misma venta paga dos veces o ninguna. Por eso hace falta que coincidan, y en la práctica coinciden: «with limited exceptions, states have adopted the destination basis as the primary basis… This requires a charge to VAT on all transactions occurring within the state and also on all imports to the state». Por qué la mayoría eligió destino no quedó registrado en lo leído; lo que sí dice el capítulo, para los servicios, es que la neutralidad exige gravar igual al servicio de afuera y al de adentro.

## Exportar a tasa cero, importar con impuesto

El principio de destino pide dos cosas en la frontera.

La exportación sale limpia. No alcanza con no cobrar IVA en la venta al exterior: hay que devolver el que pagaron los insumos. El FMI: «The destination principle calls not only for removing a direct charge to VAT from exports… but also for removing any VAT indirectly imposed on those supplies in the form of input tax paid by a supplier. Only if the input tax is rebated will the goods leave the state free of VAT». Por eso la exportación va a tasa cero (o «exenta con crédito»: la Directiva europea la exime en el art. 146 y da derecho a deducir en el art. 169 b). La diferencia está en [IVA](iva.md#exento-no-es-lo-mismo-que-tasa-cero).

La consecuencia para el exportador es, por inferencia de esta base, un saldo a favor casi permanente: vende sin débito y compra con crédito. Las exportaciones figuran entre las causas de saldo que cita Harrison y Krelove; que el fisco lo devuelva a tiempo es lo que decide si la exportación de verdad sale sin impuesto. Un impuesto en cascada no puede hacer esto: el impuesto de las etapas anteriores ya está en el costo y nadie lo devuelve, como recuerda Keen (ver [impuesto a las ventas](impuesto-a-las-ventas.md#por-qué-los-organismos-lo-critican)).

La importación paga en la aduana. El FMI: «The destination principle requires a charge to VAT to be placed on all imports», con las reglas de la aduana para decidir qué es un bien y cuándo entra. El importador paga el IVA al despachar, junto con los derechos, y si es un contribuyente inscripto lo toma como crédito. Con los bienes es fácil: la mercadería misma garantiza el pago. El trámite de aduana es del tema Cadena de suministro y logística, todavía no escrito.

## Servicios: dónde se consume

Los servicios no pasan por la aduana. Según el FMI, el lugar es difícil de determinar, y los bienes importados garantizan el pago pero los servicios no. Que el país del cliente no tenga cómo obligar a un proveedor que no está en su territorio es inferencia de esta base. Y si no lo grava, el proveedor extranjero compite con ventaja: «fairness and neutrality require that services that originate overseas be taxed in the same way as services that originate in the state».

Hay dos soluciones, según quién sea el cliente.

### Cliente empresa: inversión del sujeto pasivo

Cuando el cliente es un contribuyente inscripto, se le traslada la obligación: el cliente calcula el IVA del servicio que importó como si se lo hubiera vendido a sí mismo, lo declara como débito y, si tiene derecho, lo toma como crédito en la misma declaración. El FMI la define así: «Reverse charging applies where the person receiving the supply is deemed also to be the supplier so that a charge to VAT may be applied to it». En la Unión Europea, la Directiva designa deudor al destinatario sujeto pasivo cuando el prestador no está establecido en ese Estado (art. 196).

Para una empresa con derecho a crédito total, el efecto en caja es cero: débito y crédito se cancelan. Sirve para que una empresa exenta, o con prorrata, no tenga ventaja en comprar servicios afuera (inferencia de esta base).

### Cliente consumidor: el proveedor extranjero se inscribe

Un consumidor no presenta declaraciones, así que no puede autoliquidar. La salida es que el proveedor del exterior se inscriba en el país del cliente y cobre el IVA local. Para que eso sea viable, los países ofrecen una inscripción simplificada.

La Unión Europea tiene la One Stop Shop (OSS) desde el 1 de julio de 2021, que reemplazó al mini One Stop Shop del 1 de enero de 2015. Permite declarar y pagar en un solo Estado el IVA de las ventas a consumidores de todos los demás. Hay un umbral anual de EUR 10 000 para los servicios a consumidores de otros Estados. La variante para importaciones (IOSS) cubre envíos de un valor intrínseco que no exceda EUR 150.

### Las plataformas como recaudadoras

Cuando la venta pasa por un mercado en línea, una tienda de aplicaciones o un agregador de pagos, es más fácil cobrarle a ese intermediario que a miles de vendedores. La Unión Europea trata como proveedor, a efectos del IVA, a quien facilita la venta «through the use of an electronic interface (e.g. marketplace, platform, portal etc.)»: el llamado deemed supplier o proveedor presunto.

Otros países usan al intermediario del pago. Argentina, por ejemplo, grava los servicios digitales del exterior que se usan en el país y, cuando el pago pasa por un intermediario local, lo convierte en agente de percepción; los detalles están en [IVA en Argentina](iva-en-argentina.md#servicios-digitales-del-exterior). Qué es un agente de percepción está en [agente de recaudación](../Recaudacion-en-la-fuente/agente-de-recaudacion.md).

> [!NOTE] Sin fuente todavía: las *International VAT/GST Guidelines* de la OCDE (2017), que son la referencia internacional de estas reglas (destino para servicios e intangibles, jurisdicción del cliente en las ventas entre empresas, inscripción simplificada para proveedores extranjeros y papel de las plataformas). El sitio de la OCDE bloqueó la descarga y esta nota no las cita.

## En un impuesto a las ventas y entre provincias

El impuesto a la venta minorista de EE. UU. sigue el destino y tiene el mismo problema con el vendedor de afuera. Hasta 2018 un estado no podía obligar a cobrar a quien no tenía presencia física; en *South Dakota v. Wayfair* la Corte dejó sin efecto esa regla, y la ley en juego usaba un umbral económico (más de USD 100.000 o 200 operaciones al año en el estado), como cuenta [impuesto a las ventas](impuesto-a-las-ventas.md#nexus-a-quién-se-le-puede-exigir-que-cobre).

Dentro de un país, un impuesto provincial necesita su propia regla de reparto. En Argentina, el Convenio Multilateral reparte la base de Ingresos Brutos entre provincias con coeficientes de ingresos y gastos, y atribuye las ventas a distancia al domicilio del comprador ([Ingresos Brutos](ingresos-brutos.md)).

## Fallas frecuentes

Inferencia de esta base sobre lo anterior.

- Facturar con IVA local una exportación. El cliente del exterior no lo puede recuperar y el precio deja de competir.
- No autoliquidar el servicio importado. Para una empresa exenta o con prorrata, es impuesto que debía y no pagó.
- Decidir el lugar por el domicilio del proveedor. Con destino, lo que cuenta es dónde se usa o quién es el cliente, y cada país tiene presunciones propias (la dirección IP, la tarjeta, la dirección de facturación).

Para leer más: el capítulo 6 de *Tax Law Design and Drafting*, sección II («origin principle and destination principle») y sección VII.D («Zero Rating Exports and International Supplies»). Para el caso europeo vigente, la página de la One Stop Shop de la Comisión Europea.
