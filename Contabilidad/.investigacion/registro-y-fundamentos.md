# Investigación: vertical Registro y Fundamentos (Contabilidad)

Fecha de la búsqueda: 2026-11-27. Alcance: registro-contable, partida-doble, plan-de-cuentas, asiento-y-libros, devengado, cuentas-corrientes, libros-contables-en-argentina, Fundamentos.

Convenciones. Marcas: [L] leí el texto completo o el pasaje citado, [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1 a 3 en Autoridad / Profundidad / Ejemplos / Unicidad (A/P/E/U). Tipo: P primaria, S secundaria.

Aviso de método sobre las marcas:
- Las páginas de OpenStax las leí con WebFetch, que devuelve un extracto hecho por un modelo chico, no el HTML crudo. Las cifras y definiciones coinciden entre páginas y con los resúmenes de capítulo, pero las citas literales de OpenStax van con esa salvedad. Para publicar una cita literal conviene abrir la página.
- Los textos de la ley argentina (CCyC y Ley 19.550), el Marco Conceptual IFRS y la NIC 1 los bajé enteros y los leí como texto crudo (HTML o PDF convertido). Esas citas son literales.

## 0. Cómo divide el campo esta vertical (y dónde el árbol propuesto no coincide)

En la práctica del campo, "registro" es un ciclo, no un montón de componentes. OpenStax lo presenta como el ciclo contable: analizar la transacción, asentar en el diario, pasar al mayor, balance de sumas y saldos sin ajustar, ajustes, balance ajustado, estados, cierre, balance posterior al cierre y asientos de reversión opcionales (lista de pasos en https://openstax.org/books/principles-financial-accounting/pages/5-4-appendix-complete-a-comprehensive-accounting-cycle-for-a-business [S], vista por el buscador; el balance sin ajustar como cuarto paso, en https://openstax.org/books/principles-financial-accounting/pages/3-6-prepare-a-trial-balance [L]).

Desajustes con el árbol propuesto:
1. **devengado** no es de Registro: es una base de reconocimiento y medición. El Marco Conceptual lo trata como "financial performance reflected by accrual accounting" (párrafos 1.17 a 1.20), dentro del objetivo del reporte. Propuesta: dejarlo acá como nota puente, con enlace fuerte a reconocimiento y medición (si otra vertical lo cubre) y a cierre y ajustes. Los asientos de ajuste son el punto donde devengado y registro se tocan (OpenStax 4.1 y 4.3).
2. **cuentas-corrientes** (auxiliares de clientes y proveedores) es en los libros de texto parte de la mecánica de registro (libros auxiliares y diarios especiales, OpenStax capítulo 7, secciones 7.2 a 7.4). El aging aparece en OpenStax como técnica de estimación de incobrables (sección 9.2), o sea en la vertical de valuación de créditos o cobranzas. Propuesta: dividir. Auxiliar y cuenta de control quedan en Registro; el aging se enlaza hacia cobranzas.
3. **registro-contable (entrada)** y **partida-doble** se solapan. El campo no separa "qué es registrar" de "cómo": OpenStax lo enseña como secuencia (ecuación, T-accounts, diario). Propuesta: la entrada responde "del hecho al asiento" y partida-doble es el fundamento lógico (ecuación y reglas de débito y crédito).
4. **asiento-y-libros** mezcla tres cosas: el asiento (unidad), los libros (diario, mayor) y el control (balance de sumas, corrección). Funciona, pero la corrección ("contraasiento en lugar de borrar") es una idea que el derecho argentino sí fundamenta (CCyC 324 c) y que los libros de texto tratan aparte (hueco 3).
5. **libros-contables-en-argentina**: el CCyC no usa "libros contables" como categoría única: el art. 322 habla de "registros indispensables" (diario, inventario y balances, y otros). Conviene explicarlo en el primer párrafo de la nota.
6. Terminología trampa: **"contraasiento / reversión"** significa dos cosas. (a) Corregir un error con un asiento nuevo (CCyC 324 c). (b) Los "reversing entries" de OpenStax, asientos opcionales al inicio del período siguiente para simplificar devengamientos, que no son correcciones. La nota debe distinguirlos.

## 1. registro-contable (entrada)

### Fuentes
| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 1.1 | OpenStax Vol. 1, 3.1 principios, supuestos y conceptos | https://openstax.org/books/principles-financial-accounting/pages/3-1-describe-principles-assumptions-and-concepts-of-accounting-and-their-relationship-to-financial-statements | S (libro de texto) | 3/2/2/1 | [L] |
| 1.2 | OpenStax 3.5 asientos en el diario y T-accounts | https://openstax.org/books/principles-financial-accounting/pages/3-5-use-journal-entries-to-record-transactions-and-post-to-t-accounts | S | 3/3/3/1 | [L] |
| 1.3 | IFRS Foundation, Marco Conceptual (2018), copia PDF alojada en moodle2.units.it (el sitio IFRS pide suscripción) | https://moodle2.units.it/pluginfile.php/493397/mod_resource/content/1/conceptual-framework-for-financial-reporting.pdf | P (copia de texto oficial) | 3/2/1/3 | [L] |
| 1.4 | CCyC art. 321 (ver sección 8) | https://servicios.infoleg.gob.ar/infolegInternet/anexos/235000-239999/235975/texact.htm | P | 3/2/1/3 | [L] |

### Afirmaciones
- "A journal is the first place information is entered into the accounting system." Se lo llama libro de registro original. Fuente 1.2.
- "Posting refers to the process of transferring data from the journal to the general ledger." Fuente 1.2.
- El hecho que se registra se define por sus efectos sobre recursos y obligaciones. Un activo es "a present economic resource controlled by the entity as a result of past events" (4.3); un pasivo, "a present obligation of the entity to transfer an economic resource as a result of past events" (4.26). Fuente 1.3.
- Principios que condicionan qué y cómo se registra (OpenStax 3.1): "recognize revenue in the period in which it is earned"; la empresa en marcha "assumes a business will continue to operate in the foreseeable future"; unidad monetaria; costo histórico. Fuente 1.1 (citas parciales vía extractor).
- La ley argentina exige: "Los asientos deben respaldarse con la documentación respectiva" (CCyC 321). Fuente 1.4. Sostiene la idea "del comprobante al asiento".

### Ejemplo con números
Ver sección 2: el 5 de enero Printing Plus compra un equipo por 3,500 a crédito; el asiento es Débito Equipment 3,500 / Crédito Accounts Payable 3,500 (fuente 1.2).

### Recurso canónico
OpenStax Vol. 1 capítulo 3 entero (3.1 a 3.6): recorre hecho, asiento, mayor y balance con una sola empresa de ejemplo (Printing Plus). Fijarse en la progresión 3.4 (ecuación), 3.5 (asiento), 3.6 (balance), y en que todo sale del mismo conjunto de transacciones.

## 2. partida-doble

### Fuentes
| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 2.1 | OpenStax 3.2 ecuación expandida | https://openstax.org/books/principles-financial-accounting/pages/3-2-define-and-describe-the-expanded-accounting-equation-and-its-relationship-to-analyzing-transactions | S | 3/3/2/1 | [L] |
| 2.2 | OpenStax 3.4 análisis con la ecuación | https://openstax.org/books/principles-financial-accounting/pages/3-4-analyze-business-transactions-using-the-accounting-equation-and-show-the-impact-of-business-transactions-on-financial-statements | S | 3/3/3/1 | [L] |
| 2.3 | OpenStax 3.5 (saldos normales, asientos) | URL de 1.2 | S | 3/3/3/1 | [L] |
| 2.4 | Marco Conceptual IFRS, capítulo 4 | URL de 1.3 | P | 3/3/1/3 | [L] |
| 2.5 | OpenStax glosario capítulo 3 | https://openstax.org/books/principles-financial-accounting/pages/3-key-terms | S | 2/1/1/1 | [S] |

### Afirmaciones
- Ecuación: Assets = Liabilities + Equity (OpenStax 2.1; 3.1 la presenta como "Assets = Liabilities + Owner's Equity").
- Ecuación expandida: el patrimonio neto se abre en capital (common stock), dividendos, ingresos y gastos (fuente 2.1).
- "Equity is the residual interest in the assets of the entity after deducting all its liabilities." (4.63). Ingreso: "increases in assets, or decreases in liabilities, that result in increases in equity, other than those relating to contributions from holders of equity claims" (4.68). Gasto: lo inverso (4.69). Fuente 2.4. Muestra que ingresos y gastos son variaciones del patrimonio neto, por eso la partida doble los trata como cuentas de patrimonio.
- Doble entrada: el glosario dice que exige que la suma de los débitos sea igual a la suma de los créditos en cada transacción (fuente 2.5 [S]).
- Reglas de saldo (fuente 2.3): activos suben con débitos; pasivos suben con créditos; capital sube con crédito; dividendos son débito y reducen el patrimonio; ingresos suben con créditos; gastos suben con débitos. Formato: fecha, débitos primero, créditos indentados, "Total debits must equal total credits", explicación breve.
- Asiento simple (una cuenta deudora y una acreedora) frente a compuesto (más de una en alguna columna): OpenStax 3.5, visto por buscador [S].
- Contracuenta: "An account is a contra account if its normal balance is opposite of the normal balance of the category to which it belongs." Fuente 2.1.
- Eco legal argentino: CCyC 321 pide poder individualizar "las operaciones y las correspondientes cuentas acreedoras y deudoras"; LGS art. 61 lo repite. Ver sección 8.

### Ejemplo con números (fuente 2.2, Printing Plus, enero de 2019)
| # | Hecho | Activo | Pasivo | Patrimonio neto |
|---|---|---|---|---|
| 1 | Emite acciones por $20,000 en efectivo | +20,000 Cash | | +20,000 Common Stock |
| 2 | Compra equipo a crédito $3,500 | +3,500 Equipment | +3,500 Accounts Payable | |
| 3 | Cobra $4,000 por adelantado | +4,000 Cash | +4,000 Unearned Revenue | |
| 4 | Presta servicios por $5,500, facturados | +5,500 Accounts Receivable | | +5,500 Revenues |
| 5 | Paga luz $300 | -300 Cash | | -300 Expenses |
| 6 | Distribuye dividendos $100 | -100 Cash | | -100 Dividends |

Totales de la fuente: Activo $32,600 (Cash 23,600; A/R 5,500; Equipment 3,500); Pasivo $7,500; Patrimonio neto $25,100; "Liabilities + Equity = $32,600".

Los mismos hechos como asientos (fuente 2.3): 3 de enero Débito Cash / Crédito Common Stock 20,000; 5 de enero Débito Equipment / Crédito Accounts Payable 3,500; 9 de enero Débito Cash / Crédito Unearned Revenue 4,000; 10 de enero Débito Accounts Receivable / Crédito Service Revenue 5,500; 12 de enero Débito Utility Expense / Crédito Cash 300; 14 de enero Débito Dividends / Crédito Cash 100.

### Recurso canónico
OpenStax 3.4 junto con 3.5: primero la ecuación sin débito ni crédito, después las reglas. Fijarse en que cada hecho cambia al menos dos filas y la ecuación sigue cerrando. Para quien construye software, la invariante es "suma de débitos = suma de créditos" por asiento.

## 3. plan-de-cuentas

### Fuentes
| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 3.1 | OpenStax 3.2 (Tabla 3.2, numeración) | URL de 2.1 | S | 3/2/3/1 | [L] |
| 3.2 | OpenStax glosario capítulo 3 | https://openstax.org/books/principles-financial-accounting/pages/3-key-terms | S | 2/1/1/1 | [S] |
| 3.3 | OpenStax 3.5 (códigos del ejemplo) | URL de 1.2 | S | 3/2/3/1 | [L] |

### Afirmaciones
- Tabla 3.2 de OpenStax: activos 100 a 199 (empresa chica) y 1000 a 1999 (grande); pasivos 200-299 / 2000-2999; patrimonio neto 300-399 / 3000-3999; ingresos 400-499 / 4000-4999; gastos 500-599 / 5000-5999. "We call this account numbering system a chart of accounts." Una empresa grande de comercio o manufactura puede usar números que empiezan con 6. Fuente 3.1.
- Las cuentas se presentan "in the order in which they appear on the financial statements": primero las patrimoniales y después las de resultado (esa frase, vía buscador [S]; la tabla sí [L]).
- Códigos de ejemplo (fuente 3.3): Cash 101, Accounts Receivable 111, Accounts Payable 201, Common Stock 301.
- Glosario: plan de cuentas como "account numbering system that lists all the accounts a business uses in its day-to-day transactions" (fuente 3.2 [S]).
- Lo de "qué no meter en el plan (dimensiones o auxiliares)" no lo cubre OpenStax ni la norma. Lo que sí hay son los auxiliares por cliente y proveedor (sección 6), que dejan el plan chico y llevan el detalle fuera. Dimensiones analíticas (centro de costo, proyecto): hueco 2.

### Ejemplo con números
La tabla de numeración y los códigos de arriba. Saldos del mayor de Printing Plus al cierre de enero de 2019 (fuente 1.2): Cash 24,800 deudor; A/R 1,200; Supplies 500; Equipment 3,500; A/P 500 acreedor; Unearned Revenue 4,000; Common Stock 20,000; Service Revenue 9,500; Dividends 100; Salaries Expense 3,600; Utility Expense 300.

### Recurso canónico
OpenStax 3.2, Tabla 3.2. Es corta. Fijarse en que el primer dígito identifica el rubro y en la diferencia entre 3 y 4 dígitos (espacio para crecer). Para lo exigible en Argentina: CCyC 322 c) pide registros "que corresponden a una adecuada integración de un sistema de contabilidad".

## 4. asiento-y-libros

### Fuentes
| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 4.1 | OpenStax 3.5 | URL de 1.2 | S | 3/3/3/1 | [L] |
| 4.2 | OpenStax 3.6 balance de sumas y saldos | https://openstax.org/books/principles-financial-accounting/pages/3-6-prepare-a-trial-balance | S | 3/3/3/1 | [L] |
| 4.3 | CCyC arts. 322 a 327 | URL en sección 8 | P | 3/3/1/3 | [L] |
| 4.4 | OpenStax 4.3 y apéndice 5.4 (correcting entry; reversing entries) | https://openstax.org/books/principles-financial-accounting/pages/5-4-appendix-complete-a-comprehensive-accounting-cycle-for-a-business | S | 2/1/1/1 | [S] |

### Afirmaciones
- "Recall that the general ledger is a record of each account and its balance." Se pasa del diario al mayor por posting. Fuente 4.1.
- Saldo en el mayor: se suman los movimientos del lado que aumenta, se restan los del otro y el lado mayor fija el saldo. Ejemplo: Cash con $20,000 al debe y $300 al haber da saldo deudor de $19,700. Fuente 4.1.
- "A trial balance is a list of all accounts in the general ledger that have nonzero balances." Es el cuarto paso del ciclo y en esa etapa es "sin ajustar". Fuente 4.2.
- Qué detecta: columnas desiguales ("If the two balances are not equal, there is a mistake in at least one of the columns"); un saldo en el lado equivocado (débitos 33,900 contra créditos 34,100: diferencia 200, mitad 100, el saldo de Dividends estaba al haber); una transposición (débitos 35,800 contra 34,000: diferencia 1,800 dividida por 9 da 200, Equipment 5,300 en lugar de 3,500). Qué no detecta: "We can have errors and still be mathematically in balance." Fuente 4.2.
- Corrección: CCyC 324 prohíbe "alterar el orden en que los asientos deben ser hechos", "dejar blancos que puedan utilizarse para intercalaciones o adiciones", "interlinear, raspar, emendar o tachar", y dice: "Todas las equivocaciones y omisiones deben salvarse mediante un nuevo asiento hecho en la fecha en que se advierta la omisión o el error". Fuente 4.3. Es el sustento normativo de "contraasiento, no borrar".
- Diario: CCyC 327: "En el Diario se deben registrar todas las operaciones relativas a la actividad de la persona que tienen efecto sobre el patrimonio, individualmente o en registros resumidos que cubran períodos de duración no superiores al mes. Estos resúmenes deben surgir de anotaciones detalladas practicadas en subdiarios". El Libro Caja y todo diario auxiliar "integra el Diario". Fuente 4.3.
- OpenStax distingue asiento de corrección (cuando hay que arreglar Caja) de asiento de ajuste, y ubica los reversing entries como paso opcional 10, tras el balance posterior al cierre (fuente 4.4 [S]).

### Ejemplo con números
- Balance sin ajustar de Printing Plus al 31 de enero de 2019 (fuente 4.2): Débitos: Cash 24,800; A/R 1,200; Supplies 500; Equipment 3,500; Dividends 100; Salaries Expense 3,600; Utility Expense 300; total 34,000. Créditos: A/P 500; Unearned Revenue 4,000; Common Stock 20,000; Service Revenue 9,500; total 34,000.
- Error que el balance no detecta (ejemplo de construcción propia, no de la fuente): imputar un cobro de 5,500 a Service Revenue en lugar de a A/R deja el balance cuadrado y el mayor mal. La corrección es un asiento nuevo: Débito Service Revenue 5,500 / Crédito Accounts Receivable 5,500, fechado cuando se advierte (CCyC 324 c).

### Recurso canónico
OpenStax 3.5 y 3.6 juntos, más CCyC 324 y 327 para lo normativo. Fijarse en la sección de errores del balance (reglas de dividir por 2 y por 9) y en que el libro admite que un balance cuadrado no prueba que esté bien.

## 5. devengado

### Fuentes
| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 5.1 | Marco Conceptual IFRS 1.17 a 1.21 | URL de 1.3 | P | 3/2/1/3 | [L] |
| 5.2 | NIC 1 párr. 27 y 28 (copia en moodle2.units.it) | https://moodle2.units.it/pluginfile.php/493402/mod_resource/content/1/ias-1-presentation-of-financial-statements.pdf | P (copia; versión previa a IFRS 18) | 3/2/1/3 | [L] |
| 5.3 | OpenStax 4.1 devengado frente a caja | https://openstax.org/books/principles-financial-accounting/pages/4-1-explain-the-concepts-and-guidelines-affecting-adjusting-entries | S | 3/2/2/1 | [L] |
| 5.4 | OpenStax 4.3 asientos de ajuste con cifras | https://openstax.org/books/principles-financial-accounting/pages/4-3-record-and-post-the-common-types-of-adjusting-entries | S | 3/3/3/1 | [L] |
| 5.5 | AccountingTools, "How a profitable business can run out of cash" | https://www.accountingtools.com/articles/how-a-profitable-business-can-run-out-of-cash | S (portal profesional) | 1/1/1/1 | [L] |
| 5.6 | FACPCE RT 16, texto ordenado por Res. C.D. 93/2005 (copia en consejo.org.ar) | https://consejo.org.ar/storage/attachments/06_RT%2016.pdf-KAcvYHhwSH.pdf | P (norma profesional, no ley) | 2/1/1/3 | [L] solo el pasaje de devengamiento |

### Afirmaciones
- Marco Conceptual 1.17: "Accrual accounting depicts the effects of transactions and other events and circumstances on a reporting entity's economic resources and claims in the periods in which those effects occur, even if the resulting cash receipts and payments occur in a different period." Esa información "provides a better basis for assessing the entity's past and future performance than information solely about cash receipts and payments during that period". Fuente 5.1.
- El mismo marco (1.20) dice que los flujos de caja también sirven para evaluar la capacidad de generar flujos netos, la liquidez y la solvencia: complementan el resultado devengado. Fuente 5.1.
- NIC 1.27: "An entity shall prepare its financial statements, except for cash flow information, using the accrual basis of accounting." Fuente 5.2.
- OpenStax: devengado exige que "revenues and expenses must be recorded in the accounting period in which they were earned or incurred"; base caja: "transactions are not recorded in the financial statements until there is an exchange of cash". Los principios de reconocimiento de ingresos y de gastos (matching) derivan del devengado. Fuente 5.3.
- Regla de los ajustes: cada asiento de ajuste toca una cuenta de resultado y una patrimonial y nunca Caja (resumen del capítulo 4 [S]; la tabla de 4.3 lo confirma [L]).
- Por qué una empresa con ganancia se queda sin plata (fuente 5.5, una sola fuente secundaria, sin cifras): el ingreso se registra antes del cobro ("revenue may be earned well in advance of the related cash receipt"); grandes inversiones en activos fijos que se amortizan en años; inventario inmovilizado; crédito largo a clientes mientras proveedores exigen pago rápido; sueldos, cargas, alquiler y seguros vencen antes del cobro.
- Norma argentina: la RT 16 usa "devengamiento (atribuir a cada período contable lo que le corresponde)" en un pasaje sobre el estado de cambios en la situación financiera. Fuente 5.6. No encontré el pasaje que define la base de devengado como tal (hueco 4).

### Ejemplo con números (fuente 5.4; Printing Plus, ajustes al 31 de enero de 2019)
| Tipo | Débito | Crédito | Monto |
|---|---|---|---|
| Suministros usados | Supplies Expense | Supplies | 100 (Supplies pasa de 500 a 400) |
| Depreciación del equipo comprado el 5 de enero | Depreciation Expense: Equipment | Accumulated Depreciation: Equipment | 75 |
| Ingreso diferido ganado (adelanto de 4,000 del 9 de enero) | Unearned Revenue | Service Revenue | 600 (el pasivo baja a 3,400) |
| Ingreso devengado (intereses) | Interest Receivable | Interest Revenue | 140 |
| Sueldos devengados no pagados (21 al 31 de enero) | Salaries Expense | Salaries Payable | 1,500 |

Ganancia sin caja con datos de la misma fuente: el hecho 4 de la sección 2 registra $5,500 de ingresos facturados; sube Revenues y A/R y la caja no se mueve hasta el cobro del 23 de enero (fuente 1.2). El libro de texto no lo plantea como caso de quiebra; esa lectura es mía.

### Recurso canónico
Marco Conceptual IFRS 1.17 a 1.21 (cinco párrafos, primario) más OpenStax 4.1 y 4.3. Fijarse en 1.17 (por qué el devengado es mejor base para evaluar desempeño) y en que 1.20 no descarta la caja: la complementa.

## 6. cuentas-corrientes (auxiliares)

### Fuentes
| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 6.1 | OpenStax 7.4 libro auxiliar | https://openstax.org/books/principles-financial-accounting/pages/7-4-prepare-a-subsidiary-ledger | S | 3/2/3/1 | [L] |
| 6.2 | OpenStax 7.2 y 7.3 diarios especiales | https://openstax.org/books/principles-financial-accounting/pages/7-2-describe-and-explain-the-purpose-of-special-journals-and-their-importance-to-stakeholders | S | 3/2/2/1 | [S] (título y resumen de capítulo) |
| 6.3 | OpenStax 9.2 aging | https://openstax.org/books/principles-financial-accounting/pages/9-2-account-for-uncollectible-accounts-using-the-balance-sheet-and-income-statement-approaches | S | 3/3/3/1 | [L] |
| 6.4 | CCyC 327 (subdiarios) | URL en sección 8 | P | 3/2/1/3 | [L] |

### Afirmaciones
- El libro auxiliar registra el saldo de cada cliente (cuentas a cobrar) y de cada proveedor (a pagar). La cuenta del mayor (por ejemplo Accounts Receivable) es la cuenta de control: su saldo debe coincidir con la suma de los auxiliares, y si no coincide hay un error que buscar (cita: "must agree with the balance shown in the accounts receivable general ledger account"). Fuente 6.1.
- Las ventas se pasan al auxiliar de cada cliente de forma individual y al mayor en total (resumen de capítulo [S]). Fuente 6.2.
- Aging (fuente 6.3): "accounts receivable is organized into categories by length of time outstanding"; "The longer the time passes with a receivable unpaid, the lower the probability that it will get collected". OpenStax lo usa para estimar incobrables, no como herramienta de cobranzas.
- Argentina: el diario puede llevarse con subdiarios detallados y resúmenes de hasta un mes (CCyC 327, literal). Es el anclaje legal de diarios y auxiliares.

### Ejemplo con números
- Auxiliar de clientes al 31 de enero (Store Inc., fuente 6.1): PB&J 0; Jones Co. 328; Black & White Inc. 0; Tiny Tim's Inc. 2,661; total 2,989, igual al control Accounts Receivable ($2,989). Auxiliar de proveedores: D & D Inc. 5,646; BSA 0; Dow John 425; total 6,071, igual al control.
- Aging (fuente 6.3, Billie's Watercraft Warehouse): 0 a 30 días 145,740 al 10% = 14,574; 31 a 90 días 102,100 al 20% = 20,420; más de 90 días 77,010 al 30% = 23,103; total 324,850, estimación 58,097. Asiento: Débito Bad Debt Expense 58,097 / Crédito Allowance for Doubtful Accounts 58,097. El apéndice 9.7 del mismo libro da otro ejemplo con $58,250 (buscador [S]); son ejemplos distintos, no una contradicción.

### Recurso canónico
OpenStax 7.4 (el control de igualdad auxiliar-mayor es la clave de diseño) y, para el aging, 9.2. Fijarse en que la suma de los auxiliares coincide con el control y en la tabla de tres tramos con porcentajes crecientes.

## 7. Fundamentos (historia, glosario, fuentes del campo)

### Fuentes
| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 7.1 | Sangster, A. (2025), "The emergence of double entry bookkeeping", Economic History Review 78(2), 499-528 (versión Research Insights, Univ. de Aberdeen) | https://www.abdn.ac.uk/media/site/business/content-images/Sangster---RI---Emergence.pdf | S (artículo académico revisado por pares) | 3/2/1/3 | [M] (resumen y relevancia; no leí el artículo) |
| 7.2 | Yamey, B. S. (2010), "Market for Luca Pacioli's Summa de Arithmetica: some comments", Accounting Historians Journal 37(2), art. 8 | https://egrove.olemiss.edu/aah_journal/vol37/iss2/8 | S | 3/1/1/2 | [M] |
| 7.3 | Wikipedia, "Double-entry bookkeeping" | https://en.wikipedia.org/wiki/Double-entry_bookkeeping | S (terciaria) | 1/1/1/1 | [L] sección de historia, vía extractor |
| 7.4 | Wikipedia, "Summa de arithmetica" | https://en.wikipedia.org/wiki/Summa_de_arithmetica | S (terciaria) | 1/1/1/1 | [L] vía extractor |
| 7.5 | Otros trabajos de Sangster y coautores sobre Pacioli (2008, 2012, 2020) | https://core.ac.uk/download/288025325.pdf (no abierto) | S | sin puntaje | [S] (títulos del buscador) |

### Afirmaciones
- "One of the earliest known records of double-entry bookkeeping comes from a ledger kept by Florentine bankers in 1211" (fuente 7.3). Sangster 2025 sostiene que ese libro contiene verdaderas partidas dobles, es consistente con los sistemas de toda la entidad de 1296 y 1299, y que el método nace en el siglo XII entre cambistas-banqueros del norte de Italia, por escasez de moneda, crédito y exigencias de prueba ante tribunales (fuente 7.1 [M]).
- 1299 a 1300: el libro de Giovannino Farolfi & Company, con Amatino Manucci, "evidences full double-entry bookkeeping" (fuente 7.3).
- Benedetto Cotrugli escribió su tratado en 1458; "no manuscript older than 1475 is known to remain" y se imprimió en 1573 (fuente 7.3). La atribución a los Medici (Giovanni di Bicci) carece de evidencia según la misma fuente.
- Pacioli: *Summa de arithmetica* publicada en 1494 en Venecia por Paganino Paganini; segunda edición idéntica en 1523 en Toscolano. La sección contable es *Particularis de computis et scripturis* (fuente 7.4).
- Discrepancia sobre fechas de origen: Wikipedia (7.4) dice que la partida doble "was invented in the 13th century"; Sangster 2025 (7.1) la retrotrae al siglo XII. Hay que dar las dos. Sobre el uso real de la *Summa*: Yamey 2010 sostiene que no fue "neither an effective reference text for merchants nor a satisfactory text for their sons" (abstract parafraseado por el extractor, 7.2 [M]); Sangster, Stoner y McCarthy (2008) argumentan sobre el mercado de la obra de otro modo (buscador [S], no leído).
- Pacioli no inventó la partida doble: la codificó y la imprimió. Es el punto de consenso entre 7.1, 7.3 y 7.4.
- Marco normativo: el Marco Conceptual IFRS se emitió en septiembre de 2010 y se revisó en marzo de 2018 (portada del PDF, fuente 1.3). La RT 16 de la FACPCE es el "Marco Conceptual de las Normas Contables Profesionales", texto ordenado por Resolución C.D. 93/2005 (fuente 5.6).

### Glosario (candidatos, con fuente)
Asiento / journal entry (OpenStax 3.5); mayor / general ledger (3.5); posting (3.5); cuenta de control y libro auxiliar (7.4); balance de sumas y saldos / trial balance (3.6); plan de cuentas / chart of accounts (3.2); devengado y base caja (4.1); activo, pasivo, patrimonio neto, ingreso y gasto (Marco Conceptual 4.3, 4.26, 4.63, 4.68, 4.69); contracuenta (3.2); estados contables (CCyC 326); inventario y balances (CCyC 322).

### Recurso canónico (Fundamentos)
Historia: Sangster 2025 (resumen en Aberdeen y luego el artículo) para el origen, y la *Summa* misma para Pacioli (no la pude leer; hueco 1). Para el campo: el Marco Conceptual IFRS (capítulos 1 y 4) y OpenStax Vol. 1 como libro de lectura entera.

## 8. libros-contables-en-argentina

Tema de alto riesgo legal. Hay dos fuentes primarias (CCyC y Ley 19.550), ambas texto de la norma. No son independientes en el contenido: el art. 61 de la LGS remite a los arts. 320 y siguientes del CCyC, así que no confirma su contenido, solo el régimen digital. La nota debe decir que lo del CCyC se apoya en un único texto, el de la norma, que cuenta como primaria.

### Fuentes
| # | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| 8.1 | Ley 26.994, Código Civil y Comercial de la Nación, texto actualizado en Infoleg. Libro Primero, Título IV, Capítulo 5 "Actos jurídicos", Sección 7ª "Contabilidad y estados contables", arts. 320 a 331 | https://servicios.infoleg.gob.ar/infolegInternet/anexos/235000-239999/235975/texact.htm (también https://www.argentina.gob.ar/normativa/nacional/ley-26994-235975/texto) | P | 3/3/1/3 | [L] los doce artículos |
| 8.2 | Ley 19.550 (T.O. 1984), texto actualizado, Sección IX "De la Documentación y de la Contabilidad", arts. 61 a 63. Copia PDF impresa de argentina.gob.ar el 1/8/22 | https://www.argentina.gob.ar/normativa/nacional/ley-19550-25553/actualizacion (copia leída: https://www.santafe.gov.ar/index.php/web/content/download/268890/1404204/file/Ley%20General%20de%20Sociedades%2019550.pdf) | P | 3/2/1/3 | [L] arts. 61 y 62 |
| 8.3 | Manual de libros digitales, argentina.gob.ar | https://www.argentina.gob.ar/sites/default/files/manual_de_libros_digitales.pdf | administrativa | sin puntaje | [S] (solo apareció en el buscador) |

Nota de acceso: Infoleg devuelve 403 al acceso automatizado simple; con un User-Agent de navegador responde.

### Afirmaciones literales (CCyC, fuente 8.1)
- Art. 320, Obligados. Excepciones: "Están obligadas a llevar contabilidad todas las personas jurídicas privadas y quienes realizan una actividad económica organizada o son titulares de una empresa o establecimiento comercial, industrial, agropecuario o de servicios." Cualquier otra persona puede llevarla si solicita su inscripción y la habilitación de sus registros o la rubricación de los libros. Quedan excluidas "las personas humanas que desarrollan profesiones liberales o actividades agropecuarias y conexas no ejecutadas u organizadas en forma de empresa"; cada jurisdicción local puede eximir actividades por el volumen de su giro.
- Art. 321, Modo de llevar la contabilidad: "debe ser llevada sobre una base uniforme de la que resulte un cuadro verídico de las actividades y de los actos que deben registrarse, de modo que se permita la individualización de las operaciones y las correspondientes cuentas acreedoras y deudoras. Los asientos deben respaldarse con la documentación respectiva".
- Art. 322, Registros indispensables: a) diario; b) inventario y balances; c) los que correspondan a "una adecuada integración de un sistema de contabilidad" según la importancia y naturaleza de la actividad; d) los que imponen el Código u otras leyes.
- Art. 323, Libros: debe llevarse "mediante la utilización de libros" y presentarlos "debidamente encuadernados" para su individualización en el Registro Público; consiste en anotar en el primer folio nota fechada y firmada de su destino, número de ejemplar, nombre del titular y número de folios. El Registro lleva una nómina alfabética de consulta pública.
- Art. 324, Prohibiciones: alterar el orden de los asientos; dejar blancos; interlinear, raspar, emendar o tachar ("Todas las equivocaciones y omisiones deben salvarse mediante un nuevo asiento hecho en la fecha en que se advierta la omisión o el error"); mutilar el libro; cualquier otra circunstancia que afecte "la inalterabilidad de las registraciones".
- Art. 325, Forma de llevar los registros: "en forma cronológica, actualizada, sin alteración alguna que no haya sido debidamente salvada", en idioma y moneda nacional; deben permitir determinar al cierre de cada ejercicio anual "la situación patrimonial, su evolución y sus resultados"; los registros del art. 322 permanecen en el domicilio del titular.
- Art. 326, Estados contables: al cierre del ejercicio se confeccionan estados contables que comprenden "como mínimo un estado de situación patrimonial y un estado de resultados que deben asentarse en el registro de inventarios y balances".
- Art. 327, Diario: ver sección 4.
- Art. 328, Conservación: diez años (libros desde el último asiento; demás registros desde la última anotación; instrumentos respaldatorios desde su fecha), salvo plazos superiores de leyes especiales.
- Art. 329, Actos sujetos a autorización: el titular puede, "previa autorización del Registro Público de su domicilio", sustituir libros "excepto el de Inventarios y Balances" por ordenadores u otros medios que permitan la individualización de las operaciones y de las cuentas deudoras y acreedoras y su verificación posterior, y conservar la documentación en microfilm, discos ópticos u otros medios. La petición lleva una descripción del sistema "con dictamen técnico de Contador Público". La autorización solo se otorga si los medios son equivalentes en "inviolabilidad, verosimilitud y completitud".
- Art. 330, Eficacia probatoria: la contabilidad llevada en forma y con requisitos "debe ser admitida en juicio, como medio de prueba"; sus registros "prueban contra quien la lleva o sus sucesores, aunque no estuvieran en forma, sin admitírseles prueba en contrario"; el adversario no puede aceptar los asientos que le favorecen y desechar los que lo perjudican.
- Art. 331, Investigaciones: "ninguna autoridad, bajo pretexto alguno, puede hacer pesquisas de oficio"; la exhibición general solo a instancia de parte en sucesión, comunión, contrato asociativo o sociedad, administración por cuenta ajena, liquidación, concurso o quiebra.

### Afirmaciones literales (Ley 19.550, fuente 8.2, copia del 1/8/22)
- Art. 61 (título "Medios mecánicos y otros"): "Podrá prescindirse del cumplimiento de las formalidades impuestas por los artículos 73, 162, 213, 238 y 290 de la presente ley, como así también de las impuestas por los artículos 320 y subsiguientes del Código Civil y Comercial de la Nación para llevar los libros societarios y contables por Registros Digitales mediante medios digitales de igual manera y forma que los registros digitales de las Sociedades por Acciones Simplificadas instituidos por la ley 27.349." Siguen: "El libro diario podrá ser llevado con asientos globales que no comprendan períodos mayores de un (1) mes"; el sistema debe permitir la individualización de las operaciones y de las cuentas deudoras y acreedoras y su verificación "con arreglo al artículo 321"; la CNV dicta la normativa para las sociedades bajo su control; los registros públicos deben implementar un sistema para comprobar el tracto registral.
- Nota de modificaciones de la copia: "Artículo sustituido por art. 21 de la Ley N° 27.444 B.O. 18/6/2018" junto al art. 61, y en antecedentes "Artículo 61 sustituido por art. 5° del Decreto N° 27/2018 B.O. 11/1/2018". Aparecen las dos anotaciones; no verifiqué cómo se concilian (hueco 6).
- Art. 62: la sociedad hace constar en el balance la fecha de vencimiento del plazo de duración; las SRL con capital igual o superior al del art. 299 inc. 2) y las sociedades por acciones "deberán presentar los estados contables anuales regulados por los artículos 63 a 65"; las controlantes presentan estados consolidados; y los estados contables "deberán confeccionarse en moneda constante". Tensión aparente con CCyC 325 ("idioma y moneda nacional"): no es contradicción (moneda nacional frente a moneda constante, es decir reexpresada por inflación), pero la nota debe decirlo.
- Art. 63: contenido del balance general (no leí el detalle).

### Ejemplo con números
La norma no trae asientos. Cifras literales útiles: conservación por diez años (CCyC 328); asientos globales de hasta un (1) mes (CCyC 327 y LGS 61). El umbral del art. 299 inc. 2) figura en la nota de la copia como $10.000.000 (Disposición 6/2006, B.O. 17/5/2006); es un dato de 2006 que puede haberse actualizado y no lo verifiqué.

### Recurso canónico
CCyC arts. 320 a 331 (doce artículos, se leen en diez minutos) más LGS art. 61. Fijarse en: 322 (qué registros son indispensables), 324 c) (corrección por nuevo asiento), 327 (diario con resúmenes mensuales y subdiarios), 329 (el libro de Inventarios y Balances no se puede sustituir por medios electrónicos) y 330 (los registros prueban contra quien los lleva).

## Huecos

1. **Pacioli en primaria**: no leí la *Summa* ni una traducción de *Particularis de computis et scripturis*. No cito nada de lo que Pacioli dice sobre memorial, diario y mayor. Falta una edición o traducción en acceso abierto.
2. **Dimensiones y auxiliares en el plan de cuentas** ("qué no meter en el plan"): ninguna fuente leída lo trata. Necesita fuente (guías de diseño de plan de cuentas, documentación de ERP) o declararlo criterio propio de la organización.
3. **Contraasiento / reversión como corrección**: la base legal argentina está (CCyC 324 c), pero no encontré en OpenStax un pasaje sobre cómo corregir un asiento mal hecho. Solo "correcting entry" frente a "adjusting entry" (buscador [S]) y los reversing entries opcionales, que son otra cosa.
4. **Devengado en la norma argentina**: de la RT 16 solo obtuve el pasaje de "devengamiento" dentro del estado de cambios en la situación financiera. Falta el pasaje de la RT 54 o de la RT 17 que define la base de devengado. Candidatos no abiertos: https://sfap.facpce.org.ar/normasweb/documentos/1590.pdf y https://sfap.facpce.org.ar/normasweb/documentos/1725.pdf.
5. **Marco Conceptual IFRS y NIC 1**: leí copias PDF alojadas en un servidor universitario; el sitio de IFRS exige suscripción. La NIC 1 que leí es la versión previa a IFRS 18; que IFRS 18 la reemplace es una afirmación mía de memoria, sin verificar en esta ronda. Confirmar la versión vigente.
6. **Ley argentina, segunda fuente**: para el CCyC la LGS art. 61 es complementaria, no independiente. No leí la resolución general de la IGJ ni la de ningún Registro Público sobre rúbrica y libros digitales, ni el manual de libros digitales (solo en el buscador). La copia de la LGS es de 2022: no verifiqué reformas posteriores, ni cómo se concilian las dos notas de modificación del art. 61 (Ley 27.444 y Decreto 27/2018).
7. **Ubicación del CCyC**: Infoleg lo ubica en Título IV, Capítulo 5 "Actos jurídicos", Sección 7ª. No lo contrasté con otra edición.
8. **Aging**: OpenStax lo trata como estimación de incobrables. No hay fuente que lo trate como herramienta de gestión de cobranzas.
9. **Ganancia sin caja con cifras**: la explicación viene de una sola fuente secundaria (AccountingTools) sin ejemplo numérico. Falta un caso con cifras (estado de flujo de efectivo de OpenStax o un caso de libro de texto).
10. **Textos en castellano**: no busqué manuales de contabilidad básica en castellano; cubrirían la terminología local (balance de sumas y saldos, asiento, diario, mayor).
11. **Historia**: faltan profesionalización (institutos de contadores, siglos XIX y XX) y normalización (IASC 1973, IASB 2001, FACPCE). No hice ronda para eso.
12. **Rondas**: partida-doble, asiento-y-libros y Fundamentos agotaron o rozaron las tres rondas; el resto usó una o dos.
