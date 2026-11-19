---
resumen: >-
  Las estrategias de despliegue (recreate, rolling, blue/green, canary y feature flags) son las formas de
  reemplazar una versión en producción por otra controlando el riesgo y la velocidad del
  rollback.
estado: borrador
estabilidad: estable
fuentes:
  - "Martin Fowler, BlueGreenDeployment: https://martinfowler.com/bliki/BlueGreenDeployment.html"
  - "Danilo Sato, CanaryRelease, martinfowler.com: https://martinfowler.com/bliki/CanaryRelease.html"
  - "Pete Hodgson, Feature Toggles, martinfowler.com: https://martinfowler.com/articles/feature-toggles.html"
  - "Kubernetes Docs, Deployments: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/"
  - "Archivo/DevOps/devops-referencia.md (original, texto generado con IA)"
aliases: [Deployment strategies, Estrategia de despliegue, Blue/green, Canary, Rolling update]
creado: 2026-10-03
revisado:
---

# Estrategias de despliegue

Las estrategias de despliegue (recreate, rolling, blue/green, canary y feature flags) son las formas de
reemplazar una versión en producción por otra controlando el riesgo y la velocidad del
rollback.

## Por qué no reemplazar todo de golpe

Reemplazar todo de golpe deja al servicio caído durante el cambio y expone a todos los usuarios
a un posible error. Cada estrategia cambia cuánta gente ve la versión nueva, cuánto tiempo y cómo
se vuelve atrás. Es lo que permite el [Despliegue continuo](../Integracion-y-entrega/despliegue-continuo.md) sin aprobación manual.

## Recreate, rolling, blue/green, canary y feature flags

| Estrategia | Cómo | Rollback | Cuándo elegirla |
|---|---|---|---|
| **Recreate** | Se apaga la versión vieja y se levanta la nueva. | Redesplegar; hay corte. | Si se tolera un corte o las dos versiones no pueden convivir. |
| **Rolling** | Se reemplazan instancias de a poco. | Otro rolling hacia atrás. | Por defecto: es la de un Deployment de Kubernetes. |
| **Blue/green** | Dos producciones iguales; se prueba la inactiva y se cambia el router (el balanceador que reparte el tráfico). | Volver el router al entorno anterior. | Si el rollback tiene que ser instantáneo y se puede pagar el doble de infraestructura. |
| **Canary** | La versión nueva recibe primero una parte chica del tráfico; se amplía si las métricas acompañan. | Sacarle el tráfico. | Si hay métricas por versión y el riesgo de un cambio es alto. |
| **Feature flag** | El código se despliega apagado y se enciende en runtime. | Apagar el flag. | Para funcionalidades a medio hacer o que se liberan a un grupo. |

En Kubernetes, el ritmo del rolling lo fijan `maxSurge` (cuántas instancias nuevas se crean de
más) y `maxUnavailable` (cuántas pueden faltar a la vez).

Las cuatro primeras deciden cómo llega el código; los feature flags deciden cuándo lo ve el
usuario, y se combinan con cualquiera. Todas suponen **artefactos inmutables**: cada versión es
un paquete que no se modifica después de construido, así que la vieja sigue existiendo y se
puede volver a ella. Las migraciones de base de datos tienen que servir a las dos versiones
mientras conviven.

## Un canary del 5 % al 100 %

Una API pasa el 5 % del tráfico a la versión nueva. Durante 15 minutos se compara su tasa de
errores con la de la versión vieja; como es igual, sube al 25 %, al 50 % y al 100 %. Si hubiera
subido, el tráfico vuelve entero a la versión vieja en segundos.

## Desplegar dentro de un entorno no es promover

La promoción entre entornos. Las estrategias de despliegue cambian la versión dentro de un
entorno; la [Promoción entre entornos](promocion-entre-entornos.md) decide cuándo una versión pasa de staging a producción.

## Ver también

- [Entrega continua](../Integracion-y-entrega/entrega-continua.md) — el paso a producción usa una de estas estrategias.
