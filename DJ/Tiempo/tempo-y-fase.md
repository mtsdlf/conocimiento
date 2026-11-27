---
resumen: >-
  El tempo es la velocidad de un tema en pulsos por minuto (BPM) y la fase es si sus pulsos caen
  en el mismo instante que los de otro tema. Sincronizar es igualar las dos cosas y sostenerlas
  contra la deriva; al corregir, primero se alinea la fase y después el tempo.
estado: borrador
estabilidad: estable
fuentes:
  - "Mixxx, manual 2.4, DJing With Mixxx: https://manual.mixxx.org/2.4/chapters/djing_with_mixxx"
  - "Chris Cartledge, Learn To Beatmatch, Digital DJ Tips (2018): https://www.digitaldjtips.com/learn-to-beatmatch/"
  - "Phil Morse, Beginners' Guide To Keylocking, Digital DJ Tips (2018): https://www.digitaldjtips.com/keylocking-dj-beginners/"
  - "Yemi Abiade, Should DJs be using the sync button?, Mixcloud (2026): https://www.mixcloud.com/blog/2026/03/25/should-djs-be-using-the-sync-button"
  - "Kim, Choi, Sacks, Yang y Nam, ISMIR 2020: https://arxiv.org/abs/2008.10267"
  - "Mark J. Butler, Turning the Beat Around, Music Theory Online 7.6 (2001): https://mtosmt.org/issues/mto.01.7.6/mto.01.7.6.butler.php"
  - "DJ/.investigacion/tiempo-y-forma.md"
aliases: [Tempo, BPM, Fase, Deriva, Pitch, Pulso, Beat]
creado: 2026-11-27
revisado:
---

# Tempo y fase

El tempo es la velocidad de un tema en pulsos por minuto (BPM) y la fase es si sus pulsos caen
en el mismo instante que los de otro tema. Sincronizar es igualar las dos cosas y sostenerlas
contra la deriva; al corregir, primero se alinea la fase y después el tempo.

## El pulso y el BPM

El pulso (en inglés, *beat*) es la unidad que cuenta el BPM. Butler explica que en la música
electrónica de baile el bombo "tends to function as a source of metrical stability", por ser el
sonido más grave y resonante
([Butler 2001](https://mtosmt.org/issues/mto.01.7.6/mto.01.7.6.butler.php)). El informe de
investigación lo toma como la base teórica de por qué se sincroniza con el bombo. Cómo se agrupan
los pulsos en compases y frases es asunto de [Forma](../Forma/frase.md).

El tempo se mide en BPM. El reproductor lo cambia con un control de velocidad graduado en
porcentaje (el *pitch*), y el cambio es proporcional al tempo de partida, no un paso fijo. La
cuenta, que el informe de investigación hace como cálculo propio, es BPM final = BPM × (1 + %/100):
un tema de 128 BPM a +6 % queda en 135,68, y a −4 % en 122,88. Pasar de 128 a 126 BPM es bajar
1,56 %.

## La fase y cómo suena cuando falla

Igualar el tempo no alcanza: dos temas a 128 BPM exactos pueden tener los bombos corridos. El
manual de Mixxx define el beatmatching como ajustar la velocidad de un tema "so that it matches
the tempo of another track" y suma la fase como segundo paso
([Mixxx](https://manual.mixxx.org/2.4/chapters/djing_with_mixxx)). El tempo se iguala con el
control de velocidad; la fase, empujando o frenando un momento el tema (el *nudge*, con el jog o
los botones de pitch bend). El desfase se oye como un bombo doblado, el *flam*.

## Primero la fase, después el tempo

Cuando dos temas se separan, la corrección tiene dos movimientos y un orden. Primero se empuja o
frena para volver a alinear los bombos; después se mueve el control de velocidad para que no se
vuelvan a separar. Cartledge insiste en el orden: "Always remember that when adjusting you
always need to make these two steps, and in that order"
([Digital DJ Tips](https://www.digitaldjtips.com/learn-to-beatmatch/)). Según el informe, esa
regla separa lo que quien empieza suele mezclar en un solo gesto. La práctica de esto está en
[beatmatching a oído](beatmatching-a-oido.md).

## La deriva y de dónde sale

La deriva es la separación lenta de dos temas que parecían sincronizados. Según Cartledge se
nota sutil al principio y crece cada compás; la música electrónica en 4/4 es la más fácil de
igualar, y una banda en vivo deriva porque su tempo oscila.

Tres cosas la producen:

1. Una diferencia de tempo que no se ve. El informe de investigación calcula que entre 128,00
   y 127,98 BPM cada pulso difiere unos 73 microsegundos, y que en 512 pulsos (unos cuatro
   minutos) se acumulan unos 37 milisegundos, audibles como flam. Con 0,5 BPM de diferencia, los
   temas se corren un pulso entero cada dos minutos, siempre según ese cálculo.
2. Un tempo detectado que no es el de producción. El BPM que muestra la máquina sale de un
   análisis, y según usuarios de foros puede tener decimales que la pantalla no muestra.
3. Temas de tempo variable. Un vinilo viejo o una grabación en vivo no entran en una grilla
   constante: "Tracks can drift"
   ([Mixcloud](https://www.mixcloud.com/blog/2026/03/25/should-djs-be-using-the-sync-button)).

> [!NOTE] Sin fuente todavía: un estudio sobre el umbral de deriva audible entre dos bombos (en
> milisegundos) y una fuente oficial sobre cuántos decimales usa y muestra cada reproductor. Lo
> del redondeo de pantalla viene solo de foros de usuarios.

## Cuánto se mueve el tempo en una mezcla real

Poco. Kim y otros alinearon 1557 mezclas reales, con 20.765 transiciones y un promedio de 60,5
minutos, y midieron el cambio de tempo de cada tema: el 86,1 % se tocó con menos de 5 %, el
94,5 % con menos de 10 % y el 98,6 % con menos de 20 %
([ISMIR 2020](https://arxiv.org/abs/2008.10267)). Un pitch grande es la excepción, y lo normal
es mezclar temas de tempo parecido.

El dato tiene dos límites. El corpus, dicen los autores, "mostly focuses on House and Trance", y
el método de alineación "does not work well" con techno de mucho tambor y ambiente. Además, el
estudio no distingue si el ajuste se hizo a oído o con sync.

## Mover el tempo mueve el tono

Acelerar un tema sube la altura de sus notas. Morse da la equivalencia: "Every 6% change in a
track's tempo shifts its key by about one semitone"
([Digital DJ Tips](https://www.digitaldjtips.com/keylocking-dj-beginners/)); la cuenta exacta,
que el informe hace como cálculo propio, da 5,95 %. Eso importa cuando el tema tiene material
tonal, y se resuelve con el key lock, que tiene sus costos (ver
[sync y beatgrid](sync-y-beatgrid.md#el-key-lock-y-lo-que-cuesta)). Qué tonalidades conviven está
en [tonalidad y compatibilidad](../Armonia/tonalidad-y-compatibilidad.md).

## Para leer en el manual

El capítulo "DJing With Mixxx" del manual de Mixxx
([manual 2.4](https://manual.mixxx.org/2.4/chapters/djing_with_mixxx)) es abierto y no depende
de una marca de equipo. Conviene leer la sección de beatmatching y fijarse en que trata tempo y
fase como dos problemas, y en que igualar el tempo no garantiza la fase.
