---
resumen: >-
  La tabla de eventos registra lo que hace cada usuario como una fila por acción (qué hizo, quién,
  cuándo y con qué detalles), y el plan de tracking es el documento que decide qué acciones se
  registran y por qué.
estado: borrador
estabilidad: estable
fuentes:
  - "Google, Analytics Help, Events: https://support.google.com/analytics/answer/9322688"
  - "Google, Analytics Help, límites de recolección y configuración: https://support.google.com/analytics/answer/9267744"
  - "Amplitude, Plan your implementation: https://amplitude.com/docs/get-started/plan-your-implementation"
  - "Segment, Spec: Track (no leída, 403): https://segment.com/docs/connections/spec/track/"
  - "Datos/.investigacion/modelado-e-ingesta.md (sección 5)"
aliases: [eventos, event tracking, plan de tracking, tracking plan, instrumentación, tabla de eventos]
creado: 2026-11-27
revisado:
---

# Tabla de eventos

La tabla de eventos registra lo que hace cada usuario como una fila por acción (qué hizo, quién,
cuándo y con qué detalles), y el plan de tracking es el documento que decide qué acciones se
registran y por qué.

Es la fuente de la [analítica de producto](../Analitica-de-producto/analitica-de-producto.md): de
ella salen el [embudo](../Analitica-de-producto/embudo.md), las
[cohortes](../Analitica-de-producto/Cohortes/cohorte.md) y la
[retención](../Analitica-de-producto/Retencion-y-churn/retencion.md). Vive en
[modelado y almacenamiento](modelado-y-almacenamiento.md) porque lo que se decide acá es la forma
de la tabla.

## Qué es un evento y qué columnas tiene

La documentación de una herramienta de analítica web lo define así: «An event allows you to measure
a specific interaction or occurrence on your website or app». Ver un producto, agregarlo al carrito,
pagar o cancelar una suscripción son eventos.

Una tabla de eventos tiene, como mínimo, estas columnas:

| Columna | Qué guarda | Ejemplo |
|---|---|---|
| evento | el nombre de la acción | `producto_agregado` |
| usuario | un identificador estable de quién la hizo | `u_10482`, o un id anónimo si no inició sesión |
| momento | fecha y hora | `2026-11-27 18:42:10` |
| propiedades | el contexto de esa acción | producto, precio, medio de pago |

Es una tabla de hechos con el grano más fino posible: una fila por acción (lectura de la base). Por
eso se lee con las ideas del [modelado dimensional](modelado-dimensional.md): el usuario y el
producto son dimensiones, y el evento es el hecho.

> [!NOTE]
> Sin fuente todavía: el esquema estándar de un evento según la spec de Track de Segment (nombre,
> propiedades, identificador de usuario o anónimo), la referencia que más se cita; la página no se
> pudo leer. Las columnas de arriba son las de uso general.

## El plan de tracking sale de la pregunta

Registrar todo «por las dudas» llena la tabla de eventos que nadie usa y olvida los que hacían
falta. Una documentación de producto lo ordena con un documento previo: «it's critical to create a
tracking plan document that outlines what events and properties to track, why you're tracking them,
and where they're tracked». Y agrega: «A tracking plan should derive from the business outcomes
you're trying to measure or improve».

En la práctica, el plan es una tabla con una fila por evento: nombre, cuándo se dispara, qué
propiedades lleva, para qué métrica sirve y quién lo implementó (lectura de la base; Amplitude no define sus columnas). Arranca de la métrica, no de la
pantalla. Si la métrica es la [activación](../../Producto/Medicion/activacion.md), el plan necesita
el evento que marca la llegada al valor; si es un [experimento
A/B](../../Producto/Medicion/experimento-ab.md), la variante que vio cada usuario como propiedad.

## Cómo se rompe una tabla de eventos

Se rompe en silencio, y el tablero sigue mostrando números (lectura de la base):

- El mismo evento con dos nombres. `compra` en la web y `purchase_completed` en la app parten
  las ventas en dos. Una convención de nombres, por ejemplo objeto más verbo en pasado, lo evita.
- Usuario sin identificador estable. Si el id cambia entre visitas, cada visita parece un
  usuario nuevo y la retención se desploma.
- Eventos que cambian de significado. Un rediseño mueve el botón y el evento se dispara en otro
  momento; la serie se corta sin que nadie lo anote.
- Límites de la herramienta. Google Analytics 4 limita el largo del nombre del evento, la
  cantidad de propiedades por evento y cuánto tarde puede llegar un evento (ignora los que llegan
  con más de dos días); los valores, leídos el 2026-11-27, están en sus [límites de recolección](https://support.google.com/analytics/answer/9267744).

Detectar y prevenir estos problemas es parte de la [calidad de
datos](../Gobierno-y-calidad/calidad-de-datos.md). Si los eventos guardan datos de personas, qué se
puede guardar está en [privacidad de datos
personales](../Gobierno-y-calidad/privacidad-de-datos-personales.md).

## Dónde se lee la versión larga

Para el plan de tracking, la página de plan de implementación de Amplitude, corta y práctica. Para
la forma estándar de un evento, la spec de Track de Segment. En las dos conviene fijarse, como sugiere el informe y sin que
se haya confirmado en esas fuentes, en el nombre del evento como acción terminada, las propiedades
como contexto y un identificador de usuario que no cambie.
