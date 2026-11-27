---
resumen: >-
  Una base relacional guarda los datos en tablas de filas y columnas, une las tablas con claves y
  se consulta con SQL; la base misma hace cumplir las reglas de integridad, como que todo pedido
  apunte a un cliente que existe.
estado: vigente
estabilidad: estable
fuentes:
  - "E. F. Codd, A Relational Model of Data for Large Shared Data Banks, Communications of the ACM 13(6), junio de 1970: https://courses.cs.washington.edu/courses/cse544/02sp/papers/codd70.pdf (solo metadatos y resumen; no se leyó el cuerpo)"
  - "PostgreSQL Documentation, 5.5 Constraints: https://www.postgresql.org/docs/current/ddl-constraints.html"
  - "IBM, The relational database: https://www.ibm.com/history/relational-database (según un resumen de la página)"
  - "Michael Stonebraker y Andrew Pavlo, What Goes Around Comes Around... And Around..., SIGMOD Record 53(2), 2024: https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf"
  - "Bases-de-datos/.investigacion/ (informes del 2026-11-27)"
aliases: [base de datos relacional, relational database, RDBMS, modelo relacional, base SQL]
creado: 2026-11-27
revisado: 2026-11-27
---

# Base relacional

Una base relacional guarda los datos en tablas de filas y columnas, une las tablas con claves y
se consulta con SQL; la base misma hace cumplir las reglas de integridad, como que todo pedido
apunte a un cliente que existe.

Es el modelo por defecto para el sistema de un comercio. Acá va lo que hace falta para usarlo y
elegirlo. La teoría del modelo, con la definición de Codd de las claves y la normalización
explicada desde la planilla, está en [modelo relacional](../../Datos/Modelado-y-almacenamiento/modelo-relacional.md),
del tema Datos. Por qué la base de la aplicación no es la misma que la base para analizar está en
[OLTP y OLAP](../../Datos/Modelado-y-almacenamiento/oltp-y-olap.md).

## Tablas, filas y claves en un comercio

Cada tipo de cosa es una tabla: `clientes`, `productos`, `pedidos` e `items_pedido`. Cada fila es
un caso (un cliente, un pedido) y cada columna, un dato con un tipo fijo (un número, un texto, una
fecha). Todas las filas de una tabla tienen las mismas columnas.

Las claves conectan las tablas (qué es cada una según Codd, y cómo una clave mal elegida rompe el
modelo, está en [modelo relacional](../../Datos/Modelado-y-almacenamiento/modelo-relacional.md#claves-cómo-una-fila-se-identifica-y-apunta-a-otra)):

- La **clave primaria** identifica cada fila. En PostgreSQL, una clave primaria es única y no nula
  a la vez: no puede haber dos pedidos con el mismo número ni un pedido sin número.
- La **clave foránea** es una columna que apunta a la clave primaria de otra tabla. `pedidos.cliente_id`
  apunta a `clientes.id`, y la base rechaza un pedido cuyo cliente no existe.
- Una relación de **muchos a muchos** se arma con una tabla intermedia. Un pedido tiene muchos
  productos y un producto está en muchos pedidos: `items_pedido` guarda un par pedido-producto por
  fila, con la cantidad y el precio de ese momento.

En la jerga formal, la tabla se llama relación, la fila tupla y la columna atributo. De ahí sale el
nombre del modelo, no de que las tablas "se relacionen" entre sí.

## La base hace cumplir las reglas

La diferencia con una planilla es que las reglas viven en la base y no en la disciplina de quien
carga. Una restricción que se declara al [definir la tabla](../SQL/definir-tablas.md) se cumple
para cualquier programa o persona que escriba:

- `NOT NULL`: el pedido tiene que tener fecha.
- `UNIQUE`: no se repite el SKU (el código interno) de un producto.
- `CHECK`: la cantidad tiene que ser mayor que cero.
- `FOREIGN KEY`: el ítem tiene que apuntar a un producto que existe, y se decide qué pasa si se
  borra el producto.

Dos detalles de PostgreSQL sorprenden a quien empieza. Un `CHECK` se cumple si la expresión da
verdadero "or the null value", así que solo no impide un dato vacío: hace falta sumarle `NOT NULL`.
Y en una clave foránea, la acción por defecto al borrar el padre es `ON DELETE NO ACTION`, que
rechaza el borrado si quedan hijos; `CASCADE` borra los hijos, y, según un resumen de la
documentación, conviene solo cuando no pueden existir sin el padre.

## SQL se ocupa del qué, no del cómo

Una consulta SQL dice qué filas se quieren, no cómo buscarlas. El motor decide el camino, y por eso
la misma consulta se acelera agregando un [índice](../SQL/indice.md) sin tocar el SQL. Codd buscaba
eso en 1970: según el resumen de su artículo, "maximal independence between programs on the one
hand and machine representation and organization of data on the other".

El total vendido por cliente, incluidos los que no compraron, sale de unir `clientes` con `pedidos`
por la clave, como explica [join](../SQL/join.md). El lenguaje entero está en [SQL](../SQL/sql.md),
y las diferencias entre motores en la [ficha de dialectos](../SQL/dialectos-de-sql.md).

## De Codd a SQL

El modelo nace en el artículo de E. F. Codd en *Communications of the ACM*, en junio de 1970,
escrito desde IBM Research en San José. Según la página de historia de IBM, un grupo empezó en 1973
una implementación industrial (System R), de la que salió SQL; Oracle, entonces Relational Software,
sacó en 1977 la primera base relacional comercial, y DB2 se entregó en 1983. La historia completa
está en [fundamentos](../Fundamentos/fundamentos-de-bases-de-datos.md).

## Dónde se queda corto

El modelo pide decidir las columnas antes de cargar datos. Un catálogo donde cada tipo de producto
tiene atributos distintos (talle y color para ropa, voltaje para electrónica) se modela con
esfuerzo, y ahí la [base de documentos](base-de-documentos.md) o una columna JSON dentro de la
tabla resuelven mejor. También cuesta reconstruir un objeto anidado de la aplicación a partir de
varias tablas; Stonebraker y Pavlo reconocen ese desajuste como la ventaja real de los documentos.

La crítica de que "SQL y las uniones son lentos" la discuten los mismos autores, que la cuentan
entre los mensajes de venta de NoSQL. Cuándo una carga concreta sí le pesa a un motor relacional
está en [criterios de elección](../Elegir-una-base/criterios-de-eleccion.md).

Las transacciones, que hacen que un pedido y su descuento de stock se guarden juntos o no se
guarden, son el otro pilar de estas bases y tienen su vertical en
[Transacciones](../Transacciones/transacciones.md).
