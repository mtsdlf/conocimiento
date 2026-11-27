---
resumen: >-
  El beatgrid es la grilla de pulsos que el programa le pone a un tema al analizarlo, y el sync
  usa esa grilla para igualar tempos (y, con quantize, la fase). Funciona tan bien como el
  análisis, no resuelve las frases, y su lugar en el oficio se discute más por valores que por
  datos.
estado: borrador
estabilidad: semi
fuentes:
  - "Mixxx, manual 2.4, DJing With Mixxx: https://manual.mixxx.org/2.4/chapters/djing_with_mixxx"
  - "Phil Morse, Beginners' Guide To Keylocking, Digital DJ Tips (2018): https://www.digitaldjtips.com/keylocking-dj-beginners/"
  - "DJ Vintage, Is Sync Really So Different To Beatmatching?, Digital DJ Tips (2018): https://www.digitaldjtips.com/your-questions-is-sync-really-so-different-to-beatmatching/"
  - "Yemi Abiade, Should DJs be using the sync button?, Mixcloud (2026): https://www.mixcloud.com/blog/2026/03/25/should-djs-be-using-the-sync-button"
  - "DJ Craze, Sync is your friend, Mixmag (2019): https://mixmag.net/read/dj-craze-sync-is-your-friend-embrace-news"
  - "Kristan Caryl, What makes a great DJ, Attack Magazine (2015): https://www.attackmagazine.com/features/long-read/what-makes-a-great-dj/"
  - "Kim, Choi, Sacks, Yang y Nam, ISMIR 2020: https://arxiv.org/abs/2008.10267"
  - "DJ/.investigacion/tiempo-y-forma.md"
  - "DJ/.investigacion/posicion-contraria.md"
aliases: [Sync, Beatgrid, Beat grid, Quantize, Key lock, Master tempo, Grilla de pulsos]
creado: 2026-11-27
revisado:
---

# Sync y beatgrid

El beatgrid es la grilla de pulsos que el programa le pone a un tema al analizarlo, y el sync
usa esa grilla para igualar tempos (y, con quantize, la fase). Funciona tan bien como el
análisis, no resuelve las frases, y su lugar en el oficio se discute más por valores que por
datos.

## La grilla: pulsos y un "1"

El beatgrid es una marca en cada pulso del tema más una marca distinta en el primero de cada
compás, el "1". Sale de analizar el audio. Dependen de ella el sync, el quantize y los cues que
se ajustan solos.

Según un resumen de Mixxx que el informe no verificó, el análisis suele acertar el BPM y fallar
en dónde cae el primer pulso
([Mixxx](https://manual.mixxx.org/2.4/chapters/djing_with_mixxx)). Los programas permiten
estirar, comprimir y mover la grilla a mano. Si el "1" está mal puesto, la fase puede coincidir y
la mezcla caer igual fuera de compás: ahí Tiempo y [frase](../Forma/frase.md) no se separan.

## Sync, quantize y key lock

| Función | Qué hace | Qué no hace |
|---|---|---|
| Sync | Iguala el tempo de un tema al de otro | Según el programa, no garantiza la fase |
| Quantize | Hace que los cues, los loops y los arranques caigan en el pulso más cercano de la grilla | Depende de la grilla |
| Key lock | Mantiene la altura de las notas cuando cambia el tempo | No es gratis: degrada el sonido |

La diferencia entre sync y quantize es la que más confunde. En Mixxx, el sync "usually only makes
sure the rate sliders are set correctly", y la fase la asegura el quantize: "Quantize will ensure
that the beats are perfectly lined up as well"
([Mixxx](https://manual.mixxx.org/2.4/chapters/djing_with_mixxx)). El sync de tempo y el de fase
son cosas distintas y varían según el programa; cómo lo resuelven dos programas concretos está en
la [ficha de sync en reproductores](ficha-sync-en-reproductores.md).

El sync también reconoce tempos dobles o mitades, por ejemplo 140 con 70 (Mixxx). Sirve con
temas de percusión a media velocidad.

## Cuándo falla el sync

El sync "requires an accurately detected BPM value and a correct beat grid for both tracks"
([Mixxx](https://manual.mixxx.org/2.4/chapters/djing_with_mixxx)). Las fuentes dan cuatro casos:

1. Grilla mal puesta. Según el resumen de Mixxx, el análisis suele fallar en el primer pulso.
2. Tempo variable. Un tema grabado sin grilla constante no entra en una sola línea de pulsos.
   Cuando el programa sigue a un tema "líder" que cambia de tempo, el que lo sigue cambia
   también, lo que "may result in a notable pitch change"; el key lock lo reduce (Mixxx).
3. Correcciones perdidas. rekordbox sobrescribe la grilla corregida a mano si el tema se vuelve
   a analizar; ver la [ficha](ficha-sync-en-reproductores.md).
4. Frase equivocada. El sync alinea pulsos, no frases: dos temas sincronizados pueden estar
   en lugares distintos de su estructura. Eso se resuelve en
   [puntos de entrada y salida](../Forma/puntos-de-entrada-y-salida.md).

> [!IMPORTANT]
> Disputado: cuánto acierta el análisis. DJ Vintage dice que los programas logran "between 65%
> and 80% accurate beatgrids" y que Traktor y rekordbox son pobres con BPM variable
> ([Digital DJ Tips](https://www.digitaldjtips.com/your-questions-is-sync-really-so-different-to-beatmatching/)),
> sin decir cómo lo midió. Según el resumen de Mixxx, lo que suele fallar es el primer pulso, no
> el BPM. No son incompatibles, pero miden cosas distintas, y ninguna es una medición
> independiente.

## El key lock y lo que cuesta

Sin key lock, cambiar el tempo cambia el tono, más o menos un semitono cada 6 % (ver
[tempo y fase](tempo-y-fase.md#mover-el-tempo-mueve-el-tono)). Con key lock, "changing the speed
of a track won't affect the key" (Mixxx). El precio es la calidad: según Morse, "can degrade the
sound quality", más cuanto más lejos del tempo original y cuanto más complejo el material
([Digital DJ Tips](https://www.digitaldjtips.com/keylocking-dj-beginners/)). El informe de
investigación infiere que en techno, cuando el bombo suena solo, un artefacto en el bombo se
oye; no es un dato medido.

> [!IMPORTANT]
> Disputado: hasta dónde se puede estirar con key lock. Morse recomienda "no more than + or – 6%".
> Según el resumen de una comparación de DJ TechTools de 2014, los cortes y artefactos aparecen
> sobre todo fuera de un 5 % del BPM original. Ninguna de las dos es una medición independiente.

Kim y otros infieren que los DJ dejan el key lock encendido, porque solo el 2,5 % de los temas
de sus mezclas estaba transpuesto y de esos el 94,3 % un semitono
([ISMIR 2020](https://arxiv.org/abs/2008.10267)). El corpus es sobre todo de house y trance. Qué
pasa con la tonalidad al mezclar está en
[tonalidad y compatibilidad](../Armonia/tonalidad-y-compatibilidad.md).

## El debate del sync

Hay dos posiciones, y las dos vienen de practicantes; no hay estudio que mida nada.

A favor. El sync libera atención para la selección, las capas y los efectos, y baja la barrera
de entrada para quien empieza, que puede atender primero frases y energía
([Mixcloud](https://www.mixcloud.com/blog/2026/03/25/should-djs-be-using-the-sync-button)). DJ
Vintage lo compara con un carpintero que usa taladro eléctrico. DJ Craze pide dejar de
rechazarlo porque libera tiempo para lo creativo
([Mixmag](https://mixmag.net/read/dj-craze-sync-is-your-friend-embrace-news)).

En contra. Usarlo de más "can also limit your development and connection to the music"
(Mixcloud). Quien solo sabe sincronizar con el botón queda en problemas cuando falla o cuando el
equipo no lo tiene. Según Mixmag, "many DJs and electronic artists consider sync harmful to the
art form", y los ravers de la vieja escuela lo ven como fidelidad a la cultura: una discusión de
valores, no un argumento técnico.

Dónde convergen. Las fuentes de practicantes coinciden en aprender a oído primero y usar el
sync después como herramienta. Craze dice "If you can't beat match you shouldn't DJ", y a la vez
llama al sync su amigo. Spencer Parker agrega que mezclar con mixer rotativo y bandejas
flotantes es más difícil que sincronizar en software, "just a fact", y que prefiere buena música
con mezclas algo corridas
([Attack](https://www.attackmagazine.com/features/long-read/what-makes-a-great-dj/)).

> [!IMPORTANT]
> Disputado: si el beatmatching a oído es "la base" del oficio. Se sostiene que aprenderlo sirve.
> No se sostiene que sea lo que hace buena una mezcla: los mismos practicantes lo ponen por debajo
> de la [selección](../Seleccion/seleccion.md). El dato de Kim y otros (86,1 % de los temas con
> menos de 5 % de cambio de tempo) no decide nada, porque no distingue oído de sync.

La práctica a oído está en [beatmatching a oído](beatmatching-a-oido.md); las escuelas que
defienden cada postura, en [escuelas de mezcla](../Fundamentos/escuelas-de-mezcla.md).

## Para leer en el manual

En el capítulo "DJing With Mixxx" ([manual 2.4](https://manual.mixxx.org/2.4/chapters/djing_with_mixxx)),
conviene leer la parte de Sync Lock y Quantize y fijarse en que el sync de tempo no asegura la
fase, y en cómo se corrige una grilla a mano.
