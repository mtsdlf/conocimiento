---
resumen: >-
  Una fitness function es una prueba automática y objetiva de que el sistema sigue cumpliendo una
  característica arquitectónica, como un test unitario pero para la arquitectura; con un modelo de
  IA adentro, una evaluación con umbral cumple ese papel.
estado: vigente
estabilidad: estable
fuentes:
  - https://www.thoughtworks.com/en-us/insights/podcasts/technology-podcasts/rethinking-software-governance-reflecting-second-edition-building-evolutionary-architectures
  - "Ford, Parsons, Kua, Sadalage, Building Evolutionary Architectures, 2ª ed. (O'Reilly, 2022), cap. 2 'Fitness Functions' (no leído)"
  - https://oreilly.com/library/view/building-evolutionary-architectures/9781491986356/ch02.html
  - https://martinfowler.com/articles/gen-ai-patterns/
  - https://huyenchip.com/2024/07/25/genai-platform.html
aliases: [función de aptitud, architectural fitness function]
creado: 2026-11-27
revisado: 2026-11-27
---

# Fitness function

Una fitness function es una prueba automática y objetiva de que el sistema sigue cumpliendo una
característica arquitectónica, como un test unitario pero para la arquitectura; con un modelo de
IA adentro, una evaluación con umbral cumple ese papel.

## Un test unitario para una característica

El nombre viene de los algoritmos genéticos, donde la función de aptitud dice qué tan buena es una
solución. Ford, Parsons y Kua la llevaron a la arquitectura en *Building Evolutionary
Architectures*; la 1ª edición la define, según el buscador, como "objective integrity assessment of
some architectural characteristic(s)". Neal Ford la describe como "unit tests for architectural
characteristics", y agrega que son más difíciles de escribir que un test unitario.

Lo que la define es que su resultado no se discute. Rebecca Parsons lo dice así: "we will never
disagree on the result of the fitness function". "Be maintainable" no sirve como fitness function;
"cyclomatic complexity below a set threshold" sí. Por eso una
[característica](caracteristicas-arquitectonicas.md) tiene que tener un número antes de poder
gobernarse.

## Gobernar con pruebas en lugar de revisiones

La 2ª edición del libro pone el acento en usarlas para automatizar la gobernanza, además de para
guiar la evolución. Según Parsons, eso mueve la gobernanza del "box-ticking" a discutir la
sustancia: qué característica gana cuando dos chocan. También marca el límite: "no concept, no
tool, no nothing, can solve for bad behavior". Una fitness function avisa que algo se degradó;
decidir qué hacer sigue siendo un acuerdo entre personas, que se registra en un
[ADR](../Decisiones/adr.md).

## La evaluación como fitness function probabilística

Con un [modelo de lenguaje](../../IA/Modelos/modelo-base.md), la misma entrada da salidas distintas y "pasa o no
pasa" deja de alcanzar. El artículo de Bharani Subramaniam sobre patrones de IA generativa, en el sitio de Martin Fowler, lo dice así: los evals "aren't simple
binary pass/fail results, instead we have to set thresholds". Huyen pide evaluar "at every step of
the development process".

Leer una [evaluación](../../IA/Evaluacion/evals.md) con umbral como una fitness
function probabilística es inferencia de esta base: ninguna de las fuentes lo formula así. La
equivalencia sirve porque trae las reglas del canon al sistema con modelos. La evaluación tiene que
dar un número que nadie discute (una proporción sobre un conjunto de casos), tiene que correr sola
en cada cambio, y su umbral es una decisión que se registra. Lo que no hereda es la certeza: un
juez automático también se equivoca, y eso se trata en
[IA como juez](../../IA/Evaluacion/ia-como-juez.md).

## Qué leer

*Building Evolutionary Architectures*, 2ª ed., cap. 2 "Fitness Functions". Fijarse en que el
resultado sea objetivo y en cómo las clasifica (por ejemplo, las que miran una sola característica
frente a las que miran varias juntas, y las que corren ante un evento frente a las que corren todo
el tiempo). Sin acceso al libro, el podcast de Thoughtworks con Ford y Parsons de noviembre de 2022
es la entrada gratuita.
