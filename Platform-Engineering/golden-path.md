---
tipo: concepto
resumen: >-
  Un golden path es el camino soportado y con opinión para hacer algo común, como crear un
  servicio backend, con plantillas y automatización listas; se puede salir de él, pero se pierde
  el soporte.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Gary Niemen, How We Use Golden Paths to Solve Fragmentation in Our Software Ecosystem, Spotify Engineering (2020): https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem/"
  - "Ajay Chankramath, Nic Cheneweth, Bryan Oliver y Sean Alvarez, Effective Platform Engineering (Manning), sección 3.3.3: https://livebook.manning.com/book/effective-platform-engineering/chapter-3/v-1/"
  - "CNCF TAG App Delivery, Platforms White Paper: https://tag-app-delivery.cncf.io/whitepapers/platforms/"
aliases: [Paved road, Camino pavimentado, Starter kit]
parte_de: [internal-developer-platform]
requiere: [carga-cognitiva]
relacionado: [developer-portal, observability-driven-development]
---

# Golden path

Un golden path es el camino soportado y con opinión para hacer algo común, como crear un
servicio backend, con plantillas y automatización listas; se puede salir de él, pero se pierde
el soporte.

## Por qué importa

Sin un camino estándar, cada equipo arma su servicio a su manera y la organización termina con
decenas de variantes de lo mismo. Spotify introdujo los golden paths para resolver esa
fragmentación. Además bajan la [[carga-cognitiva]] extrínseca: el desarrollador no tiene que
decidir ni aprender todo lo que la plantilla ya resuelve.

## Cómo funciona

Spotify lo define como "el camino soportado y con opinión para construir algo", por ejemplo un
servicio backend, un sitio web o un pipeline de datos. Es opcional: quien quiera puede salirse,
pero no recibe el mismo soporte.

Effective Platform Engineering lo describe como un acelerador: las formas estándar de usar los
recursos de la plataforma se ofrecen como acciones preconfiguradas y automatizadas. La CNCF lo
describe como plantillas que combinan código con capacidades integradas, junto con su
documentación.

Un golden path suele tener:

- una plantilla de proyecto que genera el repositorio, el pipeline y la configuración;
- las capacidades ya conectadas (base de datos, observabilidad, secretos);
- documentación del camino y de cuándo conviene salirse;
- versiones, para que los servicios creados antes puedan actualizarse.

## Ejemplo

Según Effective Platform Engineering, un desarrollador llama a la API de un starter kit de Python
y recibe un repositorio completo con su pipeline de CI/CD. Empieza a escribir lógica de negocio
sin entender Helm, Kubernetes ni OpenAPI para desplegar.

## No confundir con

Un estándar obligatorio. El golden path se elige porque ahorra trabajo, no porque esté impuesto.
Tampoco debe esconder del todo lo que genera: ese límite es la [[mechanical-sympathy]].

## Relaciones

- Parte de: [[internal-developer-platform]] — una de las piezas que ofrece la plataforma.
- Requiere: [[carga-cognitiva]] — es la carga que el golden path reduce.
- Relacionado: [[developer-portal]] — el lugar habitual desde donde se elige y se lanza una plantilla.
- Relacionado: [[observability-driven-development]] — una plantilla con la telemetría ya conectada cumple de fábrica buena parte de lo que pide ODD.
