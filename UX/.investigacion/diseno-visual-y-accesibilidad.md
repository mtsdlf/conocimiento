# Investigación: Diseño visual y Accesibilidad

Fecha de la investigación: 2026-11-22. Marcas: [L] leído el texto o la sección; [M] metadatos o abstract; [S] resumen secundario o del buscador. Puntajes 1-3 (A = autoridad, P = profundidad, E = ejemplos, U = unicidad). Todo lo que se leyó pasó por WebFetch (un modelo chico resume la página), así que las citas literales son las que devolvió la herramienta; donde la herramienta limitó la cita lo digo.

## Sobre la división del árbol

El árbol (Diseno-visual con jerarquia-visual y sistema-de-diseno; Accesibilidad con wcag) funciona, con tres observaciones:

- El campo no separa "diseño visual" de "accesibilidad" tan limpio: el contraste, el tamaño de objetivo y el largo de línea son a la vez decisiones visuales y criterios de WCAG (1.4.3, 2.5.8, 1.4.8). Conviene que cada nota diga en qué vertical vive el criterio y enlace a la otra.
- La parte legal (EAA, ADA, Ley 26.653) no cabe en `wcag` sin inflarla. Propuesta: una nota propia dentro de Accesibilidad (por ejemplo `marco-legal-de-accesibilidad`), o una sección de `wcag` si se quiere mantener el árbol. Decisión del dueño del árbol.
- Los patrones de lectura en F y los principios de Gestalt son percepción: quedan bien dentro de `jerarquia-visual`, con enlace a `Percepcion-y-decision`.

---

## 1. Diseño visual (vertical)

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 1.1 | Tractinsky, Katz e Ikar (2000), Interacting with Computers 13(2), 127-145 | https://academic.oup.com/iwc/article-abstract/13/2/127/898608 | primaria (paper) | 3 | 2 | 1 | 3 | [S] abstract reproducido por el buscador desde varias copias |
| 1.2 | Kurosu y Kashimura (1995), CHI '95, "Apparent usability vs. inherent usability" | https://chi1995.chistatic.hosting.acm.org/proceedings/shortppr/mk_bdy.htm | primaria (paper corto) | 3 | 1 | 1 | 3 | [S] solo resúmenes secundarios (no se leyó el paper) |
| 1.3 | NN/g, Aesthetic-Usability Effect | https://www.nngroup.com/articles/aesthetic-usability-effect/ | secundaria (instituto con método) | 2 | 2 | 2 | 1 | [L]  |
| 1.4 | Lindgaard, Fernandes, Dudek y Brown (2006), Behaviour & Information Technology 25(2), 115-126 | https://api.crossref.org/works/10.1080/01449290500330448 | primaria (paper) | 3 | 1 | 1 | 3 | [M] Crossref sin abstract; el abstract y el r viene de [S] |
| 1.5 | IxDF, Gestalt principles | https://ixdf.org/literature/topics/gestalt-principles | secundaria | 2 | 2 | 3 | 1 | [L] |
| 1.6 | Garrett, The Elements of User Experience (cinco planos) | https://www.oreilly.com/library/view/the-elements-of/9780321688651/ch02.html | primaria (libro) | 3 | 3 | 2 | 3 | [S] resúmenes secundarios; no se leyó el libro |
| 1.7 | Baymard, Line length readability | https://baymard.com/blog/line-length-readability | secundaria (instituto con método) | 2 | 2 | 2 | 2 | [L] |
| 1.8 | Bringhurst, The Elements of Typographic Style (p. 26 según Peña 2014) | https://webtypography.net/2.1.2 | primaria (libro), leído en terciaria | 3 | 3 | 2 | 3 | [S] |
| 1.9 | Dyson y Haselgrove (2001), Int. J. Human-Computer Studies 54, 585-612 | https://journals.uc.edu/index.php/vl/article/view/5671 (relacionado) / https://scite.ai/authors/mary-c-dyson-G3EwK6 | primaria (paper) | 3 | 2 | 1 | 3 | [S] |
| 1.10 | W3C, Understanding 1.4.3 Contrast (Minimum) | https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html | norma (documento Understanding) | 3 | 3 | 2 | 3 | [L] |

Nota 1.3: la lectura de la página de NN/g sobre el efecto estético-usabilidad fue exitosa; el paper de Kurosu y Kashimura se conoce solo por esa página y por resúmenes. Además, la URL de NN/g sobre Gestalt dio 404 y se sustituyó por IxDF (1.5).

### Afirmaciones

**Qué abarca (plano de superficie).** Garrett ordena la experiencia en cinco planos: estrategia, alcance, estructura, esqueleto y superficie; la superficie es "the outer elements of the site that the user sees and can sometimes interact with" e incluye identidad visual, color, tipografía, imágenes (https://mason.gmu.edu/~gprimera/375/module5-page2.html, [S], apunte universitario que resume a Garrett). Las fuentes secundarias notan que Garrett los lista de lo concreto a lo abstracto y recomienda empezar por la estrategia (https://mason.gmu.edu/~lroger13/507/module5-planes.html, [S]). Implicancia para el árbol: el diseño visual es la capa más superficial; arreglar la superficie no arregla un problema de estructura o estrategia.

**Gestalt aplicado a interfaces.** Origen: Max Wertheimer, años 1920; refinadas por Köhler (1929), Koffka (1935) y Metzger (1936) (https://ixdf.org/literature/topics/gestalt-principles). Definiciones literales de IxDF, mismo URL:
- Proximidad: "We group closer-together elements, separating them from those farther apart."
- Similitud: "When items, objects or elements share superficial characteristics, we perceive them as grouped."
- Región común: "We perceive elements that are in the same closed region as one group."
- Continuidad: "we group elements that seem to follow a continuous path in a particular direction."
- Cierre: "We prefer complete shapes, so we automatically fill the gaps between elements to perceive a complete image."
- Figura/fondo: "Unless an image is ambiguous—like Rubin's Vase above—we see its foreground first."
- Simetría y orden: "Humans tend to see visual elements as grouped when they are arranged symmetrically."

**Tipografía: largo de línea.**
- Baymard: "The optimal line length for body text is 50–75 characters"; cita a Emil Ruder (50-60); cita WCAG 1.4.8 ("80 or fewer characters", 40 para chino, japonés y coreano); en sus pruebas, los usuarios se fatigaban con líneas "extremely long lines of text (e.g., 100+ characters)" (https://baymard.com/blog/line-length-readability).
- Bringhurst: 45 a 75 caracteres para una columna en tipografía con serif y tamaño de texto, con 66 (contando espacios) como ideal; para varias columnas, 40 a 50 (https://webtypography.net/2.1.2, [S]; la cita de página 26 viene del paper de Peña 2014, referido en la misma búsqueda, sin URL verificada). Una lista de TeX dice 60-70 (https://www.tug.org/pipermail/texhax/2014-August/021304.html, [S]); discrepancia menor, se dan las dos.
- Evidencia empírica: Dyson y Haselgrove (2001) comparan largos de línea en pantalla; reportan que "a medium line length of 55 characters per line" parecía sostener la lectura efectiva a velocidad normal y rápida (resumen en https://scite.ai/authors/mary-c-dyson-G3EwK6, [S]; el abstract no se leyó en la fuente primaria). Importante: el rango 45-75 de Bringhurst es una convención de imprenta; la evidencia con pantalla es más limitada y la dependencia de la tarea es explícita en el propio paper (lectura veloz vs. exacta).

**Color y contraste.** WCAG 1.4.3 (AA): "The visual presentation of text and images of text has a contrast ratio of at least 4.5:1" (https://www.w3.org/TR/WCAG22/). El Understanding explica que 3:1 sale de ISO 9241-3 y ANSI-HFES-100-1988 y que 4.5:1 = 3 x 1,5, por una pérdida de sensibilidad al contraste de "roughly 1.5" asociada a visión 20/40, típica a los ~80 años; texto grande (18 pt, o 14 pt en negrita) necesita 3:1 (https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html). WebAIM: contraste insuficiente es la falla más frecuente (ver sección 5).

**Estética y usabilidad.**
- Kurosu y Kashimura (1995, Hitachi): 26 variantes de una interfaz de cajero, 252 participantes; el atractivo correlacionó más con la facilidad de uso percibida que con la real (https://www.nngroup.com/articles/aesthetic-usability-effect/, [L]; el paper original no se leyó).
- Tractinsky, Katz e Ikar (2000): experimento con una aplicación sustituta de cajero; "Pre-experimental measures indicate strong correlations between system's perceived aesthetics and perceived usability. Post-experimental measures indicated that the strong correlation remained intact."; la estética afectó las percepciones posteriores de estética y usabilidad "whereas the degree of actual usability had no such effect" (https://academic.oup.com/iwc/article-abstract/13/2/127/898608, [S]). Es una réplica en otro contexto cultural del estudio de Kurosu; Monk y Lelos señalan que la crítica al original es que los participantes no usaron los productos (https://www-users.york.ac.uk/~am1/HOIT07MonkLelos.pdf, [S] vía buscador).
- Límites según NN/g: lo atractivo perdona problemas menores, no mayores; puede ocultar problemas en un test porque los participantes elogian después de tropezar (https://www.nngroup.com/articles/aesthetic-usability-effect/).

**Primera impresión.** Lindgaard et al. (2006), BIT 25(2), 115-126: tres estudios; los juicios de atractivo visual de páginas de inicio expuestas 50 ms correlacionan fuerte con los de 500 ms; concluyen que el atractivo visual se puede evaluar en 50 ms (https://tandfonline.com/doi/abs/10.1080/01449290500330448, [S], el sitio dio 403; metadatos verificados en https://api.crossref.org/works/10.1080/01449290500330448 [M]). Una cifra citada, r = .97, no se pudo confirmar contra el original: no usar sin verificar. Ojo: es un juicio de atractivo, no de usabilidad ni de conversión.

### Recurso canónico

- Garrett, cap. 2 y el capítulo de la superficie (plano de superficie): qué decisiones son visuales y cuáles no. Fijarse en que la superficie depende de los cuatro planos de abajo.
- WCAG 1.4.3 y su Understanding, como regla práctica de contraste verificable.
- NN/g "Aesthetic-Usability Effect" por los límites; el paper de Tractinsky (2000) por el método.

---

## 2. jerarquia-visual

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 2.1 | NN/g, Visual Hierarchy in UX | https://www.nngroup.com/articles/visual-hierarchy-ux-definition/ | secundaria | 2 | 2 | 3 | 2 | [L] |
| 2.2 | NN/g, F-Shaped Pattern of Reading on the Web: Misunderstood, But Still Relevant (Even on Mobile), 2017, revisado ago. 2026 | https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/ | secundaria (estudio propio con eye-tracking) | 2 | 2 | 3 | 3 | [L] |
| 2.3 | NN/g, F-Shaped Pattern For Reading Web Content, 2006 | https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content-discovered/ | secundaria (estudio original) | 2 | 2 | 2 | 3 | [L] |
| 2.4 | IxDF, Gestalt (ver 1.5) | https://ixdf.org/literature/topics/gestalt-principles | secundaria | 2 | 2 | 3 | 1 | [L] |

Nota de URLs: las dos páginas de NN/g sobre la F se intercambiaron en la lectura: el slug `...-content/` contiene el artículo de 2017 (publicado 12 nov. 2017) y `...-content-discovered/` el de 2006. Lo que cito está atribuido a la página donde apareció.

### Afirmaciones

- Definición de NN/g: la jerarquía visual "refers to the organization of the design elements on the page" de modo que el ojo se guíe a cada elemento en el orden de importancia buscado (https://www.nngroup.com/articles/visual-hierarchy-ux-definition/).
- Cómo se arma (misma fuente): contraste con el contexto, no color solo ("Do not rely only on color to communicate visual hierarchy"); escala (no más de tres tamaños; como máximo dos elementos grandes); agrupamiento por proximidad, espacio en blanco y regiones comunes; "If everything is contrasted, then nothing stands out." (misma URL). Posición y alineación: la fuente no trata alineación; quedó como hueco, y se cubre con continuidad de Gestalt (sección 1).
- Cómo falla: tamaño, color y espaciado uniformes no dejan foco; el contenido puede pisar la plantilla (una foto muy coloreada domina); agrupar sin cuidado puede hacer que se ignore un bloque entero (ceguera a banners); el test de entrecerrar los ojos revela jerarquías no buscadas; hay que probarla con usuarios (misma URL).
- Patrón en F, 2006: tres movimientos: "Users first read in a horizontal movement, usually across the upper part of the content area", luego otro movimiento horizontal más corto, y "users scan the content's left side in a vertical movement" (https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content-discovered/ y 2017 en la otra URL). La página del 2017 dice que el patrón se identificó "in 2006", que "Our eyetracking study 11 years later confirmed these findings" (en la página de 2006) y que es "rarely a perfect F". Condición: "The F-pattern is the default pattern when there are no strong cues"; "The F-Shaped Pattern Is Not the Only Scanning Pattern"; el patrón es "bad for users and businesses" (https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/). La fuente da el número "more than 45 people" para un mapa de calor de ejemplo de principios de los 2000, no para el estudio 2006: tamaño de muestra del estudio de 2006 y del 2017 sin verificar. Otros patrones (capas, manchas, compromiso): nombrados en la literatura de NN/g; no se leyeron.
- Advertencia de evidencia: eye-tracking de NN/g es estudio de practicante, no revisado por pares. Marcar como "pista fuerte, no ley".

### Recurso canónico
NN/g "Visual Hierarchy in UX" (principios y fallas) y la versión 2017 del artículo de la F (leer el apartado "no es el único patrón"). Fijarse en que la F es lo que pasa cuando el diseño no guía.

---

## 3. sistema-de-diseno

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 3.1 | NN/g, Design Systems 101 | https://www.nngroup.com/articles/design-systems-101/ | secundaria | 2 | 2 | 2 | 2 | [L] |
| 3.2 | Frost, Atomic Design (2016), cap. 2 | https://atomicdesign.bradfrost.com/chapter-2/ | primaria (libro, edición del autor) | 3 | 3 | 3 | 3 | [L] |
| 3.3 | Design Tokens Community Group, Format Module 2025.10 | https://www.designtokens.org/tr/2025.10/format/ | primaria (especificación de grupo comunitario) | 2 | 3 | 2 | 3 | [L] (primeros 100.000 caracteres) |
| 3.4 | designtokens.org (portada) | https://www.designtokens.org/ | primaria | 2 | 1 | 1 | 2 | [L] |
| 3.5 | GOV.UK Design System | https://design-system.service.gov.uk/ | guía de plataforma (ejemplo de práctica) | 2 | 2 | 3 | 2 | [L] |
| 3.6 | IBM Carbon, What is Carbon | https://carbondesignsystem.com/all-about-carbon/what-is-carbon/ | guía de plataforma (ejemplo) | 2 | 1 | 2 | 1 | [L] |
| 3.7 | Sparkbox, Design Systems Survey (2018-2022) | https://sparkbox.com/foundry/2022_design_systems_survey | secundaria (encuesta de agencia) | 1 | 2 | 1 | 2 | [S] (resumen del buscador) |
| 3.8 | zeroheight, Design System Report 2025 | https://othr.zeroheight.com/hubfs/zeroheight%20-%20Design%20System%20Report%202025%20-%20release%20version.pdf | secundaria (vendor) | 1 | 2 | 1 | 2 | [S] |

Material Design no se leyó en esta ronda (hueco).

### Afirmaciones

- Definición NN/g: "A design system is a complete set of standards intended to manage design at scale using reusable components and patterns." Beneficios: "The primary benefit of design systems is their ability to replicate designs quickly"; lenguaje común; consistencia; onboarding (https://www.nngroup.com/articles/design-systems-101/).
- Costo y cuándo conviene (misma URL): "Creating and maintaining a design system is a time-intensive activity which requires a dedicated team"; adoptar uno existente es lo más barato; "Design systems are best when the company foresees years of future, replicable design work"; para una prueba de concepto o prototipo que va a cambiar, "a full system often won't pay off" en el corto plazo (paráfrasis de la fuente).
- Cómo falla (misma URL): "When poorly implemented and maintained, design systems can become unwieldly collections of components and code"; uso inconsistente sin instrucciones; acumulación de entradas viejas; sin patrocinante ejecutivo cuesta conseguir recursos.
- Atomic Design (Frost, 2016): "Atomic design is a methodology composed of five distinct stages": átomos, moléculas, organismos, plantillas y páginas; es un modelo mental, no una secuencia estricta (https://atomicdesign.bradfrost.com/chapter-2/).
- Tokens: la especificación "describes the technical specification for a file format to exchange design tokens between different tools"; estado: Final Community Group Report, 28 de octubre de 2025, versión 2025.10 (https://www.designtokens.org/tr/2025.10/format/). La portada anuncia "First stable version 2025.10" y llama al grupo "Design Tokens W3C Community Group" (https://www.designtokens.org/). Un Community Group no es un órgano de estándares del W3C: no es una Recomendación del W3C. Esa lectura es de la herramienta y de mi conocimiento del proceso del W3C; el texto de la especificación sobre su propio estatus no se leyó completo.
- Ejemplos públicos como práctica, no evidencia: GOV.UK, "for everyone that works on government services", mantenido por Government Digital Service, para evitar "repeating work that's already been done" (https://design-system.service.gov.uk/); Carbon: "Carbon is IBM's open-source design system for products and digital experiences" (https://carbondesignsystem.com/all-about-carbon/what-is-carbon/).
- Evidencia empírica: no se encontró un estudio revisado por pares que cuantifique el retorno de un sistema de diseño ni tasas de fracaso. Lo que hay son encuestas autoseleccionadas o de proveedores: Sparkbox 2018 (86 respondientes con sistema; algo más del 25% dijo "average" o "unsuccessful"; falta de patrocinante como causa), 2019 (éxito más probable con equipo dedicado), 2020 (la adopción es el desafío principal; 41% de los internos mide la adopción) (https://designsystemssurvey.sparkbox.com/2018, https://designsystemsurvey.sparkbox.com/2020, [S]). Estudio de Forrester encargado por Adobe (patrocinado, causalidad no verificada) (https://blog.adobe.com/en/publish/2020/09/29/unlocking-designs-full-business-potential, [S]); un trabajo de máster en Aalto, caso de una sola empresa (https://aaltodoc.aalto.fi/server/api/core/bitstreams/912148c0-b551-41bc-bd35-43d8c8057935/content, [S]).

### Recurso canónico
Frost, Atomic Design, caps. 1-2 (gratis en línea) para el vocabulario; NN/g Design Systems 101 para costo y gobierno; GOV.UK Design System como ejemplo de sistema con gobierno y contribución abiertos (fijarse en cómo documenta cada componente con investigación y uso).

---

## 4. Accesibilidad (vertical)

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 4.1 | OMS, Disability (hoja informativa) | https://www.who.int/news-room/fact-sheets/detail/disability-and-health | primaria (organismo) | 3 | 2 | 1 | 3 | [L] |
| 4.2 | Microsoft Inclusive Design | https://inclusive.microsoft.design/ | guía de empresa (ejemplo de práctica) | 2 | 1 | 1 | 2 | [L] (la página no trae el espectro de personas) |

### Afirmaciones
- OMS: "An estimated 1.3 billion people – or 16% of the global population – experience a significant disability today." Hoja informativa del 7 de marzo de 2023 (https://www.who.int/news-room/fact-sheets/detail/disability-and-health). La fecha es la de la versión leída; chequear si hay una versión más nueva.
- Microsoft Inclusive Design: tres principios: "Recognize exclusion", "Learn from diversity" y "Solve for one, extend to many" ("Creating products for people with permanent disabilities creates results that benefit everyone.") (https://inclusive.microsoft.design/). El espectro permanente, temporal y situacional (ejemplo clásico: un brazo; una lesión de brazo; cargar un bebé) es parte del toolkit de Microsoft, pero NO se pudo leer en esta ronda: sin URL verificada, hueco.
- Tecnologías de apoyo: sin fuente leída. Hueco (lectores de pantalla, ampliadores, control por voz o conmutador; ver Understanding de WCAG y WebAIM).

### Recurso canónico
Pendiente: el toolkit "Inclusive 101" de Microsoft (PDF) para el espectro; no verificado. Mientras, la hoja de la OMS para la cifra.

---

## 5. wcag

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 5.1 | W3C, WCAG 2.2 (Recomendación) | https://www.w3.org/TR/WCAG22/ | norma | 3 | 3 | 2 | 3 | [L] parcial (caracteres 0-200.000 de ~270.000; incluye 1.4.3, 2.1.1, 2.5.8; no se leyó la sección de conformidad) |
| 5.2 | W3C WAI, What's New in WCAG 2.2 | https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/ | norma (documento de apoyo) | 3 | 2 | 2 | 2 | [L] |
| 5.3 | W3C WAI, WCAG 2 Overview | https://www.w3.org/WAI/standards-guidelines/wcag/ | norma (documento de apoyo) | 3 | 1 | 1 | 2 | [L] |
| 5.4 | W3C WAI, WCAG 2 at a Glance | https://www.w3.org/WAI/standards-guidelines/wcag/glance/ | norma (apoyo) | 3 | 1 | 2 | 1 | [L] |
| 5.5 | W3C, Understanding Conformance | https://www.w3.org/WAI/WCAG22/Understanding/conformance | norma (Understanding) | 3 | 2 | 1 | 3 | [L] |
| 5.6 | W3C, WCAG 3.0 (Working Draft) | https://www.w3.org/TR/wcag-3.0/ | norma en borrador | 3 | 2 | 1 | 3 | [L] (primeros 100.000 caracteres) |
| 5.7 | WebAIM Million | https://webaim.org/projects/million/ | secundaria (instituto con método, análisis automático) | 2 | 2 | 2 | 3 | [L] |

### Afirmaciones
- Fechas: WCAG 2.2 "was published on 5 October 2023, and an update was published on 12 December 2024" (https://www.w3.org/WAI/standards-guidelines/wcag/). La versión vigente en /TR/ lleva el encabezado "W3C Recommendation, 12 December 2024" (https://www.w3.org/TR/WCAG22/). Son dos fechas, las dos correctas: la Recomendación original y su republicación con correcciones.
- Qué agregó respecto de 2.1 (https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/): "9 additional success criteria": 2.4.11 Focus Not Obscured (Minimum) AA; 2.4.12 Focus Not Obscured (Enhanced) AAA; 2.4.13 Focus Appearance AAA; 2.5.7 Dragging Movements AA; 2.5.8 Target Size (Minimum) AA; 3.2.6 Consistent Help A; 3.3.7 Redundant Entry A; 3.3.8 Accessible Authentication (Minimum) AA; 3.3.9 Accessible Authentication (Enhanced) AAA. Y: "4.1.1 Parsing is obsolete and removed from WCAG 2.2."
- Cantidad de criterios: 86 NO figura en las páginas del W3C que se leyeron; se obtiene como 78 (WCAG 2.1) + 9 - 1 = 86, y una guía de terceros lo dice (https://www.accessibilitychecker.org/guides/wcag-2-2/, [S]). El W3C da 13 pautas bajo los cuatro principios (https://www.w3.org/WAI/standards-guidelines/wcag/). Los conteos por nivel difieren entre sitios de terceros (por ejemplo 30 o 31 en A): no usarlos sin contar contra la norma.
- POUR literales: "perceivable, operable, understandable, and robust" (https://www.w3.org/TR/WCAG22/ y https://www.w3.org/WAI/standards-guidelines/wcag/). Primera pauta de cada uno: "Provide text alternatives for non-text content."; "Make all functionality available from a keyboard."; "Make text readable and understandable."; "Maximize compatibility with current and future user tools." (https://www.w3.org/WAI/standards-guidelines/wcag/glance/).
- Niveles: A es el mínimo; AA exige todos los A y AA; AAA exige todos (https://www.w3.org/WAI/WCAG22/Understanding/conformance). Cita sobre AAA: "It is not recommended that Level AAA conformance be required as a general policy for entire sites" "because it is not possible to satisfy all Level AAA success criteria for some content." (misma URL; la herramienta devolvió la cita en dos fragmentos). Por qué AA es el objetivo habitual: no hay cita del W3C que lo diga así; es una inferencia (las leyes de las secciones siguientes lo fijan en AA, y el W3C desaconseja exigir AAA).
- Criterios clave (https://www.w3.org/TR/WCAG22/): 1.4.3 (AA): "The visual presentation of text and images of text has a contrast ratio of at least 4.5:1, except for the following:" (texto grande 3:1, texto incidental, logotipos). 2.1.1 (A): "All functionality of the content is operable through a keyboard interface" (con una excepción para entrada que depende del trazado). 2.5.8 (AA): "The size of the target for pointer inputs is at least 24 by 24 CSS pixels, except when:" con excepciones de espaciado, equivalente, en línea, controlado por el agente de usuario y esencial.
- WCAG 3.0: "W3C Working Draft, 10 September 2026"; "This is a draft document and may be updated, replaced, or obsoleted by other documents at any time."; "WCAG 3 does not replace WCAG 2." (https://www.w3.org/TR/wcag-3.0/). Antes llamada "Silver" (https://www.w3.org/WAI/standards-guidelines/wcag/). Es decir, sigue en borrador y WCAG 2.x es lo que se exige.
- Prevalencia en sitios: WebAIM Million, análisis de febrero de 2026, 1.000.000 de páginas de inicio: 95,9% con fallas WCAG 2 detectables; 56,1 errores detectados por página en promedio; contraste insuficiente 83,9%; texto alternativo faltante en imágenes 53,1%; etiquetas de formulario faltantes 51%; enlaces vacíos 46,3%; botones vacíos 30,6%; idioma del documento faltante 13,5% (https://webaim.org/projects/million/). Es una detección automática: subestima las fallas reales, y mide la página de inicio.

### Recurso canónico
La norma WCAG 2.2 en https://www.w3.org/TR/WCAG22/ y, para cada criterio, su documento Understanding (qué parte: Intent, Benefits, Techniques). Para empezar leer 1.4.3, 2.1.1, 2.5.8, 3.3.x. WebAIM Million para el estado real.

---

## 6. Lo legal (riesgo alto: ley)

Regla: dos fuentes independientes o se declara que hay una. Abajo, por cada norma.

### Fuentes

| # | Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|---|
| 6.1 | Directiva (UE) 2019/882, EUR-Lex | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L0882 y https://eur-lex.europa.eu/eli/dir/2019/882/oj/eng | primaria (norma) | 3 | 3 | 1 | 3 | [L] parcial (Arts. 2, 3, 4, 31, 32, 14, 15 leídos por tramos) |
| 6.2 | Comisión Europea, European Accessibility Act | https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en | primaria (institución) | 3 | 1 | 2 | 1 | [L] |
| 6.3 | Comisión Europea, Web accessibility policy (EN 301 549) | https://digital-strategy.ec.europa.eu/en/policies/web-accessibility | primaria (institución) | 3 | 1 | 1 | 1 | [L] |
| 6.4 | ADA.gov, Web Rule First Steps | https://www.ada.gov/resources/web-rule-first-steps/ | primaria (gobierno de EE. UU.) | 3 | 2 | 1 | 3 | [L] |
| 6.5 | Ley 26.653, texto en argentina.gob.ar | https://www.argentina.gob.ar/normativa/nacional/175694/texto | primaria (norma) | 3 | 3 | 1 | 3 | [L] (la herramienta limitó las citas literales a fragmentos y resumió el resto) |
| 6.6 | Disposición ONTI 6/2019 | https://www.argentina.gob.ar/normativa/nacional/329284/texto | primaria (norma) | 3 | 2 | 1 | 3 | [L] (sin los anexos) |
| 6.7 | W3C WAI, Policies: Argentina | https://www.w3.org/wai/policies/argentina | secundaria (catálogo del W3C) | 2 | 1 | 1 | 1 | [L] |
| 6.8 | Decreto 656/2019 | https://www.argentina.gob.ar/normativa/nacional/decreto-656-2019-328722/texto | primaria (norma) | 3 | 3 | 1 | 3 | NO leído (HTTP 500); datos solo de [S] del buscador |

### European Accessibility Act (Directiva 2019/882)
- Aplica "to the following services provided to consumers after 28 June 2025", entre ellos "e-commerce services" (art. 2(2)(f)) y "consumer banking services" (art. 2(2)(d)) (https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L0882). Los Estados miembro debían aplicar sus medidas nacionales "from 28 June 2025" (art. 31(2)) y "Service contracts agreed before 28 June 2025 may continue without alteration until they expire" (art. 32) (https://eur-lex.europa.eu/eli/dir/2019/882/oj/eng; la herramienta numeró esos artículos 31 y 32, no 32 como se supone en el encargo: corregido).
- Art. 4(5): "Microenterprises providing services shall be exempt from complying with the accessibility requirements" del apartado 3; microempresa: menos de 10 personas y facturación anual o balance que no supere EUR 2 millones (art. 3(23), https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L0882).
- Lista de cubiertos según la Comisión: computadoras y sistemas operativos, cajeros, teléfonos, TV, servicios bancarios, libros electrónicos, comercio electrónico, transporte de pasajeros, etc.; los Estados debían transponerla "by June 2022" (https://commission.europa.eu/.../european-accessibility-act_en).
- EN 301 549: "underpinned by technical criteria specified in the harmonised European standard EN 301 549 v3.2.1" (https://digital-strategy.ec.europa.eu/en/policies/web-accessibility). Ojo: esa frase la dice la Comisión sobre la Directiva de accesibilidad web (sector público) y su relación con la EAA; la presunción de conformidad con normas armonizadas es el art. 15(1) de la Directiva 2019/882 (https://eur-lex.europa.eu/eli/dir/2019/882/oj/eng). Que la EN 301 549 sea la norma armonizada de la EAA para servicios web no está dicho literalmente en lo leído: hueco a confirmar (la referencia al estándar publicada en el Diario Oficial).
- Dos fuentes independientes: texto de la Directiva (EUR-Lex) y página de la Comisión: sí, para fecha y alcance. Para EN 301 549 como norma de la EAA: una sola fuente indirecta.

### ADA (EE. UU.)
- Regla del Departamento de Justicia para gobiernos estatales y locales: requiere "Web Content Accessibility Guidelines Version 2.1 Level AA"; plazos: gobiernos con 50.000 habitantes o más, 26 de abril de 2027; menos de 50.000 y distritos especiales, 26 de abril de 2028; la página menciona una Interim Final Rule de abril de 2026 que extiende esos plazos, cuyo contenido no se leyó (https://www.ada.gov/resources/web-rule-first-steps/). Verificar las fechas vigentes.
- Empresas privadas (Título III): la página no lo trata. Que la ADA cubre sitios de negocios por vía judicial, sin norma técnica específica, es del conocimiento general, no verificado aquí. Hueco: sin fuente leída.
- Fuente: una (ADA.gov).

### Argentina: Ley 26.653 de accesibilidad de la información en las páginas web
- Quién está obligado (art. 1): "deberán respetar en los diseños de sus páginas Web las normas y requisitos sobre accesibilidad de la información"; son el Estado nacional en sus tres poderes, sus organismos descentralizados o autárquicos, los entes públicos no estatales, las empresas del Estado y las empresas privadas concesionarias de servicios públicos, prestadoras o contratistas (https://www.argentina.gob.ar/normativa/nacional/175694/texto, resumen de la herramienta).
- Art. 2: las instituciones de la sociedad civil que reciban subsidios, donaciones o condonaciones del Estado, o contraten servicios con él, deben cumplir; si prueban que no pueden, el Estado les da asistencia técnica (misma URL).
- Privados en general: art. 8, "El Estado promoverá la difusión de las normativas de accesibilidad a las instituciones de carácter privado": promover, no exigir (misma URL). Lectura mía para el caso de una tienda online privada sin vínculo con el Estado: la ley no la alcanza como obligación directa; no se encontró una fuente que lo diga con esas palabras ni jurisprudencia o proyecto reformando la ley. Esto es una conclusión sin fuente directa, a validar con un abogado.
- Sanción (art. 10): los entes que incumplan "no podrán establecer, renovar contratos, percibir subsidios, donaciones, condonaciones" del Estado nacional (misma URL). Art. 5: la ONTI define las normas, actualizadas periódicamente. Art. 7: 24 meses para páginas existentes, 12 para las en elaboración. Art. 12: invita a las provincias y a la Ciudad de Buenos Aires a adherir.
- Reglamentación: Decreto 656/2019 (dictado 19/09/2019, publicado 20/09/2019) deroga el Decreto 355/2013; designa a la ONTI autoridad de aplicación (fuente: resultados del buscador sobre https://www.argentina.gob.ar/normativa/nacional/decreto-656-2019-328722/texto y https://www.argentina.gob.ar/onti/accesibilidad-web; el texto no se pudo leer: [S]).
- Norma técnica: la Disposición ONTI 6/2019 aprueba las "Pautas de Accesibilidad de Contenido Web 2.0" y dice incorporar "criterios de conformidad de nivel 'AA'"; su art. 4 pide 20 criterios en el primer año y 30 en los períodos siguientes, de 38 en el Anexo II; no nombra WCAG en el texto leído (https://www.argentina.gob.ar/normativa/nacional/329284/texto). El W3C anota "WCAG Version Used: WCAG 2.0" (https://www.w3.org/wai/policies/argentina).
- Discrepancias a mostrar: (a) la ficha del W3C dice nivel de conformidad A, mientras la Disposición 6/2019 habla de AA; (b) la fecha de la ley: el W3C anota "2010-11-26" (promulgación), un dictamen de Diputados fija la sanción el 3 de noviembre de 2010 (https://www4.hcdn.gob.ar/dependencias/dcomisiones/periodo-130/130-470.pdf, [S]): son sanción y promulgación, probablemente no contradictorias, pero no verificado.
- Independencia de fuentes: la ley y la Disposición son dos normas, no dos fuentes sobre el mismo hecho; para "qué exige la norma técnica" hay una fuente leída (la Disposición) más una ficha del W3C que discrepa en el nivel. Declaro que sobre el decreto reglamentario hay una sola fuente, no leída directamente.

### Recurso canónico
Para la UE, el texto de la Directiva 2019/882, arts. 2, 4 y 32 (y 3(23)). Para Argentina, el texto de la Ley 26.653 en argentina.gob.ar (arts. 1, 2, 8, 10) y la Disposición ONTI 6/2019 con sus anexos. Para EE. UU., ADA.gov. Fijarse en quién queda alcanzado y en qué versión y nivel se exige, y no tratar ninguna de las tres como asesoramiento legal.

---

## Huecos

1. Espectro de discapacidad permanente, temporal y situacional de Microsoft: no se pudo leer (el sitio actual no lo trae); falta el PDF del toolkit.
2. Tecnologías de apoyo: sin fuente leída.
3. Cantidad de criterios de WCAG 2.2 (86) solo por aritmética y fuente de terceros; no figura en las páginas del W3C leídas. Sección de conformidad de la norma (cita completa de AAA en el cuerpo de la norma) no leída: se citó el Understanding.
4. Lindgaard (2006) y Kurosu y Kashimura (1995), Garrett y Bringhurst: sin lectura de la fuente primaria (403, paga o libro). Cifra r = .97 sin confirmar.
5. Largo de línea 45-75: convención de imprenta; evidencia en pantalla (Dyson y Haselgrove) solo por resumen; sin estudio que valide el rango para texto de interfaz.
6. Patrones de lectura de NN/g: tamaño de muestra de los estudios 2006 y 2017 y los patrones alternativos no verificados; no hay réplica independiente revisada por pares.
7. Sistemas de diseño: sin evidencia rigurosa de retorno ni de tasa de fracaso (solo encuestas de proveedores); Material Design no leído; estatus formal de la especificación de tokens como no estándar del W3C sin lectura de su propio apartado de estatus.
8. Legal: Decreto 656/2019 no leído (HTTP 500); si la EN 301 549 es la norma armonizada de la EAA para servicios web no está literal en lo leído; ADA para empresas privadas sin fuente; contenido de la Interim Final Rule de abril de 2026 sin leer; Ley 26.653 leída vía resumen de herramienta (citas literales de ≤125 caracteres). Nada de esto sustituye una revisión legal.
9. WebAIM Million: solo el último informe (2026); no se comparó con años anteriores.
10. División del árbol: ver al principio (legal sin lugar propio).
