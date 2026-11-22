---
resumen: >-
  La North Star es la métrica única que un equipo de producto elige para resumir el valor que los clientes reciben del producto, acompañada de unas pocas métricas de entrada que el equipo sí puede mover. La propuesta y sus criterios vienen de Amplitude, un vendedor de analítica, y no tienen un estudio que los respalde.
estado: borrador
estabilidad: semi
fuentes:
  - "Amplitude, North Star Playbook, introducción (los capítulos no se abrieron): https://amplitude.com/books/north-star/about-north-star-framework"
  - "Amplitude, What Makes a Good vs Bad North Star Metric: https://www.amplitude.com/blog/good-bad-north-star-metric"
  - "Amplitude, North Star, inputs, flywheels (vía buscador): https://amplitude.com/resources/north-star-inputs-flywheels"
  - "Producto/.investigacion/medicion-y-monetizacion.md"
  - "Producto/.investigacion/posicion-contraria.md (afirmación 1)"
aliases: [North Star Metric, NSM, métrica estrella del norte, North Star Framework]
creado: 2026-11-22
revisado:
---

# North Star

La North Star es la métrica única que un equipo de producto elige para resumir el valor que los clientes reciben del producto, acompañada de unas pocas métricas de entrada que el equipo sí puede mover. La propuesta y sus criterios vienen de Amplitude, un vendedor de analítica, y no tienen un estudio que los respalde.

Es una forma de poner en un número los [resultados](../Estrategia/resultados-y-entregables.md) que busca la [estrategia](../Estrategia/estrategia-de-producto.md). Dentro de la [medición](medicion-de-producto.md), contesta si el producto entrega valor en conjunto; si los usuarios nuevos llegan a ese valor lo contesta la [activación](activacion.md).

## Qué hace buena a una North Star, según Amplitude

Amplitude pone tres condiciones. La primera es el valor: "A good North Star Metric represents what customers value about your product". La segunda es la influencia: "Your North Star should be something you can influence or change". La tercera es que adelante los ingresos: tiene que subir antes que la facturación, no después.

De ahí salen las que descarta. Los indicadores rezagados, como "MRR or ARPU", llegan tarde para corregir algo. Las métricas de vanidad "look great on the surface but don't translate to meaningful business outcomes"; los ejemplos que da son usuarios activos diarios (DAU), usuarios registrados, páginas vistas, impresiones y tiempo en página.

## La métrica y sus métricas de entrada

El equipo no mueve la North Star directamente: mueve las métricas de entrada, y estas la mueven a ella. John Cutler lo dice así, citado por Amplitude: "If you can move your North Star directly, it's probably not a good North Star". Según un resumen del buscador, el playbook trata las métricas de entrada como la parte central y "often overlooked" del marco, y dice que dependen de cada negocio.

La separación ordena el trabajo: la North Star dice a dónde se va y las métricas de entrada, qué palanca toca cada equipo. Cómo se reparten las entradas entre equipos y cuándo se cambia la North Star está en capítulos del playbook que no se abrieron. El propio playbook avisa que "there are no silver bullets to success".

## Dónde se discute la North Star

> [!IMPORTANT]
> La lista de métricas malas es posición del vendedor, no consenso. Amplitude descarta el DAU, pero, según el informe de investigación (sin fuente citada), en muchos productos de consumo es la métrica que otros usan como North Star. El marco tampoco tiene un estudio que compare equipos que lo usan con equipos que no: es práctica publicada por quien vende la herramienta para medirlo.

La crítica de fondo es la [ley de Goodhart](../Estrategia/resultados-y-entregables.md#goodhart-cuando-el-resultado-se-vuelve-meta): una métrica que se vuelve meta se desvía de lo que medía. Una North Star sola no evita esa desviación (lectura de la base). La práctica prudente, según el informe de posición contraria, es acompañarla de métricas de guarda que avisen si se sube a costa de otra cosa.

> [!NOTE]
> Sin fuente todavía: el capítulo del playbook sobre cuándo cambiar la North Star, un ejemplo de métricas de entrada leído en el original y los textos originales de Goodhart, Campbell y Strathern.

## En qué se diferencia de una métrica por etapa

Lean Analytics propone mirar [una métrica que importa](../../Marketing/Medicion/metrica-que-importa.md) por vez, que cambia según la etapa del negocio: empatía, retención, viralidad, ingresos o escala. La North Star, en cambio, resume el valor que el producto entrega al cliente. Las dos piden concentrarse en un número; una sigue la etapa del negocio y la otra el valor para el cliente.

Tampoco es una métrica de vanidad en el sentido de Ries, que se trata en la [contabilidad de la innovación](../../Emprender/Validacion/contabilidad-de-la-innovacion.md): ahí la pregunta es si un número dice qué acción lo movió.

## Leer el North Star Playbook

La referencia es el [North Star Playbook de Amplitude](https://amplitude.com/books/north-star/about-north-star-framework), en los capítulos de definición y de métricas de entrada. Conviene fijarse en la separación entre la métrica y las entradas que el equipo sí mueve, y leerlo sabiendo que es de un vendedor de analítica. De este playbook solo se abrió la introducción.
