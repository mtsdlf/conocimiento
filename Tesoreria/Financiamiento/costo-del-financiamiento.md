---
resumen: >-
  El costo del financiamiento es lo que de verdad cuesta una plata prestada, medido como tasa efectiva anual con todos los cargos incluidos y, con inflación, como tasa real; es la medida que permite comparar un descubierto, un factoring, un préstamo y un descuento por pronto pago que no se toma.
estado: vigente
estabilidad: estable
fuentes:
  - "OpenStax, Principles of Finance, 8.4 Stated versus Effective Rates (leído): https://openstax.org/books/principles-finance/pages/8-4-stated-versus-effective-rates"
  - "BCRA, texto ordenado Tasas de interés en las operaciones de crédito, al 01/07/2024, puntos 3.2 y 3.4 (leído en esas secciones): https://www.bcra.gob.ar/Pdfs/Texord/t-tasint.pdf"
  - "BCRA, texto ordenado Protección de los usuarios de servicios financieros, al 06/05/2026, punto 2.3.3 (leído en esa sección): https://www.bcra.gob.ar/Pdfs/Texord/t-pusf.pdf"
  - "Wikipedia, Fisher equation, como fuente terciaria (según su resumen): https://en.wikipedia.org/wiki/Fisher_equation"
  - "Wikipedia, Revolving credit, como fuente terciaria (según su resumen): https://en.wikipedia.org/wiki/Revolving_credit"
  - "Wikipedia, Factoring (finance), como fuente terciaria (según su resumen): https://en.wikipedia.org/wiki/Factoring_(finance)"
  - "Tesoreria/.investigacion/financiamiento-y-pagos-segunda-ronda.md, sección 3 (2026-11-27)"
  - "Tesoreria/.investigacion/financiamiento-y-riesgos-verificacion.md (2026-11-27)"
aliases: [costo del financiamiento, cost of financing, cost of debt, costo de la deuda, tasa efectiva, tasa efectiva anual, TEA, effective annual rate, EAR, tasa nominal, TNA, nominal rate, APR, tasa real, real interest rate, ecuación de Fisher, Fisher equation, costo financiero total, CFT]
creado: 2026-11-27
revisado: 2026-11-27
---

# Costo del financiamiento

El costo del financiamiento es lo que de verdad cuesta una plata prestada, medido como tasa efectiva anual con todos los cargos incluidos y, con inflación, como tasa real; es la medida que permite comparar un descubierto, un factoring, un préstamo y un descuento por pronto pago que no se toma.

Cada instrumento del [financiamiento](financiamiento.md) se cotiza distinto: una tasa nominal anual, una comisión por documento, un porcentaje por lo que no se usa. Hace falta una cuenta común que los ponga en la misma unidad. La fórmula de la tasa efectiva sale de un libro de texto abierto (OpenStax). La de Fisher tiene una sola fuente, terciaria (Wikipedia, leída a través de un resumen), pero es matemática estándar. Los ejemplos propios los verificó esta base.

## De la tasa nominal a la efectiva

La tasa nominal anual es la tasa del período multiplicada por la cantidad de períodos del año, sin capitalizar. La efectiva anual cuenta que el interés de cada período también genera interés. Según OpenStax, con i la tasa de cada período y n los períodos de capitalización por año:

TEA = (1 + i)^n − 1

El ejemplo de la fuente: una tarjeta que cobra 1,5% por mes sobre el saldo impago durante un año rinde (1,015)^12 − 1 = 19,56% efectivo anual, contra el 18% que sugiere multiplicar 1,5% por 12. Con el 1% mensual del ejemplo de [préstamos](prestamos.md), el nominal es 12% y el efectivo 12,68% (cálculo de esta base).

## Todos los cargos, no solo el interés

La tasa efectiva del interés no es el costo completo. Entran también las comisiones de apertura, la comisión por no uso de una línea, los seguros obligatorios y los gastos a cargo del deudor (lectura de esta base sobre los componentes). Dos ejemplos de las fuentes del tema:

- Comisión por no uso. En el ejemplo de Wikipedia sobre líneas rotativas, 0,8% anual sobre USD 600.000 sin usar cuesta USD 4.800 por año aunque no se retire nada. Ver [financiamiento de corto plazo](financiamiento-de-corto-plazo.md).
- Comisión del factoring. Una comisión de 5% por una factura a 45 días, ejemplo de Wikipedia, equivale a 40,6% nominal anual sobre el valor de la factura, y a 51,6% efectivo anual medido sobre lo que se recibe (cálculo de esta base, detallado en [financiamiento de corto plazo](financiamiento-de-corto-plazo.md)).

Renunciar a un descuento por pronto pago también es financiarse con el proveedor, y su costo anualizado se calcula con la misma lógica. Esa cuenta, con el ejemplo de 2/10 neto 30, vive en la [programación de pagos](../Pagos-a-proveedores/programacion-de-pagos.md); la decisión es compararla con el costo del financiamiento más barato que la empresa tenga.

## El costo financiero total

El costo financiero total (CFT) es, en Argentina, la medida completa que fija el BCRA. Según su texto ordenado de tasas de interés en las operaciones de crédito (punto 3.4.1), «se expresará en forma de tasa efectiva anual» y se determina «agregando a la tasa de interés el efecto de las comisiones y cargos asociados a la operación, cualquiera sea su concepto». Lo argentino va en [tesorería en Argentina](../tesoreria-en-argentina.md).

Lo que entra y lo que no, según el punto 3.4 de esa norma:

- Computan, entre otros: las primas de seguros que se exigen como condición del crédito, los gastos de apertura y mantenimiento de cuentas asociadas, los cargos de tasación y los de envío postal de avisos. El IVA sobre los intereses computa solo si el prestatario es consumidor final.
- No computan, entre otros: los impuestos que gravan préstamos prendarios y personales, las tasas de reparticiones públicas, los honorarios de escribanía dentro del valor de plaza y el impuesto sobre los intereses y el costo financiero del endeudamiento empresario.
- Tampoco computan las comisiones por acuerdos de utilización de fondos como adelantos en cuenta corriente, mientras respondan estrictamente a la asignación y no dependan del capital efectivamente utilizado. En otras palabras, la comisión por tener el adelanto acordado y no usarlo queda afuera del CFT, aunque sea un costo real para la empresa.

La norma pide que en todos los documentos de la operación figuren la tasa nominal anual pactada, la efectiva anual, si la tasa es fija o variable y el CFT (punto 3.2). Según las normas de protección de los usuarios (punto 2.3.3), si el documento omite la tasa o el CFT, la entidad puede cobrar como máximo la tasa promedio de los plazos fijos de 30 a 59 días. Los dos textos son del BCRA, así que son dos documentos de una misma fuente. El de tasas de interés es el texto ordenado al 01/07/2024 y puede haber cambiado después.

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
