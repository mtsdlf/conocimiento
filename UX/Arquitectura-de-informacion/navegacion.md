---
resumen: >-
  La navegación es el sistema con el que una persona se mueve por la estructura de un producto: sus tipos (global, local, migas de pan) se eligen para que las etiquetas anticipen bien el destino, algo que según NN/g importa más que cualquier regla de conteo.
estado: borrador
estabilidad: semi
fuentes:
  - "NN/g, Pernice y Budiu, Hamburger Menus and Hidden Navigation Hurt UX Metrics, 26 de junio de 2016: https://www.nngroup.com/articles/hamburger-menus/"
  - "NN/g, Nielsen y Li, Mega Menus Work Well for Site Navigation, 26 de marzo de 2017: https://www.nngroup.com/articles/mega-menus-work-well/"
  - "NN/g, Laubheimer, Breadcrumbs: 11 Design Guidelines for Desktop and Mobile, 23 de diciembre de 2018: https://www.nngroup.com/articles/breadcrumbs/"
  - "NN/g, Laubheimer, Local Navigation Is a Valuable Orientation and Wayfinding Aid, 4 de julio de 2021: https://www.nngroup.com/articles/local-navigation/"
  - "NN/g, Budiu, Information Scent: How Users Decide Where to Go Next, 2 de febrero de 2020: https://www.nngroup.com/articles/information-scent/"
  - "Wai-Tat Fu y Peter Pirolli, SNIF-ACT: A Cognitive Model of User Navigation on the World Wide Web, Human-Computer Interaction 22, 2007, pp. 355-412 (abstract y teoría): https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/25938.pdf"
  - "Peter Pirolli y Stuart Card, Information Foraging, Psychological Review 106(4), 1999 (solo referencia)"
  - "NN/g, The 3-Click Rule for Navigation Is False: https://www.nngroup.com/articles/3-click-rule/"
  - "UX/.investigacion/arquitectura-e-interaccion.md y UX/.investigacion/posicion-contraria.md"
aliases: [navegación global, navegación local, migas de pan, breadcrumbs, information scent, olor de información]
creado: 2026-11-22
revisado:
---

# Navegación

La navegación es el sistema con el que una persona se mueve por la estructura de un producto: sus tipos (global, local, migas de pan) se eligen para que las etiquetas anticipen bien el destino, algo que según NN/g importa más que cualquier regla de conteo.

Es uno de los cuatro sistemas de la [arquitectura de información](arquitectura-de-informacion.md). La estructura de la que depende sale de cómo se organiza el contenido y de cómo se lo llama; la navegación la expone. Cada paso que la persona da por ella suma, por inferencia de esta base, [carga cognitiva](../Percepcion-y-decision/carga-cognitiva.md) y tiempo de elegir, como describen las [leyes de Fitts y de Hick](../Percepcion-y-decision/leyes-de-fitts-y-hick.md).

## Tipos de navegación

Según NN/g, la navegación global es el nivel superior de la jerarquía: estable en todo el sitio, sirve para saltar entre las categorías principales. La local es "contextual to the user's current location": muestra las páginas pares y, si corresponde, las subordinadas, y cambia por categoría, no por usuario ni por sesión.

NN/g usa "contextual" para describir la navegación local, y menciona los enlaces contextuales a contenido relacionado como alternativa liviana en sitios profundos. En otras fuentes, "contextual" son los enlaces dentro del contenido. Esta base usa "local" para el bloque de la sección actual y "enlaces contextuales" para los de dentro del contenido.

Las migas de pan muestran dónde está una página en la estructura, no el recorrido: "Breadcrumbs are not intended to show the history of pages traversed during a session on the site". Sirven sobre todo a quien llega desde un enlace externo sin pasar por la portada. En sitios planos, de uno o dos niveles, sobran. El último ítem no es un enlace, y las migas complementan la navegación global y la local, no las reemplazan.

## El olor de información explica por qué una etiqueta funciona

Según NN/g, el olor de información es la estimación imperfecta que hace una persona del valor que le dará una fuente, a partir de una representación de ella. Según descripciones secundarias, la teoría adapta a la búsqueda de información la del forrajeo óptimo (Pirolli y Card, 1999; solo se leyó una referencia). En SNIF-ACT, el modelo de Fu y Pirolli (2007), el olor se calcula con las pistas próximas (las etiquetas de los enlaces) para predecir si la fuente distante contiene lo buscado. El modelo supone que la persona evalúa los enlaces en secuencia y decide entre hacer clic o volver.

NN/g da estas guías para etiquetar: etiquetas específicas y autoexplicativas (evitar "More"), con el lenguaje del público, que no dependan del contexto que las rodea, coherentes con el destino (el clickbait erosiona la confianza) y reforzadas en la página de destino. Para entender el mecanismo, leer a Fu y Pirolli (2007); para aplicarlo a etiquetas, el artículo de Budiu (2020).

## Qué dice la evidencia sobre el menú hamburguesa

El estudio de NN/g de 2016 (Pernice y Budiu) midió la navegación oculta con 179 participantes reclutados en WhatUsersDo, seis sitios reales, en escritorio y celular, con dos tareas por sitio.

| Condición | Uso en escritorio | Uso en celular | Dificultad de la tarea (1 a 7, menor es más fácil) |
|---|---|---|---|
| Oculta | 27 % | 57 % | 2,6 |
| Visible | 48 % | no se probó | 2,1 |
| Combinada | 50 % | 86 % | 2,3 |

La descubribilidad del contenido cayó más de 20 % con navegación oculta frente a visible o combinada. En escritorio, la tarea tomó al menos 39 % más de tiempo con navegación oculta; en celular, 15 % más que con la combinada. Según NN/g, la tarea resultó 21 % más difícil con navegación oculta que con visible.

Los límites son del propio estudio: es de 2016, la navegación visible pura no se probó en celular y las convenciones del ícono pueden haber cambiado. No hay evidencia más nueva y comparable en lo leído.

## Cuándo funcionan los mega menús

Según Nielsen y Li (NN/g, 26 de marzo de 2017), los mega menús funcionan bien si se cuidan varios detalles:

- Activar lo que depende del cursor solo después de que el mouse quede quieto 0,5 segundos ("the mouse should remain stationary for 0.5 seconds"); sin esa demora, "the screen flicker insufferably".
- No cerrar el menú mientras la persona apunta en diagonal a una opción de adentro.
- En pantallas táctiles, las opciones pequeñas causan errores de selección.
- Con lupa o pantalla chica, los usuarios "may assume that the visible content is all the content that is available".
- Agrupar con granularidad media, con etiquetas concisas y cada opción una sola vez, porque las duplicadas hacen dudar si son lo mismo.

En lo leído no hay cifras de uso: es una guía de instituto, no un estudio cuantitativo como el del menú hamburguesa.

## Dónde falla la regla de los tres clics

La regla dice que todo debe estar a tres clics. NN/g afirma que "has not been supported by data in any published studies to date", y que la referencia publicada más antigua que encontró es un libro de Jeffrey Zeldman de 2001, sin datos. Atribuye a un estudio de Porter (2003, de la consultora UIE) el hallazgo de que el abandono no crece cuando la tarea pasa de tres clics, ni baja la satisfacción. Esa cita es de segunda mano: el estudio de Porter no se leyó. Lo que importa, según NN/g, son las etiquetas, la orientación (migas de pan) y el tiempo de carga. Es la lectura de un solo instituto, sin contraste con otra fuente. Está en la lista de [mitos de UX](../Fundamentos/mitos-de-ux.md).

## Qué falta de la navegación

[Arquitectura de información](arquitectura-de-informacion.md) ubica este sistema entre los otros tres. Faltan por escribir la búsqueda y los filtros, con las facetas para catálogos, de las que no hay una fuente leída.
