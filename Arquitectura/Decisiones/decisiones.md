---
resumen: >-
  Las decisiones de arquitectura son las elecciones de estructura que cuestan caro cambiar, y esta
  vertical cubre cómo se toman, cómo se registran, cómo se analizan sus riesgos y cómo se dibujan,
  empezando siempre por lo más simple que funcione.
estado: vigente
estabilidad: estable
fuentes:
  - https://nealford.com/books/SAF2e.html
  - https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions
  - https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html
  - https://c4model.com/
aliases: [decisiones de arquitectura, architectural decisions]
creado: 2026-11-27
revisado: 2026-11-27
---

# Decisiones

Las decisiones de arquitectura son las elecciones de estructura que cuestan caro cambiar, y esta
vertical cubre cómo se toman, cómo se registran, cómo se analizan sus riesgos y cómo se dibujan,
empezando siempre por lo más simple que funcione.

Es la vertical que deja rastro de las demás. Elegir un [estilo](../Estilos/estilos.md), priorizar
una [característica](../Caracteristicas/caracteristicas.md) sobre otra o sumar una pieza a un
[sistema con modelos](../../IA/Produccion/sistemas-con-modelos.md) son decisiones; esta
vertical dice cómo se toman y cómo se guardan. La evidencia para tomarlas llega de la
[evaluación y la observabilidad](../../IA/Evaluacion/evaluacion.md).
La definición de "cuestan caro cambiar" es de trabajo de esta base; ninguna fuente leída la formula así. Richards y Ford agrupan decisiones, análisis de riesgo y diagramas en la parte de técnicas de su
libro, y esta vertical sigue esa división.

## Decidir, registrar y revisar

Una decisión de arquitectura sale bien, según esta base, cuando se pueden reconstruir sus razones años después. El
ciclo tiene cuatro piezas:

1. **Partir de lo más simple** que podría funcionar y sumar complejidad solo con evidencia. Huyen
   cuenta "Starting too complex" entre los errores comunes al construir con modelos; es la regla de
   [empezar simple](empezar-simple.md).
2. **Mirar qué puede salir mal** antes de comprometerse, en grupo y sobre un diagrama: es el
   [análisis de riesgo](analisis-de-riesgo.md).
3. **Escribir la decisión** con su contexto, lo elegido y sus consecuencias, en un texto corto que
   vive junto al código: es el [ADR](adr.md), que Michael Nygard popularizó en 2011.
4. **Dibujar la estructura** con un vocabulario que todos lean igual, para que el ADR y el análisis
   de riesgo tengan sobre qué apoyarse: son los [diagramas](diagramas.md), con C4 como modelo de ejemplo.

Una decisión tomada no se reescribe: si cambia el contexto, se escribe otra que la reemplaza. Con
un modelo de IA adentro, además del estilo se deciden el modelo, el umbral de la evaluación y cada
pieza nueva, y cada una de esas decisiones envejece rápido porque los modelos cambian.

## Qué hay adentro de Decisiones

- [ADR](adr.md) — el registro corto de una decisión, de Nygard a MADR.
- [Empezar simple](empezar-simple.md) — sumar una pieza solo cuando la medición la pide; el
  principio que comparten Huyen y Anthropic, y que Fowler defiende para los monolitos.
- [Análisis de riesgo](analisis-de-riesgo.md) — risk storming y la matriz de impacto por
  probabilidad.
- [Diagramas](diagramas.md) — el modelo C4 y sus cuatro niveles.
