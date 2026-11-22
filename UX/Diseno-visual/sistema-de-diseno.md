---
resumen: >-
  Un sistema de diseño es el conjunto de estándares, componentes reutilizables y patrones con que una organización gestiona su diseño a escala. Rinde cuando hay años de trabajo repetible por delante, y falla si nadie lo mantiene.
estado: vigente
estabilidad: semi
fuentes:
  - "NN/g, Design Systems 101: https://www.nngroup.com/articles/design-systems-101/"
  - "Brad Frost, Atomic Design (2016), cap. 2: https://atomicdesign.bradfrost.com/chapter-2/"
  - "Design Tokens Community Group, Format Module 2025.10 (Final Community Group Report, 28 de octubre de 2025): https://www.designtokens.org/tr/2025.10/format/"
  - "Design Tokens Community Group, portada: https://www.designtokens.org/"
  - "GOV.UK Design System: https://design-system.service.gov.uk/"
  - "IBM Carbon, What is Carbon: https://carbondesignsystem.com/all-about-carbon/what-is-carbon/"
  - "Sparkbox, Design Systems Survey 2018 y 2020 (resúmenes): https://designsystemssurvey.sparkbox.com/2018 y https://designsystemsurvey.sparkbox.com/2020"
  - "UX/.investigacion/diseno-visual-y-accesibilidad.md"
aliases: [design system, sistema de diseño, biblioteca de componentes, design tokens, token de diseño, atomic design]
creado: 2026-11-22
revisado: 2026-11-22
---

# Sistema de diseño

Un sistema de diseño es el conjunto de estándares, componentes reutilizables y patrones con que una organización gestiona su diseño a escala. Rinde cuando hay años de trabajo repetible por delante, y falla si nadie lo mantiene.

NN/g lo define como "a complete set of standards intended to manage design at scale using reusable components and patterns". Es la parte del [diseño visual](diseno-visual.md) que lo vuelve repetible: convierte las decisiones de [jerarquía](jerarquia-visual.md), tipografía y color en piezas que cualquier equipo reutiliza. La implementación en código (las librerías de componentes) es del tema [Desarrollo](../../Desarrollo/desarrollo.md).

## De qué está hecho

Un sistema se compone de cuatro piezas (la división es de esta base y NN/g la describe solo en parte):

- Componentes y patrones: los elementos reutilizables (botón, campo, tabla) y las combinaciones recurrentes de ellos.
- Tokens de diseño: los valores con nombre (un color, un espacio, un tamaño de letra) que los componentes consumen en vez de repetir el valor.
- Guías: la documentación de cuándo y cómo usar cada pieza.
- Gobierno: quién decide qué entra, quién mantiene y cómo se contribuye.

Brad Frost propone en Atomic Design un vocabulario para ordenar los componentes en cinco etapas: átomos, moléculas, organismos, plantillas y páginas. Frost lo presenta como un modelo mental, no como una secuencia estricta de trabajo.

## El formato de tokens del W3C, con fecha

La especificación del Design Tokens Community Group "describes the technical specification for a file format to exchange design tokens between different tools". Al 2026-11-22, la versión leída es la 2025.10, con estado de Final Community Group Report del 28 de octubre de 2025; la portada del grupo anuncia "First stable version 2025.10".

Un Community Group del W3C no es un órgano de estándares: ese informe no es una Recomendación del W3C. Esa lectura sale de la herramienta de lectura y del conocimiento general del proceso del W3C; no se leyó el apartado de estatus de la especificación. Como los formatos cambian, se vuelve a mirar la fuente viva antes de apoyarse en ella.

## Cuánto cuesta y cuándo conviene

Según NN/g, el beneficio principal es replicar diseños rápido, y además aportan lenguaje común, consistencia y una incorporación más ágil de gente nueva. El costo es real: crear y mantener uno "is a time-intensive activity which requires a dedicated team". Adoptar uno existente es la vía más barata.

Conviene cuando la empresa prevé años de trabajo de diseño repetible. Para una prueba de concepto o un prototipo que va a cambiar, un sistema completo a menudo no se paga en el corto plazo (paráfrasis de NN/g).

## Ejemplos públicos como práctica

GOV.UK se presenta como el sistema "for everyone that works on government services", mantenido por el Government Digital Service para evitar "repeating work that's already been done". Carbon es "IBM's open-source design system for products and digital experiences". Sirven para ver cómo documenta cada componente y cómo abre la contribución. Muestran qué hacen dos organizaciones, no que el enfoque funcione: son práctica, no evidencia.

## Cómo falla

NN/g advierte que mal implementado y mal mantenido se vuelve una colección inmanejable de componentes y código. Los modos concretos: uso inconsistente cuando faltan instrucciones, entradas viejas que se acumulan, y falta de un patrocinante ejecutivo que consiga recursos.

Dos encuestas de Sparkbox, leídas solo por resumen, apuntan en la misma dirección. En la de 2018 (86 respondientes con sistema), algo más del 25% lo calificó "average" o "unsuccessful", y el resumen cita la falta de patrocinante como causa. La de 2020 señala la adopción como desafío principal, con un 41% de los equipos internos midiéndola.

> [!NOTE] Sin fuente todavía: evidencia revisada por pares sobre el retorno de un sistema de diseño o sus tasas de fracaso. Solo hay encuestas autoseleccionadas o de proveedores, un estudio de Forrester encargado por Adobe (patrocinado) y un trabajo de máster sobre una sola empresa. Material Design no se leyó.

## Qué leer

Para el vocabulario, Frost, Atomic Design, caps. 1 y 2 (gratis en línea; en la investigación solo se leyó el cap. 2). Para costo y gobierno, NN/g, Design Systems 101. Para ver un sistema con gobierno y contribución abiertos, GOV.UK Design System, con atención a cómo documenta cada componente con su investigación y su modo de uso.
