---
resumen: >-
  Un API gateway es el punto de entrada único entre los clientes y los servicios: enruta, junta
  respuestas, adapta protocolos y aplica la seguridad. Un BFF (backend for frontend) es un backend
  dedicado a una sola experiencia de usuario, mantenido por el equipo de esa interfaz.
estado: borrador
estabilidad: estable
fuentes:
  - "Chris Richardson, Pattern: API Gateway / Backends for Frontends, microservices.io: https://microservices.io/patterns/apigateway.html"
  - "Sam Newman, Backends For Frontends: https://samnewman.io/patterns/architectural/bff/"
  - "Microsoft, Backends for Frontends pattern, Azure Architecture Center (2025-03-19): https://learn.microsoft.com/en-us/azure/architecture/patterns/backends-for-frontends"
  - "Thoughtworks Technology Radar, ESBs in API gateway's clothing (2020-10): https://www.thoughtworks.com/en-us/radar/techniques/esbs-in-api-gateway-s-clothing"
aliases: [API gateway, BFF, backend for frontend, backends for frontends, puerta de enlace de API]
creado: 2026-11-27
revisado:
---

# API gateway y BFF

Un API gateway es el punto de entrada único entre los clientes y los servicios: enruta, junta respuestas, adapta protocolos y aplica la seguridad. Un BFF (backend for frontend) es un backend dedicado a una sola experiencia de usuario, mantenido por el equipo de esa interfaz.

## El gateway: una sola puerta delante de muchos servicios

Cuando un sistema se parte en [microservicios](../Estilos/microservicios.md), un cliente que llamara a cada servicio tendría que conocer la partición entera y hacer muchos viajes por la red para armar una pantalla. Richardson pone un gateway en el medio: recibe cada pedido y lo enruta a un servicio, o lo abre en abanico a varios y junta los resultados. También adapta protocolos y maneja la seguridad.

Los beneficios, según Richardson: el cliente no ve cómo está partido el sistema, y hace menos viajes por la red, que es lo que más pesa en un teléfono ("An API gateway is essential for mobile applications"). Los costos: otro componente que construir y operar, y un salto de red más en cada pedido.

## El BFF: un backend por experiencia

Newman define el BFF como un componente de servidor "tightly coupled to a specific user experience", que normalmente mantiene el mismo equipo que hace la interfaz. La app móvil tiene el suyo y la web el suyo, y cada uno arma exactamente los datos que su pantalla muestra. La regla "one experience, one BFF" es de Stewart Gleadow, y el nombre lo puso Phil Calçado en SoundCloud, según Newman.

Sus riesgos, según Newman: duplicar lógica entre BFFs, el costo de tener más servicios, y que un BFF que atiende a muchos tipos de cliente se hinche ("the more types of clients you have using a single BFF, the more temptation there may be for it to become bloated").

## Qué va en cada uno

Azure separa las responsabilidades: el BFF tiene solo la lógica propia de su cliente, y lo transversal (autorización, monitoreo) va en el gateway. Un diseño común, que es lectura de esta base sobre las tres fuentes, pone un gateway en el borde y un BFF por experiencia detrás.

Las fuentes no encuadran igual la relación. Richardson trata el BFF como una variante del gateway (un gateway por tipo de cliente); Newman y Azure lo tratan como un patrón propio, distinto de un gateway genérico. Por eso esta base los trata en una sola nota.

El BFF se parece a la capa Experience de [API-led connectivity](api-led-connectivity.md): las dos adaptan los datos a un consumidor y no tienen reglas de negocio. La correspondencia es de esta base; API-led agrega además una capa Process que orquesta, que ni el gateway ni el BFF deberían absorber. En un sistema [multi-tenant](multi-tenancy.md), el tenant se resuelve en el borde, y el gateway es un lugar natural para hacerlo.

## Cuándo no hace falta

Azure desaconseja el BFF cuando las interfaces hacen pedidos iguales o parecidos, cuando hay una sola interfaz, o cuando una capa GraphQL con resolvers por frontend ya cumple ese papel. Si hay un gateway y un solo cliente, el BFF probablemente todavía no hace falta, y con un [monolito modular](../Estilos/monolito-modular.md) tampoco el gateway: no hay partición que ocultar. Esto último es inferencia de esta base.

## Un gateway que se vuelve ESB

El riesgo de fondo es poner en el gateway lo que no le toca. El Technology Radar de Thoughtworks puso en Hold, en octubre de 2020, "ESBs in API gateway's clothing": centralizar orquestación y transformación en una herramienta "adds architectural coupling, reduces transparency, and increases vendor lock-in". Es la misma crítica que dejó atrás a la SOA con ESB ([Lo que pierde peso](../Fundamentos/lo-que-pierde-peso.md)). El gateway enruta y protege; la orquestación va en un servicio o en una [saga](saga.md).

En un sistema con modelos de IA, la misma idea de un punto de entrada único aparece delante de los modelos: [Router y gateway de modelos](../Sistemas-con-modelos/router-y-gateway-de-modelos.md).

> [!NOTE]
> Sin fuente todavía: un postmortem de un gateway que se volvió cuello de botella o punto único de falla; las fuentes solo lo advierten en abstracto.

Para leer más: Newman sobre BFF, en la parte de duplicación y crecimiento, y Richardson para el gateway. Fijarse en la pregunta que agrega Azure: si hay un gateway y un solo cliente, el BFF todavía no hace falta.
