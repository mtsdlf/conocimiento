---
resumen: >-
  Una base administrada es una base que opera un proveedor: instala, actualiza, respalda y
  replica, y quien la usa solo se conecta. Conviene cuando no hay quien opere una propia, pero el
  respaldo, la restauración a un punto, la réplica y la alta disponibilidad no vienen solos: se
  piden y se pagan según el plan.
estado: borrador
estabilidad: estable
fuentes:
  - "Amazon RDS, Multi-AZ deployments: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html (según un resumen)"
  - "Jepsen, Amazon RDS for PostgreSQL 17.4, 2025-04-29 (actualizado 2025-05-03): https://jepsen.io/analyses/amazon-rds-for-postgresql-17.4 (según un resumen)"
  - "Jepsen, MySQL 8.0.34, 2023-12-19: https://jepsen.io/analyses/mysql-8.0.34 (según un resumen)"
  - "Redis, Redis persistence: https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/"
  - "Supabase, Pricing: https://supabase.com/pricing (según un resumen)"
  - "Neon, Plans: https://neon.com/docs/introduction/plans (según un resumen)"
  - "Bases-de-datos/.investigacion/modelos-transacciones-elegir.md (informe del 2026-11-27)"
aliases: [base de datos administrada, managed database, DBaaS, base como servicio, base propia, self-hosted]
creado: 2026-11-27
revisado:
---

# Base administrada

Una base administrada es una base que opera un proveedor: instala, actualiza, respalda y
replica, y quien la usa solo se conecta. Conviene cuando no hay quien opere una propia, pero el
respaldo, la restauración a un punto, la réplica y la alta disponibilidad no vienen solos: se
piden y se pagan según el plan.

Es uno de los [criterios de elección](criterios-de-eleccion.md), el de la operación, y suele decidir
el costo. El motor puede ser el mismo en las dos opciones; lo que cambia es quién responde cuando
algo se rompe.

## Propia o administrada

| | Base propia | Base administrada |
|---|---|---|
| Quién instala y actualiza | El equipo, en un servidor o una máquina virtual | El proveedor |
| Respaldo | Hay que armarlo, probarlo y vigilarlo | Viene según el plan; en algunos planes gratis no hay |
| Réplica y alta disponibilidad | Configuración a mano | Una opción del plan, con su costo |
| Control | Total: versión, extensiones, configuración | El que deje el proveedor |
| Costo | El servidor más las horas de quien la opera | La factura del plan, que crece con el uso |

Para el sistema de un comercio sin nadie dedicado a la operación, la administrada suele ganar:
las horas de operación son el costo que no se ve. Esto es una inferencia, no una cifra de fuente.
La propia tiene sentido cuando ya hay servidores y alguien que los cuida, o cuando el proveedor no
ofrece una extensión que hace falta.

## Cuatro requisitos que se piden por escrito

Antes de elegir un plan conviene escribir qué se exige de cada uno de estos puntos, porque los
planes difieren mucho y lo gratis suele recortar justo acá:

1. **Respaldo automático**: copias diarias y cuántos días se guardan. Hay planes gratis que no
   hacen ninguna.
2. **Restauración a un punto en el tiempo** (PITR, por *point-in-time recovery*): volver la base al
   estado de un minuto dado, por ejemplo justo antes de un `DELETE` sin `WHERE`. La ventana va de
   unas horas a semanas según el plan, y a veces se cobra aparte.
3. **Réplica**: una copia que se mantiene al día en otra máquina o zona, para no perder datos si se
   cae la principal y, en algunos casos, para repartir lecturas.
4. **Alta disponibilidad**: que una réplica tome el lugar de la principal sola y rápido.

Los dos números que ordenan esos requisitos son cuánto tiempo puede estar caído el sistema (RTO) y
cuántos datos se pueden perder (RPO), como explica
[Alta disponibilidad y DR en Azure](../../Cloud/Operacion/alta-disponibilidad-y-dr-en-azure.md).
Un comercio que toma pedidos en línea difícilmente acepta perder un día de pedidos, y eso descarta
los planes sin respaldo.

Con una base clave-valor el requisito es el mismo con otro nombre: la persistencia. Redis recomienda
combinar sus dos mecanismos para "a degree of data safety comparable to what PostgreSQL can provide
you", como detalla [base clave-valor](../Modelos-de-datos/base-clave-valor.md).

## Una réplica no siempre atiende lecturas

La palabra réplica no dice lo mismo en todos los servicios. Según un resumen de la documentación de
Amazon RDS, el despliegue en varias zonas puede ser de una instancia en espera, que no atiende
lecturas, o de un clúster con dos en espera, que sí las atienden. Si la idea es repartir la carga de
lectura, hay que confirmar cuál se contrata.

## Alta disponibilidad no garantiza el aislamiento esperado

Un clúster con réplicas puede dar garantías más débiles que una sola instancia del mismo motor. Según
el resumen del análisis de Jepsen sobre Amazon RDS for PostgreSQL, publicado el 2025-04-29, "Amazon
RDS for PostgreSQL multi-AZ clusters violate Snapshot Isolation". La anomalía (Long Fork) apareció en
clústeres sanos, en todas las versiones probadas, y el autor llama a su trabajo "a cursory
exploration".

Una actualización del 2025-05-03 atribuye la causa a que la instancia principal y las secundarias
ordenan de forma distinta qué transacciones son visibles. Según el resumen del análisis de Jepsen
sobre MySQL, los clústeres de RDS MySQL "routinely violate Serializability", en parte por una opción
de replicación apagada por defecto.

> [!IMPORTANT]
> La consecuencia práctica es una inferencia: si el sistema depende de un nivel de aislamiento para
> no vender stock que no hay, ese supuesto se prueba en la configuración real, con réplicas, y no
> solo en una instancia de desarrollo. Las anomalías y cómo evitarlas sin depender del nivel están en
> [nivel de aislamiento](../Transacciones/nivel-de-aislamiento.md) y
> [concurrencia](../Transacciones/concurrencia.md).

## Qué traen los planes de hoy

Los planes, sus precios y su ventana de restauración cambian seguido, así que viven en la
[ficha de motores](motores-de-bases-de-datos.md), con la fecha de la copia. Los servicios
administrados de Azure, con sus opciones de réplica, están en
[Almacenamiento y bases de datos en Azure](../../Cloud/Datos-operacionales/almacenamiento-y-bases-de-datos-en-azure.md).

> [!NOTE]
> Sin fuente todavía: la retención de respaldos y los precios de Amazon RDS, y el acuerdo de nivel
> de servicio (SLA) y la política de réplicas de los servicios administrados de la ficha.
