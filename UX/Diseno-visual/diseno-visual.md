---
resumen: >-
  El diseño visual es la capa de superficie de la experiencia: lo que la persona ve, con su jerarquía, tipografía, color y grilla. Condiciona cuánto parece usable un producto, pero no arregla un problema de estructura, de interacción o de estrategia.
estado: borrador
estabilidad: estable
fuentes:
  - "Jesse James Garrett, The Elements of User Experience (2.ª ed., 2010), cap. 2 y capítulo del plano de superficie; leído solo por resúmenes de cátedra: https://mason.gmu.edu/~gprimera/375/module5-page2.html"
  - "Interaction Design Foundation, Gestalt principles: https://ixdf.org/literature/topics/gestalt-principles"
  - "Baymard Institute, Line length readability: https://baymard.com/blog/line-length-readability"
  - "Robert Bringhurst, The Elements of Typographic Style, según https://webtypography.net/2.1.2 (leído en tercera mano)"
  - "Dyson y Haselgrove (2001), Int. J. Human-Computer Studies 54, 585-612 (solo resumen secundario)"
  - "W3C, Understanding WCAG 1.4.3 Contrast (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html"
  - "Kurosu y Kashimura (1995), CHI '95, vía https://www.nngroup.com/articles/aesthetic-usability-effect/"
  - "Tractinsky, Katz e Ikar (2000), Interacting with Computers 13(2), 127-145 (abstract): https://academic.oup.com/iwc/article-abstract/13/2/127/898608"
  - "Lindgaard, Fernandes, Dudek y Brown (2006), Behaviour & Information Technology 25(2), 115-126 (solo metadatos): https://api.crossref.org/works/10.1080/01449290500330448"
  - "UX/.investigacion/diseno-visual-y-accesibilidad.md"
  - "UX/.investigacion/posicion-contraria.md"
aliases: [UI, diseño de interfaces, diseño gráfico de interfaces, plano de superficie]
creado: 2026-11-22
revisado:
---

# Diseño visual

El diseño visual es la capa de superficie de la experiencia: lo que la persona ve, con su jerarquía, tipografía, color y grilla. Condiciona cuánto parece usable un producto, pero no arregla un problema de estructura, de interacción o de estrategia.

Es lo que suele llamarse interfaz (UI) en el uso corriente, y la última de las capas de [UX](../ux.md): recibe la estructura de la [arquitectura de información](../Arquitectura-de-informacion/arquitectura-de-informacion.md) y los controles de la [interacción](../Interaccion/interaccion.md), y los vuelve visibles. Comparte con [Accesibilidad](../Accesibilidad/accesibilidad.md) varias decisiones: el contraste, el tamaño de los objetivos y el largo de línea son a la vez elecciones visuales y criterios verificables de [WCAG](../Accesibilidad/wcag.md).

## La superficie depende de los planos de abajo

Garrett ordena la experiencia en cinco planos: estrategia, alcance, estructura, esqueleto y superficie. La superficie es, en su definición, "the outer elements of the site that the user sees and can sometimes interact with": identidad visual, color, tipografía e imágenes. Los resúmenes de cátedra que se leyeron (no el libro) señalan que los planos van de lo concreto a lo abstracto y que Garrett recomienda empezar por la estrategia.

La consecuencia práctica es que un rediseño visual no corrige un menú mal organizado ni un flujo que pide datos de más. Tampoco es sinónimo de UX: [Qué es UX](../Fundamentos/que-es-ux.md) y [Mitos de UX](../Fundamentos/mitos-de-ux.md) tratan esa distinción, y el árbol del tema la apoya en que la norma ISO 9241-210 trata la experiencia de uso y no la apariencia.

> [!NOTE] Sin fuente todavía: una referencia que estudie el mito "UX es diseño visual" como tal. Lo que sostiene esta sección es el modelo de Garrett, leído por resúmenes, y la definición de ISO que cita [UX](../ux.md).

La identidad de marca (logotipo, tono, capital de marca) es de otro tema: la define [Marca](../../Marketing/Marca/marca.md) en Marketing. El diseño visual de un producto la aplica a pantallas. Según esta base (inferencia, sin fuente), decide además cosas que la marca no cubre, como la jerarquía de una tabla o el estado de un botón.

## Gestalt: cómo agrupa el ojo antes de leer

Las leyes de la Gestalt nacen con Max Wertheimer en los años veinte y las refinaron Köhler (1929), Koffka (1935) y Metzger (1936). La Interaction Design Foundation las resume y las aplica a interfaces. La tabla recoge seis de sus principios; la columna de usos son ejemplos de esta base, no de esa fuente.

| Principio | Qué agrupa | Uso en una interfaz |
|---|---|---|
| Proximidad | Lo que está más cerca | Separar un grupo de campos de otro con espacio |
| Similitud | Lo que comparte rasgos superficiales | Todos los enlaces con el mismo estilo |
| Región común | Lo que está dentro de un mismo borde | Tarjetas y paneles |
| Continuidad | Lo que sigue una trayectoria | Alinear elementos para que se lean como fila |
| Cierre | Formas incompletas que se completan | Íconos y logotipos con trazos abiertos |
| Figura y fondo | El primer plano se ve primero | Un modal sobre un fondo atenuado |

Estos principios pertenecen a la percepción: la base científica está en [Percepción y decisión](../Percepcion-y-decision/percepcion-y-decision.md), y su aplicación al orden de lectura en [Jerarquía visual](jerarquia-visual.md).

## Tipografía: el largo de línea tiene convención, no ley

Baymard recomienda para texto corrido de 50 a 75 caracteres por línea, cita a Emil Ruder (50 a 60) y recuerda que WCAG 1.4.8 pide 80 o menos (40 en chino, japonés y coreano). En sus pruebas, las líneas de más de 100 caracteres fatigaban a los lectores. Bringhurst da 45 a 75 para una columna, con 66 como ideal, y 40 a 50 para varias columnas (cifras leídas en una reproducción web, no en el libro).

Estos rangos vienen de la imprenta. La evidencia con pantallas es más limitada. Según un resumen secundario, Dyson y Haselgrove (2001) hallaron que una línea de unos 55 caracteres parecía sostener la lectura efectiva a velocidad normal y rápida, y el trabajo señala que el resultado depende de la tarea (lectura veloz o exacta). No se leyó el artículo. Conviene tratar el rango como punto de partida y comprobarlo con la tarea real.

## Color y contraste: la regla verificable

WCAG 1.4.3 (nivel AA) exige una relación de contraste de al menos 4,5 a 1 para texto, y 3 a 1 para texto grande (18 pt, o 14 pt en negrita). El documento Understanding explica el origen: el 3 a 1 viene de las normas ISO 9241-3 y ANSI-HFES-100-1988, y el 4,5 es 3 multiplicado por 1,5, por la pérdida de sensibilidad al contraste de "roughly 1.5" que acompaña a una visión 20/40, típica hacia los 80 años. Según WebAIM, el contraste insuficiente es la falla más frecuente en las páginas de inicio, en una detección automática (ver [Accesibilidad](../Accesibilidad/accesibilidad.md)).

## Lo atractivo parece más usable, con límites

Según NN/g, Kurosu y Kashimura (1995) probaron 26 variantes de una interfaz de cajero con 252 participantes, y el atractivo correlacionó más con la facilidad de uso percibida que con la real. No se leyó el paper original. Tractinsky, Katz e Ikar (2000) lo replicaron en otro contexto cultural; según su abstract, la correlación entre estética y usabilidad percibidas se mantuvo tras el uso, mientras que la usabilidad real no tuvo ese efecto. Según Monk y Lelos (visto en un resultado de buscador), la crítica al original es que los participantes no usaron los productos.

Los límites los fija NN/g: lo atractivo perdona problemas menores, no mayores, y puede ocultar fallas en un [test de usabilidad](../Evaluacion/test-de-usabilidad.md), porque los participantes elogian después de tropezar.

Sobre la primera impresión, Lindgaard y colaboradores (2006) concluyeron, según un resumen secundario, que el atractivo visual de una página de inicio se puede evaluar en 50 milisegundos: en tres estudios, los juicios a 50 ms correlacionaron fuerte con los de 500 ms. Se midió el atractivo, no la usabilidad ni la conversión. Circula una correlación de r = .97 que no se pudo confirmar contra el original, así que no se usa.

## Qué hay adentro

- [Jerarquía visual](jerarquia-visual.md): cómo se guía el ojo por la página, con los patrones de lectura en F y sus correcciones.
- [Sistema de diseño](sistema-de-diseno.md): componentes, tokens de diseño y gobierno que hacen repetible el diseño visual.

## Qué falta

El [alcance](../ALCANCE.md) prevé sumar notas sobre tipografía (escalas, interlineado, elección de familias), color (paletas, modos claro y oscuro, significado), grilla y espaciado, e iconografía. Hoy solo se tocan en esta entrada, la grilla sin fuente leída.
