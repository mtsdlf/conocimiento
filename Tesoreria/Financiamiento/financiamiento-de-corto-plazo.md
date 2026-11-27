---
resumen: >-
  El financiamiento de corto plazo cubre los baches de caja de semanas o meses con cuatro instrumentos: el descubierto en la cuenta corriente, la línea de crédito rotativa, el descuento de documentos y el factoring, que adelanta lo que deben los clientes.
estado: vigente
estabilidad: estable
fuentes:
  - "Wikipedia, Overdraft, como fuente terciaria, centrada en el Reino Unido (según su resumen): https://en.wikipedia.org/wiki/Overdraft"
  - "Wikipedia, Revolving credit, como fuente terciaria (según su resumen): https://en.wikipedia.org/wiki/Revolving_credit"
  - "Wikipedia, Factoring (finance), como fuente terciaria (según su resumen): https://en.wikipedia.org/wiki/Factoring_(finance)"
  - "Wikipedia, Invoice discounting, como fuente terciaria (según su resumen): https://en.wikipedia.org/wiki/Invoice_discounting"
  - "Wikipedia, Liquidity risk, como fuente terciaria, orientada a bancos y aseguradoras (según su resumen): https://en.wikipedia.org/wiki/Liquidity_risk"
  - "OCC (Estados Unidos), Comptroller's Handbook, Asset-Based Lending, versión 1.1 (2017), secciones de línea rotativa, covenants y glosario (leído en esas secciones): https://www.occ.treas.gov/publications-and-resources/publications/comptrollers-handbook/files/asset-based-lending/pub-ch-asset-based-lending.pdf"
  - "Tesoreria/.investigacion/financiamiento-y-pagos-segunda-ronda.md, sección 1 (2026-11-27)"
  - "Tesoreria/.investigacion/financiamiento-y-riesgos-verificacion.md (2026-11-27)"
aliases: [financiamiento de corto plazo, short-term financing, descubierto, overdraft, giro en descubierto, línea de crédito, revolving credit, línea rotativa, factoring, factoraje, descuento de documentos, descuento de cheques, invoice discounting, descuento de facturas]
creado: 2026-11-27
revisado: 2026-11-27
---

# Financiamiento de corto plazo

El financiamiento de corto plazo cubre los baches de caja de semanas o meses con cuatro instrumentos: el descubierto en la cuenta corriente, la línea de crédito rotativa, el descuento de documentos y el factoring, que adelanta lo que deben los clientes.

Los dos primeros se apoyan en el crédito de la empresa con su banco. Los dos últimos se apoyan en lo que le deben sus clientes: convierten en plata hoy una cuenta a cobrar que vence mañana. Qué instrumento conviene depende de su costo, que se compara con la cuenta de [costo del financiamiento](costo-del-financiamiento.md), y del pozo que muestre la [proyección de caja](../Caja-y-liquidez/proyeccion-de-caja.md). La entrada de la vertical, [financiamiento](financiamiento.md), los pone al lado del préstamo y del financiamiento de la cadena.

Casi todas las fuentes de esta nota son artículos de Wikipedia, leídos a través de un resumen: cada afirmación tiene una sola fuente terciaria. La excepción es la línea rotativa, que tiene además el manual del OCC. Lo que se dice de Argentina (el acuerdo en cuenta corriente, el descuento de cheques en el mercado de capitales, la factura de crédito electrónica) está en [tesorería en Argentina](../tesoreria-en-argentina.md), y las tasas de una fecha en [tasas de referencia en Argentina](../tasas-de-referencia-en-argentina.md).

## El descubierto: pactado o no pactado

Un descubierto ocurre cuando se saca de la cuenta corriente más de lo que hay en ella. Wikipedia, con terminología del Reino Unido, distingue el pactado, cubierto por un límite acordado con el banco, del no pactado, que excede ese límite: el banco puede rechazar el débito o tratarlo como un pedido informal de más límite. El no pactado cuesta típicamente más que el pactado, con interés, comisiones o las dos cosas.

La consecuencia práctica es que el descubierto se negocia antes de necesitarlo (lectura de esta base). Para la [posición de caja](../Caja-y-liquidez/posicion-de-caja.md), el límite pactado sin usar es plata disponible que no está en el saldo, y el sistema tiene que mostrar las dos cifras por separado.

## La línea de crédito rotativa y su comisión por no uso

Una línea rotativa es un tope de crédito disponible durante un plazo: la empresa retira, devuelve y vuelve a retirar dentro del tope. Según Wikipedia, cada retiro suele tomarse por uno, tres o seis meses, y algunos prestamistas cobran una comisión sobre lo que no se usa. El OCC describe lo mismo con otras palabras: la empresa retira, devuelve y vuelve a retirar durante la vida del préstamo, hasta el menor de dos valores, la base de garantía disponible o el monto comprometido de la línea. Según el manual, el plazo es típicamente corto, para que el banco pueda reevaluar el riesgo, y en un número creciente de casos llegó a cinco años. El manual trata la línea garantizada con cuentas a cobrar e inventario; la cifra de uno, tres o seis meses no figura en él.

El ejemplo de la fuente: una comisión del 40% de un margen de 2,0% da 0,8% anual sobre lo no usado, y sobre USD 600.000 sin usar son USD 4.800 por año. Esa comisión es parte del costo de la línea aunque no se retire nada, y entra al [costo del financiamiento](costo-del-financiamiento.md).

> [!NOTE] Sin fuente todavía: la diferencia entre línea comprometida (el banco se obliga a prestar hasta el tope mientras no haya incumplimiento, y por eso cobra la comisión por no uso) y no comprometida (el banco puede negarse a desembolsar). La fuente no la trata. En la segunda pasada tampoco la trataron OpenStax (19.1 y 19.2, que no hablan de comisión por no uso ni de línea comprometida) ni el manual del OCC; las páginas de la ACT y de FCI que se probaron dieron error 404. Falta una guía profesional.

El artículo de Wikipedia sobre riesgo de liquidez, pensado para aseguradoras, recomienda tener líneas siempre disponibles con prestamistas de buena calificación y repartirlas entre varios. Por qué una línea que el banco puede cortar es un riesgo está en [riesgos financieros](../Riesgos-financieros/riesgos-financieros.md).

## Factoring: vender lo que deben los clientes

En el factoring la empresa cede sus facturas a un factor, que le adelanta la plata y después cobra al cliente. Wikipedia distingue dos ejes:

- Con o sin recurso. Sin recurso, la cesión es una venta del crédito y el factor absorbe la pérdida si el deudor no paga; puede quedar un recurso por calidad, por ejemplo si el cliente devuelve la mercadería. Con recurso, el factor le reclama a la empresa lo que el cliente no pagó.
- Con o sin notificación. Con notificación, el cliente recibe un aviso de cesión y le paga al factor. Sin notificación, la empresa sigue cobrando como agente del factor.

El adelanto típico, según la misma fuente, es de 80% a 85% del valor de la factura, y el resto se devuelve menos las comisiones cuando el cliente paga. La comisión se cobra como porcentaje de la factura (el ejemplo de la fuente es 5% por una factura a 45 días), a veces con un cargo de administración más interés. Algunos factores retienen además una reserva de 10% a 15% de la línea.

### Cuánto es 5% por 45 días en un año

Un 5% por 45 días no es un 5% anual. Cálculo de esta base, verificado: sobre el valor de la factura, 0,05 × 365/45 da 40,6% nominal anual simple. Medido sobre lo que la empresa recibe (95 por cada 100), es 5/95 × 365/45 = 42,7% simple, y capitalizado, (100/95)^(365/45) − 1 = 51,6% efectivo anual. El resultado depende de la base que se elija; por eso [costo del financiamiento](costo-del-financiamiento.md) pide declararla al comparar.

## Descuento de facturas y descuento de documentos

«Descuento» nombra cosas distintas según el idioma. En el uso británico, el descuento de facturas (*invoice discounting*) se parece al factoring, pero la empresa sigue cobrando por cuenta del financiador y el cliente no se entera: según Wikipedia, la diferencia principal entre los dos es la confidencialidad. En Estados Unidos, según la misma fuente, el factoring es una venta y el descuento es un préstamo con la cuenta a cobrar como garantía.

En el uso local, descontar es entregar un cheque o un pagaré antes de su vencimiento y recibir hoy su valor menos un descuento.

> [!NOTE] Sin fuente todavía: el mecanismo general del descuento de documentos. La definición de trabajo de esta base, sin fuente: el banco o un inversor compra el documento por su valor nominal menos un descuento que depende de la tasa y de los días al vencimiento, y la empresa que lo endosa responde si el librador no paga. El descuento de cheques y cheques electrónicos en el mercado de capitales argentino tiene fuentes en [tesorería en Argentina](../tesoreria-en-argentina.md).

## Lo que cambia en cada instrumento

| Instrumento | Qué entrega la empresa | Quién pierde si el cliente no paga | El cliente se entera |
|---|---|---|---|
| Descubierto y línea | nada; es crédito del banco | no aplica | no aplica |
| Factoring sin recurso | la factura, vendida | el factor | sí, si hay notificación |
| Factoring con recurso | la factura | la empresa | sí, si hay notificación |
| Descuento de facturas | la factura, como garantía | la empresa | no |
| Descuento de documentos | el cheque o pagaré, endosado | la empresa, por el endoso (sin fuente) | sí: el documento cambia de manos |

## Qué tiene que registrar un sistema

Cada instrumento deja rastros distintos en el sistema de gestión (lectura de esta base):

- Factura cedida. La factura cambia de estado y de acreedor: el cobro del cliente se le aplica al factor, y la [aplicación de cobros](../Credito-y-cobranzas/aplicacion-de-cobros.md) tiene que reconocerlo. Con notificación, el cliente le paga al factor y la empresa recibe la liquidación neta de comisiones.
- Recurso. Con recurso, la empresa sigue expuesta a la deuda del cliente aunque ya cobró del factor: el riesgo de crédito sigue en [crédito a clientes](../Credito-y-cobranzas/credito-a-clientes.md) hasta que el cliente paga.
- Documento descontado. El cheque sale de la cartera, pero si el librador no paga vuelve como deuda con quien lo descontó.
- Límites. El tope pactado del descubierto y de cada línea, lo usado y lo disponible, para que la [proyección de caja](../Caja-y-liquidez/proyeccion-de-caja.md) cuente con ese margen.

Cómo se registran la cesión, la comisión y los intereses es de [Contabilidad](../../Contabilidad/contabilidad.md); acá importa cuándo entra la plata y cuánto queda en el camino.

## Cómo falla el financiamiento de corto plazo

- El descubierto que se vuelve permanente. Si la cuenta está siempre en rojo, el descubierto financia un hueco de capital de trabajo que no es transitorio, y conviene mirarlo en el [capital de trabajo](../Caja-y-liquidez/capital-de-trabajo.md) (lectura de esta base).
- Mirar la comisión del factoring como si fuera anual. Un 5% por 45 días ronda el 40% anual o más, según la cuenta de arriba.
- Creer que el factoring saca el riesgo. Con recurso, el riesgo de que el cliente no pague sigue en la empresa.
- Cobrar dos veces o ninguna. Un cliente que no se enteró de la cesión le paga a la empresa en lugar de al factor, y el sistema tiene que saber que ese cobro es de otro (lectura de esta base).
