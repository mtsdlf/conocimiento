---
resumen: >-
  La tonalidad de un tema es su centro de notas, dicho como una nota y un modo (mayor o menor), y
  dos tonalidades son compatibles cuando sus notas conviven sin chocar. La rueda de compatibilidad
  numera las tonalidades para que las vecinas se encuentren contando, y mover el pitch sin key lock
  cambia la tonalidad.
estado: vigente
estabilidad: estable
fuentes:
  - "Mixed In Key, Harmonic Mixing Guide (fabricante): https://mixedinkey.com/harmonic-mixing-guide/"
  - "Phil Morse, How Important Is It For DJs To Mix In Key?, Digital DJ Tips (act. 2024-02-21): https://www.digitaldjtips.com/how-important-is-it-to-mix-in-key/"
  - "Produce Like A Pro, Camelot wheel (resumen del buscador): https://producelikeapro.com/blog/camelot-wheel/"
  - "DJ TechTools, Mixing in Key: When and How to Change Track Key in DJ Software, 2013-05-15: https://djtechtools.com/2013/05/15/mixing-in-key-when-and-how-to-change-track-key-in-dj-software/"
  - "Mixxx, manual 2.5, DJing With Mixxx (key lock): https://manual.mixxx.org/2.5/en/chapters/djing_with_mixxx"
  - "Kim et al., A Computational Analysis of Real-World DJ Mixes, ISMIR 2020: https://program.ismir2020.net/static/final_papers/352.pdf"
  - "Faraldo, Tonality Estimation in Electronic Dance Music, tesis doctoral UPF, 2017 (descripción): https://zenodo.org/records/1154586"
  - "Wolf y Wüst, Detection of Clash of Keys in a Non-Dichotomous Task, Jahrbuch Musikpsychologie 34, e225, 2026 (resumen): https://jbdgm.psychopen.eu/index.php/JBDGM/article/download/225/225.html?inline=1"
  - "Gebhardt, Davies y Seeber, Harmonic mixing based on roughness and pitch commonality, DAFx-15 (abstract): https://dafx.de/paper-archive/details/VVCYuTXWkEB3l4VKeUZ0-A"
aliases: [Tonalidad, Key, Tono, Rueda Camelot, Camelot, Open Key, Círculo de quintas, Key lock, Key shift]
creado: 2026-11-27
revisado: 2026-11-27
---

# Tonalidad y compatibilidad

La tonalidad de un tema es su centro de notas, dicho como una nota y un modo (mayor o menor), y
dos tonalidades son compatibles cuando sus notas conviven sin chocar. La rueda de compatibilidad
numera las tonalidades para que las vecinas se encuentren contando, y mover el pitch sin key lock
cambia la tonalidad.

## Nota y modo

Una tonalidad (*key*) se nombra con una nota, la que funciona como centro, y un modo: mayor o
menor. En un tema de electrónica, la sugieren sobre todo el bajo y lo que tenga melodía o
acordes (inferencia, sin fuente). La tesis de Faraldo critica ese modelo de dos modos como un
vocabulario centrado en la tonalidad clásica occidental que puede no servir para la música popular
([tesis, descripción](https://zenodo.org/records/1154586)): hay temas modales o ambiguos que no
son ni mayores ni menores.

> [!NOTE] Sin fuente todavía: la teoría de fondo (qué es un modo, el círculo de quintas, las
> tonalidades relativas) contrastada con un texto de teoría musical. Lo que sigue sale de fuentes
> de práctica de DJ.

## La rueda Camelot

La rueda Camelot traduce las 24 tonalidades a un reloj: un número del 1 al 12 y una letra. Se
apoya en el círculo de quintas: los números vecinos están a una quinta de distancia, y la
tonalidad mayor y su relativa menor (las que comparten notas) quedan en la misma hora, según el
resumen de [Produce Like A Pro](https://producelikeapro.com/blog/camelot-wheel/) y
[Digital DJ Tips](https://www.digitaldjtips.com/how-important-is-it-to-mix-in-key/).

Las reglas que da la empresa dueña de la rueda, que también vende un detector de tonalidad
([guía del fabricante](https://mixedinkey.com/harmonic-mixing-guide/)):

| Paso | Ejemplo | Según el fabricante |
|---|---|---|
| Misma tonalidad | 8A a 8A | Combina |
| Misma hora, otra letra (relativa) | 8A a 8B | Combina |
| Una hora arriba o abajo | 8A a 9A o 7A | Combina |
| Salto grande | 3A a 9A | "Curveball", riesgoso |

El fabricante lo resume como "as easy as counting up and down". Dice también que su sistema
"started the harmonic mixing movement in 2006"; es una afirmación comercial, sin fuente en la
página.

> [!NOTE] Sin fuente todavía: quién inventó la rueda Camelot (se atribuye a una persona, sin
> verificar) y una descripción primaria de Open Key, la otra notación de rueda que muestran
> algunos programas.

## Compatibilidad y consonancia

La rueda mide cercanía en el círculo de quintas. Según los trabajos de Gebhardt, no captura cómo
interactúan las alturas reales de dos temas: propusieron alinear temas por rugosidad y notas en
común, y según su abstract, en un test de escucha sus combinaciones más consonantes se prefirieron
a las de un sistema comercial basado en tonalidad
([DAFx-15](https://dafx.de/paper-archive/details/VVCYuTXWkEB3l4VKeUZ0-A)). El abstract no da el
número de participantes.

Que el choque se oye sí tiene apoyo. En un experimento en línea con 97 personas, acompañamientos un
tono entero por debajo se calificaron mucho menos armónicos que los ajustados, y la diferencia se
correlacionó con la capacidad perceptiva y los años de práctica, según su resumen
([Wolf y Wüst](https://jbdgm.psychopen.eu/index.php/JBDGM/article/download/225/225.html?inline=1)).
Es una melodía con acompañamiento, no dos temas de techno: el efecto existe, pero cuánto pesa en
una transición de percusión es otra pregunta (ver [armonía](armonia.md)).

## Mover el pitch mueve la tonalidad

Sin key lock, mover el pitch cambia el tono y el tempo juntos. Con key lock (en algunos equipos,
*master tempo*) la altura queda fija mientras cambia el tempo
([DJ TechTools](https://djtechtools.com/2013/05/15/mixing-in-key-when-and-how-to-change-track-key-in-dj-software/)).
El manual de Mixxx avisa que el sync puede producir un cambio de tono notable, y que el key lock lo
reduce ([Mixxx](https://manual.mixxx.org/2.5/en/chapters/djing_with_mixxx)). El ajuste de tempo
está en [tempo y fase](../Tiempo/tempo-y-fase.md) y el key lock como función, en
[sync y beatgrid](../Tiempo/sync-y-beatgrid.md).

Cuánto pitch es un semitono: según Morse, en Digital DJ Tips, cada 6 % de cambio de tempo mueve la
tonalidad cerca de un semitono (ver [tempo y fase](../Tiempo/tempo-y-fase.md#mover-el-tempo-mueve-el-tono)).
El cálculo da lo mismo: un semitono es un factor de 2^(1/12) ≈ 1,0595 en la frecuencia, o sea un
cambio de pitch de cerca de 5,95 %. En mezclas reales, el 86,1 % de los temas se tocó con menos de
5 % de cambio de tempo ([Kim et al., ISMIR 2020](https://program.ismir2020.net/static/final_papers/352.pdf));
por el cálculo anterior, eso es menos de un semitono, aun sin key lock. En música tonal un desvío
de menos de un semitono también desafina, porque deja al tema entre dos tonalidades; esto último
es inferencia, sin fuente.

## Cambiar la tonalidad a propósito

Traktor y Virtual DJ tienen key shift, que transpone de a un semitono por pulsación
([DJ TechTools](https://djtechtools.com/2013/05/15/mixing-in-key-when-and-how-to-change-track-key-in-dj-software/)).
La misma fuente advierte que cambiar la tonalidad más de dos semitonos empieza a degradar el audio;
es una sola fuente secundaria de 2013. Según Pioneer, la CDJ-3000 suma key sync y key shift.
Digital DJ Tips agrega que los botones de key sync pueden mover la tonalidad tanto que el tema
suena "ridiculous"
([Digital DJ Tips](https://www.digitaldjtips.com/how-important-is-it-to-mix-in-key/)).

Kim y otros encontraron que solo el 2,5 % de los temas de las mezclas estudiadas se transpuso, y
casi todos un semitono ([Kim et al.](https://program.ismir2020.net/static/final_papers/352.pdf)).

## Dónde leer más

Para las reglas de la rueda, leé la
[guía de mezcla armónica del fabricante de la rueda](https://mixedinkey.com/harmonic-mixing-guide/),
sabiendo que vende un detector: fijate en la tabla de pasos compatibles y descontá las afirmaciones de
exactitud. Para saber cuándo la tonalidad automática no alcanza, la
[tesis de Faraldo](https://zenodo.org/records/1154586), en el capítulo sobre el vocabulario de
tonalidades: fijate por qué el binario mayor/menor falla en música electrónica.
