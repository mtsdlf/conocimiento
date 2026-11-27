---
resumen: >-
  El riesgo de tipo de cambio es que un movimiento de la cotización cambie lo que la empresa va a cobrar o pagar en otra moneda, lo que muestran sus estados o lo que vale su negocio; se acota primero con la cobertura natural (cobrar y pagar en la misma moneda) y después con contratos como el forward.
estado: borrador
estabilidad: estable
fuentes:
  - "Wikipedia, Currency risk, como fuente terciaria (leído; cita a Levi 2005, Moffett, Stonehill y Eiteman 2009, Eun y Resnick 2011 y Hull 2003): https://en.wikipedia.org/wiki/Currency_risk"
  - "OpenStax, Principles of Finance, 20.3 Exchange Rates and Risk (leído): https://openstax.org/books/principles-finance/pages/20-3-exchange-rates-and-risk"
  - "Wikipedia, Natural hedge, como fuente terciaria (según su resumen): https://en.wikipedia.org/wiki/Natural_hedge"
  - "Wikipedia, Forward contract, como fuente terciaria (según su resumen): https://en.wikipedia.org/wiki/Forward_contract"
  - "Duke FinReg Blog, Hedging of currency exposures: Lessons for SME exporters and importers (25/01/2022), reseña de Fabling y Grimes 2008, ACCA 2013, Acharán, Álvarez y Villena 2009 y EFIGE (leído): https://sites.duke.edu/thefinregblog/2022/01/25/hedging-of-currency-exposures-lessons-for-sme-exporters-and-importers"
  - "Jin y Jorion (2006), Journal of Finance 61(2):893-919 (según su abstract): https://ideas.repec.org/a/bla/jfinan/v61y2006i2p893-919.html"
  - "APQC, Process Classification Framework 7.4 (2024), 9.7.5.3 Manage foreign exchange risk (leído): https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Tesoreria/.investigacion/financiamiento-y-riesgos.md, sección 2 (2026-11-27)"
  - "Tesoreria/.investigacion/financiamiento-y-pagos-segunda-ronda.md, sección 4 (2026-11-27)"
  - "Tesoreria/.investigacion/fundamentos-y-contraria.md, sección 4.5 (2026-11-27)"
  - "Tesoreria/.investigacion/financiamiento-y-riesgos-verificacion.md (2026-11-27)"
aliases: [riesgo de tipo de cambio, riesgo cambiario, currency risk, foreign exchange risk, FX risk, exposición cambiaria, exposición de transacción, transaction exposure, exposición de traslación, translation exposure, exposición económica, economic exposure, cobertura cambiaria, cobertura natural, natural hedge, forward, futuros de moneda, currency futures]
creado: 2026-11-27
revisado:
---

# Riesgo de tipo de cambio

El riesgo de tipo de cambio es que un movimiento de la cotización cambie lo que la empresa va a cobrar o pagar en otra moneda, lo que muestran sus estados o lo que vale su negocio; se acota primero con la cobertura natural (cobrar y pagar en la misma moneda) y después con contratos como el forward.

Es uno de los cuatro [riesgos financieros](riesgos-financieros.md), el único con nota propia porque, en la lectura de esta base, en una empresa que importa, exporta o se endeuda en otra moneda puede decidir el resultado. El registro de la diferencia de cambio, cuando la cotización ya se movió, es de Contabilidad y está en [moneda extranjera](../../Contabilidad/Operaciones/moneda-extranjera.md). Acá va lo anterior: cuánto se arriesga y qué se hace antes.

Las definiciones salen de OpenStax (libro de texto abierto) y de Wikipedia (fuente terciaria), que cita libros de finanzas internacionales que no se leyeron (Moffett, Stonehill y Eiteman; Eun y Resnick; Hull). La evidencia sobre pymes sale de una reseña secundaria.

## Las tres exposiciones

Según el artículo de Wikipedia sobre riesgo cambiario, y con las mismas tres categorías en OpenStax (20.3), la empresa está expuesta de tres formas:

| Exposición | Qué cambia | Ejemplo (de esta base) |
|---|---|---|
| De transacción | el valor de cobros y pagos ya contratados en otra moneda, entre que se pactan y se liquidan | una importación a pagar en dólares a 60 días |
| De traslación | lo que muestran los estados contables al convertirlos, «the extent to which its financial reporting is affected by exchange-rate movements», sin que cambien los flujos | una filial en otro país cuyos estados se convierten a la moneda del grupo |
| Económica | el valor de mercado de la empresa por cambios inesperados del tipo de cambio: su cuota de mercado, sus flujos futuros | un fabricante local que pierde ventas cuando el dólar baja y entran importados |

Para una pyme pesa sobre todo la de transacción, porque es la que cambia la caja de las próximas semanas; la de traslación es de grupos con filiales (lectura de esta base, sin fuente). APQC pide en 9.7.5.3.2 «Determine foreign exchange exposure for all currencies»: el primer paso es saber cuánto se debe y se cobra en cada moneda y cuándo.

## Cobertura natural: cobrar y pagar en la misma moneda

La cobertura natural compensa los flujos en una moneda con flujos en la misma moneda y cubre solo el neto. Según OpenStax, «a natural hedge occurs when a business can offset its risk simply through its own operations»; su ejemplo es una agencia de viajes cuyo tour a Italia pierde valor justo lo que gana el tour a Londres. Wikipedia la define, según su resumen, como una inversión que reduce el riesgo emparejando ingresos y gastos, con ejemplos como un exportador que abre una planta en el país donde vende o una empresa que se endeuda en la moneda de sus ingresos. El artículo de riesgo cambiario agrega que reduce los márgenes que cobran los bancos por convertir, que exige seguir las exposiciones de forma sistemática y que puede apoyarse en cuentas en moneda extranjera.

Un ejemplo de esta base, sin fuente: un comercio que compra mercadería en dólares y vende una parte en dólares solo está expuesto por la diferencia entre lo que paga y lo que cobra en esa moneda. Por eso la deuda en dólares de un [préstamo](../Financiamiento/prestamos.md) es más riesgosa para quien cobra en pesos que para quien exporta.

## El forward y los futuros

Un forward es, según OpenStax, «a contractual agreement between two parties to exchange a specified amount of currencies», individualizado entre comprador y vendedor, y «only as good as the promise of the counterparty». Según Wikipedia, es un contrato no estandarizado entre dos partes para comprar o vender un activo en una fecha futura a un precio fijado hoy. Se negocia fuera de bolsa, a la medida de la operación, sin pago inicial y en general sin pagos intermedios. Salir antes exige negociarlo con la misma contraparte, y la fuente advierte que tiene un riesgo de contraparte significativo.

Los futuros de moneda son parecidos, pero estandarizados: OpenStax dice que tienen «set sizes and maturity dates», y según los dos artículos de Wikipedia se negocian en bolsa, por montos fijos, solo para ciertas monedas y plazos, y se liquidan a diario. A cambio de la rigidez, la bolsa saca el riesgo de que la otra parte no cumpla (lectura de esta base sobre la liquidación diaria).

En Argentina el acceso al mercado de cambios y los instrumentos disponibles para una empresa están en [tesorería en Argentina](../tesoreria-en-argentina.md).

## Qué hacen las pymes

La reseña del Duke FinReg Blog (2022) junta los pocos datos que hay:

- En Nueva Zelanda (Fabling y Grimes, 2008, Banco de la Reserva), los exportadores cubrieron en promedio el 39% de sus transacciones de exportación en moneda extranjera: las firmas chicas, el 33%, y las grandes, el 49%.
- En la encuesta europea EFIGE, de unas 15.000 firmas de más de diez empleados y probablemente sesgada a las grandes según el autor, el 9,5% usaba derivados y el 17,4% alguna protección cambiaria, sin desglose por tamaño.
- En la encuesta de ACCA (2013), sin porcentajes en la reseña, las grandes cubren más, las chicas las siguen y las intermedias cubren menos.

Los datos contradicen la idea de que las chicas no cubren: cubren menos que las grandes, no nada, y en ACCA las intermedias cubren aún menos que las chicas.

> [!IMPORTANT]
> Por qué una pyme no cubre: dos explicaciones. Una, según el resumen de un buscador sobre estudios que no se leyeron (Dolde 1993, un estudio de 2020 sobre 73 pymes alemanas, una tesis neozelandesa), dice que las chicas cubren poco por el costo de la gestión del riesgo y la falta de recursos. La otra, de un estudio sobre firmas chilenas (Acharán, Álvarez y Villena, 2009, Banco Central de Chile) leído en la reseña de Duke, encuentra que las grandes usan menos derivados porque usan más cobertura natural, y que el traslado de precios a los compradores reemplaza la cobertura. A eso se suma que el valor de cubrir no es obvio ni en empresas grandes: Jin y Jorion (2006), según su abstract, no hallaron efecto de la cobertura sobre el valor de mercado de productoras de petróleo y gas. No hay un estudio con método sobre pymes y cobertura cambiaria leído en su fuente. En la segunda pasada el documento de SSRN al que remite la reseña de Duke devolvió error 403, y la búsqueda web se agotó antes de poder buscar los estudios originales.

La lectura de esta base sobre las dos posiciones: para una pyme con poca exposición neta, la cobertura natural y el traslado de precios suelen bastar, y el forward entra cuando hay un pago o un cobro grande, fechado y que no se puede trasladar. Es inferencia, no un resultado de los estudios.

## Lo que un sistema tiene que mostrar

Para medir la exposición de transacción, un sistema de gestión junta, por moneda y por fecha, las cuentas a cobrar y a pagar abiertas, los pedidos de venta y de compra confirmados y las cuotas de deuda, y muestra el neto (lectura de esta base sobre APQC 9.7.5.3.2). La [proyección de caja](../Caja-y-liquidez/proyeccion-de-caja.md) en cada moneda es la misma información en el tiempo. Cada cobertura contratada se guarda con su monto, su tipo pactado, su vencimiento y su contraparte, ligada a la exposición que cubre.

El tipo de cambio de cada operación y la diferencia al cerrar las registra la contabilidad, como explica [moneda extranjera](../../Contabilidad/Operaciones/moneda-extranjera.md). La diferencia de cambio que aparece en el resultado es el efecto ya ocurrido de la exposición que acá se mide antes.

## Cómo falla

- Mirar solo la diferencia de cambio contable. Cuando aparece en el resultado, la cotización ya se movió; la exposición se mide antes, con lo contratado y lo proyectado (lectura de esta base).
- Cubrir el bruto y no el neto. Si la empresa cobra y paga en la misma moneda, cubrir los dos lados paga dos veces por un riesgo que se compensaba.
- Olvidar la contraparte del forward. El contrato protege mientras la otra parte cumpla.
- Endeudarse en otra moneda por la tasa. Una tasa en dólares más baja que una en pesos no es más barata si el tipo de cambio sube más que la diferencia, como explica [costo del financiamiento](../Financiamiento/costo-del-financiamiento.md).
