---
tipo: concepto
resumen: >-
  Multi-tenancy es servir a varios clientes (tenants) desde una misma instancia, con los datos de
  cada uno aislados de los demás.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "AWS, SaaS Lens, Silo, pool, and bridge models: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/silo-pool-and-bridge-models.html"
  - "Microsoft, Multi-tenant SaaS database tenancy patterns: https://learn.microsoft.com/en-us/azure/azure-sql/database/saas-tenancy-app-design-patterns"
  - "RFC 9110, HTTP Semantics, 15.5.4 403 Forbidden: https://www.rfc-editor.org/rfc/rfc9110.html#section-15.5.4"
  - "Archivo/Arquitectura/mvp-ecommerce-arquitectura.md (original, texto generado con IA)"
  - "Archivo/Desarrollo/epicas-historias-usuario-ecommerce.md (original)"
aliases: [Multitenancy, Multi-tenant, Multiinquilino, Tenant]
parte_de: []
requiere: []
relacionado: [api-led-connectivity]
---

# Multi-tenancy

Multi-tenancy es servir a varios clientes (tenants) desde una misma instancia, con los datos de
cada uno aislados de los demás.

## Por qué importa

Una plataforma que da una tienda online a cada comercio no puede levantar una instalación por
cliente sin que el costo y la operación crezcan con cada alta. Compartir la instancia baja ese
costo, pero cualquier consulta que olvide filtrar por tenant expone datos de otro cliente. La
decisión central es cuánto se comparte.

## Cómo funciona

AWS agrupa los modelos de aislamiento en tres: pool, bridge y silo. Microsoft describe los
extremos (base multi-tenant con columna de tenant, y base por tenant) y los híbridos.

| Modelo | Aislamiento | Costo por tenant | Riesgo |
|---|---|---|---|
| **Pool**: tablas compartidas con columna `tenant_id` | lógico: cada consulta filtra | el más bajo | una consulta sin filtro mezcla tenants |
| **Bridge**: por ejemplo, un esquema por tenant en una base compartida | por esquema | medio | migraciones repetidas por esquema |
| **Silo**: una base por tenant | físico | el más alto | operar cientos de bases |

El tenant se resuelve una vez por request, en el borde: por subdominio (`tienda1.ejemplo.com`),
por un header (`X-Tenant-Id`) o por un claim del token. Un header o subdominio se valida contra
el token, para que nadie pida otro tenant cambiando un valor. Después viaja por todas las capas. En una
arquitectura [API-led connectivity](api-led-connectivity.md), la capa Experience lo resuelve y lo pasa a Process y System.

Los identificadores únicos se definen por tenant: dos comercios pueden tener cada uno un producto
con el SKU `SKU-001`. Lo mismo vale para las claves de idempotencia y las cuotas.

Si un tenant pide un recurso de otro, la API responde 404 y no 403. Un 403 confirma que el
recurso existe; RFC 9110 (sección 15.5.4) permite responder 404 justamente para no revelarlo.

## Ejemplo

Un catálogo multi-tenant usa una sola base PostgreSQL con `tenant_id` en cada tabla. Un filtro
global del ORM agrega `WHERE tenant_id = ?` a toda consulta, con el valor del header
`X-Tenant-Id`. Un caso de prueba consulta como tenant B un producto creado por el tenant A y espera
404.

## No confundir con

Una aplicación con varios usuarios. Los usuarios de un mismo tenant comparten datos (el catálogo
de su comercio); los tenants no comparten nada entre sí.

## Relaciones

- Relacionado: [API-led connectivity](api-led-connectivity.md) — define en qué capa se resuelve el tenant.
- Ver también: [Clave de idempotencia](clave-de-idempotencia.md) — las claves también se aíslan por tenant.
- La usa: [Diseñar casos de prueba de una API](../Desarrollo/disenar-casos-de-prueba-de-api.md) (Desarrollo) — el aislamiento entre tenants es una categoría de casos.
