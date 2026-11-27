# Contabilidad, vertical Operaciones: informe de investigación

Fecha: 2026-11-27. Alcance: cómo se registra cada tipo de hecho habitual. Tema agnóstico; lo de Argentina queda fuera (hueco declarado al final).

Marcas: [L] texto completo leído, [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1 a 3 en autoridad / profundidad / ejemplos / unicidad (A/P/E/U). "Primaria" = la norma o el libro mismo; "secundaria" = guía de firma, proveedor de software, sitio educativo.

Aviso de método (normas IFRS). Las páginas `ifrs.org/issued-standards/list-of-standards/...` son solo resúmenes. El texto de las normas lo bajé de las ediciones HTML oficiales `https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/<norma>.html` y lo leí por búsqueda de párrafos, no entero: marca [L] parcial (los párrafos citados). Ese HTML pierde la numeración de varios párrafos: los números de párrafo que doy salen de referencias cruzadas internas y de la estructura conocida de cada norma; hay que confirmarlos antes de citar con número (los textos literales sí están leídos).

Aviso (OpenStax). El libro se llama "Principles of Accounting, Volume 1: Financial Accounting" (URL `principles-financial-accounting`). Es de EE. UU. (US GAAP, "$"); donde difiere de NIIF lo marco. Su licencia es CC BY-NC-SA y la página pide no usarlo para entrenar modelos sin permiso de OpenStax; abajo solo hay citas cortas y cifras para atribuir.

---

## 0. Sobre la división del árbol

La lista de componentes coincide a medias con cómo el campo divide esta vertical:

1. El campo divide por ciclos: ventas-a-cobro (order-to-cash), compra-a-pago (procure-to-pay), inventario y costos, activos fijos, nómina (hire-to-pay) y cierre (record-to-report). Los seis ciclos de `operaciones` lo respetan.
2. **gastos-y-rendiciones no es un ciclo propio en los textos**: es compra-a-pago con el empleado como proveedor (reembolso) o con adelanto (anticipo). Los libros lo tratan dentro de caja y control interno (OpenStax cap. 8, caja chica). Se sostiene como componente porque en software es un flujo distinto (aprobación, comprobante, rendición), pero hay que enlazarlo con compras.
3. **moneda-extranjera es transversal, no un ciclo**: toca ventas, compras, préstamos y caja. OpenStax no tiene capítulo de moneda extranjera; solo NIC 21 y contabilidad intermedia. Es el componente con menos fuentes abiertas introductorias.
4. **costo-de-lo-vendido e inventario** son un solo ciclo en los libros (OpenStax cap. 10): el costo de lo vendido es el efecto en resultados del mismo registro que mueve el inventario. Conviene mostrarlo en `operaciones` como segundo asiento de cada venta.
5. **Sueldos**: los libros lo tratan en pasivos corrientes (cap. 12), no como ciclo; dejarlo como sección es coherente.
6. **Incobrables y previsión** caen en "cuentas a cobrar" en el campo (OpenStax cap. 9), pero normativamente son instrumentos financieros (NIIF 9), no ingresos (NIIF 15). Dos normas distintas en un mismo componente.
7. **Deterioro y baja de activos**: la baja va con NIC 16; el deterioro es otra norma (NIC 36), solo mención.

---

## 1. operaciones (entrada: ciclos y documento que dispara cada asiento)

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| OpenStax 6.3, compras (inventario permanente) | https://openstax.org/books/principles-financial-accounting/pages/6-3-analyze-and-record-transactions-for-merchandise-purchases-using-the-perpetual-inventory-system | primaria (libro) | 3/2/3/2 | [L] |
| OpenStax 6.4, ventas (inventario permanente) | https://openstax.org/books/principles-financial-accounting/pages/6-4-analyze-and-record-transactions-for-the-sale-of-merchandise-using-the-perpetual-inventory-system | primaria (libro) | 3/2/3/2 | [L] |
| OpenStax 12.5, sueldos | https://openstax.org/books/principles-financial-accounting/pages/12-5-record-transactions-incurred-in-preparing-payroll | primaria (libro) | 3/2/3/2 | [L] |
| OpenStax 4.2, ajustes (diferimientos y devengamientos) | https://openstax.org/books/principles-financial-accounting/pages/4-2-discuss-the-adjustment-process-and-illustrate-common-types-of-adjusting-entries | primaria (libro) | 3/2/3/2 | [L] |
| OpenStax 11.2, capitalizar o gastar | https://openstax.org/books/principles-financial-accounting/pages/11-2-analyze-and-classify-capitalized-costs-versus-expenses | primaria (libro) | 3/2/2/2 | [L] |

Son cinco capítulos del mismo libro: una sola fuente de autoridad con cinco pasajes.

### Afirmaciones

- En inventario permanente cada venta lleva dos asientos: el ingreso y el costo. OpenStax: el 1-oct vende 55 impresoras a $350: Dr Cuentas por cobrar 19.250 / Cr Ventas 19.250, y Dr Costo de lo vendido 5.500 / Cr Inventario 5.500 (55 × $100). https://openstax.org/books/principles-financial-accounting/pages/6-4-analyze-and-record-transactions-for-the-sale-of-merchandise-using-the-perpetual-inventory-system
- Una compra a crédito es Dr Inventario / Cr Cuentas por pagar; el pago, Dr Cuentas por pagar / Cr Caja (30 computadoras a $400 = $12.000). https://openstax.org/books/principles-financial-accounting/pages/6-3-analyze-and-record-transactions-for-merchandise-purchases-using-the-perpetual-inventory-system
- Los sueldos se registran con un asiento de devengamiento (gasto contra pasivos) y otro de pago. https://openstax.org/books/principles-financial-accounting/pages/12-5-record-transactions-incurred-in-preparing-payroll
- Capitalizar es "the process by which a long-term asset is recorded on the balance sheet"; es gasto corriente lo que "did not help to extend the life of or improve the asset". https://openstax.org/books/principles-financial-accounting/pages/11-2-analyze-and-classify-capitalized-costs-versus-expenses
- Regla de los ajustes (un lado de resultados, otro de balance, nunca caja): me llegó por el buscador [S], no la verifiqué en el texto de 4.2. https://openstax.org/books/principles-financial-accounting/pages/4-2-discuss-the-adjustment-process-and-illustrate-common-types-of-adjusting-entries

### Matriz documento -> asiento (síntesis propia, no cita; el patrón viene de la fuente indicada)

| Ciclo | Documento o evento | Asiento típico | Patrón en |
|---|---|---|---|
| Ventas | Factura de venta / entrega | Dr Cuentas por cobrar / Cr Ventas; Dr Costo de lo vendido / Cr Inventario | OpenStax 6.4 |
| Ventas | Cobro | Dr Caja / Cr Cuentas por cobrar | OpenStax 6.4 |
| Ventas | Nota de crédito | Dr Devoluciones sobre ventas / Cr Cuentas por cobrar; Dr Inventario / Cr Costo de lo vendido | OpenStax 6.4 |
| Compras | Recepción sin factura | Dr Inventario / Cr Recepciones no facturadas (GRNI) | sección 3 |
| Compras | Factura del proveedor | Dr Inventario o gasto / Cr Cuentas por pagar | OpenStax 6.3 |
| Gastos | Rendición con comprobantes | Dr gasto / Cr Caja o deuda con el empleado | OpenStax 8.4 |
| Inventario | Rebaja a valor neto de realización | Dr resultados / Cr Inventario | NIC 2 |
| Activos | Compra de activo | Dr Activo / Cr Caja o Cuentas por pagar | OpenStax 11.2 |
| Activos | Depreciación del período | Dr Gasto de depreciación / Cr Depreciación acumulada | OpenStax 11.3 |
| Sueldos | Liquidación devengada | Dr Gasto de sueldos / Cr varios pasivos | OpenStax 12.5 |
| Cierre | Diferimientos y devengamientos | pares gasto-pasivo o ingreso-activo | OpenStax 4.2 |

### Ejemplo con números (OpenStax 6.4)

Venta del 1-oct (arriba). Devolución de 10 impresoras el 6-oct: Dr Devoluciones y rebajas sobre ventas 3.500 / Cr Cuentas por cobrar 3.500, y Dr Inventario 1.000 / Cr Costo de lo vendido 1.000. Rebaja de 300. Cobro del 15-oct con descuento de 10 % sobre 15.450 (19.250 - 3.500 - 300): Dr Caja 13.905, Dr Descuentos sobre ventas 1.545 / Cr Cuentas por cobrar 15.450. https://openstax.org/books/principles-financial-accounting/pages/6-4-analyze-and-record-transactions-for-the-sale-of-merchandise-using-the-perpetual-inventory-system

### Recurso canónico

OpenStax cap. 6 (6.3 y 6.4), más 4.2 y 12.5. Fijarse en: dos asientos por venta con inventario; devoluciones y descuentos en cuentas "contra", no restados de la venta.

---

## 2. ingresos-y-cuentas-a-cobrar

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| NIIF 15, texto oficial (HTML 2026) | https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15.html | primaria | 3/3/1/3 | [L] parcial (criterios del contrato, momento, presentación) |
| NIIF 15, Ejemplos ilustrativos | https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15-ie.html | primaria | 3/3/3/3 | [L] parcial (Ejemplo 38) |
| Resumen NIIF 15 en ifrs.org | https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/ | primaria (resumen) | 3/1/1/1 | [L] |
| NIIF 9, texto oficial (HTML 2026) | https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html | primaria | 3/3/1/3 | [L] parcial (5.5.15 y matriz de provisiones) |
| OpenStax 9.2, incobrables | https://openstax.org/books/principles-financial-accounting/pages/9-2-account-for-uncollectible-accounts-using-the-balance-sheet-and-income-statement-approaches | primaria (libro, US GAAP) | 3/3/3/2 | [L] |
| OpenStax 4.2, ingresos no devengados | https://openstax.org/books/principles-financial-accounting/pages/4-2-discuss-the-adjustment-process-and-illustrate-common-types-of-adjusting-entries | primaria (libro) | 3/2/3/2 | [L] |

### Afirmaciones

- Principio central: "an entity recognises revenue to depict the transfer of promised goods or services to the customer". https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/
- Cinco pasos (resumen oficial): identificar el contrato; identificar las promesas separadas; determinar el precio de la transacción (estimando la contraprestación variable); repartirlo entre las promesas según su precio de venta independiente; reconocer el ingreso al cumplir cada promesa, en un momento o a lo largo del tiempo. Misma URL.
- Vigencia: períodos anuales que empiezan en o después del 1 de enero de 2018, adopción anticipada permitida. Misma URL.
- Momento (párr. 31): "An entity shall recognise revenue when (or as) the entity satisfies a performance obligation by transferring a promised good or service (ie an asset) to a customer. An asset is transferred when (or as) the customer obtains control of that asset." https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15.html
- Criterios del contrato (párr. 9): las partes lo aprobaron y se comprometen; se identifican derechos y condiciones de pago; tiene sustancia comercial; y "it is probable that the entity will collect the consideration". Mismo URL.
- Un pasivo del contrato es "an entity's obligation to transfer goods or services to a customer for which the entity has received consideration (or an amount of consideration is due)". Una cuenta a cobrar es "an entity's right to consideration that is unconditional" (solo falta que pase el tiempo). Si el cliente paga, o el pago vence, antes de la entrega, se presenta un pasivo del contrato en lo que ocurra primero. Mismo URL.
- Ingreso diferido (OpenStax): "represents a customer's advanced payment for a product or service that has yet to be provided by the company"; es pasivo hasta que se presta. https://openstax.org/books/principles-financial-accounting/pages/4-2-discuss-the-adjustment-process-and-illustrate-common-types-of-adjusting-entries
- Incobrables (OpenStax): el método de la previsión estima la mala deuda al cierre con experiencia pasada y estándares de la industria: Dr Gasto por incobrables / Cr Previsión (contra-activo). La baja directa solo reconoce al identificar un cliente incobrable y, según el libro, "GAAP does not accept it because it violates the matching principle"; se usa para impuestos. https://openstax.org/books/principles-financial-accounting/pages/9-2-account-for-uncollectible-accounts-using-the-balance-sheet-and-income-statement-approaches
- NIIF 9 (5.5.15): para cuentas a cobrar comerciales y activos del contrato de NIIF 15 sin componente de financiación significativo, la entidad "shall always measure the loss allowance at an amount equal to lifetime expected credit losses". Admite como recurso práctico la matriz de provisiones con experiencia histórica ajustada: "An example of a practical expedient is the calculation of the expected credit losses on trade receivables using a provision matrix". https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html

### Discrepancia entre fuentes

OpenStax enseña la previsión con las bases de US GAAP clásico (porcentaje de ventas a crédito, de saldo de cuentas a cobrar, o por antigüedad). NIIF 9 exige pérdida esperada de por vida y admite la matriz de provisiones, parecida al método por antigüedad. Lo conceptual (previsión como contra-activo, baja contra previsión) es común; difiere la base de la estimación (histórica contra prospectiva). Dos fuentes independientes en lo normativo (libro de EE. UU. y NIIF 9); la comparación entre ambas es mi lectura.

### Ejemplos con números

1. NIIF 15, Ejemplo 38, caso B (contrato no cancelable, CU1.000): el importe vence el 31-ene-20X9: Dr Cuenta a cobrar 1.000 / Cr Pasivo del contrato 1.000. Cobro el 1-mar: Dr Caja 1.000 / Cr Cuenta a cobrar 1.000. Entrega el 31-mar: Dr Pasivo del contrato 1.000 / Cr Ingreso 1.000. Caso A (cancelable): cobro el 1-mar Dr Caja 1.000 / Cr Pasivo del contrato 1.000, y luego Dr Pasivo / Cr Ingreso. Si se factura antes del vencimiento, no se presentan cuenta a cobrar y pasivo en bruto, porque aún no hay derecho incondicional. https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15-ie.html
2. Ingreso diferido (OpenStax 4.2, anticipos de honorarios de un estudio de abogados; mismo patrón que una suscripción): cobro de 48.000: Dr Caja 48.000 / Cr Honorarios no devengados 48.000. Al cierre se devengó el 40 %: Dr Honorarios no devengados 19.200 / Cr Honorarios 19.200; quedan 28.800 de pasivo. https://openstax.org/books/principles-financial-accounting/pages/4-2-discuss-the-adjustment-process-and-illustrate-common-types-of-adjusting-entries
3. Previsión (OpenStax 9.2, BWW): ventas a crédito 458.230 × 5 % = 22.911,50: Dr Gasto por incobrables 22.911,50 / Cr Previsión 22.911,50. Baja del cliente Craft por 5.000: Dr Previsión 5.000 / Cr Cuenta a cobrar 5.000. Recupero parcial de 3.000: Dr Cuenta a cobrar 3.000 / Cr Previsión 3.000 y luego Dr Caja 3.000 / Cr Cuenta a cobrar 3.000. Por antigüedad: 14.574 + 20.420 + 23.103 = 58.097 (10 %, 20 %, 30 % sobre 145.740, 102.100 y 77.010). Con método de saldo: 324.850 × 15 % = 48.727,50; con previsión previa acreedora de 23.000 el ajuste es 25.727,50. Valor neto: 90.000 - 4.800 = 85.200. https://openstax.org/books/principles-financial-accounting/pages/9-2-account-for-uncollectible-accounts-using-the-balance-sheet-and-income-statement-approaches (el libro trae una errata evidente, "42,500" por 2.500, sin efecto en el resultado de 3.500)
4. Factura, nota de crédito y cobro con descuento: ver sección 1.

### Recurso canónico

1. NIIF 15 Ejemplos ilustrativos, Ejemplo 38, y los párrafos de presentación (pasivo del contrato, cuenta a cobrar, activo del contrato). Fijarse en: cuenta a cobrar es derecho incondicional; el activo del contrato no.
2. OpenStax 9.2 completo. Fijarse en: la previsión es estimación; la baja cancela contra la previsión y no toca resultados.

Anticipos con impuestos (IVA): jurisdiccional, hueco.

---

## 3. compras-y-cuentas-a-pagar

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| OpenStax 6.3, compras | https://openstax.org/books/principles-financial-accounting/pages/6-3-analyze-and-record-transactions-for-merchandise-purchases-using-the-perpetual-inventory-system | primaria (libro) | 3/2/3/2 | [L] |
| Microsoft Learn (Dynamics 365 Finance), conciliación de tres vías | https://learn.microsoft.com/en-us/training/modules/work-invoice-matching-finance/three-way-matching | secundaria (proveedor de software) | 2/1/1/2 | [L] |
| Planergy, GRNI | https://planergy.com/blog/grni-reconciliation-process-benefits | secundaria (proveedor) | 1/2/2/1 | [L] |
| Resultados del buscador: Oracle (acumulación por recepción), AccountingCoach, Sage, Precoro, Softco | https://docs.oracle.com/cd/A60725_05/html/comnls/us/po/rcvacc02.htm | secundarias | 1-2/1/1/1 | [S] |

Las guías de proveedores parafrasean la misma práctica; cuentan como una sola fuente de práctica.

### Afirmaciones

- La conciliación de tres vías verifica que la variación de precio entre pedido y factura esté dentro de tolerancia y que la cantidad facturada coincida con las recepciones; si no, hay un error de cantidad. Sin ella "the system could post the invoice with errors and affect accounting further down the line". https://learn.microsoft.com/en-us/training/modules/work-invoice-matching-finance/three-way-matching
- La recepción sin factura crea un pasivo (GRNI): es un pasivo corriente, "an adjustment or contra account that's similar to an accrual account". Al llegar la mercadería: Dr Inventario / Cr GRNI. https://planergy.com/blog/grni-reconciliation-process-benefits
- Al llegar la factura se cancela GRNI contra la deuda con el proveedor. Las fuentes discrepan: la prosa de Planergy y el hilo de Oracle EBS (vía buscador) dicen Dr GRNI / Cr Cuentas por pagar; la tabla de Planergy muestra Cr Inventario (error aparente de la fuente). Se dan ambas. https://planergy.com/blog/grni-reconciliation-process-benefits
- En sistema periódico no se registra la recepción hasta la factura o el cierre, por lo que no hace falta GRNI [S, glosario de Softco]. https://softco.com/glossary/grni/
- Descuento por pronto pago y devoluciones reducen el inventario. https://openstax.org/books/principles-financial-accounting/pages/6-3-analyze-and-record-transactions-for-merchandise-purchases-using-the-perpetual-inventory-system
- OpenStax 6.3 no define pedido ni factura, ni trae ejemplo de flete.

### Ejemplos con números

1. OpenStax 6.3, descuento 5/10 n/30: 1-may compra de 67 tabletas a $60 = $4.020: Dr Inventario 4.020 / Cr Cuentas por pagar 4.020. Pago el 10-may con descuento de $201: Dr Cuentas por pagar 4.020 / Cr Inventario 201, Cr Caja 3.819. Pago el 25-may sin descuento: Dr Cuentas por pagar 4.020 / Cr Caja 4.020.
2. OpenStax 6.3, devolución y rebaja: 80 impresoras a $100 = 8.000; devolución de 15 dañadas: Dr Cuentas por pagar 1.500 / Cr Inventario 1.500; rebaja de 120: Dr Cuentas por pagar 120 / Cr Inventario 120; pago de 6.380 con descuento 5 % (319): Dr Cuentas por pagar 6.380 / Cr Inventario 319, Cr Caja 6.061. (Misma URL que 1.)
3. GRNI (Planergy): recepción de 5.000: Dr Inventario 5.000 / Cr GRNI 5.000. Recibe por 2.000 y la factura dice 2.500: se revierte lo registrado, Dr GRNI 2.000 / Cr Inventario 2.000, y se registra el valor correcto de la factura. https://planergy.com/blog/grni-reconciliation-process-benefits

### Recurso canónico

No hay uno único de autoridad y abierto para tres vías y GRNI. Propongo OpenStax 6.3 (asiento de compra, descuentos y devoluciones) y, como segundo recurso declarado secundario, Microsoft Learn (el control) y Oracle "Accrual Process for Perpetual Accruals" (el asiento). Fijarse en: el pasivo nace con la recepción, no con la factura.

---

## 4. gastos-y-rendiciones

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| OpenStax 8.4, caja chica | https://openstax.org/books/principles-financial-accounting/pages/8-4-define-the-purpose-and-use-of-a-petty-cash-fund-and-prepare-petty-cash-journal-entries | primaria (libro) | 3/2/3/2 | [L] |
| Washington State Auditor, Best practices for travel and reimbursable expenses (ene 2024) | https://www.sao.wa.gov/sites/default/files/2024-01/Travel_and_Reimbursable_Expenses_1_11_24_updated.pdf | guía de auditoría del sector público de EE. UU., secundaria | 2/2/1/2 | [L] (PDF pasado a texto) |
| MNCPA, Employee expense reimbursements | https://mncpa.org/publications/footnote/2015-02/employee-expense-reimbursements-legitimate-or-fraudulent | secundaria (colegio profesional) | 2/1/1/1 | [S] |
| NY Office of the State Comptroller, auditoría de anticipos | https://www.osc.ny.gov/files/state-agencies/pdf/XII-4-B-1-att6.pdf | guía de auditoría, secundaria | 2/2/1/1 | [S] |

### Afirmaciones

- Caja chica: "a predetermined amount of cash held on hand to be used to make payments for small day-to-day purchases"; es "a type of imprest account" que "contains a fixed amount of cash that is replaced as it is spent". https://openstax.org/books/principles-financial-accounting/pages/8-4-define-the-purpose-and-use-of-a-petty-cash-fund-and-prepare-petty-cash-journal-entries
- El gasto se carga al reponer el fondo contra los comprobantes; un faltante va a "Cash Over and Short" y un sobrante invierte el asiento. Misma URL.
- Anticipos (guía de Washington): limitar los anticipos "to 75 percent of estimated travel expenses" (viñeta; confirmar en la página), no darlos demasiado pronto, asignar a alguien el seguimiento de los vencidos, no dar un anticipo nuevo a quien no rindió el anterior (cita la ley estatal RCW 42.24.140), y resolver los anticipos pendientes antes de la liquidación final de quien se va. Pide una política clara, revisada cada año y actualizada al menos cada tres años. https://www.sao.wa.gov/sites/default/files/2024-01/Travel_and_Reimbursable_Expenses_1_11_24_updated.pdf
- Rendiciones [S]: comprobantes originales, propósito del negocio, aprobación firmada y fechada, revisión de segundo nivel sobre una muestra (MNCPA); la conciliación de anticipos la hace alguien que no registra cobros ni pagos (NY OSC). Ver URLs de la tabla.
- Lo del "accountable plan" del IRS que menciona la guía de Washington es régimen de EE. UU., se descarta.

### Ejemplo con números (OpenStax 8.4, Galaxy's Best Yogurt)

Constitución del 1-jul: Dr Caja chica 75 / Cr Caja 75. Reposición del 31-jul: Dr Franqueo 30, Dr Inventario 10, Dr Gastos varios 5 / Cr Caja 45. Aumento del 1-ago: Dr Caja chica 25 / Cr Caja 25 (fondo a 100). Faltante: Dr Cash Over and Short 5 / Cr Caja 5. https://openstax.org/books/principles-financial-accounting/pages/8-4-define-the-purpose-and-use-of-a-petty-cash-fund-and-prepare-petty-cash-journal-entries

### Recurso canónico

OpenStax 8.4 (mecanismo imprest) y la guía del Auditor de Washington (políticas, anticipos, seguimiento). Fijarse en: las dos son de EE. UU.; la lógica de control (fondo fijo, comprobante, aprobación, quien registra no concilia) es universal, pero hay que decir de dónde viene.

---

## 5. costo-de-lo-vendido

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| NIC 2, texto oficial (HTML 2026) | https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias2.html | primaria | 3/3/1/3 | [L] parcial |
| NIC 2, copia PDF en ktkt.uel.edu.vn (edición antigua del volumen de normas; Introducción, párr. 9, 23-34) | https://ktkt.uel.edu.vn/Resources/Docs/SubDomain/ktkt/VanBan/IAS/ias2_en.pdf | primaria (espejo) | 3/3/1/1 | [L] parcial |
| NIC 2, Fundamentos de las conclusiones BC9-BC20 (copia AASB) | https://www.aasb.gov.au/admin/file/content105/c9/IAS2_BC_1-22.pdf | primaria (texto de IFRS Foundation) | 3/3/1/3 | [L] parcial |
| Resumen NIC 2 en ifrs.org | https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/ | primaria (resumen) | 3/1/1/1 | [L] |
| OpenStax 10.3, método permanente | https://openstax.org/books/principles-financial-accounting/pages/10-3-calculate-the-cost-of-goods-sold-and-ending-inventory-using-the-perpetual-method | primaria (libro) | 3/3/3/2 | [L] |
| OpenStax cap. 10 (resumen, 10.1, 10.2) | https://openstax.org/books/principles-financial-accounting/pages/10-summary | primaria (libro) | 3/2/2/2 | [S] (solo por buscador) |

El HTML de ifrs.org y el PDF espejo son la misma norma: una sola fuente.

### Afirmaciones

- IN13: "The Standard does not permit the use of the last-in, first-out (LIFO) formula to measure the cost of inventories." https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias2.html (también en el PDF espejo)
- Párr. 9: "Inventories shall be measured at the lower of cost and net realisable value." https://ktkt.uel.edu.vn/Resources/Docs/SubDomain/ktkt/VanBan/IAS/ias2_en.pdf
- Fórmulas (párr. 23 y 25): identificación específica para ítems no intercambiables y bienes segregados por proyecto; para el resto, "first-in, first-out (FIFO) or weighted average cost formula", la misma fórmula para inventarios de similar naturaleza y uso. El promedio puede calcularse periódicamente o con cada recepción (párr. 27). Misma URL.
- Por qué no LIFO (BC10): "This is generally not a reliable representation of actual inventory flows." BC19: "The Board decided to eliminate the LIFO method because of its lack of representational faithfulness of inventory flows." Y los motivos fiscales no justifican un tratamiento contable (BC20). https://www.aasb.gov.au/admin/file/content105/c9/IAS2_BC_1-22.pdf
- NRV: precio de venta estimado en el curso normal del negocio menos costos de terminación y venta (resumen oficial). Normalmente se rebaja ítem por ítem; no se rebaja por clase en bloque ("finished goods"); se reevalúa en cada período (párr. 29 y 33). https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/ ; https://ktkt.uel.edu.vn/Resources/Docs/SubDomain/ktkt/VanBan/IAS/ias2_en.pdf
- Permanente contra periódico [S]: el permanente se actualiza en cada compra y venta (el promedio se recalcula en cada cambio de unidades); el periódico se cuenta al cierre y el promedio es el total disponible dividido por las unidades disponibles. https://openstax.org/books/principles-financial-accounting/pages/10-summary
- OpenStax define LIFO como "the last units purchased are the first units sold" y no menciona NIIF. https://openstax.org/books/principles-financial-accounting/pages/10-3-calculate-the-cost-of-goods-sold-and-ending-inventory-using-the-perpetual-method

### Discrepancia entre fuentes

OpenStax enseña LIFO como método disponible; NIC 2 lo prohíbe. No es un error: son marcos distintos (US GAAP lo admite). La nota debe decir qué marco aplica.

### Ejemplo con números (OpenStax 10.3, permanente)

Julio: inventario inicial 150 u. a $21 ($3.150); 5-jul venta de 120 a $36; 10-jul compra de 225 a $27 ($6.075); 15-jul venta de 180 a $39; 25-jul compra de 210 a $33 ($6.930); quedan 285 u. Disponible $16.155; ventas $11.340.

| Método | Costo de lo vendido | Inventario final | Margen bruto |
|---|---|---|---|
| FIFO | 7.200 | 8.955 | 4.140 |
| LIFO | 7.380 | 8.775 | 3.960 |
| Promedio ponderado | 7.253 | 8.902 | 4.087 |

Asientos de la venta del 5-jul: Dr Cuentas por cobrar o Caja 4.320 / Cr Ventas 4.320, y Dr Costo de lo vendido 2.520 / Cr Inventario 2.520 (120 × $21). Venta del 15-jul bajo FIFO: Dr Costo 4.680 / Cr Inventario 4.680 (30 × $21 + 150 × $27; lo verifiqué). La página dice "Journal entries are not shown": los asientos son derivados de las cifras (por la página misma o por mí), no transcriptos del libro. https://openstax.org/books/principles-financial-accounting/pages/10-3-calculate-the-cost-of-goods-sold-and-ending-inventory-using-the-perpetual-method

Ejemplo numérico de valor neto de realización: no encontré en fuente abierta (hueco).

### Recurso canónico

NIC 2: IN13, párr. 9, 23-33 y BC9-BC20; más OpenStax 10.3 por el cuadro de los tres métodos sobre las mismas compras. Fijarse en: con precios que suben, FIFO da el mayor margen y el mayor inventario (cifras de arriba); el método cambia resultado y balance, no el efectivo.

---

## 6. activos-fijos-y-amortizacion

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| NIC 16, texto oficial (HTML 2026) | https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias16.html | primaria | 3/3/1/3 | [L] parcial |
| Resumen NIC 16 en ifrs.org | https://www.ifrs.org/issued-standards/list-of-standards/ias-16-property-plant-and-equipment/ | primaria (resumen) | 3/1/1/1 | [L] |
| OpenStax 11.2, capitalizar o gastar | https://openstax.org/books/principles-financial-accounting/pages/11-2-analyze-and-classify-capitalized-costs-versus-expenses | primaria (libro) | 3/2/2/2 | [L] |
| OpenStax 11.3, métodos de depreciación | https://openstax.org/books/principles-financial-accounting/pages/11-3-explain-and-apply-depreciation-methods-to-allocate-capitalized-costs | primaria (libro) | 3/3/3/2 | [L] |
| OpenStax 11.5, cambio de estimación y baja | https://openstax.org/books/principles-financial-accounting/pages/11-5-describe-some-special-issues-in-accounting-for-long-term-assets | primaria (libro) | 3/3/3/2 | [L] |

### Afirmaciones

- Reconocimiento (párr. 7): el costo "shall be recognised as an asset if, and only if" es probable que fluyan beneficios económicos futuros y el costo se pueda medir con fiabilidad. https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias16.html
- El servicio diario (mano de obra, consumibles, puede incluir "the cost of small parts") no se capitaliza: va a resultados (párr. 12). Misma URL.
- Costo: el equivalente al precio de contado a la fecha de reconocimiento; si el pago se difiere más allá del crédito normal, la diferencia es interés (párr. 23). Resumen oficial: incluye precio de compra neto de descuentos, costos directamente atribuibles y estimación de desmantelamiento. Misma URL y https://www.ifrs.org/issued-standards/list-of-standards/ias-16-property-plant-and-equipment/
- OpenStax: el costo incluye envío, impuestos, armado y honorarios legales; una comisión de $8.000 sobre un terreno de $100.000 lo deja en $108.000. Mantenimiento de rutina y reparaciones menores se gastan; las mejoras que extienden la vida o la capacidad se capitalizan. https://openstax.org/books/principles-financial-accounting/pages/11-2-analyze-and-classify-capitalized-costs-versus-expenses
- Cada parte significativa se deprecia por separado (párr. 43); el terreno no se deprecia (vida ilimitada, salvo canteras y similares) y el edificio sí. Misma URL del HTML.
- "The depreciable amount of an asset shall be allocated on a systematic basis over its useful life." (párr. 50). El importe depreciable es el costo menos el valor residual. Empieza cuando el activo está disponible para usar; cesa en la reclasificación a mantenido para la venta o en la baja; no cesa porque esté ocioso. Misma URL.
- Vida útil y valor residual se revisan al menos al cierre de cada ejercicio y el cambio es de estimación contable (párr. 51); igual con el método (párr. 61). Métodos: lineal, saldo decreciente y unidades de producción; se elige "the method that most closely reflects the expected pattern of consumption of the future economic benefits" (párr. 62). Misma URL.
- Un método basado en ingresos está prohibido (enmienda de 2014). https://www.ifrs.org/issued-standards/list-of-standards/ias-16-property-plant-and-equipment/
- Baja (párr. 67): en la disposición o cuando no se esperan beneficios futuros. Resultado (párr. 71): producto neto de la disposición menos importe en libros, a resultados, y "Gains shall not be classified as revenue". Misma URL del HTML.
- Deterioro: solo mención (NIC 36). OpenStax 11.5 habla de obsolescencia y no usa el término deterioro. https://openstax.org/books/principles-financial-accounting/pages/11-5-describe-some-special-issues-in-accounting-for-long-term-assets

### Discrepancia entre fuentes

Coinciden en lo conceptual. Difieren en vocabulario (salvage value contra valor residual; el "double-declining" de OpenStax es un caso de saldo decreciente que NIC 16 no nombra). NIC 16 admite además el modelo de revaluación, que OpenStax no cubre.

### Ejemplos con números

1. OpenStax 11.3 (máquina de serigrafía): costo $10.000, residual $1.000, vida 5 años o 100.000 impresiones; 20.000 en el año 1 y 30.000 en el año 2.

| Método | Año 1 | Año 2 |
|---|---|---|
| Lineal (10.000 - 1.000)/5 | 1.800 | 1.800 |
| Unidades de producción (9.000/100.000 = $0,09 por impresión) | 1.800 | 2.700 |
| Saldo decreciente doble ((10.000 - 0)/5 × 2; luego (10.000 - 4.000)/5 × 2) | 4.000 | 2.400 |

Asiento de cada año: Dr Gasto de depreciación / Cr Depreciación acumulada por el importe de la tabla. https://openstax.org/books/principles-financial-accounting/pages/11-3-explain-and-apply-depreciation-methods-to-allocate-capitalized-costs

2. OpenStax 11.5 (prensa de Kenzie): costo 58.000, residual 10.000, vida 5 años, lineal 9.600 por año; a los 3 años, depreciación acumulada 28.800 y valor en libros 29.200. Cambio de estimación (residual 6.000, vida restante 5 años): 23.200 / 5 = 4.640 por año. Venta a 31.000: Dr Caja 31.000, Dr Depreciación acumulada 28.800 / Cr Prensa 58.000, Cr Ganancia en venta 1.800. A 27.100: pérdida de 2.100. A 29.200: sin resultado. https://openstax.org/books/principles-financial-accounting/pages/11-5-describe-some-special-issues-in-accounting-for-long-term-assets
3. Compra: Dr Máquina 5.000 / Cr Caja 5.000 (OpenStax 11.2, 1-ene-2019).

### Recurso canónico

OpenStax 11.3 (tres métodos sobre un mismo activo) y 11.5 (cambio de estimación y baja), más NIC 16 párr. 7, 12, 43, 50-62, 67-71. Fijarse en: el método cambia cuándo se carga el costo, no cuánto; la ganancia o pérdida al vender depende de la depreciación acumulada a esa fecha; la ganancia no es ingreso.

---

## 7. moneda-extranjera

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| NIC 21, texto oficial (HTML 2026) | https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias21.html | primaria | 3/3/1/3 | [L] parcial (definiciones, 9, 21-23, 28) |
| Resumen NIC 21 en ifrs.org | https://www.ifrs.org/issued-standards/list-of-standards/ias-21-the-effects-of-changes-in-foreign-exchange-rates/ | primaria (resumen) | 3/1/1/1 | [L] |
| PwC Viewpoint, Foreign currency (US GAAP, ASC 830), ejemplo FX 4-2 | https://viewpoint.pwc.com/dt/us/en/pwc/accounting_guides/foreign_currency/foreign_currency__2_US/chapter_4_foreign_cu_US/44_subsequent_measur_US.html | secundaria (firma), US GAAP | 2/2/3/1 | [L] |
| Oracle (JD Edwards), Infor, Sage Intacct: ganancias realizadas y no realizadas | https://docs.oracle.com/cd/E16582_01/doc.91/e15123/processcurrlossgainap.htm | secundarias (proveedores) | 1/1/2/1 | [S] |

OpenStax no tiene capítulo de moneda extranjera.

### Afirmaciones

- Moneda funcional: "the currency of the primary economic environment in which the entity operates"; cualquier otra es moneda extranjera. https://www.ifrs.org/issued-standards/list-of-standards/ias-21-the-effects-of-changes-in-foreign-exchange-rates/
- Indicadores (párr. 9): la moneda que influye en los precios de venta (a menudo aquella en que se denominan y liquidan) y la que influye en los costos de mano de obra, materiales y otros; si son mixtos, la gerencia usa su juicio y prioriza los indicadores principales. https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias21.html
- Reconocimiento inicial (párr. 21): se registra en moneda funcional con "the spot exchange rate ... at the date of the transaction"; por razones prácticas puede usarse un tipo promedio semanal o mensual, salvo que los tipos fluctúen significativamente (párr. 22). Misma URL.
- Al cierre (párr. 23): las partidas monetarias, al tipo de cierre; las no monetarias a costo histórico, al tipo de la fecha de la transacción; las no monetarias a valor razonable, al tipo de la fecha en que se midió. Misma URL.
- Las diferencias de cambio por liquidar partidas monetarias o por convertirlas a tipos distintos "shall be recognised in profit or loss in the period in which they arise" (párr. 28), salvo la excepción del párr. 32 (inversión neta en el extranjero). Misma URL.
- Partida monetaria: derecho a recibir (u obligación de entregar) "a fixed or determinable number of units of currency". Misma URL.
- NIC 21 no usa "realizada" y "no realizada": habla de diferencias por liquidar y por convertir al cierre. La terminología realizada/no realizada es de la práctica y de las guías de ERP [S]; en NIIF ambas van a resultados del período.

### Ejemplo con números (PwC, US GAAP; la mecánica de partidas monetarias es equivalente a NIC 21, pero no encontré un ejemplo bajo NIIF)

Moneda funcional USD. 1-ago-20X1: impresoras compradas a crédito por GBP 1.000 a USD 1,5 por GBP (pasivo inicial USD 1.500). 30-sep, tipo 1,4: remedición GBP 1.000 × 1,4 = USD 1.400: Dr Cuentas por pagar 100 / Cr Ganancia por diferencia de cambio 100. 15-oct, tipo 1,3: remedición Dr Cuentas por pagar 100 / Cr Ganancia 100; pago Dr Cuentas por pagar 1.300 / Cr Caja 1.300. Las impresoras (no monetarias) no se ajustan. La ganancia total es 200: 100 pendiente al cierre y 100 al liquidar. https://viewpoint.pwc.com/dt/us/en/pwc/accounting_guides/foreign_currency/foreign_currency__2_US/chapter_4_foreign_cu_US/44_subsequent_measur_US.html

### Discrepancia entre fuentes

Las guías de ERP (Oracle, Sage Intacct) revierten la remedición no realizada al inicio del período siguiente y luego registran la realizada al pagar (vía buscador [S]); PwC remide de forma acumulativa sin reversa. Son dos formas de llegar al mismo resultado; es una decisión de diseño del sistema.

### Recurso canónico

NIC 21 párr. 8-9, 21-23 y 28 (texto oficial) y el ejemplo FX 4-2 de PwC como caso numérico, avisando que es US GAAP. Fijarse en: qué partidas son monetarias (se remiden al cierre) y cuáles no (quedan al tipo histórico).

---

## 8. Sueldos y su registro (sección)

### Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| OpenStax 12.5 | https://openstax.org/books/principles-financial-accounting/pages/12-5-record-transactions-incurred-in-preparing-payroll | primaria (libro, EE. UU.) | 3/2/3/2 | [L] |
| NIC 19, texto oficial (HTML 2026) | https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias19.html | primaria | 3/3/1/3 | [L] parcial (párr. 11 y 13) |
| OpenStax 4.2, sueldos devengados | https://openstax.org/books/principles-financial-accounting/pages/4-2-discuss-the-adjustment-process-and-illustrate-common-types-of-adjusting-entries | primaria (libro) | 3/2/3/2 | [L] |
| Paychex, accrued payroll | https://www.paychex.com/articles/payroll-taxes/accrued-payroll | secundaria | 1/1/2/1 | [S] |

### Afirmaciones

- NIC 19 párr. 11: cuando el empleado prestó el servicio, se reconoce el importe sin descontar de los beneficios a corto plazo "as a liability (accrued expense), after deducting any amount already paid" y "as an expense", salvo que otra norma permita incluirlos en el costo de un activo (NIC 2, NIC 16). https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias19.html
- Ausencias pagadas (párr. 13): las acumulativas se reconocen cuando el empleado presta el servicio que aumenta su derecho a ausencias futuras; las no acumulativas, cuando ocurre la ausencia. Misma URL. Es el fundamento del devengamiento de vacaciones.
- OpenStax 12.5 trata vacaciones y PTO como "considered estimated liabilities", sin plazo ni importe claros y sin asiento. https://openstax.org/books/principles-financial-accounting/pages/12-5-record-transactions-incurred-in-preparing-payroll
- Sueldos devengados al cierre: 5 empleados × $2.500 = $12.500: Dr Gasto de sueldos 12.500 / Cr Sueldos a pagar 12.500. https://openstax.org/books/principles-financial-accounting/pages/4-2-discuss-the-adjustment-process-and-illustrate-common-types-of-adjusting-entries

### Ejemplo con números (OpenStax 12.5, EE. UU.)

Sueldo bruto $2.000 (31-ago): Dr Gasto de sueldos 2.000 / Cr Seguro social 124, Medicare 29, impuesto federal 102, impuesto estatal 25, seguro de salud del empleado 200, plan de retiro 150, Sueldos a pagar (neto) 1.370. Pago del 1-sep: Dr Sueldos a pagar 1.370 / Cr Caja 1.370. Cargas del empleador: Dr Gasto por cargas 265 / Cr desempleo federal 12, desempleo estatal 100, seguro social 124, Medicare 29. Beneficio: Dr Gasto por beneficios 300 / Cr Seguro de salud a pagar 300. Porcentajes y cuentas son de EE. UU.; lo transferible es la estructura: bruto = gasto; retenciones y neto = pasivos; cargas del empleador = gasto adicional con su pasivo. https://openstax.org/books/principles-financial-accounting/pages/12-5-record-transactions-incurred-in-preparing-payroll

### Recurso canónico

OpenStax 12.5 (estructura del asiento) y NIC 19 párr. 11 y 13 (devengamiento y vacaciones). Fijarse en: el gasto nace cuando se presta el servicio, no cuando se paga.

---

## 9. Huecos

1. **Argentina**: nada local (normas de la FACPCE, factura electrónica, IVA en anticipos y notas de crédito, aportes y contribuciones, SAC y vacaciones, ajuste por inflación, tipos de cambio oficiales). Va en notas aparte.
2. **Tres vías y GRNI**: no hay fuente primaria, solo documentación de proveedores de software, y una (Planergy) tiene una tabla incoherente con su texto. El fundamento conceptual sería el devengamiento (NIC 37, párr. 11), que no leí.
3. **Valor neto de realización**: sin ejemplo numérico de fuente abierta; no revisé el apéndice de NIC 2.
4. **Moneda extranjera bajo NIIF**: el único ejemplo numérico es de US GAAP. Falta un ejemplo bajo NIC 21 y un capítulo de libro abierto.
5. **Anticipos y rendiciones**: ninguna fuente trae los asientos de un anticipo a empleado y su rendición (Dr Anticipos a rendir / Cr Caja; al rendir, Dr gasto / Cr Anticipos, con la diferencia contra Caja o deuda con el empleado). Si se escribe la nota, hay que marcar el ejemplo como construido. Las guías de auditoría son de sector público de EE. UU.; falta una del sector privado. El 75 % de la guía de Washington hay que confirmarlo en la página.
6. **OpenStax 10.1, 10.2 y el capítulo 9 salvo 9.2, y el cap. 5**: inventario periódico y definiciones de métodos quedaron en resultados del buscador [S]; no leí esas páginas.
7. **Números de párrafo**: los del HTML de ifrs.org se perdieron en varios casos; confirmar los de NIC 16, NIC 19, NIC 21 y NIIF 15 antes de citarlos con número.
8. **NIIF para las PYMES**: solo leí la página de entrada (edición de febrero de 2025, vigente desde el 1 de enero de 2027; la de 2015 se puede seguir usando hasta entonces). No leí secciones de inventarios, PPE, ingresos ni moneda extranjera, ni las diferencias con las NIIF completas.
9. **NIIF 15 en profundidad**: solo nivel de divulgación (cinco pasos, presentación, Ejemplo 38). No cubrí contraprestación variable, derecho de devolución ni licencias.
10. **Deterioro de activos (NIC 36)** y **NIIF 9 en detalle**: solo mención.
11. **Suscripción de software con asientos mensuales**: ninguna fuente trae el caso; el ejemplo de OpenStax es de honorarios de abogados (mismo patrón) y el de NIIF 15 es de un producto.
12. **Vigencia**: las páginas de ifrs.org se bajaron el 2026-11-27; no verifiqué enmiendas posteriores ni si la edición HTML 2026 de cada norma incorpora todas las vigentes. La copia de NIC 2 del espejo de uel.edu.vn es de una edición antigua.
