---
resumen: >-
  Multiempresa y moneda en el BI es cómo se suman empresas de un grupo y operaciones en monedas
  distintas sin inventar un número: cada importe se guarda en su moneda de origen y en una moneda
  común convertida con una regla escrita, las operaciones entre empresas del grupo se eliminan al
  consolidar, y los planes de cuentas y calendarios de cada empresa se llevan a uno común.
estado: vigente
estabilidad: estable
fuentes:
  - "Kimball Group, Multiple Currency Facts: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/multiple-currencies/"
  - "IFRS Foundation, NIC 21 The Effects of Changes in Foreign Exchange Rates, edición 2026, párrafos 8, 21 a 23, 26 y 38 a 45: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias21.html"
  - "IFRS Foundation, NIIF 10 Consolidated Financial Statements, edición 2026, párrafo 19 y B86 a B93: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs10.html"
  - "Datos/.investigacion/bi-gestion-conciliacion-moneda.md (2026-11-27)"
aliases: [multiempresa en el BI, varias empresas, consolidación en el BI, multimoneda en el BI, multiple currency facts, moneda de presentación, presentation currency, eliminación entre empresas, intercompany]
creado: 2026-11-27
revisado: 2026-11-27
---

# Multiempresa y moneda en el BI

Multiempresa y moneda en el BI es cómo se suman empresas de un grupo y operaciones en monedas distintas sin inventar un número: cada importe se guarda en su moneda de origen y en una moneda común convertida con una regla escrita, las operaciones entre empresas del grupo se eliminan al consolidar, y los planes de cuentas y calendarios de cada empresa se llevan a uno común.

Es la parte del [BI sobre el software de gestión](bi-sobre-software-de-gestion.md) donde más fácil es mostrar un total que no existe. Cómo guarda el sistema el importe con su moneda está en [cantidades, unidades y monedas](../../../Software-de-gestion/Columnas-tecnicas/cantidades-unidades-y-monedas.md#importes-con-moneda), y cómo lleva varias empresas, en [estructura de la organización](../../../Software-de-gestion/Columnas-tecnicas/estructura-de-la-organizacion.md). Qué tipo de cambio corresponde lo dice la norma contable, que está en [moneda extranjera](../../../Contabilidad/Operaciones/moneda-extranjera.md).

## Dos columnas por importe

Kimball propone que una [tabla de hechos](hechos-de-gestion.md) con operaciones en varias monedas lleve «a pair of columns for every financial fact in the row»: una con el importe «in the true currency of the transaction» y otra en «a single standard currency that is used throughout the fact table». La conversión la hace la carga «according to an approved business rule for currency conversion», y el hecho lleva además una dimensión de moneda que dice cuál era la original.

En un sistema de gestión eso ya viene casi hecho: cada documento guarda el importe en la moneda de la operación y su equivalente en la moneda de la empresa, con el tipo de cambio usado. En lectura de esta base, el BI no debería volver a convertir lo que el sistema ya convirtió: si recalcula con otra tabla de tipos de cambio, el importe en moneda de la empresa deja de coincidir con el mayor y la [conciliación](conciliar-el-bi.md) no cierra.

## Tres monedas que no son la misma

| Moneda | Qué es | De dónde sale en el BI |
|---|---|---|
| De la operación | la de la factura o el pago | el documento del sistema |
| Funcional | para la NIC 21, «the currency of the primary economic environment in which the entity operates»; en el sistema, la moneda de la empresa | el documento, ya convertido por el sistema al tipo de su fecha |
| De presentación | «the currency in which the financial statements are presented»; en el BI, la moneda en que se muestra el grupo o el tablero | una conversión que hace el BI con una regla escrita |

Las definiciones son del párrafo 8 de la NIC 21. Cómo se elige la moneda funcional está en [la moneda funcional](../../../Contabilidad/Operaciones/moneda-extranjera.md#la-moneda-funcional). Con una sola empresa, la de presentación suele ser la funcional y la única regla es la del sistema. Hace falta otra con dos empresas de monedas distintas o con un tablero en otra moneda.

## La regla de conversión del grupo

Para llevar los números de una empresa a la moneda de presentación, la NIC 21 (párrafo 39) pide convertir los activos y pasivos «at the closing rate», los ingresos y gastos «at exchange rates at the dates of the transactions», y reconocer las diferencias que resultan «in other comprehensive income». Por razones prácticas admite un tipo promedio del período para ingresos y gastos, salvo que el tipo fluctúe mucho (párrafo 40). Cuando hay varios tipos disponibles, usa aquel al que se podrían haber cancelado los flujos a la fecha de medición (párrafo 26).

Eso le pone tres exigencias al BI (lectura de esta base):

1. Una tabla de tipos de cambio por fecha y por clase de tipo: el de cada día, el promedio de cada mes, el de cierre de cada período. La regla dice qué clase usa cada hecho.
2. Saldos y resultados no se convierten igual. El saldo de deudores va al tipo de cierre; las ventas del mes, al de cada día o al promedio. Un estado de resultados del grupo convertido entero al tipo de cierre no es el que pide la norma.
3. La diferencia de conversión es un renglón propio. Si los activos van a un tipo y los resultados a otro, el balance convertido no cuadra sin la diferencia. Esa diferencia no es una ganancia operativa: la norma la saca del resultado porque los cambios de tipo «have little or no direct effect on the present and future cash flows from operations» (párrafo 41).

Para un tablero de gestión que no es un estado contable, la empresa puede elegir otra regla, como mostrar todo al tipo de cierre para comparar. En lectura de esta base, lo que no puede pasar es que la regla no esté escrita, o que el tablero y el balance usen reglas distintas sin decirlo.

## Consolidar no es sumar

Sumar las ventas de las dos empresas del grupo cuenta dos veces lo que una le vendió a la otra. La NIIF 10 (B86) pide combinar las partidas iguales y «eliminate in full intragroup assets and liabilities, equity, income, expenses and cash flows relating to transactions between entities of the group». También la ganancia que quedó en el stock de la que compró: las ganancias de operaciones dentro del grupo reconocidas en activos «such as inventory and fixed assets, are eliminated in full».

Para el BI, eso pide marcar cada operación con la empresa del grupo que está del otro lado (lectura de esta base). El cliente o el proveedor que es otra empresa del grupo lleva un atributo que lo identifica, y el reporte consolidado filtra o elimina esas filas. Antes de eliminar, los dos lados tienen que coincidir; esa conciliación es de Contabilidad, en [entre empresas del mismo grupo](../../../Contabilidad/Control-interno/conciliaciones.md#entre-empresas-del-mismo-grupo).

Con monedas distintas, los dos lados no se cancelan solos. La NIC 21 (párrafo 45) dice que un crédito y una deuda dentro del grupo en monedas distintas no se pueden eliminar «without showing the results of currency fluctuations in the consolidated financial statements». La empresa A le debe 1.000 dólares a la B; en pesos, la deuda de A y el crédito de B dan lo mismo solo si las dos convirtieron al mismo tipo el mismo día (ejemplo de esta base).

## Un solo plan de cuentas y un solo calendario

La NIIF 10 (párrafo 19) pide preparar los estados consolidados «using uniform accounting policies for like transactions and other events in similar circumstances». Es la versión contable de [conformar](dimensiones-conformadas.md#qué-es-conformar): si cada empresa tiene su plan de cuentas, el BI necesita una tabla que lleve cada cuenta de cada empresa a una cuenta del grupo, y un resultado por rubro se arma sobre la del grupo (lectura de esta base).

Con el calendario pasa lo mismo. La norma pide que los estados de las empresas del grupo tengan la misma fecha de cierre, y, cuando no es practicable, que la diferencia sea de «no more than three months» (B92 y B93). Si una empresa cierra el ejercicio en junio y otra en diciembre, la dimensión de fecha lleva los dos calendarios, como dice [el calendario y los períodos fiscales](dimensiones-conformadas.md#el-calendario-y-los-períodos-fiscales).

## Cómo falla

- Pesos más dólares. Un total de deudores que suma las dos monedas sin convertir.
- La conversión repetida. El BI reconvierte con su propia tabla lo que el sistema ya convirtió, y las ventas en moneda de la empresa no coinciden con el mayor.
- El grupo inflado. Las ventas consolidadas incluyen lo que una empresa le vendió a otra del grupo.
- Todo al tipo de hoy, sin decirlo. El tablero convierte las ventas de hace un año al tipo de cambio de hoy, nadie lo avisa, y muestra un crecimiento que es solo el tipo.
- El renglón que falta. El balance del grupo convertido no cuadra porque nadie guardó la diferencia de conversión.

La inflación agrega un paso antes de convertir: en una economía hiperinflacionaria, la NIC 21 (párrafo 43) pide reexpresar primero y convertir después. Lo propio de la Argentina está en [BI de gestión en la Argentina](bi-de-gestion-en-argentina.md).
