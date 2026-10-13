---
tipo: concepto
resumen: >-
  API-led connectivity organiza las APIs en tres capas: System (expone un sistema o dominio),
  Process (orquesta varias System) y Experience (adapta los datos a un frontend).
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "MuleSoft Documentation, API-led connectivity overview: https://docs.mulesoft.com/general/api-led-overview"
  - "Archivo/Arquitectura/mvp-ecommerce-arquitectura.md (original, texto generado con IA)"
  - "Archivo/Arquitectura/circuit-breaking-resilience4j.md (original)"
aliases: [API-led, Arquitectura API-led, System Process Experience APIs]
parte_de: []
requiere: []
relacionado: [multi-tenancy]
---

# API-led connectivity

API-led connectivity organiza las APIs en tres capas: System (expone un sistema o dominio),
Process (orquesta varias System) y Experience (adapta los datos a un frontend).

## Por qué importa

Sin capas, cada frontend llama directo a cada servicio y repite la misma orquestación: la tienda
y el backoffice arman cada uno su propia vista de un producto. Con capas, la orquestación vive en
un solo lugar y cada frontend recibe exactamente los datos que muestra. El término y las tres
capas los propuso MuleSoft.

## Cómo funciona

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
dependencias: ahí van el [[circuit-breaker]] y la [[degradacion-controlada]].

## Ejemplo

En una tienda online, `GET /exp/store/products/{slug}` (Experience) llama a un ProductViewProcess,
que junta el producto (System Catálogo), su precio vigente (System Precios) y su stock (System
Inventario). El backoffice usa otra Experience sobre las mismas System.

## No confundir con

Un API gateway. El gateway enruta, autentica y limita tráfico, pero no orquesta datos de varios
servicios; puede estar delante de cualquiera de las tres capas.

## Relaciones

- Relacionado: [[multi-tenancy]] — el tenant se resuelve en la capa Experience y viaja a las de abajo.
- Ver también: [[circuit-breaker]] — se aplica en las llamadas de Process a System.
- Ver también: [[plataforma-api-first]] (Platform-Engineering) — API-first dice cómo se expone una
  capacidad; API-led, en qué capa va.
