# Investigación: modelado para BI sobre el software de gestión

Fecha: 2026-11-27. Fuentes primarias, con las citas literales en inglés.

**Cómo se leyó cada fuente.** Bajé las páginas de Kimball Techniques con `curl` y extraje el cuerpo completo (`div.pf-content`), así que todas están **leídas enteras**. Son cortas, de uno o dos párrafos. Los índices de Wiley son PDF oficiales de `media.wiley.com` convertidos con `pdftotext` y **leídos enteros**. El capítulo 1 del Toolkit también se leyó entero (es el extracto oficial de Wiley). El *white paper* de calidad de datos de Kimball lo **leí por páginas** (1 a 9 y 13 a 14, no entero). Los textos de Inmon salen de copias de archive.org de los originales, **leídas enteras** salvo donde aviso. Donde dice «snippet» solo vi el resultado del buscador.

En las citas cambié las ligaduras tipográficas del original (ﬁ, ﬂ) por «fi» y «fl». Aparte de eso, el texto es el original.

---

## 1. Los tres tipos de tabla de hechos, *factless* y semiaditivos

**Transaction fact table**: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/transaction-fact-table/> (leída entera)
> "A row in a transaction fact table corresponds to a measurement event at a point in space and time. Atomic transaction grain fact tables are the most dimensional and expressive fact tables; this robust dimensionality enables the maximum slicing and dicing of transaction data. Transaction fact tables may be dense or sparse because rows exist only if measurements take place."

**Periodic snapshot**: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/periodic-snapshot-fact-table/> (leída entera)
> "A row in a periodic snapshot fact table summarizes many measurement events occurring over a standard period, such as a day, a week, or a month. The grain is the period, not the individual transaction. [...] These fact tables are uniformly dense in their foreign keys because even if no activity takes place during the period, a row is typically inserted in the fact table containing a zero or null for each fact."

**Accumulating snapshot**: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/accumulating-snapshot-fact-table/> (leída entera)
> "A row in an accumulating snapshot fact table summarizes the measurement events occurring at predictable steps between the beginning and the end of a process. Pipeline or workflow processes, such as order fulfillment or claim processing, that have a defined start point, standard intermediate steps, and defined end point can be modeled with this type of fact table. There is a date foreign key in the fact table for each critical milestone in the process. [...] As pipeline progress occurs, the accumulating fact table row is revisited and updated. This consistent updating of accumulating snapshot fact rows is unique among the three types of fact tables. [...] They often include numeric lag measurements consistent with the grain, along with milestone completion counters."

**Lag/Duration facts**: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/lag-duration-fact/> (leída entera)
> "Rather than forcing the user's query to calculate each possible lag from the date/time stamps or date dimension foreign keys, just one time lag can be stored for each step measured against the process's start point. Then every possible lag between two steps can be calculated as a simple subtraction between the two lags stored in the fact table."

**Cuándo conviene cada tipo, y que se complementan.** Design Tip #167, «Complementary Fact Table Types» (Bob Becker, junio de 2014): <https://www.kimballgroup.com/2014/06/design-tip-167-complementary-fact-table-types/> (leída entera)
> "There are three fundamental types of fact tables in the data warehouse presentation area: transaction fact tables, periodic snapshot fact tables, and accumulating snapshot fact tables."
> "Transaction fact tables help answer the "how many?" question."
> "The periodic snapshot fact table does an excellent job of helping understand the volume of vehicles in our pipeline. It answers the "how much?" question."
> "The accumulating snapshot fact table supports the key efficiency measures of velocity."
> "Often the best design response is a combination of two, or even all three, fact table types."

**Factless fact tables**: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/factless-fact-table/> (leída entera)
> "Although most measurement events capture numerical results, it is possible that the event merely records a set of dimensional entities coming together at a moment in time. [...] Factless fact tables can also be used to analyze what didn't happen. These queries always have two parts: a factless coverage table that contains all the possibilities of events that might happen and an activity table that contains the events that did happen. When the activity is subtracted from the coverage, the result is the set of events that did not happen."

**Additive, Semi-Additive, and Non-Additive Facts**: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/additive-semi-additive-non-additive-fact/> (leída entera)
> "Semi-additive measures can be summed across some dimensions, but not all; balance amounts are common semi-additive facts because they are additive across all dimensions except time. Finally, some measures are completely non-additive, such as ratios. A good approach for non-additive facts is, where possible, to store the fully additive components of the non-additive measure and sum these components into the final answer set before calculating the final non-additive fact."

**El inventario como semiaditivo.** Lo dice la fe de erratas del Toolkit, 3.ª ed., capítulo 4, en la página del libro en Kimball Group: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/> (leída entera)
> "The only fully additive metric in the figure is Quantity Sold. The Quantity on Hand and inventory valuation metrics are semi-additive as they can't be simply summed over time periods; you would want to divide the sum by the number of daily observations to arrive at an average inventory balance or valuation."

**Year-to-Date Facts**: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/year-to-date-fact/> (leída entera)
> "YTD requests can easily morph into "YTD at the close of the fiscal period" or "fiscal period to date." A more reliable, extensible way to handle these assorted requests is to calculate the YTD metrics in the BI applications or OLAP cube rather than storing YTD facts in the fact table."

**Cabecera/línea y hechos asignados** (cómo se modela un comprobante como factura, pedido o remito). Las dos páginas se leyeron enteras.
- <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/header-line-fact-table/>: "With header/line schemas (also known as parent/child schemas), all the header-level dimension foreign keys and degenerate dimensions should be included on the line-level fact table."
- <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/allocated-fact/>: "It is quite common in header/line transaction data to encounter facts of differing granularity, such as a header freight charge. You should strive to allocate the header facts down to the line level based on rules provided by the business, so the allocated facts can be sliced and rolled up by all the dimensions."
- <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/degenerate-dimension/>: "when an invoice has multiple line items, the line item fact rows inherit all the descriptive dimension foreign keys of the invoice, and the invoice is left with no unique content. But the invoice number remains a valid dimension key for fact tables at the line item level. [...] Degenerate dimensions are most common with transaction and accumulating snapshot fact tables."

**Profit and Loss Fact Tables Using Allocations**: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/profit-loss-fact-table/> (leída entera)
> "However, these fact tables are difficult to build because the cost components must be allocated from their original sources to the fact table's grain. This allocation step is often a major ETL subsystem and is a politically charged step that requires high-level executive support. For these reasons, profit and loss fact tables are typically not tackled during the early implementation phases of a DW/BI program."

**Consolidated Fact Tables** (por ejemplo, real contra presupuesto): <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/consolidated-fact-table/> (leída entera)
> "It is often convenient to combine facts from multiple processes together into a single consolidated fact table if they can be expressed at the same grain. For example, sales actuals can be consolidated with sales forecasts in a single fact table to make the task of analyzing actuals versus forecasts simple and fast, as compared to assembling a drill-across application using separate fact tables. Consolidated fact tables add burden to the ETL processing, but ease the analytic burden on the BI applications."

## 2. Dimensiones conformadas, bus, matriz y *drill across*

**Conformed Dimensions**: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/conformed-dimension/> (leída entera)
> "Dimension tables conform when attributes in separate dimension tables have the same column names and domain contents. Information from separate fact tables can be combined in a single report by using conformed dimension attributes that are associated with each fact table. [...] This is the essence of integration in an enterprise DW/BI system. Conformed dimensions, defined once in collaboration with the business's data governance representatives, are reused across fact tables; they deliver both analytic consistency and reduced future development costs because the wheel is not repeatedly re-created."

**Conformed Facts**: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/conformed-fact/> (leída entera)
> "If the separate fact definitions are consistent, the conformed facts should be identically named; but if they are incompatible, they should be differently named to alert the business users and BI applications."

**Shrunken Rollup Dimensions**: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/shrunken-rollup-dimension/> (leída entera)
> "Shrunken dimensions are conformed dimensions that are a subset of rows and /or columns of a base dimension. [...] They are also necessary for business processes that naturally capture data at a higher level of granularity, such as a forecast by month and brand (instead of the more atomic date and product associated with sales data)."

**Drilling Across**: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/drilling-across/> (leída entera)
> "Drilling across simply means making separate queries against two or more fact tables where the row headers of each query consist of identical conformed attributes. The answer sets from the two queries are aligned by performing a sort-merge operation on the common dimension attribute row headers. BI tool vendors refer to this functionality by various names, including stitch and multipass query."

**Value Chain**: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/value-chain/> (leída entera)
> "A value chain identifies the natural flow of an organization's primary business processes. For example, a retailer's value chain may consist of purchasing to warehousing to retail sales. A general ledger value chain may consist of budgeting to commitments to payments. Operational source systems typically produce transactions or snapshots at each step of the value chain. Because each process produces unique metrics at unique time intervals with unique granularity and dimensionality, each process typically spawns at least one atomic fact table."

**Enterprise Data Warehouse Bus Architecture**: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/enterprise-data-warehouse-bus-architecture/> (leída entera)
> "The enterprise data warehouse bus architecture provides an incremental approach to building the enterprise DW/BI system. This architecture decomposes the DW/BI planning process into manageable pieces by focusing on business processes, while delivering integration via standardized conformed dimensions that are reused across processes. [...] The bus architecture is technology and database platform independent; both relational and OLAP dimensional structures can participate."

**Enterprise Data Warehouse Bus Matrix**: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/enterprise-data-warehouse-bus-matrix/> (leída entera)
> "The enterprise data warehouse bus matrix is the essential tool for designing and communicating the enterprise data warehouse bus architecture. The rows of the matrix are business processes and the columns are dimensions. The shaded cells of the matrix indicate whether a dimension is associated with a given business process. [...] the bus matrix is used as input to prioritize DW/BI projects with business management as teams should implement one row of the matrix at a time."
> "The detailed implementation bus matrix is a more granular bus matrix where each business process row has been expanded to show specific fact tables or OLAP cubes. At this level of detail, the precise grain statement and list of facts can be documented."

## 3. SCD tipos 0 a 7, y datos que llegan tarde

Todas estas páginas se leyeron enteras. Los títulos son los de Kimball. La URL base es `https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/` más el *slug* que va entre paréntesis.

| Tipo (título literal) | Cita de una línea |
|---|---|
| Type 0: Retain Original (`type-0`) | "With slowly changing dimension type 0, the dimension attribute value never changes, so facts are always grouped by this original value." Agrega: "It also applies to most attributes in a date dimension." |
| Type 1: Overwrite (`type-1`) | "the old attribute value in the dimension row is overwritten with the new value; type 1 attributes always reflects the most recent assignment, and therefore this technique destroys history." |
| Type 2: Add New Row (`type-2`) | "Slowly changing dimension type 2 changes add a new row in the dimension with the updated attribute values." Agrega: "A minimum of three additional columns should be added [...]: 1) row effective date or date/time stamp; 2) row expiration date or date/time stamp; and 3) current row indicator." |
| Type 3: Add New Attribute (`type-3`) | "add a new attribute in the dimension to preserve the old attribute value; the new value overwrites the main attribute as in a type 1 change. This kind of type 3 change is sometimes called an alternate reality." |
| Type 4: Add Mini-Dimension (`type-4-mini-dimension`) | "Slowly changing dimension type 4 is used when a group of attributes in a dimension rapidly changes and is split off to a mini–dimension. This situation is sometimes called a rapidly changing monster dimension." |
| Type 5: Add Mini-Dimension and Type 1 Outrigger (`type-5`) | "Type 5 builds on the type 4 mini-dimension by also embedding a current type 1 reference to the mini-dimension in the base dimension." |
| Type 6: Add Type 1 Attributes to Type 2 Dimension (`type-6`) | "Type 6 builds on the type 2 technique by also embedding current type 1 versions of the same attributes in the dimension row so that fact rows can be filtered or grouped by either the type 2 attribute value in effect when the measurement occurred or the attribute's current value." |
| Type 7: Dual Type 1 and Type 2 Dimensions (`type-7`) | "Slowly changing dimension type 7 is the final hybrid technique used to support both as-was and as-is reporting. [...] Both the durable key and primary surrogate key of the dimension are placed in the fact table." |

**Natural, Durable, and Supernatural Keys** (`natural-durable-supernatural-key`, leída entera)
> "Natural keys created by operational source systems are subject to business rules outside the control of the DW/BI system. For instance, an employee number (natural key) may be changed if the employee resigns and then is rehired. [...] While multiple surrogate keys may be associated with an employee over time as their profile changes, the durable key never changes."

**Late Arriving Facts** (`late-arriving-fact`, leída entera)
> "A fact row is late arriving if the most current dimensional context for new fact rows does not match the incoming row. This happens when the fact row is delayed. In this case, the relevant dimensions must be searched to find the dimension keys that were effective when the late arriving measurement event occurred."

**Late Arriving Dimensions** (`late-arriving-dimension`, leída entera)
> "Sometimes the facts from an operational business process arrive minutes, hours, days, or weeks before the associated dimension context. [...] In these cases, special dimension rows are created with the unresolved natural keys as attributes. [...] When this dimensional context is eventually supplied, the placeholder dimension rows are updated with type 1 overwrites. Late arriving dimension data also occurs when retroactive changes are made to type 2 dimension attributes. In this case, a new row needs to be inserted in the dimension table, and then the associated fact rows must be restated."

## 4. La dimensión de fecha y los períodos fiscales

**Calendar Date Dimensions**: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/calendar-date-dimension/> (leída entera)
> "Calendar date dimensions are attached to virtually every fact table to allow navigation of the fact table through familiar dates, months, fiscal periods, and special days on the calendar. You would never want to compute Easter in SQL, but rather want to look it up in the calendar date dimension. The calendar date dimension typically has many attributes describing characteristics such as week number, month name, fiscal period, and national holiday indicator. [...] However, the date dimension table needs a special row to represent unknown or to-be-determined dates. If a smart date key is used, filtering and grouping should be based on the dimension table's attributes, not the smart key."

**Multiple Hierarchies in Dimensions**: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/multiple-hierarchies/> (leída entera)
> "For example, calendar date dimensions may have a day to week to fiscal period hierarchy, as well as a day to month to year hierarchy. [...] In all of these cases, the separate hierarchies can gracefully coexist in the same dimension table."

**Role-Playing Dimensions** (fechas de pedido, de envío, de factura…): <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/role-playing-dimension/> (leída entera)
> "For instance, a fact table can have several dates, each of which is represented by a foreign key to the date dimension. It is essential that each foreign key refers to a separate view of the date dimension so that the references are independent."

**Design Tip #51: Latest Thinking On Time Dimension Tables** (Ralph Kimball, febrero de 2004): <https://www.kimballgroup.com/2004/02/design-tip-51-latest-thinking-on-time-dimension-tables/> (leída entera)
> "Only a few of these attributes (such as month name and year) can be generated directly from an SQL date-time expression. Holidays, work days, fiscal periods, week numbers, last day of month flags, and other navigational attributes must be embedded in the calendar date dimension and all date navigation should be implemented in applications by using the dimensional attributes. The calendar date dimension has some very unusual properties. It is one of the only dimensions that is completely specified at the beginning of the data warehouse project. It also doesn't have a conventional source. The best way to generate the calendar date dimension is to spend an afternoon with a spreadsheet and build it by hand. Ten years worth of days is less than 4000 rows."

**Calendarios fiscales múltiples.** El Toolkit 3.ª ed. trae la subsección «Multiple Fiscal Accounting Calendars 208» (cap. 7) y, en el cap. 12, «Country-Specific Calendars as Outriggers 321». En el índice del libro figura «fiscal calendar, multiple, 208». **Hueco:** no pude leer el texto de esas secciones. Los accesos a O'Reilly y Packt devolvieron 403, así que solo tengo los títulos.

## 5. Varias monedas y varias unidades de medida

**Multiple Currency Facts**: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/multiple-currencies/> (leída entera)
> "Fact tables that record financial transactions in multiple currencies should contain a pair of columns for every financial fact in the row. One column contains the fact expressed in the true currency of the transaction, and the other contains the same fact expressed in a single standard currency that is used throughout the fact table. The standard currency value is created in an ETL process according to an approved business rule for currency conversion. This fact table also must have a currency dimension to identify the transaction's true currency."

**Multiple Units of Measure Facts**: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/multiple-units-of-measure/> (leída entera)
> "If the fact table contains a large number of facts, each of which must be expressed in all units of measure, a convenient technique is to store the facts once in the table at an agreed standard unit of measure, but also simultaneously store conversion factors between the standard measure and all the others. [...] The conversion factors must reside in the underlying fact table row to ensure the view calculation is simple and correct, while minimizing query complexity."

En el libro, «Multiple Currencies 182» y «Multiple Units of Measure 197» están en el cap. 6, y «Multiple Currencies Revisited 206» en el cap. 7 (índice de Wiley, abajo).

## 6. Lo que cubre el Toolkit, 3.ª ed., capítulo por capítulo

Fuente: índice oficial en PDF de Wiley, <https://media.wiley.com/product_data/excerpt/02/11185308/1118530802-34.pdf> (leído entero), y la página del producto, <https://www.wiley.com/en-us/The+Data+Warehouse+Toolkit%3A+The+Definitive+Guide+to+Dimensional+Modeling%2C+3rd+Edition-p-9781118530801> (Kimball y Ross, Wiley, 2013, 608 páginas). Los títulos de subsección se copian tal cual. El número es la página.

**Cap. 3, Retail Sales (69).** Four-Step Dimensional Design Process 70 (Step 1: Select the Business Process; Step 2: Declare the Grain; Step 3: Identify the Dimensions; Step 4: Identify the Facts) · Retail Case Study 72 · Dimension Table Details 79 (Date Dimension 79; Product Dimension 83; Store Dimension 87; Promotion Dimension 89; Other Retail Sales Dimensions 92; Degenerate Dimensions for Transaction Numbers 93) · Retail Schema in Action 94 · Retail Schema Extensibility 95 · Factless Fact Tables 97 · Dimension and Fact Table Keys 98 (Dimension Table Surrogate Keys 98; Dimension Natural and Durable Supernatural Keys 100; Degenerate Dimension Surrogate Keys 101; Date Dimension Smart Keys 101; Fact Table Surrogate Keys 102) · Resisting Normalization Urges 104 (Snowflake Schemas with Normalized Dimensions 104; Outriggers 106; Centipede Fact Tables with Too Many Dimensions 108).

**Cap. 4, Inventory (111).** Value Chain Introduction 111 · Inventory Models 112 (Inventory Periodic Snapshot 113; Inventory Transactions 116; Inventory Accumulating Snapshot 118) · Fact Table Types 119 (Transaction Fact Tables 120; Periodic Snapshot Fact Tables 120; Accumulating Snapshot Fact Tables 121; Complementary Fact Table Types 122) · Value Chain Integration 122 · Enterprise Data Warehouse Bus Architecture 123 (Understanding the Bus Architecture 124; Enterprise Data Warehouse Bus Matrix 125) · Conformed Dimensions 130 (Drilling Across Fact Tables 130; Identical Conformed Dimensions 131; Shrunken Rollup Conformed Dimension with Attribute Subset 132; Shrunken Conformed Dimension with Row Subset 132; Shrunken Conformed Dimensions on the Bus Matrix 134; Limited Conformity 135; Importance of Data Governance and Stewardship 135; Conformed Dimensions and the Agile Movement 137) · Conformed Facts 138.

**Cap. 5, Procurement (141).** Procurement Case Study 141 · Procurement Transactions and Bus Matrix 142 (Single Versus Multiple Transaction Fact Tables 143; Complementary Procurement Snapshot 147) · Slowly Changing Dimension Basics 147 (Type 0 a Type 4) · Hybrid Slowly Changing Dimension Techniques 159 (Type 5: Mini-Dimension and Type 1 Outrigger 160; Type 6 160; Type 7 162) · Slowly Changing Dimension Recap 164.

**Cap. 6, Order Management (167).** Order Management Bus Matrix 168 · Order Transactions 168 (Fact Normalization 169; Dimension Role Playing 170; Product Dimension Revisited 172; Customer Dimension 174; Deal Dimension 177; Degenerate Dimension for Order Number 178; Junk Dimensions 179; Header/Line Pattern to Avoid 181; Multiple Currencies 182; Transaction Facts at Different Granularity 184; Another Header/Line Pattern to Avoid 186) · Invoice Transactions 187 (Service Level Performance as Facts, Dimensions, or Both 188; Profit and Loss Facts 189; Audit Dimension 192) · Accumulating Snapshot for Order Fulfillment Pipeline 194 (Lag Calculations 196; Multiple Units of Measure 197; Beyond the Rearview Mirror 198).

**Cap. 7, Accounting (201).** Accounting Case Study and Bus Matrix 202 · General Ledger Data 203 (General Ledger Periodic Snapshot 203; Chart of Accounts 203; Period Close 204; Year-to-Date Facts 206; Multiple Currencies Revisited 206; General Ledger Journal Transactions 206; Multiple Fiscal Accounting Calendars 208; Drilling Down Through a Multilevel Hierarchy 209; Financial Statements 209) · Budgeting Process 210 · Dimension Attribute Hierarchies 214 (Fixed Depth Positional Hierarchies 214; Slightly Ragged Variable Depth Hierarchies 214; Ragged Variable Depth Hierarchies 215; Shared Ownership in a Ragged Hierarchy 219; Time Varying Ragged Hierarchies 220; Modifying Ragged Hierarchies 220; Alternative Ragged Hierarchy Modeling Approaches 221; Advantages of the Bridge Table Approach for Ragged Hierarchies 223) · Consolidated Fact Tables 224 · Role of OLAP and Packaged Analytic Solutions 226.

**Cap. 8, Customer Relationship Management (229).** Lo que interesa acá: Customer Data Integration Approaches 256 (Master Data Management Creating a Single Customer Dimension 256; Partial Conformity of Multiple Customer Dimensions 258; Avoiding Fact-to-Fact Table Joins 259) · Low Latency Reality Check 260.

**Cap. 9, Human Resources Management (263).** Employee Profile Tracking 263 (Precise Effective and Expiration Timespans 265; Dimension Change Reason Tracking 266; Profile Changes as Type 2 Attributes or Fact Events 267) · Headcount Periodic Snapshot 267 · Bus Matrix for HR Processes 268 · Packaged Analytic Solutions and Data Models 270 · Recursive Employee Hierarchies 271 (Change Tracking on Embedded Manager Key 272; Drilling Up and Down Management Hierarchies 273) · Multivalued Skill Keyword Attributes 274 · Survey Questionnaire Data 277.

**Otros capítulos con material para gestión.** Cap. 12: More Date and Time Considerations 321 (Country-Specific Calendars as Outriggers 321; Date and Time in Multiple Time Zones 323). Cap. 14: Dealing with Retroactive Changes 351. Cap. 16: Policy/Claim Consolidated Periodic Snapshot 395 y Common Dimensional Modeling Mistakes to Avoid 397. Cap. 19: ETL Subsystems and Techniques 443 (ver §8). Cap. 20: Develop Incremental ETL Processing 512 (Step 7: Dimension Table Incremental Processing 512; Step 8: Fact Table Incremental Processing 515) y Real-Time Implications 520.

**Huecos del punto 6:**
- No hay capítulo ni entrada de índice para cuentas por cobrar o por pagar (AR/AP) ni para horas trabajadas o *time cards*. Busqué en el índice de Wiley, <https://media.wiley.com/product_data/excerpt/02/11185308/1118530802-33.pdf> (leído entero), y no aparecen «payable», «receivable» ni «time card». Las entradas relacionadas que sí están son «G/L (general ledger), 203–210», «budgeting process, 210–213», «period close, 204–206», «fiscal calendar, multiple, 208», «currency, multiple, 182–184» y «packaged analytic solutions, 270–271».
- Del cuerpo de los capítulos 4 a 7 y 9 solo tengo los títulos. No leí el texto (O'Reilly y Packt dieron 403).

## 7. Inmon: definición, ODS y Corporate Information Factory

**La definición, en un texto de Inmon.** W. H. Inmon, «What Is a Data Warehouse?», *Prism Tech Topic*, vol. 1, n.º 1, © 1995 Prism Solutions. Copia en archive.org: <https://web.archive.org/web/20010424175209/http://www.cait.wustl.edu:80/cait/papers/prism/vol1_no1/> (página principal leída entera)
> "A data warehouse is a: subject-oriented, integrated, time-variant, nonvolatile collection of data in support of management's decision making process"
> "The data entering the data warehouse comes from the operational environment in almost every case. The data warehouse is always a physically separate store of data transformed from the application data found in the operational environment."

Las subpáginas del mismo texto, también en archive.org (`.../vol1_no1/integration/home.html`, `.../time_variance/home.html`, `.../nonvolatile/home.html`, `.../subject/home.html`), las leí enteras, menos la de *nonvolatile*, que corté en la mitad:
- Integración: "Easily the most important aspect of the data warehouse environment is that data found within the data warehouse is integrated. ALWAYS. WITH NO EXCEPTIONS. [...] The integration shows up in many different ways - in consistent naming conventions, in consistent measurement of variables, in consistent encoding structures, in consistent physical attributes of data, and so forth."
- Variación en el tiempo: "All data in the data warehouse is accurate as of some moment in time. [...] In the operational environment data is accurate as of the moment of access." Y también: "data warehouse data represents data over a long time horizon - from five to ten years. The time horizon represented for the operational environment is much shorter - from the current values of today up to sixty to ninety days." Y: "Data warehouse data is, for all practical purposes, a long series of snapshots."
- No volatilidad: "There are only two kinds of operations that occur in the data warehouse - the initial loading of data, and the access of data. There is no update of data (in the general sense of update) in the data warehouse as a normal part of processing."
- Orientación a temas: "The operational world is designed around applications and functions such as loans, savings, bank card and trust for a financial institution. The data warehouse world is organized around major subjects such as customer, vendor, product and activity."

**Datos primitivos y derivados, y la CIF.** Inmon, *Building the Data Warehouse*, 4.ª ed. (Wiley, 2005), cap. 1. Es el extracto oficial de Wiley: <https://media.wiley.com/product_data/excerpt/45/07645994/0764599445-18.pdf> (leído entero)
> "There are fundamentally two kinds of data at the heart of an "architected" environment — primitive data and derived data."
> "It is a wonder that the information processing community ever thought that both primitive and derived data would fit and peacefully coexist in a single database. In fact, primitive data and derived data are so different that they do not reside in the same database or even the same environment."
> "There are four levels of data in the architected environment — the operational level, the atomic (or the data warehouse) level, the departmental (or the data mart) level, and the individual level. These different levels of data are the basis of a larger architecture called the corporate information factory (CIF). The operational level of data holds application-oriented primitive data only and primarily serves the high-performance transaction-processing community. The data-warehouse level of data holds integrated, historical primitive data that cannot be updated."

El índice del mismo libro, <https://media.wiley.com/product_data/excerpt/45/07645994/0764599445.pdf> (leído entero), trae el capítulo «Chapter 16 The Data Warehouse and the ODS 429». Sus subsecciones son Complementary Structures; Updates in the ODS; Historical Data and the ODS; Profile Records; Different Classes of ODS; Database Design — A Hybrid Approach; Transaction Integrity in the ODS; Time Slicing the ODS Day; Multiple ODS; ODS and the Web Environment; An Example of an ODS.

**El ODS en un texto de Inmon.** Bill Inmon, columna en *Information Management* (antes *DM Review*), enero de 2000, URL original `information-management.com/issues/20000101/1749-1.html`. Copia en archive.org: <https://web.archive.org/web/2005/http://www.information-management.com/issues/20000101/1749-1.html> (leída entera)
> "The operational data store (ODS) is the original stealth structure."
> "From the beginning, it was predicted that there would be different classes of ODSs based on how fast data was loaded into the ODS and the source of the load. It was predicted that there would be four classes of ODSs:"
> "Class I. Transactions were moved to the ODS in an immediate manner from applications in a range of one to two seconds from the moment the transaction was executed in the operational environment until the transaction arrived at the ODS."
> "Class II. Activities that occurred in the operational environment were stored and forwarded to the ODS every four hours or so."
> "Class III. The time lag between execution in the operational environment and reflection in the ODS is overnight."
> "Class IV. A Class IV ODS is one that is fed from the data warehouse from analysis created by the DSS analyst in the data warehouse environment and condensed down to a point where the results of the analytical processing fit comfortably in the ODS."
> "The first type of an ODS built [...] is an ODS where whole tables are copied on a wholesale basis from the operational environment. While this is a form of an ODS, it is a very weak form. [...] There is absolutely no integration of data in this form of an ODS. [...] If anything, it is a Class 0 ODS."
> "As a rule, the easier the ODS is to build, the shorter the life span. The real worth of the ODS appears in the ability to hold integrated data."

**La definición «oficial» del ODS.** Solo la vi en fuentes secundarias. El blog dwh-faq (<https://dwh-faq.blogspot.com/2013/09/the-operational-data-store-ods.html>, leído vía WebFetch, que resume) atribuye a Inmon e Imhoff, *Building the Operational Data Store* (1996), la frase: "subject-oriented, integrated, volatile, current valued data store, containing only corporate detailed data". El glosario de VITA (Virginia) dice algo parecido (eso lo vi solo en el snippet del buscador). **Hueco:** no conseguí el texto del libro de 1996 ni de la 2.ª ed. de 1999 para confirmar la redacción literal.

**La CIF según Kimball y Ross.** Toolkit 3.ª ed., cap. 1, extracto oficial de Wiley: <https://media.wiley.com/product_data/excerpt/02/11185308/1118530802-32.pdf> (leído entero)
> "With the CIF, data is extracted from the operational source systems and processed through an ETL system sometimes referred to as data acquisition. The atomic data that results from this processing lands in a 3NF database; this normalized, atomic repository is referred to as the Enterprise Data Warehouse (EDW) within the CIF architecture. Although the Kimball architecture enables optional normalization to support ETL processing, the normalized EDW is a mandatory construct in the CIF."
> "NOTE The process of normalization does not technically speak to integration. Normalization simply creates physical tables that implement many-to-one relationships. Integration, on the other hand, requires that inconsistencies arising from separate sources be resolved."

## 8. Dimensión de auditoría, filtros de calidad, conciliación y subsistemas de ETL

**Audit Dimension**: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/audit-dimension/> (leída entera)
> "When a fact table row is created in the ETL back room, it is helpful to create an audit dimension containing the ETL processing metadata known at the time. A simple audit dimension row could contain one or more basic indicators of data quality, perhaps derived from examining an error event schema that records data quality violations encountered while processing the data. Other useful audit dimension attributes could include environment variables describing the versions of ETL code used to create the fact rows or the ETL process execution time stamps."

**Error Event Schemas**: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/error-event-schema/> (leída entera)
> "Managing data quality in a data warehouse requires a comprehensive system of data quality screens or filters that test the data as it flows from the source systems to the BI platform. When a data quality screen detects an error, this event is recorded in a special dimensional schema that is available only in the ETL back room. This schema consists of an error event fact table whose grain is the individual error event and an associated error event detail fact table whose grain is each column in each table that participates in an error event."

**Kimball, «An Architecture for Data Quality»** (*white paper*, © 2007): <https://www.kimballgroup.com/2007/10/white-paper-an-architecture-for-data-quality/>, PDF en <http://www.kimballgroup.com/wp-content/uploads/2007/10/An-Architecture-for-Data-Quality1.pdf> (leí las páginas 1 a 9 y 13 a 14 de unas 20)
> "The heart of the data warehouse quality architecture is a set of quality screens that act as diagnostic filters in the back room ETL data flow pipelines. A quality screen is simply a test, implemented at any point in the ETL or data migration processes. If the test is successful, nothing happens and the screen has no side effects. But if the test fails, then every screen has two simple responsibilities: Drop an error event record into the error event schema, and Choose to halt the process, send the offending data into suspension, or merely tag the data."
> "Column screens test the data within a single column."
> "Structure screens test the relationship of data across columns. [...] Structure screens include testing foreign key/primary key relationships between fields in two tables"
> "Business rule screens implement more complex tests that do not fit the simpler column or structure screen categories. [...] Business rule screens also include aggregate threshold data quality checks"
> "Relatively few data errors can be fixed in the data warehouse."
> "The audit dimension is a normal dimension that is assembled in the back room by the ETL process for each fact table."

En el ejemplo de la figura 2, la dimensión de auditoría tiene estos atributos: overall quality, completeness, validation, out-of-bounds, screens failed, record modified, extract/clean/conform time stamp, ETL master version, allocation version, currency version, error event group.

**Los 34 subsistemas de ETL.** Bob Becker, «Subsystems of ETL Revisited», Kimball Group, octubre de 2007: <https://www.kimballgroup.com/2007/10/subsystems-of-etl-revisited/> (leída entera). Antes de la lista dice: "the "ETL" process really has four major components: Extracting, Cleaning and Conforming, Delivering and Managing." Copio los subsistemas que pidió la consigna:
- "Data Profiling (subsystem 1) – Explores a data source to determine its fit for inclusion as a source and the associated cleaning and conforming requirements."
- "Change Data Capture (subsystem 2) – Isolates the changes that occurred in the source system to reduce the ETL processing burden."
- "Extract System (subsystem 3) – Extracts and moves source data into the data warehouse environment for further processing."
- "Data Cleansing System (subsystem 4) – Implements data quality processes to catch quality violations."
- "Error Event Tracking (subsystem 5) – Captures all error events that are vital inputs to data quality improvement."
- "Audit Dimension Creation (subsystem 6) – Attaches metadata to each fact table as a dimension. This metadata is available to BI applications for visibility into data quality."
- "Deduplication (subsystem 7) – Eliminates redundant members of core dimensions, such as customers or products."
- "Data Conformance (subsystem 8 ) – Enforces common dimension attributes across conformed master dimensions and common metrics across related fact tables."
- "Slowly Changing Dimension (SCD) Manager (subsystem 9) – Implements logic for slowly changing dimension attributes."
- "Hierarchy Manager (subsystem 11) – Delivers multiple, simultaneous, embedded hierarchical structures in a dimension."
- "Fact Table Builders (subsystem 13) – Construct the three primary types of fact tables: transaction grain, periodic snapshot and accumulating snapshot."
- "Surrogate Key Pipeline (subsystem 14) – Replaces operational natural keys in the incoming fact table record with the appropriate dimension surrogate keys."
- "Late Arriving Data Handler (subsystem 16) – Applies special modifications to the standard processing procedures to deal with late-arriving fact and dimension data."
- "Lineage and Dependency (subsystem 29) – Identifies the source of a data element and all intermediate locations and transformations for that data element [...]"

Los nombres cambian un poco en el Toolkit 3.ª ed. (índice de Wiley): Subsystem 5 se llama «Error Event Schema», Subsystem 6 «Audit Dimension Assembler», Subsystem 8 «Conforming System» y Subsystem 2 «Change Data Capture System». El mismo artículo dice además: "the data warehouse is expected to provide an accurate picture of the data as it was captured by the organization's production systems."

**Hueco: conciliar el almacén con el sistema fuente** (control totals, *tie-out*, cuadre con el mayor). No encontré un texto primario de Kimball que lo trate con ese nombre. Lo más cercano es lo de arriba: la cita de Becker sobre la «accurate picture», los filtros de umbral agregado y la dimensión de auditoría. También busqué en el sitio de Kimball «reconcile» y «balancing» y no apareció ningún artículo sobre el tema. Probablemente esté en el cap. 7 del Toolkit (Period Close 204) o en el *ETL Toolkit* (2004), pero no lo pude leer.

## 9. La mirada contraria: no separar el almacén del ERP (HTAP)

**Fuente académica neutral.** Zhang, Li, Zhang, Zhang y Feng, «HTAP Databases: A Survey», arXiv:2404.15670v1, abril de 2024: <https://arxiv.org/pdf/2404.15670> (el PDF de arXiv tiene 4 páginas y lo leí entero)
> "Compared with the traditional data processing pipeline that processes transactions and analytical queries separately, HTAP architecture enables a unified system that not only can handle online transactional processing (OLTP) efficiently, but also can perform online analytical processing (OLAP) concurrently [35]. Such an architecture aims to eliminate the need for an explicit Extract-Transform-Load (ETL) process, thereby enabling real-time data analytics on transaction data."
> "Nevertheless, HTAP databases must strike a trade-off between performance isolation and data freshness when handling the mixed workloads of OLTP and OLAP. [...] Consequently, HTAP databases cannot guarantee the metrics of query throughput and data freshness simultaneously, albeit with a unified architecture."
> "The year 2014 is the time when the HTAP term was formally defined by a Gartner report [98]."
> "Year 2010-2014: Standalone Column-based HTAP databases. [...] the applications they targeted were mainly analytical applications with read-heavy transactional workloads, such as the ERP applications [34]."
> "We do not consider the loosely-coupled HTAP architectures [93] as those architectures employ multiple databases to form an HTAP solution that entails a costly ETL process."

La misma línea aparece en otro artículo: Song et al., «A survey on hybrid transactional and analytical processing», *The VLDB Journal* (2024), DOI 10.1007/s00778-024-00858-9. Ese lo vi solo en el snippet.

**El argumento original de que OLTP y OLAP compartan una base.** Plattner, «A common database approach for OLTP and OLAP using an in-memory column database», SIGMOD 2009, DOI 10.1145/1559845.1559846. **Hueco:** no conseguí el texto del artículo (las copias de typeset/scispace vinieron vacías). Solo pude ver las diapositivas del autor en HPI (<https://hpi.de/oldsite/fileadmin/user_upload/fachgebiete/plattner/teaching/inmemorydataprocessing/2010/ShareOneDB.pdf>, leídas enteras), cuyo título es «Enterprise Applications – OLTP and OLAP – Share One Database». Dicen: "Modern ERP systems are challenged by a mixed workload including OLAP-style queries, e.g., Dunning-run, Available-to-promise, and Real-time operational reporting". Ojo: el autor es parte interesada, así que conviene citarlo solo como origen del argumento.

**La respuesta de Kimball (la postura a favor de separar).**
- Joy Mundy, Design Tip #179, «Key Tenets of the Kimball Method» (noviembre de 2015): <https://www.kimballgroup.com/2015/11/design-tip-179-key-tenets-of-kimball-method/> (leída entera)
  > "Don't skip the relational data warehouse. Designing and populating an enterprise conformed data warehouse is hard. Everyone would like to skip this step. Throughout the 23+ years of my career in data warehousing, I have observed any number of technological attempts to simplify the process, from building the BI layer directly on the transaction system, to so-called virtual data warehouses, back full circle to the current flavor of visualization tool build scripts. [...] Unless you completely control all of your source data, you should leave ETL to the ETL tool, leave data storage and management to a relational database engine, and let the BI tools shine at what they do best"
  > "Supporting different or deeper hierarchies than are managed in the source systems, such as marketing versus manufacturing views of the product dimension."
- Toolkit 3.ª ed., cap. 1 (extracto de Wiley, leído entero):
  > "Unfortunately, we still encounter supposed DW/BI systems that are mere copies of the operational systems of record stored on a separate hardware platform. Although these environments may address the need to isolate the operational and analytical environments for performance reasons, they do nothing to address the other inherent differences between the two types of systems."
  > "Source systems maintain little historical data; a good data warehouse can relieve the source systems of much of the responsibility for representing the past. In many cases, the source systems are special purpose applications without any commitment to sharing common data such as product, customer, geography, or calendar with other operational systems in the organization. Of course, a broadly adopted cross-application enterprise resource planning (ERP) system or operational master data management system could help address these shortcomings."
  > "operational systems typically do not maintain history, but rather update data to reflect the most current state."
- Inmon, en el cap. 1 citado en §7, dice que los datos primitivos y los derivados "do not reside in the same database or even the same environment".

**Lectura mía, no de las fuentes.** El argumento HTAP ataca la frescura del dato y el costo del ETL. Kimball defiende la separación por otras razones: historia (SCD), integración entre sistemas (dimensiones conformadas) y atributos que el sistema fuente no tiene. Una sola base sobre un único ERP resuelve la latencia, pero no esas otras tres cosas. Ninguna fuente lo dice con estas palabras. Kimball mismo admite que un ERP único reduce el problema de integración ("could help address these shortcomings").

---

## Resumen de huecos

1. **Cuerpo de los capítulos 4 a 7 y 9 del Toolkit** (GL, cierre de período, calendarios fiscales múltiples, presupuesto, *headcount*): solo tengo los títulos de subsección del índice oficial. O'Reilly y Packt dieron 403.
2. **AR/AP y horas trabajadas**: el Toolkit no tiene capítulo ni entrada de índice para eso. Habría que buscar otra fuente.
3. **Conciliación con la fuente** (control totals, cuadre contra el mayor): no hay texto primario de Kimball que lo trate con nombre propio.
4. **Definición literal del ODS** en *Building the Operational Data Store* (Inmon e Imhoff): la vi solo citada por terceros. Lo que sí tengo de primera mano es la columna de Inmon de 2000 sobre las clases de ODS.
5. **Plattner (SIGMOD 2009)**: no conseguí el texto del artículo, solo las diapositivas del autor.
6. **El informe de Gartner de 2014 que acuñó «HTAP»**: es de pago. Solo lo tengo citado por el *survey*.
