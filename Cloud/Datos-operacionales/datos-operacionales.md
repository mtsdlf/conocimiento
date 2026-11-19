---
resumen: >-
  Datos operacionales es la parte de Cloud que guarda los datos de la aplicación en línea: objetos y
  archivos, bases relacionales y NoSQL, motores abiertos administrados y cache.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Datos operacionales

Datos operacionales es la parte de Cloud que guarda los datos de la aplicación en línea: objetos y
archivos, bases relacionales y NoSQL, motores abiertos administrados y cache.

Dentro de [Cloud](../cloud.md), los datos reciben lecturas y escrituras del
[cómputo](../Computo/computo.md) y se alcanzan por un
[private endpoint](../Redes/Acceso-privado-a-PaaS/private-endpoint.md) con el acceso público
apagado. [Operación](../Operacion/operacion.md) define cómo se replica cada servicio según el RTO y
el RPO. La analítica (data lake, transformación, reportes) no es esta parte: aparece como una de las
[arquitecturas de referencia](../arquitecturas-de-referencia-en-azure.md).

## Lo que se decide al principio

El dato es lo más difícil de mover después. El modelo (relacional o documentos), la redundancia y
la clave de partición se eligen al principio y cambiarlos implica migrar. Por eso esta parte se
decide antes que el resto de la carga: qué servicio, con qué redundancia y, en Cosmos DB, con qué
clave.

## La nota de datos operacionales

- [Almacenamiento y bases de datos en Azure](almacenamiento-y-bases-de-datos-en-azure.md) — Storage, Azure SQL, Cosmos DB, PostgreSQL y MySQL, y Managed Redis: qué resuelve cada uno, su redundancia, sus tiers y sus retiros.
