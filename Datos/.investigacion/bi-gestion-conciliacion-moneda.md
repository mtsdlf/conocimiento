# Investigación: BI sobre el sistema de gestión (ERP): conciliar, combinar fuentes, multiempresa y moneda, y la nota de Argentina

Fecha: 2026-11-27. Material de trabajo para notas en borrador; no es una nota.

**Cómo leer las marcas de lectura.**
- *Texto completo (curl)*: bajé la página o el PDF entero con curl, lo pasé a texto y leí las líneas citadas en ese texto. Las citas son copia literal del texto extraído; solo pueden diferir en espacios o saltos de línea.
- *Extracción*: la herramienta de lectura bajó la página y me devolvió frases. Esa herramienta corta las citas a unos 125 caracteres, así que solo uso lo que vino entre comillas.
- *Snippet*: solo vi el resultado de un buscador. No se cita como fuente firme.

Las citas van en su idioma original. Donde no vi la frase literal, lo digo y no la presento como cita.

**Fuentes primarias usadas.** Las normas de la IFRS Foundation en sus ediciones HTML públicas (edición 2026, `ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/…`). Para Argentina: el Boletín Oficial, argentina.gob.ar (Infoleg), BCRA y CPCECABA. CPCECABA es el consejo profesional que adopta las resoluciones de la FACPCE en CABA y transcribe su texto. Los PDF de la propia FACPCE (`facpce.org.ar/web2014/pdf/RESJG539-18.pdf` y `MetodologiaIndices.pdf`) devuelven 404 desde noviembre de 2026, así que usé la adopción de CPCECABA, que reproduce la Segunda Parte de la JG 539/18.

---

## 1. NIC 21 (IAS 21): moneda funcional, moneda de presentación y conversión

URL: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias21.html. Texto completo (curl).

**Ojo con la edición.** La edición 2026 ya trae marcada la enmienda *Translation to a Hyperinflationary Presentation Currency* (noviembre de 2025), y el texto extraído mezcla lo agregado con lo borrado en los encabezados de los párrafos 39 y 42. Los incisos (a) a (c) del 39 no cambian. Según el párrafo 60P, la enmienda rige así: «An entity shall apply those amendments for annual reporting periods beginning on or after 1 January 2027. Earlier application of the amendments is permitted.» (Ese texto está en la nota de transición que lista los párrafos 39, 42, 44, 47 y 55 como modificados.)

### Definiciones (párrafo 8)
- «Functional currency is the currency of the primary economic environment in which the entity operates.»
- «Presentation currency is the currency in which the financial statements are presented.»
- «Closing rate is the spot exchange rate at the end of the reporting period.»
- «Exchange difference is the difference resulting from translating a given number of units of one currency into another currency at different exchange rates.»
- «Foreign operation is an entity that is a subsidiary, associate, joint arrangement or branch of a reporting entity, the activities of which are based or conducted in a country or currency other than those of the reporting entity.»

### Cómo se elige la moneda funcional (párrafo 9)
- «The primary economic environment in which an entity operates is normally the one in which it primarily generates and expends cash.»
- Factores: «(a) the currency: (i) that mainly influences sales prices for goods and services (this will often be the currency in which sales prices for its goods and services are denominated and settled); and (ii) of the country whose competitive forces and regulations mainly determine the sales prices of its goods and services. (b) the currency that mainly influences labour, material and other costs of providing goods or services».
- Cambio de moneda funcional (párrafo 37): «The effect of a change in functional currency is accounted for prospectively.»

### Transacciones en moneda extranjera (párrafos 21 a 23)
- §21: «A foreign currency transaction shall be recorded, on initial recognition in the functional currency, by applying to the foreign currency amount the spot exchange rate between the functional currency and the foreign currency at the date of the transaction».
- §22 (tipo promedio como aproximación): «For practical reasons, a rate that approximates the actual rate at the date of the transaction is often used, for example, an average rate for a week or a month might be used for all transactions in each foreign currency occurring during that period. However, if exchange rates fluctuate significantly, the use of the average rate for a period is inappropriate.»
- §23: «(a) foreign currency monetary items shall be translated using the closing rate; (b) non‑monetary items that are measured in terms of historical cost in a foreign currency shall be translated using the exchange rate at the date of the transaction».
- **Cuando hay varios tipos de cambio (§26).** Sirve para Argentina con tipos múltiples: «When several exchange rates are available, the rate used is that at which the future cash flows represented by the transaction or balance could have been settled if those cash flows had occurred at the measurement date.»

### Conversión a una moneda de presentación distinta (párrafos 38 a 41)
- §38: «An entity may present its financial statements in any currency (or currencies). If the presentation currency differs from the entity's functional currency, it translates its results and financial position into the presentation currency. For example, when a group contains individual entities with different functional currencies, the results and financial position of each entity are expressed in a common currency so that consolidated financial statements may be presented.»
- §39, incisos (sin cambios por la enmienda), para monedas funcionales no hiperinflacionarias:
  - «(a) assets and liabilities for each statement of financial position presented (ie including comparatives …) shall be translated at the closing rate at the date of that statement of financial position;»
  - «(b) income and expenses for each statement presenting profit or loss and other comprehensive income (ie including comparatives) shall be translated at exchange rates at the dates of the transactions; and»
  - «(c) all resulting exchange differences shall be recognised in other comprehensive income.»
- §40 (tipo promedio): «For practical reasons, a rate that approximates the exchange rates at the dates of the transactions, … for example an average rate for the period, is often used to translate income and expense items. However, if exchange rates fluctuate significantly, the use of the average rate for a period is inappropriate.»
- §41, de dónde sale la diferencia y por qué no va a resultados: «(a) translating income and expenses at the exchange rates at the dates of the transactions … and assets and liabilities at the closing rate. (b) translating the opening net assets at a closing rate that differs from the previous closing rate. These exchange differences are not recognised in profit or loss because the changes in exchange rates have little or no direct effect on the present and future cash flows from operations. The cumulative amount of the exchange differences is presented in a separate component of equity until disposal of the foreign operation.»

### Moneda funcional hiperinflacionaria (párrafos 42 y 43)
- §42(a): «all amounts (ie assets, liabilities, equity items, income and expenses, including comparatives) shall be translated at the closing rate at the date of the most recent statement of financial position».
- §42(b): «when amounts are translated into the currency of a non‑hyperinflationary economy, comparative amounts shall be those that were presented as current year amounts in the relevant prior year financial statements (ie not adjusted for subsequent changes in the price level or subsequent changes in exchange rates).»
- §43, primero se reexpresa y después se convierte: «When an entity's functional currency is the currency of a hyperinflationary economy, … the entity shall restate its financial statements in accordance with IAS 29 before applying the translation method set out in paragraph 42».
- §41A (nuevo, rige desde 2027), moneda funcional estable con presentación hiperinflacionaria (el caso inverso): «the results and financial position of the entity shall be translated into the presentation currency by translating all amounts (ie assets, liabilities, equity items, income and expenses, including comparatives) at the closing rate at the date of the most recent statement of financial position.»

### Consolidar operaciones en el extranjero (párrafos 45 y 46)
- §45: «The incorporation of the results and financial position of a foreign operation with those of the reporting entity follows normal consolidation procedures, … such as the elimination of intragroup balances and intragroup transactions of a subsidiary (see IFRS 10 Consolidated Financial Statements). However, an intragroup monetary asset (or liability), whether short‑term or long‑term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements.» **Para la nota multiempresa.** Este es el motivo por el que las cuentas intercompañía en distinta moneda no se cancelan a cero solas.
- §46: si la subsidiaria cierra en otra fecha, NIIF 10 admite usar esa fecha «provided that the difference is no greater than three months».

---

## 2. NIC 29 (IAS 29): economías hiperinflacionarias

URL: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias29.html. Texto completo (curl).

- **Sin umbral absoluto (§3):** «This Standard does not establish an absolute rate at which hyperinflation is deemed to arise. It is a matter of judgement when restatement of financial statements in accordance with this Standard becomes necessary.»
- **Indicadores (§3 (a) a (e)):**
  - «(a) the general population prefers to keep its wealth in non‑monetary assets or in a relatively stable foreign currency. Amounts of local currency held are immediately invested to maintain purchasing power;»
  - «(b) the general population regards monetary amounts not in terms of the local currency but in terms of a relatively stable foreign currency. Prices may be quoted in that currency;»
  - «(c) sales and purchases on credit take place at prices that compensate for the expected loss of purchasing power during the credit period, even if the period is short;»
  - «(d) interest rates, wages and prices are linked to a price index; and»
  - «(e) the cumulative inflation rate over three years is approaching, or exceeds, 100%.»
- **Una sola señal no alcanza.** En la decisión de agenda del IFRIC de junio de 2025, reproducida al pie del §3, los interesados «do not conclude that an economy becomes hyperinflationary based solely on one of the indicators listed in paragraph 3 of IAS 29».
- **Desde cuándo se aplica (§4):** «this Standard applies to the financial statements of any entity from the beginning of the reporting period in which it identifies the existence of hyperinflation in the country in whose currency it reports.»
- **Por qué (§7):** «In a hyperinflationary economy, financial statements, whether they are based on a historical cost approach or a current cost approach, are useful only if they are expressed in terms of the measuring unit current at the end of the reporting period. … Presentation of the information required by this Standard as a supplement to unrestated financial statements is not permitted. Furthermore, separate presentation of the financial statements before restatement is discouraged.» **Para la nota.** Esto choca con un BI que muestre cifras históricas sin reexpresar como si fueran el balance.
- **La regla (§8):** «The financial statements of an entity whose functional currency is the currency of a hyperinflationary economy, … shall be stated in terms of the measuring unit current at the end of the reporting period. … The corresponding figures … for the previous period … and any information in respect of earlier periods shall also be stated in terms of the measuring unit current at the end of the reporting period.»
- **Resultado por posición monetaria (§9):** «The gain or loss on the net monetary position … shall be included in profit or loss … and separately disclosed.»
- **Consistencia antes que precisión (§10):** «The consistent application of these procedures and judgements from period to period is more important than the precise accuracy of the resulting amounts included in the restated financial statements.»
- **Monetarias y no monetarias (§11, 12 y 15):**
  - §11: «Statement of financial position amounts not already expressed in terms of the measuring unit current at the end of the reporting period are restated by applying a general price index.»
  - §12: «Monetary items are not restated because they are already expressed in terms of the monetary unit current at the end of the reporting period.»
  - §15: «The restated cost, or cost less depreciation, of each item is determined by applying to its historical cost and accumulated depreciation the change in a general price index from the date of acquisition to the end of the reporting period.»
- **Comparativos (§34):** «Corresponding figures for the previous reporting period … are restated by applying a general price index so that the comparative financial statements are presented in terms of the measuring unit current at the end of the reporting period.»
- **Grupo (§35 y 36):** «The financial statements of any such subsidiary need to be restated by applying a general price index of the country in whose currency it reports before they are included in the consolidated financial statements issued by its parent. Where such a subsidiary is a foreign subsidiary, its restated financial statements are translated at closing rates.» Y el §36: «If financial statements with different ends of the reporting periods are consolidated, all items, whether non‑monetary or monetary, need to be restated into the measuring unit current at the date of the consolidated financial statements.»
- **Índice (§37):** «The restatement of financial statements in accordance with this Standard requires the use of a general price index that reflects changes in general purchasing power. It is preferable that all entities that report in the currency of the same economy use the same index.»
- **Al salir de la hiperinflación (§38):** «it shall treat the amounts expressed in the measuring unit current at the end of the previous reporting period as the basis for the carrying amounts in its subsequent financial statements.»

---

## 3. Argentina: ajuste por inflación, índice, prohibición y vuelta, tipos de cambio

### 3.1 RT 6 «Estados contables en moneda homogénea» (texto ordenado de CPCECABA)
URL: https://consejo.org.ar/storage/attachments/01_RT%206.pdf-R1cZ0V8jtI.pdf. Texto completo (curl + pdftotext). Es primaria a nivel de consejo profesional: el texto ordenado que adoptó CPCECABA, con las modificaciones de las RT 19, 27 y 39 y de la JG 539/18.
- Portada: «La resolución de J.G. FACPCE N° 539/2018, adoptada por la resolución C.D. Nº 107/2018 del CPCECABA, estableció la aplicación obligatoria de la RT N° 6 para la preparación de estados contables correspondientes a ejercicios anuales o intermedios cerrados a partir del 1º de julio de 2018 (inclusive).»
- Alcance (nota 2): «Las presentes normas son aplicables a todos los estados contables para ser presentados a terceros, excepto los que emitan aquellos entes que, en forma obligatoria u opcional, apliquen las Normas de la segunda parte de la Resolución Técnica Nº 26 (Normas contables profesionales: Adopción de las NIIF del IASB).» (Esos entes aplican la NIC 29 directamente.)
- **Pasos (IV.B.2):**
  - «b) Las partidas expresadas en moneda de cierre no deben reexpresarse.»
  - «c) Las partidas expresadas en moneda de fecha anterior al cierre, deberán reexpresarse en moneda de cierre del siguiente modo: i) Eliminación de los ajustes parciales contabilizados para reflejar el efecto de la inflación, a fin de evitar su duplicación. ii) Determinación del momento o período de origen de las partidas (anticuación) iii) Cálculo de los coeficientes de reexpresión aplicables. iv) Aplicación de los coeficientes de reexpresión a los importes de las partidas anticuadas, a efectos de reexpresarlas en moneda de cierre.»
- **Anticuación (IV.B.4).** Clave para un modelo de datos, porque obliga a guardar la fecha de origen: «La anticuación del saldo de una cuenta consiste en su descomposición en partidas o grupos de partidas, según los distintos momentos o períodos de origen de estas, a efectos de reexpresarlas en moneda de cierre. Es razonable agrupar las partidas por mes de origen a efectos de proceder a su reexpresión. En tanto no se generen distorsiones significativas, es aceptable descomponer el saldo de la cuenta en períodos mayores de un mes.»
- **Índice (IV.B.5):** «La serie de índices que se utilizará es la resultante de combinar el Índice de Precios al Consumidor Nacional (IPC) publicado por el INDEC (mes base: diciembre de 2016) con el IPIM publicado por la FACPCE, tal como lo establece la resolución JGN°517/16. La serie completa del índice, según la definición del párrafo anterior, será elaborada y publicada mensualmente por esta Federación una vez que tome conocimiento público la variación mensual del IPC Nacional por el INDEC.»
- **Coeficiente (IV.B.6):** «Los coeficientes aplicables a las distintas partidas resultan de dividir el valor del índice correspondiente a la fecha de cierre por el valor del índice correspondiente a la fecha o período de origen de la partida.» Y también: «las partidas del mes de cierre no se reexpresarán, ya que el coeficiente aplicable será la unidad.»
- **RECPAM (IV.B.8 y IV.B.9):** «El resultado por exposición al cambio en el poder adquisitivo de la moneda, comprenderá el efecto de ese cambio sobre las partidas monetarias (o expuestas al cambio en el poder adquisitivo de la moneda).» Además, la partida se llama «“Resultados financieros y por tenencia (incluyendo resultados por exposición al cambio en el poder adquisitivo de la moneda)”».
- **Interrupción y reanudación (IV.B.13):** «Si en un período posterior fuera necesario reanudar el ajuste para reflejar el efecto de los cambios ocurridos en el poder adquisitivo de la moneda, los cambios a considerar serán los habidos desde el momento en que se interrumpió el ajuste.»

### 3.2 RT 39 (2013): el umbral del 100 % en tres años
URL: https://www.argentina.gob.ar/normativa/nacional/resolución-39-2013-256576/texto (publicación en el Boletín Oficial del 09/12/2015). Texto completo (curl). Vi solo la Primera Parte; la Segunda Parte (el texto modificado de la RT 17, sección 3.1) dice «Publicada en www.facpce.org.ar» y no la leí (**hueco**: la redacción literal de la sección 3.1 de la RT 17 tal como quedó).
- Considerando f: «(i) el parámetro cuantitativo de una variación en el nivel general de precios que se aproxime o sobrepase el 100% acumulativo en tres años».
- Considerando g: «que es necesario precisar el parámetro (i) indicando que el mismo se cumple cuando la variación en el nivel general de precios alcance o sobrepase el 100% acumulativo en tres años».

### 3.3 Resolución JG FACPCE 539/18, en la adopción de CPCECABA (Res. C.D. 107/2018)
URL: https://consejo.org.ar/storage/attachments/ResolucionCD107.pdf-7tClFYvNUW.pdf. Texto completo (curl + pdftotext). El anexo reproduce la Segunda Parte de la JG 539/18. CPCECABA solo cambió el punto 7, para remitir a su propia Res. C.D. 24 en lugar de la RT 48.
- **Por qué (considerando d):** «la Federación Argentina de Consejos Profesionales de Ciencias Económicas (FACPCE) ha realizado un monitoreo permanente de los índices de precios, concluyendo que la tasa acumulada de inflación en los últimos 3 años supera el 100 %, medida en las diferentes combinaciones posibles de índices disponibles y, entre otros, con el Índice de Precios Internos al por Mayor (IPIM), lo que permite concluir que debe iniciarse la aplicación del ajuste por inflación … para la preparación de los estados contables correspondientes a períodos contables (anuales o intermedios) que cierren a partir del 01/07/2018 (inclusive).»
- **Por qué el IPC del INDEC (considerando f):** «atento a la publicación del Índice de Precios al Consumidor (IPC Nacional, el que contiene una toma de precios de diversas zonas geográficas) por el Instituto Nacional de Estadística y Censos (INDEC) a partir de enero de 2017 (base diciembre de 2016), existen condiciones que permiten utilizar este índice para compatibilizar la aplicación del procedimiento de la RT N° 6 con la práctica internacional en relación con la NIC 29 … basados en una serie que empalme el IPC Nacional desde enero de 2017, con el IPIM hasta esa fecha.»
- **Lo que cuesta (considerando g):** «la aplicación del ajuste integral por inflación requiere esfuerzos diversos (capacitación, modificación de sistemas informáticos, búsqueda de información, definición de ciertos aspectos conceptuales por parte de la profesión, y otros)». Sirve para la nota: los sistemas tuvieron que cambiar.
- **Fecha y lugar de la JG 539/18 (considerando i):** fue aprobada «en la reunión realizada el 29 de septiembre de 2018 en la ciudad de San Juan».
- **Anexo, 1.1:** «La declaración de que nos encontramos en un contexto de inflación en Argentina (en los términos de la sección 3.1 de la RT N° 17 y 2.6 de la RT N° 41) a partir del 01/07/2018 (inclusive) implica que los estados contables correspondientes a ejercicios anuales o de períodos intermedios cuyo cierre haya ocurrido a partir del 01/07/2018 (inclusive) deberán reexpresarse de acuerdo con el procedimiento establecido en la RT N° 6.»
- **Anexo, 1.3 (el ajuste anterior):** «El último período en el que correspondió realizar el ajuste por inflación de la RT N° 6 fue el iniciado el 01/01/2002 y terminado el 30/09/2003. … Adicionalmente, como consecuencia de la vigencia del Decreto 1269/2002 (modificado por el Decreto 664/2003) ciertos entes realizaron el ajuste por inflación hasta el 28/02/2003.»
- **Anexo, 2.1 (opción de transición):** «El ente podrá optar, por única vez, por no realizar el ajuste por inflación de los estados contables correspondientes a los ejercicios anuales cerrados entre el 01/07/2018 y el 30/12/2018, ambas fechas inclusive».
- **Anexo, 3.6:** «Se podrán reexpresar los activos, pasivos y componentes del patrimonio neto con fecha de origen anterior al último proceso de reexpresión, tomando como base las cifras reexpresadas previamente desde la última reexpresión realizada (febrero de 2003).»
- **Anexo, 4.1(a) (simplificación):** «Esto es particularmente aplicable a la reexpresión de las partidas que componen las causas del estado de resultados, incluso mediante la aplicación de coeficientes de reexpresión anuales.» Y 4.1(b): «Se podrán determinar y presentar los resultados financieros y por tenencia (incluido el RECPAM) en una sola línea.»

### 3.4 La prohibición legal y su levantamiento
**Ley 23.928, art. 10 (Convertibilidad), Decreto 1269/2002 y Decreto 664/2003.** Resumidos en los considerandos de la Resolución General IGJ 10/2018.
URL: https://www.argentina.gob.ar/normativa/nacional/norma-318198/texto. Texto completo (curl).
- «el artículo 10 de la Ley N° 23.928 -Ley de Convertibilidad- derogó desde el 1º de abril de 1991 todas las normas legales o reglamentarias que establecen o autorizan la indexación por precio, actualización monetaria, variación de costos o cualquier otra forma de repotenciación de las deudas, impuestos, precios o tarifas de los bienes, obras o servicios».
- «el Decreto Nº 1269/2002 agregó al final del texto del citado artículo, un párrafo indicando que dicha derogación no comprendía a los estados contables».
- «el Decreto Nº 664/2003 derogó el último párrafo del artículo 10 de la Ley N° 23.928 introducido por el Decreto Nº 1269/2002, e instruyó a los Organismos dependientes del Poder Ejecutivo Nacional para que dispongan en el ámbito de sus competencias, que los balances o los estados contables deberían observar lo dispuesto por el citado artículo.»
- «el artículo 62 in fine de la Ley General de Sociedades, establece que los estados contables correspondientes a ejercicios completos o períodos intermedios dentro de un mismo ejercicio, deberán confeccionarse en moneda constante.»
- Lo que dispone la IGJ (nuevo art. 312 de la RG 7/2015): «Los estados contables correspondientes a ejercicios económicos completos o periodos intermedios, … deberán presentarse ante este Organismo expresados en moneda homogénea.» Además: «Las decisiones adoptadas por el órgano de gobierno de la sociedad deberán tomarse con la información contable en moneda constante.»

**Decreto 664/2003.** Texto en Justia, que copia Infoleg.
URL: https://docs.argentina.justia.com/federales/decretos/decreto-n-664-2003-mar-25-2003.pdf. Texto completo (curl + pdftotext). Justia no es oficial; la fuente oficial es el Boletín Oficial del 25/03/2003, que no bajé.
- Art. 1: «Derógase el último párrafo del Artículo 10 de la Ley N° 23.928 introducido por el Artículo 2° del Decreto N° 1.269 de fecha 16 de julio de 2002.»
- Motivo (considerandos): «la estabilidad lograda a partir del segundo semestre del año 2002 en el nivel de precios y en el tipo de cambio, hace necesario revisar las medidas adoptadas a efectos de evitar que persista un marco normativo destinado a corregir situaciones que ya no existen.»
- Art. 3: «Las disposiciones del presente decreto entrarán en vigencia el día de su publicación en el Boletín Oficial y surtirán efecto para los ejercicios comerciales que cierren a partir de dicha fecha, inclusive.»

**Ley 27.468 (B.O. 04/12/2018).**
URL: https://www.boletinoficial.gob.ar/pdf/aviso/primera/197153/20181204. Texto completo (curl + pdftotext); primaria oficial.
- Art. 5: «Incorpórase como último párrafo del artículo 10 de la ley 23.928 y sus modificatorias, el siguiente: La indicada derogación no comprende a los estados contables, respecto de los cuales continuará siendo de aplicación lo dispuesto en el artículo 62 in fine de la Ley General de Sociedades 19.550 (t.o. 1984) y sus modificatorias.»
- Art. 6: «Derógase el decreto 1.269 del 16 de julio de 2002 y sus modificatorios.»
- Art. 7(c): «El artículo 5°: a partir de la fecha que establezcan el Poder Ejecutivo nacional a través de sus organismos de contralor y el Banco Central de la República Argentina en relación con los balances o estados contables que les sean presentados.»
- Art. 1 (impositivo, no contable): reemplaza el IPIM por el IPC en la ley de Ganancias. Lo vi solo en la extracción de la página del aviso (URL https://www.boletinoficial.gob.ar/detalleAviso/primera/197153/20181204) y no lo cito literal.

**CNV, Resolución General 777/2018.**
URL: https://www.boletinoficial.gob.ar/pdf/aviso/primera/199000/20181228. Texto completo (curl + pdftotext), solo la primera página.
- «se establece que la aplicación de las normas que regulan la reexpresión de los estados financieros será obligatoria para aquellos estados financieros anuales, por períodos intermedios o especiales, que cierren a partir del 31 de diciembre de 2018 inclusive».
- **Para la nota.** La fecha cambia según el organismo: FACPCE y CPCECABA fijaron los cierres desde el 01/07/2018 y la CNV, los cierres desde el 31/12/2018.

### 3.5 RT 54 (Norma Unificada Argentina de Contabilidad)
URL: https://consejo.org.ar/micrositios-profesionales/rt-54-norma-unificada-argentina-de-contabilidad. Texto completo (curl).
- Vigencia en CABA: «Para la preparación de estados contables correspondientes a ejercicios iniciados a partir del 1° de enero de 2025 inclusive, sin exigir su aplicación a los períodos intermedios comprendidos en el primer ejercicio.» Y además: «Se admite la aplicación anticipada para la preparación de estados contables correspondientes a ejercicios finalizados a partir del 30 de septiembre de 2024 inclusive.»
- Marco con la RT 54 vigente: RT 54, RT 36, RT 26 y RT 16. La RT 6 no aparece en esa lista.
- **Hueco.** No leí el texto de la RT 54 sobre moneda homogénea. Un snippet dice que la versión original de la RT 54 derogaba la RT 6 e incorporaba la reexpresión dentro de la norma unificada, pero no lo verifiqué. Las fechas de vigencia también difieren entre snippets: 1/1/2024 en la versión original, 1/7/2024 según otras fuentes y 1/1/2025 según CPCECABA. La nota debería decir «según la jurisdicción» y citar la de CPCECABA.

### 3.6 Tipo de cambio oficial de referencia (BCRA, Comunicación «A» 3500)
- **Texto original (01/03/2002).** URL: https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A3500.pdf. Texto completo (curl + pdftotext); primaria.
  - «El Banco Central obtendrá cada día hábil bancario cotizaciones del tipo de cambio de compra y venta del dólar estadounidense para operaciones liquidables en pesos y dólares estadounidenses en la fecha de cotización. Esas cotizaciones, solicitadas a través del sistema SIOPEL del Mercado Abierto Electrónico a todas las entidades participantes, deberán reflejar las condiciones predominantes en el mercado de cambios mayorista.»
  - «El Banco Central informará mediante comunicado de prensa el tipo de cambio que resulte conforme al procedimiento previsto y lo publicará en la página institucional el día hábil bancario inmediato siguiente.»
- **Metodología nueva desde el 1/1/2026.** Nota de prensa del 4/12/2025: https://www.bcra.gob.ar/noticias/con-el-aporte-de-los-principales-actores-del-mercado-el-bcra-aprobo-una-nueva-metodologia-para-el-calculo-del-tipo-de-cambio-de-referencia-a-3500/. Texto completo (curl).
  - «El Banco Central de la República Argentina (BCRA) aprobó una nueva metodología de cálculo del Tipo de Cambio de Referencia (TCR), regido por la Comunicación A 3500, que entrará en vigor el 1° de enero de 2026.»
  - «al reemplazar el esquema anterior basado en encuestas de cotizaciones por una metodología que se sustenta en operaciones concretas y ponderadas por volumen.»
  - **Hueco.** No leí la comunicación «A» que fija la nueva fórmula, solo la nota de prensa.
- **Serie histórica.** La página https://www.bcra.gob.ar/tipo-cambio-referencia-comunicacion-a-3500-tcnpm/ (texto completo, curl) dice: «Planilla con la serie histórica del tipo de cambio de referencia establecido por la Comunicación A 3500 (segmento mayorista) y del Tipo de Cambio Nominal Promedio Mensual (TCNPM), disponible en un único archivo para su descarga y análisis.» Esa serie es la fuente natural para una tabla de tipos de cambio en el BI.

### 3.7 «Moneda dual», reportes de gestión en dólares y tipos de cambio múltiples
- **Hueco (fuente primaria).** No encontré una fuente primaria y confiable que describa la práctica de llevar la gestión en dólares en Argentina, ni que defina los tipos MEP, CCL o paralelo. Lo que hay es prensa y blogs.
- Lo que sí está en fuentes primarias y sirve para la nota:
  - NIC 21 §38: se puede presentar «in any currency (or currencies)».
  - NIC 21 §26: con varios tipos disponibles se usa aquel al que se podrían haber cancelado los flujos.
  - NIC 29 §3(b): uno de los indicadores de hiperinflación es que «the general population regards monetary amounts not in terms of the local currency but in terms of a relatively stable foreign currency. Prices may be quoted in that currency».
  - La NIC 29 §7 prohíbe presentar la información reexpresada como suplemento de estados sin reexpresar. Un reporte de gestión en dólares es información interna, no estados contables; esa distinción la infiero yo, no la dice ninguna fuente.
- **Salida del cepo (abril de 2025).** Los snippets dicen que la Comunicación «A» 8226 del BCRA (11/04/2025) levantó el límite a personas humanas y que sigue habiendo restricciones para personas jurídicas. Solo vi snippets (Boletín Oficial https://www.boletinoficial.gob.ar/detalleAviso/primera/324125/20250416 y estudios jurídicos). **Hueco**: no lo leí.

---

## 4. NIIF 10 (IFRS 10): procedimientos de consolidación

URL: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs10.html. Texto completo (curl).
- **B86, literal:**
  - «Consolidated financial statements: (a) combine like items of assets, liabilities, equity, income, expenses and cash flows of the parent with those of its subsidiaries.»
  - «(b) offset (eliminate) the carrying amount of the parent's investment in each subsidiary and the parent's portion of equity of each subsidiary (IFRS 3 explains how to account for any related goodwill).»
  - «(c) eliminate in full intragroup assets and liabilities, equity, income, expenses and cash flows relating to transactions between entities of the group (profits or losses resulting from intragroup transactions that are recognised in assets, such as inventory and fixed assets, are eliminated in full). Intragroup losses may indicate an impairment that requires recognition in the consolidated financial statements. IAS 12 Income Taxes applies to temporary differences that arise from the elimination of profits and losses resulting from intragroup transactions.»
- **§19:** «A parent shall prepare consolidated financial statements using uniform accounting policies for like transactions and other events in similar circumstances.» Y B87: «appropriate adjustments are made to that group member's financial statements in preparing the consolidated financial statements to ensure conformity with the group's accounting policies.» **Para la nota multiempresa.** Es el equivalente contable de «conformar» planes de cuentas y criterios.
- **§20:** «Consolidation of an investee shall begin from the date the investor obtains control of the investee and cease when the investor loses control of the investee.»
- **B92:** «The financial statements of the parent and its subsidiaries used in the preparation of the consolidated financial statements shall have the same reporting date.»
- **B93:** «the difference between the date of the subsidiary's financial statements and that of the consolidated financial statements shall be no more than three months».

---

## 5. Conciliar el BI con la fuente y con el mayor

### Kimball Group, Design Tip #134 «Data Warehouse Testing Recommendations» (Joy Mundy, 4/5/2011)
URL: https://www.kimballgroup.com/2011/05/design-tip-134-data-warehouse-testing-recommendations/. Texto completo (curl).
- «For unit testing and data quality testing, define tests to run a query in the source and target data warehouse. You're looking for row counts and amounts to match up.»
- «Create a small static test database, derived from real data.»
- «We need the business users' expertise to define good system tests. How do we know the data is correct?»

### Kimball, técnica «Audit Dimension»
URL: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/audit-dimension/. Texto completo (curl).
- «When a fact table row is created in the ETL back room, it is helpful to create an audit dimension containing the ETL processing metadata known at the time. A simple audit dimension row could contain one or more basic indicators of data quality, perhaps derived from examining an error event schema that records data quality violations encountered while processing the data.»
- «These environment variables are especially useful for compliance and auditing purposes because they enable BI tools to drill down to determine which rows were created with what versions of the ETL software.»

### Kimball, técnica «Error Event Schemas»
URL: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/error-event-schema/. Texto completo (curl).
- «Managing data quality in a data warehouse requires a comprehensive system of data quality screens or filters that test the data as it flows from the source systems to the BI platform. When a data quality screen detects an error, this event is recorded in a special dimensional schema that is available only in the ETL back room.»

### Kimball, «ETL Architecture's 34 Subsystems» (página resumen)
URL: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/etl-architecture-34-subsystems/. Texto completo (curl).
- «Five subsystems deal with value-added cleaning and conforming, including dimensional structures to monitor quality errors.» El detalle está en el libro *The Data Warehouse Toolkit*, 3.ª ed., que no leí.

### Mayores auxiliares contra la cuenta de control del mayor: OpenStax, *Principles of Accounting, Volume 1: Financial Accounting*, 7.4 «Prepare a Subsidiary Ledger»
URL: https://openstax.org/books/principles-financial-accounting/pages/7-4-prepare-a-subsidiary-ledger. Texto completo (curl). Es un libro de texto universitario abierto, no una norma de auditoría.
- «The purpose of keeping subsidiary ledgers is for accuracy and efficiency. … Since the total of the accounts receivable subsidiary ledger must agree with the balance shown in the accounts receivable general ledger account, the system helps us find mistakes.»
- «Today, computerized accounting information systems use the same method to store and total amounts, but it takes a lot less time.»

### Huecos de la sección 5
- **Kimball: el mayor contra el balance de sumas y saldos.** No encontré en kimballgroup.com un texto que hable de conciliar el depósito de datos con el balance de sumas y saldos (*trial balance*). El capítulo de contabilidad del *Toolkit* (instantánea periódica del mayor, asientos y presupuesto) está detrás del muro de O'Reilly, que devolvió 403. Las copias en archive.org no son legítimas y no las usé.
- **Totales de control en auditoría de sistemas.** Del manual de examen de TI de la FFIEC (*hash totals*, *record counts*, *run-to-run totals*) solo vi un snippet de una copia archivada de 2004. La copia archivada devolvió 504 y no la leí.
- **Normas de auditoría (PCAOB o NIA) sobre conciliar auxiliares con el mayor:** no lo busqué a fondo.

---

## 6. Combinar varias fuentes (ERP, CRM, comercio electrónico, planillas)

### Kimball: dimensiones conformadas, arquitectura en bus y *drill-across*
Las cuatro páginas son de https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/… Texto completo (curl).
- **conformed-dimension:** «Dimension tables conform when attributes in separate dimension tables have the same column names and domain contents. Information from separate fact tables can be combined in a single report by using conformed dimension attributes that are associated with each fact table. … This is the essence of integration in an enterprise DW/ BI system. Conformed dimensions, defined once in collaboration with the business's data governance representatives, are reused across fact tables».
- **enterprise-data-warehouse-bus-architecture:** «This architecture decomposes the DW/ BI planning process into manageable pieces by focusing on business processes, while delivering integration via standardized conformed dimensions that are reused across processes.»
- **drilling-across:** «Drilling across simply means making separate queries against two or more fact tables where the row headers of each query consist of identical conformed attributes. The answer sets from the two queries are aligned by performing a sort-merge operation on the common dimension attribute row headers.»
- **conformed-fact:** «If the same measurement appears in separate fact tables, care must be taken to make sure the technical definitions of the facts are identical if they are to be compared or computed together. … if they are incompatible, they should be differently named to alert the business users and BI applications.»

### Claves distintas en cada sistema
- **natural-durable-supernatural-key:** «Natural keys created by operational source systems are subject to business rules outside the control of the DW/BI system. … When the data warehouse wants to have a single key for that employee, a new durable key must be created that is persistent and does not change in this situation. … The best durable keys have a format that is independent of the original business process and thus should be simple integers assigned in sequence beginning with 1.»

### Granos distintos
- **grain:** «The grain establishes exactly what a single fact table row represents. … Each proposed fact table grain results in a separate physical table; different grains must not be mixed in the same fact table.»
- **allocated-fact:** «It is quite common in header/line transaction data to encounter facts of differing granularity, such as a header freight charge. You should strive to allocate the header facts down to the line level based on rules provided by the business».

### Lo que pasa si no se conforma: Design Tip #135 (Margy Ross, junio de 2011)
URL: https://www.kimballgroup.com/2011/06/design-tip-135-conformed-dimensions-as-the-foundation-for-agile-data-warehousing/. Texto completo (curl).
- «data sets may look like they can be compared and integrated due to similar labels, but the underlying business rules may be slightly different. Business users waste inordinate amounts of time trying to reconcile and resolve these data inconsistencies».

### Varias monedas en la tabla de hechos: técnica «Multiple Currency Facts»
URL: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/multiple-currencies/. Texto completo (curl).
- «Fact tables that record financial transactions in multiple currencies should contain a pair of columns for every financial fact in the row. One column contains the fact expressed in the true currency of the transaction, and the other contains the same fact expressed in a single standard currency that is used throughout the fact table. The standard currency value is created in an ETL process according to an approved business rule for currency conversion. This fact table also must have a currency dimension to identify the transaction's true currency.»
- **Para la nota.** La «approved business rule» de Kimball es donde entran la NIC 21 (tipo de la fecha de la transacción o promedio, y cierre para los saldos) y, en Argentina, la elección del tipo según la NIC 21 §26.

### Planillas como fuente: Panko y EuSpRIG
- **Panko (2000), «Spreadsheet Errors: What We Know. What We Think We Can Do.»** Actas del EuSpRIG 2000. URL: https://arxiv.org/pdf/0802.3457. Texto completo (curl + pdftotext).
  - «Fifteen years of research studies have concluded unanimously that spreadsheet errors are both common and non-trivial.»
  - «The field audits found errors in 24% of the 367 spreadsheets audited, and most older audits used audit techniques not likely to catch a majority of errors. The most recent field audits, in contrast, generally used better methodologies and found errors in at least 86% of the spreadsheets audited.»
  - «[Hicks and Lukasik] found that the cell error rates, that is, the percentages of cells containing original errors … were 1.1%, 2.2%, and 2.5%.» (Lo que está entre corchetes es mío; el original dice «They».)
  - «Across these experiments, 51% of all spreadsheets contained errors, despite the fact that most spreadsheets were only 25 to 50 cells in total size.»
- **Panko (2015), «What We Don't Know About Spreadsheet Errors Today».** Actas del EuSpRIG 2015. URL: https://arxiv.org/pdf/1602.02601. Texto completo (curl + pdftotext).
  - «The first is that spreadsheet errors are rare on a per-cell basis, but in large programs, at least one incorrect bottom-line value is very likely to be present. The second is that errors are extremely difficult to detect and correct. The third is that spreadsheet developers and corporations are highly overconfident in the accuracy of their spreadsheets.»
  - «The table shows the results of 85 intensive inspection studies that took several days per spreadsheet. … Collectively, these studies found errors in 94% of the spreadsheets studied.»
  - «The average across these studies is a cell error rate of 3.9%.» Esa cifra corresponde a los estudios de laboratorio sobre desarrollo de planillas.
- **Hueco.** No busqué la página de «horror stories» de EuSpRIG ni casos documentados de errores de planilla con impacto financiero.

### Datos maestros (MDM)
- **Hueco.** No busqué una fuente primaria sobre datos maestros (DAMA-DMBOK o similar). Kimball cubre la parte analítica con las dimensiones conformadas y las claves durables.

---

## 7. Presupuesto contra real en el BI

### Kimball, técnica «Consolidated Fact Tables»
URL: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/consolidated-fact-table/. Texto completo (curl).
- «It is often convenient to combine facts from multiple processes together into a single consolidated fact table if they can be expressed at the same grain. For example, sales actuals can be consolidated with sales forecasts in a single fact table to make the task of analyzing actuals versus forecasts simple and fast, as compared to assembling a drill-across application using separate fact tables. Consolidated fact tables add burden to the ETL processing, but ease the analytic burden on the BI applications.»

### Kimball, «The Soul of the Data Warehouse, Part 2: Drilling Across» (Ralph Kimball, 5/4/2003)
URL: https://www.kimballgroup.com/2003/04/the-soul-of-the-data-warehouse-part-two-drilling-across/. Texto completo (curl).
- «you can drill across two fact tables, one at the brand level with a brand dimension (such as a forecast), and the other at a detailed product level with a product dimension (such as sales transactions).»
- «If the names of the brands are drawn from the same domain, you can complete the drill-across (of forecast vs. actual) by confidently merging the rows with the same brand names.»

### Kimball, Design Tip #137 «Creating and Managing Shrunken Dimensions» (Warren Thornthwaite, 2/8/2011)
URL: https://www.kimballgroup.com/2011/08/design-tip-137-creating-and-managing-shrunken-dimensions/. Texto completo (curl).
- «For example, a Month dimension would be a shrunken dimension of the Date dimension. The Month dimension could be connected to a forecast fact table whose grain is at the monthly level.»

### Huecos de la sección 7
- **Las tablas de presupuesto del capítulo de contabilidad del *Toolkit*** (Kimball y Ross, 3.ª ed., 2013, cap. 7: el presupuesto con grano de «cambio neto» y las tablas de compromisos y pagos). No leí el texto; O'Reilly devolvió 403. Un blog de terceros (gyaankatta.blogspot.com) dice que el grano del presupuesto es «the net change», pero solo lo vi en un snippet y no lo cito.
- **«El presupuesto suele vivir en planillas».** No encontré una fuente primaria que lo afirme. Si la nota lo dice, tiene que ir como observación de práctica, sin cita, o apoyarse en Panko para el riesgo de usar planillas como fuente.

---

## Resumen de huecos
1. NIC 21: los encabezados de los §39 y §42 con la enmienda de noviembre de 2025 en limpio (la edición 2026 mezcla texto agregado y borrado). Los incisos que importan no cambian.
2. La redacción literal de la sección 3.1 de la RT 17 (modificada por la RT 39) y el texto de la RT 54 sobre moneda homogénea. Las fechas de vigencia de la RT 54 difieren entre fuentes.
3. Los PDF propios de la FACPCE (JG 539/18 y la metodología del índice) dan 404. Usé la adopción de CPCECABA, que transcribe la Segunda Parte.
4. «Moneda dual» o gestión en dólares en Argentina, y los tipos MEP, CCL o paralelo: no hay fuente primaria confiable. La Comunicación «A» 8226 (salida del cepo) solo la vi en snippets.
5. La comunicación del BCRA con la fórmula nueva del tipo de cambio de referencia A 3500: solo leí la nota de prensa.
6. Kimball sobre conciliar con el mayor o el balance de sumas y saldos, y el capítulo de presupuesto del *Toolkit*: detrás del muro de O'Reilly.
7. Totales de control según una norma de auditoría o el manual de la FFIEC: solo snippet.
8. Datos maestros (DAMA) y los casos de EuSpRIG: no los busqué.
