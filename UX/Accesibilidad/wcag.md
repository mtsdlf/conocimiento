---
resumen: >-
  WCAG 2.2 es la recomendación del W3C que fija criterios verificables para que el contenido web sea perceptible, operable, comprensible y robusto. El W3C desaconseja exigir el nivel AAA como política general, y WCAG 3.0 sigue en borrador.
estado: borrador
estabilidad: semi
fuentes:
  - "W3C, Web Content Accessibility Guidelines (WCAG) 2.2, Recomendación del 12 de diciembre de 2024 (leída en parte): https://www.w3.org/TR/WCAG22/"
  - "W3C WAI, WCAG 2 Overview: https://www.w3.org/WAI/standards-guidelines/wcag/"
  - "W3C WAI, What's New in WCAG 2.2: https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/"
  - "W3C WAI, WCAG 2 at a Glance: https://www.w3.org/WAI/standards-guidelines/wcag/glance/"
  - "W3C, Understanding Conformance: https://www.w3.org/WAI/WCAG22/Understanding/conformance"
  - "W3C, WCAG 3.0, Working Draft del 10 de septiembre de 2026: https://www.w3.org/TR/wcag-3.0/"
  - "UX/.investigacion/diseno-visual-y-accesibilidad.md"
aliases: [WCAG 2.2, Web Content Accessibility Guidelines, pautas de accesibilidad para el contenido web]
creado: 2026-11-22
revisado:
---

# WCAG

WCAG 2.2 es la recomendación del W3C que fija criterios verificables para que el contenido web sea perceptible, operable, comprensible y robusto. El W3C desaconseja exigir el nivel AAA como política general, y WCAG 3.0 sigue en borrador.

Es la norma técnica de la [accesibilidad](accesibilidad.md): la regla de la ADA la cita (véase la [normativa](normativa-de-accesibilidad.md)), y los criterios son requisitos para el [diseño visual](../Diseno-visual/diseno-visual.md) y la [interacción](../Interaccion/interaccion.md).

## La versión vigente y sus dos fechas

Según el W3C, WCAG 2.2 "was published on 5 October 2023, and an update was published on 12 December 2024". La versión que figura hoy en la dirección oficial lleva el encabezado "W3C Recommendation, 12 December 2024". Son dos fechas correctas: la Recomendación original y su republicación con correcciones.

Respecto de WCAG 2.1, la versión 2.2 agregó "9 additional success criteria" y eliminó el 4.1.1 Parsing, "obsolete and removed". El W3C agrupa los criterios en 13 pautas bajo los cuatro principios.

## Los cuatro principios

Se los conoce por la sigla POUR: el contenido debe ser "perceivable, operable, understandable, and robust". La primera pauta de cada uno:

| Principio | Primera pauta |
|---|---|
| Perceptible | Proporcionar alternativas de texto para el contenido que no es texto |
| Operable | Hacer toda la funcionalidad disponible desde un teclado |
| Comprensible | Hacer el texto legible y comprensible |
| Robusto | Maximizar la compatibilidad con las herramientas actuales y futuras del usuario |

## Niveles A, AA y AAA

El nivel A es el mínimo. Para conformar con AA hay que cumplir todos los criterios A y AA, y para AAA todos. El documento Understanding Conformance desaconseja exigir AAA como política general: "It is not recommended that Level AAA conformance be required as a general policy for entire sites" "because it is not possible to satisfy all Level AAA success criteria for some content".

El W3C no dice que AA sea el objetivo habitual; eso sería una inferencia. Lo que consta es que desaconseja exigir AAA y que la regla de la ADA pide WCAG 2.1 nivel AA y la Disposición ONTI habla de AA, mientras la ficha del W3C anota nivel A para Argentina (ver [Normativa de accesibilidad](normativa-de-accesibilidad.md)).

## Criterios clave, con su número

| Criterio | Nivel | Qué exige |
|---|---|---|
| 1.4.3 Contraste (mínimo) | AA | Contraste de al menos 4,5 a 1 en texto e imágenes de texto; 3 a 1 en texto grande; con excepciones para texto incidental y logotipos |
| 2.1.1 Teclado | A | Toda la funcionalidad se opera desde una interfaz de teclado (excepción para entrada que depende del trazado) |
| 2.5.8 Tamaño del objetivo (mínimo) | AA | El objetivo de un puntero mide al menos 24 por 24 píxeles CSS, salvo excepciones de espaciado, equivalente, en línea, controlado por el agente de usuario y esencial |

El origen del 4,5 a 1 está en [Diseño visual](../Diseno-visual/diseno-visual.md).

Los criterios nuevos de la 2.2 son nueve: 2.4.11 Foco no oculto (mínimo, AA), 2.4.12 Foco no oculto (mejorado, AAA), 2.4.13 Apariencia del foco (AAA), 2.5.7 Movimientos de arrastre (AA), 2.5.8 Tamaño del objetivo (mínimo, AA), 3.2.6 Ayuda coherente (A), 3.3.7 Entrada redundante (A), 3.3.8 Autenticación accesible (mínimo, AA) y 3.3.9 Autenticación accesible (mejorado, AAA). Los 3.3.x tocan a los [formularios](../Interaccion/formularios.md).

> [!NOTE] Sin fuente todavía: el total de criterios de WCAG 2.2 no figura en las páginas del W3C que se leyeron. Por aritmética (78 de WCAG 2.1, más 9, menos 1) da 86, y una guía de terceros lo dice; los conteos por nivel de sitios de terceros difieren entre sí y no se usan. Tampoco se leyó la sección de conformidad de la norma, solo su documento Understanding.

## WCAG 3.0 no reemplaza a WCAG 2

La versión 3.0, antes llamada "Silver", está en estado de "W3C Working Draft, 10 September 2026". El borrador avisa que "may be updated, replaced, or obsoleted by other documents at any time" y que "WCAG 3 does not replace WCAG 2". Lo que se exige hoy es WCAG 2.x.

## Cómo leerla

Se lee la norma en [w3.org/TR/WCAG22](https://www.w3.org/TR/WCAG22/) y, para cada criterio, su documento Understanding, en las partes Intent, Benefits y Techniques. Para empezar sirven 1.4.3, 2.1.1, 2.5.8 y los 3.3.x. El estado real de la web, con WebAIM, está en [Accesibilidad](accesibilidad.md).
