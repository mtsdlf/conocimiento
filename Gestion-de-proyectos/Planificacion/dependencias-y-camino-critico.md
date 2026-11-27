---
resumen: >-
  Las dependencias dicen qué pieza del trabajo espera a cuál; el camino crítico es la cadena de dependencias más larga, la que fija el plazo, y subestima la duración cuando hay varias cadenas casi tan largas o recursos compartidos.
estado: borrador
estabilidad: estable
fuentes:
  - "MacCrimmon y Ryavec (1964), An Analytical Study of the PERT Assumptions, Operations Research 12(1):16-37 (según resumen): https://pubsonline.informs.org/doi/fpi/10.1287/opre.12.1.16"
  - "PMI, Project network models past, present, and future (según resumen): https://www.pmi.org/learning/library/project-network-models-past-present-future-5685"
  - "Raz, Barnes y Dvir (2003), A critical look at critical chain project management, Project Management Journal 34(4):24-32 (solo el registro): https://cris.bgu.ac.il/en/publications/a-critical-look-at-critical-chain-project-management-2/"
  - "Mirzaei y Mabin (2018), revisión de la cadena crítica, Int. J. Project Organisation and Management 10(3) (según resumen): https://ideas.repec.org/a/ids/ijpoma/v10y2018i3p242-267.html"
  - "Revisión sistemática de la cadena crítica multiproyecto, Applied Sciences (2025) (según resumen): https://www.mdpi.com/2076-3417/15/15/8147"
  - "Estudio de 10 casos de cadena crítica (según resumen del buscador): https://ir.wgtn.ac.nz/handle/123456789/29888"
  - "Goldratt, Critical Chain (1997) (no se leyó)"
  - "Gestion-de-proyectos/.investigacion/planificacion-y-riesgo.md"
aliases: [camino crítico, ruta crítica, critical path, CPM, PERT, cadena crítica, critical chain, CCPM, dependencias, dependencies]
creado: 2026-11-27
revisado:
---

# Dependencias y camino crítico

Las dependencias dicen qué pieza del trabajo espera a cuál; el camino crítico es la cadena de dependencias más larga, la que fija el plazo, y subestima la duración cuando hay varias cadenas casi tan largas o recursos compartidos.

Las piezas salen de la [descomposición del trabajo](descomposicion-del-trabajo.md). Ordenarlas por dependencias da una red, y sobre esa red se calcula el plazo que después entra al [pronóstico](pronostico.md). Es parte de la [planificación](planificacion.md).

## Dos clases de espera

Una pieza espera a otra por la lógica del trabajo o porque las dos necesitan lo mismo. Al lanzar un servicio, no se puede abrir la venta antes de tener el permiso habilitante: eso es lógica. Si la misma persona tiene que redactar los términos y revisar la tarifa, una espera a la otra aunque el trabajo no lo pida: eso es un recurso compartido. La red clásica dibuja la primera clase y suele omitir la segunda.

Con agentes cambia qué recurso se comparte. La ejecución se puede paralelizar si hay presupuesto, pero la revisión de una persona no. La lectura de esta base, coherente con la lente de restricciones y sin evidencia que la mida todavía, es que el recurso compartido que alarga el plazo pasa a ser la atención de quien revisa: está en [la atención humana como restricción](../Personas-y-agentes/la-atencion-humana-como-restriccion.md).

## Por qué la ruta más larga promete de menos

Los métodos clásicos de red (PERT y el método del camino crítico) calculan la duración del proyecto sobre la ruta de mayor suma de duraciones esperadas. Según un resumen de PMI sobre modelos de red, ese cálculo da resultados "overly optimistic" porque mira una sola ruta. MacCrimmon y Ryavec (1964) ya cuestionaron la distribución que PERT supone para cada tarea, según el resumen de su artículo.

La razón estructural es conocida en la teoría de redes, aunque esta base no la verificó con una cita: cuando varias rutas casi críticas convergen en un mismo punto, la duración esperada del proyecto es mayor que la de la ruta más larga. Basta que se atrase cualquiera de ellas para que se atrase el punto donde se juntan. En un evento con tres frentes de dos meses cada uno (sede, proveedores y difusión) que confluyen en la apertura, cada frente puede cumplir con buena probabilidad y la apertura no.

El camino crítico sirve para leer dependencias y saber dónde un atraso mueve el final. No garantiza el plazo. Para el plazo se usa un rango, como explica [pronóstico](pronostico.md).

## La cadena crítica y su evidencia

Goldratt propuso la cadena crítica como la teoría de restricciones aplicada a un proyecto. Saca el margen de cada tarea y lo junta en reservas compartidas. En la descripción habitual del método, que esta base no cotejó con el libro, la cadena se calcula contando también los recursos compartidos, y las reservas van al final de la cadena y donde otras cadenas la alimentan. Dónde van esas reservas y quién las administra está en [márgenes](../Incertidumbre-y-riesgo/margenes.md).

La evidencia del método es escasa:

- Raz, Barnes y Dvir (2003) publicaron una crítica en una revista con revisión (el informe la toma como la crítica a leer; solo se vio el registro). Según el registro, piden examinar sus ideas de cuello de botella y de reserva, y los costos de adoptarla.
- Las revisiones la siguen dando como "under investigation" (Grant y Gergely 2012, según la revisión de 2025), y la de 2025 dice que faltan validaciones empíricas en organizaciones reales.
- Un estudio de 10 casos encontró, según el resumen del buscador, que el supuesto de una cadena más larga como restricción vale solo en algunos: con equipo dedicado, el límite pasa a ser el recurso más restringido.

> [!NOTE] Sin fuente todavía: cifras de mejora atribuidas a la cadena crítica. El libro de Goldratt (1997) no se leyó y no hay metaanálisis ni ensayo verificado.

Lo que se conserva sin depender del método es la pregunta que hace: qué recurso compartido manda sobre el plazo. En un proyecto con agentes, esa pregunta es la misma que hace [flujo continuo](../Enfoque/flujo-continuo.md) sobre la cola.

El recurso canónico para la crítica es Raz, Barnes y Dvir (2003): leer qué supuestos de la cadena crítica se rompen. Para el vocabulario, las secciones de cronograma de ISO 21502 y del PMBOK, que lista la ficha de [marcos de referencia](../Fundamentos/marcos-de-referencia.md).
