---
resumen: >-
  Una base clave-valor guarda cada dato bajo una clave y solo lo encuentra por esa clave; suele
  vivir en memoria y se usa como caché, para sesiones y contadores. Redis es el caso típico, y lo
  que pierde si se cae depende de cómo se configure su persistencia.
estado: vigente
estabilidad: estable
fuentes:
  - "Redis, Redis as an in-memory data store: https://redis.io/docs/latest/develop/get-started/data-store/"
  - "Redis, Redis persistence: https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/"
  - "Michael Stonebraker y Andrew Pavlo, What Goes Around Comes Around... And Around..., SIGMOD Record 53(2), 2024: https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf"
  - "Pavel Stehule, hilo de pgsql-general de 2019: https://www.postgresql.org/message-id/CAFj8pRA9Chqr2m2_AieG02fyDq3oJcM6RrE3Z%2BGsceiqTv17-A%40mail.gmail.com (según un resumen del buscador)"
  - "Bases-de-datos/.investigacion/ (informes del 2026-11-27)"
aliases: [key-value, key-value store, almacén clave-valor, caché, Redis]
creado: 2026-11-27
revisado: 2026-11-27
---

# Base clave-valor

Una base clave-valor guarda cada dato bajo una clave y solo lo encuentra por esa clave; suele
vivir en memoria y se usa como caché, para sesiones y contadores. Redis es el caso típico, y lo
que pierde si se cae depende de cómo se configure su persistencia.

Es el modelo más simple de los cuatro de [modelos de datos](modelos-de-datos.md): un diccionario
gigante. Lo que gana en velocidad y simpleza lo pierde en preguntas: no hay forma de pedir "todos
los carritos con más de tres productos" sin recorrer todas las claves.

## Qué guarda un comercio en una clave

En el sistema de un comercio, la base clave-valor acompaña a la base principal y no la reemplaza:

- **El carrito de una sesión**: clave `carrito:<id de sesión>`, valor con los productos y
  cantidades. Si se pierde, el cliente vuelve a cargar el carrito.
- **Una caché**: clave `producto:31`, valor con la ficha ya armada, para no consultar la base
  relacional en cada visita.
- **Un contador**: visitas a un producto o intentos de inicio de sesión por minuto.

Los pedidos, los clientes y el stock no van acá: son la verdad del negocio y piden reglas y
[transacciones](../Transacciones/transacciones.md).

## Redis, un diccionario con tipos

Redis "stands for Remote Dictionary Server". No guarda solo texto: sus strings guardan "text,
serialized objects, counter values, and binary arrays", y sus hashes sirven para "plain objects",
como una ficha con campos. Su documentación lo ofrece también como base de documentos y de
vectores.

## Lo que se pierde si se cae

Redis trabaja en memoria, y cuánto se pierde ante un corte lo decide su persistencia. La
documentación ofrece cuatro opciones:

| Persistencia | Qué hace | Lo que se puede perder |
|---|---|---|
| Ninguna | Todo vive en memoria; "sometimes used when caching" | Todo |
| RDB | Fotos del contenido cada cierto tiempo | Hay que estar "prepared to lose the latest minutes of data" |
| AOF | Un registro de cada escritura; por defecto `appendfsync everysec` | Con ese defecto, "you can only lose one second worth of writes" |
| RDB más AOF | Las dos a la vez | Lo de AOF, con fotos para recuperar más rápido |

Para una caché, perder todo es aceptable: se reconstruye desde la base principal. Para carritos, por
inferencia propia, perder un segundo puede ser aceptable. Si se quiere usar Redis como base principal, la propia documentación pide
combinar RDB y AOF para lograr "a degree of data safety comparable to what PostgreSQL can provide
you". Esa persistencia es un requisito que se pide al
[elegir una base administrada](../Elegir-una-base/base-administrada.md).

## Por qué no usar la base principal como caché, ni al revés

Hay dos tentaciones opuestas. Una es usar Redis para datos que no se pueden perder sin configurar la
persistencia. La otra es usar la base relacional como caché: según un resumen de un hilo de 2019 en
la lista de PostgreSQL, Pavel Stehule desaconseja PostgreSQL para caché o datos efímeros con mucha
actualización.

> [!IMPORTANT]
> Stonebraker y Pavlo sostienen que el rendimiento de las bases clave-valor "can generally be
> equaled or beaten by modern high-performance RDBMSs". Es una afirmación general de autores con
> sesgo relacional declarado (ver [modelos de datos](modelos-de-datos.md#lo-que-sostienen-stonebraker-y-pavlo))
> y no dice nada de una instalación concreta. Para el comercio, la decisión práctica suele ser
> otra: si la base principal ya aguanta la carga, sumar una segunda base es un sistema más para
> operar. Esto último es una inferencia, no una cifra de fuente.

Versión vigente y licencia de Redis, que cambió con la serie 8, en la
[ficha de motores](../Elegir-una-base/motores-de-bases-de-datos.md). En Azure, el servicio de este
modelo está en
[Almacenamiento y bases de datos en Azure](../../Cloud/Datos-operacionales/almacenamiento-y-bases-de-datos-en-azure.md).
