---
resumen: >-
  Las características arquitectónicas son lo que el sistema tiene que cumplir además de su
  funcionalidad (rendimiento, disponibilidad, escalabilidad, costo), y esta vertical cubre cómo se
  eligen, cómo se miden y cómo se gobiernan para que no se degraden con el tiempo.
estado: vigente
estabilidad: estable
fuentes:
  - https://nealford.com/books/SAF2e.html
  - https://www.thoughtworks.com/en-us/insights/podcasts/technology-podcasts/rethinking-software-governance-reflecting-second-edition-building-evolutionary-architectures
  - https://huyenchip.com/2024/07/25/genai-platform.html
aliases: [características, -ilities, requisitos no funcionales]
creado: 2026-11-27
revisado: 2026-11-27
---

# Características

Las características arquitectónicas son lo que el sistema tiene que cumplir además de su
funcionalidad (rendimiento, disponibilidad, escalabilidad, costo), y esta vertical cubre cómo se
eligen, cómo se miden y cómo se gobiernan para que no se degraden con el tiempo.

Es la vertical que da el criterio a las demás. Las características priorizadas deciden qué
[estilo](../Estilos/estilos.md) conviene, la [modularidad](../Modularidad/modularidad.md) decide
dónde caen los límites para cumplirlas, y la
[evaluación y observabilidad](../Evaluacion-y-observabilidad/evaluacion-y-observabilidad.md)
verifica en producción que se cumplen. Cada elección de característica, con lo que se resignó, se
deja escrita en un [ADR](../Decisiones/adr.md).

## Elegir pocas, medirlas y gobernarlas

Richards y Ford separan el asunto en capítulos propios en la 2ª edición de *Fundamentals of
Software Architecture* (2025): qué es una característica, cómo se identifica, cómo se mide y se
gobierna, y cuál es su alcance. El orden es el de esta vertical. Primero se eligen las pocas que
importan, porque varias se contradicen entre sí (más disponibilidad suele costar más; más
seguridad suele sumar latencia). Después se les pone un número, porque "que sea mantenible" no se
puede verificar. Por último se automatiza la verificación con una
[fitness function](fitness-function.md), para que una característica no se pierda en silencio con
cada cambio.

## Lo que un modelo de IA pone al frente

En un sistema sin modelos, el costo y la latencia son características entre otras. Con un
[modelo de lenguaje](../../IA/llm.md) adentro, cada consulta tiene un costo que crece con los
tokens y una latencia que se parte en el primer token y los siguientes, y las dos se vuelven
decisiones de diseño de primera. Huyen las mide como métricas propias de la observabilidad de una
plataforma de IA generativa. Hay una tercera que no figura en el índice del canon: la calidad de una salida que
cambia de una vez a otra, que solo se mide con [evaluación](../Evaluacion-y-observabilidad/evaluacion.md).

## Qué hay adentro de Características

- [Características arquitectónicas](caracteristicas-arquitectonicas.md) — qué cuenta como
  característica, por qué se eligen pocas y por qué todo es un trade-off.
- [Fitness function](fitness-function.md) — la prueba automática que dice si el sistema sigue
  cumpliendo una característica; con un modelo, una evaluación con umbral.
- [Costo y latencia](costo-y-latencia.md) — TTFT, TPOT y costo por consulta, las características
  que un modelo vuelve de primera.
