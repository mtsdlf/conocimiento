---
resumen: >-
  Los impuestos al consumo gravan lo que una empresa vende y no lo que gana: el IVA, el impuesto a la venta minorista, los impuestos en cascada sobre los ingresos brutos y los específicos. La ley se los cobra a quien vende, pero el que los soporta, en principio, es quien consume.
estado: borrador
estabilidad: estable
fuentes:
  - "Directiva 2006/112/CE del Consejo, texto original (DO L 347, 11/12/2006), art. 1, copia del BOE: https://www.boe.es/doue/2006/347/L00001-00118.pdf"
  - "Williams, D., «Value-Added Tax», cap. 6 de Thuronyi (ed.), Tax Law Design and Drafting, vol. 1, FMI, 1996: https://www.imf.org/external/pubs/nft/1998/tlaw/eng/ch6.pdf"
  - "Keen, M., Targeting, Cascading, and Indirect Tax Design, IMF Working Paper WP/13/57, 2013: https://www.imf.org/external/pubs/ft/wp/2013/wp1357.pdf"
  - "Mirrlees y otros, Tax by Design, IFS/OUP, 2011, caps. 2 y 7 (leído por el ángulo de posición contraria): https://ifs.org.uk/sites/default/files/output_url_files/taxbydesign.pdf"
  - "Fullerton y Metcalf, Tax Incidence, NBER WP 8829, 2002 (leído por el ángulo de posición contraria): https://www.nber.org/system/files/working_papers/w8829/w8829.pdf"
  - "Código Fiscal de la Provincia de Buenos Aires, Ley 10.397 (t.o. 2011), art. 188: https://normas.gba.gob.ar/ar-b/ley/1986/10397/6417"
  - "Impuestos/.investigacion/impuestos-al-consumo.md (2026-11-27)"
  - "Impuestos/.investigacion/posicion-contraria.md (2026-11-27)"
aliases: [impuestos al consumo, impuestos indirectos, impuestos sobre bienes y servicios, consumption taxes, indirect taxes, taxes on goods and services, impuestos a las ventas, impuestos sobre las ventas]
creado: 2026-11-27
revisado:
---

# Impuestos al consumo

Los impuestos al consumo gravan lo que una empresa vende y no lo que gana: el IVA, el impuesto a la venta minorista, los impuestos en cascada sobre los ingresos brutos y los específicos. La ley se los cobra a quien vende, pero el que los soporta, en principio, es quien consume.

Son la vertical que decide qué impuesto lleva cada renglón de una factura. Reciben de [Obligación tributaria](../Obligacion-tributaria/obligacion-tributaria.md) el vocabulario (el [hecho imponible, la base y la alícuota](../Obligacion-tributaria/hecho-imponible-y-base.md), quién es [contribuyente y quién responsable](../Obligacion-tributaria/sujetos-del-impuesto.md)). Una parte se cobra por adelantado con [Recaudación en la fuente](../Recaudacion-en-la-fuente/recaudacion-en-la-fuente.md), y todo se liquida y se declara cada mes en [Cumplimiento](../Cumplimiento/cumplimiento.md). El otro gran grupo, el que grava la ganancia, está en [Impuestos a la renta](../Impuestos-a-la-renta/impuestos-a-la-renta.md).

## Cuatro formas de gravar una venta

Los impuestos al consumo se distinguen por la etapa de la cadena en que cobran y por si dejan descontar lo que se pagó antes.

| Tipo | Dónde cobra | Descuenta lo de las compras | Ejemplo |
|---|---|---|---|
| Valor agregado (IVA) | en cada etapa | sí: cada empresa resta el impuesto de sus compras | el IVA de la Unión Europea (Directiva 2006/112/CE) y el de Argentina |
| Venta minorista o final | solo en la venta al consumidor | no hace falta: las ventas entre empresas quedan afuera | el sales tax de los estados de EE. UU. |
| En cascada o sobre los ingresos brutos | en cada etapa | no: cada etapa paga sobre el precio, que ya trae el impuesto anterior | Ingresos Brutos en las provincias argentinas |
| Específicos o internos | en una etapa, sobre ciertos productos | según el caso | combustibles (el Código Fiscal de Buenos Aires los nombra); otros ejemplos, sin fuente |

El IVA y el impuesto a la venta minorista buscan lo mismo: que el impuesto total sea una proporción fija del precio final. La Directiva europea del IVA lo dice como principio: un impuesto «exactamente proporcional al precio de los bienes y de los servicios, sea cual fuere el número de operaciones que se produzcan en el circuito de producción y distribución» (art. 1.2). El impuesto en cascada no lo logra: cuantas más etapas tiene un producto, más impuesto acumula. Por qué eso es un problema está en [impuesto a las ventas](impuesto-a-las-ventas.md).

Los específicos gravan un producto en particular (cómo se calculan no quedó registrado). En Argentina conviven con los otros: el Código Fiscal de la Provincia de Buenos Aires saca de la base de Ingresos Brutos «los importes correspondientes a impuestos internos, impuesto al Valor Agregado –débito fiscal-, impuesto sobre los Combustibles Líquidos y Gas Natural» (art. 188 a). Esta base no les dedica una nota.

> [!NOTE] Sin fuente todavía: un manual que trate los impuestos específicos e internos como grupo (qué gravan, cómo se calculan y cómo se combinan con el IVA).

## Quién paga y quién soporta

Quién paga tiene dos respuestas, y las dos son ciertas. La incidencia legal dice quién tiene que entregarle el impuesto al fisco: la empresa que vende. La incidencia económica dice de quién sale la plata al final.

En el diseño del IVA, la empresa es un recaudador. *Tax by Design* (según el informe de posición contraria, que lo leyó) lo resume así: el impuesto «is in effect imposed on the value of the final product but is collected in small chunks from each link in the supply chain», y «only VAT on retail sales cannot be reclaimed». Cada empresa cobra impuesto en sus ventas, resta el de sus compras y entrega la diferencia; solo el consumidor final no tiene a quién trasladarlo.

> [!IMPORTANT]
> «El IVA lo paga el cliente» es cierto como diseño y como obligación legal, pero es una simplificación económica. Según Fullerton y Metcalf (según el informe de posición contraria, que los leyó), quién soporta un impuesto depende de cuánto reaccionan compradores y vendedores al precio, no de quién tiene la obligación legal: parte del impuesto puede terminar en un precio más bajo para el vendedor. Además, la empresa sí soporta el IVA de sus compras cuando vende algo exento, cuando no puede usar el crédito o cuando no lo puede trasladar al precio (ver [IVA](iva.md)).

En un impuesto en cascada la empresa tampoco recupera lo que pagaron las etapas anteriores: ese impuesto queda en su costo y sube el precio siguiente. Por eso, para una empresa, un impuesto en cascada se parece más a un costo que a un cobro por cuenta de otro (inferencia de esta base sobre la definición de cascada de Keen: «the levying of tax on items that have already been taxed»).

## Qué hace la empresa con un impuesto al consumo

Para la empresa que vende, cualquier impuesto al consumo sigue el mismo recorrido:

1. Decide si la venta está alcanzada, a qué alícuota y en qué lugar se considera hecha. Eso depende del producto, de quién compra y de dónde está (ver [lugar de la operación](lugar-de-la-operacion.md)).
2. Lo muestra en el [comprobante fiscal](../Cumplimiento/comprobante-fiscal.md), separado o incluido según quién compra.
3. Lo registra en los [registros fiscales](../Cumplimiento/registros-fiscales.md), con el de sus compras si el impuesto da crédito.
4. Liquida el período, resta lo que ya le cobraron por adelantado ([pagos a cuenta](../Recaudacion-en-la-fuente/pagos-a-cuenta.md)) y [declara y paga](../Cumplimiento/declaracion-y-pago.md).

Cómo se registra en la contabilidad (las cuentas de impuesto a pagar y a recuperar) es del tema [Contabilidad](../../Contabilidad/contabilidad.md). Cómo lo calcula un sistema, renglón por renglón y con la alícuota vigente a la fecha, es del tema Software de gestión, todavía no escrito.

## Fallas frecuentes

- Tratar el impuesto como precio. Si el sistema guarda el precio con impuesto incluido y la alícuota cambia, el margen se mueve sin que nadie lo decida. El precio neto y el impuesto son dos datos.
- Aplicar la alícuota del producto sin mirar al cliente ni al lugar. La misma venta lleva impuesto o no según quién compra y adónde va (ver [lugar de la operación](lugar-de-la-operacion.md)).
- Borrar o editar una factura para corregir el impuesto. Un descuento o una devolución posterior cambia la base del impuesto y se documenta con una nota de crédito (ver [IVA](iva.md#el-descuento-y-la-nota-de-crédito-cambian-la-base)).
- Confundir un impuesto en cascada con uno que da crédito. El primero es costo; el segundo, en principio, no.

Estas fallas son inferencia de esta base a partir de las fuentes de cada nota.

## Notas de la vertical

- [IVA](iva.md) — el impuesto al valor agregado: débito menos crédito, exento frente a tasa cero, prorrata, saldo a favor, alícuotas reducidas y umbrales. Leelo primero.
- [Impuesto a las ventas](impuesto-a-las-ventas.md) — el que grava solo la venta al consumidor y el que cobra en cada etapa sin crédito (en cascada), con la evidencia de por qué el segundo distorsiona.
- [Lugar de la operación](lugar-de-la-operacion.md) — destino u origen: la exportación sin impuesto, la importación gravada en la aduana y los servicios del exterior, incluidos los digitales.
- [IVA en Argentina](iva-en-argentina.md) — la ley argentina: alícuotas, crédito fiscal, prorrata, saldos, servicios digitales del exterior e IVA Simple.
- [Ingresos Brutos](ingresos-brutos.md) — el impuesto provincial argentino sobre lo facturado, sus alícuotas por actividad, el Convenio Multilateral y el monotributo unificado.

Para leer más: el capítulo 6 de *Tax Law Design and Drafting* del FMI (David Williams), secciones I y II, ubica el IVA frente a los demás impuestos al consumo y explica sus dos principios territoriales; conviene leerlo antes que cualquier ley nacional.
