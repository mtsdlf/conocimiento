---
resumen: >-
  Migrar y actualizar es mantener el software al día con sus dependencias, versiones y plataformas,
  desde subir una librería hasta cambiar el mismo patrón en miles de archivos. Con modelos de lenguaje,
  las migraciones grandes siguen un patrón: el modelo propone, una verificación determinista decide y
  las personas revisan.
estado: borrador
estabilidad: semi
fuentes:
  - https://research.google/blog/accelerating-code-migrations-with-ai/
  - https://arxiv.org/abs/2501.06972
  - https://www.infoq.com/news/2025/03/airbnb-llm-test-migration/
  - https://airbnb.tech/?p=366
  - https://aws.amazon.com/blogs/devops/amazon-q-developer-just-reached-a-260-million-dollar-milestone
  - https://docs.renovatebot.com/bot-comparison/
  - https://code.claude.com/docs/en/best-practices
aliases: [migración de código, actualización de dependencias, dependency updates, code migration, migraciones masivas, large-scale changes]
creado: 2026-11-27
revisado:
---

# Migraciones y actualizaciones

Migrar y actualizar es mantener el software al día con sus dependencias, versiones y plataformas, desde subir una librería hasta cambiar el mismo patrón en miles de archivos. Con modelos de lenguaje, las migraciones grandes siguen un patrón: el modelo propone, una verificación determinista decide y las personas revisan.

## Dos tamaños de cambio

Una actualización chica sube una dependencia o una versión y casi no toca código propio. Pasa seguido: un bot abre la propuesta, la integración continua la prueba y alguien la acepta. Los cambios de versión se leen con el [versionado semántico](../../DevOps/Ramas-y-versiones/versionado-semantico.md): un cambio mayor avisa que puede romper.

Una migración grande cambia código propio en muchos lugares por la misma razón: una librería que cambió su interfaz, un tipo que hay que agrandar, un marco de pruebas que se reemplaza. Los casos de abajo la muestran como tarea de semanas cuando hay una suite que decida; en el de Airbnb, seis semanas frente a una estimación manual de un año y medio. Si lo que se reemplaza es un sistema entero y no un patrón de código, el camino es [strangler fig](../../Arquitectura/Estilos/strangler-fig.md).

Las dos fallan por posponer. Cada actualización que se salta hace más grande la siguiente, hasta que una actualización chica se vuelve una migración (criterio de esta base).

## El patrón de las migraciones asistidas por modelos

Hay tres casos grandes publicados, y los tres son autoinformes de las empresas que los hicieron, sin replicación independiente.

| Caso | Qué se migró | Qué reportan | Fuente |
|---|---|---|---|
| Google | decenas de tipos de ID numéricos de 32 a 64 bits en un producto publicitario | 80 % de los cambios de código aprobados generados por el modelo; 50 % menos de tiempo total, según estiman los propios ingenieros | blog de Google Research, leído |
| Airbnb | unos 3.500 archivos de pruebas de componentes de un marco de pruebas a otro | unas seis semanas frente a una estimación manual de un año y medio; 97 % automatizado | resúmenes, no el original |
| Amazon | actualización de aplicaciones a una versión nueva de Java | "We estimate this has saved us the equivalent of 4,500 developer-years of work"; de unos 50 días-desarrollador a pocas horas por aplicación | blog del vendedor, por resúmenes |

Las cifras no se comparan entre sí ni se trasladan a un proyecto de cliente: son estimaciones internas de las propias empresas, y una de ellas (Amazon) es del proveedor de la herramienta.

Lo que se aprende es el patrón común. En Google, cada cambio propuesto se valida compilando y corriendo pruebas de unidad, hay un paso de reparación por aprendizaje automático y las personas revisan, con los cambios repartidos entre los equipos dueños de cada parte. En Airbnb, según los resúmenes, cada archivo pasa por etapas: reescribir, hacer pasar las pruebas, limpiar lint y tipos, marcar terminado. En los dos, el modelo nunca decide solo si un cambio entra.

1. El modelo propone el cambio, archivo por archivo.
2. Una verificación determinista (compilar, probar, lint) decide si entra.
3. Lo que no pasa vuelve al modelo con el error, o pasa a una persona.
4. Las personas revisan lo que pasó, repartido entre quienes conocen cada parte.

Es el mismo patrón que [el LLM emite, el reasoner verifica](../../IA/llm-emite-reasoner-verifica.md) en IA, aplicado a código. En un proyecto de cliente sin pruebas, la ventaja no se traslada tal cual, porque falta el paso 2; esa es inferencia de esta base. Ahí, antes de migrar, se fija el comportamiento como en [sistema heredado](sistema-heredado.md).

## Herramientas, a 2026-11

Esta sección envejece rápido; las herramientas cambian y el patrón de arriba queda.

- Bots de dependencias. Renovate y Dependabot abren pull requests de actualización y los dos soportan actualizaciones agrupadas. Según la comparación que publica Renovate (fuente de uno de los dos bots), Dependabot viene integrado en GitHub y Renovate se instala como app o se aloja por cuenta propia; Renovate trae un tablero de dependencias activado por defecto. Siguen siendo la primera línea para lo chico; el agente entra cuando una actualización obliga a cambiar código (criterio de esta base).
- Agentes de código. La guía de buenas prácticas de Anthropic (leída el 2026-11-27) describe un comando que divide un cambio mecánico grande en 5 a 30 unidades, cada una en su propio worktree y con su propio pull request; su nombre está en la ficha [herramientas de agentes de código](../Construccion/herramientas-de-agentes-de-codigo.md).

> [!NOTE]
> Sin fuente todavía: la documentación oficial de Dependabot no se leyó, y las herramientas de codemods (transformaciones de código por reglas, sin modelo) no tienen fuente leída. Una actualización de dependencias también es un punto de entrada a la [cadena de suministro](../../DevOps/DevSecOps/cadena-de-suministro-de-software.md), y eso tampoco se investigó para esta nota.

Para leer: el paper de Google (Nikolov et al., ICSE SEIP 2025), el apartado del flujo (descubrimiento de archivos, validación en varias etapas, revisión humana) y sus criterios de éxito. Cómo corre la verificación en cada cambio está en [integración continua](../../DevOps/Integracion-y-entrega/integracion-continua.md).
