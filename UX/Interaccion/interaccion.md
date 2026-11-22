---
resumen: >-
  La interacción es la parte de la experiencia que decide cómo se usa un producto: qué controles ofrece, cómo responde a cada acción y cómo ayuda a evitar y corregir errores.
estado: borrador
estabilidad: estable
fuentes:
  - "Jenny Preece, Yvonne Rogers y Helen Sharp, Interaction Design: Beyond Human-Computer Interaction (resumen en https://oro.open.ac.uk/47656)"
  - "Alan Cooper, Robert Reimann, David Cronin y Christopher Noessel, About Face: The Essentials of Interaction Design, 4.ª ed., Wiley, 2014 (solo fichas del libro e índice)"
  - "NN/g, Kaplan, Designing Empty States in Complex Applications, 19 de septiembre de 2021: https://www.nngroup.com/articles/empty-state-interface-design/"
  - "NN/g, Flaherty, Indicators, Validations, and Notifications: Pick the Correct Communication Option, 17 de enero de 2024: https://www.nngroup.com/articles/indicators-validations-notifications/"
  - "NN/g, Laubheimer, Data Tables, 3 de abril de 2022 (solo resumen): https://www.nngroup.com/articles/data-tables/"
  - "UX/.investigacion/arquitectura-e-interaccion.md y UX/.investigacion/fundamentos.md, sección 5"
aliases: [diseño de interacción, interaction design, IxD]
creado: 2026-11-22
revisado:
---

# Interacción

La interacción es la parte de la experiencia que decide cómo se usa un producto: qué controles ofrece, cómo responde a cada acción y cómo ayuda a evitar y corregir errores.

Recibe de la [arquitectura de información](../Arquitectura-de-informacion/arquitectura-de-informacion.md) la estructura que se recorre y se presenta con el [diseño visual](../Diseno-visual/diseno-visual.md). La [accesibilidad](../Accesibilidad/accesibilidad.md) le pone requisitos verificables, y la [evaluación](../Evaluacion/evaluacion.md) comprueba si funciona. Se apoya en lo que la persona cree sobre el sistema, el [modelo mental](../Percepcion-y-decision/modelo-mental.md), y en cuánto esfuerzo le pide, la [carga cognitiva](../Percepcion-y-decision/carga-cognitiva.md).

## Qué es diseñar una interacción

Según el resumen de la Open University, Preece, Rogers y Sharp definen el diseño de interacción como diseñar productos interactivos "to support the way people communicate and interact in their everyday and working lives". La redacción citada es la de la 3.ª edición y del abstract de la 4.ª; la 1.ª lo decía distinto. Según resultados de buscador, Cooper presenta el diseño dirigido por metas como método válido en cualquier plataforma y dominio; su cita literal no se leyó. El índice de su libro incluye "Optimizing for Intermediates", "Perpetual Intermediates" y "Goal-Directed Tasks versus Excise Tasks". La investigación señala el "excise" (el trabajo que la interfaz impone y no ayuda a la meta de la persona) como idea útil para sistemas internos; es una recomendación, sin un pasaje leído que lo sostenga. Para profundizar, leer el capítulo 1 de Preece, Rogers y Sharp, y los capítulos de Cooper sobre excise y sobre intermedios.

## La respuesta del sistema en tres estados

Tres estados de una pantalla se diseñan aparte, y ninguno tiene nota todavía.

- Vacío. Según Kaplan (NN/g, 2021), conviene no dejarlo totalmente vacío: explicar qué podría aparecer y cómo llenarlo, enlazar a los primeros pasos, mostrar progreso mientras procesa y decir "no hay contenido" si terminó sin datos.
- Error. Según Flaherty (NN/g, 2024), los mensajes de validación "should explain the fix, not just the problem"; "Field is blank" es peor que decir qué ingresar. Los toasts son mala opción para errores: un usuario no vio el aviso y esperó cinco minutos.
- Carga. Los umbrales de tiempo de respuesta están en [Principios de interacción](principios-de-interaccion.md). No hay otra fuente leída sobre cómo mostrar la espera.

## Tablas de datos: una guía de instituto

Para tablas empresariales, el resumen de Laubheimer (NN/g, 3 de abril de 2022) propone cuatro tareas centrales: encontrar registros, comparar, ver o editar una fila y actuar sobre registros. Sus recomendaciones incluyen fijar filas y columnas de encabezado si la tabla excede la pantalla, editar una fila fuera de la tabla con un panel lateral no modal, y ofrecer acciones por lote con casillas y "Select All" cuando hay más de una o dos acciones. Es una guía de instituto, leída solo en su resumen. Este material queda para la nota de patrones de interacción, que falta.

## Qué hay adentro

- [Principios de interacción](principios-de-interaccion.md): el concepto de significante de Norman (con su corrección sobre affordance), los siete principios de ISO 9241-110 y los umbrales de tiempo de respuesta, como criterio para mirar una pantalla.
- [Formularios](formularios.md): etiquetas, validación en línea, cantidad de campos, placeholders y abandono de checkout, con estudios fechados.

## Qué falta

Quedan por escribir: los estados de la interfaz (vacío, carga, error), el microcopy (el texto de etiquetas, botones y mensajes) y los patrones de interacción (tablas de datos, búsqueda, onboarding).

> [!NOTE]
> Sin fuente todavía: microcopy (no hay fuente primaria leída) y formularios largos de sistemas internos (de Cooper solo se leyó el índice).
