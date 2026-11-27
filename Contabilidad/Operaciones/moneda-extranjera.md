---
resumen: >-
  Una operación en moneda extranjera se registra en la moneda funcional de la empresa al tipo de cambio del día, y las deudas y créditos que siguen abiertos se vuelven a convertir en cada cierre; la diferencia entre un tipo y otro es una diferencia de cambio que va a resultados.
estado: borrador
estabilidad: estable
fuentes:
  - "IFRS Foundation, NIC 21 Efectos de las variaciones en las tasas de cambio de la moneda extranjera, resumen oficial: https://www.ifrs.org/issued-standards/list-of-standards/ias-21-the-effects-of-changes-in-foreign-exchange-rates/"
  - "IFRS Foundation, NIC 21, texto oficial (edición HTML 2026): https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias21.html"
  - "PwC Viewpoint, Foreign currency, cap. 4, ejemplo FX 4-2 (US GAAP, ASC 830): https://viewpoint.pwc.com/dt/us/en/pwc/accounting_guides/foreign_currency/foreign_currency__2_US/chapter_4_foreign_cu_US/44_subsequent_measur_US.html"
  - "Oracle, JD Edwards, ganancias y pérdidas de cambio (documentación de un proveedor de software, vía buscador): https://docs.oracle.com/cd/E16582_01/doc.91/e15123/processcurrlossgainap.htm"
  - "Contabilidad/.investigacion/operaciones.md (2026-11-27)"
aliases: [moneda extranjera, foreign currency, diferencia de cambio, diferencias de cambio, exchange difference, foreign exchange gain or loss, moneda funcional, functional currency, conversión, remedición, remeasurement, NIC 21, IAS 21]
creado: 2026-11-27
revisado:
---

# Moneda extranjera

Una operación en moneda extranjera se registra en la moneda funcional de la empresa al tipo de cambio del día, y las deudas y créditos que siguen abiertos se vuelven a convertir en cada cierre; la diferencia entre un tipo y otro es una diferencia de cambio que va a resultados.

Atraviesa los ciclos: toca las ventas, las compras, los préstamos y las cuentas bancarias cada vez que están en otra moneda. El asiento de cada ciclo (ver [operaciones](operaciones.md)) sigue igual y se le suma la conversión. La norma es la NIC 21. La inflación y el ajuste por inflación tienen su propia norma y están en [normas contables en Argentina](../Estados-contables/normas-contables-en-argentina.md).

## La moneda funcional

La moneda funcional es, según la NIC 21, "the currency of the primary economic environment in which the entity operates"; cualquier otra es moneda extranjera. Para decidirla, la norma mira primero la moneda que más influye en los precios de venta (muchas veces aquella en que se fijan y se cobran) y la que más influye en los costos de mano de obra, materiales y otros. Si los indicadores se mezclan, decide la gerencia con su juicio, dando prioridad a esos primeros.

La moneda funcional sale de esos indicadores. Aplicándolos, una empresa que factura y paga sueldos en pesos tiene el peso como moneda funcional aunque sus dueños piensen en dólares; el ejemplo es inferencia, no de la norma.

## Al registrar y al cerrar

Una operación en moneda extranjera entra en la moneda funcional al tipo de cambio de contado de la fecha de la operación. Por razones prácticas la NIC 21 admite un tipo promedio de la semana o del mes, salvo que el tipo fluctúe mucho.

En cada cierre, lo que se hace depende de si la partida es monetaria. Una partida monetaria es un derecho a recibir, o una obligación de entregar, "a fixed or determinable number of units of currency": una cuenta a cobrar, una deuda con un proveedor, un préstamo, el saldo de una cuenta bancaria. La NIC 21 pide:

| Partida | Tipo de cambio al cierre |
|---|---|
| Monetaria (créditos, deudas, efectivo) | el tipo de cierre |
| No monetaria medida al costo (inventario, máquinas) | el tipo de la fecha de la operación, sin cambios |
| No monetaria medida a valor razonable | el tipo de la fecha en que se midió el valor |

Las diferencias de cambio que surgen al cobrar o pagar una partida monetaria, o al convertirla a un tipo distinto del anterior, "shall be recognised in profit or loss in the period in which they arise". La excepción es la inversión neta en un negocio en el extranjero, que es de consolidación ([normas contables](../Estados-contables/normas-contables.md)).

## Diferencia realizada y no realizada

La práctica distingue dos diferencias de cambio. La realizada aparece cuando la partida se cobra o se paga: es definitiva. La no realizada aparece al convertir al cierre una partida que sigue abierta: puede cambiar en el próximo cierre. La NIC 21 no usa esos nombres; habla de diferencias por liquidar y por convertir, y las dos van a resultados del período. La distinción viene de la práctica y de la documentación de los sistemas de gestión.

El único ejemplo con números encontrado es de PwC y aplica el US GAAP (ASC 830); la mecánica de las partidas monetarias es la misma que en la NIC 21, pero no se encontró un ejemplo bajo NIIF. Una empresa con moneda funcional dólar compra a crédito el 1 de agosto impresoras por 1.000 libras, a 1,5 dólares por libra: la deuda entra por 1.500 dólares.

El 30 de septiembre, en el cierre, la libra vale 1,4 y la deuda pasa a 1.400 dólares:

| Cuenta | Debe | Haber |
|---|---|---|
| Cuentas a pagar | 100 | |
| Diferencia de cambio (ganancia) | | 100 |

El 15 de octubre la libra vale 1,3. Se vuelve a convertir la deuda (Cuentas a pagar 100 al debe, Diferencia de cambio 100 al haber) y se paga:

| Cuenta | Debe | Haber |
|---|---|---|
| Cuentas a pagar | 1.300 | |
| Caja | | 1.300 |

La ganancia total es de 200 dólares: 100 quedaron registrados en el cierre de septiembre, sin realizar, y 100 al pagar. Las impresoras no se tocan: son una partida no monetaria y quedan al tipo del 1 de agosto.

> [!NOTE] Sin fuente todavía: un ejemplo con números bajo la NIC 21 y un capítulo de libro de texto abierto sobre moneda extranjera.

## Dos maneras de registrar la conversión del cierre

Las fuentes muestran dos maneras de llegar al mismo resultado. En el ejemplo de PwC, cada cierre ajusta la partida en forma acumulada y el pago solo registra la diferencia desde el último cierre. Según documentación de sistemas de gestión leída por el buscador, otra práctica revierte la diferencia no realizada al empezar el período siguiente y registra toda la diferencia, ya realizada, al pagar. Las dos terminan con la misma ganancia total; cambian los asientos intermedios.

Para quien construye un sistema, esto se traduce en guardar cada partida abierta con su importe en moneda extranjera y el tipo con que entró, poder convertir al cierre solo las monetarias, y elegir una de las dos maneras y sostenerla. Este párrafo es inferencia a partir de las fuentes.
