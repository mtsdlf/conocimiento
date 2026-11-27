---
resumen: >-
  Los puntos de entrada y salida son los momentos de un tema en que empieza y termina su
  transición con otro. La práctica habitual los pone en comienzos de frase, de modo que las
  frases de los dos temas queden alineadas, aunque la regla se rompe a propósito.
estado: vigente
estabilidad: semi
fuentes:
  - "Kim, Choi, Sacks, Yang y Nam, A Computational Analysis of Real-World DJ Mixes using Mix-To-Track Subsequence Alignment, ISMIR 2020: https://program.ismir2020.net/static/final_papers/352.pdf"
  - "Kim et al. 2020, versión HTML: https://ar5iv.labs.arxiv.org/html/2008.10267"
  - "Zehren, Alunno y Bientinesi, Automatic Detection of Cue Points for DJ Mixing (2020), solo el resumen: https://arxiv.org/abs/2007.08411"
  - "Mixmag, Does a DJ set have to be perfect? (2017): https://mixmag.net/feature/does-a-dj-set-have-to-be-perfect/2"
  - "Brejcha, Pioneer DJ blog: https://blog.pioneerdj.com/?p=4768"
  - "Mark J. Butler, Turning the Beat Around, Music Theory Online 7.6 (2001): https://mtosmt.org/issues/mto.01.7.6/mto.01.7.6.butler.php"
  - "Mixed In Key, Control the Energy Level of Your DJ Sets, solo el resumen: https://mixedinkey.com/Book/Control-The-Energy-Level-Of-Your-DJ-Sets"
  - "DJ/.investigacion/tiempo-y-forma.md"
  - "DJ/.investigacion/posicion-contraria.md"
aliases: [Cue in, Cue out, Phrase mixing, Mezcla por frases, Alinear frases, Punto de mezcla]
creado: 2026-11-27
revisado: 2026-11-27
---

# Puntos de entrada y salida

Los puntos de entrada y salida son los momentos de un tema en que empieza y termina su
transición con otro. La práctica habitual los pone en comienzos de frase, de modo que las
frases de los dos temas queden alineadas, aunque la regla se rompe a propósito.

## Tres momentos de una transición

Kim y otros, que midieron mezclas reales, definen tres puntos
([ISMIR 2020](https://program.ismir2020.net/static/final_papers/352.pdf)):

- Cue-out: "a timestamp that the previous track starts fading out and the next track starts
  fading in". Es donde empieza la transición.
- Cue-in: cuando el tema anterior terminó de salir. Es donde termina.
- Cue-mid: el medio de la región de transición.

Entre el cue-out y el cue-in suenan los dos temas a la vez. Es el tramo donde se resuelven las
otras dimensiones: el [swap de graves](../Espectro/swap-de-graves.md), la convivencia de
[tonalidades](../Armonia/tonalidad-y-compatibilidad.md) y el rumbo de la
[energía](../Energia/energia.md).

## Alinear frases

Alinear es arrancar el tema nuevo para que el compás 1 de una de sus [frases](frase.md) caiga
con el compás 1 de una frase del que suena. Los pasos combinan el cue en un comienzo de frase
(Cartledge), el cambio de grave en un límite de frase (guías de bass swap) y la regla de Mixed In
Key; el orden y los detalles son de esta nota, sin fuente medida.

1. Contá las frases del tema que suena y ubicá cuándo empieza la próxima.
2. En el tema nuevo, poné el cue en el primer pulso de la frase por donde querés entrar.
3. Sincronizá tempo y fase en los auriculares (ver [tempo y fase](../Tiempo/tempo-y-fase.md)).
4. Soltá el tema nuevo en el "1" de la frase que empieza.
5. Decidí cuántas frases dura la transición y hacé cada cambio (el grave, un filtro, el volumen)
   en un comienzo de frase.
6. Sacá el tema anterior al final de una frase, idealmente cuando entra su salida.

Con quantize, la máquina ajusta el cue al pulso más cercano de la grilla, y eso depende de que la
grilla esté bien puesta (ver [sync y beatgrid](../Tiempo/sync-y-beatgrid.md#la-grilla-pulsos-y-un-1)).
Según el resumen de una nota de Mixed In Key, lo más básico es mezclar la intro de un tema
sobre la salida del otro; qué es cada una está en [secciones de un tema](secciones-de-un-tema.md).

## Lo que muestran las mezclas reales

Kim y otros alinearon 1557 mezclas reales, con 13.728 temas y 20.765 transiciones, contra los
temas originales ([ISMIR 2020](https://program.ismir2020.net/static/final_papers/352.pdf)). Dos
resultados importan acá:

- Los largos de transición forman picos cada 32 pulsos, que los autores leen como "a phrase in
  the context of dance music": los DJs "consider the repetitive structures". Los cue-out muestran
  picos cada 32 pulsos más claros que los cue-in.
- Cuando DJs distintos mezclan el mismo tema, solo el 23,6 % de los pares de puntos coincide
  exacto. El 40,4 % cae dentro de un compás (4 pulsos), el 73,6 % dentro de 8 compases y el
  86,2 % dentro de 16. El estudio lo lee como reglas compartidas. Según el informe de posición
  contraria, los mismos datos muestran que uno de cada cuatro pares queda a más de 8 compases y
  que la elección de punto es creativa, no única.

El estudio tiene límites declarados. El corpus "mostly focuses on House and Trance", con un
tempo medio de 127 BPM, y los autores dicen que su alineación "does not work well" con techno de
mucho tambor y ambiente. No da la duración de las transiciones en segundos, solo en pulsos. Y
mostrar picos no es mostrar que todas las transiciones estén alineadas.

> [!IMPORTANT]
> Disputado: qué estilos cubre el corpus. El informe de Tiempo y Forma lee en el paper que es
> sobre todo house y trance; el informe de posición contraria, por el tempo medio de 127 BPM,
> lo describe como mayormente house y techno de pista. Lo que dicen los autores es lo primero, y
> la advertencia sobre techno es suya.

Para leer el paper, conviene ir a la sección de análisis de cue points y largo de transición
([versión HTML](https://ar5iv.labs.arxiv.org/html/2008.10267)): fijarse en los picos cada 32
pulsos, en las definiciones de cue-in, cue-mid y cue-out y en la advertencia sobre techno. Es la
única evidencia empírica de mezclas reales sobre este punto.

## Cuándo se rompe la regla

Alinear frases es lo habitual, no una condición de una buena transición. Ninguna fuente leída
mide si una transición desalineada le suena peor al público.

Algunos DJs eligen la aspereza. En Mixmag, Antal dice: "If a DJ made two trainwrecks in a night,
people would talk about it. But now I think I don't care so much", y que una mezcla áspera "can
say a lot about what kind of decisions I'm making"
([Mixmag](https://mixmag.net/feature/does-a-dj-set-have-to-be-perfect/2)). El mismo artículo
cuenta, como dato del autor, que David Mancuso pasaba los discos enteros sin mezclar.

El largo también se elige. Brejcha, que hace techno melódico, corta en seco el grave entrante
cuando busca impacto; con temas melódicos prefiere transiciones lentas, y mantiene el tema
entrante en loop uno o dos minutos antes de subirlo
([Pioneer DJ](https://blog.pioneerdj.com/?p=4768)). La transición larga en capas es una elección
y no una regla del techno; las dos maneras se comparan en
[escuelas de mezcla](../Fundamentos/escuelas-de-mezcla.md).

Y hay temas que no se dejan alinear. Butler documenta la disonancia métrica y la
reinterpretación del compás como recursos del productor
([Butler 2001](https://mtosmt.org/issues/mto.01.7.6/mto.01.7.6.butler.php)): temas que desplazan
el "1" o entran con un patrón que parece fuera de compás.

> [!IMPORTANT]
> Disputado: si alinear frases es necesario. Se sostiene como regularidad estadística de los DJs
> de baile (picos cada 32, 64 y 128 pulsos en los datos de Kim). No se sostiene como condición
> necesaria: no hay datos de percepción, y los mismos datos muestran gran dispersión entre DJs.

Según su resumen, Zehren y otros generaron puntos de cue con reglas sacadas de entrevistas a DJs
profesionales, y el 96 % se juzgó bueno para una mezcla
([arXiv](https://arxiv.org/abs/2007.08411)); no se leyó el paper entero.

> [!NOTE] Sin fuente todavía: estudios de percepción del público sobre frases desalineadas, y
> testimonios de DJs de techno sobre fraseo irregular (el foro de DJ TechTools sobre fraseo en
> techno no se pudo leer).
