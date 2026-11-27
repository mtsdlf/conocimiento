---
resumen: >-
  El tiempo es la dimensión en que dos temas se ponen a la misma velocidad y con los pulsos
  cayendo juntos. Se resuelve en dos pasos, tempo y fase, a oído o con la máquina, y hay que
  mantenerlo mientras dura la transición porque los pulsos derivan.
estado: vigente
estabilidad: estable
fuentes:
  - "Mixxx, manual 2.4, DJing With Mixxx: https://manual.mixxx.org/2.4/chapters/djing_with_mixxx"
  - "Kim, Choi, Sacks, Yang y Nam, A Computational Analysis of Real-World DJ Mixes using Mix-To-Track Subsequence Alignment, ISMIR 2020: https://arxiv.org/abs/2008.10267"
  - "Chris Cartledge, Learn To Beatmatch, Digital DJ Tips (2018): https://www.digitaldjtips.com/learn-to-beatmatch/"
  - "DJ/.investigacion/tiempo-y-forma.md"
  - "DJ/.investigacion/posicion-contraria.md"
aliases: [Sincronía, Beatmatching, Tempo]
creado: 2026-11-27
revisado: 2026-11-27
---

# Tiempo

El tiempo es la dimensión en que dos temas se ponen a la misma velocidad y con los pulsos
cayendo juntos. Se resuelve en dos pasos, tempo y fase, a oído o con la máquina, y hay que
mantenerlo mientras dura la transición porque los pulsos derivan.

Es la primera de las cinco dimensiones de la [transición](../dj.md#la-transición-cruza-las-cinco-dimensiones)
y la base de las demás: sin pulsos juntos no hay frase que contar en [Forma](../Forma/forma.md).
Tocar el tempo también mueve la altura de las notas, y eso conecta con la
[Armonía](../Armonia/armonia.md). Con los dos temas ya juntos, el [Espectro](../Espectro/espectro.md)
reparte el grave.

## Tempo y fase son dos problemas

Sincronizar dos temas son dos ajustes distintos. El tempo es la velocidad, en pulsos por minuto
(BPM), y se iguala con el control de velocidad del reproductor. La fase es que los pulsos de los
dos temas caigan en el mismo instante, y se corrige empujando o frenando un momento uno de los
temas. El manual de Mixxx los separa así y describe el error de fase como un bombo "doblado" (en
inglés, *flam*) ([Mixxx](https://manual.mixxx.org/2.4/chapters/djing_with_mixxx)). Los detalles,
con las cuentas de porcentaje a BPM, están en [tempo y fase](tempo-y-fase.md).

Las correcciones van en un orden fijo: primero se alinea la fase y después se retoca el tempo
para que no vuelva a irse. Cartledge lo dice como regla: "Always remember that when adjusting
you always need to make these two steps, and in that order"
([Digital DJ Tips](https://www.digitaldjtips.com/learn-to-beatmatch/)).

## Por qué el tiempo hay que sostenerlo

Dos temas igualados no quedan igualados: una diferencia de tempo mínima se acumula pulso a
pulso hasta que se oye. Según Cartledge, la deriva se nota sutil al principio y crece cada
compás. El informe de investigación infiere que en una mezcla larga de techno eso obliga a
retocar cada tanto, también con sync. Las causas de la deriva están en
[tempo y fase](tempo-y-fase.md#la-deriva-y-de-dónde-sale).

En la práctica se corrige poco. Kim y otros midieron 1557 mezclas reales y encontraron que el
86,1 % de los temas se tocó con menos de 5 % de cambio de tempo
([ISMIR 2020](https://arxiv.org/abs/2008.10267)); el corpus es sobre todo de house y trance.

## Oído y máquina

Hay dos maneras de resolver el tiempo. A oído, quien pincha escucha los dos temas y corrige con
las manos; es lo que se practica en [beatmatching a oído](beatmatching-a-oido.md). Con la
máquina, el programa analiza cada tema, le pone una grilla de pulsos y empareja los tempos con
el botón de sync; cómo funciona y cuándo falla está en [sync y beatgrid](sync-y-beatgrid.md).

La discusión entre las dos es de valores más que de hechos. Los practicantes leídos coinciden en
que aprender a oído sirve, sobre todo para cuando la máquina falla, pero no en que sea "la base"
de una buena mezcla: varios lo ponen por debajo de la [selección](../Seleccion/seleccion.md).
Las posiciones, con sus citas, están en
[sync y beatgrid](sync-y-beatgrid.md#el-debate-del-sync). La historia de cómo llegó el sync al
oficio va en [Fundamentos](../Fundamentos/historia-del-dj.md).

## Dónde se tocan Tiempo y Forma

El "1" de cada compás, el pulso fuerte, es la frontera entre las dos verticales. La grilla de la
máquina marca pulsos y además cuál es el primero de cada compás. Si ese "1" está mal puesto, la
fase puede coincidir y la mezcla igual cae fuera de compás. Por eso igualar la fase no alcanza:
falta que los dos temas estén en el mismo lugar de su [frase](../Forma/frase.md), y el sync no
resuelve eso.

## Qué hay adentro de Tiempo

- [Tempo y fase](tempo-y-fase.md): pulso, BPM, porcentaje de velocidad, fase y deriva; los dos
  problemas de sincronizar y cuánto se mueve el tempo en la práctica.
- [Beatmatching a oído](beatmatching-a-oido.md): cómo se iguala a oído y una rutina para
  practicarlo.
- [Sync y beatgrid](sync-y-beatgrid.md): la grilla, el sync, el quantize y el key lock; cuándo
  fallan y el debate entre oído y máquina.
- [Sync en reproductores](ficha-sync-en-reproductores.md): ficha fechada de cómo lo resuelven
  dos programas concretos (2026-11).
