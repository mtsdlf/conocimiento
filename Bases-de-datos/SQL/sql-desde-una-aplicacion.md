---
resumen: >-
  Una aplicación le manda SQL a la base por un driver o un ORM; los datos que vienen del usuario van
  siempre como parámetros, separados del texto de la consulta, para evitar la inyección SQL, y las
  consultas se agrupan para no caer en el problema N+1.
estado: vigente
estabilidad: estable
fuentes:
  - "OWASP, SQL Injection Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html"
  - "OWASP Top 10 2021, A03 Injection: https://top10.owasp.org/2021/A03_2021-Injection"
  - "OWASP Top 10:2025 (Injection en A05): https://top10.owasp.org/2025/"
  - "Django 5.2, QuerySet API reference (select_related y prefetch_related): https://docs.djangoproject.com/en/5.2/ref/models/querysets/ (leída hasta la mitad)"
  - "Martin Fowler, OrmHate (2012-05-08): https://martinfowler.com/bliki/OrmHate.html (según un resumen)"
  - "Michael Stonebraker y Andrew Pavlo, What Goes Around Comes Around... And Around..., SIGMOD Record 53(2), 2024: https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf (lectura parcial)"
  - "Bill Karwin, SQL Antipatterns, Volume 1 (Pragmatic Bookshelf, 2022): https://pragprog.com/titles/bksap1/sql-antipatterns-volume-1/ (solo la tabla de capítulos)"
  - "Bases-de-datos/.investigacion/sql.md y posicion-contraria-y-fundamentos.md (informes del 2026-11-27)"
aliases: [inyección SQL, SQL injection, consulta parametrizada, prepared statement, ORM, N+1, problema N+1]
creado: 2026-11-27
revisado: 2026-11-27
---

# SQL desde una aplicación

Una aplicación le manda SQL a la base por un driver o un ORM; los datos que vienen del usuario van
siempre como parámetros, separados del texto de la consulta, para evitar la inyección SQL, y las
consultas se agrupan para no caer en el problema N+1.

Un driver es la biblioteca que conecta el programa con el motor y le pasa el SQL. Las notas
anteriores de la vertical tratan el SQL que escribe una persona en una consola. Desde una
aplicación cambian tres cosas: los valores vienen de afuera y pueden ser hostiles, el SQL lo puede
generar una biblioteca, y la misma consulta se ejecuta miles de veces.

## Cómo funciona la inyección SQL

La inyección pasa cuando el texto de la consulta se arma pegando lo que escribió el usuario. Un
buscador de clientes por email que hace esto:

```
consulta = "SELECT id, nombre FROM clientes WHERE email = '" + email + "'"
```

funciona con `ana@example.com`. Con `x' OR '1'='1` en el campo, el texto resultante es:

```sql
SELECT id, nombre FROM clientes WHERE email = 'x' OR '1'='1';
```

y devuelve todos los clientes de la base. La comilla del usuario cerró la cadena y lo que siguió se
interpretó como SQL. Con otro texto se puede borrar una tabla o leer otra. OWASP la ubica en su lista
de riesgos de aplicaciones web: en 2021, "94% of the applications were tested for some form of
injection", y la categoría quedó en el tercer puesto. En la edición 2025 de la lista, Injection
quedó quinta (A05); las cifras de esa edición no se revisaron.

## La defensa: consultas parametrizadas

La defensa principal, según OWASP, es "Define the SQL structure separately from its data values and
bind those values through the database API". El texto de la consulta lleva un marcador, y el valor
viaja aparte:

```java
String query = "SELECT account_balance FROM user_data WHERE user_name = ?";
PreparedStatement statement = connection.prepareStatement(query);
statement.setString(1, customerName);
```

El ejemplo es de OWASP, en Java. La base recibe la estructura y el dato por separado, y el dato
nunca se interpreta como SQL: `tom' or '1'='1` se busca como un nombre literal. PostgreSQL muestra
el mismo mecanismo en SQL puro, con `PREPARE` y `$1`:

```sql
PREPARE buscar_cliente(text) AS
  SELECT id, nombre FROM clientes WHERE email = $1;

EXECUTE buscar_cliente('x'' OR ''1''=''1');   -- 0 filas: se buscó ese texto como email
```

El marcador cambia según el driver y el lenguaje (`?`, `$1`, `%s`, `:nombre`); qué marcador usa cada
uno no se verificó en esta ronda.

Lo que no sirve como defensa principal, según OWASP:

- **Escapar a mano** está "STRONGLY DISCOURAGED": "SQL escaping rules are not always
  straightforward" y cambian entre motores.
- **Validar la entrada** ayuda, pero "Input validation complements parameter binding; it does not
  replace it."

Como defensa adicional, OWASP recomienda el menor privilegio: el usuario con que se conecta la
aplicación no necesita permiso para borrar tablas. Las credenciales de esa conexión no van en el
código; cómo se guardan está en [gestión de secretos](../../DevOps/DevSecOps/gestion-de-secretos.md).

## Lo que no se puede parametrizar

Un parámetro reemplaza un valor, no un nombre de columna ni una palabra de SQL. Ordenar una tabla
de pedidos por la columna que elige el usuario (`ORDER BY fecha DESC`) no se puede hacer con `ORDER
BY $1`. Para esos casos OWASP indica una lista de valores permitidos: la aplicación compara lo que
llega contra las columnas válidas (`fecha`, `total`, `cliente`) y el sentido válido (`ASC`, `DESC`),
y solo entonces lo pega en el texto. Cualquier otro valor se rechaza.

## ORM o SQL a mano

Un ORM (mapeador objeto-relacional) es una biblioteca que convierte filas en objetos del lenguaje y
genera el SQL de las operaciones comunes. OWASP prefiere una API que "avoids using the
interpreter entirely" y cuenta ahí a los ORM; que eso se deba a que el ORM parametriza por su
cuenta es inferencia propia. El debate es sobre cuánto esconde:

> [!IMPORTANT]
> **A favor del ORM.** Fowler, según un resumen de su artículo "OrmHate" (2012): "However much you
> may hate using an ORM, take my word for it - you're better off", porque ahorra el código repetido
> de convertir filas en objetos: "A framework that allows me to avoid 80% of that is worthwhile
> even if it is only 80%". El mismo texto admite que la abstracción tiene fugas y que hay que saber
> SQL cuando hace falta.
>
> **En contra.** El ORM genera consultas que nadie ve, y la falla típica es el problema N+1 (abajo).
> Stonebraker y Pavlo (2024) nombran el problema N+1 entre las razones que empujaron a las bases de
> documentos. El estudio "Feral Concurrency Control" (Bailis y otros, 2015), según el resumen de un
> buscador, trata invariantes que los ORM de Rails validan en la aplicación en lugar de en la base;
> el paper no se abrió.
>
> No se encontró una fuente con evidencia empírica a favor de escribir SQL a mano.

Lo que se desprende de las dos posiciones (inferencia propia): un ORM para las operaciones de una
fila y las pantallas comunes, SQL escrito a mano para reportes, agregaciones y consultas que tienen
que ser rápidas, y en los dos casos mirar el SQL que llega a la base. Las restricciones que importan
(stock no negativo, email único) van declaradas en la base, como dice [definir tablas](definir-tablas.md),
aunque el ORM también las valide.

## El problema N+1

El problema N+1 es pedir una lista con una consulta y después hacer una consulta más por cada
elemento de la lista. Una pantalla que muestra los últimos 50 pedidos con el nombre del cliente:

```sql
SELECT id, cliente_id, fecha FROM pedidos ORDER BY fecha DESC LIMIT 50;   -- 1 consulta
SELECT nombre FROM clientes WHERE id = 1;                                 -- y una por pedido:
SELECT nombre FROM clientes WHERE id = 2;                                 -- 50 consultas más
-- ...
```

Son 51 consultas, cada una rápida. Lo que tarda, por inferencia propia, es el ida y vuelta a la
base 51 veces, y por eso no aparece al mirar una consulta sola ni lo arregla un [índice](indice.md). Con un ORM pasa sin que
se vea: el código recorre los pedidos y lee `pedido.cliente.nombre`, y cada lectura dispara una
consulta. La salida es pedir todo junto, con un [join](join.md):

```sql
SELECT p.id, p.fecha, c.nombre
FROM pedidos p
JOIN clientes c ON c.id = p.cliente_id
ORDER BY p.fecha DESC
LIMIT 50;
```

Los ORM tienen una forma de pedir eso. En Django, según su documentación, `select_related` "results
in a single more complex query" con un join, y `prefetch_related` hace "a separate lookup for each
relationship, and does the 'joining' in Python". Su ejemplo: sin precarga, "Pizza.objects.all() will
run a query on the Toppings table for every item in the Pizza QuerySet", y con
`prefetch_related("toppings")` se reduce "to just two queries". Otros ORM tienen equivalentes con otro
nombre. No se encontró una definición del problema independiente de un ORM concreto.

## Lo que no se cubrió todavía

> [!NOTE] Sin fuente todavía: el pool de conexiones (reusar conexiones abiertas en vez de abrir una
> por pedido) y cómo se manejan las transacciones desde el código. Las
> [transacciones](../Transacciones/transacciones.md) tienen su vertical; la parte de la aplicación
> falta.

## Para leer en la fuente

El "SQL Injection Prevention Cheat Sheet" de OWASP, secciones "Primary Defenses" y la de listas de
valores permitidos; fijarse en el caso de `ORDER BY` y nombres de columna. Karwin trata el tema en
el capítulo "SQL Injection" de *SQL Antipatterns* ("Trust no one"), y en "Implicit Columns" la
costumbre de nombrar las columnas en vez de `SELECT *`.
