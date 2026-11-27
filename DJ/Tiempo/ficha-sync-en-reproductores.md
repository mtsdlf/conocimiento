---
resumen: >-
  Cómo resuelven la grilla, el sync, el quantize y el key lock dos programas concretos, Mixxx 2.4
  y rekordbox 7.1.4, según sus manuales, con la fecha de la copia.
estado: vigente
estabilidad: volatil
fuentes:
  - "Mixxx, manual 2.4, DJing With Mixxx: https://manual.mixxx.org/2.4/chapters/djing_with_mixxx"
  - "rekordbox 7.1.4, manual en inglés (PDF): https://cdn.rekordbox.com/files/20250718115648/rekordbox7.1.4_manual_EN.pdf"
  - "DJ/.investigacion/tiempo-y-forma.md"
aliases: [Sync en Mixxx, Sync en rekordbox, Master Tempo, Sync Lock]
creado: 2026-11-27
revisado: 2026-11-27
---

# Sync en reproductores

Cómo resuelven la grilla, el sync, el quantize y el key lock dos programas concretos, Mixxx 2.4
y rekordbox 7.1.4, según sus manuales, con la fecha de la copia.

Implementa lo que explica [sync y beatgrid](sync-y-beatgrid.md).

Fuentes vivas: el capítulo "DJing With Mixxx" del
[manual de Mixxx 2.4](https://manual.mixxx.org/2.4/chapters/djing_with_mixxx) y el
[manual de rekordbox 7.1.4](https://cdn.rekordbox.com/files/20250718115648/rekordbox7.1.4_manual_EN.pdf),
este último leído por secciones. Copiado de esas fuentes el 2026-11-27; conviene verificar contra
la versión que se use.

## Grilla, sync y fase

| Qué | Mixxx 2.4 | rekordbox 7.1.4 |
|---|---|---|
| Nombre del sync | Sync Lock | Beat Sync |
| Qué iguala el sync | "usually only makes sure the rate sliders are set correctly": el tempo | — |
| Cómo se asegura la fase | Quantize: "will ensure that the beats are perfectly lined up as well" | Con quantize encendido, el cue se ajusta al pulso más cercano de la grilla |
| Marca del "1" en la grilla | — | "the first beat of bar" en rojo, cada 4 pulsos |
| Corregir la grilla a mano | Se puede estirar, comprimir y mover | "Adjust the beat grid" |
| Proteger la grilla corregida | — | Volver a analizar sobrescribe la grilla corregida; Analysis Lock lo evita |
| Tempo doble o mitad | El sync reconoce, por ejemplo, 140 con 70 | — |
| Temas que cambian de tempo | Desde 2.4 el seguidor sigue al líder "unconditionally" y "changes its tempo matching the leader which may result in a notable pitch change"; el keylock lo reduce | — |

Un guion significa que el informe de investigación no lo leyó en ese manual, no que el programa
no lo tenga.

## Key lock y resolución del control de velocidad

| Qué | Mixxx 2.4 | rekordbox 7.1.4 |
|---|---|---|
| Nombre del key lock | Keylock: "When it is active changing the speed of a track won't affect the key" | Master Tempo (MT): "The pitch of the track does not change even when you change the playback speed" |
| Sin key lock | — | La tonalidad que muestra cambia si el BPM cambia por Beat Sync |
| Paso del control de velocidad | El manual no da el rango del control | "0.02% at ±6 / 0.04% at ±10 and ±16 / 0.5% at WIDE" |

El paso del control de rekordbox es la resolución de cada rango: cuanto más corto el rango, más
fino el ajuste, y no es una medida de precisión absoluta.

## Lo que el mismo análisis hace con las frases

rekordbox también analiza la estructura del tema y convierte cada sección en una "phrase", con
un Fill-in de hasta 4 pulsos al final de algunas secciones (manual 7.1.4, leído en parte).
Según un foro de usuarios, los nombres de sección cambian con el carácter del tema: Intro, Verse,
Bridge, Chorus y Outro en uno, y Up, Down y Chorus en otro. El informe los describe como
categorías de pop y EDM, no como el vocabulario de techno (ver
[secciones de un tema](../Forma/secciones-de-un-tema.md)). El CUE Analysis pone cues
automáticos, y si el tema tiene pocas frases pone menos.

> [!NOTE] Sin fuente todavía: el apéndice de Phrase Analysis del manual de rekordbox y la guía
> aparte de Phrase Edit no se leyeron, y los nombres de sección vienen de un foro.
