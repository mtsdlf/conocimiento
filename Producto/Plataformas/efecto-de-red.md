---
resumen: >-
  Hay efecto de red cuando el valor de un producto para cada usuario cambia según cuántos y quiénes más lo usan. Puede darse dentro de un mismo grupo de usuarios o entre grupos distintos, y puede sumar o restar valor.
estado: borrador
estabilidad: estable
fuentes:
  - "Michael Katz y Carl Shapiro (1985), Network Externalities, Competition, and Compatibility, AER 75(3):424-440: https://blog.rchss.sinica.edu.tw/FCLai/wp-content/uploads/2016/11/980730_Network-Externalities-Competition-and-Compatibility_Michael-L.-Katz-and-Carl-Shapiro-1985_AER-753_p.424-440.pdf (no se abrió; según bibliografía y citas)"
  - "Thomas Eisenmann, Geoffrey Parker y Marshall Van Alstyne (2006), Strategies for Two-Sided Markets, HBR 84(10):92-101: https://www.kth.se/social/files/546b8e7ef2765474dd3f23fe/4.Eisenmann+et+al+(2006).pdf (leído en pasajes)"
  - "Bob Briscoe, Andrew Odlyzko y Benjamin Tilly (2006), Metcalfe's Law is Wrong, IEEE Spectrum: https://spectrum.ieee.org/metcalfes-law-is-wrong (según resumen); y Odlyzko y Tilly (2005), A refutation of Metcalfe's Law: https://www.Gwern.net/doc/economics/automation/metcalfes-law/2005-odlyzko.pdf (según resumen)"
  - "Frank Vanhove (2014), crítica a Odlyzko y Tilly: https://www.Gwern.net/doc/economics/automation/metcalfes-law/2014-vanhove.pdf (según resumen)"
  - "Feng Zhu y Marco Iansiti (2012), Entry into platform-based markets, Strategic Management Journal 33(1):88-106: https://ideas.repec.org/a/bla/stratm/v33y2012i1p88-106.html (solo abstract)"
  - "Feng Zhu y Marco Iansiti (2019), Why Some Platforms Thrive and Others Don't, HBR, según el resumen de https://maaw.info/ArticleSummaries/ArtSumZhuandIansiti2019.htm"
  - "David McIntyre, Beyond a 'Winner-Takes-All' Strategy for Platforms, MIT Sloan Management Review: https://sloanreview.mit.edu/article/beyond-a-winner-takes-all-strategy-for-platforms"
  - "Parker, Van Alstyne y Choudary, Platform Revolution (2016), cap. 2 Network effects: The Power of the Platform, p. 16 (no leído; solo el índice: https://toc.uni.li/FLMF051021.pdf)"
  - "Producto/.investigacion/plataformas.md"
  - "Producto/.investigacion/posicion-contraria.md (afirmación 6)"
aliases: [network effect, network effects, efectos de red, externalidad de red, network externality, ley de Metcalfe]
creado: 2026-11-22
revisado:
---

# Efecto de red

Hay efecto de red cuando el valor de un producto para cada usuario cambia según cuántos y quiénes más lo usan. Puede darse dentro de un mismo grupo de usuarios o entre grupos distintos, y puede sumar o restar valor.

Es el mecanismo que hace que una [plataforma](plataformas.md) funcione como tal. Las decisiones que salen de él, como a qué lado cobrarle o cómo arrancar sin usuarios, están en [mercado de dos lados](mercado-de-dos-lados.md).

## De dónde sale la idea: Katz y Shapiro

Katz y Shapiro (1985) formalizaron que la utilidad de un bien crece con el número de otros usuarios. Según la bibliografía que los cita, de ese paper sale la definición de "externalidad de red" y su vínculo con la compatibilidad, la adopción y el encierro del usuario. El paper trata efectos directos en productos de un solo lado; la extensión a dos lados vino después. Esta base no leyó el texto original, solo las citas.

## Del mismo lado y entre lados

Eisenmann, Parker y Van Alstyne (2006) separan dos efectos. El del mismo lado ("same-side") es el que un usuario recibe de otros usuarios de su mismo grupo. El cruzado ("cross-side") es el que recibe del otro grupo. Lo dicen así: "Cross-side network effects are typically positive, but they can be negative (TV viewers preferring fewer ads). Same-side network effects are often negative (sellers preferring fewer rivals in a B2B exchange), but they may be positive".

| Efecto | Signo habitual | En una plataforma de tiendas online |
|---|---|---|
| Cruzado | positivo, a veces negativo | más compradores hacen más valiosa la plataforma para los comerciantes, y más comerciantes con apps instaladas, para los desarrolladores |
| Del mismo lado | negativo, a veces positivo | los comerciantes compiten entre sí por los mismos compradores: más vendedores del mismo rubro restan |

La columna de la plataforma de tiendas es una aplicación de la distinción, no un dato medido. Un efecto negativo también aparece por calidad, como en un listado de apps lleno de apps malas; por qué las consolas filtran a los desarrolladores y qué arriesga un listado abierto está en el [ecosistema de terceros](ecosistema-de-terceros.md).

## Cuánto crece el valor: la disputa sobre Metcalfe

La ley de Metcalfe dice que el valor de una red crece con el cuadrado del número de usuarios. Es la cifra que más se repite y la que más se discute.

> [!IMPORTANT]
> En contra de Metcalfe: Odlyzko y Tilly (2005), y luego Briscoe, Odlyzko y Tilly en IEEE Spectrum (2006), sostienen que "the value of a network of size n grows in proportion to n log(n)". El argumento usa la ley de Zipf: no todas las conexiones se usan con la misma intensidad, así que las nuevas valen menos que las primeras. Son el mismo grupo de autores, así que cuentan como una sola fuente. Se leyeron por resúmenes.
>
> A favor de Metcalfe: Zhang, Liu y Xu (2015) dicen respaldarla con datos de Tencent y Facebook; el dato llegó vía Wikipedia y no se verificó en el origen. Vanhove (2014) objeta uno de los argumentos de Odlyzko y Tilly, también según resumen.
>
> La disputa sigue abierta. Para decidir en un producto alcanza con esto: el valor crece más rápido que la cantidad de usuarios, pero no sin tope ni de forma pareja.

## Importa la estructura de la red, no solo el tamaño

Contar usuarios no dice cuánto protege un efecto de red. Zhu e Iansiti (2012), según su abstract, modelan cuándo un competidor puede entrar a un mercado de plataformas. La entrada depende de la fuerza de los efectos de red indirectos y del descuento de los consumidores, y lo aplican a Xbox frente a PlayStation 2. Tiene método, modelo y estimación, pero es de un solo mercado.

En HBR (2019), según un resumen de terceros, los mismos autores listan cinco propiedades de la red:

1. La fuerza de los efectos de red.
2. El agrupamiento de la red.
3. El riesgo de desintermediación: que los lados se conozcan y sigan por fuera.
4. La vulnerabilidad al multi-homing: que los usuarios estén en varias plataformas a la vez.
5. Los puentes a otras redes.

Sostienen que esa estructura importa más que la escala y que los efectos de red pueden cambiar con el tiempo. Para ellos los efectos de red dependen de esas propiedades; no los consideran débiles en general. Las frases son paráfrasis del resumen, no citas.

McIntyre, en un artículo de revisión, va en la misma dirección: "the fundamental distinction in platform-based markets is no longer whether there are network effects or not". El efecto puede ser entre lados, local o informacional, y la idea de que más usuarios siempre implica más valor no vale como regla general.

## Dónde se confunde con otras cosas

Un efecto de red habla del valor que recibe cada usuario. El crecimiento por recomendación, en que cada usuario trae a otros, habla de cómo se adquieren clientes y está en [motores de crecimiento](../../Emprender/Crecimiento/motores-de-crecimiento.md), del tema Emprender. Un producto puede tener uno sin el otro: esto es una distinción de esta base, no de las fuentes leídas.

Para la versión de escuela, *Platform Revolution* dedica el capítulo 2, "Network effects: The Power of the Platform", al tema. No se leyó.

> [!NOTE] Sin fuente todavía: el capítulo 2 de Platform Revolution, el texto completo de Katz y Shapiro y el mapa de efectos de red de NFX, que se nombra seguido pero no se verificó.
