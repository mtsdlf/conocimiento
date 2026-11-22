---
resumen: >-
  Lanzar es poner una funcionalidad o un producto en manos de la gente. La parte de producto decide qué sale, para quién y cómo se despliega y se mide, a menudo con feature toggles y de a un grupo por vez; el mensaje y los canales son de product marketing.
estado: vigente
estabilidad: semi
fuentes:
  - "Pete Hodgson, Feature Toggles (aka Feature Flags) (martinfowler.com, 2017-10-09): https://martinfowler.com/articles/feature-toggles.html"
  - "Pragmatic Institute Framework, categoría Go-to-Market: https://www.pragmaticinstitute.com/framework/"
  - "Producto/.investigacion/planificacion-y-entrega.md"
aliases: [launch, product launch, release, feature flags, feature toggles, lanzamiento gradual]
creado: 2026-11-22
revisado: 2026-11-22
---

# Lanzamiento

Lanzar es poner una funcionalidad o un producto en manos de la gente. La parte de producto decide qué sale, para quién y cómo se despliega y se mide, a menudo con feature toggles y de a un grupo por vez; el mensaje y los canales son de product marketing.

Es el último paso de [Planificación y entrega](planificacion-y-entrega.md) y el primero de [Medición](../Medicion/medicion-de-producto.md): lo que se lanza es lo que después se mide. La palabra mezcla dos trabajos distintos. Uno es de producto e ingeniería: separar el despliegue del código del momento en que la gente lo ve. El otro es *go-to-market*: contarle al mercado que existe.

## Separar desplegar de lanzar con feature toggles

Con un *feature toggle* (o *feature flag*), el código nuevo llega a producción con un interruptor, y el interruptor decide quién lo ve: desplegar deja de ser lanzar. La mecánica (cómo se despliega con flags y cómo se vuelve atrás) es de DevOps y está en [estrategias de despliegue](../../DevOps/Despliegue/estrategias-de-despliegue.md); acá importa qué decide producto con ellos.

Hodgson distingue cuatro tipos por su propósito: *release*, *experiment*, *ops* y *permissioning*. Los de release sirven para "allow incomplete and un-tested codepaths to be shipped to production as latent code": el equipo integra trabajo a medio hacer sin que nadie lo vea. Los de experiment muestran variantes a grupos distintos y son la base técnica del [experimento A/B](../Medicion/experimento-ab.md). Los de permissioning, por su nombre, tocan una decisión de [pricing y empaquetado](../Monetizacion/pricing-y-empaquetado.md): qué usuarios ven qué funcionalidad (inferencia, no del artículo).

Los toggles tienen un costo de mantenimiento, y el artículo lo trata: algunos son de vida corta y deberían borrarse cuando cumplieron su función. Qué tipos son de vida corta y cuáles duran se lee en el original; el informe de esta base no lo detalla.

## Lanzamiento gradual: canary y grupos elegidos

Con un toggle, un lanzamiento se abre de a poco. El *canary release* enciende la funcionalidad para un porcentaje chico de usuarios y la amplía si las métricas acompañan; cómo funciona está en [estrategias de despliegue](../../DevOps/Despliegue/estrategias-de-despliegue.md). Hodgson lo distingue del "Champagne Brunch", que no toma un porcentaje: apunta a un grupo específico de usuarios.

La pregunta de producto en un lanzamiento gradual es qué métrica decide si se amplía. Esa métrica sale de [Medición](../Medicion/medicion-de-producto.md), y si el lanzamiento es para gente nueva, el momento en que ve el valor es la [activación](../Medicion/activacion.md).

> [!NOTE]
> Sin fuente todavía: fuentes de producto (no de ingeniería) sobre lanzamiento gradual guiado por métricas. Lo único leído sobre toggles y canary es el artículo de Hodgson.

## Dónde termina producto y empieza product marketing

Producto decide qué sale, a quién y cómo se despliega y se mide. Marketing decide el mensaje, los canales y el posicionamiento. Ese reparto es una síntesis del informe de investigación de esta base; ninguna fuente leída lo fija.

El Pragmatic Institute ubica el lanzamiento en la categoría "Go-to-Market", junto con el plan de marketing, el crecimiento, la retención y la concientización, y separado de "Focus", donde vive el roadmap. Lo define así: "A launch introduces a product or release to the market", y pide que "teams, systems, content, support, and measures" estén listos. El marco no asigna roles: no dice qué hace el product manager y qué hace product marketing. Ninguna nota lo resuelve todavía (ver el hueco en [roles de producto](../Organizacion/roles-de-producto.md#product-marketing)).

El posicionamiento de lo que se lanza no se inventa en el lanzamiento. Sale del trabajo de [posicionamiento](../../Marketing/Propuesta/posicionamiento.md) del tema Marketing, que sigue *Obviously Awesome* de April Dunford: contra qué alternativas se compara el producto, qué atributos tiene que ellas no, qué valor dan, para qué clientes y en qué categoría. Como inferencia, sin fuente: una funcionalidad nueva puede cambiar los atributos únicos, y entonces el lanzamiento obliga a revisar el posicionamiento. Si el producto crece por su propio uso, el canal de adquisición se trata en [growth y product-led growth](../../Marketing/Canales/growth-y-product-led-growth.md).

> [!NOTE]
> Sin fuente todavía: una fuente primaria sobre el límite entre product manager y product marketing manager. La página de SVPG sobre product marketing no tenía contenido útil para esto y el Pragmatic Institute no asigna roles. Candidato sin verificar: el libro de Martina Lauchengco.

## Cómo falla un lanzamiento

Las fuentes leídas registran una falla: el costo de los toggles que se quedan en el código después de cumplir su función. Las otras dos que aparecen en la práctica son inferencia, sin fuente: lanzar a todos de una vez sin un interruptor para volver atrás, y lanzar sin haber decidido qué métrica dice si funcionó, con lo que la [medición](../Medicion/medicion-de-producto.md) llega tarde.

## Qué leer

"Feature Toggles" de Hodgson en martinfowler.com es la referencia de la parte de producto e ingeniería. Interesan las secciones de categorías de toggles y de canary, y el costo de mantenerlos: qué toggles son de vida corta.
