---
resumen: >-
  Una plantilla de proyecto es un repositorio base versionado del que sale todo proyecto nuevo, con
  la estructura, las dependencias, la configuración y, desde que trabajan agentes, lo que el agente
  lee desde el primer commit.
estado: borrador
estabilidad: estable
fuentes:
  - "Copier, documentación: https://copier.readthedocs.io/en/stable/"
  - "Backstage, Software Templates: https://backstage.io/docs/features/software-templates/"
  - "Gary Niemen, How We Use Golden Paths to Solve Fragmentation in Our Software Ecosystem, Spotify Engineering (2020), citado en golden-path: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem/"
  - "Anthropic, Best practices for Claude Code (leída 2026-11-27): https://code.claude.com/docs/en/best-practices"
  - "Desarrollo/.investigacion/construccion.md (2026-11-27)"
aliases: [generación de proyectos, project template, scaffolding, plantilla de servicio, starter, esqueleto de proyecto]
creado: 2026-11-19
revisado:
---

# Plantilla de proyecto

Una plantilla de proyecto es un repositorio base versionado del que sale todo proyecto nuevo, con la estructura, las dependencias, la configuración y, desde que trabajan agentes, lo que el agente lee desde el primer commit.

Dentro de [Construcción](construccion.md), la plantilla es el punto de partida de cada proyecto: deja armada la [configuración](Configuracion/configuracion.md) común, el repositorio de [Git](Git/git.md) con sus hooks y el [contexto del repositorio](contexto-del-repositorio.md) que necesita un agente. En una organización con plataforma interna, la plantilla es la pieza concreta de un [golden path](../../Platform-Engineering/Plataforma-interna/golden-path.md), el camino soportado para crear un servicio; cómo se estructura el sistema que va adentro se decide en [Arquitectura](../../Arquitectura/Estilos/elegir-un-estilo.md).

## Por qué no copiar otro servicio

Sin plantilla, cada servicio nuevo copia otro existente y arrastra lo que tenga de más o de menos: dependencias viejas, otra estructura de paquetes, otra configuración de logs. La organización termina con decenas de variantes de lo mismo, la fragmentación que Spotify buscó resolver con sus golden paths. Una plantilla fija esas decisiones en un solo lugar versionado, y un proyecto nuevo sale con un comando o un formulario.

> [!NOTE] Sin fuente todavía: no se encontró evidencia empírica de que las plantillas reduzcan defectos o el tiempo de arranque de un proyecto; es práctica reconocida de la ingeniería de plataformas, no un resultado medido.

## Copiar una vez o volver a aplicar

La diferencia que más importa entre los mecanismos es qué pasa cuando la plantilla cambia después de generar el proyecto.

| Mecanismo | Qué hace | Cuando la plantilla cambia |
|---|---|---|
| Generador que copia una vez | copia los archivos, los completa con parámetros y puede correr un script al final | lo generado no se entera; cada proyecto se actualiza a mano |
| Plantilla que se vuelve a aplicar | genera el proyecto y permite volver a aplicar la plantilla sobre él | el proyecto puede traer los cambios de la plantilla |
| Proyecto padre o lista de versiones compartida | no genera nada: los proyectos heredan configuración y versiones | los cambios llegan a todos los hijos al subir la versión del padre |
| Formulario de un portal interno | pide los datos, genera el esqueleto y crea el repositorio | depende del generador que use por debajo |

Copier, por ejemplo, plantea dos objetivos: "Code scaffolding" y "Code lifecycle management", este último con la aclaración "When the template evolves, let consumers update their projects. Not all templates allow updating." Las Software Templates de Backstage son el caso del portal: un formulario con variables, el esqueleto de código y la publicación en un servidor de Git que crea el repositorio. Cómo encaja ese portal en la plataforma está en [developer portal](../../Platform-Engineering/Plataforma-interna/developer-portal.md).

En la práctica se combinan. La plantilla genera la estructura una vez, y lo que tiene que cambiar en todos los proyectos a la vez (versiones de dependencias, configuración del build) se hereda de un padre en lugar de copiarse.

## Lo que trae una plantilla cuando trabajan agentes

Un agente puede generar un proyecto desde cero sin plantilla, y cada vez decidiría distinto la estructura, la seguridad y la integración continua. El criterio de esta base es que la plantilla fije justamente lo que no se quiere que el agente reinvente. Además del código base, una plantilla trae:

- El archivo de instrucciones para agentes, corto y con los comandos de verificación, como pide [contexto del repositorio](contexto-del-repositorio.md).
- Los comandos para correr las pruebas, el typecheck y el linter, que funcionan desde el primer commit.
- Los hooks que imponen lo que no tiene excepción, en el agente y en [Git](Git/hook-de-git.md).
- La definición del entorno de desarrollo, para que una persona o un agente lo levanten igual.
- El pipeline de [integración continua](../../DevOps/Integracion-y-entrega/integracion-continua.md), que corre las mismas verificaciones.
- La separación entre configuración y secretos, con los archivos de secretos fuera del alcance del agente.

Un agente también puede llevar a muchos proyectos ya generados un cambio de la plantilla, partiendo el trabajo en un cambio por repositorio. La guía de Anthropic describe un comando que divide un cambio mecánico grande en unidades con su propia rama y su propio PR ([herramientas de agentes de código](herramientas-de-agentes-de-codigo.md)). Eso alivia la debilidad de los generadores que copian una vez, aunque no la elimina: cada proyecto se alejó a su manera de la plantilla.

## Cómo falla una plantilla

Una plantilla falla cuando nadie la mantiene. Las dependencias envejecen y los proyectos nuevos nacen desactualizados; quien la usa empieza a copiar el último servicio en lugar de la plantilla, y la fragmentación vuelve. También falla por exceso: una plantilla que trae todo lo que algún proyecto necesitó obliga a cada proyecto a borrar lo que no usa. Por eso la plantilla tiene dueño y versión, como cualquier producto de la [plataforma interna](../../Platform-Engineering/Plataforma-interna/plataforma-como-producto.md).

## Una implementación para Java

Para servicios Java con Maven, la plantilla es un [arquetipo de Maven](arquetipo-de-maven.md): un artefacto que `mvn archetype:generate` copia y completa con parámetros, del tipo que copia una vez. Generar nombres de clase a partir del nombre del proyecto no entra cómodo en sus parámetros, y para eso está [derivar nombres en un arquetipo de Maven](derivar-nombres-en-un-arquetipo-de-maven.md).
