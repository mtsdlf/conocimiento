# Informe de investigación: Del registro al balance (record-to-report)

Fecha: 2026-11-27. Sesión 13 de 16 (issue #120). Ángulo: el cierre de período como recorrido entre dominios (decisión de #99: Contabilidad, Tesorería, Impuestos y Datos; Contabilidad se queda con el cómo registrar).

Marcas: [L] texto completo leído; [M] metadatos o resumen de la página; [S] resumen secundario o del buscador.

## Fuentes

| # | Fuente | Tipo | Autoridad | Profundidad | Ejemplos | Unicidad | Marca |
|---|---|---|---|---|---|---|---|
| F1 | APQC, Process Classification Framework 7.4 (agosto de 2024), categoría 9.0: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf | primaria | 3 | 2 | 1 | 3 | [L] (copia local del brief, pcf74.txt) |
| F2 | APQC, Open Standards Benchmarking Measure List, General Accounting and Reporting (291), impresa el 28/6/2018: https://www.apqc.org/sites/default/files/osb/291%20-%20GARC%20Measure%20List.pdf | primaria | 3 | 2 | 1 | 3 | [L] (las secciones de tiempo de ciclo y eficiencia; el resto de las 96 medidas, hojeado) |
| F3 | Perry D. Wiggins (APQC), «Metric of the Month: Cycle Time for Monthly Close», CFO.com, 5/3/2018: https://www.cfo.com/news/metric-of-the-month-cycle-time-for-monthly-close/659297/ | secundaria con datos de APQC | 2 | 2 | 2 | 3 | [L] a través de un extractor |
| F4 | OJP Financial Management and Support Center (Departamento de Justicia de EE. UU.), «Monthly Financial Close Policy» (guía para quienes reciben subsidios, sin fecha): https://www.ojp.gov/sites/ojp/files/media/document/FMSC_Monthly%20Financial%20Close%20Policy_Guide%20Sheet_Final_508.pdf | secundaria institucional; dice seguir recomendaciones del AICPA | 2 | 2 | 2 | 3 | [L] (PDF de 4 páginas, convertido a texto) |
| F5 | Therese Tucker (CEO de BlackLine), «Putting Continuous Accounting to Work», CFO.com, 6/5/2016: https://www.cfo.com/news/putting-continuous-accounting-to-work/661894/ | práctica comercial (proveedor de software) | 1 | 1 | 1 | 2 | [L] a través de un extractor |
| F6 | APQC, «End-to-End Process Maps and Measures: Record-to-Report» (noviembre de 2025): https://www.apqc.org/resource-library/resource-listing/end-end-process-maps-and-measures-record-report | primaria, solo socios | 3 | ? | ? | 3 | [S] (403; solo el resumen del buscador) |
| F7 | Romney y Steinbart, Accounting Information Systems, capítulo del sistema de mayor general y reportes (GLARS) | libro de texto | 3 | ? | ? | 2 | [S] (solo apuntes y diapositivas de terceros en el buscador) |
| F8 | Notas de la base: Contabilidad (ajustes de cierre, conciliaciones, registro contable, asiento y libros, cuentas corrientes, estados contables, normas contables, operaciones, compras y cuentas a pagar, costo de lo vendido, activos fijos, moneda extranjera, control interno), Impuestos (cumplimiento, registros fiscales, declaración y pago, resultado impositivo), Tesorería (posición de caja), Inventario (conteo cíclico), Datos (Visualización y BI) | base | — | — | — | — | [L] |

Cinco artículos de proveedores de software sobre «continuous accounting» (Sage, BlackLine, FloQast, NetSuite, Planergy) parafrasean la misma idea y cuentan como una sola línea de práctica comercial; solo se leyó F5.

## Afirmaciones

### Códigos APQC 7.4 (F1, [L])

- 9.3 «Perform general accounting and reporting (10730)».
- 9.3.2 «Perform general accounting (10748)», con 9.3.2.1 «Maintain chart of accounts», 9.3.2.2 «Process journal entries», 9.3.2.3 «Process allocations», 9.3.2.4 «Process period end adjustments (10822)», 9.3.2.5 «Post and reconcile intercompany transactions (10823)», 9.3.2.6 «Reconcile general ledger accounts (10824)», 9.3.2.7 «Perform consolidations and process eliminations (10825)», 9.3.2.8 «Prepare trial balance (10826)», 9.3.2.9 «Prepare and post management adjustments (10827)».
- 9.3.3 «Perform fixed-asset accounting (10749)», con 9.3.3.6 «Calculate and record depreciation expense (10833)» y 9.3.3.7 «Reconcile fixed-asset ledger (10834)».
- 9.3.4 «Perform financial reporting (10750)»: 9.3.4.1 «Prepare business unit financial statements», 9.3.4.2 «Prepare consolidated financial statements», 9.3.4.3 «Perform business unit reporting/review management reports», 9.3.4.5 «Prepare statements for board review», 9.3.4.6 «Produce quarterly/annual filings and shareholder reports», 9.3.4.7 «Produce regulatory reports», 9.3.4.8 «Perform legal and management consolidation».
- 9.7.2.1 «Manage and reconcile cash positions (10893)».
- 9.9.2 «Process taxes (10766)», con 9.9.2.2 «Prepare tax returns (10931)» y 9.9.2.5 «Account for taxes (10934)».
- 9.5.2.7 «Process period-end adjustments (10864)», dentro de la nómina, y 9.6.1.5 «Process financial accruals and reversals (10873)», dentro de cuentas a pagar: los cierres de cada dominio aparecen en el proceso de ese dominio, no en 9.3. Lectura de esta base: el marco funcional reparte el cierre, y por eso el recorrido entre dominios hace falta.

### El calendario del cierre (F4, [L])

- Definición: «A monthly financial close is a period from the first to last day of each month in which the "books are closed."»
- Cierre mensual: «according to the Generally Accepted Accounting Principles, it is a best practice to perform a monthly financial close.» Razón: un período corto tiene menos transacciones y reduce el riesgo de error; además «Monthly financial closes also promote timely preparation of quarterly financial reports».
- «These procedures are often a checklist outlining how a grantee reviews, records, reconciles, and balances accounting information in each monthly period.»
- La guía dice que «The American Institute of Certified Public Accountants has recommendations for closing cycle best practices organized by timeframes». No cita el documento del AICPA, que no se leyó.
- Calendario, literal en lo esencial:
  - «Four days prior to period end»: «Review the closing schedule and distribute it to staff»; «Corroborate recurring journal entries are correct and still needed for current period» (ejemplo: con rotación de personal, el asiento de sueldos recurrente puede no corresponder); «Download preliminary financial statements and verify for errors and unusual variances».
  - «Two days prior to period end»: «Verify any contractual agreements for obligations to be paid»; «Update fixed asset schedule and calculate/verify depreciation».
  - «One day prior to period end»: «Complete preliminary bank reconciliations»; «Audit inventory».
  - «Day of period end»: «Print or download all period-end reports and process period-end closing program»; el programa de cierre «cannot be modified after the period close».
  - «One day after period end»: «Reconcile general ledger balances to period-end reports»; «Complete accruals and close accounts receivable and payable books».
  - «Two days after period end»: «Complete financial statements»; «Process any back-dated adjusting entries needed to correct any errors, omissions, or inaccuracies not caught in the prior steps».
- Sobre la dependencia entre pasos: «the monthly close progress is subject to processes that are built upon one another or that are conditioned on the previous completion of another. If one falls behind, it could contribute to untimely final reporting.»
- Límite: es una guía para organizaciones chicas que reciben subsidios federales; el calendario de dos días después del cierre es una recomendación, no una medida. Quién hace cada tarea por área no lo dice; la asignación por dominio de la nota es lectura de esta base.

### Días de cierre (F2 [L], F3 [L])

- F2, tiempo de ciclo (8 medidas): 100162 «Cycle time in days to complete the monthly consolidated financial statements»; 100613 «Cycle time in days to perform annual close at the site level», definida como «Cycle time in calendar days between running trial balance to completing the consolidated financial statements»; 100625 «Cycle time in days to produce period-end management reports», definida como «Cycle time in calendar days from running the initial trial balance to completing the period-end management report»; 100597 de los informes preliminares («flash») a los estados consolidados; 100555 y 100552 de los estados a la publicación de resultados; 100591 «Cycle time in days to capitalize a fixed asset purchase».
- F3: la medida se define como «the cycle time in calendar days between running the trial balance» y la emisión de los estados consolidados, e incluye trabajo y espera. Mediana «6.4 calendar days»; cuartil superior «4.8 days or less»; cuartil inferior «10 or more calendar days»; «2,300 organizations that answered this survey question». Encuesta: General Accounting Open Standards Benchmarking. Publicado el 5/3/2018; los datos pueden ser viejos.
- F3, por qué se demora (resumen del extractor, con citas parciales): datos de mala calidad; sin plan de cuentas estándar (según los datos de APQC, adoptarlo ahorra unos dos días); definiciones financieras distintas entre sitios, que alargan la consolidación; sin gobierno del dato; procesos sin documentar; la carga de fin de mes (muchas conciliaciones y asientos se pueden hacer antes, con listas de control previas); fechas de corte poco claras (las áreas que no saben cuándo deja de registrar la contabilidad demoran contratos o facturas); usar el mayor para el detalle en lugar de auxiliares con asientos resumen.
- APQC publicó en mayo de 2025 un artículo «Cycle Time to Perform the Monthly Close» solo para socios ([S], no leído). La cifra vigente de la mediana queda sin verificar.

### Asientos manuales y de ajuste (F2, [L])

- 100848 «Manual journal entry line item percentage»: «Percentage of journal entry line items from a manual recurring source + Percentage of journal entry line items from a manual non-recurring source».
- 106325 «Percentage of corrective/adjusting journal entry line item types».
- 101765 «Percentage of journal entry line items processed error free the first time».
- 106333 «Percentage of total accruals generated using a fully manual method» (nombre leído en la lista; fórmula: «Percentage of total accruals generated manually»).

### Partidas conciliatorias viejas

- No se encontró una medida de APQC ni una fuente que defina la antigüedad de las partidas conciliatorias. HUECO. La nota la define como medida de esta base y lo dice.

### Cierre continuo (F5, [L]; resto [S])

- F5: «Continuous accounting is a measured and balanced alternative to compressing a month's (or more) worth of accounting tasks.» Sin datos; la autora es CEO de un proveedor de software de cierre.
- Resúmenes del buscador de otros proveedores ([S]): conciliaciones diarias o semanales según la cuenta; «continuous close» como poder hacer un cierre preliminar en cualquier momento. Una sola línea de práctica comercial; no se encontró evidencia independiente de que acorte el cierre.

### Romney y Steinbart (F7, [S])

- Según apuntes de terceros, el sistema de mayor general y reportes tiene cuatro actividades: actualizar el mayor, registrar los ajustes, preparar los estados y producir los informes de gestión; recibe asientos resumen de cada ciclo de transacciones, asientos no rutinarios del tesorero, cifras del presupuesto y ajustes del contador. No se leyó el libro: queda [S] y la nota lo dice.

### De la base (F8, [L])

- Ajustes de cierre: un ajuste no toca la caja; el ajuste que falta no descuadra el balance de sumas y saldos; hace falta una lista de ajustes recurrentes y la conciliación de cada cuenta (Contabilidad/Estados-contables/ajustes-de-cierre.md).
- Conciliaciones: banco contra libros, auxiliar contra control, entre empresas del grupo; los asientos que salen de ellas tienen que estar antes de emitir los estados (Contabilidad/Control-interno/conciliaciones.md, «Quién la usa después»).
- Libro de IVA como subdiario; su total tiene que coincidir con la cuenta de IVA del mayor antes de cada declaración (Impuestos/Cumplimiento/registros-fiscales.md).
- Cumplimiento: el contador necesita todos los comprobantes del período unos días antes del vencimiento; fallan la factura de compra que llega tarde, la nota de crédito sin registrar, la retención sufrida sin certificado (Impuestos/Cumplimiento/cumplimiento.md).
- Lo recibido sin facturar como pasivo al cierre (Contabilidad/Operaciones/compras-y-cuentas-a-pagar.md).
- La posición de caja se apoya en la conciliación (Tesorería/Caja-y-liquidez/posicion-de-caja.md).
- El resultado impositivo parte del resultado contable del ejercicio (Impuestos/Impuestos-a-la-renta/resultado-impositivo.md).
- Consolidación: NIIF 10, solo resumen de su página (Contabilidad/Estados-contables/normas-contables.md).
- El software de nómina leído contabiliza el devengamiento al confirmar recibos (Administracion-de-personal-y-nomina/Liquidacion-de-sueldos/liquidacion-de-sueldos.md, paso 7).

## Recurso canónico

- Para el calendario: F4 entera (cuatro páginas); fijarse en la tabla por días y en que cada tarea depende de la anterior.
- Para la medida: F2, sección «Cycle time», y F3 para los cuartiles de 2018.
- Para el mecanismo de cada ajuste: OpenStax, Principles of Financial Accounting, caps. 4 y 5, ya citado en Contabilidad.

## Huecos

- El documento del AICPA que F4 dice seguir: no se identificó ni se leyó.
- Una guía de cierre de un consejo profesional argentino (FACPCE o un CPCE): no se buscó a fondo; ninguna nota de la base la cita.
- El mapa R2R de APQC (F6) y su artículo de 2025 sobre el cierre: solo socios.
- Romney y Steinbart: no se leyó el capítulo.
- Antigüedad de partidas conciliatorias: sin fuente.
- Evidencia independiente sobre el cierre continuo.
- Cifras de APQC posteriores a 2018 para la mediana de días de cierre.

## Borrador para la nota de Argentina

Apartado «Del registro al balance»:

- El cierre mensual tira de los vencimientos. El IVA se determina y se paga cada mes con IVA Simple (F.2051), que desde el período de noviembre de 2025 reemplazó al Libro de IVA digital; la declaración parte de los comprobantes que ARCA ya tiene y el contribuyente los valida ([IVA en Argentina](../Impuestos/Impuestos-al-consumo/iva-en-argentina.md#iva-simple-reemplazó-al-libro-de-iva-digital)). Ingresos Brutos tiene calendario provincial, y con Convenio Multilateral se declara por SIFERE ([Ingresos Brutos](../Impuestos/Impuestos-al-consumo/ingresos-brutos.md#sifere-y-padrón-federal)). El F.931 de sueldos vence el mes siguiente al devengado, en tres fechas según la CUIT ([cargas sociales en la Argentina](../Administracion-de-personal-y-nomina/Cargas-y-declaraciones/cargas-sociales-en-argentina.md#la-declaración-mensual)). La agenda completa está en [impuestos en Argentina](../Impuestos/impuestos-en-argentina.md#el-calendario-de-vencimientos). El brief pedía «libro IVA digital»: la base dice que ya no rige, y conviene que la nota lo diga así.
- Para que el IVA declarado y el balance coincidan, el libro de IVA funciona como subdiario y se concilia con el mayor antes de declarar ([registros fiscales](../Impuestos/Cumplimiento/registros-fiscales.md#cómo-se-relaciona-con-la-contabilidad)); los libros y los subdiarios que pide el Código Civil y Comercial están en [libros contables en Argentina](../Contabilidad/Registro/libros-contables-en-argentina.md).
- Los estados anuales siguen la RT 54 de la FACPCE, o las NIIF si la empresa cotiza, y se reexpresan por inflación desde los cierres del 1 de julio de 2018 ([normas contables en Argentina](../Contabilidad/Estados-contables/normas-contables-en-argentina.md#el-ajuste-por-inflación)). Las sociedades del art. 299 y las controlantes presentan estados (consolidados, en el caso de las controlantes) ([libros contables en Argentina](../Contabilidad/Registro/libros-contables-en-argentina.md#los-estados-contables-de-las-sociedades)).
- El cierre anual alimenta la declaración de Ganancias de sociedades (F.713), que vence hasta el quinto mes después del cierre, con su propio ajuste por inflación impositivo ([Ganancias en Argentina](../Impuestos/Impuestos-a-la-renta/ganancias-en-argentina.md#la-declaración-jurada-anual), [ajuste por inflación impositivo](../Impuestos/Impuestos-a-la-renta/ganancias-en-argentina.md#ajuste-por-inflación-impositivo)).
