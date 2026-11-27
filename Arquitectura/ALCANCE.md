---
tema: Arquitectura
para: panorama de arquitectura de software para quien construye software hoy, con un modelo de IA como una pieza más del sistema
nivel: programa y conoce lo básico de servicios y APIs
escuela: AI engineering centrado en evaluación (Chip Huyen) sobre el canon de estilos y características (Richards y Ford)
fuera:
  - patrones de diseño de código (GoF), que irían en Desarrollo
  - el sistema con un modelo adentro (el modelo, su contexto, agentes, evaluación y producción), que vive en IA desde 2026-11-27
  - plataformas internas y API-first, que viven en Platform-Engineering
  - lo que pierde peso (entrenar modelos desde cero, trucos de prompt, frameworks de agentes pesados, SOA con ESB, space-based, ML clásico a medida, microservicios por defecto), que solo se nombra en Fundamentos/lo-que-pierde-peso
fuentes: []
preguntas:
  - Arranco un producto con un LLM adentro, ¿qué piezas pongo el primer día y cuáles después?
  - Para un SaaS chico, ¿monolito modular o microservicios?
  - ¿Cómo pruebo algo cuya salida cambia cada vez?
  - ¿Cuándo hace falta fine-tuning en lugar de mejorar el prompt o sumar RAG?
  - ¿Cómo registro una decisión de arquitectura para poder revisarla después?
  - ¿Qué de lo que se enseñaba en arquitectura ya no conviene aprender primero?
aprobado: 2026-11-27
---

# Alcance: Arquitectura

Un panorama de arquitectura de software escrito desde la mirada de Chip Huyen en *AI Engineering*: el sistema importa más que el modelo, la evaluación ocupa el centro y una pieza se suma solo cuando la medición la pide. Sale de una conversación del 2026-11-27, en la que se pidió el panorama sin lo que está perdiendo peso. Amplía y reordena el tema `Arquitectura/` que ya existía, con patrones de sistemas distribuidos.

## Árbol

```
Arquitectura/
  arquitectura.md               el todo, con el catálogo de patrones (problema → patrón)
  Caracteristicas/              definir, medir y gobernar las características
    caracteristicas-arquitectonicas
    fitness-function
    costo-y-latencia
  Modularidad/                  límites, acoplamiento y cohesión
    modularidad
    aislar-lo-no-determinista
  Estilos/                      las formas de armar el sistema y cómo se elige
    monolito-modular
    estilos-simples             capas, pipeline y microkernel
    service-based               pocos servicios grandes, el paso intermedio
    event-driven
    microservicios
    elegir-un-estilo
    strangler-fig               migrar de un estilo a otro sin apagar el sistema
  Sistemas-distribuidos/        las ocho notas que ya existían, más los patrones que faltaban
    api-led-connectivity, multi-tenancy, circuit-breaker, degradacion-controlada, saga,
    clave-de-idempotencia, resilience4j-en-spring-boot (ficha)
    outbox, cqrs (con event sourcing), api-gateway-y-bff
  Decisiones/
    adr
    empezar-simple
    analisis-de-riesgo
    diagramas
  Fundamentos/
    escuelas-de-arquitectura
    lo-que-pierde-peso
    bibliografia-de-arquitectura
```

## Supuestos

- Se reordena el tema existente en lugar de crear uno aparte; las ocho notas viejas se mudan a `Sistemas-distribuidos/` y se actualizan sus enlaces en toda la base.
- Las verticales que van más hondo eran `Sistemas-con-modelos/` y `Evaluacion-y-observabilidad/`; los estilos clásicos quedan en panorama.
- El 2026-11-27, al rehacer el tema IA, esas dos verticales se mudaron a `IA/` (Sistemas con modelos a `IA/Produccion/`, `IA/Contexto/` y `IA/Agentes/`; Evaluación a `IA/Evaluacion/`, y la observabilidad a `IA/Produccion/`). Arquitectura se queda con la base sobre la que se montan.
- Los patrones viven en la vertical de su problema; la entrada del tema los junta en un catálogo.
- La investigación sumó service-based (el canon lo trata como estilo propio) y análisis de errores (el campo lo trata aparte de la evaluación), y llevó strangler fig a Estilos, porque es una técnica de migración.
- Harness engineering no es de Huyen (el ensayo de 2026 es de Lilian Weng): va como sección fechada de `agente`, citada a sus autores.
- Fuera de lo que Huyen dice (frameworks de agentes y fine-tuning prematuros), la lista de lo que pierde peso es criterio propio y se escribe como tal.
