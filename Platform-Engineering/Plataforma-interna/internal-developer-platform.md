---
resumen: >-
  Una Internal Developer Platform (IDP) es el conjunto integrado de capacidades self-service que un
  platform team ofrece como producto para que los equipos de desarrollo construyan, desplieguen y
  operen software sin depender de tickets.
estado: borrador
estabilidad: estable
fuentes:
  - "CNCF TAG App Delivery, Platforms White Paper: https://tag-app-delivery.cncf.io/whitepapers/platforms/"
  - "internaldeveloperplatform.org, What is an Internal Developer Platform: https://internaldeveloperplatform.org/what-is-an-internal-developer-platform/"
aliases: [IDP, Plataforma interna, Plataforma interna de desarrollo]
creado: 2026-10-03
revisado:
---

# Internal Developer Platform

Una Internal Developer Platform (IDP) es el conjunto integrado de capacidades self-service que un
platform team ofrece como producto para que los equipos de desarrollo construyan, desplieguen y
operen software sin depender de tickets.

## El objeto del platform engineering

Construir y operar una IDP es el objeto del platform engineering. Sin una plataforma, cada equipo
resuelve por su cuenta despliegue, bases de datos y monitoreo, o espera a que otro equipo lo haga.
Según internaldeveloperplatform.org, la IDP baja la carga cognitiva de los desarrolladores sin
quitarles el contexto que necesitan.

## Las partes de una IDP

La CNCF define una plataforma como "una colección integrada de capacidades, definidas y
presentadas según las necesidades de sus usuarios". Las partes de una IDP tienen nota propia:

- [capacidades](capacidad-de-plataforma.md): lo que la plataforma ofrece, como bases de datos,
  despliegue u observabilidad;
- [Self-service](self-service.md): el equipo pide y recibe esas capacidades por su cuenta;
- interfaces: API, CLI y [Developer portal](developer-portal.md), según el principio [Plataforma API-first](plataforma-api-first.md);
- [golden paths](golden-path.md): plantillas que combinan código y capacidades para lo común;
- [gobernanza](gobernanza-de-plataforma.md): los límites y controles incorporados.

El white paper de la CNCF agrupa las capacidades típicas en trece áreas: portales web, APIs y CLIs,
plantillas de golden path, automatización de build y test, automatización de entrega, entornos de
desarrollo, observabilidad, servicios de infraestructura, servicios de datos, mensajería y
eventos, identidad y secretos, servicios de seguridad y almacenamiento de artefactos.

La IDP la construye un [Platform team](../Organizacion-de-equipos/platform-team.md), que según internaldeveloperplatform.org suele empezar
por una plataforma mínima viable y la itera con el feedback de los desarrolladores.

## Un servicio nuevo sin tickets

Un desarrollador crea un servicio nuevo desde el portal: elige la plantilla de API en Python,
recibe el repositorio con su pipeline, pide una base de datos por la CLI y ve sus métricas en un
tablero ya armado. No abrió ningún ticket.

## Lo que no es una IDP

- El developer portal: es una de las interfaces de la IDP, no la plataforma entera.
- Un Identity Provider, que también se abrevia "IDP" y es el sistema que autentica usuarios
  (Keycloak, Okta). En este Tema, "IDP" es siempre la plataforma.

## Ver también

- [Plataforma como producto](plataforma-como-producto.md): el enfoque con que se diseña la IDP.
