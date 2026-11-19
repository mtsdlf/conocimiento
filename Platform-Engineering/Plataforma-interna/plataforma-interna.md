---
resumen: >-
  La plataforma interna es la parte del platform engineering que trata lo que el platform team
  construye: las capacidades self-service, sus interfaces, sus plantillas y los límites que trae
  incorporados.
estado: borrador
estabilidad: estable
fuentes:
  - "CNCF TAG App Delivery, Platforms White Paper: https://tag-app-delivery.cncf.io/whitepapers/platforms/"
  - "internaldeveloperplatform.org, What is an Internal Developer Platform: https://internaldeveloperplatform.org/what-is-an-internal-developer-platform/"
creado: 2026-11-19
revisado:
---

# Plataforma interna

La plataforma interna es la parte del platform engineering que trata lo que el platform team
construye: las capacidades self-service, sus interfaces, sus plantillas y los límites que trae
incorporados.

La construye un [platform team](../Organizacion-de-equipos/platform-team.md) para los
[stream-aligned teams](../Organizacion-de-equipos/stream-aligned-team.md), y existe para bajar la
carga que estudia [Experiencia de desarrollo](../Experiencia-de-desarrollo/experiencia-de-desarrollo.md).
Ofrece la observabilidad como una capacidad más, que se trata en
[Operación de la plataforma](../Operacion-de-la-plataforma/operacion-de-la-plataforma.md). Un equipo
que ejecuta pasos por los demás en vez de construir self-service cae en el anti-patrón que
describe [Colaboración Dev–Ops](../Colaboracion-Dev-Ops/colaboracion-dev-ops.md).

## Cómo se arma una IDP

La unidad es la capacidad: una función con dueño, contrato y ciclo de vida, separada de la
tecnología que la implementa. Cada capacidad se expone primero como API, y el portal, la CLI y los
bots son presentaciones de esa API. Los equipos la consumen por self-service, sin ticket, dentro
de los límites que fija la gobernanza. Para lo común, un golden path combina plantillas con
capacidades ya conectadas.

Todo eso se diseña como producto: con usuarios internos a los que se investiga, adopción opcional
y métricas de satisfacción y de entrega.

## Dónde falla una plataforma

Un formulario que crea un ticket no es self-service: cambia la interfaz, pero el proceso sigue
manual. Un portal con reglas propias deja afuera a quien usa la CLI o la API. Un comité que
aprueba cada pedido se vuelve una cola. Una plataforma construida como proyecto de
infraestructura ofrece lo que su equipo cree útil, y los desarrolladores la esquivan.

## Las nueve notas de la plataforma interna

- [Internal Developer Platform](internal-developer-platform.md) — qué es una IDP y de qué partes se compone; la puerta de entrada.
- [Plataforma como producto](plataforma-como-producto.md) — qué cambia al tratar la plataforma como producto.
- [Capacidad de plataforma](capacidad-de-plataforma.md) — la unidad de lo que ofrece la plataforma, separada de la tecnología.
- [Self-service](self-service.md) — qué hace que pedir un recurso no necesite un ticket.
- [Plataforma API-first](plataforma-api-first.md) — por qué cada capacidad se expone primero como API.
- [Gobernanza de plataforma](gobernanza-de-plataforma.md) — cómo se da autonomía sin perder control ni trazabilidad.
- [Golden path](golden-path.md) — el camino estándar con plantillas para lo común.
- [Developer portal](developer-portal.md) — la interfaz web de la plataforma, como Backstage.
- [Crossplane](crossplane.md) — una herramienta concreta para ofrecer infraestructura como APIs declarativas sobre Kubernetes.
