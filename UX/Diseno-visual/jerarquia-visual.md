---
resumen: >-
  La jerarquía visual es la organización de los elementos de una página para que el ojo recorra primero lo más importante. Se arma con contraste, escala y agrupamiento, y falla cuando todo pesa igual.
estado: borrador
estabilidad: estable
fuentes:
  - "NN/g, Visual Hierarchy in UX: https://www.nngroup.com/articles/visual-hierarchy-ux-definition/"
  - "NN/g (2006), F-Shaped Pattern For Reading Web Content: https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content-discovered/"
  - "NN/g (2017, revisado agosto de 2026), F-Shaped Pattern of Reading on the Web: Misunderstood, But Still Relevant (Even on Mobile): https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/"
  - "Interaction Design Foundation, Gestalt principles: https://ixdf.org/literature/topics/gestalt-principles"
  - "UX/.investigacion/diseno-visual-y-accesibilidad.md"
aliases: [jerarquía visual, patrón en F, F-pattern, visual hierarchy]
creado: 2026-11-22
revisado:
---

# Jerarquía visual

La jerarquía visual es la organización de los elementos de una página para que el ojo recorra primero lo más importante. Se arma con contraste, escala y agrupamiento, y falla cuando todo pesa igual.

NN/g la define como la organización de los elementos de diseño de modo que el ojo se guíe a cada uno en el orden de importancia buscado. Se apoya en el [diseño visual](diseno-visual.md) y usa los principios de agrupamiento de la Gestalt, que explica [Percepción y decisión](../Percepcion-y-decision/percepcion-y-decision.md), para decidir qué se ve primero.

## Tres recursos para armarla

Contraste con el contexto. Un elemento destaca por diferir de lo que lo rodea. NN/g advierte que no hay que apoyarse solo en el color para comunicar jerarquía, y resume el límite en una frase: "If everything is contrasted, then nothing stands out."

Escala. Lo más importante se ve más grande. La recomendación de NN/g es no pasar de tres tamaños y tener como máximo dos elementos grandes.

Agrupamiento. La proximidad, el espacio en blanco y las regiones comunes separan bloques y muestran qué va con qué. La alineación no la trata esa fuente; esta base la cubre con la continuidad de la Gestalt, por inferencia: los elementos alineados se leerían como una serie.

## Cómo falla una jerarquía

NN/g describe tres fallas. Tamaño, color y espaciado uniformes no dejan foco. El contenido puede pisar la plantilla: una foto muy coloreada domina aunque no sea lo importante. Agrupar sin cuidado puede hacer que se ignore un bloque entero, la ceguera a banners. Además propone entrecerrar los ojos frente a la pantalla, que revela jerarquías no buscadas, y probar la jerarquía con usuarios ([test de usabilidad](../Evaluacion/test-de-usabilidad.md)).

## El patrón en F: qué dijo NN/g en 2006 y cómo lo corrigió después

En 2006, NN/g publicó con eye-tracking que los usuarios leían en tres movimientos: primero un recorrido horizontal por la parte superior del contenido, luego otro horizontal más corto, y por último un barrido vertical por el lado izquierdo. La forma se parece a una F.

El artículo de 2017, revisado en agosto de 2026, corrige la lectura habitual. Según NN/g (esa página y la de 2006):

- El patrón se identificó en 2006, y un estudio de eye-tracking once años después confirmó los hallazgos.
- Casi nunca es una F perfecta.
- Es el patrón por defecto cuando no hay señales fuertes: aparece cuando el diseño no guía.
- No es el único patrón de lectura.
- Es malo para usuarios y negocios. La fuente leída no dejó registrado el porqué.

Para diseñar, la lectura de esta base es que la F describe lo que pasa cuando no se hace jerarquía y no sirve de plantilla donde colocar cosas. Que títulos, listas y destacados que guían la mirada rompan el patrón es una inferencia, sin fuente leída.

> [!NOTE] Sin fuente todavía: el tamaño de muestra de los estudios de 2006 y de 2017, y los otros patrones de lectura (capas, manchas, compromiso). La página de 2017 menciona "more than 45 people" solo para un mapa de calor de principios de los años 2000.

## Cuánto pesa esta evidencia

El eye-tracking de NN/g es un estudio de practicantes, no revisado por pares, y no se encontró una réplica independiente revisada por pares. Se trata como pista fuerte, no como ley.

El contraste del texto es un caso aparte: además de jerarquía, es un requisito de [WCAG](../Accesibilidad/wcag.md) (1.4.3).

## Dónde seguir

Para leer: NN/g, Visual Hierarchy in UX, por los principios y las fallas, y la versión de 2017 del artículo de la F, en el apartado que dice que no es el único patrón.
