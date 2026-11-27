---
resumen: >-
  En un software de gestión, cada documento confirmado deja movimientos que no se editan (de stock, de cuenta corriente, contables) según reglas de contabilización, y el saldo de cualquier cosa es la suma de sus movimientos. Cada movimiento lleva dimensiones (centro de costo, proyecto, sucursal) para analizarlo sin multiplicar cuentas.
estado: borrador
estabilidad: estable
fuentes:
  - "Martin Fowler, Accounting Narrative: https://martinfowler.com/eaaDev/AccountingNarrative.html"
  - "Martin Fowler, Analysis Patterns (1997), cap. 6 Inventory and Accounting (solo el índice): https://www.oreilly.com/library/view/analysis-patterns-reusable/9780134271453/"
  - "McCarthy, Geerts y Gal, The REA Accounting Model as an Accounting and Economic Ontology, borrador 0.90, 2019, caps. 1 y 5: https://static1.squarespace.com/static/5feb9bf81c227637fcd6262b/t/667f4e6e846ebb74f8b18595/1719619185764"
  - "Nikitkov (2020), REA model, its development and integration as an enterprise ontology framework, AMIS 19(3): https://online-cig.ase.ro/RePEc/ami/articles/19_3_6.pdf"
  - "Informe técnico ITU TR-2006-92 sobre REA y ERP (según resumen): https://en.itu.dk/-/media/EN/Research/About-ITU-Research/Technical-Reports/2006/ITU-TR-2006-92-pdf.pdf"
  - "Documentación de un ERP de código abierto, Immutable Ledger: https://docs.frappe.io/erpnext/user/manual/en/immutable-ledger-in-erpnext"
  - "Documentación de un ERP de código abierto, Accounting Dimensions: https://docs.frappe.io/erpnext/user/manual/en/accounting-dimensions"
  - "Documentación de un ERP de un proveedor grande, Financial dimensions: https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-dimensions"
  - "Dittrich y Vaucouleur (2008), Customization and Upgrade of ERP Systems: An Empirical Perspective, ITU TR-2008-105: https://en.itu.dk/-/media/EN/Research/About-ITU-Research/Technical-Reports/2008/ITU-TR-2008-105-pdf.pdf"
  - "Software-de-gestion/.investigacion/columnas-tecnicas-97.md, columnas-tecnicas-complemento.md y contraria.md (2026-11-27)"
aliases: [registro de movimientos, libro mayor, ledger, general ledger, reglas de contabilización, posting rules, contabilización automática, dimensiones, dimensiones analíticas, dimensiones financieras, accounting dimensions, financial dimensions, REA, resources events agents]
creado: 2026-11-27
revisado:
---

# Registro de movimientos y dimensiones

En un software de gestión, cada documento confirmado deja movimientos que no se editan (de stock, de cuenta corriente, contables) según reglas de contabilización, y el saldo de cualquier cosa es la suma de sus movimientos. Cada movimiento lleva dimensiones (centro de costo, proyecto, sucursal) para analizarlo sin multiplicar cuentas.

El patrón de base, la fila que no se edita y el saldo que se calcula, con su tabla y sus consultas, está en [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md), en Bases de datos. Acá va lo que agrega un software de gestión: que el mismo patrón sirve para la plata, el stock y las horas; que los movimientos salen de los documentos por reglas; y que cada fila lleva las dimensiones con que se va a analizar.

## El mismo patrón para la plata, el stock y las horas

Fowler lo formula para la contabilidad: «The value, or balance, of the Account is derived as the sum of all the Accounting Entrys». Según el índice de *Analysis Patterns* (1997), el capítulo 6 trata el inventario y la contabilidad juntos, con las mismas piezas: cuenta, transacción, cuenta resumen y reglas de contabilización. Para Fowler la cuenta es en el fondo un descriptor que clasifica movimientos, y otros objetos pueden cumplir ese papel.

En un software de gestión eso se ve en tres registros que conviven:

| Registro | Qué suma | Qué descriptor lo clasifica | Dominio |
|---|---|---|---|
| Contable | importes en debe y haber | la cuenta del [plan de cuentas](../../Contabilidad/Registro/plan-de-cuentas.md) | Contabilidad |
| De stock | cantidades que entran y salen | el artículo, el depósito y el lote | [Existencias](../../Inventario-y-depositos/Existencias/existencias.md#la-cantidad-es-un-saldo-de-movimientos) |
| De cuenta corriente | lo facturado, cobrado y pagado por cada parte | el cliente o el proveedor | [cuentas corrientes](../../Contabilidad/Registro/cuentas-corrientes.md) |

Las horas de un proyecto siguen la misma forma: la [hoja de horas](../../Servicios-profesionales-y-proyectos/Registro-de-horas/hoja-de-horas.md#corregir-una-hora-aprobada-o-facturada) aprobada no se edita, se revierte con un movimiento de signo contrario.

## Del documento al movimiento: las reglas de contabilización

Nadie carga a mano el asiento de cada factura. El sistema lo arma con una regla que dice qué movimientos produce cada tipo de documento al confirmarse. Fowler llama a esa pieza *posting rule*: cuando se procesa un hecho del negocio, «it can produce a set of Accounting Transactions».

Una venta confirmada muestra la regla en tres dominios a la vez (ejemplo de esta base). El remito deja una salida de stock en [Inventario](../../Inventario-y-depositos/inventario-y-depositos.md). La factura deja un asiento de ingreso y de deudores por ventas según la [partida doble](../../Contabilidad/Registro/partida-doble.md), más el débito de IVA. Y la cuenta corriente del cliente suma lo que debe. En producción, el [consumo y la declaración](../../Produccion/Ejecucion-en-planta/consumo-y-declaracion.md) de una orden convierten el trabajo de la planta en movimientos de stock y en costo.

La documentación del ERP de código abierto pone la regla de corrección por escrito: «Corrections are made through traceable follow-up documents instead of silently rewriting history», y al anular un documento se agregan filas opuestas. Fowler da tres maneras de corregir (reemplazar, revertir o registrar la diferencia) y las dos últimas conservan la historia.

## Partida doble o REA

> [!IMPORTANT]
> **Dos modelos para lo mismo.** Casi todos los productos guardan asientos de partida doble como modelo central del registro contable. El modelo REA (recursos, eventos y agentes), que William McCarthy publicó en 1982, propone otra cosa: guardar los eventos económicos y sus relaciones, y no las cuentas.
>
> - **REA, según sus autores.** McCarthy, Geerts y Gal (2019) escriben que «REA does not use accounts as modeling primitives, nor does it follow debit-credit posting procedures»: arma una base enlazada donde las filas de distintas tablas capturan el significado de cada transacción. Cada intercambio es una dualidad entre lo que se entrega y lo que se recibe. En la variante que llaman ERP de cadena de valor «no heredado», la partida doble queda relegada «to a database view» y alcanza con «a minimal general ledger». De los ERP heredados dicen que conservan «bloated charts of accounts with long faceted account codes».
> - **La práctica de los productos.** Según el resumen de un informe técnico de la IT-Universitetet de Copenhague (2006), los modelos como REA no se adoptaron en los ERP, que siguen usando la partida doble como modelo contable que alimenta a las demás aplicaciones. Nikitkov (2020) dice que REA entró en normas ISO y sirvió de base a «at least one cloud-based enterprise system», pero que no recibió atención suficiente de académicos ni de practicantes.
>
> Lo que dicen los autores de REA es testimonio de parte: alcanza para decir que existe una implementación, no que funcione mejor. Que el mayor sea una vista derivada vale para la variante no heredada, no como regla general.

En lectura de esta base, las dos posiciones se acercan más de lo que parece. Un software que guarda los documentos confirmados y genera los asientos por regla ya tiene los eventos (el documento) y el mayor (los asientos) a la vez; la diferencia es cuál de los dos trata como fuente. La versión contable de la discusión está en [fundamentos de contabilidad](../../Contabilidad/Fundamentos/fundamentos-de-contabilidad.md#rea-registrar-los-hechos-y-no-los-asientos). Para leer REA de primera mano, el capítulo 1 del libro de 2019 muestra las mismas transacciones en cuentas T y en tablas REA, y el capítulo 5 clasifica los sistemas en cinco tipos.

## Dimensiones en lugar de cuentas

Una dimensión es una etiqueta más en cada movimiento: centro de costo, proyecto, sucursal, región. La documentación del ERP de un proveedor grande dice que los valores de dimensión «become segments within the ledger account»; la del ERP de código abierto, que agregan «business context to the same accounting entry». Por qué los [centros de costo](../../Contabilidad/Contabilidad-de-gestion/centros-de-costo.md#por-qué-los-centros-de-costo-van-en-dimensiones-y-no-en-el-plan-de-cuentas) van en dimensiones y no en el plan de cuentas está explicado en Contabilidad.

Lo que pide al diseño, según esa misma nota: que cada movimiento pueda llevar sus dimensiones, que ciertas cuentas exijan una dimensión y que un reparto por porcentajes quede guardado junto al movimiento. Las dimensiones viajan del documento al movimiento: el centro de costo de la orden de compra llega al asiento de la factura del proveedor (lectura de esta base). Una dimensión no reemplaza a una empresa legal; esa frontera es de [estructura de la organización](estructura-de-la-organizacion.md).

## Cómo falla el registro

- **Movimientos que se editan.** Un ajuste que pisa un saldo en lugar de agregar una fila borra la causa de la diferencia.
- **Reglas personalizadas que no sobreviven a la versión nueva.** Dittrich y Vaucouleur (2008) dan este ejemplo textual: «the postings to the general ledger are often modified to mirror specific business rules», y en cada actualización cada modificación hay que identificarla, analizarla y volver a aplicarla. El costo de cada manera de adaptar está en [configurar o personalizar](configurar-o-personalizar.md).
- **Un movimiento con fecha pasada.** La documentación del ERP de código abierto advierte que un movimiento de stock con fecha anterior revaloriza todo lo posterior. La fecha del hecho y el cierre son de [fechas, vigencias y cierre](fechas-vigencias-y-cierre.md).
- **Dimensiones opcionales.** Un gasto sin centro de costo no entra en ningún presupuesto, y el reporte por dimensión no cuadra con el total ([reportes operativos y legales](reportes-operativos-y-legales.md)).

Los movimientos salen del [documento](documento-y-estados.md) que los produce y referencian los [datos maestros](datos-maestros-y-partes.md): sin esas dos columnas, una fila de movimiento no dice qué pasó ni a quién.
