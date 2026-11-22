---
resumen: >-
  La accesibilidad es el diseño de productos que pueda usar cualquiera, con o sin discapacidad, en cualquier situación. Pone requisitos verificables a la interacción y al diseño visual, y su estado real en la web es malo: casi todas las páginas de inicio fallan en algo detectable.
estado: vigente
estabilidad: estable
fuentes:
  - "OMS, Disability (hoja informativa, 7 de marzo de 2023): https://www.who.int/news-room/fact-sheets/detail/disability-and-health"
  - "Microsoft Inclusive Design: https://inclusive.microsoft.design/"
  - "WebAIM, The WebAIM Million (análisis de febrero de 2026): https://webaim.org/projects/million/"
  - "W3C WAI, WCAG 2 Overview: https://www.w3.org/WAI/standards-guidelines/wcag/"
  - "UX/.investigacion/diseno-visual-y-accesibilidad.md"
aliases: [accesibilidad web, a11y, diseño inclusivo, accesibilidad digital]
creado: 2026-11-22
revisado: 2026-11-22
---

# Accesibilidad

La accesibilidad es el diseño de productos que pueda usar cualquiera, con o sin discapacidad, en cualquier situación. Pone requisitos verificables a la interacción y al diseño visual, y su estado real en la web es malo: casi todas las páginas de inicio fallan en algo detectable.

Dentro de [UX](../ux.md), la accesibilidad exige condiciones a la [interacción](../Interaccion/interaccion.md) y al [diseño visual](../Diseno-visual/diseno-visual.md). Tiene la particularidad de que sus requisitos se pueden verificar uno por uno, con un criterio de éxito de [WCAG](wcag.md) cada vez, y de que en algunas jurisdicciones una [norma legal](normativa-de-accesibilidad.md) exige accesibilidad digital. Varios criterios son a la vez decisiones visuales: el contraste del texto, por ejemplo, se trata como diseño en [Diseño visual](../Diseno-visual/diseno-visual.md) y como requisito en WCAG.

## A cuánta gente alcanza

La OMS estima que "1.3 billion people – or 16% of the global population – experience a significant disability today" (hoja informativa del 7 de marzo de 2023; conviene comprobar si hay una versión más reciente). La cifra es de discapacidad significativa, así que no cuenta a quienes tienen una limitación temporal o de contexto.

El enfoque de diseño inclusivo de Microsoft parte de tres principios: "Recognize exclusion", "Learn from diversity" y "Solve for one, extend to many". El tercero lo justifica así: "Creating products for people with permanent disabilities creates results that benefit everyone."

> [!NOTE] Sin fuente todavía: el espectro de limitación permanente, temporal y situacional que se atribuye al toolkit de Microsoft (el ejemplo clásico es un brazo, un brazo lesionado y cargar un bebé). No se pudo leer en el sitio actual; falta el toolkit "Inclusive 101". Tampoco hay fuente leída sobre las tecnologías de apoyo (lectores de pantalla, ampliadores, control por voz o por conmutador); el lugar donde mirar son los documentos Understanding de WCAG y WebAIM.

## Cómo está la web

El informe WebAIM Million analizó con detección automática las páginas de inicio de un millón de sitios. En el análisis de febrero de 2026, el 95,9% tenía fallas de WCAG 2 detectables, con un promedio de 56,1 errores por página. Las fallas más frecuentes:

| Falla | Páginas de inicio afectadas |
|---|---|
| Contraste de texto insuficiente | 83,9% |
| Imágenes sin texto alternativo | 53,1% |
| Campos de formulario sin etiqueta | 51% |
| Enlaces vacíos | 46,3% |
| Botones vacíos | 30,6% |
| Idioma del documento sin declarar | 13,5% |

La detección automática subestima las fallas reales, y el análisis mide solo la página de inicio. Solo se leyó el informe de 2026, sin comparar con años anteriores.

## Qué hay adentro

- [WCAG](wcag.md): la norma técnica que fija los criterios verificables, con sus niveles A, AA y AAA.
- [Normativa de accesibilidad](normativa-de-accesibilidad.md): ficha fechada de las normas de la Unión Europea, Estados Unidos y Argentina que exigen accesibilidad digital.

## Qué falta

El [alcance](../ALCANCE.md) prevé sumar notas sobre diseño inclusivo (método y espectro de personas), pruebas con tecnologías de apoyo (cómo se verifica con un lector de pantalla) y accesibilidad cognitiva. Hoy solo se mencionan en esta entrada.
