---
resumen: >-
  El enmascaramiento es el efecto por el que un sonido hace más difícil oír otro cuando los dos
  caen en la misma zona de frecuencias. Explica por qué dos graves a la vez se confunden y por qué
  en la mezcla se reparten bandas en lugar de sumarlas.
estado: vigente
estabilidad: estable
fuentes:
  - "Wikipedia, Critical band (cita a Fletcher 1933/1940, Glasberg y Moore 1990, Moore 1998): https://en.wikipedia.org/wiki/Critical_band"
  - "Mike Senior, Mixing Bass, Sound On Sound, sept. 2012: https://www.soundonsound.com/techniques/mixing-bass"
  - "Zwicker y Fastl, Psychoacoustics: Facts and Models, Springer (no leído; recurso recomendado)"
aliases: [Masking, Enmascaramiento auditivo]
creado: 2026-11-27
revisado: 2026-11-27
---

# Enmascaramiento

El enmascaramiento es el efecto por el que un sonido hace más difícil oír otro cuando los dos
caen en la misma zona de frecuencias. Explica por qué dos graves a la vez se confunden y por qué
en la mezcla se reparten bandas en lugar de sumarlas.

## La banda crítica decide quién tapa a quién

La banda crítica es el ancho de banda del filtro auditivo: según el resumen de
[Wikipedia](https://en.wikipedia.org/wiki/Critical_band), "is the bandwidth of the 'auditory
filter' created by the cochlea", y es "roughly, the band of frequencies within which a second
tone interferes with the perception of a first tone through auditory masking". La idea la
introdujo Harvey Fletcher en 1933 y la refinó en 1940.

Dos consecuencias importan en la cabina:

1. Solo tapa lo que está cerca. Únicamente los sonidos que caen dentro de la banda crítica de
   otro contribuyen a enmascararlo.
2. Los graves tapan hacia arriba. El enmascaramiento es asimétrico: un sonido grave tapa a uno
   más agudo más de lo que el agudo tapa al grave (en la literatura, *upward spread of masking*).

## La banda crítica en los graves

Con la fórmula ERB de Glasberg y Moore que cita la misma página, el informe de investigación
calcula una banda de unos 79 Hz alrededor de 500 Hz (cálculo, no cifra de la fuente). Las notas
graves están separadas entre sí por pocos hertz, así que debajo de 100 Hz, donde Senior ubica el
conflicto entre bombo y bajo, casi todo cae en una misma banda. Esa lectura es inferencia del
informe a partir de la fórmula, no una afirmación de la fuente.

Para Mike Senior, la zona de 20 a 100 Hz "presents probably the most difficult challenge" y el
conflicto entre bajo y bombo es el más crítico de los graves
([Sound On Sound](https://www.soundonsound.com/techniques/mixing-bass)). Es consejo de estudio.
En una transición de DJ hay dos bombos y dos bajos donde una producción tiene uno de cada uno;
aplicar el principio de Senior con el [swap de graves](swap-de-graves.md) es una extensión de esta
nota, sin fuente de DJ.

> [!NOTE] Sin fuente todavía: la escala Bark de Zwicker (24 bandas) y el ancho de banda crítica
> en graves con cifra primaria; la página consultada no lo trae.

## Del oído a la perilla

Si dos temas no pueden ocupar la misma banda sin taparse, el [ecualizador](ecualizador-y-filtros.md)
decide quién se queda con cada una. Por la asimetría, el orden de prioridad iría de abajo hacia
arriba: primero el dueño del grave, después los medios, y los agudos serían los que mejor toleran
la superposición. Esa jerarquía es inferencia de las dos reglas de arriba, no una receta de una
fuente.

El informe de investigación propone pensar la [armonía](../Armonia/armonia.md) como un caso
particular del espectro, porque las dos dependen de lo que suena en la misma zona de frecuencias.

## Dónde leer más

El texto canónico es Zwicker y Fastl, *Psychoacoustics: Facts and Models* (Springer), capítulos de
enmascaramiento y bandas críticas. No es de acceso abierto y no se leyó para esta nota. Al leerlo,
fijate en la escala Bark, en el ancho de la banda crítica en graves y en el gráfico del
enmascaramiento asimétrico hacia arriba.
