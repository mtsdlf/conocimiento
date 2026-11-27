---
resumen: >-
  Construcción es la parte del ciclo técnico en que una tarea definida se convierte en código que
  compila y pasa sus pruebas, escrito cada vez más por agentes que leen el repositorio y corren sus
  comandos.
estado: vigente
estabilidad: semi
fuentes:
  - https://code.claude.com/docs/en/best-practices
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - https://arxiv.org/abs/2602.11988
  - https://www.thoughtworks.com/en-au/radar/techniques/agent-instruction-bloat
  - https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
  - https://metr.org/blog/2026-02-24-uplift-update/
  - https://containers.dev/
  - https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen
  - https://docs.renovatebot.com/key-concepts/minimum-release-age/
  - "Desarrollo/.investigacion/construccion.md (2026-11-27)"
aliases: [construcción de software, implementación, codificación, software construction, coding]
creado: 2026-11-27
revisado: 2026-11-27
---

# Construcción

Construcción es la parte del ciclo técnico en que una tarea definida se convierte en código que compila y pasa sus pruebas, escrito cada vez más por agentes que leen el repositorio y corren sus comandos.

Dentro de [Desarrollo](../desarrollo.md), Construcción recibe de [Definición](../Definicion/definicion.md) la tarea con sus [criterios de aceptación](../Definicion/criterios-de-aceptacion.md) y le entrega a [Verificación](../Verificacion/verificacion.md) un cambio que se puede comprobar. Cómo se estructura el sistema que se construye está en [Arquitectura](../../Arquitectura/arquitectura.md); cómo se integra y se despliega el cambio, en [integración y entrega](../../DevOps/Integracion-y-entrega/integracion-y-entrega.md).

## El repositorio como lo que lee el agente

Con agentes, el repositorio tiene un lector que no estuvo en ninguna reunión. Lo que el agente sabe del proyecto sale de tres lugares: el código, un archivo de instrucciones que el repositorio le ofrece y lo que la persona le dice en la sesión. La guía de Anthropic para su agente recomienda que ese archivo guarde solo lo que el agente no puede deducir del código: cómo se comprueba el trabajo, dónde el código engaña, las decisiones que no están en el repositorio y lo que ya hubo que corregir dos veces.

La evidencia empuja en la misma dirección. Un estudio de ETH Zürich (arXiv 2602.11988, preprint de febrero de 2026, según su resumen) halla que los archivos de contexto "do not generally improve task success rates" y suben el costo de inferencia más de un 20 %, aunque sirven para especificar prácticas no estándar. El Radar de Thoughtworks pone el crecimiento descontrolado de esas instrucciones en Caution. El detalle está en [contexto del repositorio](contexto-del-repositorio.md).

La regla que tiene que cumplirse siempre no va en las instrucciones, porque el agente puede decidir que una indicación no aplica. Va a un mecanismo determinista: un [hook de Git](Git/hook-de-git.md) o del agente, una regla de permisos, un paso de [integración continua](../../DevOps/Integracion-y-entrega/integracion-continua.md).

## Darle al agente una forma de comprobar

La guía de Anthropic pone en el centro que el agente tenga una verificación que pueda correr solo: una prueba, un typecheck, un linter, un script que diga sí o no. Pide evidencia (el comando y su salida) en lugar de un "pasan las pruebas". Esta base lo usa para unir Construcción con Verificación: la tarea bien definida trae su prueba, el agente la corre mientras trabaja y quien revisa mira el resultado de la prueba antes que el código. Las señales de trabajo incompleto o inventado están en [verificar lo que hizo un agente](../Verificacion/verificar-lo-que-hizo-un-agente.md).

## Cuánto rinde, con la evidencia que hay

No hay una cifra confiable de cuánto acelera un agente. Hay ensayos controlados con ganancias y uno con pérdidas, y el autor de ese último (METR) advirtió en febrero de 2026 que su diseño ya no mide bien el efecto. DORA 2025 encuentra, en una encuesta de casi 5.000 profesionales, una relación positiva entre la adopción de IA y el volumen de entrega (throughput) y el desempeño del producto, y una negativa con la estabilidad de la entrega: "AI doesn't fix a team; it amplifies what's already there". La lectura de esta base es que el agente acelera la escritura y que la estabilidad depende de los controles alrededor (pruebas automáticas, lotes chicos, retroalimentación rápida). Los estudios, sus límites y la crítica a los benchmarks están en [agente de código](agente-de-codigo.md).

## Que todo proyecto arranque igual

Un proyecto nuevo sale de una [plantilla de proyecto](plantilla-de-proyecto.md) versionada y no de copiar otro servicio. Con agentes, la plantilla trae también lo que el agente lee desde el primer commit: el archivo de instrucciones, los comandos de verificación, los hooks y la integración continua. La plantilla es la pieza concreta de un [golden path](../../Platform-Engineering/Plataforma-interna/golden-path.md). La [configuración](Configuracion/configuracion.md) separa del código lo que cambia entre entornos o es secreto, y decide qué no puede leer un agente; [Git](Git/git.md) versiona todo y es donde el agente trabaja en su rama.

## Lo que hay adentro de Construcción

En orden de lectura:

- [Contexto del repositorio](contexto-del-repositorio.md): qué necesita saber un agente del repositorio, qué poner en el archivo de instrucciones y qué pasar a un mecanismo determinista; leerla antes de preparar un repositorio para agentes.
- [Agente de código](agente-de-codigo.md): cómo trabaja un agente, los modos de trabajar con él, dónde rinde y dónde falla, con la evidencia y sus límites.
- [Herramientas de agentes de código](herramientas-de-agentes-de-codigo.md): la ficha fechada con los nombres de archivos, hooks y comandos de las herramientas a 2026-11.
- [Plantilla de proyecto](plantilla-de-proyecto.md): por qué un proyecto nuevo sale de una plantilla versionada y qué trae; desde ahí, su implementación con [arquetipos de Maven](arquetipo-de-maven.md) y cómo [derivar nombres en un arquetipo](derivar-nombres-en-un-arquetipo-de-maven.md).
- [Configuración](Configuracion/configuracion.md): separar del código lo que cambia entre entornos o es secreto: YAML, Spring Boot y el entorno local con Compose.
- [Git](Git/git.md): el control de versiones: modelo de objetos, integrar, deshacer, hooks y repositorios grandes.

Pendientes, sin nota todavía:

- Entorno reproducible: el entorno de desarrollo como contenedor declarado en el repositorio (la especificación abierta de [dev containers](https://containers.dev/)), que, por inferencia de esta base (no hay fuente primaria), también serviría de sandbox para correr un agente sin permisos amplios. Hoy solo existe [levantar un entorno local con Docker Compose](Configuracion/levantar-un-entorno-local-con-docker-compose.md), que cubre el entorno de ejecución.
- Dependencias: agregar y actualizar dependencias cuando un agente las suma con facilidad: los paquetes que los modelos inventan (estudiados por Spracklen et al., USENIX Security 2025, con 16 modelos y 576.000 muestras de código) y la espera mínima antes de adoptar una versión recién publicada. Las actualizaciones masivas van a [migraciones y actualizaciones](../Evolucion/migraciones-y-actualizaciones.md) y la integridad de los artefactos a [cadena de suministro de software](../../DevOps/DevSecOps/cadena-de-suministro-de-software.md).
- Worktrees para sesiones paralelas: varios agentes trabajando a la vez, cada uno en su propio directorio de trabajo sobre el mismo repositorio; iría en [Git](Git/git.md), que hoy los menciona solo en [Git en repositorios grandes](Git/git-en-repositorios-grandes.md).
