---
resumen: >-
  La ley de Fitts predice cuánto tarda un movimiento apuntado a un blanco, y la de Hick cuánto tarda elegir entre alternativas. Fitts tiene respaldo en diseño de interfaces; Hick no justifica por sí sola que menos opciones sea mejor.
estado: borrador
estabilidad: estable
fuentes:
  - "I. Scott MacKenzie (1992), Fitts' law as a research and design tool in human-computer interaction, Human-Computer Interaction 7, 91-139 (copia del autor, leída en parte): https://www.yorku.ca/mack/hci1992.html"
  - "Paul M. Fitts (1954), J. Exp. Psychology 47(6), 381-391 (no leído; citado por MacKenzie)"
  - "W. E. Hick (1952), On the rate of gain of information, Q. J. Exp. Psychology 4(1), 11-26: doi:10.1080/17470215208416600 (no leído; solo metadatos)"
  - "Ray Hyman (1953), Stimulus information as a determinant of reaction time, J. Exp. Psychology 45(3), 188-196: doi:10.1037/h0056940 (no leído)"
  - "Liu, Gori, Rioul, Beaudouin-Lafon y Guiard (2020), How Relevant is Hick's Law for HCI?, CHI 2020: https://researchportal.ip-paris.fr/en/publications/how-relevant-is-hicks-law-for-hci/ (solo abstract)"
  - "Wikipedia, Hick's law (fórmulas y límites; secundaria): https://en.wikipedia.org/wiki/Hick%27s_law"
  - "UX/.investigacion/percepcion-y-decision.md y UX/.investigacion/posicion-contraria.md"
aliases: [Fitts' law, Hick's law, ley de Hick-Hyman, Hick-Hyman, índice de dificultad]
creado: 2026-11-22
revisado:
---

# Leyes de Fitts y Hick

La ley de Fitts predice cuánto tarda un movimiento apuntado a un blanco, y la de Hick cuánto tarda elegir entre alternativas. Fitts tiene respaldo en diseño de interfaces; Hick no justifica por sí sola que menos opciones sea mejor.

Las dos suelen presentarse juntas en la literatura de practicantes, pero miden cosas distintas: Fitts es control motor, Hick es decisión. Esta nota las junta por comodidad, así que separa qué dice y qué límites tiene cada una. Ambas pertenecen a [Percepción y decisión](percepcion-y-decision.md) como cota de lo que una persona puede hacer rápido.

## Fitts: el tiempo de apuntar

El tiempo de un movimiento apuntado crece con el logaritmo de la distancia sobre el ancho del blanco. MacKenzie (1992) da la forma original (ecuaciones 3 y 6) y la de Shannon que propone él (ecuación 10):

- Original: `ID = log2(2A/W)` y `MT = a + b·log2(2A/W)`.
- Shannon: `MT = a + b·log2(A/W + 1)`.

A es la amplitud (la distancia al blanco), W el ancho del blanco, `a` (en ms) y `b` (en ms por bit) son constantes empíricas, e IP = 1/b se mide en bits por segundo. La consecuencia de diseño es que un blanco más grande y más cercano se alcanza más rápido.

Límites que señala MacKenzie: el 2 de la forma original fue un ajuste arbitrario, y esa forma da dificultad negativa cuando A < W/2, "a serious theoretical problem", que la de Shannon evita. La ley vale para movimientos rápidos con error cercano al 4 %. Las predicciones empeoran por debajo de unos 3 bits. En blancos rectangulares abordados desde ángulos distintos, qué cuenta como "W" no está resuelto. Las extensiones al dedo y a pantallas táctiles son otra literatura, que este material no cubre.

## Hick: el tiempo de elegir

Hick (1952) relacionó el tiempo de reacción de elección con el número de alternativas estímulo-respuesta, y concluyó que la tasa de ganancia de información es en promedio constante durante un acto perceptivo-motor. Hyman (1953) lo extendió a alternativas con probabilidades desiguales. Ambos datos vienen de un resultado de buscador, sin abrir los textos. Las fórmulas, según Wikipedia (fuente secundaria; las ecuaciones originales no se leyeron):

- Alternativas equiprobables: `T = b · log2(n + 1)`.
- Probabilidades desiguales: `T = b·H`, con `H = Σ pi · log2(1/pi + 1)`.

El "+1" refleja la incertidumbre sobre si responder o no.

> [!IMPORTANT] Hick no demuestra que "menos opciones, decisión más rápida". Una práctica extendida (por ejemplo, el artículo de la Interaction Design Foundation, del que solo se vio un extracto) cita la ley como base del diseño de menús y de la simplicidad. Liu et al. (CHI 2020, según su abstract) sostienen lo contrario: la ley "no apoya" el principio de "menos es mejor", un crecimiento logarítmico en los datos no implica Hick, el paradigma estímulo-respuesta rara vez es relevante en tareas de HCI, y conviene mirar la búsqueda visual y la decisión en lugar de citar la ley. Según el mismo abstract y Wikipedia, Seow (2005) ya había mostrado que Fitts y Hick no se justifican con la ley de Hick.

Los límites que lista Wikipedia, que son secundarios, coinciden con esa lectura: buscar en una lista desordenada es lineal y no permite generalizar la ley; con respuestas verbales a estímulos familiares, Longstreth et al. (1985) hallaron poca o ninguna relación; en movimientos sacádicos del ojo no hay relación o hay un efecto "anti-Hick"; y la compatibilidad entre estímulo y respuesta cambia el tiempo.

La lectura que sostiene esta base es la prudente: Hick describe elecciones entre alternativas equiprobables, no conocidas de antemano y con la respuesta mapeada al estímulo. No describe la búsqueda en una lista desordenada ni la elección entre opciones que la persona ya conoce, y no es evidencia por sí misma de que reducir opciones acelere la decisión. La formulación no contempla agrupar ni jerarquizar las opciones (inferencia de esta base, sin una fuente que la declare como crítica). Para un menú largo, ver [Navegación](../Arquitectura-de-informacion/navegacion.md) y [jerarquía visual](../Diseno-visual/jerarquia-visual.md). Los umbrales de tiempo de respuesta del sistema (0,1 s, 1 s y 10 s) son otro asunto, que está en [Principios de interacción](../Interaccion/principios-de-interaccion.md).

## Dónde leer más

Para Fitts, MacKenzie (1992), las secciones sobre la formulación de Shannon y el ancho efectivo (We): fijarse en cuándo la forma original falla. Para Hick, el texto completo de Liu et al. (2020) antes que cualquier artículo de practicantes; este material solo vio su abstract.

> [!NOTE] Sin fuente todavía: las ecuaciones originales de Hick (1952) y de Fitts (1954) no se leyeron; las fórmulas vienen de MacKenzie y de Wikipedia. Tampoco hay fuente sobre los límites de Fitts en pantallas táctiles ni sobre el argumento alternativo de convexidad de Liu et al.
