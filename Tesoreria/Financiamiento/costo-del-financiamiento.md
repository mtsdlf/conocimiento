---
resumen: >-
  El costo del financiamiento es lo que de verdad cuesta una plata prestada, medido como tasa efectiva anual con todos los cargos incluidos y, con inflación, como tasa real; es la medida que permite comparar un descubierto, un factoring, un préstamo y un descuento por pronto pago que no se toma.
estado: borrador
estabilidad: estable
fuentes:
  - "Wikipedia, Effective interest rate, como fuente terciaria (según su resumen): https://en.wikipedia.org/wiki/Effective_interest_rate"
  - "Wikipedia, Fisher equation, como fuente terciaria (según su resumen): https://en.wikipedia.org/wiki/Fisher_equation"
  - "Wikipedia, Revolving credit, como fuente terciaria (según su resumen): https://en.wikipedia.org/wiki/Revolving_credit"
  - "Wikipedia, Factoring (finance), como fuente terciaria (según su resumen): https://en.wikipedia.org/wiki/Factoring_(finance)"
  - "Tesoreria/.investigacion/financiamiento-y-pagos-segunda-ronda.md, sección 3 (2026-11-27)"
aliases: [costo del financiamiento, cost of financing, cost of debt, costo de la deuda, tasa efectiva, tasa efectiva anual, TEA, effective annual rate, EAR, tasa nominal, TNA, nominal rate, APR, tasa real, real interest rate, ecuación de Fisher, Fisher equation, costo financiero total, CFT]
creado: 2026-11-27
revisado:
---

# Costo del financiamiento

El costo del financiamiento es lo que de verdad cuesta una plata prestada, medido como tasa efectiva anual con todos los cargos incluidos y, con inflación, como tasa real; es la medida que permite comparar un descubierto, un factoring, un préstamo y un descuento por pronto pago que no se toma.

Cada instrumento del [financiamiento](financiamiento.md) se cotiza distinto: una tasa nominal anual, una comisión por documento, un porcentaje por lo que no se usa. Hace falta una cuenta común que los ponga en la misma unidad. Las fórmulas tienen una sola fuente, terciaria (Wikipedia, leída a través de un resumen), pero son matemática estándar, y los ejemplos los verificó esta base.

## De la tasa nominal a la efectiva

La tasa nominal anual es la tasa del período multiplicada por la cantidad de períodos del año, sin capitalizar. La efectiva anual cuenta que el interés de cada período también genera interés. Según Wikipedia, con i la nominal anual y m los períodos de capitalización por año:

TEA = (1 + i/m)^m − 1

El ejemplo de la fuente: 6% nominal con capitalización mensual es 0,5% por mes, y (1,005)^12 − 1 da 6,17% efectivo anual. Con tasas más altas la brecha crece: el 1% mensual del ejemplo de [préstamos](prestamos.md) es 12% nominal y 12,68% efectivo (cálculo de esta base).

## Todos los cargos, no solo el interés

La tasa efectiva del interés no es el costo completo. Entran también las comisiones de apertura, la comisión por no uso de una línea, los seguros obligatorios y los gastos a cargo del deudor (lectura de esta base sobre los componentes). Dos ejemplos de las fuentes del tema:

- Comisión por no uso. En el ejemplo de Wikipedia sobre líneas rotativas, 0,8% anual sobre USD 600.000 sin usar cuesta USD 4.800 por año aunque no se retire nada. Ver [financiamiento de corto plazo](financiamiento-de-corto-plazo.md).
- Comisión del factoring. Una comisión de 5% por una factura a 45 días, ejemplo de Wikipedia, equivale a 40,6% nominal anual sobre el valor de la factura, y a 51,6% efectivo anual medido sobre lo que se recibe (cálculo de esta base, detallado en [financiamiento de corto plazo](financiamiento-de-corto-plazo.md)).

Renunciar a un descuento por pronto pago también es financiarse con el proveedor, y su costo anualizado se calcula con la misma lógica. Esa cuenta, con el ejemplo de 2/10 neto 30, vive en la [programación de pagos](../Pagos-a-proveedores/programacion-de-pagos.md); la decisión es compararla con el costo del financiamiento más barato que la empresa tenga.

## El costo financiero total

El costo financiero total es el nombre que recibe, en Argentina, la medida completa: una tasa efectiva anual que suma al interés las comisiones, los seguros y los gastos. Es un término de las normas del BCRA; lo argentino va en [tesorería en Argentina](../tesoreria-en-argentina.md).

> [!NOTE] Sin fuente todavía: la definición del costo financiero total en las normas del BCRA de protección de los usuarios de servicios financieros. Lo que dice el párrafo de arriba sobre qué incluye sale de la memoria del informe de investigación, sin verificar; tampoco se verificó si se informa con y sin impuestos. Las dos URLs del BCRA probadas dieron error.

## La tasa real con inflación

Con inflación, una tasa nominal alta puede ser barata. La ecuación de Fisher, según Wikipedia, relaciona la tasa nominal i, la real r y la inflación π: (1 + i) = (1 + r)(1 + π), o sea r = (1 + i)/(1 + π) − 1. La fuente da la aproximación r ≈ i − π, que vale porque el producto r·π es despreciable cuando las tasas son bajas.

Con inflación alta la aproximación engaña. Cálculo de esta base, verificado:

| Nominal anual | Inflación anual | Real exacta | Real aproximada (i − π) |
|---|---|---|---|
| 8% | 3% | 4,85% | 5% |
| 60% | 50% | 6,67% | 10% |

En el segundo caso la aproximación exagera la tasa real en un 50%. En una economía con inflación alta se usa la fórmula exacta. Las tasas de una fecha en Argentina están en [tasas de referencia en Argentina](../tasas-de-referencia-en-argentina.md).

La tasa real que se calcula con la inflación que ya ocurrió (*ex post*) no es la que se usa para decidir: para tomar un préstamo cuenta la inflación esperada (*ex ante*). La fuente no hace esa distinción; es lectura de esta base.

## Cómo se comparan dos alternativas

Para que dos costos sean comparables, la base propone estas reglas (lectura de esta base, sin fuente con método):

1. Pasá todo a tasa efectiva anual, con todos los cargos.
2. Usá la misma base de días. Una cuenta con año de 360 días y otra con 365 difieren aunque el instrumento sea el mismo; declarala.
3. Medí el costo sobre la plata que efectivamente se recibe, no sobre el valor nominal del documento.
4. Compará en la misma moneda, o en términos reales. Una tasa en dólares y una en pesos solo se comparan sumando lo que se espera que se mueva el tipo de cambio, que es tema de [riesgo de tipo de cambio](../Riesgos-financieros/riesgo-de-tipo-de-cambio.md).
5. Mirá lo que no es precio: el recurso del factoring, si la línea es comprometida, las garantías y los covenants de un [préstamo](prestamos.md).

## Lo que un sistema tiene que guardar para calcularlo

Para mostrar el costo de una deuda, un sistema de gestión guarda la tasa nominal, el período de capitalización, la base de días, cada comisión con su base de cálculo (sobre el saldo, sobre lo no usado, sobre el documento) y los seguros y gastos. Con eso calcula la tasa efectiva y, si tiene la inflación, la real. Guardar solo «la tasa» obliga a adivinar cuál de todas es (lectura de esta base).

## Cómo se equivoca la comparación

- Nominal contra efectiva. Un 12% nominal con capitalización mensual es más caro que un 12% efectivo.
- Una comisión por período contra una tasa anual. El 5% por 45 días del factoring parece barato al lado de cualquier tasa anual de descubierto hasta que se lo anualiza: ronda el 40%.
- Aproximar a Fisher con inflación alta. Con 60% nominal y 50% de inflación, la tasa real es 6,67% y no 10%.
- Olvidar los cargos fijos. Una comisión de apertura pesa más cuanto más corto es el préstamo (lectura de esta base).
