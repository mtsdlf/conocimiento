# Investigación: Contabilidad, vertical Estados contables

Fecha de la investigación: 2026-11-27. Marcas de lectura: [L] texto completo, [M] metadatos o abstract, [S] resumen secundario o del buscador. Aclaración de método: las páginas web se leyeron con una herramienta que devuelve un resumen hecho por un modelo, no el texto crudo. Por eso toda página HTML está marcada [S] aunque se haya abierto entera. Solo los PDF que bajé y extraje con `pdftotext` llevan [L] (y digo si fue parcial). Puntajes 1 a 3: Aut(oridad), Prof(undidad), Ej(emplos), Uni(cidad), Rec(encia, solo en lo normativo).

## Sobre la división del árbol

La división propuesta (entrada, balance, resultados, flujo de efectivo, ajustes de cierre, normas, normas en Argentina) coincide con cómo el campo parte el tema: NIC 1 define el "juego completo" y cada estado tiene su norma o capítulo. Tres observaciones:

1. **"Ajustes de cierre" no es un estado.** Es el puente entre el libro diario y los estados (ciclo contable). En los libros de texto va con "ciclo contable", no con "estados". Conviene que la nota enlace a la vertical de registro, y que esta solo diga cómo se registra el ajuste.
2. **El estado de cambios en el patrimonio neto falta como componente.** NIC 1 lo exige en el juego completo (ver abajo). Propongo meterlo como sección de la entrada `estados-contables`, o como componente propio chico. Sin él no cierra "cómo se conectan los estados" (resultado del período, dividendos y aportes llegan al patrimonio del balance).
3. **Las notas (revelaciones) también integran el juego completo.** Mismo tratamiento: sección en la entrada.
4. **Riesgo de caducidad:** NIIF 18 reemplaza a NIC 1 para períodos anuales desde el 1 de enero de 2027. Las notas de balance y resultados deberían decir "NIC 1 hoy, NIIF 18 desde 2027" en una sección corta, porque cambia la estructura del estado de resultados.
5. **Argentina:** el nombre de los estados cambia con la RT 54 (ver el componente 7). La nota agnóstica no debe depender de esos nombres.

---

## 1. estados-contables (entrada)

### Fuentes

| # | Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|---|
| 1.1 | IFRS Foundation, página de NIC 1 | https://www.ifrs.org/issued-standards/list-of-standards/ias-1-presentation-of-financial-statements/ | primaria | 3 | 1 | 1 | 3 | [S] |
| 1.2 | IFRS Foundation, Marco Conceptual | https://www.ifrs.org/issued-standards/list-of-standards/conceptual-framework/ | primaria | 3 | 1 | 1 | 3 | [S] |
| 1.3 | OpenStax, 5.4 Appendix: ciclo contable completo | https://openstax.org/books/principles-financial-accounting/pages/5-4-appendix-complete-a-comprehensive-accounting-cycle-for-a-business | primaria (libro abierto) | 2 | 2 | 3 | 2 | [S] |
| 1.4 | IFRS Foundation, IFRS 18 | https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/ | primaria | 3 | 1 | 1 | 3 | [S] (Rec 3) |

### Afirmaciones

- NIC 1 "sets out overall requirements for the presentation of financial statements" (1.1).
- Un juego completo incluye "a statement of financial position as at the end of the period", "a statement of profit and loss and other comprehensive income for the period", "a statement of changes in equity for the period", "a statement of cash flows for the period" y "notes, comprising a summary of significant accounting policies and other explanatory information"; más, en ciertos casos (reexpresión retroactiva o reclasificación), un tercer estado de situación al comienzo del período comparativo anterior (1.1).
- El Marco Conceptual dice que ayuda a que las normas den "useful information for investors, lenders and other creditors". Se emitió en septiembre de 2010 y se revisó en marzo de 2018 (1.2). El objetivo textual y los usuarios primarios no aparecieron en el resumen (hueco: leer el capítulo 1 del Marco).
- IFRS 18 "replaces IAS 1" y "is effective for annual reporting periods beginning on or after 1 January 2027, with earlier application permitted" (1.4).

### Ejemplo con números

Clip'em Cliff, agosto de 2019 (OpenStax 1.3): ingresos totales $10.650 (servicios $10.300, intereses $350); gastos totales $10.625; resultado neto $25. Estado de resultados acumulados: saldo inicial $0, más $25, menos dividendos $150, saldo final -$125. Balance: activo total $80.875; pasivo total $11.000; patrimonio $69.875; pasivo más patrimonio $80.875. Balance de comprobación sin ajustar $87.900; ajustado $94.150. Lo que muestra la conexión: el resultado ($25) y los dividendos ($150) mueven el patrimonio del balance (-$125 en resultados acumulados), y el balance cierra (80.875 = 11.000 + 69.875). Nota: OpenStax usa "estado de resultados acumulados" y no "estado de cambios en el patrimonio neto"; para el árbol conviene el segundo.

### Recurso canónico

OpenStax cap. 5.4 (el ciclo completo con estados encadenados, para ver cómo cierran) y la página de NIC 1 de IFRS Foundation (lista literal del juego completo). Fijarse en el orden: resultado, patrimonio, balance, luego flujo.

---

## 2. balance (estado de situación patrimonial)

### Fuentes

| # | Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|---|
| 2.1 | IFRS Foundation, NIC 1 | (ver 1.1) | primaria | 3 | 1 | 1 | 3 | [S] |
| 2.2 | BDO, nota técnica sobre clasificación de préstamos corriente/no corriente, junio de 2026 | https://www.bdo.global/getmedia/b8866082-2b56-4ed8-9df2-600f56d20d1a/IFRS-IP_Classification-of-loans-as-current-or-non-current_June-2026.pdf?ext=.pdf | secundaria | 2 | 2 | 2 | 1 | [S] |
| 2.3 | KPMG, enmiendas a NIC 1 sobre pasivos corrientes | https://kpmg.com/us/en/articles/2024/current-noncurrent-classification-liabilities-ias-amendments.html | secundaria | 2 | 2 | 1 | 1 | [S] |
| 2.4 | OpenStax, cap. 5 (secciones clasificadas del balance) | https://openstax.org/books/principles-financial-accounting/pages/5-4-appendix-complete-a-comprehensive-accounting-cycle-for-a-business | primaria | 2 | 2 | 3 | 2 | [S] |

### Afirmaciones

- Criterio de no corriente: el derecho a diferir la cancelación "for at least twelve months after the reporting period" (reformas de 2020, resumidas en 2.3 y 2.2). La intención de la gerencia no cambia la clasificación (2.3). Las enmiendas rigen para períodos anuales desde el 1 de enero de 2024 (2.3).
- De los convenios (covenants) solo afectan la clasificación los que se deben cumplir en o antes de la fecha de cierre; los posteriores se revelan (2.3). La página de NIC 1 cita las enmiendas de octubre de 2022 "Non-current Liabilities with Covenants" (2.1).
- BDO sostiene que los requisitos de clasificación son "completely identical" entre NIC 1 e IFRS 18 (2.2), una sola fuente, secundaria.
- El texto literal de los párrafos 66 y 69 de NIC 1 no se pudo leer: la versión HTML del estándar exige suscripción (IFRS Digital). **Hueco**.
- Estructura clásica del balance de OpenStax (ejercicios del cap. 5): activo corriente, propiedad, intangibles, otros activos, pasivo corriente, pasivo a largo plazo, patrimonio (2.4, vía el buscador). Capital de trabajo es activo corriente menos pasivo corriente (OpenStax índice, vía buscador).

### Ejemplo con números

Balance de Clip'em Cliff al 31/8/2019 (1.3): activo $80.875, pasivo $11.000, patrimonio $69.875. Es la identidad A = P + PN con cifras de fuente.

### Recurso canónico

NIC 1 párrafos 54 a 80A (hay que acceder por suscripción o por un texto oficial traducido; en su defecto OpenStax cap. 5). Fijarse en el criterio de los doce meses y en el ciclo normal de operación, que es lo que un sistema de gestión tiene que modelar al clasificar cuentas.

---

## 3. estado-de-resultados

### Fuentes

| # | Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|---|
| 3.1 | IFRS Foundation, IFRS 18 | (ver 1.4) | primaria | 3 | 1 | 1 | 3 | [S] (Rec 3) |
| 3.2 | OpenStax 6.6, estados de resultados de un solo paso y de varios pasos | https://openstax.org/books/principles-financial-accounting/pages/6-6-describe-and-prepare-multi-step-and-simple-income-statements-for-merchandising-companies | primaria | 2 | 2 | 3 | 2 | [S] (solo extractos del buscador) |
| 3.3 | CPCE Salta, "La presentación del estado de resultados en el marco de la RT 54 (T.O. RT 59)" | https://www.consejosalta.org.ar/wp-content/uploads/La-presentacion-del-estado-de-resultados-en-el-marco-de-la-RT-54-t.-o.-RT-59.pdf | secundaria | 2 | ? | ? | 2 | no leída; solo el título apareció |

### Afirmaciones

- IFRS 18 pide "two new defined subtotals in the statement of profit or loss": resultado operativo y resultado antes de financiación e impuestos (3.1). Mueve párrafos de NIC 1 a NIC 8 y NIIF 7 y suma medidas de desempeño definidas por la gerencia (3.1).
- Formato de varios pasos: separa costo de ventas de gastos operativos, da margen bruto y resultado operativo, y aparte otros ingresos y gastos. El de un solo paso "combine all revenues and all expenses into general categories" y no distingue operativo de no operativo (3.2, extractos).
- Análisis de gastos por naturaleza o por función (NIC 1 párrafos 99 a 105) y partidas mínimas (párrafo 82): **no verificado**, mismo bloqueo que en el componente 2. Hueco.
- Otro resultado integral: solo mención; la página de NIC 1 lo incluye en el estado "profit and loss and other comprehensive income" (1.1).

### Ejemplo con números

Clip'em Cliff, agosto de 2019 (1.3): ingresos $10.650, gastos $10.625, resultado neto $25. Es de un solo paso. Para el de varios pasos con margen bruto no conseguí cifras literales (hueco: abrir OpenStax 6.6 completo).

### Recurso canónico

OpenStax 6.6 para el formato, y la página de IFRS 18 para saber hacia dónde va. Fijarse en que "resultado operativo" hoy no está definido en NIC 1 y IFRS 18 lo define.

---

## 4. estado-de-flujo-de-efectivo

### Fuentes

| # | Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|---|
| 4.1 | IFRS Foundation, NIC 7 | https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/ | primaria | 3 | 1 | 1 | 3 | [S] |
| 4.2 | OpenStax 16.3, método indirecto | https://openstax.org/books/principles-financial-accounting/pages/16-3-prepare-the-statement-of-cash-flows-using-the-indirect-method | primaria | 2 | 3 | 3 | 2 | [S] |
| 4.3 | OpenStax 16.1, propósito del estado | https://openstax.org/books/principles-financial-accounting/pages/16-1-explain-the-purpose-of-the-statement-of-cash-flows | primaria | 2 | 2 | 2 | 2 | [S] |

### Afirmaciones

- NIC 7: el estado muestra "how an entity's cash and cash equivalents changed during the period" (4.1).
- Operación: "the principal revenue-producing activities of the entity". Inversión: "the acquisition and disposal of long-term assets and other investments not included in cash equivalents". Financiación: "activities that result in changes in the size and composition of the contributed equity and borrowings of the entity" (4.1).
- Método directo: "major classes of gross cash receipts and gross cash payments". Indirecto: parte de "profit or loss" y lo ajusta por "the effects of transactions of a non-cash nature" y variaciones del capital de trabajo (4.1).
- Las transacciones de inversión y financiación sin efectivo se excluyen del estado y se revelan aparte (4.1; en OpenStax, el ejemplo del terreno comprado con un pagaré de $20.000, 4.2).
- Una enmienda de 2024, junto con NIIF 18, hace que el indirecto parta del resultado operativo y cambia la clasificación de intereses y dividendos (4.1).
- Por qué difieren resultado y caja: "cash flows often differ significantly from accrual basis net income". Ejemplo: Amazon reportó una pérdida de unos $720 millones en 2019 y su caja subió más de $91 millones (4.3).
- El método solo cambia la sección operativa; inversión y financiación se arman igual (4.2).

### Ejemplo con números (conciliación resultado a caja, método indirecto, Propensity Company, 2018, OpenStax 4.2)

| Concepto | $ |
|---|---|
| Resultado neto | 4.340 |
| Depreciación | +14.400 |
| Ganancia por venta de activos | -4.800 |
| Disminución de cuentas a cobrar | +4.500 |
| Aumento de seguros pagados por adelantado | -700 |
| Aumento de inventario | -2.500 |
| Disminución de cuentas a pagar | -1.800 |
| Aumento de sueldos a pagar | +400 |
| Total de ajustes | 9.500 |
| **Flujo operativo** | **13.840** |
| Inversión: venta de terreno +14.800; compra de activos -60.000 | -45.200 |
| Financiación: pagarés +10.000; acciones +45.000; dividendos -440 | +54.560 |
| **Variación neta de caja** | **+23.200** (de 24.300 al 31/12/2017 a 47.500 al 31/12/2018) |

Control: 4.340 + 9.500 = 13.840; -60.000 + 14.800 = -45.200; 10.000 + 45.000 - 440 = 54.560; suma 23.200. **Discrepancia dentro de la propia fuente:** el texto narrativo de OpenStax da inversión ($25.200) y financiación $34.560, mientras el estado muestra ($45.200) y $54.560; la aritmética respalda el estado. Usar las cifras del estado y avisar.

### Recurso canónico

OpenStax 16.3 (ejemplo completo con la conciliación) y la página de NIC 7 para las definiciones. Fijarse en que cada partida de capital de trabajo cambia de signo según sea activo o pasivo.

---

## 5. ajustes-de-cierre

### Fuentes

| # | Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|---|
| 5.1 | OpenStax 4.3, asientos de ajuste | https://openstax.org/books/principles-financial-accounting/pages/4-3-record-and-post-the-common-types-of-adjusting-entries | primaria | 2 | 3 | 3 | 2 | [S] |
| 5.2 | OpenStax 4.2, el proceso de ajuste | https://openstax.org/books/principles-financial-accounting/pages/4-2-discuss-the-adjustment-process-and-illustrate-common-types-of-adjusting-entries | primaria | 2 | 2 | 2 | 1 | [S] (extractos del buscador) |
| 5.3 | OpenStax 5.1, asientos de cierre | https://openstax.org/books/principles-financial-accounting/pages/5-1-describe-and-prepare-closing-entries-for-a-business | primaria | 2 | 3 | 3 | 2 | [S] (extractos del buscador) |

Nota de unicidad: las tres son capítulos del mismo libro; cuentan como una sola fuente para efectos de corroboración. No encontré una segunda fuente independiente para este componente (es conocimiento estándar, riesgo bajo, pero el árbol pide dos para lo normativo; esto no es normativo).

### Afirmaciones

- Un ajuste hace falta porque no toda transacción genera un documento fuente; no significa que hubo un error (5.2).
- "Every adjusting entry includes at least one income statement account and one balance sheet account, and Cash never appears in one" (5.2, 5.1).
- El balance de comprobación ajustado lista las cuentas con saldo distinto de cero después de contabilizar los ajustes y ayuda a detectar errores de cálculo de los pasos previos (5.2).
- Cierre: cuatro asientos. Ingresos a Resumen de resultados, gastos a Resumen de resultados, Resumen a Resultados acumulados, dividendos a Resultados acumulados (5.3). Las cuentas temporales vuelven a cero; el balance de comprobación posterior al cierre solo debe tener cuentas permanentes (5.3).
- La distinción previsiones/provisiones y amortizaciones del período está cubierta por la depreciación (5.1 abajo); **la distinción de vocabulario rioplatense (previsión = corrección de un activo, provisión = pasivo incierto) no apareció en ninguna fuente**. Hueco, y se resuelve con las normas locales o NIC 37 (no investigada).

### Ejemplo con números (Printing Plus, enero, OpenStax 5.1)

1. Ingreso devengado: Intereses a cobrar $140 / Ingresos por intereses $140.
2. Gasto pagado por adelantado: se compraron suministros por $500 y se usaron $100. Gasto de suministros $100 / Suministros $100. Saldo restante $400.
3. Depreciación: $75. Gasto por depreciación $75 / Depreciación acumulada $75.
4. Ingreso diferido: un cliente pagó $4.000 por adelantado el 9 de enero; hasta el 31 se prestaron servicios por $600. Ingreso diferido $600 / Ingresos por servicios $600. Saldo restante $3.400.
5. Gasto devengado: $1.500 de sueldos del 21 al 31 de enero sin pagar. Gasto de sueldos $1.500 / Sueldos a pagar $1.500.

Cierre de enero: el saldo de Resumen de resultados queda en $4.665 acreedor, "the same figure as what is reported on Printing Plus's Income Statement" (5.3).

### Recurso canónico

OpenStax 4.3 (los cinco ajustes con cifras) y 5.1 (cierre). Fijarse en la regla "una cuenta de resultado más una patrimonial, nunca caja": es lo que un sistema puede validar.

---

## 6. normas-contables

### Fuentes

| # | Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Marca |
|---|---|---|---|---|---|---|---|---|
| 6.1 | IFRS Foundation, NIIF para las PYMES | https://www.ifrs.org/issued-standards/ifrs-for-smes/ | primaria | 3 | 1 | 1 | 3 | [S] (Rec 3) |
| 6.2 | IFRS Foundation, NIIF 10 | https://www.ifrs.org/issued-standards/list-of-standards/ifrs-10-consolidated-financial-statements/ | primaria | 3 | 1 | 1 | 3 | [S] |
| 6.3 | IFRS Foundation, Marco Conceptual | (ver 1.2) | primaria | 3 | 1 | 1 | 3 | [S] |
| 6.4 | IFRS Foundation, NIC 29 | https://www.ifrs.org/issued-standards/list-of-standards/ias-29-financial-reporting-in-hyperinflationary-economies/ | primaria | 3 | 1 | 1 | 3 | [S] |

### Afirmaciones

- La norma para PYMES "reflects five types of simplifications from full IFRS Accounting Standards": omite temas, restringe opciones de política, simplifica reconocimiento y medición, y pide menos revelaciones (6.1). Se "updated in February 2025" y la nueva edición es "effective for periods beginning on or after 1 January 2027"; se puede aplicar antes o seguir con la edición de 2015 hasta entonces (6.1). Quién califica como PYME: la página no lo dice (la definición es de cada jurisdicción; **hueco**, ver Sección 36 y la definición de "entidad sin responsabilidad pública de rendir cuentas").
- NIIF 10 "establishes principles for presenting and preparing consolidated financial statements", y toma el control como base de la consolidación (6.2). La definición literal de control no apareció (hueco). Nivel de divulgación: un grupo presenta estados consolidados como si fuera una sola entidad.
- Quién emite: el IASB (IFRS Foundation) emite las NIIF y el Marco (6.3). Las normas locales las emite cada país; ver componente 7.
- Marco Conceptual: septiembre de 2010, revisado en marzo de 2018 (6.3).
- NIC 29 aplica a "any entity whose functional currency is the currency of a hyperinflationary economy"; indicador: "cumulative inflation over three years of around 100 per cent or more"; reexpresar "using the change in a general price index" (6.4). La mención entra aquí en una línea; el detalle argentino va en el componente 7.

### Ejemplo con números

No encontré un ejemplo numérico de consolidación en fuentes primarias dentro de las rondas disponibles. **Hueco**: OpenStax no tiene un capítulo de consolidación en Volumen 1 (verificar en Volumen 2 / Intermediate). Para NIIF 10 la nota puede quedarse en divulgación, como pide el encargo.

### Recurso canónico

Las cuatro páginas de ifrs.org, cada una de una frase. Para el estudio profundo, el texto completo del estándar (de pago en ifrs.org). Fijarse en la fecha de vigencia 1 de enero de 2027 de la edición 2025 de la norma PYMES.

---

## 7. normas-contables-en-argentina

Es lo normativo vigente: alto riesgo. Estado de la corroboración por afirmación entre paréntesis.

### Fuentes

| # | Fuente | URL | Tipo | Aut | Prof | Ej | Uni | Rec | Marca |
|---|---|---|---|---|---|---|---|---|---|
| 7.1 | FACPCE, "Montos de los ingresos... Entidad pequeña y mediana" (dic 2022 / ago 2026; T.O. RT 62) | https://www.facpce.org.ar/wp-content/uploads/2026/09/Indice-y-actualizacion-ingresos-RT54-2026-08.pdf | primaria | 3 | 2 | 3 | 3 | 3 | [L] (3 páginas, texto extraído) |
| 7.2 | FACPCE, Resolución JG 660/26 | https://www.facpce.org.ar/wp-content/uploads/2026/03/Resolucion-JG-N-660-26-Dispensa-transitoria.pdf | primaria | 3 | 2 | 1 | 3 | 3 | [L] (primeras páginas) |
| 7.3 | CPCE Santa Fe 2, "Entrada en vigencia" (ene 2026) | https://www.cpcesfe2.org.ar/wp-content/uploads/2026/01/2-entrada-en-vigencia.pdf | secundaria (consejo local) | 2 | 1 | 1 | 2 | 3 | [L] |
| 7.4 | CPCE Córdoba / Consejo Profesional CABA (consejo.org.ar), micrositio RT 54 (T.O. RT 59 y mod.) | https://consejo.org.ar/micrositios-profesionales/rt-54-norma-unificada-argentina-de-contabilidad | secundaria | 2 | 1 | 1 | 2 | 3 | [S] |
| 7.5 | CPCECABA, "Todo sobre la RT 54" | https://web.cpcecba.org.ar/todo-sobre-la-rt-54/ | secundaria | 2 | 1 | 1 | 2 | 3 | [S] |
| 7.6 | iProfesional, nota sobre la RT 54 (artículo de 30/09/2022) | https://www.iprofesional.com/impuestos/370445-nueva-norma-contable-para-contadores-auditores-y-empresas | secundaria (prensa), fechada | 1 | 1 | 1 | 1 | 1 (desactualizada) | [S] |
| 7.7 | KPMG Argentina, "Qué es la NUA" (ago 2025) | https://kpmg.com/ar/es/home/insights/2025/08/que-es-la-nua-2.html | secundaria | 2 | 1 | 1 | 1 | 2 | [S] |
| 7.8 | CNV, Resolución General 562 (29/12/2009) | https://www.cnv.gov.ar/descargas/marcoregulatorio/blob/8e3200d6-57ed-4403-84e7-6199edb9048d | primaria | 3 | 2 | 1 | 3 | 2 | [L] (extracción parcial: considerandos y arts. 1 y 2) |
| 7.9 | CPCECABA, nota sobre Res. JG 539/18 (CPCE Córdoba adopta con Res. 69/18) | https://web.cpcecba.org.ar/?p=32942 | secundaria | 2 | 2 | 1 | 2 | 2 | [S] |
| 7.10 | Deloitte IFRS in Focus (traducción), 1 de julio de 2018, Inflación en Argentina | https://iasplus.com/content/cc047ddc-7fb6-45fb-b10b-c31f34629236 | secundaria | 2 | 2 | 1 | 2 | 2 | [L] parcial (grep del texto) |
| 7.11 | Consejo Profesional (consejo.org.ar), micrositio ajuste por inflación | https://consejo.org.ar/micrositios-profesionales/ajuste-por-inflacion | secundaria | 2 | 1 | 1 | 1 | 3 | [S] |
| 7.12 | FACPCE, texto de la Res. JG 539/18 | https://www.facpce.org.ar/web2014/pdf/RESJG539-18.pdf | primaria | 3 | 3 | ? | 3 | ? | **no leída**: devolvió HTML/404; solo identificada por el buscador |
| 7.13 | CNV, Res. 562/09 vía buscador, RT 26 | https://archivo.consejo.org.ar/noticias09/files/RT26.pdf | primaria | 3 | ? | ? | 3 | ? | **no leída** |

Conteo de independencia: 7.2 y 7.1 son de la FACPCE (una sola fuente institucional, dos documentos). 7.3, 7.4, 7.5 son consejos locales que repiten la FACPCE (una sola familia secundaria).

### Afirmaciones

**RT 54, norma unificada (NUA)**

- Aprobación: la Junta de Gobierno de la FACPCE "aprobó, en su reunión del 1 de julio de 2022, la publicación de la Resolución Técnica N° 54 'Normas Contables Profesionales: Norma Unificada Argentina de Contabilidad' [Introducción y Primera Parte]" (7.1). El 30 de junio de 2023 aprobó la RT 56, que "completó el proceso", con las mejoras a la Introducción, al Título Primero y al Glosario, el Título Segundo (normas particulares), el Título Tercero (normas específicas) y el Apéndice A (transición) (7.1). El texto ordenado figura como "T.O. RT 62" en 7.1 y como "T.O. RT 59 y mod." en 7.4, por lo que la nota debe nombrar el texto ordenado por su fecha de consulta (discrepancia de nomenclatura entre fuentes de distinta fecha).
- Vigencia según la FACPCE: "de aplicación obligatoria para la preparación de estados contables correspondientes a ejercicios iniciados a partir del 1° de julio de 2024, inclusive, sin exigir su aplicación a los períodos intermedios comprendidos en el primer ejercicio"; aplicación anticipada desde ejercicios iniciados el 1° de enero de 2023 (7.1). La misma fuente advierte que "la versión definitiva que resulta aplicable en cada jurisdicción, que incluye a la vigencia, es la que apruebe cada CPCE" (7.1, nota 2).
- Vigencia según consejos locales (**discrepa con la FACPCE**): Santa Fe, "para los ejercicios iniciados a partir del 1 de enero de 2025" (7.3); Córdoba, "ejercicios anuales iniciados a partir del 1° de enero de 2025", con la Res. CPCE Córdoba 35/24 (7.5, 7.4); KPMG da "1 de enero de 2025 o 1 de julio de 2024, según la jurisdicción" (7.7). Tres de la familia local coinciden en 2025 y dependen de adopción local. Para la nota: dar la fecha de la FACPCE y avisar que cada consejo adoptó la suya. La nota de iProfesional (7.6) dice "ejercicios iniciados a partir del 1° de enero de 2024" y aplicación anticipada desde 2023: es del texto aprobado en 2022, superado por la RT 56 y por 7.1. Se descarta como desactualizada, pero se registra.
- Aplicación a los ejercicios cerrados desde el 31/12/2025: un recordatorio del CPCE Córdoba lo indica (visto solo en el resumen del buscador, no verificado).
- Dispensa transitoria: la Resolución JG 660/26, del 27 de marzo de 2026, otorga "con carácter excepcional y transitorio, una dispensa limitada en materia de presentación (exposición) de la información contenida en el cuerpo de los estados contables básicos mencionados en los incisos a) al d) del párrafo 32 y en los incisos a) al d) del párrafo 785 de la Resolución Técnica N° 54, sin que ello implique una dispensa respecto del cumplimiento de los restantes requerimientos" (7.2). Art. 3°: "aplicable solo a la preparación de estados contables correspondientes a ejercicios iniciados a partir del 1 de enero de 2025, que constituyan los primeros preparados de acuerdo con la Resolución Técnica N° 54" (7.2). Motivo: la RT 54 "introduce modificaciones en los criterios de presentación (exposición) de los estados contables, incluyendo nuevas denominaciones y criterios de agregación o desagregación de partidas" (7.2). Que "no constituye una prórroga" lo dicen fuentes secundarias vistas en el buscador, no el texto leído; lo que sí se lee es que la dispensa es solo de presentación.
- Clasificación de entes: la RT 54 distingue entidades pequeñas, medianas y "las demás" según actividad, ingresos y control (7.5). Resolución JG 608/22 (diciembre de 2022): pequeña si en el ejercicio anterior no superó $650.000.000; mediana si superó $650.000.000 y no pasó de $3.250.000.000, en pesos de octubre de 2022 (7.1). Actualizados por el índice FACPCE: al cierre 31/12/2025, $4.861.549.242 y $24.307.746.212 (coeficiente 7,4793); y al cierre 31/05/2026, $5.506.351.295 y $27.531.756.474 (7.1; la tabla sigue hasta 2026-08 en la fuente).
- La Interpretación 18 trae guía para aplicar los párrafos 6 y 7 (7.1, nota 3).
- **Qué normas reemplaza la RT 54: las fuentes discrepan.** iProfesional (2022) dice derogadas por completo las RT 6, 7, 8, 9, 11, 17, 41, 42 y 48, y parcialmente la 18 y la 21 (7.6). Una presentación de un consejo (vista por el buscador) da ocho: 6, 8, 9, 11, 17, 41, 42 y 48. KPMG dice que consolida las RT 16, 17, 18, 21, 22 y 26 (7.7). El micrositio del consejo dice que después de la RT 54 el marco queda en RT 54, RT 36 (Balance Social), RT 26 (adopción de NIIF y NIIF para PYMES) y RT 16 (marco conceptual para lo que no es RT 26) (7.4). La única lista que coincide con ese esquema es la de 7.6; la de KPMG contradice a 7.4 porque incluye la RT 26 y la RT 16, que 7.4 dice que siguen. **No hay texto de la FACPCE leído que enumere las derogaciones.**
- **RT 41 (entes pequeños y medianos): "si sigue".** Según 7.6 y la presentación del consejo, la RT 41 queda derogada por la RT 54, que la reemplaza con el tratamiento diferenciado de la entidad pequeña. 7.4, 7.5 y 7.7 no la mencionan o hablan del "enfoque diferencial" para entes pequeños sin citarla. Conclusión provisoria: se derogó, con baja confianza (fuentes secundarias que coinciden pero comparten origen). Hay un indicio contrario: la página de ajuste por inflación (7.11) todavía describe la segunda parte de la Res. 539/18 "bajo la RT 17 y la RT 41", pero eso es historia de 2018.

**CNV y NIIF obligatorias para cotizantes**

- Resolución General 562, de la CNV, "BUENOS AIRES, 29 de diciembre de 2009", "Adopción de Normas Internacionales de Información Financiera" (7.8). Art. 2°, que incorpora el art. 114 al Capítulo XXXI: "Para los ejercicios que se inicien a partir del 1º de enero de 2012, las entidades emisoras de acciones y/u obligaciones negociables presentarán sus estados financieros aplicando la Resolución Técnica Nº 26 de la FEDERACIÓN ARGENTINA DE CONSEJOS PROFESIONALES DE CIENCIAS ECONÓMICAS, que dispone la adopción de las Normas Internacionales de Información Financiera (NIIF) emitidas por el Consejo de Normas Internacionales de Contabilidad (IASB), y sus modificatorias. Se aceptará la aplicación anticipada para los ejercicios que se inicien a partir del 1º de enero de 2011" (7.8).
- La RT 26 se aprobó en marzo de 2009 (7.8, considerandos). Corroboración independiente de la CNV y la RT 26: solo el buscador (RG 576/10, RT 29 de 2011, RG 1115/2026 del 25/02/2026 que modifica el Título IV). **No leí el texto vigente actual de las Normas CNV**, así que la afirmación se queda en 2009/2012 y no en el estado de 2026. Una sola fuente primaria leída.

**Ajuste por inflación contable**

- Resolución JG FACPCE 539/18 aprobada el 29/09/2018 (7.9, 7.11; la FACPCE no se leyó). Se aplica a los estados contables anuales o intermedios cerrados desde el 01/07/2018 inclusive; los cerrados hasta el 30/06/2018 no se reexpresan (7.9). Hay una opción única de no ajustar los cierres entre el 31/12/2017 y el 30/06/2018 (buscador, guía FACPCE, no verificada con texto).
- Criterio: la FACPCE concluyó que la inflación acumulada de tres años superó el 100% (7.11). Deloitte, traducida: "la tasa de inflación acumulada tres años (basada en todos los índices disponibles) excedió el 100 por ciento. Esta situación ha persistido y, por consiguiente, la economía argentina debe ser considerada híper-inflacionaria" y la NIC 29 se aplica a los períodos que terminan después del 1 de julio de 2018 (7.10). La NIC 29 usa "around 100 per cent or more" (6.4). Dos fuentes independientes (FACPCE vía consejo, y Deloitte) coinciden en el criterio y la fecha.
- Obstáculo legal anterior: el Decreto 664/03 prohibía recibir información ajustada por organismos de control; la Ley 27.468 lo derogó (promulgada el 03/12/2018) y habilitó el ajuste "sujeto a la reglamentación" (7.9, [S]; el último ajuste fue al 30/09/2003 o 28/02/2003 según el decreto 1269/02 modificado). Fowler Newton (buscador): FACPCE "deja de considerar al decreto 664/03 como obstáculo". Una sola fuente leída; la fecha 03/12/2018 de la ley no tiene verificación en Infoleg.
- Serie de índices: Res. 539/18 pasó de una serie con IPIM a una empalmada con el IPC Nacional del INDEC "a partir de enero de 2017" (7.9). La FACPCE sigue publicando índices (octubre de 2026 en la planilla, 7.11; índice con base octubre 2022 en 7.1: 1.028,706).
- Modificaciones posteriores de la 539/18: Res. 553/19 y Res. 584/21 (buscador; textos sin leer).
- **Cuándo se reactivó:** el ajuste se aplica desde los cierres del 1/7/2018, con vigencia profesional desde la RT 6 (adoptada por CPCECABA con Res. 107/2018, 7.11). Hoy el cuerpo normativo del ajuste es **dudoso**: si la RT 6 fue derogada por la RT 54, el procedimiento pasó a la RT 54 (buscador: "la RT 54 describe el proceso de ajuste"), pero la FACPCE "sigue publicando índices para aplicar tanto la RT 6 como la RT 54". Sin el texto de la RT 54 no se puede decir dónde vive el procedimiento. Tampoco sé si la economía argentina sigue siendo hiperinflacionaria en 2026 bajo NIC 29 (hueco).

**IGJ**

- RG IGJ 7/2015 (aprobada el 28/07/2015) contiene "Normas de la IGJ"; el régimen contable está en el Título I, Libro IV, arts. 305 y siguientes (buscador, [S]). La RG IGJ 15/2023 reglamentó la presentación digital de estados contables de sociedades por acciones no comprendidas en el art. 299 de la ley 19.550, obligatoria desde el 01/03/2024 (buscador). Una página oficial dice que la RG IGJ 15/2024 reemplaza a la RG 7/2015, pero es ambigua y es de asociaciones civiles. **Hueco grande**: no leí ninguna norma de IGJ ni confirmé la legalización ante el consejo profesional.

### Ejemplo con números

Umbrales de la clasificación de entes (7.1): una entidad que en el ejercicio anterior facturó $4.000.000.000 en pesos de octubre de 2022 es mediana. En pesos de cierre 31/12/2025, el umbral de pequeña es $4.861.549.242, así que con $4.000.000.000 (hipótesis ilustrativa mía, no de la fuente) sería pequeña. Cálculo del propio coeficiente: 650.000.000 × 7,4793 = 4.861.545.000, que coincide con la fuente salvo redondeo del coeficiente.
Ejemplo de reexpresión (ajuste por inflación): no obtuve uno con cifras de fuente primaria. La "Guía de aplicación de las normas contables sobre ajuste por inflación (RT 6 y NIC 29)" (FACPCE, partes 1 a 4) trae ejercicios, pero no pude abrirla.

### Recurso canónico

1. FACPCE, texto ordenado de la RT 54, Título Primero (presentación de estados) y Apéndice A (transición), más la Res. JG 660/26 y la Interpretación 18. Fijarse en los párrafos 6 y 7 (clasificación) y 32 (estados básicos).
2. Para ajuste por inflación: Res. JG 539/18 (segunda parte) y la Guía de aplicación RT 6 y NIC 29 de la FACPCE.
3. Para cotizantes: RG CNV 562/09 y las Normas CNV (Título IV) vigentes.

---

## Huecos

1. **Texto de la RT 54.** No lo leí; las vigencias y derogaciones salen de la FACPCE (solo la tabla de montos y la 660/26) y de fuentes secundarias. Hay que abrir el texto ordenado en facpce.org.ar. Aquí se juega (a) qué RT deroga y si la RT 41 sigue o no, (b) dónde vive el procedimiento de ajuste por inflación, (c) los nombres de los estados.
2. **Res. JG 539/18, 553/19 y 584/21.** Los PDF oficiales devolvieron HTML o 404; solo secundarias.
3. **Vigencia local de la RT 54.** FACPCE dice 1/7/2024; Santa Fe y Córdoba dicen 1/1/2025. Falta la tabla jurisdicción por jurisdicción, y la de CABA específicamente (la página de CPCECABA que leí no daba fecha).
4. **NIC 1, párrafos 54 a 80A, 82 y 99 a 105, NIC 7 completa, NIIF 10 definición de control, Marco Conceptual cap. 1 y 2:** el texto de las normas exige suscripción a IFRS Digital; solo hay resúmenes oficiales cortos. Faltan por eso: la lista literal de criterios corriente/no corriente, por naturaleza vs por función, otro resultado integral y la definición de control.
5. **Ejemplos con números** que faltan en fuente: estado de resultados de varios pasos con margen bruto; conciliación de patrimonio; consolidación (NIIF 10); reexpresión por inflación.
6. **Previsiones vs. provisiones** (vocabulario rioplatense y NIC 37): sin fuente.
7. **CNV vigente 2026** (RG 1115/2026 y Normas Título IV) e **IGJ** (RG 7/2015, 15/2023, 15/2024): sin texto leído. Tampoco la legalización por los consejos profesionales.
8. **Estado actual de hiperinflación en Argentina bajo NIC 29** (si se sigue aplicando en 2026): no se encontró.
9. **Ley 27.468 y Decreto 664/03:** sin verificar en Infoleg (los links de Infoleg no se probaron).
10. **Fecha de la RT 41 y su sucesión exacta**, y **si la RT 41 "sigue"**: sin confirmación primaria.
11. **Limitación del método:** las páginas HTML llegaron como resúmenes de un modelo; las citas literales entre comillas de esas páginas pueden estar mediadas. Conviene recitar contra la página antes de publicar cualquier cita de ifrs.org u OpenStax.
