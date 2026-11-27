---
resumen: >-
  Los estados contables son el resumen del registro de una empresa en un juego de informes para quien la mira desde afuera: qué tiene y qué debe a una fecha, cuánto ganó en un período, cómo cambió su patrimonio y de dónde vino y a dónde fue su caja, con notas que los explican.
estado: vigente
estabilidad: estable
fuentes:
  - "IFRS Foundation, NIC 1 Presentation of Financial Statements (página de la norma, según su resumen): https://www.ifrs.org/issued-standards/list-of-standards/ias-1-presentation-of-financial-statements/"
  - "IFRS Foundation, Conceptual Framework for Financial Reporting (página, según su resumen): https://www.ifrs.org/issued-standards/list-of-standards/conceptual-framework/"
  - "IFRS Foundation, NIIF 18 Presentation and Disclosure in Financial Statements (página, según su resumen): https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/"
  - "OpenStax, Principles of Financial Accounting (2019), 5.4 Appendix: Complete a Comprehensive Accounting Cycle for a Business: https://openstax.org/books/principles-financial-accounting/pages/5-4-appendix-complete-a-comprehensive-accounting-cycle-for-a-business"
  - "KPMG, Current/non-current classification of liabilities (2024, según su resumen): https://kpmg.com/us/en/articles/2024/current-noncurrent-classification-liabilities-ias-amendments.html"
  - "Contabilidad/.investigacion/estados-contables.md (2026-11-27)"
aliases: [estados contables, estados financieros, juego completo de estados financieros, financial statements, estado de cambios en el patrimonio neto, estado de evolución del patrimonio neto, statement of changes in equity, notas a los estados contables, notes to the financial statements]
creado: 2026-11-27
revisado: 2026-11-27
---

# Estados contables

Los estados contables son el resumen del registro de una empresa en un juego de informes para quien la mira desde afuera: qué tiene y qué debe a una fecha, cuánto ganó en un período, cómo cambió su patrimonio y de dónde vino y a dónde fue su caja, con notas que los explican.

Reciben del [registro](../Registro/registro-contable.md) los saldos de las cuentas, ya corregidos por los [ajustes de cierre](ajustes-de-cierre.md). Las [normas contables](normas-contables.md) dicen cómo se presentan. Las [operaciones](../Operaciones/operaciones.md) llegan acá sin pasar por ninguna otra puerta: cada venta, compra o amortización termina en un saldo que algún estado muestra. La [contabilidad de gestión](../Contabilidad-de-gestion/contabilidad-de-gestion.md) usa el mismo registro para decidir adentro, sin el formato que piden las normas.

## Para quién se informa

El Marco Conceptual del IASB dice que su propósito es ayudar a que las normas den información útil a inversores, prestamistas y otros acreedores (según el resumen de su página). Esos usuarios no ven el registro: ven los estados. Por eso (inferencia propia, que ninguna fuente leída dice) los estados siguen reglas comunes de forma y de contenido, para que dos empresas se puedan comparar y para que una misma empresa se compare con su año anterior.

> [!NOTE]
> Sin fuente todavía: el texto del capítulo 1 del Marco Conceptual (el objetivo literal de la información financiera y la definición de usuarios primarios). Se leyó solo el resumen de su página.

El Marco se emitió en septiembre de 2010 y se revisó en marzo de 2018.

## El juego completo

La NIC 1 fija qué estados forman un juego completo. La NIIF 18 reemplaza a la NIC 1 para los ejercicios anuales que empiezan el 1 de enero de 2027 o después, y admite aplicarla antes; lo que sigue es la NIC 1, que rige hasta entonces. Según el resumen de su página, el juego completo tiene cinco piezas:

| Estado | Mira | Nota |
|---|---|---|
| Estado de situación financiera, al final del período | una fecha | [balance](balance.md) |
| Estado del resultado y otro resultado integral del período | un período | [estado de resultados](estado-de-resultados.md) |
| Estado de cambios en el patrimonio del período | un período | sección de esta entrada |
| Estado de flujos de efectivo del período | un período | [estado de flujo de efectivo](estado-de-flujo-de-efectivo.md) |
| Notas: resumen de las políticas contables significativas y otra información explicativa | todo lo anterior | sección de esta entrada |

Hay un sexto estado en un caso puntual: cuando la empresa reexpresa cifras hacia atrás o reclasifica partidas, agrega un estado de situación al comienzo del período comparativo anterior.

Los nombres cambian según el país y la época. «Balance» es el nombre corriente del estado de situación, y en muchos libros el estado de resultados se llama cuenta de pérdidas y ganancias (uso habitual, sin fuente leída). Las normas propias de un país pueden usar otros nombres; los de Argentina están en [normas contables en Argentina](normas-contables-en-argentina.md).

## Cómo se encadenan los cuatro estados

Los estados se arman en un orden, porque cada uno toma un dato del anterior. OpenStax lo muestra con el ciclo contable completo de Clip'em Cliff, un ejemplo de agosto de 2019:

1. El estado de resultados da el resultado del período: ingresos de $10.650 (servicios por $10.300 e intereses por $350) menos gastos de $10.625, un resultado de $25.
2. El estado de cambios en el patrimonio toma ese resultado. En el libro, los resultados acumulados parten de $0, suman los $25, restan $150 de dividendos y terminan en −$125.
3. El balance toma ese saldo final dentro del patrimonio. Activo de $80.875, pasivo de $11.000 y patrimonio de $69.875: 11.000 + 69.875 = 80.875.
4. El estado de flujo de efectivo explica por qué la caja del balance de cierre es distinta de la del balance anterior.

| Del estado | Sale | Y entra en |
|---|---|---|
| Resultados | el resultado del período ($25) | cambios en el patrimonio |
| Cambios en el patrimonio | los resultados acumulados al cierre (−$125) | el patrimonio del balance |
| Balance de apertura y de cierre | la variación de la caja | el flujo de efectivo, que la explica |

La conexión es una prueba de consistencia. Si el resultado del estado de resultados no coincide con el que suma el patrimonio, o la caja del flujo no coincide con la del balance, hay un error en el registro o en el armado. Un registro de movimientos que emite los cuatro estados desde los mismos asientos debería cumplir estas igualdades por construcción (es una inferencia sobre el diseño, no algo que digan las fuentes); el modelo técnico de ese registro está en [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md).

## El estado de cambios en el patrimonio

El estado de cambios en el patrimonio cuenta qué movió el patrimonio entre el principio y el final del período. Lo mueven el resultado del período, lo que los dueños aportan y lo que se les distribuye (los dividendos o retiros). Sin este estado no se ve por qué el patrimonio del balance de cierre difiere del de apertura.

En el ejemplo de OpenStax el estado se llama «estado de resultados acumulados» y muestra solo esa parte del patrimonio. El patrimonio total del balance ($69.875) incluye además el capital aportado; restando los −$125 de resultados acumulados, ese capital sería de $70.000 (cálculo propio desde las cifras del libro).

> [!NOTE]
> Sin fuente todavía: un ejemplo con cifras de un estado de cambios en el patrimonio completo, con columnas por componente (capital, reservas, resultados acumulados, otro resultado integral).

## Las notas

Las notas integran el juego completo con el mismo rango que los estados. Según la NIC 1, traen el resumen de las políticas contables significativas (por ejemplo, con qué criterio se valúa el stock o se amortizan los bienes) y otra información explicativa que no entra en el cuerpo de los estados. Lo que una norma pide revelar va en las notas. Un caso: los convenios de un préstamo que se tienen que cumplir después del cierre no cambian cómo se clasifica la deuda en el [balance](balance.md), pero se revelan.

## El cierre del período queda en otro tema

Para llegar a los estados, la empresa cierra el período: concilia, ajusta, revisa y emite. El recorrido entero entre áreas (del registro al informe) es un proceso del tema Procesos de negocio, todavía no escrito. Acá queda cómo se registra cada ajuste, en [ajustes de cierre](ajustes-de-cierre.md), y la [conciliación bancaria](../Control-interno/conciliaciones.md), que es un control.

## Qué hay adentro de Estados contables

- [Balance](balance.md): el estado de situación, con activo, pasivo y patrimonio, lo corriente y lo no corriente, y lo que el balance no dice sobre el valor de la empresa.
- [Estado de resultados](estado-de-resultados.md): ingresos, costos y gastos de un período, los resultados intermedios y lo que cambia con la NIIF 18.
- [Estado de flujo de efectivo](estado-de-flujo-de-efectivo.md): la caja por actividades de operación, inversión y financiación; método directo e indirecto.
- [Ajustes de cierre](ajustes-de-cierre.md): devengamientos, diferimientos, previsiones, amortización del período y el cierre de las cuentas de resultado.
- [Normas contables](normas-contables.md): el Marco Conceptual, las NIIF, la NIIF para las PYMES, las normas locales, la consolidación y la disputa entre valor razonable y costo histórico.
- [Normas contables en Argentina](normas-contables-en-argentina.md): la FACPCE y la RT 54, las NIIF para cotizantes y el ajuste por inflación.
