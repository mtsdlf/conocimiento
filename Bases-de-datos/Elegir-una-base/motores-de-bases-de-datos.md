---
resumen: >-
  Versión vigente, licencia y fuente de PostgreSQL, MySQL, SQLite, MongoDB y Redis, y lo que trae
  el plan gratis de Neon y Supabase, copiado de las páginas oficiales el 2026-11-27.
estado: borrador
estabilidad: volatil
fuentes:
  - "PostgreSQL, Versioning Policy: https://www.postgresql.org/support/versioning/"
  - "MySQL 8.4 Release Notes: https://dev.mysql.com/doc/relnotes/mysql/8.4/en/ (según un resumen)"
  - "MySQL 9.7 Release Notes: https://dev.mysql.com/doc/relnotes/mysql/9.7/en/ (según un resumen)"
  - "SQLite, Release History: https://www.sqlite.org/changes.html (según un resumen de la primera parte de la página)"
  - "MongoDB, Release Notes: https://www.mongodb.com/docs/manual/release-notes/ (según un resumen)"
  - "Redis, Releases en GitHub: https://github.com/redis/redis/releases (según un resumen)"
  - "Redis, Licenses: https://redis.io/legal/licenses/"
  - "Neon, Plans: https://neon.com/docs/introduction/plans (según un resumen; página actualizada el 2026-11-24)"
  - "Supabase, Pricing: https://supabase.com/pricing (según un resumen)"
aliases: [versiones de bases de datos, database engines, motores, PostgreSQL, MySQL, SQLite, MongoDB, Redis, Neon, Supabase]
creado: 2026-11-27
revisado:
---

# Motores de bases de datos

Versión vigente, licencia y fuente de PostgreSQL, MySQL, SQLite, MongoDB y Redis, y lo que trae
el plan gratis de Neon y Supabase, copiado de las páginas oficiales el 2026-11-27.

Implementa [criterios de elección](criterios-de-eleccion.md) y
[base administrada](base-administrada.md). Los valores se leyeron el 2026-11-27, casi todos a través
de un resumen automático de cada página; antes de decidir, conviene abrir la fuente viva.

## Motores

| Motor | Modelo | Versión vigente al 2026-11-27 | Licencia | Fuente viva |
|---|---|---|---|---|
| PostgreSQL | [Relacional](../Modelos-de-datos/base-relacional.md) | 19.0, lanzada el 2026-11-19; la serie 18 va por la 18.7 y tiene soporte hasta el 2030-11-14 | Sin verificar | [Versioning Policy](https://www.postgresql.org/support/versioning/) |
| MySQL | Relacional | 8.4.13.1 y 9.7.4.1, las dos del 2026-11-24 | Sin verificar | [Notas de la 8.4](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/) y [de la 9.7](https://dev.mysql.com/doc/relnotes/mysql/9.7/en/) |
| SQLite | Relacional, en un archivo | 3.54.1, del 2026-10-16 | Sin verificar | [Release History](https://www.sqlite.org/changes.html) |
| MongoDB | [Documentos](../Modelos-de-datos/base-de-documentos.md) | Serie 9.0 (9.0.0 el 2026-09-28; 9.0.8 el 2026-11-10) | Sin verificar | [Release Notes](https://www.mongodb.com/docs/manual/release-notes/) |
| Redis | [Clave-valor](../Modelos-de-datos/base-clave-valor.md) | 8.12.0, del 22 de noviembre (la página no dice el año) | Desde la 8.0, "RSALv2 or SSPLv1 or AGPLv3", a elección | [Releases](https://github.com/redis/redis/releases) y [Licenses](https://redis.io/legal/licenses/) |

Notas sobre la tabla:

- **PostgreSQL**: la versión de PostgreSQL que conviene para un sistema nuevo no la dice la página.
  La 19.0 tenía ocho días al copiar esta ficha; la 18.7 es la última de una serie con más tiempo en
  uso.
- **MySQL**: la serie 9.x es la de innovación. Que la 8.4 sea la serie de soporte largo (LTS) no lo
  dice su página de notas; viene del conocimiento previo de quien investigó y queda sin confirmar.
- **MongoDB**: según la página de notas, la serie anterior a la 9.0 es la 8.3 (y no la 8.2 ni la
  8.1), y antes la 8.0 y la 7.0. No se contrastó con otra fuente. La 9.0.7 corrigió 27 CVE (vulnerabilidades con identificador público), según la
  misma página.
- **Redis**: hubo un parche de seguridad el 26 de octubre para la 8.10.3 y ramas anteriores.

> [!NOTE]
> Sin fuente todavía: la licencia de PostgreSQL, MySQL, SQLite y MongoDB (no se leyó la página de
> licencia de ninguno), la confirmación de MySQL 8.4 como LTS en su política de versiones, la serie
> 8.3 de MongoDB en una segunda fuente, y el año de la 8.12.0 de Redis.

## Servicios administrados: lo que trae el plan gratis

| Servicio | Motor | Plan gratis | Restauración a un punto | Planes pagos | Fuente viva |
|---|---|---|---|---|---|
| Neon | PostgreSQL | 100 CU-horas (una unidad de cómputo de Neon encendida una hora) por proyecto por mes y 1 GB por proyecto | 6 horas | Launch y Scale, sin cargo mínimo mensual ("No minimum monthly fee"); PITR de hasta 7 días en Launch y hasta 30 en Scale | [Plans](https://neon.com/docs/introduction/plans) |
| Supabase | PostgreSQL | 500 MB; se pausa tras una semana sin actividad | No: el plan gratis no tiene respaldos automáticos ni PITR | Pro desde USD 25 por mes, con 8 GB y respaldos diarios por 7 días; PITR como extra de USD 100 por mes por 7 días. Team desde USD 599 por mes, con respaldos por 14 días | [Pricing](https://supabase.com/pricing) |

Precios de Neon por uso, según la misma página: Launch a USD 0,106 por CU-hora y USD 0,35 por
GB-mes, con PITR a USD 0,20 por GB-mes; Scale a USD 0,222 por CU-hora.

Para un comercio que toma pedidos en línea, el plan gratis de Supabase no cumple el requisito de
respaldo de [base administrada](base-administrada.md), y el de Neon permite volver solo seis horas
atrás. Esta lectura es una inferencia a partir de los valores copiados.

> [!NOTE]
> Sin fuente todavía: el SLA (acuerdo de nivel de servicio: la disponibilidad que promete el
> proveedor) y la política de réplicas de Neon y Supabase, y la retención de
> respaldos y los precios de Amazon RDS. Los servicios de Azure están en
> [Almacenamiento y bases de datos en Azure](../../Cloud/Datos-operacionales/almacenamiento-y-bases-de-datos-en-azure.md).
