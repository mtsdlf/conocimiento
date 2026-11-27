---
resumen: >-
  Un modelo de datos es la forma en que una base organiza lo que guarda: tablas que se cruzan,
  documentos anidados, pares de clave y valor, o estructuras especializadas como grafos y vectores.
  Se elige por las preguntas que se le van a hacer a los datos, no por cuántos hay.
estado: borrador
estabilidad: estable
fuentes:
  - "Michael Stonebraker y Andrew Pavlo, What Goes Around Comes Around... And Around..., SIGMOD Record 53(2), junio de 2024, pp. 21-37: https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf (leídos el abstract, la sección de documentos y las conclusiones)"
  - "MongoDB, Data Modeling: https://www.mongodb.com/docs/manual/data-modeling/"
  - "Redis, Redis as an in-memory data store: https://redis.io/docs/latest/develop/get-started/data-store/"
  - "Neo4j, What is a graph database: https://neo4j.com/docs/getting-started/get-started-with-neo4j/graph-database/"
  - "Martin Kleppmann, Designing Data-Intensive Applications (O'Reilly), cap. 2 Data Models and Query Languages: https://dataintensive.net/ (según la ficha del libro; no se leyó ni se confirmó la numeración de la edición vigente)"
  - "Bases-de-datos/.investigacion/ (informes del 2026-11-27)"
aliases: [modelo de datos, data model, modelos de bases de datos, NoSQL]
creado: 2026-11-27
revisado:
---

# Modelos de datos

Un modelo de datos es la forma en que una base organiza lo que guarda: tablas que se cruzan,
documentos anidados, pares de clave y valor, o estructuras especializadas como grafos y vectores.
Se elige por las preguntas que se le van a hacer a los datos, no por cuántos hay.

El modelo es la primera decisión de [Bases de datos](../bases-de-datos.md) y condiciona las demás.
Decide qué lenguaje de consulta hay: el modelo relacional trae [SQL](../SQL/sql.md), y los otros traen
cada uno el suyo. Decide también qué garantías da la base cuando varias
[transacciones](../Transacciones/transacciones.md) escriben a la vez, y por eso es el primer
criterio al [elegir una base](../Elegir-una-base/elegir-una-base.md).

## Cuatro familias y qué forma le dan al dato

Un comercio con pedidos, clientes, productos y stock se puede guardar en cualquiera de las
familias. Lo que cambia es qué preguntas salen fáciles y cuáles obligan a trabajar en la aplicación.

| Modelo | Unidad que guarda | Cómo se consulta | Le sale fácil al comercio | Le cuesta |
|---|---|---|---|---|
| [Relacional](base-relacional.md) | Filas en tablas con columnas fijas, unidas por claves | SQL, con uniones entre tablas | Cruzar pedidos con clientes, productos y stock en cualquier dirección | Guardar algo de forma variable o muy anidada |
| [Documentos](base-de-documentos.md) | Documentos tipo JSON, con campos anidados y listas | Por campos del documento; las uniones son limitadas | Leer un pedido entero con sus ítems de una vez | Preguntas que cruzan muchos documentos distintos |
| [Clave-valor](base-clave-valor.md) | Un valor opaco o una estructura chica bajo una clave | Solo por la clave | El carrito de una sesión, un contador, una caché | Cualquier pregunta que no empiece por la clave |
| [Especializados](modelos-especializados.md) | Nodos y relaciones, mediciones en el tiempo, texto indexado, vectores | Lenguaje o índice propio de cada uno | Una pregunta de un tipo muy particular | Todo lo demás, que suele quedar en otra base |

Las familias no son excluyentes. MongoDB permite imponer estructura con validación de esquema
"if needed", y Redis se ofrece también como base de documentos y de vectores. Un motor relacional
guarda JSON y, con extensiones, vectores o series de tiempo, como cuenta
[modelos especializados](modelos-especializados.md).

## Las preguntas deciden el modelo

La regla que más pesa es mirar cómo se va a leer el dato. MongoDB la formula como principio:
"data that's accessed together should be stored together". Si el comercio siempre muestra el
pedido completo con sus ítems y su dirección de envío, ese pedido entra bien en un documento.

Si además hay que saber cuánto compró cada cliente, qué productos se quedan sin stock y qué
pedidos incluyen un producto dado, el mismo dato se lee desde varios lados. Esas preguntas se
contestan con [uniones](../SQL/join.md) entre tablas, que es lo que el modelo relacional hace bien.
Guardar el pedido como documento obliga a duplicar datos del producto o a resolver las uniones en
la aplicación.

El volumen pesa menos de lo que suele creerse, aunque esto es una inferencia y no una cifra de
fuente: un comercio con cien mil pedidos entra cómodo en cualquier familia, y cuando una consulta
anda lenta lo primero que se mira es un [índice](../SQL/indice.md), no el modelo.

## Lo que sostienen Stonebraker y Pavlo

En 2024, Michael Stonebraker y Andrew Pavlo repasaron veinte años de modelos alternativos al
relacional. Su conclusión es que SQL y el modelo relacional absorben las buenas ideas de las
alternativas. Según el paper, los dos mensajes de venta de NoSQL fueron "SQL and joins are slow" y
"ACID transactions are unnecessary", y casi todos esos sistemas terminaron agregando una interfaz
parecida a SQL y transacciones.

Sobre cada familia son tajantes. Las bases de documentos están "on a collision course with
RDBMSs"; las de clave-valor "can generally be equaled or beaten by modern high-performance RDBMSs";
las de familia de columnas son "a niche market".

> [!IMPORTANT]
> **Sesgo declarado y matiz.** Stonebraker fundó empresas de bases relacionales y columnares
> (el informe de investigación nombra Ingres, Vertica y VoltDB, sin fuente leída para el dato), así
> que es una fuente autorizada pero interesada. El
> propio paper reconoce que los documentos resuelven el desajuste entre el objeto de la aplicación
> y las tablas, y evitan el problema N+1 que describe
> [SQL desde una aplicación](../SQL/sql-desde-una-aplicacion.md). Sus objeciones son tres: datos
> duplicados cuando la relación no es de uno a muchos, uniones precalculadas que no siempre son más
> rápidas y la pérdida de independencia entre los datos y el programa. Leído así, el documento
> conviene cuando el dato es un árbol que se lee entero. Kleppmann, en el capítulo de modelos de
> datos de *Designing Data-Intensive Applications*, presenta el mismo intercambio con menos toma de
> partido; esa lectura no se verificó para esta nota.

## Qué hay adentro de los modelos de datos

- [Base relacional](base-relacional.md) — tablas, claves, relaciones e integridad; el modelo por
  defecto para el sistema de un comercio.
- [Base de documentos](base-de-documentos.md) — documentos JSON con esquema flexible, embeber o
  referenciar, y el caso Jepsen sobre las garantías de MongoDB.
- [Base clave-valor](base-clave-valor.md) — una clave y un valor, en memoria; caché y sesiones, y
  lo que se pierde si se cae.
- [Modelos especializados](modelos-especializados.md) — grafos, series de tiempo, búsqueda de
  texto y vectores; cuándo alcanza una base relacional con una extensión.

Los servicios de Azure que implementan cada familia están en
[Almacenamiento y bases de datos en Azure](../../Cloud/Datos-operacionales/almacenamiento-y-bases-de-datos-en-azure.md).
