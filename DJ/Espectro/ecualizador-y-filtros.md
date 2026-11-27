---
resumen: >-
  El ecualizador del mixer sube o baja bandas de frecuencia de cada canal, y en la mezcla sirve
  para repartir el espacio entre dos temas. El kill y el isolator apagan una banda entera; los
  filtros sacan todo lo que está por arriba o por debajo de un punto.
estado: vigente
estabilidad: estable
fuentes:
  - "Native Instruments, Traktor Pro 2 EQ and filter models: https://support.native-instruments.com/support/solutions/articles/69000879507-traktor-pro-2-eq-and-filter-models"
  - "Foro de la comunidad Pioneer DJ, modos EQ e isolator (usuario, resumen del buscador): https://community.pioneerdj.com/hc/en-us/community/posts/22980396236697/comments/22989884666137"
  - "Algoriddim, manual de djay Pro, Sound (resumen del buscador): https://help.algoriddim.com/user-manual/djay-pro-mac/settings/sound"
  - "Mike Senior, Mixing Bass, Sound On Sound, sept. 2012: https://www.soundonsound.com/techniques/mixing-bass"
  - "MusicRadar, harmonic mixing (resumen del buscador): https://musicradar.com/news/harmonic-mixing"
aliases: [EQ, Ecualizador, Kill, Isolator, Filtro, HPF, LPF]
creado: 2026-11-27
revisado: 2026-11-27
---

# Ecualizador y filtros

El ecualizador del mixer sube o baja bandas de frecuencia de cada canal, y en la mezcla sirve
para repartir el espacio entre dos temas. El kill y el isolator apagan una banda entera; los
filtros sacan todo lo que está por arriba o por debajo de un punto.

## Tres bandas para repartir el espacio

El EQ (ecualizador) típico de un canal de mixer tiene tres perillas: graves (LOW), medios (MID)
y agudos (HIGH). Como dos temas en la misma banda se [enmascaran](enmascaramiento.md), bajar una
banda de un tema le hace lugar a la misma banda del otro. El uso central es el
[swap de graves](swap-de-graves.md): el LOW de un tema baja mientras el del otro sube.

Las otras dos bandas seguirían la misma lógica con menos urgencia: por la asimetría del
enmascaramiento, los agudos de dos temas tolerarían mejor la superposición que los graves. Es
inferencia de esta nota, no una receta citada.

> [!NOTE] Sin fuente todavía: las frecuencias de cruce entre las tres bandas de un EQ de mixer de
> DJ. Ningún manual consultado las da, y cambian de un aparato a otro.

## Cuánto corta una perilla

Un EQ de mixer corta una cantidad fija de decibeles en su tope, y cada aparato tiene su cifra.
Las únicas cifras encontradas no son de manual:

- Un usuario del foro de un fabricante de mixers de cabina dice que en su mixer el modo EQ corta
  unos 26 dB y el modo isolator corta del todo ("EQ mode = -26dB cut. Isolator = infinite cut"),
  según su resumen ([foro](https://community.pioneerdj.com/hc/en-us/community/posts/22980396236697/comments/22989884666137)).
- Un programa de DJ indica de -24 dB a +6 dB para su EQ clásico, según su resumen
  ([manual](https://help.algoriddim.com/user-manual/djay-pro-mac/settings/sound)).

Las cifras discrepan entre aparatos. Lo que importa es saber si la perilla del mixer que se usa
deja un resto audible al fondo o apaga la banda.

## Kill e isolator

El kill es un corte total de una banda. El isolator, por la definición de convención del oficio
(sin fuente citable), es un modo de EQ en el que cada banda llega a cero, más drástico que un EQ
común. En un programa de DJ que ofrece seis modelos de EQ, uno solo es de tipo kill o isolator,
con pendiente de "24 db/octave"
([Native Instruments](https://support.native-instruments.com/support/solutions/articles/69000879507-traktor-pro-2-eq-and-filter-models)).

Con un EQ que deja resto, un swap de graves deja un poco del bajo saliente por debajo; con
isolator o kill, el grave de un tema desaparece y el cambio es más limpio y más brusco. Esta
comparación es inferencia de las cifras de corte, no de una fuente de práctica.

## Filtros

Un filtro pasa-altos (HPF, *high-pass filter*) deja pasar lo agudo y saca lo que está por
debajo de un punto; un pasa-bajos (LPF, *low-pass filter*), al revés. Senior usa el pasa-altos
alrededor de 100 Hz para que una sola parte de bajo domine
([Sound On Sound](https://www.soundonsound.com/techniques/mixing-bass)).

En el techno, según el resumen de una nota de MusicRadar, un DJ dice que el cambio se hace más con
filtro y resonancia que con acordes ([MusicRadar](https://musicradar.com/news/harmonic-mixing)).
Barrer un filtro mueve el punto de corte durante la transición; sobre su papel en la tensión, ver
[tensión](../Energia/tension-y-descarga.md).

> [!NOTE] Sin fuente todavía: cuándo conviene el filtro y cuándo el EQ en una transición larga de
> techno, con una fuente de práctica que lo diga.

## Errores probables

Tres errores que se deducen de lo anterior (inferencia, sin fuente de práctica que los liste):

- Cortar de más y no devolver: un tema queda sin graves después de la transición.
- Subir bandas para "mejorar" un tema: subir el LOW de un tema suma volumen y puede recortar
  (ver [ganancia y volumen percibido](ganancia-y-volumen-percibido.md)).
- Confundir el corte con el volumen: bajar el fader baja todas las bandas por igual; bajar el
  LOW saca solo el grave.

> [!NOTE] Sin fuente todavía: una ficha por aparato con su corte máximo y sus frecuencias de cruce,
> sacada de los manuales.
