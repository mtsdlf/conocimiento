---
resumen: >-
  Una base de documentos guarda cada registro como un documento tipo JSON, con campos anidados y
  listas, y no exige que todos los documentos de una colección tengan los mismos campos. Conviene
  cuando el dato es un árbol que se lee entero, como un pedido con sus ítems.
estado: borrador
estabilidad: estable
fuentes:
  - "MongoDB, Data Modeling: https://www.mongodb.com/docs/manual/data-modeling/"
  - "Michael Stonebraker y Andrew Pavlo, What Goes Around Comes Around... And Around..., SIGMOD Record 53(2), 2024: https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf (sección de documentos)"
  - "Jepsen, MongoDB 4.2.6, 2020-05-15: https://jepsen.io/analyses/mongodb-4.2.6 (según un resumen del análisis; no se leyó entero)"
  - "Wikipedia, NoSQL: https://en.wikipedia.org/wiki/NoSQL (según un resumen)"
  - "Bases-de-datos/.investigacion/ (informes del 2026-11-27)"
aliases: [base documental, document database, document store, base orientada a documentos, MongoDB]
creado: 2026-11-27
revisado:
---

# Base de documentos

Una base de documentos guarda cada registro como un documento tipo JSON, con campos anidados y
listas, y no exige que todos los documentos de una colección tengan los mismos campos. Conviene
cuando el dato es un árbol que se lee entero, como un pedido con sus ítems.

MongoDB es el ejemplo más conocido. Los documentos se agrupan en colecciones, que cumplen el papel
de las tablas de una [base relacional](base-relacional.md) pero sin columnas fijas.

## Un pedido como documento

En una base relacional, un pedido del comercio queda repartido en cuatro tablas: el pedido, sus
ítems, el cliente y los productos. En una de documentos puede ser un solo documento con el cliente,
la dirección de envío y la lista de ítems adentro:

```json
{
  "numero": 1042,
  "fecha": "2026-11-20",
  "cliente": { "id": 7, "nombre": "Ana Pérez" },
  "envio": { "calle": "Av. Corrientes 1234", "ciudad": "CABA" },
  "items": [
    { "producto_id": 31, "nombre": "Taza", "cantidad": 2, "precio": 4500 },
    { "producto_id": 12, "nombre": "Mate", "cantidad": 1, "precio": 9800 }
  ]
}
```

Mostrar el pedido es leer un documento, sin uniones. Es lo que MongoDB pone como principio de su
modelado: "data that's accessed together should be stored together".

## Embeber o referenciar

La decisión central del modelado es qué va adentro del documento y qué se guarda aparte con una
referencia. MongoDB nombra las dos opciones, "embedding or referencing".

- **Embeber** sirve cuando lo de adentro pertenece al documento y se lee con él: los ítems de un
  pedido, la dirección de envío de ese pedido.
- **Referenciar** sirve cuando lo mismo se usa desde muchos documentos y cambia: el producto, con
  su precio y su stock actual. El pedido guarda `producto_id` y, si hace falta, una copia del
  nombre y el precio de ese momento.

En el ejemplo, el nombre del producto quedó copiado en el ítem. Si el producto cambia de nombre,
los pedidos viejos conservan el anterior, que en un pedido es lo correcto. En un catálogo, en
cambio, esa copia sería un dato duplicado que hay que mantener a mano.

## Esquema flexible y lo que cuesta

Según la documentación de MongoDB, "Documents within a single collection are not required to have
the same set of fields or data types", y el modelo puede cambiar "without rewriting existing
documents or running a schema migration". Un catálogo con atributos distintos por tipo de producto
se guarda sin tablas extra.

La flexibilidad corre el control de lugar. Si la base no impone forma, la tiene que imponer la
aplicación, y los documentos viejos con campos de otra época siguen ahí. MongoDB permite agregar
validación de esquema "if needed", que vuelve a poner reglas en la base.

Stonebraker y Pavlo reconocen la ventaja real: el documento coincide con el objeto de la aplicación
y evita el problema N+1 que describe [SQL desde una aplicación](../SQL/sql-desde-una-aplicacion.md).
Sus objeciones son la duplicación cuando la relación no es de uno a muchos, que la unión
precalculada no siempre es más rápida y la pérdida de independencia de datos. La discusión
completa está en [modelos de datos](modelos-de-datos.md#lo-que-sostienen-stonebraker-y-pavlo).

## Dónde se queda corto en un comercio

El problema aparece con las preguntas que cruzan documentos. "Cuánto vendió cada producto este mes"
obliga a recorrer todos los pedidos y abrir sus listas de ítems. "Qué clientes compraron mate y
nunca taza" es una unión que en SQL sale con un [join](../SQL/join.md) y acá queda en una
agregación más compleja o en la aplicación. El stock, que se descuenta desde muchos pedidos a la
vez, es un dato compartido que pide [transacciones](../Transacciones/transaccion.md) entre
documentos.

## El caso Jepsen sobre MongoDB 4.2.6

Las garantías de una base de documentos dependen del motor y de su configuración, y se prueban.
En mayo de 2020, Jepsen publicó un análisis de MongoDB 4.2.6. Según el resumen del análisis, las
transacciones no preservaban snapshot isolation ni con los niveles más estrictos, e ignoraban los
niveles configurados por base o por colección, porque usaban `local` y `w: 1` por defecto.

Siempre según ese resumen, en una corrida sin fallas aparecieron lecturas sesgadas y ciclos de
dependencia en unas 1.461 de 13.914 transacciones. MongoDB atribuyó las anomalías a un bug
(SERVER-48307), corregido en la 4.2.8.

> [!WARNING]
> Es un caso fechado, de 2020 y de la versión 4.2.6. No se verificó cómo se comportan las versiones
> posteriores. Sirve para mostrar que hay que pedir el nivel de garantía de forma explícita y no
> confiar en el valor por defecto, como explica
> [nivel de aislamiento](../Transacciones/nivel-de-aislamiento.md).

## De dónde viene el nombre NoSQL

Las bases de documentos se agrupan bajo el rótulo NoSQL, que nombra lo que no son. Según Wikipedia,
Carlo Strozzi usó el término en 1998 para una base relacional sin SQL, y Johan Oskarsson lo revivió
en 2009 para un encuentro sobre bases distribuidas no relacionales. Según Stonebraker y Pavlo, casi
todos esos sistemas terminaron agregando una interfaz parecida a SQL; MongoDB lo hizo en Atlas en
2021.

Qué motor de documentos está vigente y con qué licencia está en la
[ficha de motores](../Elegir-una-base/motores-de-bases-de-datos.md).
