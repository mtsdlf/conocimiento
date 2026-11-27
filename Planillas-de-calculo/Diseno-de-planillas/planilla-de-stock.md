---
resumen: >-
  Una planilla de stock que no se rompe guarda cada entrada y cada salida como una fila nueva en una
  hoja de movimientos, y calcula el stock de cada producto sumando esas filas, en lugar de pisar a
  mano un número por producto.
estado: borrador
estabilidad: estable
fuentes:
  - "Jan Karel Pieterse, Creating A Simple Inventory System in Excel: https://jkp-ads.com/articles/excelsimpleinventory.asp"
  - "Microsoft, Función SUMAR.SI.CONJUNTO (SUMIFS): https://support.microsoft.com/en-us/office/sumifs-function-c9e748f5-7ea7-455d-9406-611cebce642b"
  - "Google, SUMIFS: https://support.google.com/docs/answer/3238496"
  - "Microsoft, plantillas de inventario de Excel: https://excel.cloud.microsoft/create/inventory-templates/"
  - "Shopify, Excel inventory management (fuente de un vendedor): https://www.shopify.com/blog/excel-inventory-management"
  - "OpenStax, Principles of Financial Accounting, 6.2: https://openstax.org/books/principles-financial-accounting/pages/6-2-compare-and-contrast-perpetual-versus-periodic-inventory-systems"
  - "Planillas-de-calculo/.investigacion/llevar-el-stock.md (2026-11-27)"
aliases: [planilla de inventario, control de stock en Excel, inventario en Google Sheets, stock en planilla]
creado: 2026-11-27
revisado:
---

# Planilla de stock

Una planilla de stock que no se rompe guarda cada entrada y cada salida como una fila nueva en una
hoja de movimientos, y calcula el stock de cada producto sumando esas filas, en lugar de pisar a
mano un número por producto.

Es la misma idea que el [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md) de
una base de datos, llevada a la planilla. Qué es el stock y por qué aparece la sobreventa está en
[catálogo y stock](../../Comercio-electronico/Operaciones-del-comercio/catalogo-y-stock.md).

## Por qué no pisar el número

La planilla más común tiene una fila por producto y una columna «Cantidad» que alguien corrige a
mano después de cada venta. Funciona hasta el día en que el número no coincide con el estante:
entonces no hay forma de saber qué corrección estuvo mal, porque cada una borró la anterior. Esto
es criterio de esta base; no se encontró un estudio que mida cuánto falla.

Las plantillas de inventario que ofrece Microsoft van por ese lado: según su página, permiten editar
"inventory items, quantities, costs" con fórmulas que suman totales, y no se vio en ellas una hoja de
movimientos. Para Google Sheets no se encontró una plantilla oficial de inventario.

## Tres hojas: productos, movimientos y stock

El diseño sigue la separación de [entradas, cálculo y salidas](entradas-calculo-salidas.md):

| Hoja | Qué tiene | Quién la toca |
|---|---|---|
| Productos | Código, nombre, stock mínimo | Quien da de alta un producto |
| Movimientos | Fecha, código, tipo (compra, venta, devolución, ajuste, merma), cantidad, motivo, quién cargó | Todos, agregando filas |
| Stock | Una fila por producto con la suma de sus movimientos y la alerta de mínimo | Nadie: solo fórmulas |

Movimientos va como [tabla estructurada](../Datos-en-la-planilla/tabla-estructurada.md), para que la fórmula tome las
filas nuevas sola, y con [validación](../Datos-en-la-planilla/validacion-de-datos.md) en el código (una lista desde
Productos) y en el tipo. Es una fila por movimiento, como piden los [datos ordenados](../Datos-en-la-planilla/datos-ordenados.md).

Pieterse arma su sistema de inventario en Excel de forma parecida: una hoja de artículos y tablas
separadas de compras, reservas y ventas, con el disponible calculado como comprado menos reservado
menos vendido. Llevar una sola tabla con la cantidad en positivo para lo que entra y en negativo
para lo que sale es una variante de esta base, más simple de sumar.

## La fórmula del stock

En la hoja Stock, con el código en A2 y una fecha de corte en B1:

```
=SUMAR.SI.CONJUNTO(Movimientos[Cantidad]; Movimientos[Código]; A2; Movimientos[Fecha]; "<="&$B$1)
```

En inglés es `SUMIFS` y el orden es el mismo: primero el rango a sumar, después los pares de rango y
criterio (Microsoft admite hasta 127). Con `=HOY()` en B1 da el stock de hoy. Con otra fecha da el
stock que había ese día, el mismo truco que usa Pieterse. Cómo se arman las condiciones está en
[sumar y contar con condiciones](../Formulas/sumar-y-contar-con-condiciones.md). El separador `;` es el
de una configuración con coma decimal; en inglés va `,`.

Si el resumen es para mirar y no para decidir, una [tabla dinámica](../Analisis/tabla-dinamica.md) sobre
Movimientos da lo mismo por producto y por mes, sin fórmulas.

## Stock mínimo y conteo físico

La alerta compara el stock con el mínimo de Productos: un `SI(C2<=D2;"Reponer";"OK")` o un formato
condicional que pinte la fila. Shopify, que vende un sistema de gestión, da ese mismo ejemplo con
"Reorder" y "OK". En Sheets la alerta es visual; para que llegue un correo hace falta
[Apps Script](../Automatizar-y-compartir/apps-script.md).

El conteo físico no se carga pisando nada. Se cuenta el estante, se compara con la hoja Stock y la
diferencia entra como un movimiento de tipo «ajuste», con el motivo escrito. Así trabaja el
inventario permanente de la contabilidad según OpenStax: el conteo se compara con el saldo de los
libros y la diferencia se registra como un ajuste. Shopify recomienda contar "quarterly or monthly".

## Cuando cargan varias personas

Con una sola copia en la nube y varias personas agregando filas, cada una escribe en una fila
distinta, así que dos cargas al mismo tiempo no se borran entre sí como sí pasa cuando dos corrigen
la misma celda de cantidad. Es una inferencia de esta base, no un comportamiento documentado de
Excel ni de Sheets. Cómo se comparte el archivo está en [compartir y colaborar](../Automatizar-y-compartir/compartir-y-colaborar.md).

Lo que la planilla no puede hacer es impedir una venta sin stock: dos vendedores pueden cargar la
última unidad casi a la vez y el stock queda en −1. Un control de «stock negativo» en la hoja Stock
lo deja a la vista, como sugiere [revisar una planilla](revisar-una-planilla.md), pero no lo evita.
Cuando eso empieza a pasar seguido, es la señal de [pasar a una base](../cuando-pasar-a-una-base.md),
donde una [escritura condicional](../../Bases-de-datos/Transacciones/concurrencia.md) sí lo impide.

> [!NOTE]
> Sin fuente todavía: el comportamiento documentado de Excel en línea y de Google Sheets cuando dos
> personas editan a la vez; cómo proteger la hoja Stock para que nadie la pise; y qué columnas tienen
> las plantillas de inventario de Microsoft, que no se abrieron.
