---
resumen: >-
  Los mitos de producto son frases que circulan como reglas (el PM es el CEO del producto, el cliente sabe lo que quiere, más funcionalidades dan más valor, la mayoría de las ideas funciona, 7 amigos en 10 días, los efectos de red garantizan ganar) sin estudio detrás o contra lo que miden los estudios. Cada uno, con su origen, la evidencia y la nota donde se trata.
estado: borrador
estabilidad: semi
fuentes:
  - "Ben Horowitz, Good Product Manager/Bad Product Manager (a16z): https://a16z.com/good-product-manager-bad-product-manager/"
  - "Marty Cagan, Product vs. Feature Teams (SVPG, 29-ago-2019): https://www.svpg.com/product-vs-feature-teams/"
  - "Mind the Product, Product is hard, by Marty Cagan (2019): https://www.mindtheproduct.com/product-is-hard-by-marty-cagan/ (resumen)"
  - "Scrum Guide 2020: https://scrumguides.org/scrum-guide.html"
  - "Cagan, Customers Are Not The Source Of Innovation (Business of Software): https://businessofsoftware.org/talks/customers-are-not-the-source-of-innovation/ (solo metadatos)"
  - "Will Larson, notas sobre Perri, Escaping the Build Trap: https://lethain.com/notes-escaping-the-build-trap/"
  - "Kohavi y Thomke, The Surprising Power of Online Experiments, HBR (2017), reimpresión R1705E: https://web-docs.stern.nyu.edu/executive/The%20Surprising%20Power%20of%20Online%20Experiments.pdf"
  - "Kohavi et al., Online Controlled Experiments at Large Scale (KDD 2013): https://exp-platform.com/large-scale/ (abstract)"
  - "Andrew Chen, sobre 7 friends in 10 days: https://andrewchen.com/my-quora-answer-to-how-do-you-find-insights-like-facebooks-7-friends-in-10-days-to-grow-your-product-faster/"
  - "25iq, A dozen lessons on growth (2017): https://25iq.com/2017/02/10/a-dozen-lessons-on-growth (resumen)"
  - "Eisenmann, Parker y Van Alstyne, Strategies for Two-Sided Markets, HBR 84(10), 2006: https://www.kth.se/social/files/546b8e7ef2765474dd3f23fe/4.Eisenmann+et+al+(2006).pdf"
  - "McIntyre, Beyond a Winner-Takes-All Strategy for Platforms, MIT Sloan Management Review: https://sloanreview.mit.edu/article/beyond-a-winner-takes-all-strategy-for-platforms"
  - "MIT Sloan, Digital platforms: high valuations, high risk of failure: https://mitsloan.mit.edu/ideas-made-to-matter/digital-platforms-high-valuations-high-risk-failure (resumen)"
  - "Yoffie, How to be a business platform leader, HBS Working Knowledge: https://hbswk.hbs.edu/item/how-to-be-a-business-platform-leader (resumen)"
  - "Producto/.investigacion/posicion-contraria.md; Producto/.investigacion/organizacion-y-fundamentos.md, sección 3.4; Producto/.investigacion/medicion-y-monetizacion.md, sección 2; Producto/.investigacion/plataformas.md"
aliases: [mitos de producto, product management myths, PM CEO del producto, 7 friends in 10 days, el cliente sabe lo que quiere, winner takes all]
creado: 2026-11-22
revisado:
---

# Mitos de producto

Los mitos de producto son frases que circulan como reglas (el PM es el CEO del producto, el cliente sabe lo que quiere, más funcionalidades dan más valor, la mayoría de las ideas funciona, 7 amigos en 10 días, los efectos de red garantizan ganar) sin estudio detrás o contra lo que miden los estudios. Cada uno, con su origen, la evidencia y la nota donde se trata.

La mayoría de las refutaciones también es opinión de practicantes contra practicantes. Solo dos mitos tienen estudios con método en contra: el de las ideas que funcionan (experimentos controlados) y el de los efectos de red (modelos económicos y conteos de fracasos).

## De dónde viene cada mito y qué dice la evidencia

| Mito | De dónde viene | Qué dice la evidencia | Dónde se trata |
|---|---|---|---|
| "El PM es el CEO del producto" | Horowitz: "A good product manager is the CEO of the product." La página de a16z avisa que "was written 15 years ago and is probably not relevant for today's product managers" | No se encontró refutación explícita. Cagan usa la frase como aspiración de entender todas las dimensiones del producto (por resumen). El Scrum Guide no usa "CEO": el product owner responde por el valor | [Roles de producto](../Organizacion/roles-de-producto.md) |
| "El cliente sabe lo que quiere" | Sin origen rastreado | Sin fuente primaria en producto: una charla de Cagan, "Customers Are Not The Source Of Innovation", no se abrió. El tema UX trata el mito equivalente, "los usuarios saben lo que quieren", con un artículo de Nielsen (2001) | [Mitos de UX](../../UX/Fundamentos/mitos-de-ux.md) y [Árbol de oportunidades](../Descubrimiento/arbol-de-oportunidades.md) |
| "Más funcionalidades, más valor" | La práctica de medir entregables | Perri llama "build trap" a cuando "the number of features shipped becomes the primary metric of success" (según Larson). Es tesis de escuela, sin estudio | [Resultados y entregables](../Estrategia/resultados-y-entregables.md) |
| "La mayoría de las ideas funciona" | Sin origen rastreado; Kohavi y Thomke dicen que "even experts often misjudge which ones will pay off" | Kohavi y Thomke (2017): "At Google and Bing, only about 10% to 20% of experiments generate positive results. At Microsoft as a whole, one-third prove effective, one-third have neutral results, and one-third have negative results." Es el mito con más evidencia en contra | [Experimento A/B](../Medicion/experimento-ab.md) |
| "7 amigos en 10 días" | Relatos de Chamath sobre el equipo de crecimiento de Facebook | Sin documento primario de Facebook; un relato dice que se dudó con "10 friends in 14 days". Chen advierte que es correlación: "fire engines correlate with house fires, but that doesn't mean that fire engines CAUSE house fires" | [Activación](../Medicion/activacion.md) |
| "Los efectos de red garantizan ganar" | Sin origen rastreado | Eisenmann et al. (2006) piden tres condiciones para que gane una sola plataforma. McIntyre: winner-takes-all encaja en redes sociales y subastas, pero en muchos mercados sobreviven varias. Según Yoffie (por entrevista), Cusumano, Gawer y Yoffie cuentan 209 plataformas fracasadas entre 1995 y 2015 | [Efecto de red](../Plataformas/efecto-de-red.md) |

## Los matices que no entran en la tabla

Las ideas que fallan. Las cifras varían según la fuente y la familia Kohavi cuenta como una sola fuente. El abstract de KDD 2013 dice que "many ideas impact key metrics by 1% and are not well estimated a-priori". Son datos de buscadores y plataformas con mucho tráfico, en dominios ya muy optimizados. Que en un producto chico pase lo mismo es una inferencia, pero ninguna fuente halló tasas de éxito más altas en otros contextos.

El método detrás de los 7 amigos. Chen rescata el método: definir la métrica de éxito, ver qué comportamientos se correlacionan con ella, formular una hipótesis y probarla con un experimento. Dice que el umbral importa menos que tener una meta memorable: "10 friends in 12 days" serviría igual.

Las condiciones del ganador único. Eisenmann, Parker y Van Alstyne piden costos altos de usar varias plataformas a la vez para al menos un lado, efectos cruzados fuertes y poca diferenciación técnica. Yoffie lo resume así, por resumen de una entrevista: "The most important driver of success is network effects. But network effects are not enough." Según MIT Sloan, "The vast majority of digital platforms fail. And they fail quickly". La cifra de 209 fracasos sale de una entrevista y otras notas dan 43 o 45 éxitos; conviene confirmarla contra el libro.

## Confusiones del campo

Además de los mitos, el informe documenta confusiones que se cuelan en la práctica:

- Empoderar es no pedir fechas ni controles. NN/g describe equipos "empoderados" que no controlan nada relevante. Cagan define el empoderamiento como recibir problemas y elegir la solución. Ver [Equipo empoderado](../Organizacion/equipo-empoderado.md).
- Descubrir es hablar con N clientes por semana. Críticas de practicantes (por resumen) cuentan equipos que cumplieron la cuota y aun así hicieron algo que nadie quiso. La cuenta no garantiza aprendizaje.
- Founder mode se opone a delegar. Graham dice que todavía no se entiende bien y que puede usarse de excusa. La disputa está en [founder mode](../Organizacion/equipo-empoderado.md#founder-mode-el-fundador-en-los-detalles).
- Product management es un rol obligatorio. Basecamp funcionó sin un PM dedicado; es un caso, de una empresa chica con un producto, y está en [empresas sin product manager](../Organizacion/roles-de-producto.md#empresas-sin-product-manager).
- El product owner es lo mismo que el product manager. El Scrum Guide solo define una responsabilidad dentro del equipo; ninguna fuente primaria los iguala.

> [!NOTE]
> Sin fuente todavía: el origen del mito "el cliente sabe lo que quiere" en producto, una refutación explícita de "CEO del producto" por Cagan o por Horowitz, y la confusión entre product manager y project manager documentada. Lo que distingue a los dos roles está en [Qué es producto](que-es-producto.md).
