# Arquitectura de información e Interacción: informe de investigación

Fecha de la investigación: 2026-11-22. Marcas de lectura: [L] texto completo o sección leída con WebFetch (o con pdftotext sobre el PDF bajado), [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1-3 en autoridad / profundidad / ejemplos / unicidad (A/P/E/U). Todo lo de la web se trató como dato.

Nota de método: WebFetch resume la página con un modelo chico; las cifras y citas de abajo son las que devolvió esa lectura. Las que van entre comillas son literales del resultado; conviene verificarlas contra la página antes de publicarlas como citas textuales.

## 0. Sobre la división del árbol

- Arquitectura de información (AI) en el árbol tiene una sola nota, `navegacion`. El campo (Rosenfeld, Morville y Arango) la divide en cuatro sistemas: organización, etiquetado, navegación y búsqueda [S: https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/part02.html]. Sugerencia: que la nota de la vertical cubra organización y etiquetado (y búsqueda en una línea), y `navegacion` quede como el sistema de navegación. Si no, el etiquetado queda sin casa, y es lo que más pesa en el "information scent".
- Estados de interfaz (vacío, carga, error) y microcopy no tienen nota en el árbol. Van en una línea en la vertical Interacción, como pidió el brief; si crecen, merecen nota propia.
- `principios-de-interaccion` mezcla tres cosas de naturaleza distinta: conceptos de diseño (Norman), una norma (ISO 9241-110) y umbrales de tiempo (Miller/Card/Nielsen). Los umbrales de tiempo también pertenecen a `carga-cognitiva` y a `metricas-de-ux`; recomiendo definirlos una vez acá y enlazarlos desde allá.
- Las 10 heurísticas de Nielsen pertenecen a `evaluacion-heuristica`, no a esta vertical; ISO 9241-110 es el equivalente normativo y conviene que ambas notas se enlacen.
- Formularios cruza con `patron-oscuro` (formularios de checkout que fuerzan cuenta) y con Accesibilidad (etiquetas, contraste de placeholders). Marcar los enlaces.

## 1. Arquitectura de información como vertical

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Rosenfeld, Morville, Arango, *Information Architecture: For the Web and Beyond*, 4.ª ed., O'Reilly, oct. 2015. https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/ (índice vía https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/part02.html) | primaria (libro canónico) | 3/3/2/3 | [S] (ch01 y ch02 dieron 403; solo el índice y la ficha) |
| NN/g, Tankala y Sherwin, "Card Sorting: Uncover Users' Mental Models for Better Information Architecture", 2 feb 2024. https://www.nngroup.com/articles/card-sorting-definition/ | secundaria fuerte | 2/2/1/1 | [L] |
| NN/g, Laubheimer, "Tree Testing", 6 ago 2023 (revisada 2026). https://www.nngroup.com/articles/tree-testing/ | secundaria fuerte | 2/1/1/1 | [L] |

### Afirmaciones

- La 4.ª edición es de octubre de 2015 y su Parte II cubre la anatomía de una arquitectura, los sistemas de organización y los de etiquetado; un registro de biblioteca lista además sistemas de navegación y de búsqueda [S: https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/part02.html, https://libcat.library.tamu.edu/Record/in00004214380]. Los cuatro sistemas (organización, etiquetado, navegación, búsqueda) son la estructura clásica del libro; su definición literal de "arquitectura de información" no pude leerla (hueco).
- Card sorting: método en el que "study participants place individually labeled cards into groups according to criteria that make the most sense to them" [L: https://www.nngroup.com/articles/card-sorting-definition/].
- Tree testing: método para comprobar una jerarquía de navegación propuesta pidiendo a usuarios que encuentren dónde estaría un recurso dentro de categorías anidadas (paráfrasis del resumen de la página) [L: https://www.nngroup.com/articles/tree-testing/].
- Diferencia con interacción (síntesis propia, no hay una fuente que la formule así): AI decide cómo se agrupa, se llama y se encuentra el contenido (estructura y vocabulario); interacción decide cómo se opera (controles, estados, respuesta). Marcar como síntesis en la nota.

### Recurso canónico

Rosenfeld, Morville y Arango, 4.ª ed.: capítulos de sistemas de organización y de etiquetado (ch. 5-7 según el índice de O'Reilly, a verificar). Fijarse en: esquemas de organización exactos vs ambiguos, y el etiquetado como lenguaje del usuario, no de la empresa.

## 2. navegacion

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Pernice y Budiu, NN/g, "Hamburger Menus and Hidden Navigation Hurt UX Metrics", 26 jun 2016. https://www.nngroup.com/articles/hamburger-menus/ | secundaria fuerte, con estudio cuantitativo | 2/3/2/3 | [L] |
| Nielsen y Li, NN/g, "Mega Menus Work Well for Site Navigation", 26 mar 2017. https://www.nngroup.com/articles/mega-menus-work-well/ | secundaria fuerte | 2/2/2/2 | [L] |
| Laubheimer, NN/g, "Breadcrumbs: 11 Design Guidelines for Desktop and Mobile", 23 dic 2018 (rev. 2026). https://www.nngroup.com/articles/breadcrumbs/ | secundaria fuerte | 2/2/2/2 | [L] |
| Laubheimer, NN/g, "Local Navigation Is a Valuable Orientation and Wayfinding Aid", 4 jul 2021. https://www.nngroup.com/articles/local-navigation/ | secundaria fuerte | 2/1/1/2 | [L] |
| Budiu, NN/g, "Information Scent: How Users Decide Where to Go Next", 2 feb 2020. https://www.nngroup.com/articles/information-scent/ | secundaria fuerte | 2/2/2/1 | [L] |
| Fu y Pirolli, "SNIF-ACT: A Cognitive Model of User Navigation on the World Wide Web", *Human-Computer Interaction* 22, 2007, pp. 355-412. https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/25938.pdf | primaria (paper revisado por pares) | 3/3/1/2 | [L] parcial (abstract y sección de teoría; no todo el paper) |
| Pirolli y Card, "Information Foraging", *Psychological Review* 106(4), 1999, pp. 643-675, doi:10.1037/0033-295X.106.4.643 | primaria (paper original) | 3/3/1/3 | [S] (solo referencia bibliográfica y descripciones; no leí el texto) |

### Afirmaciones

- Tipos. Global: según NN/g, es el nivel superior de la jerarquía, estable en todo el sitio, para saltar entre categorías principales ("The global navigation is stable"). Local: "a type of navigation that is contextual to the user's current location"; muestra páginas pares y, si corresponde, subordinadas, y cambia por categoría pero no por usuario ni sesión [L: https://www.nngroup.com/articles/local-navigation/]. Contextual: el artículo no lo define aparte; usa "contextual" para describir la local y menciona enlaces contextuales a contenido relacionado como alternativa liviana en sitios profundos. Discrepancia terminológica: en NN/g "local" y "contextual" se solapan; en otras fuentes "contextual" son los enlaces dentro del contenido. Declarar cuál usa la base.
- Migas de pan: muestran dónde está una página en la estructura, no el recorrido: "Breadcrumbs are not intended to show the history of pages traversed during a session on the site." Útiles "especially useful when users arrive to the site through an external link and don't start with the homepage". Innecesarias en sitios planos (uno o dos niveles). El último ítem no es un enlace. Complementan, no reemplazan, la navegación global y local [L: https://www.nngroup.com/articles/breadcrumbs/].
- Hamburguesa y navegación oculta (NN/g, 26 jun 2016; 179 participantes reclutados con WhatUsersDo, 6 sitios reales, escritorio y celular, 2 tareas por sitio): uso de la navegación en escritorio 27 % oculta contra 48 % visible y 50 % combinada; en celular 57 % oculta y 86 % combinada. "Content discoverability" cae más de 20 % con navegación oculta frente a visible o combinada. Dificultad de tarea (1 a 7, menor es más fácil): 2,6 oculta, 2,3 combinada, 2,1 visible (21 % más difícil que visible). Tiempo de tarea en escritorio: al menos 39 % más con navegación oculta; en celular 15 % más que con la combinada [L: https://www.nngroup.com/articles/hamburger-menus/]. Límites: es un estudio de 2016, la visible pura no se probó en celular, y las convenciones del ícono pueden haber cambiado; no encontré evidencia más nueva comparable (hueco).
- Mega-menús (NN/g, Nielsen y Li, 26 mar 2017): funcionan bien si se cuidan: "the mouse should remain stationary for 0.5 seconds before you display anything that's hover-dependent"; si no, "the screen flicker insufferably". Fallo de la diagonal: el menú no debe cerrarse mientras el usuario apunta a algo dentro. En táctil, "tiny options inside mega menus cause selection errors". Con lupa o pantalla chica los usuarios "may assume that the visible content is all the content that is available". Agrupar con "a medium level of granularity", etiquetas concisas, "Show each choice only once"; no grupos enormes; opciones duplicadas hacen dudar si son lo mismo [L: https://www.nngroup.com/articles/mega-menus-work-well/].
- Information scent. Definición NN/g: el olor de una fuente respecto de una necesidad "represents the user's imperfect estimate of the value that the source will deliver to the user", derivada de una representación de la fuente. Guía: etiquetas específicas y autoexplicativas (evitar "More"), lenguaje del público, no depender del contexto circundante, etiqueta coherente con el destino (el clickbait erosiona confianza), y reforzar el enlace en la página de destino [L: https://www.nngroup.com/articles/information-scent/].
- Origen teórico: la teoría adapta la teoría del forrajeo óptimo a la búsqueda de información [S]. En SNIF-ACT el olor se calcula a partir de "proximal information scent cues" (las etiquetas de enlaces) para predecir la probabilidad de que una fuente distal contenga lo buscado; los usuarios evalúan enlaces en secuencia y deciden entre clic o volver con un modelo bayesiano de satisfacción [L: https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/25938.pdf]. Ojo: lo leído es el paper de 2007 que aplica la teoría; el de 1999 es [S].
- Facetas para catálogos: no conseguí una fuente leída (hueco; Baymard devolvió una página de marketing sin contenido).

### Recurso canónico

Fu y Pirolli (2007) para entender el olor como mecanismo; NN/g "Information Scent" (2020) para aplicarlo a etiquetas; NN/g "Hamburger Menus..." (2016) completo, mirando la tabla de uso por condición.

## 3. Interacción como vertical

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Cooper, Reimann, Cronin, Noessel, *About Face: The Essentials of Interaction Design*, 4.ª ed., Wiley, 2014 (fichas: https://www.infoq.com/news/2014/10/cooper-about-face-4, https://www.uxmatters.com/mt/archives/2014/11/about-face-the-essentials-of-interaction-design.php) | primaria (libro canónico) | 3/3/2/3 | [S] |
| Preece, Rogers, Sharp, *Interaction Design: Beyond Human-Computer Interaction* (https://oro.open.ac.uk/47656) | primaria (libro de texto) | 3/3/2/2 | [M] / [S] |
| Kaplan, NN/g, "Designing Empty States in Complex Applications", 19 sep 2021. https://www.nngroup.com/articles/empty-state-interface-design/ | secundaria fuerte | 2/1/2/2 | [L] |
| Flaherty, NN/g, "Indicators, Validations, and Notifications: Pick the Correct Communication Option", 17 ene 2024. https://www.nngroup.com/articles/indicators-validations-notifications/ | secundaria fuerte | 2/2/2/2 | [L] |

### Afirmaciones

- Qué es: Preece, Rogers y Sharp definen el diseño de interacción como diseñar productos interactivos "to support the way people communicate and interact in their everyday and working lives" (redacción de la 3.ª edición y del abstract de la 4.ª; la 1.ª edición lo decía distinto) [S: https://oro.open.ac.uk/47656]. Cooper presenta el diseño dirigido por metas como método válido en cualquier plataforma y dominio [S: resultados de buscador sobre la 4.ª ed.]; el índice incluye "Optimizing for Intermediates", "Perpetual Intermediates" y "Goal-Directed Tasks versus Excise Tasks" [S]. La cita literal de Cooper no la leí (hueco).
- Estado vacío: "Do not default to totally empty states"; explicar qué podría aparecer y cómo llenarlo, enlazar a los primeros pasos, mostrar progreso mientras procesa, y decir "no hay contenido" si terminó sin datos [L: https://www.nngroup.com/articles/empty-state-interface-design/].
- Estado de error: los mensajes de validación "should explain the fix, not just the problem"; "Field is blank" es peor que decir qué ingresar; los toasts son mala opción para errores (un usuario no vio el aviso y esperó cinco minutos) [L: https://www.nngroup.com/articles/indicators-validations-notifications/].
- Estado de carga: ese artículo no lo cubre; ver umbrales de tiempo en la sección 4.
- Microcopy: no hallé una fuente primaria leída; en lo leído, el texto de etiquetas y errores aparece como parte del olor (sección 2) y de los mensajes de error (arriba). Hueco.

### Recurso canónico

Preece/Rogers/Sharp cap. 1 para la definición y el proceso; Cooper cap. sobre excise y sobre intermedios para sistemas internos. Fijarse en: "excise" (trabajo que la interfaz impone y no ayuda a la meta).

## 4. principios-de-interaccion

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| ISO 9241-110:2020, *Ergonomics of human-system interaction, Part 110: Interaction principles*, 2.ª ed. Página: https://www.iso.org/standard/75258.html (403); muestra gratuita leída: https://cdn.standards.iteh.ai/samples/75258/83c8cf072187487686645aad04eff40e/ISO-9241-110-2020.pdf | primaria (norma) | 3/3/1/3 | [L] de la cláusula 4.1 y el índice (muestra de iTeh, copia pública de la norma); la página de ISO [M] |
| Norman, "Signifiers, not affordances", *Interactions* 15(6), 17 nov 2008. https://jnd.org/signifiers-not-affordances/ | primaria (autor) | 3/2/2/3 | [L] |
| Norman, *The Design of Everyday Things*, ed. revisada 2013 (fichas: https://jnd.org/the-design-of-everyday-things-revised-and-expanded/) | primaria (libro canónico) | 3/3/3/3 | [S] (la copia del capítulo 1 del MIT dio 404; el PDF completo no fue accesible) |
| Nielsen, "Response Times: The 3 Important Limits" (extracto del cap. 5 de *Usability Engineering*, 1993). https://www.nngroup.com/articles/response-times-3-important-limits/ | secundaria fuerte | 2/2/1/2 | [L] |
| Miller (1968), Card, Robertson y Mackinlay (1991), citados por Nielsen | primarias, no leídas | 3/-/-/- | [S] (solo la referencia) |

### Afirmaciones

- ISO 9241-110:2020 reemplazó los "principios de diálogo" de 2006 por "principios de interacción" y agregó "user engagement" [L: cláusula de prólogo de la muestra; S: https://www.iso.org/standard/75258.html]. Siete principios, literales (cláusula 4.1), "The order in which the principles are presented here does not imply any priority":
  1. Suitability for the user's tasks: "supports the users in the completion of their tasks, i.e. when the operating functions and the user-system interactions are based on the task characteristics (rather than the technology chosen to perform the task)".
  2. Self-descriptiveness: "presents appropriate information, where needed by the user, to make its capabilities and use immediately obvious to the user without unnecessary user-system interactions".
  3. Conformity with user expectations: "behaviour is predictable based on the context of use and commonly accepted conventions in this context".
  4. Learnability: "supports discovery of its capabilities and how to use them, allows exploration of the interactive system, minimizes the need for learning and provides support when learning is needed".
  5. Controllability: "allows the user to maintain control of the user interface and the interactions, including the speed and sequence and individualization of the user-system interaction".
  6. Use error robustness: "assists the user in avoiding errors and in case of identifiable errors treats them tolerantly and assists the user when recovering from errors".
  7. User engagement: "presents functions and information in an inviting and motivating manner supporting continued interaction with the system".
  Fuente de todas: la muestra de iTeh arriba [L]. Traducción al castellano de los nombres: la propia del equipo; no encontré versión oficial en castellano leída.
- Corrección de Norman (2008): afirma que cuando introdujo "affordance" al diseño en 1988 se refería a "perceivable affordances"; "Forget affordances: what people need, and what design must provide, are signifiers." Definición: "A 'signifier' is some sort of indicator, some signal in the physical or social world that can be interpreted meaningfully"; "I call any physically perceivable cue a signifier, whether it is incidental or deliberate." "The perceivable part of an affordance is a signifier" [L: https://jnd.org/signifiers-not-affordances/]. Gibson usaba affordance como "a relationship" entre agente y entorno [L, misma fuente]. En la edición 2013 del libro, signifier se agrega para aclarar la definición de affordance [S: https://en.wikipedia.org/wiki/The_Design_of_Everyday_Things, resumen del buscador].
- Mapeo, restricciones, feedback y modelo conceptual: no pude leer las definiciones literales del libro. Resúmenes de buscador atribuyen: "Signifiers signal things, in particular what actions are possible and how they should be done. Signifiers must be perceivable, else they fail to function"; "Poor feedback can be worse than no feedback at all"; "A conceptual model is an explanation, usually highly simplified, of how something works" [S, sin URL primaria; no usar como cita textual hasta verificar con el libro]. Estructura: principios fundamentales en el cap. 1; restricciones, descubribilidad y feedback en el cap. 4 [S: https://jnd.org/the-design-of-everyday-things-revised-and-expanded/].
- Umbrales de tiempo de respuesta (Nielsen, 1993, cap. 5 de *Usability Engineering*): "0.1 second is about the limit for having the user feel that the system is reacting instantaneously"; "1.0 second is about the limit for the user's flow of thought to stay uninterrupted"; "10 seconds is about the limit for keeping the user's attention focused on the dialogue." Cita a Miller (1968, *Proc. AFIPS Fall Joint Computer Conference*) y Card, Robertson y Mackinlay (1991, *Proc. ACM CHI'91*); dice que la guía "has been about the same for thirty years" [L: https://www.nngroup.com/articles/response-times-3-important-limits/]. Los límites son una guía de practicante de 1993 apoyada en trabajos de 1968 y 1991; no leí los originales.

### Recurso canónico

ISO 9241-110:2020, cláusula 4 y las recomendaciones por principio (cláusula 5; en la muestra el índice lista, p. ej., "clear indication of processing status" bajo self-descriptiveness y "trustworthiness of the system" bajo engagement). Norman: capítulo 1 del libro y el artículo de 2008 para la corrección affordance/signifier.

## 5. formularios

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Penzo, "Label Placement in Forms", UXmatters, 12 jul 2006. https://www.uxmatters.com/mt/archives/2006/07/label-placement-in-forms.php | secundaria (estudio de practicante, artesanal) | 1/2/2/3 | [L] (leído hasta el carácter 100000 de 104878) |
| Wroblewski, "Inline Validation in Web Forms", A List Apart, 1 sep 2009 (mismo contenido resumido en https://www.lukew.com/ff/entry.asp?883). https://alistapart.com/article/inline-validation-in-web-forms/ | secundaria (practicante, estudio de Etre) | 2/2/2/3 | [L] |
| Wroblewski, *Web Form Design: Filling in the Blanks*, Rosenfeld Media, 2008 | primaria (libro canónico) | 3/3/2/3 | [S] (sección "Label Alignment" p. 87 según índice; no leído) |
| Napier University, estudio de alineación de etiquetas (https://napier-repository.worktribe.com/OutputFile/232503) | primaria (académica) | ?/?/?/? | [S] (403; solo lo que reportó el buscador) |
| Baymard, "Checkout Flow Average Form Fields", 26 jun 2024. https://baymard.com/blog/checkout-flow-average-form-fields | secundaria fuerte (instituto con benchmark) | 2/2/1/2 | [L] |
| Baymard, "Cart Abandonment Rate Statistics". https://baymard.com/lists/cart-abandonment-rate | secundaria fuerte | 2/2/1/2 | [L] |
| Sherwin, NN/g, "Placeholders in Form Fields Are Harmful", 11 may 2014 (rev. 10 sep 2018). https://www.nngroup.com/articles/form-design-placeholders/ | secundaria fuerte | 2/2/2/2 | [L] |
| Cooper, *About Face* 4.ª ed., capítulo "Rethinking Data Entry, Storage, and Retrieval" | primaria | 3/?/?/? | [S] (solo índice) |

### Afirmaciones

- Etiquetas (Penzo, 2006; eye-tracking ad hoc, expertos y novatos, número de participantes no indicado en lo leído, páginas sin diseño visual): etiquetas a la izquierda alineadas a la izquierda, sacadas de unos 500 ms (el autor lo lee como carga cognitiva alta); alineadas a la derecha, fijaciones aproximadamente a la mitad y tiempo "casi a la mitad", sacadas de unos 170 ms (expertos) y 240 ms (novatos); etiquetas arriba, la mayoría de las fijaciones cae en los campos, sacadas de unos 50 ms. Conclusión: arriba suele funcionar mejor; si deben ir al costado, alineadas a la derecha. El autor lo describe como punto de partida, no respuesta final [L: https://www.uxmatters.com/mt/archives/2006/07/label-placement-in-forms.php]. Limitaciones declaradas: condiciones de laboratorio sin diseño visual, muestra sin cifra.
- Discrepancia: un estudio de Napier University halló que arriba y derecha quedaron cerca en velocidad (cinco participantes más rápidos con alineación a la derecha, cinco con la de arriba; diferencia de al menos 3 s, ~5 % del tiempo total) y sugiere que la brecha puede deberse al diseño de columnas [S: resumen de buscador sobre https://napier-repository.worktribe.com/OutputFile/232503; sin leer]. Las diapositivas de Wroblewski dicen cosas como "diez veces más rápido" o "casi a la mitad" sin aclarar la comparación [S: https://static.lukew.com/WebForms_LukeW_101209.pdf]; no citar esas cifras.
- Validación en línea (Wroblewski con Etre, 1 sep 2009; 22 usuarios de 21 a 49 años, seis variantes de un formulario de registro, orden aleatorio; control: validar solo al hacer clic en "crear cuenta"): la mejor variante contra el control dio éxito +22 %, errores -22 %, satisfacción +31 %, tiempo de completado -42 %, fijaciones oculares -47 %. Salvedades: en preguntas obvias (nombre) solo 30 %-50 % notó los mensajes y la marca verde confundió; validar mientras se escribe empeoró tiempo, errores y satisfacción; los mensajes de éxito que se desvanecen se pierden [L: https://alistapart.com/article/inline-validation-in-web-forms/]. Con 22 personas, las cifras son indicativas, no estimaciones estables.
- Cantidad de campos en checkout (Baymard, 26 jun 2024): "the average in 2024 was 11.3 form fields"; "most sites need only 8 form fields in total for a checkout flow"; "17% of users have abandoned due to checkout complexity" (cita su estudio premium GC050; tamaño de muestra no indicado en la página) [L: https://baymard.com/blog/checkout-flow-average-form-fields]. Una búsqueda sobre otras páginas de Baymard da la serie 12,7 (2019), 11,8 (2021), 11,3 (2024) [S].
- Discrepancia en la cifra de abandono: la misma página de Baymard da 17 %; el buscador reportó otra página con 22 % y un artículo de 2019 con 26 % ("too long or too complex") [S: https://baymard.com/blog/checkout-flow-average-form-fields y páginas relacionadas]. Dar las tres con fecha, no elegir una; la más reciente leída es 17 %.
- Contexto de abandono (Baymard, "unweighted average of 50 studies published 2006–2025", promedio 70,22 %): razones (sin contar "solo estaba mirando"): costos extra 40 %; entrega lenta 20 %; no confió en la tarjeta 19 %; pedían crear cuenta 18 %; "Too long / complicated checkout process" 17 %; errores del sitio 17 %; devoluciones 13 %; no ver el total 12 %; tarjeta rechazada 10 %; pocos medios de pago 9 %. Muestra y fecha de la encuesta de razones no están en la página [L: https://baymard.com/lists/cart-abandonment-rate]. Nota: la página muestra "Oct 28, 2026" como fecha de publicación, no de encuesta.
- Placeholders (NN/g, Sherwin, 2014, rev. 2018): "makes it difficult for people to remember what information belongs in a field"; siete problemas (memoria, no permite revisar, difícil recuperarse de errores, fricción con tabulador, campos llenos menos notables según eye-tracking, se leen como dato precargado, trabajo de borrarlos); además bajo contraste y algunos lectores de pantalla no los anuncian. Recomendación: no usarlos como reemplazo de etiquetas; etiquetas visibles fuera del campo; pistas persistentes fuera del campo; los placeholders solo para ejemplos complementarios; las etiquetas flotantes son mejores que etiqueta-como-placeholder pero peores que fuera del campo [L: https://www.nngroup.com/articles/form-design-placeholders/].
- Formularios en sistemas internos (Cooper): no hallé el pasaje; solo el índice del libro (capítulo de entrada, almacenamiento y recuperación de datos; "excise") [S]. Hueco.

### Recurso canónico

Wroblewski, *Web Form Design* (etiquetas, acciones, ayuda, validación) como libro de referencia, con "Inline Validation in Web Forms" (2009) para la evidencia; Baymard "Checkout Flow Average Form Fields" para checkout. Fijarse en: n de cada estudio y que Penzo y Etre son estudios chicos de 2006 y 2009.

## 6. Huecos

1. Definición literal de "arquitectura de información" y de los cuatro sistemas en Rosenfeld/Morville/Arango: el sitio de O'Reilly dio 403. Hace falta el libro o una vista previa.
2. Pirolli y Card (1999) no se leyó; solo se leyó un paper que lo aplica (Fu y Pirolli, 2007). Falta el abstract oficial (APA PsycNet/DOI).
3. Las definiciones literales de Norman (2013) de mapeo, restricción, feedback y modelo conceptual; los resúmenes de buscador no sirven como cita. Falta el texto del capítulo 1 y 4 (las copias públicas dieron 404/no accesible).
4. Facetas para catálogos: ninguna fuente leída (Baymard dio página vacía). Prioridad por la plataforma de tiendas.
5. Evidencia posterior a 2016 sobre hamburguesa; evidencia sobre mega-menús más allá de las guías de NN/g (no hay cifras en lo leído).
6. Miller (1968) y Card et al. (1991) en original; el estudio de Napier sin leer (403); Penzo sin n de participantes en lo leído.
7. Cooper: citas literales de diseño de interacción, "excise" y sistemas internos; no hay fuente leída sobre formularios en sistemas internos.
8. Microcopy: sin fuente primaria; estado de carga: sin fuente más allá de los umbrales de tiempo.
9. ISO 9241-110: solo la cláusula 4.1 literal; las recomendaciones por principio (cláusula 5) no se leyeron en detalle; la página de ISO dio 403 y no hay versión oficial en castellano leída.
10. Baymard: muestra, fecha de la encuesta y metodología de las cifras 17 %/22 %/26 % y de la serie de campos; el texto está tras muro premium.
