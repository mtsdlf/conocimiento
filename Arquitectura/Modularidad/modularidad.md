---
resumen: >-
  La modularidad es cómo se parte un sistema en piezas con límites claros: cuánto depende cada pieza
  de las otras (acoplamiento), cuánto tiene que ver lo que hay adentro de cada una (cohesión) y
  cuánto esconde cada una detrás de su interfaz (profundidad).
estado: borrador
estabilidad: estable
fuentes:
  - https://connascence.io/
  - https://web.stanford.edu/~ouster/cgi-bin/book.php
  - https://github.com/johnousterhout/aposd-vs-clean-code
  - https://nealford.com/books/SAF2e.html
  - "Ousterhout, A Philosophy of Software Design, 2ª ed. (2021), caps. 4 'Modules Should Be Deep' y 6 'General-Purpose Modules are Deeper' (no leídos)"
  - "Richards y Ford, Fundamentals of Software Architecture, 2ª ed. (O'Reilly, 2025), cap. 'Modularity' (no leído)"
  - https://medium.com/@nakabonne/depth-of-module-f62dac3c2fdb
aliases: [modularity, acoplamiento, cohesión, coupling, cohesion, módulo profundo, deep module]
creado: 2026-11-27
revisado:
---

# Modularidad

La modularidad es cómo se parte un sistema en piezas con límites claros: cuánto depende cada pieza
de las otras (acoplamiento), cuánto tiene que ver lo que hay adentro de cada una (cohesión) y
cuánto esconde cada una detrás de su interfaz (profundidad).

Es la vertical que delimita las piezas con las que trabaja el resto. Un
[estilo](../Estilos/estilos.md) decide cómo se despliegan y se comunican esas piezas, pero no dónde
van los límites: eso es modularidad. Por eso un [monolito modular](../Estilos/monolito-modular.md)
y unos [microservicios](../Estilos/microservicios.md) pueden tener los mismos módulos, uno en un
proceso y el otro repartido por la red (lectura de esta base, no del canon). Los límites se eligen para cumplir las
[características](../Caracteristicas/caracteristicas.md) priorizadas: lo que tiene que escalar,
desplegarse o cambiar por separado va en su propio módulo. Richards y Ford tratan la modularidad
como un capítulo de fundamentos, antes que los estilos.

## Acoplamiento y cohesión

Un módulo está bien cortado cuando lo de adentro cambia junto y lo de afuera casi no se entera. La
cohesión mide lo primero: un módulo de facturación cohesivo tiene todo lo de facturación y nada de
envíos. El acoplamiento mide lo segundo: si cambiar cómo se guarda un pedido obliga a tocar cinco
módulos, están acoplados. Se busca cohesión alta y acoplamiento bajo; es el criterio habitual del campo, sin fuente leída
para esta nota. Que una arrastre a la otra (lo que no está junto adentro termina conectado afuera)
es observación de esta base.

> [!NOTE] Sin fuente todavía: las clasificaciones de cohesión y acoplamiento del capítulo
> "Modularity" de Richards y Ford (no se pudo leer).

## Connascence: medir el acoplamiento

Connascence es "a software quality metric & a taxonomy for different types of coupling": dos
piezas son connascentes si cambiar una obliga a cambiar la otra. La taxonomía separa las formas
estáticas, que se ven en el código (de nombre, de tipo, de significado, de posición, de algoritmo),
de las dinámicas, que aparecen al ejecutar (de ejecución, de tiempo, de valor, de identidad). La
taxonomía se suele atribuir a Meilir Page-Jones; no se verificó en una fuente primaria.

Tres propiedades dicen qué acoplamiento preocupa:

- **Fuerza**: "Stronger connascences are harder to discover, or harder to refactor". Los
  ejemplos son de esta base: que dos módulos compartan un nombre es débil; que dependan del orden
  en que se ejecutan es fuerte.
- **Localidad**: "Connascent elements that are close together in a codebase are better than ones
  that are far apart". El mismo acoplamiento es tolerable dentro de un módulo y caro entre dos
  servicios.
- **Grado**: cuántas piezas están involucradas.

La regla práctica que sale de ahí (inferencia de esta base): las formas fuertes de acoplamiento se quedan adentro de un
módulo, y entre módulos solo cruzan las débiles.

## Módulos profundos

John Ousterhout, en *A Philosophy of Software Design*, propone que los módulos sean profundos:
mucha funcionalidad detrás de una interfaz chica. Un módulo superficial, en lectura de esta base, tiene una interfaz casi tan
grande como lo que hace, y quien lo usa no se ahorra nada. La definición viene de resúmenes
secundarios; el libro la trata en el capítulo 4, "Modules Should Be Deep".

En su debate con Robert Martin, Ousterhout discute que partir el código en métodos diminutos produce
"teeny-tiny methods that suffer from both shallow interfaces and entanglement", y que "the
fundamental goal of software design is to make it easy to understand and modify the system".

> [!IMPORTANT] La profundidad tiene críticos. Un artículo sostiene que las clases profundas son más
> difíciles de testear, porque mucha lógica queda detrás de pocas entradas (según su resumen). La
> tensión importa cuando el módulo esconde algo incierto, como un modelo de IA.

## El modelo de IA como módulo

Un modelo de lenguaje es la pieza menos predecible de un sistema: la misma entrada da salidas
distintas, y el proveedor puede cambiarlo. Eso lo vuelve el caso más claro para aplicar todo lo de
arriba: ponerlo detrás de una interfaz propia, chica y profunda, para que el resto del sistema no
dependa de sus detalles. Cómo se hace y dónde está el límite con las abstracciones que esconden
demasiado está en [aislar lo no determinista](aislar-lo-no-determinista.md).

## Qué hay adentro de Modularidad

- [Aislar lo no determinista](aislar-lo-no-determinista.md) — el modelo detrás de una interfaz
  propia y chica: qué se gana (cambiar de modelo, fallback, costo, pruebas) y qué no hay que
  esconder.

## Qué leer

Ousterhout, *A Philosophy of Software Design*, 2ª ed. (2021), capítulo 4, y el debate con Martin en
el repositorio `aposd-vs-clean-code` de GitHub, que es gratis. Fijarse en la profundidad como
relación entre lo que el módulo hace y el tamaño de su interfaz. Para connascence, el sitio
connascence.io, mirando fuerza, localidad y grado. El capítulo "Modularity" de Richards y Ford
completa el canon.
