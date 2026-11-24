# Plan financiero mínimo: la planilla de caja a doce meses

Informe de investigación (2026-11-24). Ángulo: la proyección de caja mes a mes que dice cuántos meses se puede probar con la plata que hay, para dos socios con una empresa chica de servicios en Argentina (proyectos más abono mensual, sin inversores).

Marcas de lectura: **[L]** leído completo, **[L parcial]** leído en parte (se dice cuánto), **[M]** metadatos o abstract, **[S]** resumen secundario o del buscador (no leí la fuente). Puntajes de 1 a 3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U). Tipo: P = primaria, S = secundaria.

Aviso general sobre el método: las herramientas de lectura devuelven un resumen hecho por un modelo chico, no el texto crudo, salvo en los dos PDF que bajé y leí con `pdftotext` (Purdue y Duquesne). Por eso, salvo esos dos, ningún [L] es una lectura palabra por palabra: lo declaro como [L] cuando la página entró entera en la lectura y como [M] o [S] cuando no. Varias páginas (SCORE, Start Up Loans, BBVA, Wyoming SBDC, UNCOMA, UCCOR, FACPCE) devolvieron 403 o bloqueo anti-bots: de ellas solo tengo lo que dijo el buscador, y va marcado [S].

Resumen de la evidencia: lo bien sostenido es la mecánica de la planilla (OpenStax, Duquesne), el desfase entre facturar y cobrar, y que las proyecciones de emprendedores son optimistas (Cassar). Lo débil es cualquier cifra de colchón en meses (una sola fuente seria, y vista solo por el buscador) y todo lo de inflación aplicado a una empresa chica argentina (hueco casi total).

---

## 1. Qué es una proyección de flujo de caja a 12 meses

### Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 1.1 | OpenStax, *Principles of Finance* 2e, 19.6 "Using Excel to create the short-term plan" (libro de texto abierto) | https://openstax.org/books/principles-finance-2e/pages/19-6-using-excel-to-create-the-short-term-plan | P (texto) | 3/3/2/2 | [L] vía WebFetch (resumen del modelo, citas textuales) |
| 1.2 | Duquesne SBDC, "Dollars and Sense" (guía de 8 páginas de un centro SBDC) | https://www.sbdc.duq.edu/Files/Admin/Resources%20PDF/10-Dollars-And-Sense.pdf | P | 2/3/3/2 | [L parcial] texto extraído con pdftotext; leí desde la introducción hasta el ejemplo de tendencia estacional (aprox. 5 de 8 páginas); lo posterior (formularios) no |
| 1.3 | U.S. SBA, "Write your business plan" | https://www.sba.gov/business-guide/plan-your-business/write-your-business-plan | P | 3/1/1/1 | [L] vía WebFetch |
| 1.4 | U.S. SBA, "Calculate your startup costs" | https://www.sba.gov/business-guide/plan-your-business/calculate-your-startup-costs | P | 3/1/1/1 | [L] vía WebFetch |
| 1.5 | Start Up Loans (programa de la British Business Bank), "What is a cash flow forecast?" | https://www.startuploans.co.uk/cash-flow-forecast/ | P | 3/2/1/1 | [S] (403 al leerla; solo lo que dijo el buscador) |
| 1.6 | SCORE, "12 month cash flow statement" (plantilla) | https://www.score.org/resource/template/12-month-cash-flow-statement | P | 3/2/3/2 | [S] (403; solo el buscador y sus listados) |
| 1.7 | BBVA Argentina, "Flujo de caja: qué es y por qué es el pulso de tu negocio" | https://www.bbva.com.ar/economia-para-tu-dia-a-dia/ef/pymes/que-es-un-flujo-de-caja.html | S (banco, contenido comercial) | 1/1/1/1 | [S] (403) |
| 1.8 | Wolters Kluwer / Chase / QuickBooks, "cash flow vs profit" (varias páginas comerciales que dicen lo mismo) | https://www.chase.com/business/knowledge-center/manage/cash-flow-vs-profit | S | 1/1/1/0 | [S] (solo buscador). Cuentan como una sola fuente de baja calidad |

### Afirmaciones

- La proyección de caja (en el libro de texto, "cash budget") se arma con filas encadenadas: saldo inicial de caja, cobranzas, desembolsos, flujo neto (cobranzas menos desembolsos), saldo final preliminar, menos un saldo mínimo que fija la gerencia, y superávit o déficit; el saldo final de un mes es el inicial del siguiente. Cita: "The formula for net cash flow is cash collections less cash disbursements." https://openstax.org/books/principles-finance-2e/pages/19-6-using-excel-to-create-the-short-term-plan
- Facturar no es cobrar: "Keep in mind that projected monthly sales amounts are not equal to cash collected from sales." Las condiciones de crédito reparten el cobro en meses posteriores, y los pagos a proveedores también se desfasan (el ejemplo supone pago al mes siguiente). Las partidas que no son caja (depreciación) se excluyen. https://openstax.org/books/principles-finance-2e/pages/19-6-using-excel-to-create-the-short-term-plan
- Una guía de SBDC dice lo mismo para un negocio chico: el flujo de caja "shows cash when it's received and when it's paid out", por lo que la depreciación no aparece, pero sí capital e intereses de deudas; y "if you have a receivable, the projection should represent your typical receivable cycle, e.g., cash coming in over 30 to 90+ days." https://www.sbdc.duq.edu/Files/Admin/Resources%20PDF/10-Dollars-And-Sense.pdf
- Esa misma guía pide incluir "Always include your own draw or salary" y estimar cargas sociales sobre sueldos (12 a 15 % en EE.UU.; no sirve como cifra argentina), y acompañar la planilla con "a written assumption statement explaining how you derived the numbers." https://www.sbdc.duq.edu/Files/Admin/Resources%20PDF/10-Dollars-And-Sense.pdf
- Para pedir plata, la SBA recomienda proyecciones con "For the first year, be even more specific and use quarterly — or even monthly — projections", y estados de resultados, balances y flujos de caja a cinco años. No define filas ni da plantilla. https://www.sba.gov/business-guide/plan-your-business/write-your-business-plan
- Start Up Loans (British Business Bank) pide un flujo a 12 meses y lo define como "an estimation of the money you expect your business to bring in and pay out over a period [of] time"; hay que incluir la cuota del préstamo. [S] https://www.startuploans.co.uk/cash-flow-forecast/ (el texto es lo que reportó el buscador; no pude abrir la página)
- Resultado distinto de caja: varias páginas comerciales coinciden en que se puede tener ganancia contable y caja que baja (cuentas por cobrar, inventario), pero las cuento como una sola fuente [S] y de baja autoridad. La explicación primaria buena es la de OpenStax (cobranzas distintas de ventas). https://www.chase.com/business/knowledge-center/manage/cash-flow-vs-profit
- Un detalle de modelado sin fuente directa: las filas de la planilla del pedido (impuestos, retiros de socios) no aparecen como filas fijas en OpenStax; el aporte de Duquesne es "include your own draw" y las cargas sociales. Las filas "impuestos" y "retiros de los socios" las propongo yo como adaptación y quedan como hipótesis de diseño, no como regla citada.

Hallazgo sobre la SBA: aunque es el organismo más autorizado, sus dos páginas son casi vacías en esta materia (una frase sobre mensual en el primer año). No sirve como recurso canónico de la planilla.

### Recurso canónico (componente 1)

- Concepto y filas: OpenStax 19.6. Fijarse en la secuencia saldo inicial, cobranzas (distintas de ventas), desembolsos, saldo mínimo, déficit que obliga a financiarse. URL arriba.
- Aplicación a negocio chico: Duquesne SBDC "Dollars and Sense", sección "Cash Flow Projection": notas por fila (incluir el sueldo propio, ciclo de cobro de 30 a 90 días, supuestos escritos). URL arriba.
- Plantilla pública de 12 meses de una fuente seria: SCORE "12 Month Cash Flow Statement" (columna "pre-startup" para lo gastado antes del mes 1) https://www.score.org/resource/template/12-month-cash-flow-statement y la plantilla de Start Up Loans / British Business Bank https://www.startuploans.co.uk/cash-flow-forecast-template. [S] Las dos las conozco solo por el buscador porque devolvieron 403 al abrirlas: hay que descargar una y mirar sus filas antes de adoptarla. SCORE tiene además variantes locales (Houston, Maine, Nordeste de Massachusetts) con filas distintas.

---

## 2. Supuestos e hipótesis: ingresos de abajo hacia arriba, escenarios y sensibilidad

### Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 2.1 | Duquesne SBDC (ver 1.2), sección "Monthly sales estimates" | https://www.sbdc.duq.edu/Files/Admin/Resources%20PDF/10-Dollars-And-Sense.pdf | P | 2/3/3/2 | [L parcial] |
| 2.2 | Purdue Extension EC-725, "Estimating Breakeven Sales for Your Small Business" (Ehmke y Miller) | https://www.extension.purdue.edu/extmedia/EC/EC-725.pdf | P | 3/2/3/2 | [L parcial] texto con pdftotext; leí las páginas 1 a 3 (cálculo, margen de seguridad, tabla de sensibilidad); la parte final no |
| 2.3 | Cassar, "Are Individuals Entering Self-Employment Overly Optimistic?...", *Strategic Management Journal* 31(8), 2010 | https://econpapers.repec.org/RePEc:bla:stratm:v:31:y:2010:i:8:p:822-840 | P | 3/2/1/3 | [S] (abstract por buscador; el repositorio de Penn dio 403) |
| 2.4 | Guías de pronóstico "bottom-up" de ingresos (Launchrock, Toptal, Wall Street Prep, Aspire, etc.) | https://www.launchrock.com/library/expert-advice/bottoms-up-forecast | S (blogs de startups y capacitación) | 1/1/2/0 | [S] (solo el resumen del buscador) |
| 2.5 | IBM "what-if analysis" y Motley Fool "sensitivity analysis" (definiciones de escenario y sensibilidad) | https://www.ibm.com/topics/what-if-analysis | S | 1/1/1/0 | [S] |

### Afirmaciones

- Proyectar ingresos de abajo hacia arriba es multiplicar cantidad por precio, y el propio SBDC lo ejemplifica para servicios: "Estimate number of clients per month 30 / Average fee per client x $65 / Compute total monthly sales = $1,950", con la advertencia "The number of successful clients is the variable number that needs to be justified from reliable sources." https://www.sbdc.duq.edu/Files/Admin/Resources%20PDF/10-Dollars-And-Sense.pdf
- La misma guía advierte que prever ventas mensuales "is the hardest task" y que no hay fórmula, pero el método debe apoyarse en información verificable, con varias fuentes para contrastar. Sugiere partir de ventas previas, ratios de industria o cámaras sectoriales, y estimar capacidad operativa. https://www.sbdc.duq.edu/Files/Admin/Resources%20PDF/10-Dollars-And-Sense.pdf
- Ritmo de captación y bajas: el puente de clientes (clientes al final = clientes al inicio + nuevos - bajas) y los ingresos como clientes activos por precio mensual aparecen en guías de blogs de startups, pero son todas secundarias y el resumen es del buscador [S]. No encontré una fuente seria (organismo o libro de texto) que describa clientes × precio con captación y bajas para un negocio de abono. Es un hueco de fuente fuerte, no de método. https://www.launchrock.com/library/expert-advice/bottoms-up-forecast
- Escenarios y sensibilidad: Purdue muestra una tabla de sensibilidad concreta (precio +25 %, unidades +25 %, costos variables -25 %, costos fijos -25 %) y cómo cambia el resultado de $0 a -$20.000 o +$50.000; dice que sirve para ver "the potential effects of undesirable outcomes like a shortfall in sales or an overrun on costs". En ese ejemplo mover el precio +25 % da la mayor mejora ($50.000) y bajar unidades 25 % da la mayor pérdida ($-20.000). https://www.extension.purdue.edu/extmedia/EC/EC-725.pdf
- Duquesne aconseja: "Make estimates reasonable, but when in doubt use worse-case projections." https://www.sbdc.duq.edu/Files/Admin/Resources%20PDF/10-Dollars-And-Sense.pdf
- La definición de escenarios base/pesimista/optimista y de sensibilidad (una variable a la vez, para ver cuál pesa más) la tengo solo de IBM y Motley Fool por el buscador [S]. https://www.ibm.com/topics/what-if-analysis
- Qué supuesto mover primero: no hay fuente que lo diga para un servicio. De lo leído se desprende una regla de trabajo, no citada: mover primero los supuestos sobre los que la propia fuente advierte que son los más inciertos (cantidad de clientes y plazo de cobro; Duquesne los marca como los difíciles) y los que más cambian el resultado en la tabla de sensibilidad (unidades y precio en Purdue). Marcar como criterio propio.
- Sobre el sesgo al armar la proyección: Cassar encontró que "the preparation of projected financial statements results in more overly optimistic venture sale forecasts" (según el abstract, por buscador). [S] https://econpapers.repec.org/RePEc:bla:stratm:v:31:y:2010:i:8:p:822-840

### Recurso canónico (componente 2)

- Duquesne SBDC, "Monthly sales estimates" y "Service Business Example": es lo más cercano a clientes × precio con fuente seria. Fijarse en que cada variable lleve una justificación escrita.
- Purdue EC-725, tabla 1 de sensibilidad: mostrar qué pasa al mover una variable por vez. Fijarse en el margen de seguridad (ventas esperadas menos punto de equilibrio).
- Hueco: una guía seria de ingresos por abono con captación y bajas (ver sección final).

---

## 3. Pista, consumo y punto de equilibrio leídos en la planilla; colchón

La base ya define pista, default alive, ramen profitable y punto de equilibrio con Paul Graham (https://www.paulgraham.com/aord.html, comprobado por el buscador: "Default Alive or Default Dead?"). No se redefinen. Acá solo cómo se leen en una planilla mensual.

### Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 3.1 | Y Combinator, Dalton Caldwell, "Advice for Companies With Less Than 1 Year of Runway", 22/1/2015 | https://www.ycombinator.com/blog/advice-startups-running-out-of-money | P (practicante, YC) | 3/2/1/2 | [L] vía WebFetch |
| 3.2 | Y Combinator, Gustaf Alströmer, "How Much Should You Spend After Fundraising?", 18/10/2019 | https://www.ycombinator.com/blog/how-much-should-you-spend-after-fundraising | P | 3/1/1/1 | [L] vía WebFetch (casi no dice nada de runway) |
| 3.3 | Purdue EC-725 (ver 2.2): punto de equilibrio y margen de seguridad | https://www.extension.purdue.edu/extmedia/EC/EC-725.pdf | P | 3/2/3/2 | [L parcial] |
| 3.4 | Duquesne SBDC (ver 1.2): punto de equilibrio para servicios y "Paying Yourself" | https://www.sbdc.duq.edu/Files/Admin/Resources%20PDF/10-Dollars-And-Sense.pdf | P | 2/3/3/2 | [L parcial] |
| 3.5 | JPMorgan Chase Institute, "Cash is King: Flows, Balances, and Buffer Days: Evidence from 600,000 Small Businesses", 1/9/2016 | https://www.jpmorganchase.com/institute/all-topics/business-growth-and-entrepreneurship/report-cash-flows-balances-and-buffer-days | P (datos bancarios propios) | 3/3/1/3 | [L] de la página resumen vía WebFetch; el informe completo no |
| 3.6 | SCORE, "How much cash should a small business keep in reserve?" | https://www.score.org/blog/how-much-cash-should-small-business-keep-reserve | P | 3/1/1/1 | [S] (403; solo el buscador) |
| 3.7 | Wyoming SBDC, "Cash Reserves: How Much is Enough?" | https://www.wyomingsbdc.org/biz-tips/cash-reserves-how-much-is-enough | P | 2/1/1/1 | [S] (403; solo el buscador) |
| 3.8 | Wells Fargo, small business reserves tips | https://smallbusinessresources.wf.com/small-business-cash-reserves-tips/ | S (banco, contenido comercial) | 1/1/1/1 | [S] |

### Afirmaciones

- Cómo se lee la pista en la planilla: el saldo final de cada mes ya es la pista, y la fila de déficit contra el saldo mínimo (OpenStax) marca el mes en que hay que financiarse. Esto sale de la mecánica de la sección 1, no de una fuente que lo diga con esas palabras. La fórmula "pista en meses = caja / consumo neto mensual" no la encontré sostenida en ninguna fuente de las leídas: Caldwell, de YC, dice expresamente que no da fórmula. Hueco.
- Umbrales de pista de YC: con menos de tres meses de caja "hay que confrontar pasivos y cierre", y "<2 months is the point of no return" (menos de dos meses es el punto sin retorno), con la advertencia "Delaying taking action to reduce burn is a bad strategy." https://www.ycombinator.com/blog/advice-startups-running-out-of-money. Es la guía de una incubadora para startups que levantan capital, no para servicios sin inversores. Una sola fuente.
- Lo que más pesa en el consumo, según Caldwell: "Payroll costs are the most likely source of high burn scenario"; los alquileres son difíciles de salir; lo más fácil de recortar es marketing, PR y beneficios. https://www.ycombinator.com/blog/advice-startups-running-out-of-money
- Punto de equilibrio en servicios: es "simply the total of your operating expenses" dividido el precio por unidad. Ejemplo: gastos fijos mensuales $5.000 y tarifa $60 la hora dan 83 horas facturables. Y se suma el sueldo propio: con $3.000 de ingreso personal y margen de 55 % el punto de equilibrio sube de $9.091 a $14.545 de ventas. https://www.sbdc.duq.edu/Files/Admin/Resources%20PDF/10-Dollars-And-Sense.pdf (la fórmula de proyectos de servicio con costos variables es más completa en Purdue)
- Margen de seguridad: la diferencia entre ventas esperadas y punto de equilibrio. Purdue: si el mercado da 1.050 cajas y el equilibrio es 1.000, queda una ganancia de solo $4.000, y "Such a small margin for error may put the business's ability to cash flow at risk." (el texto llama "margin of safety" a esa diferencia entre ventas esperadas y equilibrio) https://www.extension.purdue.edu/extmedia/EC/EC-725.pdf
- Aviso de método: Duquesne y Purdue calculan el equilibrio sobre un año o un mes estable, no el equilibrio de caja con desfases de cobro. Que el equilibrio contable no es el equilibrio de caja es un hallazgo mío a partir de la sección 1, y solo lo encontré mencionado ("cash breakeven") en páginas de proveedores comerciales vistas por buscador [S].
- Cuánto colchón: la cifra "tres a seis meses de gastos" la tengo solo por el buscador atribuida a SCORE, y esa misma fuente dice que usarla para todo negocio "is misleading" (según el resumen del buscador). [S] https://www.score.org/blog/how-much-cash-should-small-business-keep-reserve
- Otras cifras de colchón, todas [S]: Wells Fargo dice 9 a 12 meses si el negocio es estacional o sensible a recesiones https://smallbusinessresources.wf.com/small-business-cash-reserves-tips/; Wyoming SBDC propone un piso de 2 veces los gastos operativos mensuales, sin considerar rentabilidad ni capital de trabajo https://www.wyomingsbdc.org/biz-tips/cash-reserves-how-much-is-enough. Otro resultado del buscador (una cámara local) sugiere empezar con un mes; no lo cito como fuente.
- Discrepancia: SCORE (3 a 6 meses), Wyoming SBDC (piso de 2 meses) y Wells Fargo (9 a 12 si hay estacionalidad) no coinciden y ninguna da evidencia empírica. YC (2 a 3 meses como zona de peligro) es otro tipo de colchón (de supervivencia, no de reserva). No hay dos fuentes independientes que respalden una cifra: es un hueco, con una regla de partida a validar.
- Dato empírico sobre cuánto colchón tienen en realidad: JPMorgan Chase Institute (600.000 pymes de EE.UU.): "The median small business holds 27 cash buffer days in reserve", "Half of all small businesses hold a cash buffer of less than one month", cuartil inferior 13 días y superior 62 días. https://www.jpmorganchase.com/institute/all-topics/business-growth-and-entrepreneurship/report-cash-flows-balances-and-buffer-days. Otros recortes del mismo Instituto, por el buscador [S]: mediana de 15 días en 25 áreas metropolitanas (2013 a 2017) y 17,6 días en snapshots de 2025. Describe lo que hay, no lo que conviene.

### Recurso canónico (componente 3)

- Pista y umbrales: YC, Caldwell 2015 (https://www.ycombinator.com/blog/advice-startups-running-out-of-money). Fijarse en que habla de startups con consumo de capital; el principio (actuar antes de los dos o tres meses) se adapta, las cifras no.
- Equilibrio y margen de seguridad: Purdue EC-725 para la mecánica y la sensibilidad; Duquesne para el caso de servicios con sueldo propio.
- Colchón: ningún recurso canónico. Usar JPMorgan "Cash is King" como dato de contexto (cuánto suelen tener) y SCORE como referencia de la regla de tres a seis meses [S], con el aviso de que es un solo origen.

---

## 4. Inflación y moneda

### Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 4.1 | ACCA, "Inflation and investment appraisal" (equipo examinador de Financial Management; sin fecha) | https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f9/technical-articles/inflation-investment-appraisal.html | P (organismo profesional, material de examen) | 2/2/3/2 | [L] vía WebFetch |
| 4.2 | Libro de texto *Financial Management: Principles and Applications*, sección 12.3 "Inflation and Capital Budgeting" | https://oreilly.com/library/view/financial-management-principles/9780134417219/xhtml/fileP7001012477000000000000000004D7F.xhtml | P (texto) | 2/1/1/1 | [S] (extracto truncado del buscador) |
| 4.3 | UNCOMA, trabajo sobre el tratamiento de la inflación en la proyección de flujos de fondos (Revista Administración) | https://revele.uncoma.edu.ar/index.php/administracion/article/download/2479/59184 | P (académica argentina) | 2/?/?/2 | [S] (bloqueo anti-bots; solo el buscador. No sé autor ni año) |
| 4.4 | Revista Contabilidad y Dirección (UCCOR), flujo de efectivo de una pyme de Bahía Blanca en moneda homogénea | https://revistas.bibdigital.uccor.edu.ar/index.php/CyD/article/download/858/944 | P | 2/?/?/2 | [S] (403) |
| 4.5 | Forbes Argentina, 23/8/2022, recomendaciones de Daniel Aterhortúa (CFO de Alegra) | https://www.forbesargentina.com/money/como-pymes-pueden-mantener-flujo-caja-epoca-inflacion-n21013 | S (prensa; recomendaciones de un proveedor de software contable) | 1/1/1/1 | [L] vía WebFetch |
| 4.6 | Documento sobre FACPCE (RT 6) y estado de flujo de efectivo en moneda homogénea | https://core.ac.uk/download/301086769.pdf | P | 2/?/?/1 | [S] (403; solo el buscador) |

### Afirmaciones

- Regla de consistencia (finanzas corporativas): los flujos nominales se descuentan a tasa nominal y los reales a tasa real; la relación es Fisher, (1 + i) = (1 + r)(1 + h). Con 9 % nominal y 4,8 % de inflación la tasa real es cerca de 4 %, y los dos VAN coinciden salvo redondeo. https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f9/technical-articles/inflation-investment-appraisal.html (el ejemplo del VAN y el cálculo de 4 % los tomo del resumen del buscador; WebFetch confirmó las definiciones)
- Definiciones citadas: "Nominal cash flows are current price terms cash flows that have been inflated into future values." y "Real cash flows are found by deflating nominal cash flows by the general rate of inflation." https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f9/technical-articles/inflation-investment-appraisal.html
- Inflación específica: precios, costos variables y costos fijos no suben igual; "if a real terms approach is adopted, the specific inflation rates cannot be ignored." Es decir, aun proyectando en moneda constante, hay que aplicar a cada partida su propia inflación antes de deflactar. https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f9/technical-articles/inflation-investment-appraisal.html
- Un segundo texto de finanzas dice que los flujos nominales se descuentan a tasa nominal; el extracto está truncado. [S] https://oreilly.com/library/view/financial-management-principles/9780134417219/xhtml/fileP7001012477000000000000000004D7F.xhtml. Entre ACCA y este texto hay dos fuentes independientes de la regla de consistencia, pero la segunda es débil.
- Contexto argentino por buscador [S]: la normativa contable de la FACPCE (RT 6) exige presentar el estado de flujo de efectivo en moneda homogénea; un artículo de la UCCOR reexpresó los estados de una pyme de Bahía Blanca por ese motivo y dice que en inflación la información nominal "genera distorsiones". Esto es contabilidad histórica, no proyección. https://revistas.bibdigital.uccor.edu.ar/index.php/CyD/article/download/858/944 y https://core.ac.uk/download/301086769.pdf. Lo normativo argentino lo marco y lo cito, sin investigarlo más.
- Consejos prácticos (Forbes Argentina, agosto de 2022, inflación interanual de ese momento 71 %): que los días de cuentas por cobrar sean menores a los días de cuentas por pagar; evaluar escenarios; preguntarse si los clientes seguirán comprando pese al aumento; cuidar salarios, proveedores, cargas sociales e impuestos. No da fórmula de actualización de precios, y es prensa con fuente comercial. https://www.forbesargentina.com/money/como-pymes-pueden-mantener-flujo-caja-epoca-inflacion-n21013
- Precios en moneda dura contra moneda local, actualización de precios y plazo de cobro con inflación: no encontré una fuente seria (manual, guía de organismo o universidad) que lo trate para una pyme de servicios que cobra proyectos y abono. Hueco.
- Pista de lógica (propia, derivada de Fisher y de la regla de coherencia, no citada): con cobros a 30 o 60 días y alta inflación, el plazo de cobro es un costo real; cuánto vale ese costo depende de la inflación del período y debe ser un supuesto explícito en la planilla.

### Recurso canónico (componente 4)

- ACCA, "Inflation and investment appraisal": por la regla de coherencia (nominal con nominal, real con real) y por la inflación específica de cada partida. Fijarse en que es material de examen para valuar proyectos, no una guía de planilla de caja. Hay que traducirlo a "la planilla se hace en una sola unidad y las partidas se actualizan por su propio índice".
- Para lo argentino: UNCOMA (proyección en moneda extranjera y efecto Fisher) como candidato, pero hay que abrirlo y leerlo antes de recomendarlo [S].

---

## 5. Cómo falla: errores en proyecciones y evidencia sobre planes de negocio

### Fuentes

| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 5.1 | Delmar y Shane (2003), "Does business planning facilitate the development of new ventures?", *Strategic Management Journal* 24(12): 1165-1185, DOI 10.1002/smj.349 | https://ideas.repec.org/a/bla/stratm/v24y2003i12p1165-1185.html | P | 3/2/1/3 | [M] abstract (parafraseado por la herramienta) |
| 5.2 | Brinckmann, Grichnik y Kapsa (2010), "Should entrepreneurs plan or just storm the castle?...", *Journal of Business Venturing* 25(1): 24-40 | https://ideas.repec.org/a/eee/jbvent/v25y2010i1p24-40.html | P | 3/2/1/3 | [M] abstract; no vi N de estudios ni tamaños de efecto |
| 5.3 | Lange, Mollov, Pearlmutter, Singh y Bygrave (2007), "Pre-start-up formal business plans and post-start-up performance: A study of 116 new ventures", *Venture Capital* 9(4): 237-256 | https://ideas.repec.org/a/taf/veecee/v9y2007i4p237-256.html | P | 2/2/1/3 | [M] abstract |
| 5.4 | Kirsch, Goldfarb y Gera (2009), "Form or substance: the role of business plans in venture capital decision making", *Strategic Management Journal* 30(5): 487-515, DOI 10.1002/smj.751 | https://ideas.repec.org/a/bla/stratm/v30y2009i5p487-515.html | P | 3/2/1/3 | [M] abstract |
| 5.5 | Hopp, Greene, Honig, Karlsson y Samuelsson (2018), réplica de Honig y Karlsson (2004), *Management Review Quarterly* 68(4): 361-398 | https://ideas.repec.org/a/spr/manrev/v68y2018i4d10.1007_s11301-018-0143-9.html | P | 2/1/1/3 | [M] abstract |
| 5.6 | Cassar (2010), SMJ 31(8): 822-840 (ver 2.3) | https://econpapers.repec.org/RePEc:bla:stratm:v:31:y:2010:i:8:p:822-840 | P | 3/2/1/3 | [S] |
| 5.7 | UNSW Newsroom, 2021, sobre "The sandwich game: founder-CEOs and forecasting as impression management" (Anseel y otros), *Journal of Business Venturing* (DOI 10.1016/j.jbusvent.2020.106075) | https://www.unsw.edu.au/newsroom/news/2021/01/how-investors-and-entrepreneurs-can-play-an-accurate-forecasting | S (nota institucional sobre un paper) | 2/1/1/2 | [L] de la nota vía WebFetch; el paper no |
| 5.8 | Wharton Knowledge, podcast con Gavin Cassar sobre sesgos y presupuestos | https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/biased-expectations-can-accounting-tools-lead-to-rather-than-prevent-executive-mistakes/ | S | 2/1/1/1 | [L] vía WebFetch |

### Afirmaciones

- Delmar y Shane (2003) estudian 223 empresas nuevas fundadas en los primeros nueve meses de 1998 por una muestra aleatoria de fundadores suecos. Sostienen que planificar es "an important precursor to action in new ventures" y que ayuda a decidir, equilibrar oferta y demanda de recursos y bajar lo abstracto a pasos operativos; esto reduciría la probabilidad de abandono y aceleraría el desarrollo del producto. Lo anterior es la hipótesis y el marco según el abstract; no leí los resultados. https://ideas.repec.org/a/bla/stratm/v24y2003i12p1165-1185.html
- Brinckmann, Grichnik y Kapsa (2010), meta-análisis: la planificación ayuda al desempeño, pero el efecto depende del contexto; la novedad de la empresa y el entorno cultural lo moderan, y proponen "a concomitant and dynamic approach that combines planning and learning". No vi cantidad de estudios ni tamaño del efecto. https://ideas.repec.org/a/eee/jbvent/v25y2010i1p24-40.html
- Lange y otros (2007), 116 empresas nuevas fundadas por egresados de Babson (1985 a 2003): las que arrancaron con plan escrito no rindieron distinto de las que no; solo vale la pena un plan detallado si hay que levantar capital sustancial de inversores institucionales o ángeles. Corrección sobre el pedido: no salió en el *Journal of Business Venturing* sino en *Venture Capital* 9(4). https://ideas.repec.org/a/taf/veecee/v9y2007i4p237-256.html
- Réplica posterior (2018, de Honig y Karlsson 2004, otro trabajo distinto de Lange): la conclusión original de que planificar formalmente no afecta el desempeño "does not hold"; el plan formal "affects survival but not profitability". No hay evidencia en lo leído de que esto invalide a Lange. https://ideas.repec.org/a/spr/manrev/v68y2018i4d10.1007_s11301-018-0143-9.html
- Kirsch, Goldfarb y Gera (2009): 722 pedidos de fondos a una firma de capital de riesgo de EE.UU.; la presencia de planes y parte de su contenido se asocian "weakly" con la decisión de financiar. Aclaración importante: este paper no mide si planificar sirve a quien funda, sino si el plan influye en el inversor. No se aplica a una empresa sin inversores. https://ideas.repec.org/a/bla/stratm/v30y2009i5p487-515.html
- Lectura conjunta (mía): la evidencia es mixta. Delmar-Shane (según su marco) y Brinckmann (meta-análisis) favorecen planificar con efecto condicionado; Lange no encuentra efecto; la réplica de 2018 encuentra efecto en supervivencia y no en ganancia; Kirsch habla del inversor. Ninguna de estas es sobre una planilla de caja; todas son sobre "plan de negocios" escrito, que es más amplio. No hay evidencia directa sobre la planilla de caja a doce meses. Hueco.
- Optimismo en las proyecciones: Cassar (2010): entre los emprendimientos que llegaron a operar, los individuos sobreestimaron ventas y empleo futuros, y preparar estados financieros proyectados volvió más optimistas los pronósticos de ventas (según abstract y resúmenes del buscador). [S] https://econpapers.repec.org/RePEc:bla:stratm:v:31:y:2010:i:8:p:822-840
- Anseel y otros (2021, nota de UNSW): los emprendedores "overestimate realised revenues by about 22 per cent" en pronósticos dados a inversores; fundadores-CEO se pasan 15 % y no fundadores 27 %. Es un estudio de empresas con inversores; no es una muestra de empresas chicas de servicios. https://www.unsw.edu.au/newsroom/news/2021/01/how-investors-and-entrepreneurs-can-play-an-accurate-forecasting
- Wharton, con Cassar: el presupuesto solo mejora la precisión de pronósticos de gerentes "less than 2%"; los informes internos "about 8.5%", y ambos juntos "about 12%" (empresas australianas, no emprendedores); y "about an 80% likelihood" de viabilidad creída por emprendedores contra la mitad que lo logró. https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/biased-expectations-can-accounting-tools-lead-to-rather-than-prevent-executive-mistakes/
- Cifras que NO usar: el buscador devolvió "revenue 388 % más alto y ganancia 136 % inflada" sin autor, muestra ni paper (la nota de Wharton no las contiene; aparecieron en un resultado del buscador de CBS News que no abrí). No las pude atribuir a nada: descartadas.
- Cifra que NO usar, bis: "el 82 % de las pequeñas empresas fracasa por problemas de flujo de caja" se repite en blogs atribuida a U.S. Bank o a SCORE, y el buscador no encontró el estudio original. El propio SCORE dice que el flujo de caja es "a symptom" de varias causas de fondo. Dato no verificado. https://www.score.org/resource/article/the-1-reason-small-businesses-fail-and-how-to-avoid-it [S]
- Olvidar impuestos y plazos de cobro como errores documentados: lo que tengo es la advertencia de las guías (Duquesne: ciclo de cobro de 30 a 90 días, cargas sociales, "worse-case") pero no un estudio que cuantifique cuántos emprendedores los olvidan. Hueco.

### Recurso canónico (componente 5)

- Para decidir si vale escribir el plan: Brinckmann, Grichnik y Kapsa (2010) por ser el único meta-análisis. Fijarse en la conclusión de combinar planificación y aprendizaje, y en que depende de lo nueva que es la empresa. Hay que acceder al paper completo (ScienceDirect) para ver cantidad de estudios y efecto: no los vi.
- Para el sesgo de optimismo: Cassar (2010), por mostrar que armar la proyección empuja al optimismo; y la nota de UNSW por la cifra de 22 %, con la salvedad de que es con inversores.
- Lange (2007) como contrapunto, sabiendo que es una muestra de egresados de Babson y que la conclusión es más matizada de lo que suele citarse (aclara el caso de levantar capital).

---

## Huecos

1. Colchón en meses: no hay dos fuentes independientes y sólidas. SCORE (3 a 6 meses), Wyoming SBDC (2x) y Wells Fargo (9 a 12 si hay estacionalidad) discrepan y las vi solo por el buscador. Falta una fuente con evidencia empírica sobre cuántos meses evitan quiebras de empresas de servicios.
2. Fórmula de pista y consumo neto como se lee en la planilla: no la encontré dicha en las fuentes leídas (Caldwell la omite). La planilla de OpenStax da la mecánica, pero la definición "pista = caja / consumo neto" queda como derivación propia.
3. Ingresos por abono con captación y bajas: solo blogs de startups (secundarias, [S]). Falta un libro de texto o guía de organismo.
4. Escenarios y "qué supuesto mover primero": solo la tabla de sensibilidad de Purdue y definiciones genéricas de IBM y Motley Fool [S]. La regla de mover primero cantidad de clientes y plazo de cobro es criterio propio.
5. Inflación aplicada a un flujo de caja de una pyme argentina: ACCA da la teoría (nominal/real, Fisher, inflación específica), pero no hay guía seria sobre moneda dura contra pesos, actualización de precios y plazos de cobro. Las fuentes argentinas (UNCOMA, UCCOR, FACPCE) devolvieron 403 o bloqueo y solo las vi por el buscador; hay que abrirlas a mano. El único consejo práctico accesible es Forbes Argentina 2022, de un proveedor.
6. Plantillas públicas de SCORE y Start Up Loans: no pude abrirlas (403). Hay que descargarlas a mano y revisar filas antes de recomendarlas. No encontré plantilla argentina de una fuente seria (Ministerio de Economía/Sepyme): la búsqueda no devolvió ninguna guía oficial.
7. Evidencia sobre planes: ninguna evalúa específicamente la planilla de caja. Kirsch es sobre inversores. Delmar y Shane, Brinckmann y Lange las leí solo como abstract y no vi efectos numéricos. El meta-análisis de 2010 queda sin N ni tamaño de efecto.
8. Errores específicos (olvidar impuestos, plazos de cobro): sin estudio que los cuantifique. Las cifras de optimismo verificables (22 %, Cassar) son de empresas con inversores o de nacientes en EE.UU., no de servicios en Argentina.
9. Impositivo argentino (no investigado a fondo, por pedido): el flujo debe incluir impuestos y cargas sociales; no hay fuente leída para Argentina. Marcado como pendiente de la nota de Legal-e-impuestos.
10. Fuentes que no encontré o no usé: no verifiqué un texto de Brealey y Myers sobre presupuesto de caja (el buscador no devolvió el libro), por lo que el texto canónico es OpenStax. No busqué Damodaran, HBR ni Kauffman. Un cuarto tramo de búsqueda para el componente 4 (precios en dólares contra pesos) no se hizo por el límite de tres rondas.
