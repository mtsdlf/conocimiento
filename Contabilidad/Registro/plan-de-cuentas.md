---
resumen: >-
  El plan de cuentas es la lista numerada de todas las cuentas que usa una empresa para registrar, ordenada como aparecen en los estados contables y codificada para que el primer dígito diga el rubro.
estado: vigente
estabilidad: estable
fuentes:
  - "OpenStax, Principles of Financial Accounting (2019), 3.2 Define and Describe the Expanded Accounting Equation, tabla 3.2: https://openstax.org/books/principles-financial-accounting/pages/3-2-define-and-describe-the-expanded-accounting-equation-and-its-relationship-to-analyzing-transactions"
  - "OpenStax, Principles of Financial Accounting (2019), 3.5 Use Journal Entries to Record Transactions: https://openstax.org/books/principles-financial-accounting/pages/3-5-use-journal-entries-to-record-transactions-and-post-to-t-accounts"
  - "OpenStax, Principles of Financial Accounting (2019), glosario del capítulo 3 (según el buscador): https://openstax.org/books/principles-financial-accounting/pages/3-key-terms"
  - "OpenStax, Principles of Financial Accounting (2019), 7.4 Prepare a Subsidiary Ledger: https://openstax.org/books/principles-financial-accounting/pages/7-4-prepare-a-subsidiary-ledger"
  - "Contabilidad/.investigacion/registro-y-fundamentos.md (2026-11-27)"
aliases: [plan de cuentas, chart of accounts, COA, catálogo de cuentas, nomenclador de cuentas, codificación de cuentas, cuenta imputable, cuenta de detalle]
creado: 2026-11-27
revisado: 2026-11-27
---

# Plan de cuentas

El plan de cuentas es la lista numerada de todas las cuentas que usa una empresa para registrar, ordenada como aparecen en los estados contables y codificada para que el primer dígito diga el rubro.

Cada asiento elige sus cuentas de esta lista ([asiento y libros](asiento-y-libros.md)), y los estados contables salen de sumar sus saldos. Un plan mal armado se nota en los dos lados: la carga se vuelve ambigua (dos cuentas para lo mismo) y el informe no se puede armar (falta la cuenta que separa lo que hay que mostrar). Es inferencia de la base.

## Cómo se numera

OpenStax presenta el plan como un sistema de numeración de cuentas en el que el primer dígito identifica el tipo de cuenta, y lo ordena como se leen los estados: primero las cuentas patrimoniales (activo, pasivo, patrimonio) y después las de resultado. Su tabla 3.2:

| Rubro | Empresa chica | Empresa grande |
|---|---|---|
| Activo | 100 a 199 | 1000 a 1999 |
| Pasivo | 200 a 299 | 2000 a 2999 |
| Patrimonio neto | 300 a 399 | 3000 a 3999 |
| Ingresos | 400 a 499 | 4000 a 4999 |
| Gastos | 500 a 599 | 5000 a 5999 |

Según el mismo libro, una empresa grande de comercio o de industria puede sumar cuentas que empiezan con 6. Pasar de tres a cuatro dígitos deja espacio entre cuenta y cuenta para agregar las que hagan falta sin renumerar (lectura de la base; el libro solo da la tabla).

En el ejemplo de Printing Plus, los códigos son Caja 101, Cuentas a cobrar 111, Cuentas a pagar 201 y Capital 301 (cuentas traducidas). Entre 101 y 111 quedan nueve números sin usar en el ejemplo.

## Niveles: rubros que agrupan y cuentas que se imputan

Un plan se lee como un árbol. Arriba están los rubros que se van a mostrar en el [balance](../Estados-contables/balance.md) y el [estado de resultados](../Estados-contables/estado-de-resultados.md); abajo, las cuentas donde efectivamente se registran los asientos. En la codificación de OpenStax, el primer dígito es el rubro.

Las cuentas de agrupación solo suman a sus hijas y no reciben asientos; las de detalle (imputables) sí. Esta división en dos clases de cuentas es la práctica habitual de los planes de cuentas, pero no figura en las fuentes leídas.

> [!NOTE]
> Sin fuente todavía: la distinción entre cuentas de agrupación y cuentas imputables, y cuántos niveles conviene tener. Falta un manual de contabilidad básica en castellano o una guía de diseño de planes de cuentas.

Los saldos de Printing Plus al 31 de enero de 2019 muestran un plan chico funcionando, ya ordenado por rubro (cifras en dólares):

| Código | Cuenta | Saldo deudor | Saldo acreedor |
|---|---|---|---|
| 101 | Caja | 24.800 | |
| 111 | Cuentas a cobrar | 1.200 | |
| | Materiales | 500 | |
| | Equipos | 3.500 | |
| 201 | Cuentas a pagar | | 500 |
| | Ingresos cobrados por adelantado | | 4.000 |
| 301 | Capital | | 20.000 |
| | Ingresos por servicios | | 9.500 |
| | Dividendos | 100 | |
| | Sueldos | 3.600 | |
| | Gasto de luz | 300 | |

La fuente da los códigos de cuatro cuentas; las demás quedan sin código en la tabla para no inventarlo.

## Lo que no va en el plan

El plan dice qué es un importe (una deuda con proveedores, un gasto de luz). Otras preguntas sobre el mismo importe (con qué proveedor, en qué sucursal, para qué proyecto) se contestan fuera del plan. Si se mezclan, el plan crece con cada cliente nuevo y cada área que se abre, y deja de servir para armar los estados.

Los clientes y los proveedores van a auxiliares. OpenStax lleva el detalle por cliente y por proveedor en un libro auxiliar, y el mayor conserva una sola cuenta de control (Cuentas a cobrar, Proveedores) cuyo saldo tiene que coincidir con la suma del auxiliar. El plan queda con una cuenta y el auxiliar con mil clientes. Está en [cuentas corrientes](cuentas-corrientes.md).

Los centros de costo, los proyectos y las sucursales van a dimensiones. La práctica es etiquetar cada línea del asiento con datos analíticos (el centro de costo, el proyecto, la sucursal) en lugar de abrir «Sueldos de ventas», «Sueldos de producción» y «Sueldos de administración» por cada combinación. Así un mismo gasto se puede sumar por cuenta para el balance y por centro para la gestión. Cómo se usan esos centros está en [centros de costo](../Contabilidad-de-gestion/centros-de-costo.md).

> [!NOTE]
> Sin fuente todavía: ninguna fuente leída trata qué conviene dejar fuera del plan de cuentas ni el uso de dimensiones analíticas. Lo de esta sección sobre dimensiones es práctica del oficio, sin respaldo de un texto; los auxiliares sí tienen fuente (OpenStax 7.4).

Para quien construye un sistema, la regla tiene una forma concreta: la línea de asiento lleva una cuenta del plan y, aparte, referencias al tercero (cliente, proveedor) y a las dimensiones que la empresa defina. El informe por cuenta y el informe por centro salen de las mismas líneas (inferencia de la base).

## Cómo falla un plan de cuentas

- Una cuenta por cliente: el plan crece sin fin y los estados contables se vuelven ilegibles.
- Cuentas que se solapan («Gastos varios» y «Otros gastos»): cada persona carga en una distinta y el saldo de ninguna dice nada.
- Sin espacio entre códigos: la cuenta nueva no entra donde corresponde y termina en un lugar que no se lee con su rubro.
- Un plan copiado sin mirar lo que la empresa tiene que informar: falta la cuenta que separa lo que una norma o un impuesto pide mostrar aparte.

Estos cuatro modos de falla son inferencia de la base a partir de la numeración y los auxiliares de OpenStax.

Para leer más: OpenStax, sección 3.2, tabla 3.2. Es corta; conviene fijarse en que el primer dígito identifica el rubro y en la diferencia entre tres y cuatro dígitos.
