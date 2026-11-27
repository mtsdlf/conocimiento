---
resumen: >-
  La partida doble es la regla de registrar cada hecho económico en al menos dos cuentas, con débitos que suman lo mismo que los créditos, de modo que la ecuación activo = pasivo + patrimonio neto se cumpla siempre.
estado: borrador
estabilidad: estable
fuentes:
  - "OpenStax, Principles of Financial Accounting (2019), 3.2 Define and Describe the Expanded Accounting Equation: https://openstax.org/books/principles-financial-accounting/pages/3-2-define-and-describe-the-expanded-accounting-equation-and-its-relationship-to-analyzing-transactions"
  - "OpenStax, Principles of Financial Accounting (2019), 3.4 Analyze Business Transactions Using the Accounting Equation: https://openstax.org/books/principles-financial-accounting/pages/3-4-analyze-business-transactions-using-the-accounting-equation-and-show-the-impact-of-business-transactions-on-financial-statements"
  - "OpenStax, Principles of Financial Accounting (2019), 3.5 Use Journal Entries to Record Transactions: https://openstax.org/books/principles-financial-accounting/pages/3-5-use-journal-entries-to-record-transactions-and-post-to-t-accounts"
  - "IFRS Foundation, Conceptual Framework for Financial Reporting (2018), cap. 4, párrs. 4.3, 4.26, 4.63, 4.68 y 4.69: https://moodle2.units.it/pluginfile.php/493397/mod_resource/content/1/conceptual-framework-for-financial-reporting.pdf"
  - "AccountingCoach, Debits and credits: additional explanations: https://accountingcoach.com/debits-and-credits-additional-explanations/explanation"
  - "BlackLine, glosario Debits & Credits: https://www.blackline.com/resources/glossaries/debits-and-credits/"
  - "Contabilidad/.investigacion/registro-y-fundamentos.md (2026-11-27)"
  - "Contabilidad/.investigacion/posicion-contraria.md (2026-11-27)"
aliases: [partida doble, doble entrada, double-entry bookkeeping, double entry, ecuación contable, accounting equation, débito y crédito, debe y haber, debits and credits, saldo normal, normal balance, contracuenta, contra account]
creado: 2026-11-27
revisado:
---

# Partida doble

La partida doble es la regla de registrar cada hecho económico en al menos dos cuentas, con débitos que suman lo mismo que los créditos, de modo que la ecuación activo = pasivo + patrimonio neto se cumpla siempre.

Cómo se arma el asiento y en qué libros se anota es de [asiento y libros](asiento-y-libros.md). Acá va la lógica: por qué dos cuentas, qué significa débito y crédito, y qué lado aumenta cada cuenta.

## La ecuación que cada hecho deja cerrada

Todo lo que la empresa controla (el activo) está financiado por terceros (el pasivo) o por sus dueños (el patrimonio neto): activo = pasivo + patrimonio neto. El Marco Conceptual del IASB define las tres piezas. Un activo es «a present economic resource controlled by the entity as a result of past events» (4.3); un pasivo, «a present obligation of the entity to transfer an economic resource as a result of past events» (4.26); el patrimonio, «the residual interest in the assets of the entity after deducting all its liabilities» (4.63).

Como el patrimonio es lo que sobra, un hecho no puede mover un solo lado de la ecuación sin mover otro. Comprar un equipo a crédito sube un activo y un pasivo. Cobrar en efectivo una factura sube la caja y baja lo que el cliente debe. Por eso cada hecho se anota en dos cuentas: una dice de dónde vino el valor y la otra a dónde fue (razonamiento de la base a partir de la ecuación).

## Ingresos y gastos son movimientos del patrimonio

La ecuación expandida que enseña OpenStax abre el patrimonio neto en capital aportado, distribuciones a los dueños (dividendos), ingresos y gastos. El Marco Conceptual explica por qué: un ingreso es un aumento de activos o una baja de pasivos «that result in increases in equity, other than those relating to contributions from holders of equity claims» (4.68), y un gasto es lo inverso (4.69).

Por eso una venta toca una cuenta de activo y una de ingreso, y el ingreso es, en el fondo, patrimonio. Las cuentas de ingresos y gastos se llevan aparte durante el período para poder armar el [estado de resultados](../Estados-contables/estado-de-resultados.md), y al cierre se vuelcan al patrimonio (lo cuentan los [ajustes de cierre](../Estados-contables/ajustes-de-cierre.md)).

## Débito y crédito son izquierda y derecha

Débito (debe) es el lado izquierdo de una cuenta y crédito (haber), el derecho. Qué efecto tiene cada lado depende de la naturaleza de la cuenta. Según OpenStax, las reglas son estas:

| Tipo de cuenta | Aumenta con | Disminuye con | Saldo normal |
|---|---|---|---|
| Activo | débito | crédito | deudor |
| Pasivo | crédito | débito | acreedor |
| Capital aportado | crédito | débito | acreedor |
| Dividendos (retiros de los dueños) | débito | crédito | deudor |
| Ingreso | crédito | débito | acreedor |
| Gasto | débito | crédito | deudor |

La tabla sale de la ecuación. Los activos están a la izquierda del signo igual y aumentan por la izquierda; pasivo y patrimonio están a la derecha y aumentan por la derecha. Los gastos y los dividendos bajan el patrimonio, así que se comportan al revés que él (esta explicación es de la base; las fuentes dan la tabla).

Una contracuenta tiene, según OpenStax, el saldo normal opuesto al de la categoría a la que pertenece. El caso típico es la amortización acumulada: vive entre los activos con saldo acreedor y resta del valor del bien (ver [activos fijos y amortización](../Operaciones/activos-fijos-y-amortizacion.md)).

## Seis hechos de enero en la ecuación y en asientos

OpenStax sigue a una imprenta ficticia, Printing Plus, durante enero de 2019. Primero sus hechos en la ecuación, sin débitos ni créditos (cifras en dólares; los nombres de las cuentas están traducidos):

| Fecha | Hecho | Activo | Pasivo | Patrimonio neto |
|---|---|---|---|---|
| 3 de enero | Emite acciones por efectivo | Caja +20.000 | | Capital +20.000 |
| 5 de enero | Compra un equipo a crédito | Equipos +3.500 | Cuentas a pagar +3.500 | |
| 9 de enero | Cobra un trabajo por adelantado | Caja +4.000 | Ingresos cobrados por adelantado +4.000 | |
| 10 de enero | Presta servicios y los factura | Cuentas a cobrar +5.500 | | Ingresos +5.500 |
| 12 de enero | Paga la luz | Caja −300 | | Gastos −300 |
| 14 de enero | Distribuye dividendos | Caja −100 | | Dividendos −100 |

Al final, el activo suma 32.600 (caja 23.600, deudores 5.500, equipos 3.500), el pasivo 7.500 y el patrimonio neto 25.100. Pasivo más patrimonio da 32.600: la ecuación cierra después de cada fila.

Los mismos hechos como asientos:

| Fecha | Cuenta | Debe | Haber |
|---|---|---|---|
| 3 de enero | Caja | 20.000 | |
| | Capital | | 20.000 |
| 5 de enero | Equipos | 3.500 | |
| | Cuentas a pagar | | 3.500 |
| 9 de enero | Caja | 4.000 | |
| | Ingresos cobrados por adelantado | | 4.000 |
| 10 de enero | Cuentas a cobrar | 5.500 | |
| | Ingresos por servicios | | 5.500 |
| 12 de enero | Gasto de luz | 300 | |
| | Caja | | 300 |
| 14 de enero | Dividendos | 100 | |
| | Caja | | 100 |

El cobro del 9 de enero sube la caja y crea un pasivo, porque el trabajo todavía no se hizo. La factura del 10 de enero crea un ingreso sin que entre plata. Las dos diferencias entre caja y resultado son el sujeto de [devengado](devengado.md).

## El mito del débito bueno y el crédito malo

Quien llega del banco o del lenguaje diario suele creer que un débito es algo malo o una baja, y un crédito algo bueno o un alta. AccountingCoach lo corta en su explicación: débito quiere decir lado izquierdo, y no hay que pensarlo como bueno ni malo. El glosario de un proveedor de software de cierre contable (BlackLine, en las fuentes) nombra la confusión de igualar débito con disminución y crédito con aumento: el efecto depende del tipo de cuenta, y un débito a una cuenta de gasto la aumenta.

La confusión tiene un origen probable en el extracto bancario. Para el banco, el depósito del cliente es una deuda suya, y lo acredita; el cliente ve un «crédito» en su cuenta y lo asocia con algo bueno (hipótesis del informe, sin verificar en una fuente).

Para quien diseña la pantalla de un sistema, la consecuencia es concreta: mostrarle «débito» y «crédito» a alguien que no es contador, sin decir qué efecto tiene sobre esa cuenta, lleva a errores de carga (inferencia de la base).

## Lo que la regla le pide a un registro

La regla se puede comprobar en cada asiento: la suma del debe es igual a la suma del haber. Un sistema que acepta un asiento descuadrado ya no lleva partida doble. Cómo se guarda esa invariante en una base de datos está en [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md).

Que el asiento cuadre no prueba que esté bien: puede cuadrar con la cuenta equivocada. Qué errores detecta el balance de sumas y saldos y cuáles no está en [asiento y libros](asiento-y-libros.md). La historia de la regla, desde los banqueros florentinos hasta Pacioli, y las propuestas que la discuten (REA, triple entrada) están en [Fundamentos](../Fundamentos/fundamentos-de-contabilidad.md).

Para leer más: OpenStax, capítulo 3, secciones 3.4 y 3.5, en ese orden. La 3.4 trabaja la ecuación sin débito ni crédito y la 3.5 agrega las reglas; conviene fijarse en que cada hecho cambia al menos dos filas y la ecuación sigue cerrando.
