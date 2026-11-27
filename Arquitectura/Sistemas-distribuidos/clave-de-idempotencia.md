---
resumen: >-
  Una clave de idempotencia es un identificador que el cliente manda con una operación para que,
  si la reintenta, el servidor devuelva el mismo resultado sin repetir el efecto.
estado: vigente
estabilidad: estable
fuentes:
  - "IETF HTTPAPI, The Idempotency-Key HTTP Header Field, draft 07 (2025, vencido): https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/"
  - "Stripe, Idempotent requests: https://docs.stripe.com/api/idempotent_requests"
  - "RFC 9110, HTTP Semantics, 9.2.2 Idempotent Methods: https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2"
  - "Archivo/Arquitectura/mvp-ecommerce-arquitectura.md (original, texto generado con IA)"
  - "Archivo/Desarrollo/epicas-historias-usuario-ecommerce.md (original)"
aliases: [Idempotency-Key, Idempotency key, Clave idempotente]
creado: 2026-10-03
revisado: 2026-11-27
---

# Clave de idempotencia

Una clave de idempotencia es un identificador que el cliente manda con una operación para que,
si la reintenta, el servidor devuelva el mismo resultado sin repetir el efecto.

## Por qué un POST no se reintenta sin protección

Si un cliente manda `POST /payments` y la conexión se corta antes de la respuesta, no sabe si el
cobro se hizo. Reintentar sin protección puede cobrar dos veces; no reintentar puede perder la
venta. HTTP define `GET`, `PUT` y `DELETE` como idempotentes (RFC 9110), pero `POST` y `PATCH` no
lo son. La clave hace seguro el reintento de esas operaciones.

## Cómo guarda y compara la clave el servidor

1. El cliente genera un valor único por operación (un UUID v4) y lo manda en el header
   `Idempotency-Key`. Si reintenta, manda el mismo valor.
2. El servidor guarda la clave junto con un resumen del request y la respuesta.
3. Si llega la misma clave con el mismo request, devuelve la respuesta guardada sin volver a
   ejecutar.
4. Si llega la misma clave con un request distinto, lo rechaza: es un error del cliente.
5. Si llega mientras el primero todavía se procesa, lo rechaza o lo hace esperar.

La clave se guarda por un tiempo acotado: Stripe acepta claves de hasta 255 caracteres y puede
borrarlas cuando tienen al menos 24 horas. El header se propuso al IETF como Internet-Draft; la
versión 07, de 2025, venció sin llegar a RFC, así que es una convención y no un estándar. El
borrador sugiere 400 si falta una clave obligatoria, 422 si se reutiliza con otro payload y 409 si
el primer request sigue en curso.

Si el efecto vive en la misma base, la clave se guarda en la misma transacción. Si se guarda
después, una caída en el medio deja el efecto hecho y la clave sin registrar.

## Dos POST con la misma clave

Una API de catálogo recibe dos veces `POST /products` con `Idempotency-Key: abc123` y el SKU
`SKU-002`. La primera vez responde 201 Created con el `id` del producto; la segunda devuelve la
misma respuesta, 201 con el mismo `id`, y la base tiene un solo producto. En un sistema
[Multi-tenancy](multi-tenancy.md), la clave se guarda junto con el tenant, para que dos clientes no choquen.

## Por qué no alcanza una restricción de unicidad

Un índice único sobre el SKU evita duplicados, pero el segundo
intento recibe un error 409 en lugar de la respuesta original, y el cliente no sabe si su primer
intento funcionó.

## Ver también

- [Saga](saga.md): los pasos y compensaciones de una saga se reintentan y necesitan ser idempotentes.
- [Outbox](outbox.md): publica cada evento al menos una vez, así que el consumidor deduplica con la misma idea.
- [Diseñar casos de prueba de una API](../../Desarrollo/Verificacion/disenar-casos-de-prueba-de-api.md), en Desarrollo: cada operación que acepta la clave lleva un caso de reintento.
