# Informe: Proyectos de inversión, vertical EVALUACIÓN (decisión de inversión)

## Advertencias de método

- **Búsqueda web agotada.** El presupuesto de búsquedas se acabó a mitad de la investigación. No pude buscar Poterba y Summers 1995 en su fuente, Damodaran por tema, encuestas latinoamericanas, ni cubrir análisis de riesgo con una fuente propia. Esos puntos quedan como huecos al final.
- **Lo que leí entero.** Los PDF los bajé y los leí con `pdftotext`. Esos son [L] sin intermediario. Las páginas de OpenStax pasaron por el extractor de WebFetch, que resume con un modelo chico. Las frases entre comillas de OpenStax son lo que devolvió el extractor. Antes de citarlas como literales hay que cotejarlas con la página.
- **Graham y Harvey 2001.** No leí la versión de JFE. Leí la versión de divulgación de los mismos autores y la misma encuesta (JACF 2002), más la Tabla I de Graham 2022, que reproduce las cifras de 2001.
- **División por componentes.** Coincide con cómo el campo divide la vertical, con dos ajustes:
  - "Flujo de fondos" y "tasa de corte" son los dos capítulos donde los textos dedican más espacio. En OpenStax Principles of Finance, el flujo de caja del proyecto casi no aparece, y el capítulo 16 arranca con flujos ya dados.
  - Los libros de texto suelen tratar sensibilidad, escenarios, Monte Carlo y opciones reales juntos, bajo "análisis de riesgo del proyecto". Conviene mantenerlos como un solo componente.
  - OpenStax ch. 15 es riesgo y retorno (CAPM), no costo de capital. El WACC como tal no lo encontré en OpenStax.

---

## 1. Flujo de fondos del proyecto

| Fuente | URL | Tipo | Aut | Prof | Ej | Uniq | Marca |
|---|---|---|---|---|---|---|---|
| Damodaran, Sesión 13 de Corporate Finance (slides, caso mina Vale) | https://pages.stern.nyu.edu/~adamodar/pdfiles/classslidesMar12/cfsession13slides.pdf | primaria (material docente de autor de referencia) | 3 | 2 | 3 | 3 | [L] |
| Damodaran, índice de sesiones (qué cubre cada una: flujos incrementales, costos laterales, canibalización, sinergias, divisas) | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/webcastcfspr25.htm | primaria (índice) | 3 | 1 | 1 | 2 | [L] |
| Damodaran, puzzle de costos hundidos | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/cfpuzzles/cfspr23puzzle6.htm | primaria | 3 | 1 | 2 | 2 | [L] |
| OpenStax Principles of Managerial Accounting 11.4 | https://openstax.org/books/principles-managerial-accounting/pages/11-4-use-discounted-cash-flow-models-to-make-capital-investment-decisions | primaria (texto abierto) | 2 | 1 | 2 | 1 | [L] |
| OpenStax Principles of Finance 16.5 (error en estimar flujos) | https://openstax.org/books/principles-finance/pages/16-5-choosing-between-projects | primaria | 2 | 1 | 1 | 1 | [L] |

**Afirmaciones**
- **El texto OpenStax de finanzas no desarrolla los componentes del flujo.** 16.5 solo dice "Estimating cash flows from potential projects is prone to errors." Remite al capítulo 18, de pronóstico financiero (https://openstax.org/books/principles-finance/pages/16-5-choosing-between-projects). No leí el capítulo 18.
- **OpenStax contabilidad gerencial 11.4 no cubre impuestos ni escudo fiscal.** Dice que "More complex considerations, such as depreciation, the effects of income taxes" quedan para cursos avanzados. Tampoco trata capital de trabajo, costo hundido ni costo de oportunidad (https://openstax.org/books/principles-managerial-accounting/pages/11-4-use-discounted-cash-flow-models-to-make-capital-investment-decisions).
- **Costo hundido.** Damodaran: "the rational thing to do is to let go of everything that has happened in the past and focus on the future." (https://pages.stern.nyu.edu/~adamodar/New_Home_Page/cfpuzzles/cfspr23puzzle6.htm)
- **Damodaran, Sesión 14** (índice): incluye "side costs (opportunity costs, cannibalization)" y "side benefits (synergies)". No leí las notas de clase, solo el índice (https://pages.stern.nyu.edu/~adamodar/New_Home_Page/webcastcfspr25.htm).
- **Nominal vs real.** Damodaran estima flujos en US$ nominales y los descuenta al costo del capital propio en US$. Pregunta si en términos reales y a tasa real el resultado cambiaría, sin dar la respuesta en las slides (https://pages.stern.nyu.edu/~adamodar/pdfiles/classslidesMar12/cfsession13slides.pdf).
- **Financiamiento.** Damodaran lo trata como alternativa: en la versión "patrimonio" los flujos son "cashflows after debt payments to equity investors" y la tasa de corte es el costo del capital propio. Hay otra versión al costo de capital, con flujos antes de deuda. Para el lector no financiero sirve para mostrar que "financiamiento fuera del flujo" es una elección de método, no un olvido.

**Ejemplo numérico literal (Damodaran, mina de hierro de Vale, en US$ millones salvo indicación)**
- Datos de la slide:
  - Inversión inicial: "$1.25 billion". Se deprecia en diez años por saldo decreciente doble, "down to a salvage value of $250 million".
  - Capital de trabajo: "20% of total revenues", invertido al inicio de cada año. "At the end of the tenth year, it is anticipated that the entire working capital will be salvaged."
  - Impuesto: "corporate tax rate of 34%".
  - Deuda: pedir "$0.5 billion" a 4,05%.
  - Costo del capital propio usado: 11,13%.
- Tabla de flujo al capital propio, años 0 a 10: capex 750,00 en año 0. Variación de capital de trabajo: 81,60; 43,25; 44,95; 3,40; 3,46; 3,53; 3,60; 3,68; 3,75; 3,82; y (195,04) en año 10. Es negativa porque se recupera. Valor residual 250,00 en año 10. Flujo al capital propio: (831,60); 37,82; 100,05; 211,33; 206,48; 203,44; 201,86; 205,91; 210,04; 214,22; 667,42.
- Depreciación (escudo fiscal): 200,00; 160,00; 128,00; 102,40; 81,92; 65,54, y 65,54 los años siguientes. Se suma de vuelta porque es no monetaria. Su efecto fiscal entra al reducir el impuesto en la línea de resultado. Impuestos: (39,87) en año 1, 14,54 en año 2, 67,85 en año 3.
- Se pueden rehacer las cuentas con esa tabla. Verificá la columna de capex y el flujo del año 0 contra el PDF original antes de publicarla.

**Recurso canónico:** Damodaran, Sesiones 12 a 14 de Corporate Finance, y las slides de la 13 para el caso numérico completo. En el caso, fijarse en:
- tres líneas que todo no financista debe ver (capital de trabajo que sale y vuelve, residual, depreciación como no monetaria);
- el paso de resultado contable a flujo de caja;
- el contraste entre flujo al capital propio y flujo al proyecto.

Para un texto de nivel intermedio con los cuatro principios en prosa (incremental, hundido, oportunidad, colaterales), el capítulo de flujos de Brealey-Myers-Allen o Berk-DeMarzo sería lo ideal. No pude acceder a ninguno (ver huecos).

---

## 2. Valor actual neto (VAN)

| Fuente | URL | Tipo | Aut | Prof | Ej | Uniq | Marca |
|---|---|---|---|---|---|---|---|
| OpenStax Principles of Finance 16.2 | https://openstax.org/books/principles-finance/pages/16-2-net-present-value-npv-method | primaria (texto de referencia abierto) | 2 | 2 | 3 | 1 | [L] vía extractor |
| OpenStax 16.4 (índice de rentabilidad) | https://openstax.org/books/principles-finance/pages/16-4-alternative-methods | primaria | 2 | 2 | 3 | 1 | [L] vía extractor |
| OpenStax 16.5 (excluyentes, capital racionado) | https://openstax.org/books/principles-finance/pages/16-5-choosing-between-projects | primaria | 2 | 2 | 3 | 2 | [L] vía extractor |
| OpenStax 16.6 (perfil de VAN) | https://openstax.org/books/principles-finance/pages/16-6-using-excel-to-make-company-investment-decisions | primaria | 2 | 1 | 2 | 2 | [L] vía extractor |
| OpenStax Managerial Accounting 11.4 | https://openstax.org/books/principles-managerial-accounting/pages/11-4-use-discounted-cash-flow-models-to-make-capital-investment-decisions | primaria | 2 | 1 | 2 | 1 | [L] vía extractor |

**Afirmaciones**
- Fórmula, como la escribe OpenStax: "NPV = PV Cash Inflows − PV Cash Outflows". Regla: "Projects with a positive NPV should be accepted, and projects with a negative NPV should be rejected." (https://openstax.org/books/principles-finance/pages/16-2-net-present-value-npv-method)
- Índice de rentabilidad: "The profitability index (PI) uses the same inputs as the NPV calculation, but it converts the results to a ratio." Fórmula: PI = PV(inflows) / PV(outflows) (https://openstax.org/books/principles-finance/pages/16-4-alternative-methods).
- Para excluyentes: "the rule is to take the project with the highest NPV." Con capital racionado, el texto muestra que rankear por VAN puede engañar y que rankear por índice de rentabilidad agrega más valor (https://openstax.org/books/principles-finance/pages/16-5-choosing-between-projects).

**Ejemplo literal (OpenStax, Sam's Sporting Goods, máquina bordadora)**
- Desembolso año 0: $16.000. Flujos: año 1 $2.000; año 2 $4.000; años 3 a 6 $5.000 cada uno. Tasa 9% ("cost of funds").
- VAN = $2.835,63. Frase: "Because the NPV is positive, Sam's Sporting Goods should purchase the embroidery machine." (https://openstax.org/books/principles-finance/pages/16-2-net-present-value-npv-method)
- Flujos descontados (16.4): 1.834,86; 3.366,72; 3.860,92; 3.542,13; 3.249,66; 2.981,34. Suma 18.835,63, que dividido por 16.000 da índice de rentabilidad 1,18 (el texto da "$18,836 / $16,000 = 1.18").
- Excluyentes (16.5): la máquina común cuesta $16.000, tiene VAN $2.835,62 y TIR 14,10%. La de uso intensivo cuesta $25.000, VAN $3.970,67 y TIR 13,20%. Gana la de mayor VAN, aunque su TIR sea menor.
- Vidas distintas (16.5, camiones de helado, tasa 10%): el camión viejo cuesta $50.000, dura 3 años, VAN $49.474. El nuevo cuesta $50.000, dura 6 años, VAN $80.658. Cadena de reemplazo: dos viejos en secuencia, VAN $86.645. Anualidad equivalente: viejo $19.894, nuevo $18.520. Gana el viejo.
- Capital racionado (16.5): presupuesto de $200 millones con siete proyectos positivos que piden $430 millones. Con índice de rentabilidad se eligen A, E y F, que suman $78 millones de VAN. Un VAN menor de D ($15 millones) frente a E ($11 millones) y F ($7 millones), que juntos suman $18 millones por los mismos $50 millones.

**Recurso canónico:** OpenStax 16.2, y luego 16.5 para la parte de decisión entre alternativas. En 16.5 fijarse en el caso donde mayor VAN y mayor TIR no coinciden, y en el de vidas distintas. Discrepancia menor: el texto da el desembolso como $16.000 en 16.2 y 16.4, y el flujo de seis años en esas páginas, pero 16.1 muestra cinco años de entradas. Hay que usar el de seis años para VAN, TIR y repago descontado.

---

## 3. Tasa interna de retorno (TIR)

| Fuente | URL | Tipo | Aut | Prof | Ej | Uniq | Marca |
|---|---|---|---|---|---|---|---|
| OpenStax 16.3 | https://openstax.org/books/principles-finance/pages/16-3-internal-rate-of-return-irr-method | primaria | 2 | 2 | 3 | 1 | [L] vía extractor |
| OpenStax 16.4 (TIR modificada) | https://openstax.org/books/principles-finance/pages/16-4-alternative-methods | primaria | 2 | 2 | 3 | 1 | [L] vía extractor |
| OpenStax Managerial Accounting 11.4 | (misma URL de arriba) | primaria | 2 | 1 | 2 | 1 | [L] vía extractor |

**Afirmaciones**
- Definición: "The internal rate of return (IRR) is the discount rate that sets the present value of the cash inflows" igual al de las salidas. Regla: "If the IRR is greater than the cost of capital, a project should be accepted." (https://openstax.org/books/principles-finance/pages/16-3-internal-rate-of-return-irr-method)
- Problemas, con las frases del extractor:
  - Múltiples TIR: "there may not be a single mathematical solution to an IRR problem", cuando hay flujos negativos en más de un período. El texto da un ejemplo de una instalación olímpica con dos TIR, que no leí en detalle.
  - Reinversión: "The IRR assumes that the cash flows are reinvested at the internal rate of return when they are received."
  - Escala: "The IRR converts the cash flows to percentages and ignores differences in the size or scale of projects."
- TIR modificada (MIRR): capitaliza las entradas al costo de capital y da una sola solución, "unlike the IRR, which may have multiple mathematical solutions" (https://openstax.org/books/principles-finance/pages/16-4-alternative-methods).

**Ejemplo literal (OpenStax, misma máquina bordadora)**
- Flujos iguales a los del VAN. El perfil de VAN "crossed the horizontal axis at 14%". Calculadora: TIR 14,09. En 16.5 aparece como 14,10%. El texto dice "The IRR is about, but not exactly, 14%."
- MIRR: salida $16.000 en año 0. Valor terminal de las entradas capitalizadas al 9%: $31.595,22 en año 6. Ecuación $16.000 = $31.595,22 / (1+i)^6, que da i = 0,12, o 12%.
- Ejemplo de 16.6 (perfil de VAN): TIR 13,43% en el texto y 13,41% en el pie de la figura. El proyecto solar se rechaza solo si el costo de fondos supera ese valor.

**Recurso canónico:** OpenStax 16.3 más 16.5, con la lectura combinada de TIR y VAN en las excluyentes (la tabla de arriba, TIR 13,2% contra VAN mayor). Fijarse en que la TIR da 14,10% para la máquina chica y 13,20% para la grande, y aun así la grande agrega más valor.

---

## 4. Período de repago (payback)

| Fuente | URL | Tipo | Aut | Prof | Ej | Uniq | Marca |
|---|---|---|---|---|---|---|---|
| OpenStax 16.1 | https://openstax.org/books/principles-finance/pages/16-1-payback-period-method | primaria | 2 | 2 | 3 | 1 | [L] vía extractor |
| OpenStax 16.4 (repago descontado) | https://openstax.org/books/principles-finance/pages/16-4-alternative-methods | primaria | 2 | 2 | 3 | 1 | [L] vía extractor |
| Graham y Harvey (JACF 2002, divulgación de JFE 2001) | https://people.duke.edu/~charvey/Research/Published_Papers/P76_How_do_CFOs.pdf | primaria | 3 | 2 | 1 | 3 | [L] |
| Graham 2022, Journal of Finance (versión NBER) | https://nber.org/system/files/working_papers/w29841/w29841.pdf | primaria | 3 | 3 | 2 | 3 | [L] parcial (secciones de capital budgeting y Tabla I) |

**Afirmaciones**
- Definición: "how long it will take for a company to make enough free cash flow from the investment to recover the initial cost". Ventaja: "The principal advantage of the payback period method is its simplicity." Desventajas:
  - "the payback period calculation ignores the time value of money."
  - "there is not a clearly defined acceptance or rejection criterion."
  - "cash flows after the payback period are ignored."
  - "no risk adjustment is made for uncertain cash flows." (https://openstax.org/books/principles-finance/pages/16-1-payback-period-method)
- Por qué se usa igual (Graham y Harvey, 2002): "This result is surprising in the sense that financial textbooks have stressed the shortcomings of the payback criterion for decades". El repago fue el método más usado después de VAN, TIR y la tasa de corte: "56.7% always or almost always used it". Explicaciones propuestas:
  - la simplicidad;
  - la falta de familiaridad de la dirección;
  - en empresas con restricción de capital, un proyecto que no da caja temprano puede llevar a la quiebra antes de cobrar.
  - Los propios autores aclaran: "we find no direct evidence that companies are more likely to use payback when they are capital-constrained or financially distressed". Pocas empresas usaron repago descontado (https://people.duke.edu/~charvey/Research/Published_Papers/P76_How_do_CFOs.pdf).
- Graham 2022 (comentario sobre la discrepancia con los libros): "many (especially small) firms rely more heavily on payback than on NPV in capital allocation, possibly reflecting implementation challenges". En respuestas abiertas, las razones de no usar VAN son "liquidity needs, a lack of sophistication, and a preference for simple decision-making". El VAN a veces se usa "to support decisions that are driven by strategic or qualitative objectives" (https://nber.org/system/files/working_papers/w29841/w29841.pdf).

**Ejemplo literal (OpenStax)**
- Inversión $16.000, entradas $2.000, $4.000, $5.000, $5.000, $5.000 (cinco años en 16.1). Acumulado: 2.000; 6.000; 11.000; 16.000. "Thus, the payback period for the embroidery machine is four years."
- Repago descontado al 9% (con el flujo de seis años): acumulado descontado (16.000,00); (14.165,14); (10.798,42); (6.937,50); (3.395,37); (145,72); 2.835,62. Resultado: "5 + 145.72 / 2,981.34 = 5.05 years".

**Recurso canónico:** OpenStax 16.1, y 16.4 para la versión descontada. Para el "por qué igual se usa", Graham 2022, sección II (Tabla I y comentario). En la tabla fijarse en que en 2022 el repago aparece como más usado que el VAN entre las empresas chicas.

---

## 5. Tasa de corte (hurdle rate)

| Fuente | URL | Tipo | Aut | Prof | Ej | Uniq | Marca |
|---|---|---|---|---|---|---|---|
| Jagannathan, Matsa, Meier y Tarhan 2016, JFE 120(3), 445-463 (abstract en IDEAS) | https://ideas.repec.org/a/eee/jfinec/v120y2016i3p445-463.html | primaria | 3 | 2 | 1 | 3 | [M] |
| Jagannathan, Meier y Tarhan, NBER WP 16770 (2011), antecedente del anterior | https://www.nber.org/papers/w16770.pdf | primaria (WP, no revisado por pares) | 3 | 3 | 1 | 3 | [L] parcial (abstract, introducción) |
| Graham 2022, Journal of Finance (versión NBER) | https://nber.org/system/files/working_papers/w29841/w29841.pdf | primaria | 3 | 3 | 2 | 3 | [L] parcial |
| Graham y Harvey (JACF 2002) | https://people.duke.edu/~charvey/Research/Published_Papers/P76_How_do_CFOs.pdf | primaria | 3 | 2 | 1 | 3 | [L] |
| Kellogg, resumen del artículo 2016 | https://www.kellogg.northwestern.edu/academics-research/research/detail/2016/why-do-firms-use-high-discount-rates | secundaria | 2 | 1 | 1 | 1 | [S] |
| Poterba y Summers 1995 | (no verificada) | primaria | | | | | [S] a través de Jagannathan et al. |

**Afirmaciones**
- Resultado principal, abstract de JFE: "We present evidence consistent with operational constraints leading firms to use high discount rates" que "average twice the firms' cost of financial capital." Y "firms that use high discount rates have strong balance sheets", "low leverage, and large cash holdings". "In addition, firms appear to increase discount rates to account for idiosyncratic risk." Es la explicación por restricciones operativas (gente y tiempo de gestión) y no financieras (https://ideas.repec.org/a/eee/jfinec/v120y2016i3p445-463.html).
- Cifra de la muestra: 127 empresas, tasa media 15,1% nominal, mediana 15,0% (resumen del buscador, [S]; no lo verifiqué en el paper).
- WP de 2011, explicación alternativa por opción de esperar: "firms behave as though they add a hurdle premium to their CAPM based cost of capital". La prima depende del valor de la opción de diferir (McDonald y Siegel 1986). El CAPM explica solo el 10% de la variación entre empresas y las variables de opción de espera explican el 35%. "actual WACC constitutes about half of the value of the hurdle rate" (https://www.nber.org/papers/w16770.pdf). Esta es una explicación distinta de la de la versión publicada. Conviene presentar ambas como hipótesis y decir que el WP no fue revisado por pares.
- Poterba y Summers 1995, según el WP (no leí el original): "They document an average real hurdle rate of 12.2%, at a time when the long-term inflation expectation was around 5%." Encuentran tasas de corte por encima del costo de deuda y de capital propio, y "not related to CAPM betas" (https://www.nber.org/papers/w16770.pdf).
- Graham 2022: "for two decades at least, hurdle rates on average have built in a 6% 'buffer' above the cost of capital". La encuesta de 2022 (oleada de marzo 2019) da tasa de corte 15% frente a WACC 9% (Figura 3). "only 1-in-5 companies say they accept all projects whose expected return exceeds the stated hurdle rate." También: "standard textbook logic is that setting a hurdle rate higher than the cost of capital may cause firms to pass up value-creating projects." Las explicaciones de los CFO incluyen racionamiento, restricciones operativas, buscar los mejores proyectos, margen de error y riesgo no capturado. Las tasas son rígidas: unas 60% de las empresas norteamericanas cambiaron su tasa una vez o ninguna en diez años (https://nber.org/system/files/working_papers/w29841/w29841.pdf).
- Costo de capital en práctica (Graham y Harvey): "73.5% of respondents always or almost always" usaron CAPM para el costo del capital propio. Cerca del 60% usan una sola tasa para toda la empresa. "51% said they would always or almost always use a risk-matched discount rate" (https://people.duke.edu/~charvey/Research/Published_Papers/P76_How_do_CFOs.pdf).

**Hueco sobre WACC y costo de oportunidad del capital.** No encontré en OpenStax una sección de WACC (el cap. 15 es CAPM, ver arriba). Damodaran cubre costo de capital en sus sesiones 9 a 11 y 17 a 18, con notas en nyu.box.com que no abrí.

**Discrepancia entre fuentes.** El WP de 2011 dice que la prima viene de la opción de esperar. El JFE de 2016 la atribuye a restricciones operativas, y el Decaire (2021) citado por Graham la liga al riesgo idiosincrático. Ninguna fuente prueba una sola causa. Lo que sí coincide en todas es el hecho: las tasas de corte superan al WACC calculado.

**Recurso canónico:** Graham 2022, sección II.B, "Discount Rates and Hurdle Rates", y su Figura 3. Para un no financista, es la forma más corta de ver que "tasa de corte" y "costo de capital" no son lo mismo en la práctica. Para la parte teórica, el abstract de JFE 2016 en IDEAS.

---

## 6. Riesgo del proyecto

| Fuente | URL | Tipo | Aut | Prof | Ej | Uniq | Marca |
|---|---|---|---|---|---|---|---|
| Graham 2022, Tabla I | https://nber.org/system/files/working_papers/w29841/w29841.pdf | primaria | 3 | 1 | 2 | 3 | [L] parcial |
| Graham y Harvey (JACF 2002) | https://people.duke.edu/~charvey/Research/Published_Papers/P76_How_do_CFOs.pdf | primaria | 3 | 1 | 1 | 2 | [L] parcial |
| OpenStax 16.6 (perfil de VAN) | https://openstax.org/books/principles-finance/pages/16-6-using-excel-to-make-company-investment-decisions | primaria | 2 | 1 | 2 | 2 | [L] vía extractor |
| Damodaran Sesión 13 (variación del VAN ante precio del mineral, tipo de cambio) | https://pages.stern.nyu.edu/~adamodar/pdfiles/classslidesMar12/cfsession13slides.pdf | primaria | 3 | 1 | 2 | 2 | [L] parcial |

**Afirmaciones**
- OpenStax no trata sensibilidad, escenarios ni Monte Carlo. 16.6 los sustituye por un perfil de VAN (https://openstax.org/books/principles-finance/pages/16-6-using-excel-to-make-company-investment-decisions). El perfil muestra cuánto puede equivocarse la tasa antes de que cambie la decisión. Frase literal: "a company may use an NPV profile to see how sensitive their decisions are to changes in financing costs."
- Damodaran, en la Sesión 13, enumera las fuentes de incertidumbre ("Revenues may be over estimated", "Actual costs may be higher than estimated costs", "Tax rates may go up", "Interest rates may rise") y muestra gráficos de VAN según precio del mineral y tipo de cambio. Los gráficos no son legibles en el texto extraído, así que solo puedo confirmar el planteo.
- Uso en la práctica (Graham y Harvey 2002): análisis de sensibilidad aparece en la Figura 1, pero las cifras de las barras no se extraen del PDF. "14% always or almost always used value at risk or some other form of simulation", "12% used a profitability index", "11% used adjusted present value". "more than one-fourth of the companies claimed to be using real options (RO) evaluation techniques". Los autores aclaran que el uso dominante de opciones reales probablemente es cualitativo, como herramienta de planeamiento estratégico.
- Graham 2022, Tabla I (porcentaje que usa "siempre o casi siempre", encuesta 2022, muestra completa distinguida por tamaño):

| Técnica | Grandes 2001 | Grandes 2022 | Chicas 2001 | Chicas 2022 |
|---|---|---|---|---|
| Análisis de escenarios | 58,67 | 68,67 | 46,38 | 51,78 |
| Simulación / VAR | 16,08 | 35,80 | 11,94 | 17,65 |
| Opciones reales | 28,03 | 37,50 | 25,63 | 40,28 |

(https://nber.org/system/files/working_papers/w29841/w29841.pdf). Aclaro que "Grandes" es facturación mayor a US$1.000 millones y "Chicas" menor, definición de Graham, no la de pyme.

**Punto de equilibrio del VAN (break-even).** No encontré una fuente primaria que lo defina. En OpenStax 16.6 el equivalente es leer en el perfil de VAN a qué tasa el VAN se hace cero: "The cost of attracting funds would have to be higher than 13.43% for the solar panel project to be rejected."

**Árbol de decisión.** Hueco: no encontré fuente leída.

**Opciones reales, en una línea (para la nota).** Es el valor de poder esperar, ampliar o abandonar un proyecto, que el VAN simple no cuenta. La fuente que verifiqué es la hipótesis de McDonald y Siegel (1986) sobre la opción de diferir, tal como la cita https://www.nber.org/papers/w16770.pdf. El texto original no lo leí.

**Recurso canónico:** no hay uno que cubra los cuatro métodos. Para un lector no financista, mi propuesta es OpenStax 16.6 (perfil de VAN, porque es el método más sencillo de rehacer) y la Tabla I de Graham 2022 para saber cuánto se usan los otros.

---

## 7. Práctica: qué usan las empresas

| Fuente | URL | Tipo | Aut | Prof | Ej | Uniq | Marca |
|---|---|---|---|---|---|---|---|
| Graham y Harvey, JACF 2002 (misma encuesta que JFE 2001, 392 CFO) | https://people.duke.edu/~charvey/Research/Published_Papers/P76_How_do_CFOs.pdf | primaria | 3 | 2 | 2 | 3 | [L] |
| Graham 2022, Journal of Finance 77(4), 1975-2049 (NBER WP 29841) | https://nber.org/system/files/working_papers/w29841/w29841.pdf | primaria | 3 | 3 | 3 | 3 | [L] parcial |
| Danielson y Scott 2006 | (no accedido) | primaria | | | | | [S] |
| Graham y Harvey 2001 (JFE 60, 187-243), versión original | DOI 10.1016/S0304-405X(01)00044-7 (no accedido) | primaria | | | | | [M] vía buscador |

**Afirmaciones**
- Encuesta de 392 CFO (Graham y Harvey, JACF 2002): "74.9% of CFOs always or almost always used NPV and 75.7% always or almost always used IRR." Las grandes usan más VAN que las chicas, "small firms tended to rely on the payback criterion". Las empresas más endeudadas, las que pagan dividendos y las públicas usan más VAN y TIR (https://people.duke.edu/~charvey/Research/Published_Papers/P76_How_do_CFOs.pdf). Reservas del propio texto: los porcentajes por subgrupo no se reportan ahí, remiten a la versión de JFE.
- Graham 2022, Tabla I (porcentaje "siempre o casi siempre", extraído del PDF):

| Técnica | Grandes 2001 | Grandes 2022 | Chicas 2001 | Chicas 2022 |
|---|---|---|---|---|
| VAN | 84,52 | 77,38 | 67,92 | 40,22 |
| TIR / tasa de corte | 84,81 | 75,00 | 68,72 | 39,67 |
| Repago | 45,89 | 63,86 | 64,29 | 66,40 |
| Índice de rentabilidad | 8,03 | 38,75 | 14,50 | 30,56 |
| Valor presente ajustado | 7,30 | 18,75 | 13,20 | 14,85 |

  Tamaños de muestra: grandes 161 (2001) y 85 (2022); chicas 217 y 376. "Among small firms (revenues < $1B), payback is far more prevalent than NPV or IRR, which written comments imply reflects constraints on funding, time, or financial sophistication." Las comparaciones por tamaño son de Graham, y "chica" acá no equivale a pyme (https://nber.org/system/files/working_papers/w29841/w29841.pdf).
- Histórico: Gitman y Forrester (1977), según Graham 2022, en unas 100 empresas muy grandes: VAN 10% como regla primaria (26% secundaria), TIR 54% (14%), tasa contable 25% (14%), repago 9% (44%). Es cita de segunda mano en Graham, no leí el original.

**Discrepancias y límites**
- La muestra de 2022 es de empresas norteamericanas de la encuesta Duke CFO, con sesgos hacia empresas más grandes que una pyme típica. Para una empresa en marcha pero no cotizante, el porcentaje de VAN en "chicas" (40%) es la cifra más cercana que tengo, con la salvedad del corte de US$1.000 millones.
- Danielson y Scott 2006: lo único que obtuve es un resumen secundario de EBSCO. Dice que estudiaron empresas de menos de 250 empleados con datos de la NFIB (https://www.ebsco.com/research-starters/business-and-management/capital-budgeting). No tengo sus cifras. Hueco.
- Latinoamérica: no encontré ninguna encuesta (la búsqueda se agotó antes de intentarlo bien). Hueco.

**Recurso canónico:** Graham 2022, sección II.A y Tabla I, porque compara 2001 con 2022 y separa por tamaño. Fijarse en que el repago supera al VAN en las empresas chicas.

---

## Huecos finales

1. **Poterba y Summers 1995:** no verificada la fuente primaria. La cifra de 12,2% real viene del WP 16770 de Jagannathan et al. ([S]). Hay que buscar el original antes de afirmar nada más.
2. **Libros de texto de referencia:** no accedí a Brealey-Myers-Allen, Berk-DeMarzo ni al capítulo 18 de OpenStax sobre flujos y pronóstico. Por eso el componente 1 depende de Damodaran, cuya Sesión 13 es una diapositiva densa pero no un texto de lectura. Para quien no es financista, el flujo de caja del proyecto queda sin un texto introductorio verificado.
3. **Impuestos y escudo fiscal de la amortización:** solo el caso Vale de Damodaran. No hay una explicación en prosa leída.
4. **Costo de oportunidad de un activo propio que se usa, efectos colaterales, nominal vs real:** solo el índice de Damodaran (Sesión 14) y la pregunta abierta de la Sesión 13. No leí las notas de clase (nyu.box.com).
5. **WACC y costo de oportunidad del capital:** sin fuente de texto leída. El ch. 15 de OpenStax es sobre CAPM (https://openstax.org/books/principles-finance/pages/15-summary). Sesiones de Damodaran 9 a 11 y 17 a 18 no abiertas.
6. **Sensibilidad, escenarios, break-even, Monte Carlo y árbol de decisión:** sin un texto leído que los explique. Solo hay frecuencias de uso (Graham) y el perfil de VAN. Opciones reales: solo mención.
7. **TREMA / MARR (ingeniería económica):** no busqué.
8. **Graham y Harvey 2001 original (JFE):** no leído. Las cifras salen de JACF 2002, que dice ser la misma encuesta, y de la Tabla I de Graham 2022.
9. **Jagannathan et al. 2016 (JFE):** solo abstract [M]. Las cifras del WP 2011 y de Graham 2022 no son lo mismo que el paper publicado. La media de 15,1% sale de un resumen del buscador y no la verifiqué.
10. **Danielson y Scott 2006:** solo referencia secundaria. **Encuestas de Latinoamérica y de pymes:** sin fuentes.
11. **Calidad de las citas de OpenStax:** pasaron por un extractor. Cotejar contra la página antes de publicar frases entre comillas.