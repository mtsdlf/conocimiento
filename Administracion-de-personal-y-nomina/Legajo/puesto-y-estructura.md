---
resumen: >-
  El puesto es el lugar que una persona ocupa en la empresa, y la estructura es cómo se ordenan los puestos: en qué sector está cada uno, de quién depende, a qué categoría corresponde y a qué centro de costo se carga. Esta parte del legajo decide quién aprueba lo de cada empleado, con qué escala se le paga y dónde cae su sueldo en la contabilidad.
estado: vigente
estabilidad: estable
fuentes:
  - "ERPNext, Leave Application (aprobador tomado del empleado o, si falta, del departamento; como evidencia de práctica): https://docs.frappe.io/erpnext/user/manual/en/leave-application"
  - "Martin Fowler, Temporal Patterns: Time Narrative: https://martinfowler.com/eaaDev/timeNarrative.html"
  - "Ley 27.802, texto del Boletín Oficial (art. 39, que sustituye el art. 140 de la LCT; art. 130, que sustituye el art. 4 de la Ley 14.250): https://www.boletinoficial.gob.ar/detalleAviso/primera/339128/20260306"
  - "Administracion-de-personal-y-nomina/.investigacion/legajo-y-tiempo.md, componente A2"
  - "Administracion-de-personal-y-nomina/.investigacion/argentina-laboral.md, componentes 1 y 3"
aliases: [puesto, posición, cargo, categoría, sector, departamento, organigrama, jefe directo, línea de reporte, position, job, designation, department, org chart, reporting line, position management]
creado: 2026-11-27
revisado: 2026-11-27
---

# Puesto y estructura

El puesto es el lugar que una persona ocupa en la empresa, y la estructura es cómo se ordenan los puestos: en qué sector está cada uno, de quién depende, a qué categoría corresponde y a qué centro de costo se carga. Esta parte del legajo decide quién aprueba lo de cada empleado, con qué escala se le paga y dónde cae su sueldo en la contabilidad.

## Persona y puesto, en un registro o en dos

El puesto se puede guardar de dos formas, y elegir entre ellas es una decisión de diseño (criterio de esta base):

| Diseño | Cómo se ve | Cuándo alcanza |
|---|---|---|
| El puesto como dato del empleado | el legajo tiene un campo «puesto» y otro «sector» | empresa chica, donde cada puesto lo ocupa una persona y no se planifica |
| El puesto como registro propio | el puesto existe aunque esté vacante y el empleado lo ocupa desde una fecha | cuando hace falta ver vacantes, planificar dotación o abrir una [búsqueda](busquedas-y-postulantes.md) sobre un puesto que existe antes que la persona |

En el segundo diseño, una búsqueda abierta es un puesto sin ocupante, y una renuncia deja el puesto vacante sin borrarlo.

> [!NOTE]
> Sin fuente todavía: la distinción entre puesto y persona, la vacante y el organigrama como registro, en una fuente leída (la documentación de empleado, departamento y puesto de los sistemas abiertos no se consultó).

## Las cuatro piezas que cuelgan del puesto

- **Sector o departamento.** Agrupa puestos para reportar y para aprobar. En un sistema abierto, el aprobador de una licencia se toma del empleado y, si falta, «from the department's approver table»: el departamento es el respaldo cuando el empleado no tiene jefe cargado.
- **Jefe.** Es quien aprueba las [licencias](../Tiempo-y-asistencia/licencias-y-ausencias.md) de su equipo, según el sistema abierto leído; que apruebe también las horas extra y las correcciones de [marcaciones](../Tiempo-y-asistencia/registro-de-asistencia.md) es criterio de esta base, porque en otro sistema leído las horas extra se validan en forma automática o por el gerente. Con el jefe como dato del legajo, y no como un nombre escrito en cada pedido, la aprobación sigue funcionando cuando alguien cambia de área.
- **Categoría.** El escalón que fija el sueldo mínimo y los adicionales. En países con convenios colectivos sale del convenio y no la elige la empresa (ver abajo).
- **Centro de costo.** La parte de la empresa a la que se carga el sueldo de la persona en la contabilidad de gestión. Qué es un centro de costo y cómo se reparten los costos entre centros está en [centros de costo](../../Contabilidad/Contabilidad-de-gestion/centros-de-costo.md); acá alcanza con que cada legajo tenga uno, o un reparto entre varios, con su vigencia.

## Los cambios de puesto también tienen fecha

Un ascenso, un pase de sector o un cambio de jefe valen desde una fecha, igual que un aumento. Se registran con la fecha del hecho y la fecha de registro, por la misma razón que explica el [legajo](legajo.md#la-historia-del-legajo-con-sus-dos-fechas): una propiedad temporal se consulta «parameterized by date» (Fowler). Si un pase de sector del 1 de abril se carga el 20 de abril sin fecha desde, el sueldo de abril se imputa entero al centro de costo viejo. Es inferencia de esta base.

Un ascenso o un cambio de área se decide en [Gestión de personas](../../Liderazgo-y-direccion/Gestion-de-personas/gestion-de-personas.md); acá se registra.

## La categoría en la Argentina

En la Argentina, la categoría la fija el convenio colectivo de la actividad, cuyas normas homologadas rigen para todos los trabajadores comprendidos, estén o no afiliados al sindicato (art. 4 de la Ley 14.250, sustituido por el art. 130 de la Ley 27.802). El recibo tiene que mostrar la «calificación profesional» y la «tarea o categoría» del trabajador (art. 140 incs. b e i de la LCT, sustituido por el art. 39 de la Ley 27.802). Cómo se encuadra a un empleado en un convenio está en [relación laboral en la Argentina](relacion-laboral-en-argentina.md#convenios-colectivos-y-encuadre), y cómo la categoría se vuelve escala en el recibo, en [liquidación en la Argentina](../Liquidacion-de-sueldos/liquidacion-en-argentina.md).

## Cómo falla la estructura

Como criterio de esta base, la estructura falla cuando el organigrama vive en un dibujo y no en el legajo. Las aprobaciones van a un jefe que ya no está, y el sueldo de quien cambió de área se sigue cargando al centro de costo anterior. También falla cuando la categoría se carga como texto libre: dos personas de la misma categoría quedan escritas distinto y la escala no se aplica a una de ellas.
