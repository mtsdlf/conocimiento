---
resumen: >-
  El swap de graves es pasar el bajo de un tema al otro con el EQ, de modo que en la transición
  suene un solo grave por vez. Es la regla de espectro que repiten las guías de práctica, y según
  ellas se hace en un límite de frase.
estado: vigente
estabilidad: semi
fuentes:
  - "Mike Senior, Mixing Bass, Sound On Sound, sept. 2012: https://www.soundonsound.com/techniques/mixing-bass"
  - "Digital DJ Pool, DJ EQ mixing for beginners (resumen del buscador): https://digitaldjpool.com/blog/dj-eq-mixing-for-beginners/"
  - "Digital DJ Tips, Why Your DJ Mixes Sound Muddy (resumen del buscador): https://www.digitaldjtips.com/?p=2799689"
  - "Ryan Keeling, entrevista a Boris Brejcha, Pioneer DJ Blog: https://blog.pioneerdj.com/?p=4768"
  - "Hilo de KVR Audio sobre phasing en graves (foro, resumen del buscador): https://www.kvraudio.com/forum/viewtopic.php?p=8908635"
  - "Kim et al., A Computational Analysis of Real-World DJ Mixes, ISMIR 2020: https://program.ismir2020.net/static/final_papers/352.pdf"
aliases: [Bass swap, Cambio de graves, Un solo bajo por vez]
creado: 2026-11-27
revisado: 2026-11-27
---

# Swap de graves

El swap de graves es pasar el bajo de un tema al otro con el EQ, de modo que en la transición
suene un solo grave por vez. Es la regla de espectro que repiten las guías de práctica, y según
ellas se hace en un límite de frase.

## Un solo dueño para el grave

La regla se apoya en el [enmascaramiento](enmascaramiento.md), aunque ninguna fuente mide el caso
de dos temas de DJ. La práctica de estudio dice algo parecido. Mike Senior, con varias partes de
bajo en una mezcla, "would usually choose only one as the main low-end source, and high-pass
filter the others around 100Hz"
([Sound On Sound](https://www.soundonsound.com/techniques/mixing-bass)). En la cabina, la perilla
de graves (LOW) del [ecualizador](ecualizador-y-filtros.md) cumple un papel parecido y se mueve
durante la transición.

## Cómo se pasa el grave

La receta que repiten las guías de práctica, según su resumen
([Digital DJ Pool](https://digitaldjpool.com/blog/dj-eq-mixing-for-beginners/),
[Digital DJ Tips](https://www.digitaldjtips.com/?p=2799689)):

1. Antes de abrir el canal del tema entrante, bajá su LOW del todo o casi.
2. Entrá el tema sincronizado (ver [tempo y fase](../Tiempo/tempo-y-fase.md)) con el grave
   cortado.
3. En un límite de [frase](../Forma/frase.md), cada 8 o 16 compases (una o dos frases), bajá el LOW del saliente
   mientras subís el del entrante.
4. Después, sacá el resto del tema saliente (ver
   [puntos de entrada y salida](../Forma/puntos-de-entrada-y-salida.md)).

Los pasos 2 y 4 completan la receta y no vienen de las guías.

Los datos de Kim y otros muestran que en 1557 mezclas reales los largos de transición se agrupan
en múltiplos de 32 pulsos, que el estudio lee como frases de la música de baile
([Kim et al., ISMIR 2020](https://program.ismir2020.net/static/final_papers/352.pdf)). El estudio
mide la transición entera, no el momento del swap, así que no prueba que el swap caiga en una
frase.

## Swap seco o swap gradual

Las guías distinguen dos formas, según su resumen: un swap instantáneo, en el pulso, para cuando
el tema entrante tiene que pegar, y un swap gradual de dos a cuatro pulsos para grooves que ruedan
([Digital DJ Pool](https://digitaldjpool.com/blog/dj-eq-mixing-for-beginners/)).

Boris Brejcha, según su entrevista, no aplica una sola. Cuando busca impacto intenta "cut the bass
super hard on the incoming tracks"; con temas melódicos prefiere transiciones lentas, y mantiene
el tema entrante en loop uno o dos minutos antes de subirlo
([Pioneer DJ Blog](https://blog.pioneerdj.com/?p=4768)). Es un swap, pero con tiempos distintos
del esquema de cambio en la frase.

> [!NOTE] Sin fuente todavía: cómo hacen el swap los DJs de techno de mezcla larga en particular
> (cuánto dura, si se usa el filtro en lugar del EQ). Las guías citadas son generales.

## Lo que se oye cuando sale mal

Según cursa.app, en un resumen del buscador, hay dos diagnósticos opuestos:

- Grave hinchado o borroso (*boomy*): los dos graves se superpusieron demasiado tiempo.
- La sala "se hunde": se sacó demasiado grave de golpe, y por un momento no hay bajo.

Un tercer síntoma es inferencia, no cita: si el entrante entra con el LOW arriba, la suma de los
dos graves sube el nivel, y eso se ve en el medidor (ver
[ganancia](ganancia-y-volumen-percibido.md)).

> [!IMPORTANT] Disputado: por qué embarran dos bombos. Se repite que dos bombos a la vez "se
> cancelan por fase". No hay prueba de eso para la mezcla de DJ: no se encontró ningún estudio
> medido sobre dos bombos superpuestos de dos temas distintos. La cancelación por desfase sí está
> documentada para capas dentro de una misma producción: Senior advierte que las capas de bajo
> "can cancel gruesomely at certain frequencies if there are polarity or phase mismatches"
> ([Sound On Sound](https://www.soundonsound.com/techniques/mixing-bass)), pero ahí los sonidos
> están fijos entre sí, no son dos discos con una deriva lenta. Un usuario de un foro de audio
> sostiene que lo que se llama *phasing* en graves suele ser una fluctuación de volumen y de
> frecuencia al cambiar la relación de fase, no una cancelación simple, según su resumen
> ([KVR Audio](https://www.kvraudio.com/forum/viewtopic.php?p=8908635)). Las guías atribuyen el
> embarrado más a la acumulación de graves y medios que a la fase. La regla práctica (un solo
> grave dominante) se sostiene por consenso de practicantes; su explicación física queda abierta.

## Dónde leer más

Para el principio detrás del swap, leé "Mixing Bass" de Mike Senior en
[Sound On Sound](https://www.soundonsound.com/techniques/mixing-bass). Es de estudio, no de DJ:
fijate en la sección sobre varias partes de bajo y en el conflicto entre bombo y bajo debajo de
100 Hz, el problema que esta nota aplica a la transición.
