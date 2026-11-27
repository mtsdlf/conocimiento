---
resumen: >-
  Strangler fig es reemplazar un sistema de a partes, sin apagarlo: una fachada reparte los pedidos
  entre lo viejo y lo nuevo, y el tráfico se corre hacia lo nuevo hasta que lo viejo se puede quitar.
  Sirve para migrar de un estilo a otro y para modernizar un sistema heredado.
estado: vigente
estabilidad: estable
fuentes:
  - "Martin Fowler, StranglerFigApplication (actualizada 2024-08-22): https://martinfowler.com/bliki/StranglerFigApplication.html"
  - "Microsoft, Strangler Fig pattern, Azure Architecture Center (2026-05-29): https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig"
  - "AWS Prescriptive Guidance, Strangler fig pattern: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/strangler-fig.html"
  - "Sam Newman, Monolith to Microservices, página del libro: https://samnewman.io/books/monolith-to-microservices/"
aliases: [strangler fig application, strangler application, patrón estrangulador, higuera estranguladora]
creado: 2026-11-27
revisado: 2026-11-27
---

# Strangler fig

Strangler fig es reemplazar un sistema de a partes, sin apagarlo: una fachada reparte los pedidos entre lo viejo y lo nuevo, y el tráfico se corre hacia lo nuevo hasta que lo viejo se puede quitar. Sirve para migrar de un estilo a otro y para modernizar un sistema heredado.

## La higuera de Queensland

El nombre es de Martin Fowler. En 2001 vio en Queensland higueras estranguladoras, que crecen sobre un árbol huésped hasta reemplazarlo, y "a couple of years later" escribió una entrada breve con la metáfora. La entrada se llamó primero "Strangler Application" y después se retituló "Strangler Fig Application". La página lleva la fecha del 22 de agosto de 2024; no da el año de la entrada original.

El argumento de Fowler es de riesgo y de valor. Reemplazar un sistema serio de una vez "takes a long time, and the users can't wait for new features". Ir de a partes tiene costos, entre ellos las piezas de transición, pero "the reduced risk and earlier value from the gradual approach outweigh its costs".

## Fachada, convivencia y retiro

Azure describe el mecanismo: una fachada, normalmente un proxy, recibe todos los pedidos y decide si cada uno va al sistema viejo o al nuevo. Al principio casi todo va a lo viejo; a medida que se reescriben partes, la fachada corre esas rutas a lo nuevo. Cuando lo viejo ya no recibe nada, se retira, y en la versión de Azure la fachada también.

AWS lo cuenta en tres pasos:

1. **Transform**: se construye la parte nueva junto a la vieja.
2. **Coexist**: las dos conviven y un proxy en el perímetro reparte el tráfico.
3. **Eliminate**: se quita la parte vieja.

Las dos fuentes difieren en el proxy. Azure habla de una fachada que se retira al final; AWS pone un API gateway en ese lugar ([API gateway y BFF](../Sistemas-distribuidos/api-gateway-y-bff.md)). Fowler no fija el mecanismo: pide solo el avance gradual y encontrar las costuras por donde cortar.

## La base de datos también se estrangula

Azure incluye el caso más difícil: partir una base de datos monolítica por dominio. Los datos de un dominio se copian a su base nueva con captura de cambios (CDC) mientras las dos conviven, y se puede volver atrás hasta que se borran los objetos viejos. Leer el log de la base con CDC es el mismo mecanismo que usa una de las variantes del [outbox](../Sistemas-distribuidos/outbox.md).

## Lo que exige y cuándo no conviene

Fowler cita a Cartwright, Horn y Lewis, que piden cuatro actividades: entender los resultados que se buscan, partir el problema, entregar las partes y cambiar la organización. La última conecta con la [ley de Conway](../../Platform-Engineering/Organizacion-de-equipos/ley-de-conway.md): Fowler pide tener en cuenta esa ley al reorganizar los equipos durante la migración.

Azure pide que la fachada no sea un punto único de falla y sugiere una capa anticorrupción, para que el modelo del sistema viejo no se filtre al nuevo. AWS advierte que la fachada puede volverse cuello de botella y que cada servicio migrado necesita su plan para volver atrás. Según Azure no conviene cuando los pedidos no se pueden interceptar, cuando el sistema es chico y se reemplaza fácil o cuando hay que apagar lo viejo rápido; AWS coincide en que no sirve para sistemas chicos.

## Para qué lo usa este tema

En la escalera de [Estilos](estilos.md), el strangler fig es cómo se sube un escalón sin apagar nada: sacar un módulo de un [monolito modular](monolito-modular.md) a un servicio, pasar a [service-based](service-based.md) o a [microservicios](microservicios.md). Por inferencia de esta base, el mismo mecanismo sirve para el camino inverso: juntar servicios que no debieron separarse.

> [!NOTE]
> Sin fuente todavía: un caso de ingeniería publicado, con números, de una migración hecha con strangler fig.

Para leer más: la página de Fowler (2024), por el porqué y el vínculo con la organización, y la de Azure, por el mecanismo y el caso de la base de datos. Fijarse en el costo de las piezas de transición y en el plan para volver atrás. El capítulo 3 de *Monolith to Microservices* de Newman, "Splitting the Monolith", trata el tema en detalle; no se leyó.
