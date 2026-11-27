---
resumen: >-
  El criterio de selección es lo que hace que un tema merezca entrar en una sesión y que, puesto
  después de otro, la secuencia funcione. Se juega en dos planos: el tema solo (si rinde en una
  pista) y el tema en relación con el anterior (cuánto se le parece y cuánto lo contrasta).
estado: vigente
estabilidad: semi
fuentes:
  - "Kell y Tzanetakis, Empirical Analysis of Track Selection and Ordering in Electronic Dance Music using Audio Feature Extraction, ISMIR 2013: https://archives.ismir.net/ismir2013/paper/000210.pdf"
  - "Kim, Choi, Sacks, Yang y Nam, A Computational Analysis of Real-World DJ Mixes using Mix-To-Track Subsequence Alignment, ISMIR 2020: https://program.ismir2020.net/static/final_papers/352.pdf"
  - "Jeff Mills, lectura en Red Bull Music Academy, 5 de abril de 1998: https://www.redbullmusicacademy.com/lectures/jeff-mills-lecture"
  - "Vande Veire y De Bie, DJ automático de drum and bass, EURASIP Journal on Audio, Speech, and Music Processing, 2018: https://link.springer.com/article/10.1186/s13636-018-0134-8"
  - "DJ-AI, sistema de DJ automático, 2025: https://research.sabanciuniv.edu/52373/1/AI_DJ_AM2025.pdf"
  - "The Quietus, reseña de Rave Culture de Emmanuel, Noel Gardner, 4 de octubre de 2017: https://thequietus.com/quietus-reviews/emmanuel-rave-culture-album-review/"
aliases: [Elegir un tema, Coherencia y contraste]
creado: 2026-11-27
revisado: 2026-11-27
---

# Criterio de selección

El criterio de selección es lo que hace que un tema merezca entrar en una sesión y que, puesto después de otro, la secuencia funcione. Se juega en dos planos: el tema solo (si rinde en una pista) y el tema en relación con el anterior (cuánto se le parece y cuánto lo contrasta).

Es el corazón de la [selección](seleccion.md). Los dos planos usan las mismas dimensiones que la unión: [tempo](../Tiempo/tempo-y-fase.md), [espectro](../Espectro/espectro.md), [tonalidad](../Armonia/tonalidad-y-compatibilidad.md) y [energía](../Energia/energia.md). La diferencia es el momento: acá se decide antes de que el tema suene.

## Qué hace elegible a un tema

No hay un estudio sobre qué hace elegible a un tema para un DJ humano, ni sobre la calidad de producción o el groove como criterio. Lo que hay es el testimonio de practicantes y datos indirectos.

Jeff Mills, según el resumen de su lectura de 1998, elige discos que tengan "at least two" buenos temas, para poder tocar cada uno más de una vez, y dice "very rarely do I ever play a record that only has one good track". También toca "the best part of it, and then move on to the next one": usa partes de los discos como material, no el disco entero ([RBMA](https://www.redbullmusicacademy.com/lectures/jeff-mills-lecture)).

De ahí salen tres preguntas para un tema candidato. Son una síntesis de trabajo:

1. ¿Rinde en una pista? Que funcione con volumen y en un sistema grande.
2. ¿Qué función cumple? Si sirve para unir o para que la sesión se recuerde: [herramienta o pieza](herramienta-y-pieza.md).
3. ¿Tiene partes usables? Un tramo largo de percusión para entrar, un break para descargar, un final limpio para salir: los [puntos de entrada y salida](../Forma/puntos-de-entrada-y-salida.md) que dan las [secciones](../Forma/secciones-de-un-tema.md).

## Coherencia y contraste en la secuencia

Dos temas seguidos tienen que parecerse lo suficiente para que la unión no corte el baile, y diferenciarse lo suficiente para que la sesión avance. Los datos de mezclas reales muestran hacia dónde se inclina la práctica.

- Tempo: en 1557 mezclas analizadas por Kim y otros, el 86,1 % de los temas se tocó con menos de 5 % de cambio de tempo ([ISMIR 2020](https://program.ismir2020.net/static/final_papers/352.pdf)). Los DJs corrigen poco el tempo; el corpus es sobre todo de house y trance.
- Timbre como hilo: Kell y Tzanetakis encontraron que "Timbre appears to be an important factor when selecting tracks and ordering tracks", y que ordenar por parecido decreciente al primer tema quizá no sea óptimo para música de baile ([ISMIR 2013](https://archives.ismir.net/ismir2013/paper/000210.pdf)).
- Energía sin saltos grandes: la guía de un fabricante dice que saltar de 5 a 7 en su escala suena como si otro DJ se hubiera subido a la cabina; se trata en [energía](../Energia/energia.md#cómo-falla-la-energía).

Como propuesta de esta nota, el contraste puede entrar por dimensiones que no rompen la unión: un timbre nuevo sobre el mismo pulso, una percusión más seca, un tema con melodía después de varios sin ella. Un ejemplo de mezcla de rasgos dentro de un mismo disco: The Quietus describe el disco de 2017 de Emmanuel, fundador del sello [ARTS](../Fundamentos/sello-arts.md), como "solid banging rave-loving techno tunes", con "hard percussion with bright, trance-style synth melodies" ([The Quietus](https://thequietus.com/quietus-reviews/emmanuel-rave-culture-album-review/)).

## Lo que hacen los sistemas automáticos

Los DJs automáticos codifican el criterio en reglas. Uno de 2025 usa, según su resumen, compatibilidad de tonalidad, tempo dentro de ±2 BPM y energía sin saltos grandes ([DJ-AI 2025](https://research.sabanciuniv.edu/52373/1/AI_DJ_AM2025.pdf)). Uno de drum and bass ubica los temas en un "espacio de estilo" continuo, y 18 fans del género calificaron sus mezclas de alta calidad, según su resumen ([Vande Veire y De Bie 2018](https://link.springer.com/article/10.1186/s13636-018-0134-8)). Son reglas de ingeniería: muestran qué se puede automatizar, no qué hace elegible un tema para un DJ.

Para leer: Kell y Tzanetakis 2013, el abstract y las secciones de análisis de transiciones y de heurísticas de orden. Fijate en que mide timbre, tempo, tonalidad y sonoridad entre temas consecutivos de sets reales, y en que el orden importa.

## Cómo falla

Son deducciones de esta nota.

- Coherencia sin contraste: temas casi intercambiables; la unión es perfecta y la sesión no va a ningún lado.
- Contraste sin hilo: cada tema rompe con el anterior en tempo, timbre y energía a la vez.
- Elegir por el tema solo: un tema excelente que no tiene dónde entrar después del que suena; el criterio se aplica siempre contra el anterior.
- Discos de un solo tema: Mills los evita porque quiere poder volver a cada disco; cómo se arma una caja que rinda está en [colección](coleccion.md).
