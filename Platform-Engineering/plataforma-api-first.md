---
tipo: concepto
resumen: >-
  Una plataforma API-first ofrece cada capacidad a través de una API versionada y auditable; el
  portal, la CLI y los bots son presentaciones de esa API, sin lógica propia.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "CNCF TAG App Delivery, Platforms White Paper: https://tag-app-delivery.cncf.io/whitepapers/platforms/"
aliases: [API-first (plataforma), Interface-driven]
parte_de: []
requiere: [capacidad-de-plataforma]
relacionado: [developer-portal, crossplane]
---

# Plataforma API-first

Una plataforma API-first ofrece cada capacidad a través de una API versionada y auditable; el
portal, la CLI y los bots son presentaciones de esa API, sin lógica propia.

## Por qué importa

Si el portal, la CLI y un script interno implementan cada uno su propia forma de crear una base
de datos, hay tres comportamientos que mantener y tres lugares donde auditar. Con una sola API,
las reglas, el registro y el versionado viven en un solo lugar, y cualquier interfaz nueva se
suma sin duplicar lógica.

## Cómo funciona

El white paper de la CNCF pide que la plataforma ofrezca sus capacidades por interfaces
consistentes (GUI, CLI y API) para llegar a los usuarios donde estén. El principio API-first va
más allá de la CNCF, como decisión de diseño, y agrega un orden:

1. Cada [Capacidad de plataforma](capacidad-de-plataforma.md) se diseña primero como API, con su contrato (por ejemplo, una
   especificación OpenAPI) y su dueño.
2. Toda interacción pasa por esa API: nada de scripts internos, accesos directos a la base de la
   plataforma ni tickets.
3. Portal, CLI y bots consumen la API. Si una regla vive en el portal y no en la API, quien usa
   la CLI o llama a la API directamente no la cumple.
4. Todo cambio relevante que pasa por la API emite un evento y queda registrado, lo que sostiene
   la [Gobernanza de plataforma](gobernanza-de-plataforma.md).

El costo es un esfuerzo inicial mayor: hay que diseñar contratos antes de mostrar una pantalla.
Un portal que resuelve todo desde su interfaz sale más rápido; como inferencia, escala peor,
porque las reglas quedan atadas a una sola presentación.

Las APIs declarativas, como los recursos de Kubernetes que ofrece [Crossplane](crossplane.md), cuentan como
API si pasan por los mismos controles y la misma auditoría que el resto.

## Ejemplo

Crear una cola de mensajes se hace con una llamada a la API de recursos. El portal muestra un
formulario que llama a esa API, la CLI ejecuta la misma llamada y un bot de chat también; los tres
quedan auditados igual.

## No confundir con

Una empresa API-first hacia afuera, que diseña productos para clientes externos a partir de
APIs. Acá el principio es interno.

## Relaciones

- Requiere: [Capacidad de plataforma](capacidad-de-plataforma.md) — lo que se expone por cada API.
- Relacionado: [Developer portal](developer-portal.md) — el portal es una presentación de estas APIs.
- Relacionado: [Crossplane](crossplane.md) — ofrece APIs declarativas para recursos de infraestructura.
