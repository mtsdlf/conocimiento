---
resumen: >-
  El capital de trabajo es la plata que la operación tiene inmovilizada en stock y en lo que deben los clientes, menos lo que todavía se debe a los proveedores; el ciclo de conversión del efectivo mide cuántos días pasa esa plata afuera antes de volver como cobro.
estado: borrador
estabilidad: estable
fuentes:
  - "OpenStax, Principles of Finance (2022), 19.1 What Is Working Capital? (leído): https://openstax.org/books/principles-finance/pages/19-1-what-is-working-capital"
  - "OpenStax, Principles of Finance (2022), 19.4 Receivables Management y 19.5 Inventory Management (leído): https://openstax.org/books/principles-finance/pages/19-4-receivables-management"
  - "Deloof, M. (2003), Does Working Capital Management Affect Profitability of Belgian Firms?, Journal of Business Finance & Accounting 30(3-4), 573-588 (abstract): https://ideas.repec.org/a/bla/jbfnac/v30y2003i3-4p573-588.html"
  - "García-Teruel, P. J. y Martínez-Solano, P. (2007), Effects of working capital management on SME profitability, International Journal of Managerial Finance 3(2), 164-177 (según su resumen): https://www.emerald.com/insight/content/doi/10.1108/17439130710738718/full/html"
  - "Baños-Caballero, S., García-Teruel, P. J. y Martínez-Solano, P. (2014), Working capital management, corporate performance, and financial constraints, Journal of Business Research 67(3), 332-338 (abstract): https://ideas.repec.org/a/eee/jbrese/v67y2014i3p332-338.html"
  - "Petersen, M. y Rajan, R. (1997), Trade Credit: Theories and Evidence, Review of Financial Studies 10(3), 661-691 (abstract): https://ideas.repec.org/a/oup/rfinst/v10y1997i3p661-91.html"
  - "Wikipedia, Cash conversion cycle (según su resumen): https://en.wikipedia.org/wiki/Cash_conversion_cycle"
  - "Tesoreria/.investigacion/caja-y-liquidez.md, sección 4 (2026-11-27)"
  - "Tesoreria/.investigacion/fundamentos-y-contraria.md, sección 4.1 (2026-11-27)"
aliases: [capital de trabajo, capital de trabajo neto, working capital, net working capital, NWC, ciclo de conversión del efectivo, ciclo de caja, cash conversion cycle, CCC, cash cycle, días de inventario, days inventory outstanding, DIO, inventory conversion period, días de cobro, receivables collection period, días de pago, days payables outstanding, DPO, payables deferral period]
creado: 2026-11-27
revisado:
---

# Capital de trabajo

El capital de trabajo es la plata que la operación tiene inmovilizada en stock y en lo que deben los clientes, menos lo que todavía se debe a los proveedores; el ciclo de conversión del efectivo mide cuántos días pasa esa plata afuera antes de volver como cobro.

Es la pieza de [Caja y liquidez](caja-y-liquidez.md) que explica por qué una empresa que vende bien y da ganancia se queda sin plata para pagar. La [posición de caja](posicion-de-caja.md) muestra el saldo que no alcanza; el capital de trabajo muestra dónde está la plata que falta, y la [proyección de caja](proyeccion-de-caja.md) lo traduce a semanas.

## Activo corriente menos pasivo corriente

OpenStax define el capital de trabajo como lo que hace falta para la operación de todos los días: «Working capital describes the resources that are needed to meet the daily, weekly, and monthly operating cash flow needs». La medida contable es el capital de trabajo neto: «NWC = Current Assets - Current Liabilities» (*Principles of Finance*, 19.1).

Para la tesorería pesan tres renglones del balance. El stock y las cuentas a cobrar son plata que ya salió o que ya se ganó y todavía no entró. Las cuentas a pagar son plata que la empresa usa y todavía no pagó. Cada uno tiene su vertical: lo que deben los clientes es de [Crédito y cobranzas](../Credito-y-cobranzas/credito-y-cobranzas.md), lo que se debe a los proveedores es de [Pagos a proveedores](../Pagos-a-proveedores/pagos-a-proveedores.md) y el stock es del tema Inventario y depósitos, todavía no escrito.

## El ciclo de conversión del efectivo

El ciclo de conversión del efectivo cuenta los días entre que la empresa le paga al proveedor y le cobra al cliente. OpenStax lo arma con tres plazos (19.1):

> Cash Cycle = Inventory Conversion Period + Receivables Collection Period - Payables Deferral Period

Cada plazo sale de una rotación anual, y los días son 365 divididos por la rotación:

| Plazo | En esta base | Rotación que lo calcula |
|---|---|---|
| Inventory conversion period | días de inventario | costo de ventas ÷ inventario promedio |
| Receivables collection period | días de cobro | ventas a crédito ÷ cuentas a cobrar promedio |
| Payables deferral period | días de pago | costo de ventas ÷ cuentas a pagar promedio |

Los días de pago restan porque, mientras no se le paga, es el proveedor el que financia el ciclo. Los días de cobro son casi el mismo número que la cobranza llama DSO (la guía de cobranza usa el saldo final y no el promedio), con sus fórmulas y sus trampas en [gestión de la cobranza](../Credito-y-cobranzas/gestion-de-la-cobranza.md#dso-dso-mejor-posible-y-días-de-atraso).

## Un distribuidor con un ciclo de 76 días

Los números que siguen son un ejemplo armado para esta nota, sin moneda. Un distribuidor vende 12.000.000 al año, todo a crédito, y su costo de ventas es 9.000.000. En promedio tiene 1.125.000 de stock, 2.000.000 de cuentas a cobrar y 750.000 de cuentas a pagar.

| Plazo | Rotación | Días |
|---|---|---|
| Días de inventario | 9.000.000 ÷ 1.125.000 = 8 | 365 ÷ 8 = 45,6 |
| Días de cobro | 12.000.000 ÷ 2.000.000 = 6 | 365 ÷ 6 = 60,8 |
| Días de pago | 9.000.000 ÷ 750.000 = 12 | 365 ÷ 12 = 30,4 |

El ciclo es 45,6 + 60,8 − 30,4 = 76,0 días. La plata que el distribuidor tiene trabada en la operación es 1.125.000 + 2.000.000 − 750.000 = 2.375.000: alguien la tiene que poner, sea el dueño, el banco o la caja acumulada.

## Por qué crecer consume caja

Si el distribuidor vende un 50 % más con el mismo ciclo, sus saldos crecen en la misma proporción: 1.687.500 de stock, 3.000.000 de cuentas a cobrar y 1.125.000 de cuentas a pagar. La plata trabada pasa a 3.562.500. El crecimiento pide 1.187.500 más de caja antes de cobrar la primera venta adicional, aunque cada venta deje ganancia.

OpenStax lo afirma en 19.1: «Growing companies, even if they are extremely profitable, need additional working capital». El cálculo que la muestra es de esta base, con la aritmética del ciclo: el libro no lo desarrolla. La diferencia entre la ganancia y la plata es la del [devengado](../../Contabilidad/Registro/devengado.md): la venta a 60 días es resultado hoy y cobro dentro de dos meses.

## Las palancas para acortar el ciclo

Cada término de la fórmula es una palanca, y cada una tiene su costo; las citas dicen de dónde sale:

- Cobrar antes: plazos más cortos, descuento por pronto pago al cliente, mejor [gestión de la cobranza](../Credito-y-cobranzas/gestion-de-la-cobranza.md). En el ejemplo, bajar los días de cobro de 60,8 a 45,6 deja las cuentas a cobrar en 1.500.000 y libera 500.000. OpenStax advierte el costo: «If credit terms are not competitive within the industry, sales can suffer» (19.4).
- Tener menos stock: comprar más seguido y en menos cantidad. OpenStax: «Controlling inventory costs minimizes working capital needs» (19.5). El costo es el faltante, que pierde la venta.
- Pagar más tarde: estirar los días de pago. Es la palanca más barata en apariencia y la que se discute abajo; el cálculo de qué cuesta dejar pasar un descuento por pronto pago está en [programación de pagos](../Pagos-a-proveedores/programacion-de-pagos.md#el-costo-de-no-tomar-un-descuento-por-pronto-pago).
- Financiar el ciclo en lugar de acortarlo: descontar facturas o cheques, que adelanta el cobro a cambio de una tasa; está en [financiamiento de corto plazo](../Financiamiento/financiamiento-de-corto-plazo.md).

Según el resumen de Wikipedia, acortar el ciclo tiene riesgos propios, porque una política de cobrar estricto y pagar laxo no siempre se sostiene.

## El crédito de proveedores no es gratis

Petersen y Rajan (1997) estudiaron por qué las empresas usan crédito comercial. Según su resumen, las empresas chicas usan más crédito de proveedores cuando las instituciones financieras no les prestan, y los proveedores tienen ventajas para conseguir información sobre el comprador y para liquidar activos si no les pagan. La lectura de esta base es que los días de pago son financiamiento: quien estira el plazo se financia con el proveedor, y lo paga en el descuento que pierde, en el recargo por mora o en una relación peor. Por eso un ciclo corto logrado pagando tarde no es lo mismo que uno logrado cobrando antes.

## Acortar el ciclo y la rentabilidad

> [!IMPORTANT]
> Si acortar el ciclo siempre mejora la rentabilidad está en disputa. Los tres trabajos se leyeron en abstract o resumen.
>
> - A favor: Deloof (2003), con 1.009 grandes empresas belgas no financieras entre 1992 y 1996, concluye según su abstract que los directivos pueden aumentar la rentabilidad bajando los días de cobro y los de inventario. García-Teruel y Martínez-Solano (2007), con 8.872 pymes españolas entre 1996 y 2002, encuentran según su resumen que reducir el inventario y los días de cobro crea valor y que acortar el ciclo mejora la rentabilidad. Son dos muestras independientes con el mismo signo.
> - En contra: Baños-Caballero, García-Teruel y Martínez-Solano (2014), con empresas británicas no financieras, encuentran según su abstract una relación en U invertida entre la inversión en capital de trabajo y el desempeño. Hay un nivel óptimo: por debajo de él, acortar más empeora. Ese óptimo es más bajo en las empresas con más probabilidad de tener restricciones financieras, que es lo que más se parece a una pyme.
> - Sobre Deloof: el mismo abstract dice que las empresas menos rentables tardan más en pagar, así que la causa puede ir al revés: la que gana poco paga tarde porque le falta plata.
>
> Lo que la base puede afirmar: un ciclo más corto libera caja; que además mejore la rentabilidad depende de cómo se acorta, y existe un punto a partir del cual acortar más cuesta ventas o proveedores. Ninguna de las muestras es argentina.

> [!NOTE] Sin fuente todavía: Baños-Caballero et al. (2012), en *Small Business Economics* 39(2), estudia pymes españolas y se cita como evidencia de un óptimo en pymes, pero su abstract no se leyó.

## Cómo lo calcula un sistema de gestión

Un sistema tiene todos los datos para calcular el ciclo: el costo de ventas, las ventas a crédito y los saldos de stock, de [cuentas corrientes](../../Contabilidad/Registro/cuentas-corrientes.md) de clientes y de proveedores. Las decisiones de diseño que siguen son lectura de esta base:

- Promedios, no saldos de cierre: la fórmula usa saldos promedio del período. Un saldo de cierre en un negocio estacional da un ciclo que no existe el resto del año.
- Ventas a crédito, no ventas totales: las ventas al contado no generan cuentas a cobrar y achican los días de cobro si se suman.
- El período y el divisor a la vista: OpenStax usa 365 días y rotaciones anuales; si el sistema calcula por mes, dice con qué divisor.
- Por cliente, por proveedor y por línea: el ciclo de la empresa es un promedio, y la plata trabada suele estar en pocos clientes o pocos productos. La antigüedad de saldos de las cuentas corrientes lo muestra.

Según el resumen de Wikipedia, el ciclo se deriva del balance porque no se observa en los flujos de caja: describe, por lectura de esta base, el período pasado, y la [proyección de caja](proyeccion-de-caja.md) dice qué semana va a faltar la plata.

## Cómo falla

Las fallas que siguen son lectura de esta base sobre lo anterior:

- Se acorta el ciclo pagando tarde, y se pierden descuentos por pronto pago que costaban más que un descubierto.
- Se endurecen los plazos de cobro sin mirar los de la competencia, y se pierden ventas.
- Se toma el ciclo promedio como verdad, y un solo cliente grande que paga a 120 días queda escondido.

Para una empresa que recién empieza, la misma pregunta se hace en meses, con la [pista](../../Emprender/Finanzas/finanzas.md#consumo-mensual-y-pista) y el [plan financiero mínimo](../../Emprender/Finanzas/plan-financiero-minimo.md) de doce meses de Emprender.
