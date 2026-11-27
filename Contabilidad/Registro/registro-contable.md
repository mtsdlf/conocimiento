---
resumen: >-
  El registro contable es el mecanismo que convierte cada hecho económico de una empresa en un asiento de partida doble, respaldado por un comprobante, y cada asiento en saldos de cuentas de los que salen los estados contables.
estado: borrador
estabilidad: estable
fuentes:
  - "OpenStax, Principles of Financial Accounting (2019), cap. 3, secciones 3.1 a 3.6: https://openstax.org/books/principles-financial-accounting/pages/3-1-describe-principles-assumptions-and-concepts-of-accounting-and-their-relationship-to-financial-statements"
  - "OpenStax, Principles of Financial Accounting (2019), 3.5 Use Journal Entries to Record Transactions: https://openstax.org/books/principles-financial-accounting/pages/3-5-use-journal-entries-to-record-transactions-and-post-to-t-accounts"
  - "OpenStax, Principles of Financial Accounting (2019), 3.6 Prepare a Trial Balance: https://openstax.org/books/principles-financial-accounting/pages/3-6-prepare-a-trial-balance"
  - "OpenStax, Principles of Financial Accounting (2019), 5.4 Appendix: Complete a Comprehensive Accounting Cycle for a Business (según el buscador): https://openstax.org/books/principles-financial-accounting/pages/5-4-appendix-complete-a-comprehensive-accounting-cycle-for-a-business"
  - "IFRS Foundation, Conceptual Framework for Financial Reporting (2018), párrs. 4.3 y 4.26: https://moodle2.units.it/pluginfile.php/493397/mod_resource/content/1/conceptual-framework-for-financial-reporting.pdf"
  - "Contabilidad/.investigacion/registro-y-fundamentos.md (2026-11-27)"
aliases: [registro, registro contable, registración contable, teneduría de libros, bookkeeping, ciclo contable, accounting cycle, recording, contabilidad general, general ledger]
creado: 2026-11-27
revisado:
---

# Registro contable

El registro contable es el mecanismo que convierte cada hecho económico de una empresa en un asiento de partida doble, respaldado por un comprobante, y cada asiento en saldos de cuentas de los que salen los estados contables.

Las demás partes de la [contabilidad](../contabilidad.md) suponen este mecanismo. Las [Operaciones](../Operaciones/operaciones.md) le traen los hechos (una venta, una compra, un sueldo) y usan sus reglas para armar el asiento. Los [Estados contables](../Estados-contables/estados-contables.md) resumen sus saldos para afuera, la [Contabilidad de gestión](../Contabilidad-de-gestion/contabilidad-de-gestion.md) los reordena para decidir adentro y el [Control interno](../Control-interno/control-interno.md) cuida que digan la verdad.

## Qué hecho se registra

Se registra lo que cambia los recursos de la empresa o sus obligaciones. El Marco Conceptual del IASB define el activo como «a present economic resource controlled by the entity as a result of past events» (4.3) y el pasivo como «a present obligation of the entity to transfer an economic resource as a result of past events» (4.26). Una venta, una compra a crédito o un sueldo devengado cambian alguno de los dos y se registran; un pedido de un cliente o un presupuesto enviado todavía no, porque no cambian ni un recurso ni una obligación (aplicación de las definiciones, inferencia de la base).

Según OpenStax, unos pocos principios condicionan qué y cómo se registra: el ingreso se reconoce en el período en que se gana, se supone que la empresa sigue operando en el futuro previsible (empresa en marcha), todo se mide en una unidad monetaria y los bienes se anotan a su costo histórico. El primero es el [devengado](devengado.md), que decide en qué período cae cada hecho.

Cada asiento se apoya en un comprobante (factura, recibo, extracto bancario, planilla de sueldos). En Argentina, el Código Civil y Comercial exige que los asientos se respalden con la documentación respectiva (art. 321, en [libros contables en Argentina](libros-contables-en-argentina.md)). Que un auditor contraste después lo que el comprobante dice es inferencia de la base.

## Del hecho al saldo, en cuatro pasos

```mermaid
flowchart LR
  H[Hecho y comprobante] -->|se analiza y se anota en el| D[Diario]
  D -->|se pasa cuenta por cuenta al| M[Mayor]
  M -->|se lista y se controla en el| B[Balance de sumas y saldos]
  B -->|se ajusta y se resume en los| E[Estados contables]
```

1. Analizar el hecho: qué cuentas cambia y en cuánto. La regla que lo ordena es la [partida doble](partida-doble.md): cada hecho toca al menos dos cuentas y la ecuación activo = pasivo + patrimonio neto sigue cerrando.
2. Anotarlo en el diario. El asiento lleva fecha, cuentas, importes al debe y al haber, y explicación. Las cuentas salen del [plan de cuentas](plan-de-cuentas.md).
3. Pasarlo al mayor, donde cada cuenta acumula sus movimientos y su saldo. Para clientes y proveedores, el detalle va además a un auxiliar, las [cuentas corrientes](cuentas-corrientes.md).
4. Controlar con el balance de sumas y saldos: si el debe y el haber de todas las cuentas no suman lo mismo, hay un error.

La forma del asiento, los libros y cómo se corrige un error están en [asiento y libros](asiento-y-libros.md).

Un hecho del ejemplo de OpenStax recorre los cuatro pasos. El 5 de enero de 2019, la imprenta Printing Plus compra un equipo por 3.500 dólares a crédito:

| Cuenta | Debe | Haber |
|---|---|---|
| Equipos | 3.500 | |
| Proveedores | | 3.500 |

En el mayor, Equipos suma 3.500 deudor y Proveedores 3.500 acreedor. En el balance de sumas y saldos del 31 de enero, Equipos aparece con 3.500 en la columna del debe y Proveedores con 500 en la del haber (su saldo cambió con otros hechos del mes), y el total de cada columna da 34.000.

## El ciclo contable completo

Los cuatro pasos se repiten todo el período. Al cierre se agregan los que llevan el registro a los estados contables. OpenStax los ordena en un ciclo de diez pasos (lista según el buscador):

1. analizar las operaciones;
2. registrarlas en el diario;
3. pasarlas al mayor;
4. preparar el balance de sumas y saldos sin ajustar;
5. registrar los asientos de ajuste;
6. preparar el balance de sumas y saldos ajustado;
7. preparar los estados contables;
8. cerrar las cuentas de resultado;
9. preparar el balance posterior al cierre;
10. optativamente, revertir algunos ajustes al comenzar el período siguiente.

Los pasos 5 a 9 son de [ajustes de cierre](../Estados-contables/ajustes-de-cierre.md), y el 10 es el segundo sentido de «contraasiento» que separa [asiento y libros](asiento-y-libros.md). El cierre como recorrido entre áreas (quién entrega qué y cuándo) es un proceso del tema Procesos de negocio, todavía no escrito.

## Cómo falla un registro

- Un hecho sin asiento. Lo que ocurrió sin comprobante (sueldos trabajados y no pagados, el desgaste de una máquina) queda fuera hasta que un ajuste lo agrega. Por eso existen los ajustes de cierre.
- Un asiento que cuadra con la cuenta equivocada. El balance de sumas y saldos no lo detecta; lo detectan las [conciliaciones](../Control-interno/conciliaciones.md).
- Un asiento que se edita o se borra. Se pierde el rastro de qué se registró y cuándo. La regla es corregir con un asiento nuevo.
- Un plan de cuentas con un cliente por cuenta. El detalle que va en los auxiliares termina en el mayor y los estados se vuelven ilegibles.

Estas cuatro fallas son inferencia de la base: ninguna fuente leída las enumera. Para quien construye un sistema, se traducen en lo que el registro tiene que impedir o hacer posible: asientos descuadrados rechazados, asientos confirmados sin edición, el auxiliar y el mayor calculados del mismo registro (inferencia de la base). Cómo se modela eso en una base de datos está en [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md) y va a estar en el tema Software de gestión.

## Lo que hay adentro del registro

- [Partida doble](partida-doble.md): la ecuación contable, qué es débito y crédito y por qué cada hecho toca dos cuentas. Leela primero.
- [Plan de cuentas](plan-de-cuentas.md): la lista numerada de cuentas, sus niveles y lo que va en auxiliares o dimensiones en lugar de cuentas.
- [Asiento y libros](asiento-y-libros.md): el asiento, el diario, el mayor, el balance de sumas y saldos y cómo se corrige un error sin borrar.
- [Devengado](devengado.md): registrar cuando pasa y no cuando se cobra; por qué una empresa con ganancia se queda sin plata.
- [Cuentas corrientes](cuentas-corrientes.md): los auxiliares de clientes y proveedores, la cuenta de control y la antigüedad de saldos.
- [Libros contables en Argentina](libros-contables-en-argentina.md): qué registros pide el Código Civil y Comercial, la rúbrica, los registros digitales y la conservación.

Para leer más: OpenStax, *Principles of Financial Accounting*, capítulo 3 entero (3.1 a 3.6). Recorre el hecho, el asiento, el mayor y el balance con una sola empresa de ejemplo; conviene seguir la progresión de la 3.4 (la ecuación) a la 3.5 (el asiento) y la 3.6 (el balance), que salen del mismo conjunto de operaciones.
