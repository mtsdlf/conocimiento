---
resumen: >-
  SQL para análisis es lo que el analista necesita del lenguaje de consultas para que un número
  salga bien: saber qué es una fila de cada tabla (su grano) y reconocer las piezas del lenguaje
  que cambian el resultado sin dar error.
estado: vigente
estabilidad: estable
fuentes:
  - "PostgreSQL 19, 7.2 Table Expressions: https://www.postgresql.org/docs/current/queries-table-expressions.html"
  - "Kimball Group, Dimensional modeling techniques: Grain: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/grain/"
  - "Brett Sauve, The problem of SQL fanouts, Google Cloud Community (22-06-2022): https://discuss.google.dev/t/the-problem-of-sql-fanouts/119220.md"
  - "Holistics docs, Fan-out resolution (según resumen): https://docs.holistics.io/docs/joins/fan-out-resolution"
  - "Ejemplos corridos por la base en SQLite 3.53 el 2026-11-27, con sintaxis que también vale en PostgreSQL salvo las fechas"
  - "Datos/.investigacion/analisis.md"
aliases: [SQL analítico, fan-out, fanout, grano, granularidad, grain]
creado: 2026-11-27
revisado: 2026-11-27
---

# SQL para análisis

SQL para análisis es lo que el analista necesita del lenguaje de consultas para que un número
salga bien: saber qué es una fila de cada tabla (su grano) y reconocer las piezas del lenguaje
que cambian el resultado sin dar error.

Es la herramienta principal de la fase de analizar del [análisis](analisis.md). La base de datos
rechaza los errores de sintaxis; los que importan son las consultas que corren y devuelven un número
equivocado. El lenguaje mismo (cláusulas, joins, agregación, NULL, ventanas) se explica en
[SQL](../../Bases-de-datos/SQL/sql.md), del tema Bases de datos, con ejercicios en orden en la
[ruta de SQL](../../Bases-de-datos/Fundamentos/ruta-de-sql.md). Acá queda el grano y para qué usa el
analista cada pieza. La sintaxis completa también está en el tutorial de PostgreSQL (capítulos 2 y
3, y la sección 7.2), que usa una sola tabla de ejemplo en todo el recorrido. Qué motor y qué
versión usar está en la ficha [herramientas del analista](herramientas-del-analista.md).

Los ejemplos usan tres tablas de un comercio:

```sql
ventas(id_venta, fecha, id_cliente, canal, total)        -- una fila por venta
items_venta(id_venta, producto, cantidad, precio)        -- una fila por producto vendido
clientes(id_cliente, nombre, referido_por)               -- una fila por cliente
```

## El grano: qué es una fila

El grano es lo que representa una fila de una tabla. Kimball lo define para las tablas de hechos:
«The grain establishes exactly what a single fact table row represents», y pide declararlo antes
de elegir dimensiones y hechos. Llevarlo a cualquier tabla es una extensión de esta base, y es la primera pregunta
antes de consultar: en `ventas` una fila es una venta; en `items_venta`, un producto dentro de una
venta. Sumar `total` sobre la segunda tabla no da la facturación. El grano se diseña en el
[modelado dimensional](../Modelado-y-almacenamiento/modelado-dimensional.md).

## Una consulta se lee en el orden en que se ejecuta

PostgreSQL describe las cláusulas como «a pipeline of successive transformations performed on the
table derived in the `FROM` clause». Para el analista, la consecuencia es que `WHERE` filtra filas
antes de agrupar y `HAVING` filtra grupos después: «solo las ventas de la tienda» va en `WHERE`, y
«los meses que facturaron más de 800» va en `HAVING`. El orden completo, paso por paso, está en
[consulta SELECT](../../Bases-de-datos/SQL/consulta-select.md#el-orden-en-que-se-evalúan-las-cláusulas).

## Un join que multiplica filas

Un join de uno a muchos repite cada fila del lado «uno» una vez por cada pareja: si una venta tiene
tres ítems, aparece tres veces, y sumar `total` después del join la cuenta tres veces. Sauve lo
llama fan-out: «Since the joined table has more rows than the primary table, we say that a fanout
has occurred». El arreglo es llevar el lado «muchos» al grano del otro antes de unir; la mecánica,
con un pedido cuyo envío se suma dos veces, está en
[join](../../Bases-de-datos/SQL/join.md#un-join-que-multiplica-filas).

Un chequeo rápido es contar filas antes y después del join. Sauve advierte que entender el tipo de
join es mejor que contar, porque el conteo de hoy no avisa del duplicado de mañana. Las
herramientas de BI que corrigen el fan-out solas dependen de que la clave declarada sea única de
verdad; si no lo es, según la documentación de Holistics, el resultado sale mal sin aviso.

## Agregar resume y pierde detalle

`GROUP BY` junta las filas que comparten valores y devuelve una fila por grupo. Un promedio
agregado puede esconder lo que pasa adentro de cada grupo: es la paradoja de Simpson, en
[sesgos](../Estadistica/sesgos.md), y la razón para desagregar en el
[análisis exploratorio](analisis-exploratorio.md). Las reglas del lenguaje (qué columnas pueden ir
en el `SELECT`, `count(*)` contra `count(columna)`, `HAVING` y `FILTER`) están en
[agregación](../../Bases-de-datos/SQL/agregacion.md).

## NULL: el valor que no es igual a nada

NULL marca un dato que falta, y comparar con NULL no da verdadero ni falso sino desconocido. Para
el analista, el efecto es que las filas sin dato se caen sin aviso de los filtros y de los conteos:
con una venta sin canal, `canal <> 'local'` no la trae y `count(canal)` no la cuenta, mientras
`count(*)` sí. Por qué falta un dato, y qué hacer con él, es parte de la
[limpieza de datos](limpieza-de-datos.md#por-qué-falta-un-dato-importa-más-que-cuántos-faltan). La
lógica de tres valores y el `NOT IN` que no devuelve nada están en
[NULL y tipos](../../Bases-de-datos/SQL/null-y-tipos.md#la-lógica-de-tres-valores); el filtro en
`WHERE` que vuelve interno un `LEFT JOIN`, en
[join](../../Bases-de-datos/SQL/join.md#on-contra-where-en-un-left-join).

## Funciones de ventana: calcular sin agrupar

Una [función de ventana](../../Bases-de-datos/SQL/funciones-de-ventana.md) calcula sobre las filas
de un grupo sin colapsarlas en una. Al analista le sirve para lo que en una planilla se hace
arrastrando una fórmula: acumulados, número de compra, compra anterior, participación en el total.

```sql
SELECT id_cliente, fecha, total,
       sum(total)   OVER (PARTITION BY id_cliente ORDER BY fecha) AS acumulado,
       row_number() OVER (PARTITION BY id_cliente ORDER BY fecha) AS n_compra,
       lag(fecha)   OVER (PARTITION BY id_cliente ORDER BY fecha) AS compra_anterior
FROM ventas;
```

Con `n_compra = 1` se encuentra la primera compra de cada cliente, que es la base de una
[tabla de cohortes](../Analitica-de-producto/Lectura-de-cohortes/armar-una-tabla-de-cohortes.md).
Con `lag` se calcula cuántos días pasan entre compras, que entra en la recencia de la
[segmentación RFM](segmentacion-de-clientes.md). Si un cliente tiene dos ventas con la misma `fecha`,
el `acumulado` de esta consulta les da el mismo valor a las dos filas, por el marco por defecto que
explica [funciones de ventana](../../Bases-de-datos/SQL/funciones-de-ventana.md#acumulados-y-el-marco-por-defecto).

> [!NOTE]
> Sin fuente todavía: un libro o curso de referencia sobre SQL para análisis como tema.
