---
resumen: >-
  Descomponer el trabajo es partir todo el alcance en piezas definidas por lo que entregan, hasta llegar a paquetes que se pueden estimar, asignar a un responsable y verificar uno por uno.
estado: borrador
estabilidad: estable
fuentes:
  - "PMI, Practice Standard for Work Breakdown Structures, 2.ª y 3.ª ed. (según resúmenes; no se leyó el texto): https://www.pmi.org/learning/library/practice-standard-work-breakdown-structures-8063"
  - "PMI, Work Breakdown Structures Third Edition (según resumen): https://www.pmi.org/fr-fr/pmiheadless/home/standards/work-breakdown-structures-third-edition"
  - "PMI, blog sobre la estructura de desglose del trabajo (según resumen): https://www.pmi.org/blog/work-breakdown-structure"
  - "Gestion-de-proyectos/.investigacion/planificacion-y-riesgo.md"
aliases: [EDT, estructura de desglose del trabajo, WBS, work breakdown structure, paquete de trabajo, work package, regla del 100 %, 100% rule]
creado: 2026-11-27
revisado:
---

# Descomposición del trabajo

Descomponer el trabajo es partir todo el alcance en piezas definidas por lo que entregan, hasta llegar a paquetes que se pueden estimar, asignar a un responsable y verificar uno por uno.

La forma clásica es la estructura de desglose del trabajo (EDT, o WBS en inglés): un árbol cuya raíz es el resultado del proyecto y cuyas hojas son los paquetes de trabajo. Es la primera pieza de la [planificación](planificacion.md), porque las [dependencias](dependencias-y-camino-critico.md), el [pronóstico](pronostico.md) y el [costo](capacidad-y-costo.md) se calculan sobre esas hojas. Lo que entra y lo que no en el árbol lo fija el [alcance](../Encuadre/alcance.md).

## La regla del 100 %

El árbol contiene todo el trabajo del alcance y nada fuera de él, incluida la gestión del propio proyecto. La regla vale en cada nivel. Según resúmenes del estándar de PMI sobre EDT, "the sum of the work at the 'child' level must equal 100% of the work represented by the 'parent'". La 2.ª edición del estándar la trata en su sección 2.4.

La regla sirve para encontrar trabajo que nadie anotó. En la mudanza de una plataforma, el árbol suele traer "migrar los datos" y "configurar el entorno nuevo", y olvidarse de "apagar el entorno viejo" o de "avisar a los usuarios". Si los hijos de "mudanza terminada" no suman la mudanza entera, falta una rama.

## Por entregable, no por actividad

Cada elemento del árbol se nombra por lo que entrega, no por lo que se hace. Según el mismo resumen de PMI, cuando un padre se descompone en acciones, es fácil que los hijos sumen más del 100 %, porque las acciones se superponen. "Diseñar", "construir" y "probar" son actividades que cruzan todas las piezas. "El formulario de alta funcionando", "el contrato firmado con el proveedor" y "el salón reservado y pagado" son entregables, y cada uno se puede comprobar por separado.

Descomponer por entregable es lo que permite [aceptar con evidencia](../Seguimiento/aceptar-con-evidencia.md): una pieza está terminada cuando su entregable cumple lo pedido, no cuando alguien dice que terminó la actividad. Por la misma razón, el [resultado del proyecto](../Encuadre/resultado-y-terminado.md) tiene que estar escrito como algo comprobable antes de empezar a partirlo.

## El paquete de trabajo

La hoja del árbol es el paquete de trabajo. PMI lo define, según su blog, como "lowest level of the work breakdown structure for which cost and duration are estimated and managed". Tiene un identificador único y un solo responsable. Qué tan chico tiene que ser no lo fija ninguna fuente con método: se para de partir cuando la pieza se puede estimar, asignar y verificar sin partirla más.

Según un resumen de la 3.ª edición del estándar, la EDT se aplica a ciclos predictivos, iterativos, incrementales y ágiles. En un [enfoque iterativo](../Enfoque/enfoque-iterativo.md) el árbol se detalla por tramos: el próximo tramo baja hasta paquetes, y los siguientes quedan en ramas gruesas que se parten cuando se acercan.

> [!NOTE] Sin fuente todavía: un estudio con método sobre si descomponer más fino mejora el pronóstico o el resultado del proyecto. El texto completo del estándar de PMI no se leyó.

## Paquetes que ejecuta un agente

Un paquete que va a ejecutar un agente necesita algo que una persona a veces suple con criterio: un chequeo de aceptación que se pueda correr desde afuera. Si el criterio es "que quede bien", nadie puede verificar si el agente terminó o solo dice que terminó. Es una inferencia de esta base. Lo apoya que una taxonomía de fallas de sistemas multiagente (Cemri et al., según un resumen) incluye la terminación prematura y la verificación incompleta o incorrecta; no hay medición de cuánto pasa, y lo que se hace con eso está en [aceptar con evidencia](../Seguimiento/aceptar-con-evidencia.md).

El tamaño del paquete también cambia. Con personas se parte hasta lo que se puede estimar; con un agente, según la lectura de esta base y sin fuente que lo pruebe, hasta lo que completa con confianza razonable, y ese largo se mide en la ficha de [horizonte de tareas](../Personas-y-agentes/horizonte-de-tareas.md). Cómo se le pasa el paquete, con intención, límites y criterio de terminado, está en [delegar a un agente](../Personas-y-agentes/delegar-a-un-agente.md). Para software, partir un trabajo en tareas que un agente de código hace en una sesión está en [descomposición en tareas](../../Desarrollo/Definicion/descomposicion-en-tareas.md), y cómo se escribe el chequeo, en [criterios de aceptación](../../Desarrollo/Definicion/criterios-de-aceptacion.md).

El recurso canónico es el estándar de PMI sobre EDT, 3.ª edición: leer la definición de paquete de trabajo y la regla del 100 %, y fijarse en que partir por entregable, no por fase ni por actividad, es lo que permite verificar cada pieza.
