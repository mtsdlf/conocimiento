---
resumen: >-
  API-led connectivity organiza las APIs en tres capas: System (expone un sistema o dominio),
  Process (orquesta varias System) y Experience (adapta los datos a un frontend).
estado: vigente
estabilidad: estable
fuentes:
  - "MuleSoft Documentation, API-led connectivity overview: https://docs.mulesoft.com/general/api-led-overview"
  - "Archivo/Arquitectura/mvp-ecommerce-arquitectura.md (original, texto generado con IA)"
  - "Archivo/Arquitectura/circuit-breaking-resilience4j.md (original)"
aliases: [API-led, Arquitectura API-led, System Process Experience APIs]
creado: 2026-10-03
revisado: 2026-11-27
---

# API-led connectivity

API-led connectivity organiza las APIs en tres capas: System (expone un sistema o dominio),
Process (orquesta varias System) y Experience (adapta los datos a un frontend).

## Por qué separar la orquestación del frontend

Sin capas, cada frontend llama directo a cada servicio y repite la misma orquestación: la tienda
y el backoffice arman cada uno su propia vista de un producto. Con capas, la orquestación vive en
un solo lugar y cada frontend recibe exactamente los datos que muestra. El término y las tres
capas los propuso MuleSoft.

## Las tres capas y quién llama a quién

| Capa | Qué hace | Quién la llama |
|---|---|---|
| **System** | expone un sistema de registro o un dominio (catálogo, precios, inventario), sin lógica de otros dominios | las Process |
| **Process** | combina varias System para un proceso de negocio (armar el carrito, el checkout) | las Experience |
| **Experience** | adapta la respuesta a un consumidor concreto: forma, paginado, campos visibles | un frontend o un socio |

Cada capa solo llama a la de abajo. Una System no conoce a sus consumidores; por eso se reutiliza
desde varios procesos. Una Experience no tiene reglas de negocio: si dos frontends necesitan la
misma regla, la regla baja a una Process.

En un diseño por bounded contexts, cada contexto (Identidad, Catálogo, Pedido) suele tener su
System API. Las fallas se contienen en la capa Process, que es la que llama a varias
dependencias: ahí van el [Circuit breaker](circuit-breaker.md) y la [Degradación controlada](degradacion-controlada.md).

## La vista de producto de una tienda online

En una tienda online, `GET /exp/store/products/{slug}` (Experience) llama a un ProductViewProcess,
que junta el producto (System Catálogo), su precio vigente (System Precios) y su stock (System
Inventario). El backoffice usa otra Experience sobre las mismas System.

## Lo que no hace un API gateway

El gateway enruta, autentica y limita tráfico, pero no orquesta datos de varios
servicios; puede estar delante de cualquiera de las tres capas. Qué hace y qué no hace está en [API gateway y BFF](api-gateway-y-bff.md).

## Ver también

- [Multi-tenancy](multi-tenancy.md): el tenant se resuelve en la capa Experience y viaja a las de abajo.
- [Plataforma API-first](../../Platform-Engineering/Plataforma-interna/plataforma-api-first.md), en Platform-Engineering: API-first dice cómo se expone una capacidad; API-led, en qué capa va.
