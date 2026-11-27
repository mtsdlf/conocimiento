---
resumen: >-
  La forma es cómo se agrupan los pulsos de un tema en compases, frases y secciones. En la
  transición decide dónde puede entrar y salir cada tema, y la regla práctica es que los dos
  estén en el mismo lugar de su frase.
estado: borrador
estabilidad: estable
fuentes:
  - "Mark J. Butler, Turning the Beat Around, Music Theory Online 7.6 (2001): https://mtosmt.org/issues/mto.01.7.6/mto.01.7.6.butler.php"
  - "Kim, Choi, Sacks, Yang y Nam, ISMIR 2020: https://arxiv.org/abs/2008.10267"
  - "Ryan Dejaegher, How to DJ 101: Why You Must Understand Phrasing, DJ TechTools (2014): https://djtechtools.com/2014/11/16/how-to-dj-101-why-you-must-understand-phrasing/"
  - "Ryan Keeling, técnicas de mezcla por género, Pioneer DJ blog: https://blog.pioneerdj.com/?p=6295"
  - "Wayne Marshall, reseña de Unlocking the Groove, Music Theory Spectrum 31 (2009): https://wayneandwax.com/academic/mts-butler-unlocking-groove.pdf"
  - "DJ/.investigacion/tiempo-y-forma.md"
  - "DJ/.investigacion/posicion-contraria.md"
aliases: [Estructura, Phrasing, Fraseo]
creado: 2026-11-27
revisado:
---

# Forma

La forma es cómo se agrupan los pulsos de un tema en compases, frases y secciones. En la
transición decide dónde puede entrar y salir cada tema, y la regla práctica es que los dos
estén en el mismo lugar de su frase.

Recibe de [Tiempo](../Tiempo/tiempo.md) el pulso que cuenta: sin pulsos juntos no hay compás
común. Entrega al [Espectro](../Espectro/espectro.md) el cuándo: las guías de práctica sitúan el
cambio de grave en un límite de frase. Y las secciones de un tema, con sus breaks y subidas, son
la materia de la [Energía](../Energia/energia.md).

## De pulso a sección

La forma se arma en niveles, cada uno hecho de varios del anterior:

| Nivel | De qué está hecho | Cómo se reconoce |
|---|---|---|
| Compás | 4 pulsos | El "1" cae con el pulso fuerte |
| Frase | 8 compases = 32 pulsos | Algo cambia al empezar la siguiente |
| Bloque mayor | 16 compases = 64 pulsos | Dos frases seguidas |
| Sección | Una o varias frases | Intro, cuerpo, break, subida, salida |

Casi toda la música electrónica de baile está en 4/4, según Butler
([Butler 2001](https://mtosmt.org/issues/mto.01.7.6/mto.01.7.6.butler.php)). El valor de la
frase vive en [frase](frase.md), con la discrepancia de unidades entre fuentes: unas cuentan en
pulsos y otras en compases.

## Por qué se alinean las frases

Alinear frases es hacer que el compás 1 de una frase del tema nuevo caiga con el compás 1 de una
frase del que suena. Así los cambios de los dos temas coinciden. Si no, un cambio de un tema cae
a mitad de una frase del otro; ninguna fuente mide si eso le suena peor al público.

Kim y otros midieron que los largos de transición en 1557 mezclas reales se agrupan en múltiplos
de 32 pulsos, y lo leen como DJs que siguen la estructura repetitiva de la música de baile
([ISMIR 2020](https://arxiv.org/abs/2008.10267)). El corpus es sobre todo de house y trance, y los
autores advierten que su método funciona mal con techno. Las cifras están en
[puntos de entrada y salida](puntos-de-entrada-y-salida.md#lo-que-muestran-las-mezclas-reales).

> [!IMPORTANT]
> Disputado: si alinear frases es necesario o solo habitual. Se sostiene como regularidad de lo
> que hacen los DJs de baile. No hay ningún dato de que una transición desalineada suene peor al
> público, y los mismos datos de Kim muestran que DJs distintos eligen puntos distintos en el
> mismo tema. Las posiciones están en
> [puntos de entrada y salida](puntos-de-entrada-y-salida.md#cuándo-se-rompe-la-regla).

## Dónde falla la forma

La forma falla por tres lados. Por Tiempo: si la grilla de la máquina tiene el "1" corrido, los
pulsos coinciden pero los compases no (ver [sync y beatgrid](../Tiempo/sync-y-beatgrid.md)). Por
conteo: se cuenta desde un compás que no abre frase, y todo queda corrido. Y por el tema mismo:
algunos temas desplazan el "1" o cambian de frase a propósito, un recurso que Butler llama
disonancia métrica.

Un blog de Pioneer describe los sets de techno como "a single evolving machine, often making it
hard to tell where one tracks ends and another begins"
([Pioneer DJ](https://blog.pioneerdj.com/?p=6295)). Ninguna fuente leída dice cómo afecta eso al
reconocimiento de las frases.

## Qué hay adentro de Forma

- [Frase](frase.md): compás, pulso fuerte y frase de 8 compases (32 pulsos); cómo se cuenta y
  cómo se reconoce el comienzo de una frase.
- [Secciones de un tema](secciones-de-un-tema.md): intro, cuerpo, break, subida y salida, y los
  temas pensados para ser mezclados.
- [Puntos de entrada y salida](puntos-de-entrada-y-salida.md): dónde entra y sale un tema, cómo
  se alinean frases, lo que muestran las mezclas reales y cuándo se rompe la regla.

La ficha de cómo un programa analiza frases está en
[sync en reproductores](../Tiempo/ficha-sync-en-reproductores.md#lo-que-el-mismo-análisis-hace-con-las-frases),
porque sale del mismo análisis que la grilla.
