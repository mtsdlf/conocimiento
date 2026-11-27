---
resumen: >-
  En un software de gestión, un número de negocio viaja siempre con su unidad (kilos, cajas, horas) o con su moneda. Convertir unidades, redondear sin perder centavos, guardar la moneda de origen junto a la de la empresa y registrar la diferencia de cambio son decisiones de diseño que valen para todos los módulos.
estado: borrador
estabilidad: estable
fuentes:
  - "Martin Fowler, Money (Patterns of Enterprise Application Architecture): https://martinfowler.com/eaaCatalog/money.html"
  - "Martin Fowler, Analysis Patterns (1997), cap. 3 Quantity, Conversion Ratio, Compound Units (solo el índice): https://www.oreilly.com/library/view/analysis-patterns-reusable/9780134271453/"
  - "Documentación de un ERP de código abierto, Multi-currency system: https://raw.githubusercontent.com/odoo/documentation/19.0/content/applications/finance/accounting/get_started/multi_currency.rst"
  - "Software-de-gestion/.investigacion/columnas-tecnicas-97.md (2026-11-27)"
aliases: [cantidad, quantity, unidad de medida, unit of measure, UoM, conversión de unidades, conversion ratio, money, dinero, importe, multimoneda, multi-currency, moneda de la empresa, moneda de origen, redondeo, rounding, diferencia de cambio]
creado: 2026-11-27
revisado:
---

# Cantidades, unidades y monedas

En un software de gestión, un número de negocio viaja siempre con su unidad (kilos, cajas, horas) o con su moneda. Convertir unidades, redondear sin perder centavos, guardar la moneda de origen junto a la de la empresa y registrar la diferencia de cambio son decisiones de diseño que valen para todos los módulos.

Un «10» suelto no dice nada: pueden ser diez unidades, diez cajas de doce, diez kilos, diez horas o diez dólares. La columna existe para que el número nunca viaje solo. Según el índice de *Analysis Patterns* (1997), Fowler le dedica a eso el capítulo 3, con los patrones de cantidad (*Quantity*), razón de conversión (*Conversion Ratio*) y unidades compuestas.

## Cantidades con unidad

El [artículo](../../Inventario-y-depositos/Existencias/articulo.md#la-unidad-de-medida-y-sus-conversiones) guarda una unidad de stock, la más chica en que se cuenta, y las conversiones a las demás: se compra por pallet, se guarda por caja y se vende por unidad. Cada documento puede usar su unidad, pero el movimiento se registra convertido a la de stock. Así lo plantea Inventario, y es la regla que el software aplica en todos los módulos.

La misma regla aparece en dos dominios más. En compras, la [recepción contra lo pedido](../../Compras-y-abastecimiento/Seguimiento-de-la-orden/recepcion-contra-lo-pedido.md) compara lo contado con lo pedido, y si la orden habla en cajas y el depósito cuenta unidades, la comparación necesita la conversión. En servicios profesionales, la unidad es la hora y su fracción: la [hoja de horas](../../Servicios-profesionales-y-proyectos/Registro-de-horas/hoja-de-horas.md) carga horas imputadas que después se valorizan a una tarifa.

Para el diseño, en lectura de esta base, eso pide tres cosas: que cada cantidad guarde su unidad junto al número, que la conversión sea un dato del maestro y no una cuenta que hace quien carga, y que cada artículo diga si admite decimales.

## Importes con moneda

Fowler define el patrón *Money* como lo que «Represents a monetary value»: un importe con su moneda, que impide sumar dólares con yenes. El mismo patrón encapsula el redondeo, porque «it's easy to lose pennies». Repartir 100 en tres cuotas da 33,33 tres veces y se pierde un centavo; el reparto correcto pone 33,34 en una de ellas (ejemplo de esta base).

En un sistema con varias monedas, cada documento guarda el importe en la moneda de la operación y su equivalente en la moneda de la empresa, con el tipo de cambio usado. La documentación de un ERP de código abierto describe ese esquema: una moneda principal de la empresa y diferencias de cambio que el sistema registra solo, en cuentas y en un diario propios.

Qué tipo de cambio corresponde en cada momento lo dice la norma contable, no el software. La moneda funcional, el tipo de la fecha de la operación, la conversión al cierre y la diferencia realizada y no realizada están en [moneda extranjera](../../Contabilidad/Operaciones/moneda-extranjera.md). Lo que el sistema tiene que mostrar para medir la exposición, en [riesgo de tipo de cambio](../../Tesoreria/Riesgos-financieros/riesgo-de-tipo-de-cambio.md#lo-que-un-sistema-tiene-que-mostrar).

## Un caso que cruza las dos

Una empresa importa un insumo en dólares por caja y lo consume en producción por kilo (ejemplo de esta base). La orden de compra va en dólares y en cajas. La recepción convierte cajas a kilos para el stock. La factura del proveedor se registra en dólares con el tipo de su fecha, y el pago, con el tipo del día en que se paga: la diferencia entre los dos es una diferencia de cambio realizada. El costo del kilo que usa la [orden de producción](../../Produccion/Ejecucion-en-planta/orden-de-produccion.md) sale de convertir las dos cosas. Si alguna de las conversiones vive en la cabeza de quien carga, el costo del producto queda mal y nadie sabe por qué.

## Cómo falla

- La conversión en la cabeza. Se recibe «10» pensando en cajas y el sistema suma 10 unidades; el conteo lo descubre después como una diferencia sin causa.
- Importes en punto flotante. Un tipo de dato que no representa exactamente los centavos acumula diferencias en las sumas (lectura de esta base; el redondeo en planillas está en [tipos de dato](../../Planillas-de-calculo/Modelo-de-la-planilla/tipos-de-dato.md)).
- Sumar monedas distintas. Un total de deudores que suma pesos y dólares sin convertir no es un número.
- El tipo de cambio de la fecha equivocada. Convertir con el tipo de hoy un documento de hace un mes cambia lo registrado; la fecha que manda es la del hecho ([fechas, vigencias y cierre](fechas-vigencias-y-cierre.md)).

> [!NOTE]
> Sin fuente todavía: una fuente primaria sobre el redondeo cuando una conversión de unidades no es exacta, y una que trate en general cómo guarda un sistema el tipo de cambio usado en cada documento.

Las cantidades y los importes son lo que suma el [registro de movimientos](registro-de-movimientos-y-dimensiones.md); la unidad y la moneda de cada cosa se definen en los [datos maestros](datos-maestros-y-partes.md), y la moneda de cada empresa, en la [estructura de la organización](estructura-de-la-organizacion.md).
