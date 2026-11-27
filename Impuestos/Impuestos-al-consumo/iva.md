---
resumen: >-
  El IVA (impuesto al valor agregado) es un impuesto al consumo que se cobra en cada etapa de la cadena: cada empresa suma el impuesto a sus ventas (débito fiscal), resta el que le facturaron en sus compras (crédito fiscal) y entrega la diferencia, de modo que el total equivale al impuesto sobre el precio final.
estado: borrador
estabilidad: estable
fuentes:
  - "Directiva 2006/112/CE del Consejo, texto original (DO L 347, 11/12/2006), arts. 1, 90, 93, 97 a 99, 168, 169, 173, 174, 183 y 285, copia del BOE: https://www.boe.es/doue/2006/347/L00001-00118.pdf"
  - "Williams, D., «Value-Added Tax», cap. 6 de Thuronyi (ed.), Tax Law Design and Drafting, vol. 1, FMI, 1996, secs. II.B, V y VII: https://www.imf.org/external/pubs/nft/1998/tlaw/eng/ch6.pdf"
  - "Keen, M., Targeting, Cascading, and Indirect Tax Design, IMF Working Paper WP/13/57, 2013: https://www.imf.org/external/pubs/ft/wp/2013/wp1357.pdf"
  - "Harrison y Krelove, VAT Refunds: A Review of Country Experience, IMF WP/05/218, 2005 (leído por el ángulo de posición contraria): https://www.imf.org/external/pubs/ft/wp/2005/wp05218.pdf"
  - "Mirrlees y otros, Tax by Design, IFS/OUP, 2011, cap. 7 (leído por el ángulo de posición contraria): https://ifs.org.uk/sites/default/files/output_url_files/taxbydesign.pdf"
  - "Impuestos/.investigacion/impuestos-al-consumo.md (2026-11-27)"
aliases: [IVA, impuesto al valor agregado, impuesto al valor añadido, VAT, value-added tax, GST, goods and services tax, débito fiscal, crédito fiscal, output tax, input tax, tasa cero, zero rate, zero-rating, exento, exención, prorrata, pro rata, saldo a favor de IVA, devolución de IVA, alícuota reducida, umbral de inscripción, método de crédito por factura, credit-invoice method]
creado: 2026-11-27
revisado:
---

# IVA

El IVA (impuesto al valor agregado) es un impuesto al consumo que se cobra en cada etapa de la cadena: cada empresa suma el impuesto a sus ventas (débito fiscal), resta el que le facturaron en sus compras (crédito fiscal) y entrega la diferencia, de modo que el total equivale al impuesto sobre el precio final.

Es el impuesto al consumo que más toca a un sistema de gestión, porque aparece en cada factura (lectura de esta base; no se leyó una fuente que diga cuántos países lo aplican). Ver [impuestos al consumo](impuestos-al-consumo.md). Francia lo introdujo como impuesto nacional en 1954, según el capítulo del FMI.

## Débito menos crédito: el método de la factura

La Directiva europea del IVA describe el mecanismo así: «En cada operación será exigible el IVA, liquidado sobre la base del precio del bien o del servicio gravados al tipo impositivo aplicable a dichos bienes y servicios, previa deducción del importe de las cuotas impositivas devengadas que hayan gravado directamente el coste de los diversos elementos constitutivos del precio» (art. 1.2).

En la práctica, cada período la empresa hace una resta:

- Débito fiscal: el IVA que cobró en sus ventas. Se calcula sobre el precio neto, a la alícuota vigente cuando nace el impuesto (art. 93 de la Directiva).
- Crédito fiscal: el IVA que le facturaron en sus compras, en la medida en que las use para hacer operaciones gravadas (art. 168).
- Saldo: si el débito es mayor, la diferencia se paga; si es menor, queda un saldo a favor.

Se llama método de crédito por factura porque la factura del proveedor prueba el derecho a restar; por eso el [comprobante fiscal](../Cumplimiento/comprobante-fiscal.md) muestra el IVA separado cuando el comprador puede usarlo.

## Una cadena de tres etapas

Un ejemplo con una alícuota del 21 % y precios netos de impuesto (cifras de esta base, para ilustrar):

| Etapa | Vende a (neto) | Débito | Crédito | Paga al fisco |
|---|---|---|---|---|
| Productor de materia prima | 100 | 21 | 0 | 21 |
| Fabricante | 250 | 52,50 | 21 | 31,50 |
| Comercio minorista | 400 | 84 | 52,50 | 31,50 |
| **Total** | | | | **84** |

El fisco recibe 84, el 21 % del precio final de 400. Cada etapa paga el 21 % de lo que agregó (150 el fabricante, 150 el comercio). El consumidor paga 484 y no tiene a quién trasladar el IVA: por eso se dice que lo soporta él.

## Exento no es lo mismo que tasa cero

Las dos dejan una venta sin IVA, pero tratan distinto el impuesto de las compras. El capítulo del FMI lo explica así: la tasa cero vuelve a la venta «"taxable" in a technical sense and therefore achieves the objective of bringing these transactions within the operation of the VAT credit for input tax, which an exemption does not. This is because a VAT credit is allowed only for inputs to be used in making taxable supplies». Por eso a la tasa cero también se la llama «exempt with credit».

| | Exenta | Tasa cero |
|---|---|---|
| IVA en la venta | no | no (0 %) |
| Crédito por el IVA de las compras | no | sí |
| Dónde se usa | según el país; el FMI ejemplifica con los servicios bancarios | sobre todo exportaciones |

Sobre la cadena de arriba, si el fabricante estuviera exento, no cobraría IVA pero tampoco recuperaría los 21 de su compra, que pasarían a su costo. El comercio compraría sin crédito y pagaría 84 sobre su venta. El fisco recibiría 21 + 84 = 105 en lugar de 84: el impuesto de la primera etapa quedó pegado y gravado de nuevo. Si el fabricante tuviera tasa cero, recuperaría los 21 y el total volvería a 84 (aritmética de esta base).

Por eso una exención en el medio de la cadena perjudica a quien le compra al exento; Keen lo resume: «Even the best designed VATs embody some degree of cascading in the form of 'exemptions'». También tuerce decisiones: un banco exento que contrata guardias no recupera su IVA, así que le conviene tomarlos como empleados, y el FMI concluye que «Widespread exemptions can therefore undermine the integrity of the VAT as a whole».

La tasa cero dentro del país, según el mismo capítulo, «is widely viewed as inappropriate, because it amounts to a subsidy». Su uso aceptado es la exportación (ver [lugar de la operación](lugar-de-la-operacion.md)), que la Unión Europea llama «exenta» (art. 146) pero con derecho a deducir (art. 169 b).

## Prorrata: cuando se vende gravado y exento a la vez

Quien vende gravado y exento no toma todo el crédito de las compras que sirven a las dos: lo asignable se asigna, y del resto se toma la proporción de las gravadas.

La Directiva lo dice así: «sólo se admitirá la deducción por la parte de las cuotas del IVA que sea proporcional a la cuantía de las operaciones primeramente enunciadas» (art. 173.1). La proporción es una fracción (art. 174.1): arriba, el volumen de negocios anual sin IVA de las operaciones con derecho a deducción; abajo, ese mismo más el de las que no lo tienen.

Una empresa que factura 600 gravado y 400 exento toma el 60 % del IVA de sus gastos comunes (cifras de esta base); se estima en el año y se ajusta al cierre. La versión argentina está en [IVA en Argentina](iva-en-argentina.md).

## Saldo a favor y devolución

Cuando el crédito supera al débito, la Directiva deja que cada país elija: «podrán trasladar el excedente al período impositivo siguiente, o bien proceder a la devolución» (art. 183). Las causas típicas son exportar, invertir en bienes de capital, la estacionalidad o vender con una alícuota menor a la de las compras. Harrison y Krelove, en su documento del FMI (que esta base conoce por el informe de posición contraria, no por lectura directa), llaman a la devolución «the "Achilles heel" of the VAT». La distinción entre el saldo que nace de la mecánica del impuesto y el que nace de pagos de más o de retenciones está en [declaración y pago](../Cumplimiento/declaracion-y-pago.md#saldo-a-favor-técnico-o-de-libre-disponibilidad); cómo se usa lo retenido, en [pagos a cuenta](../Recaudacion-en-la-fuente/pagos-a-cuenta.md).

## Alícuotas reducidas y por qué se discuten

Muchos IVA tienen una alícuota general y alguna reducida (la Directiva europea de 2006 admitía hasta dos); para qué bienes, depende del país (no se leyó una fuente comparada). El texto de 2006 de la Directiva fijaba un mínimo: el tipo normal «no podrá ser inferior al 15 %» (art. 97, para 2006 a 2010), y los Estados «podrán aplicar uno o dos tipos reducidos» (art. 98.1) que no pueden ser inferiores «al 5 %» (art. 99.1). Esas reglas se modificaron después; esta base no leyó el texto consolidado vigente.

La alícuota reducida se defiende como ayuda a los hogares pobres; Keen lo discute: «even poorly targeted spending may be a better way to support the poor than a reduced rate». Para un sistema, cada alícuota reducida es una regla más que depende del producto y de la fecha.

## Quién tiene que inscribirse: el umbral

La mayoría de los países no obliga a todos a cobrar IVA. Según el FMI, se fija «a minimum level or threshold» de actividad, medido sobre las ventas gravadas de un período; varía mucho entre países y se justifica porque cobrarles a los muy chicos cuesta más de lo que recauda. Quien está debajo suele poder inscribirse por su cuenta. La Directiva, en su texto de 2006, permitía franquicias como la de «5 000 euros» anuales del art. 285.

Quien queda debajo no cobra IVA ni recupera el de sus compras: según *Tax by Design* (por el informe de posición contraria), las empresas debajo del umbral británico «are in effect VAT exempt». En Argentina el lugar del umbral lo ocupa el [régimen simplificado](../Obligacion-tributaria/regimen-simplificado.md).

## El descuento y la nota de crédito cambian la base

Un descuento en la misma factura baja la base. Uno posterior (una bonificación, una devolución, una anulación) también (lectura de esta base: una nota de crédito reduce el débito de quien vendió y el crédito de quien compró).

La Directiva lo dice para la Unión Europea: «En los casos de anulación, rescisión, impago total o parcial o reducción del precio, después del momento en que la operación quede formalizada, la base imponible se reducirá en la cuantía correspondiente» (art. 90.1). La ley argentina presume que el descuento reduce el precio y el impuesto en la misma proporción ([IVA en Argentina](iva-en-argentina.md)).

Para un sistema (inferencia de esta base): el IVA del descuento va a la alícuota de la operación original, y un descuento sobre renglones de distinta alícuota se reparte entre ellas. Qué lleva una nota de crédito está en [comprobante fiscal](../Cumplimiento/comprobante-fiscal.md).

> [!NOTE] Sin fuente todavía: *Consumption Tax Trends* de la OCDE (cuántos países aplican IVA, con alícuotas y umbrales comparados) y *The Modern VAT* del FMI (2001).

Para leer más: el capítulo 6 de *Tax Law Design and Drafting* del FMI, secciones V y VII, explica por qué una exención rompe la cadena.
