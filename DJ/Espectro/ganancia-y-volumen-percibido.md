---
resumen: >-
  La ganancia fija el nivel con que cada tema entra al mixer, y el volumen percibido es cuán fuerte
  lo oye la gente, que no depende solo de ese nivel. Igualar la ganancia antes de mezclar evita que
  una transición suene mejor o peor solo por sonar más fuerte, y deja margen antes de recortar.
estado: vigente
estabilidad: estable
fuentes:
  - "Mixxx, manual 2.5, DJing With Mixxx (ganancia y medidores): https://manual.mixxx.org/2.5/en/chapters/djing_with_mixxx"
  - "Sound On Sound, Establishing project studio reference monitoring levels (resumen del buscador): https://www.soundonsound.com/techniques/establishing-project-studio-reference-monitoring-levels"
  - "Sound On Sound, Q. Should I gain-stage to -6dBFS or -18dBFS? (resumen del buscador): https://www.soundonsound.com/sound-advice/q-should-gain-stage-6dbfs-or-18dbfs"
  - "ISO 226:2003, Acoustics: Normal equal-loudness-level contours (registro ISO, resumen del buscador): https://www.iso.org/standard/34222.html"
  - "Wikipedia, Equal-loudness contour (resumen del buscador): https://en.wikipedia.org/wiki/Equal-loudness_contour"
  - "Microsoft, Louder Sounds Better, blog de audio (resumen del buscador): https://learn.microsoft.com/en-us/archive/blogs/audiofool/louder-sounds-better"
  - "Digital DJ Pool, DJ mistakes beginners make (resumen del buscador): https://digitaldjpool.com/blog/dj-mistakes-beginners-make/"
  - "Serato, Auto gain: what's all that about? (resumen del buscador): https://serato.com/latest/blog/15577/auto-gain-whats-all-that-about"
aliases: [Gain, Gain staging, Headroom, Clipping, Sonoridad, Loudness, Auto gain]
creado: 2026-11-27
revisado: 2026-11-27
---

# Ganancia y volumen percibido

La ganancia fija el nivel con que cada tema entra al mixer, y el volumen percibido es cuán fuerte
lo oye la gente, que no depende solo de ese nivel. Igualar la ganancia antes de mezclar evita que
una transición suene mejor o peor solo por sonar más fuerte, y deja margen antes de recortar.

## La cadena de niveles

La ganancia (*gain*) es el nivel de entrada del canal, y se ajusta para que los medidores queden
en verde (manual de Mixxx, capítulo 12). En estudio se llama *gain staging* a repartir los niveles
a lo largo de la cadena, un término de grabación y no de DJ.

El medidor del canal es la referencia. El manual de Mixxx pide que el nivel promedio quede cerca
del tope de la zona verde, sin entrar al amarillo, y advierte: "If a level meter is in its red
region, the signal is clipping and the gain should be turned down"
([Mixxx](https://manual.mixxx.org/2.5/en/chapters/djing_with_mixxx)). El clipping (recorte) pasa
cuando los picos de la onda se aplastan por exceso de señal.

## El margen que la transición necesita

El headroom (margen) es el nivel disponible por encima del promedio antes de que la señal recorte.
En digital no hay nada por encima de 0 dBFS: lo que pasa, se recorta. En estudio, Sound On Sound
recomienda trabajar con unos 20 dB de margen, según su resumen
([Sound On Sound](https://www.soundonsound.com/techniques/establishing-project-studio-reference-monitoring-levels)),
y otras notas de la misma revista discuten si el objetivo es -6 o -18 dBFS
([Sound On Sound](https://www.soundonsound.com/sound-advice/q-should-gain-stage-6dbfs-or-18dbfs)).
Es convención de estudio, sin acuerdo entre sus propias fuentes.

Esta nota infiere, desde la regla del medidor, que en la cabina el margen importa porque en la
transición suenan dos temas y la suma sube el nivel: si cada tema ya llega al tope solo, la suma
recorta. De ahí que convenga dejar lugar por debajo del rojo y repartir bandas con el
[swap de graves](swap-de-graves.md) en lugar de sumar dos temas enteros.

> [!NOTE] Sin fuente todavía: una cifra de margen recomendada para mixers de DJ, de una fuente de
> DJ y no de estudio.

## El oído no es plano

El volumen percibido (*sonoridad*, o *loudness*) no sigue al nivel por igual en todas las
frecuencias. Las curvas de igual sonoridad dicen qué nivel necesita cada frecuencia para
sonar igual de fuerte. Fletcher y Munson las midieron en 1933 con auriculares, y Robinson y Dadson
las volvieron a determinar en 1956, base de una norma ISO 226, según el resumen de
[Wikipedia](https://en.wikipedia.org/wiki/Equal-loudness_contour).

La norma ISO 226:2003 especifica, según su resumen, los niveles de tonos puros que oyentes juzgan
igual de fuertes, para oyentes otológicamente normales de 18 a 25 años, con escucha binaural y
fuente al frente ([ISO](https://www.iso.org/standard/34222.html)). La misma página la marca como
retirada (*withdrawn*); no se confirmó con qué edición se reemplazó.

Debajo de unos 100 Hz la sonoridad crece muy rápido con el nivel, y las diferencias entre estudios
en esa zona "remain unexplained", según el mismo resumen de Wikipedia. La consecuencia para el DJ
es inferencia: a volumen bajo, en casa o en auriculares, los graves se oyen menos que a volumen
de club.

## Más fuerte parece mejor

Entre dos versiones del mismo sonido, la más fuerte suele parecer mejor. Un blog de ingeniería de
audio lo explica porque al subir el nivel la respuesta del oído se acerca a una curva más plana, y
dice que "the louder one will often subjectively sound better regardless" de su calidad, según su
resumen ([Microsoft](https://learn.microsoft.com/en-us/archive/blogs/audiofool/louder-sounds-better)).

Aplicado a la mezcla, es inferencia de esta nota que un tema que entra más fuerte puede ganar la
comparación sin ser mejor. Las guías de principiantes tratan "más volumen = mejor" como error y lo
vinculan con el clipping y la fatiga del público, según su resumen
([Digital DJ Pool](https://digitaldjpool.com/blog/dj-mistakes-beginners-make/)). También castiga
al oído propio: ver [cuidado del oído](cuidado-del-oido.md).

> [!NOTE] Sin fuente todavía: un estudio de preferencia con oyentes humanos y música a nivel
> igualado. Lo citado es un blog técnico informal.

## Igualar antes de mezclar

Los pasos son de esta nota, armados con la regla del medidor de Mixxx; no vienen de una fuente de
DJ con números.

1. Con el tema entrante en auriculares, mirá su medidor de canal y llevá la ganancia hasta que su
   promedio coincida con el del tema que suena.
2. Confirmá de oído.
3. Durante la transición, mirá el medidor del master: si sube hacia el amarillo, bajá ganancia o
   sacá una banda, no subas más.

Los programas de DJ ofrecen auto gain, un valor por tema que ajusta la ganancia sola. Serato lo
describe como el valor "required to match the perceived loudness of the track to a reference
level", según su resumen ([Serato](https://serato.com/latest/blog/15577/auto-gain-whats-all-that-about)).
Para rekordbox no se encontró manual oficial, y un vendedor de un producto competidor afirma que
mide pico y no sonoridad, sin ser una fuente neutra. Sin resolver; conviene comprobarlo de oído.
