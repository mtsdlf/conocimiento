---
tipo: concepto
resumen: >-
  La gobernanza de plataforma es fijar dentro de la plataforma, de forma central y auditable, los
  límites del self-service, los controles de seguridad y cumplimiento, y la trazabilidad de cada
  cambio.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "CNCF TAG App Delivery, Platforms White Paper: https://tag-app-delivery.cncf.io/whitepapers/platforms/"
aliases: [Gobernanza incorporada, Platform governance]
parte_de: []
requiere: [self-service, plataforma-api-first]
relacionado: []
---

# Gobernanza de plataforma

La gobernanza de plataforma es fijar dentro de la plataforma, de forma central y auditable, los
límites del self-service, los controles de seguridad y cumplimiento, y la trazabilidad de cada
cambio.

## Por qué importa

El [[self-service]] le da autonomía a los equipos, y sin límites esa autonomía termina en recursos
huérfanos, costos sin dueño y auditorías imposibles. La gobernanza incorporada resuelve la
tensión: los equipos no piden permiso, porque las reglas ya están en la plataforma.

## Cómo funciona

Según la CNCF, una plataforma es segura por defecto y ofrece capacidades para asegurar el
cumplimiento y la validación; la gobernanza y los controles se incorporan en las plantillas, los
patrones y las capacidades. Los motores de políticas, como OPA o Kyverno, restringen lo que se
puede hacer y avisan o corrigen los desvíos.

La gobernanza tiene cuatro partes:

- **límites**: quién puede pedir qué y cuánto (cuotas, tamaños, entornos permitidos);
- **controles**: aprobaciones solo donde el riesgo lo pide, como un despliegue a producción
  marcado de riesgo;
- **trazabilidad**: cada pedido, cambio y recurso deja un evento consultable, que alimenta
  auditoría, costos y reportes; con una [[plataforma-api-first]], ese registro sale de la API;
- **dueño registrado**: cada recurso y cada capacidad tiene un responsable, y no se agrega nada
  "por la puerta de atrás".

## Ejemplo

Un equipo pide una base de datos por la API. La plataforma verifica que el equipo no supere su
cuota de tres bases, aplica cifrado por defecto, etiqueta el recurso con su dueño y su centro de
costos, y registra el evento. Nadie aprobó nada a mano.

## No confundir con

Un comité de aprobación. Un comité revisa cada pedido y se vuelve una cola; la gobernanza de
plataforma escribe las reglas una vez y las aplica en cada pedido de forma automática.

## Relaciones

- Requiere: [[self-service]] — gobierna lo que los equipos hacen por su cuenta.
- Requiere: [[plataforma-api-first]] — la API es el punto donde se aplican y registran las reglas.
