---
resumen: >-
  La deuda técnica es el costo futuro de un atajo o de un diseño que ya no calza: cada cambio en esa
  zona paga intereses en tiempo y defectos. Se paga cuando los intereses pesan más que el costo de
  arreglarla, y no siempre conviene pagarla.
estado: borrador
estabilidad: semi
fuentes:
  - https://queue.acm.org/detail.cfm?id=2168798
  - https://martinfowler.com/bliki/TechnicalDebtQuadrant.html
  - https://research.chalmers.se/en/publication/507477
  - https://research.chalmers.se/publication/500162
  - https://arxiv.org/abs/2203.04374v1
  - https://arxiv.org/abs/2511.04427
  - https://www.gitclear.com/ai_assistant_code_quality_2025_research
  - https://www.thoughtworks.com/content/dam/thoughtworks/documents/radar/2026/04/tr_technology_radar_vol_34_en.pdf
aliases: [technical debt, deuda de código, tech debt, cuadrante de deuda técnica]
creado: 2026-11-27
revisado:
---

# Deuda técnica

La deuda técnica es el costo futuro de un atajo o de un diseño que ya no calza: cada cambio en esa zona paga intereses en tiempo y defectos. Se paga cuando los intereses pesan más que el costo de arreglarla, y no siempre conviene pagarla.

Según Fowler, Ward Cunningham introdujo la metáfora en un informe de OOPSLA de 1992; la frase que se le atribuye, según un artículo de ACM Queue de 2012, es "Shipping first-time code is like going into debt." El original no se leyó.

## Los cuatro tipos de deuda

Fowler (2009) la ordena en un cuadrante con dos ejes: si fue deliberada o inadvertida, y si fue prudente o imprudente.

| | Imprudente | Prudente |
|---|---|---|
| **Deliberada** | se conocen las buenas prácticas y se elige ir rápido y sucio porque se cree que no hay tiempo | se toma el atajo sabiendo que es deuda y pensando si salir antes compensa el costo de pagarla |
| **Inadvertida** | el equipo ignora las prácticas de diseño y no advierte cuánta deuda toma | se descubrió el mejor diseño después de construir |

Para Fowler, la deuda prudente e inadvertida es común e inevitable en equipos que diseñan muy bien: entregan software valioso y recién después descubren un diseño mejor. La metáfora sirve, para él, para comunicarse con personas no técnicas, como la gerencia de un cliente.

## Cuándo se paga y cuándo no

Para Fowler, la deuda prudente "may not be worth paying down if the interest payments are sufficiently small", por ejemplo en una parte del código que rara vez se toca. El corolario, que esta base propone como criterio propio, es pagarla donde el código cambia seguido y cada cambio cuesta más de lo que debería.

En la práctica eso se decide así:

1. Ubicá dónde cambia el código: las zonas que se tocan en casi cada entrega son las que cobran intereses.
2. Estimá cuánto más cuesta cada cambio ahí que en una zona sana.
3. Pagá la deuda de esas zonas en pasos chicos, cada uno con pruebas, como parte del trabajo normal y no como un proyecto aparte: es [refactorizar](refactorizar.md).
4. Dejá la deuda de las zonas quietas donde está.

> [!NOTE]
> Sin fuente todavía: ubicar la deuda por frecuencia de cambio y los cuatro pasos de arriba son criterio de esta base; no se leyó una fuente que los sostenga con datos.

## Cuánto cuesta, según los estudios

> [!IMPORTANT]
> Las mediciones del costo existen pero son pocas, autoinformadas o de un vendedor de herramientas, y no deben mezclarse entre sí.
> - **23 % del tiempo** (Besker, Martini y Bosch, Journal of Systems and Software, 2019): según su resumen, los desarrolladores pierden en promedio ese porcentaje por deuda técnica, en encuestas semanales durante unos diez meses más entrevistas. La actividad más común era hacer pruebas adicionales, y los gerentes en general no sabían que se perdía un cuarto del tiempo. Es autoinforme.
> - **36 % del tiempo** (Besker et al., ICSME 2017): otra medición distinta, según su resumen.
> - **15 veces más defectos** (Tornhill y Borg, TechDebt 2022): en 39 bases de código propietarias, el código de baja calidad tiene unas 15 veces más defectos, resolver issues lleva 124 % más de tiempo y los tiempos máximos de ciclo son 9 veces mayores, según su resumen. La métrica de calidad es la del producto que vende el autor.

## La deuda que acumula un agente

Hay un estudio causal sobre deuda y agentes. He et al. (MSR 2026) compararon, con diferencias en diferencias, repositorios que adoptaron un editor con agente frente a repositorios de control. Según el resumen del preprint, la ganancia de velocidad fue transitoria y el aumento de advertencias de análisis estático y de complejidad fue persistente; la versión preliminar da cerca de 30 % y 41 %, cifras a confirmar en la publicada.

GitClear, que vende análisis de código, midió 211 millones de líneas cambiadas de 2020 a 2024. Según su resumen, las líneas copiadas y pegadas pasaron de 8,3 % a 12,3 % y las movidas, que señalan refactor, bajaron de 24,1 % a 9,5 %; 2024 fue el primer año en que se copió más de lo que se movió. Mide patrones en el diff, no defectos, y es observacional.

Con eso, esta base sostiene una inferencia: un agente acumula deuda más rápido y a la vez la puede pagar barato. Decidir qué deuda pagar queda en personas; pagarla, con pruebas que fijen el comportamiento, puede quedar en agentes. Thoughtworks (Radar de abril de 2026, según un resumen) llama "cognitive debt" a una variante (ver [agente de código](../Construccion/agente-de-codigo.md)): adoptar soluciones generadas sin armar el modelo mental de cómo funcionan.

## Medir la deuda en puntos pierde peso

[Pierde peso](../Fundamentos/lo-que-pierde-peso-en-desarrollo.md#lo-que-pierde-peso-en-cada-etapa), en criterio de esta base, medir la deuda en puntos de historia (story points) o reservar un porcentaje fijo de cada iteración para pagarla. Ninguna fuente leída lo estudia. El cuadrante sigue valiendo como vocabulario. Las decisiones de estructura que generan deuda grande, como acoplar módulos que deberían estar separados, son de [Arquitectura](../../Arquitectura/Modularidad/modularidad.md).

Para leer: el cuadrante de Fowler, que es breve, y Besker 2019 para el costo.
