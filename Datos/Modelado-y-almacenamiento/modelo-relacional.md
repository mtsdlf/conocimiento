---
resumen: >-
  El modelo relacional guarda los datos en tablas de filas y columnas, identifica cada fila con una
  clave y relaciona las tablas por esas claves, de modo que cada dato se escribe una sola vez.
estado: borrador
estabilidad: estable
fuentes:
  - "E. F. Codd, A Relational Model of Data for Large Shared Data Banks, Communications of the ACM 13(6), junio 1970, pp. 377-387, secciones 1.3 y 1.4 (copia en UPenn): https://www.engineering.upenn.edu/~zives/03f/cis550/codd.pdf"
  - "Datos/.investigacion/modelado-e-ingesta.md (sección 2)"
aliases: [base relacional, modelo de Codd, normalización, relational model, clave primaria, clave foránea]
creado: 2026-11-27
revisado:
---

# Modelo relacional

El modelo relacional guarda los datos en tablas de filas y columnas, identifica cada fila con una
clave y relaciona las tablas por esas claves, de modo que cada dato se escribe una sola vez.

Lo propuso Edgar F. Codd en 1970, y casi toda base de una aplicación lo sigue (lectura de la base). Es la forma del
registro original del que parte el análisis, y la que se consulta con
[SQL](../Analisis/sql-para-analisis.md). Dentro de
[modelado y almacenamiento](modelado-y-almacenamiento.md) es la segunda decisión, antes del
[modelado dimensional](modelado-dimensional.md), que reordena estas tablas para analizar.

## De la planilla a las tablas

Una planilla de ventas típica tiene una fila por venta y repite en cada una el nombre, el teléfono y
la dirección del cliente. Si el cliente se muda, hay que corregir todas sus filas, y alcanza con
olvidar una para que el mismo cliente tenga dos direcciones. El modelo relacional parte esa planilla
en tablas:

| Tabla | Una fila es | Columnas |
|---|---|---|
| clientes | un cliente | id_cliente, nombre, teléfono, dirección |
| pedidos | un pedido | id_pedido, id_cliente, fecha, total |
| líneas de pedido | un producto dentro de un pedido | id_pedido, id_producto, cantidad, precio |
| productos | un producto | id_producto, nombre, categoría |

La dirección queda en un solo lugar. El pedido no la copia: guarda el id_cliente y la busca cuando
la necesita. Esa búsqueda es un *join*, la operación que une tablas por sus claves.

## Claves: cómo una fila se identifica y apunta a otra

La **clave primaria** identifica cada fila de una tabla sin ambigüedad. Codd la define como el
dominio, o la combinación de dominios, cuyos valores identifican de forma única cada fila: «Such a
domain (or combination) is called a primary key». Su ejemplo: el número de pieza es clave primaria;
el color no, porque muchas piezas comparten color.

La **clave foránea** es una columna que guarda la clave primaria de otra tabla. El id_cliente de la
tabla de pedidos es clave foránea: apunta a una fila de clientes. Codd también la nombra en su
paper, en la parte sobre redundancia y consistencia.

Una clave mal elegida rompe el modelo. Si la clave del cliente es el email y el cliente lo cambia,
sus pedidos viejos quedan apuntando a nadie. Por eso es común usar un número sin significado como
clave (lectura de la base). Qué pasa cuando el mismo cliente tiene claves distintas en dos sistemas
es tema de [datos maestros](../Gobierno-y-calidad/datos-maestros.md).

## Normalizar es sacar lo anidado y lo repetido

Normalizar es reorganizar las tablas para que cada dato viva en un solo lugar. Codd lo presenta
así: «There is, in fact, a very simple elimination procedure, which we shall call normalization».
Lo que elimina son los dominios no simples, es decir, una tabla metida adentro de otra, como una
celda «productos» que lista varios productos separados por comas. La versión de 1970 es lo que hoy
se llama primera forma normal: cada celda guarda un solo valor.

> [!NOTE]
> Sin fuente todavía: la segunda y la tercera forma normal, que vienen de trabajos posteriores y no
> se verificaron.

Normalizar tiene un costo para el análisis. Para saber cuánto se vendió por categoría hay que unir
pedidos, líneas y productos. Por eso el modelo para analizar se reordena distinto, con
[hechos y dimensiones](modelado-dimensional.md), y la escuela de Inmon es, según la descripción de Kimball, la que guarda
el almacén central en forma normalizada.

## Dónde se lee la versión larga

El texto fundador es el paper de Codd de 1970, secciones 1.3 (claves) y 1.4 (forma normal). Lo más
útil para quien viene de la planilla es la figura 3, que muestra relaciones anidadas antes y después
de normalizar. Es un paper académico denso; para aprender alcanza con hacer el ejercicio de partir
una planilla de ventas en las cuatro tablas de arriba.
