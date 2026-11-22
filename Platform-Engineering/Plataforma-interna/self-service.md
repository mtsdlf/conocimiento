---
resumen: >-
  Self-service es que un equipo obtenga por sí mismo, por API, CLI o portal, un recurso o una
  acción de la plataforma, sin ticket ni intervención manual y dentro de los límites que fija la
  plataforma.
estado: borrador
estabilidad: estable
fuentes:
  - "CNCF TAG App Delivery, Platforms White Paper: https://tag-app-delivery.cncf.io/whitepapers/platforms/"
  - "Matthew Skelton y Manuel Pais, Team Topologies (IT Revolution, 2019): https://teamtopologies.com/book"
aliases: [Self-service (plataforma), Autoservicio]
creado: 2026-10-03
revisado:
---

# Self-service

Self-service es que un equipo obtenga por sí mismo, por API, CLI o portal, un recurso o una
acción de la plataforma, sin ticket ni intervención manual y dentro de los límites que fija la
plataforma.

## Por qué el ticket no escala

Cada ticket es una cola, y la cola crece con la cantidad de equipos. Según la CNCF, el
self-service es lo que permite que un equipo de plataforma atienda a muchos equipos de producto:
los usuarios piden y reciben las capacidades de forma autónoma y automática. Si la plataforma es
lenta, los equipos buscan atajos por fuera (shadow IT) y se pierde el control.

## Las tres condiciones del self-service

Una acción es self-service cuando cumple tres condiciones:

1. El equipo la inicia solo, desde una interfaz de la plataforma.
2. Se completa de forma automática, sin que una persona ejecute pasos.
3. Respeta límites definidos de antemano (cuotas, políticas, permisos), que pone la
   [Gobernanza de plataforma](gobernanza-de-plataforma.md).

Los recursos típicos son bases de datos, buckets, colas, credenciales y entornos; las acciones
típicas son desplegar, volver atrás una versión o crear un servicio desde una plantilla.

El self-service es también la prueba de un equipo de plataforma sano. Según Team Topologies, un
equipo que ejecuta pasos de entrega por los demás, en lugar de construir capacidades self-service,
se vuelve una dependencia: el [Anti-patrón del equipo DevOps](../Colaboracion-Dev-Ops/anti-patron-equipo-devops.md).

## Un bucket en dos minutos

Un equipo necesita un bucket para guardar archivos. Ejecuta un comando de la CLI de la plataforma
y en dos minutos tiene el bucket, con cifrado, etiquetas de dueño y un límite de 100 GB. Antes
abría un ticket y esperaba tres días.

## Un formulario que crea un ticket

Si detrás del portal una persona recibe el pedido y lo ejecuta
a mano, la interfaz cambió pero el proceso sigue siendo manual.

## Ver también

- [Internal Developer Platform](internal-developer-platform.md): el self-service es la forma en que se consumen sus capacidades.
- [Observability-driven development](../../DevOps/Operacion/observability-driven-development.md): ODD pide que cada equipo cree sus alertas y tableros por self-service.
