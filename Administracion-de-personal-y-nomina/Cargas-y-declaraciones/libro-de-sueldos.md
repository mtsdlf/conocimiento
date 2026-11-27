---
resumen: >-
  El libro de sueldos es el registro obligatorio de lo que el empleador pagó a cada empleado en cada período de liquidación: quién cobró, cuánto, por qué conceptos y qué se le retuvo. Como criterio de esta base, sirve de prueba ante el empleado, el fisco y la inspección del trabajo y se guarda durante años; y, como inferencia sobre los ejemplos leídos, en varios países la declaración periódica al fisco pasó a cumplir esa función.
estado: borrador
estabilidad: estable
fuentes:
  - "OIT, Convenio sobre la protección del salario, 1949 (núm. 95), art. 15 (copia de la Universidad de Minnesota): https://hrlibrary.umn.edu/instree/ilo95.html"
  - "IRS, Publication 15 (Circular E), Employer's Tax Guide, 2026 (ejemplo de país): https://www.irs.gov/publications/p15"
  - "Martin Fowler, Time Narrative (según un extracto): https://martinfowler.com/eaaDev/timeNarrative.html"
  - "Ley 27.802, texto del Boletín Oficial del 6/3/2026, arts. 20 y 40 (ejemplo de país): https://www.boletinoficial.gob.ar/detalleAviso/primera/339128/20260306"
  - "ARCA, Libro de Sueldos Digital, diseño de interfaz de liquidación (ejemplo de país): https://www.arca.gob.ar/LibrodeSueldosDigital/documentos/nuevos/LSDiseInterfazLiquidacion.pdf"
  - "Administracion-de-personal-y-nomina/.investigacion/liquidacion-cargas-y-fundamentos.md (2026-11-27)"
  - "Administracion-de-personal-y-nomina/.investigacion/argentina-cargas.md (2026-11-27)"
  - "Administracion-de-personal-y-nomina/.investigacion/argentina-laboral.md (2026-11-27)"
aliases: [libro de sueldos, libro de sueldos y jornales, libro especial, registro de nómina, payroll register, payroll records, employment records, conservación de registros de nómina]
creado: 2026-11-27
revisado:
---

# Libro de sueldos

El libro de sueldos es el registro obligatorio de lo que el empleador pagó a cada empleado en cada período de liquidación: quién cobró, cuánto, por qué conceptos y qué se le retuvo. Como criterio de esta base, sirve de prueba ante el empleado, el fisco y la inspección del trabajo y se guarda durante años; y, como inferencia sobre los ejemplos leídos, en varios países la declaración periódica al fisco pasó a cumplir esa función.

Cierra [cargas y declaraciones](cargas-y-declaraciones.md): es lo que queda de cada nómina cuando ya se pagó y se declaró. Lo alimenta la [liquidación de sueldos](../Liquidacion-de-sueldos/liquidacion-de-sueldos.md) al cerrar cada período; cada línea del libro corresponde a un [recibo de sueldo](../Liquidacion-de-sueldos/recibo-de-sueldo.md), que es la copia que recibe el empleado.

## Por qué la ley pide un registro

La OIT pide que la ley nacional prevea «the maintenance, in all appropriate cases, of adequate records in an approved form and manner» de los salarios (Convenio 95, art. 15). En lo leído, el convenio no dice qué tiene que contener ni cuánto se guarda, así que lo deja a cada país (inferencia de esta base).

Como criterio de esta base, el registro protege a los dos lados. Al empleado le da prueba de lo que cobró y de lo que se le retuvo para su jubilación; al empleador, prueba de que pagó. En la Argentina, cuando falta la registración, el juez presume a favor de lo que diga el trabajador sobre lo que debía constar (art. 55 de la LCT, en [relación laboral en la Argentina](../Legajo/relacion-laboral-en-argentina.md#la-registración-ante-arca)).

## Qué contiene

Las fuentes agnósticas leídas no listan el contenido mínimo. El ejemplo argentino sí lo muestra, porque el archivo que el empleador le entrega al fisco para armar el libro tiene un registro por nivel (ARCA, diseño de interfaz del Libro de Sueldos Digital):

| Nivel | Qué lleva |
|---|---|
| El envío | empleador, período, tipo de liquidación (mensual, quincenal, semanal), número de liquidación, cantidad de trabajadores |
| Cada empleado | identificación, número de legajo, cuenta donde cobra, fecha de pago, forma de pago |
| Cada concepto | código del concepto, cantidad, unidad, importe, si suma o resta, y el período al que corresponde si es un ajuste retroactivo |
| Los datos para las cargas | cónyuge, hijos, convenio colectivo, seguro de vida, reducciones |

Generalizado, como criterio de esta base: un libro de sueldos tiene una fila por empleado, período y concepto, con el importe, y lo necesario para rehacer el cálculo de las cargas. Es la misma estructura que el recibo, junta para todos.

El campo del período de ajuste importa: un retroactivo se registra en el período en que se paga, pero dice a qué período corresponde. Es lo que permite recalcular las cargas del mes original sin tocar lo que ya se registró ([retroactivos y reliquidaciones](../Liquidacion-de-sueldos/retroactivos-y-reliquidaciones.md)).

## Lo registrado no se edita

Un libro de sueldos es un registro de movimientos: lo que se cerró no se corrige encima, se corrige con un movimiento nuevo. Fowler usa justamente un sistema de nómina para explicarlo: distingue la fecha en que algo pasó de la fecha en que se supo, y dice que las correcciones son entradas nuevas, porque los cambios retroactivos sobre lo registrado «break the integrity of the record». Cómo se modela eso está en [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md#un-error-se-corrige-con-otro-movimiento).

En la Argentina, el sistema del fisco lo hace cumplir: una liquidación aceptada no se puede cambiar, y un concepto que ya se usó en una liquidación no se puede editar ni borrar ([libro de sueldos digital](libro-de-sueldos-digital.md)).

## Cuánto se guarda

Cada país fija el plazo, y suele haber más de uno según para qué sirve el registro:

| País (ejemplo) | Qué se guarda | Plazo |
|---|---|---|
| EE. UU. | los registros de las cargas sobre el empleo | «at least 4 years» (IRS, Pub. 15; una sola fuente) |
| Argentina | los libros laborales anteriores a la Ley 27.802 | «diez (10) años» (art. 52 de la LCT, texto del art. 20 de la Ley 27.802) |
| Argentina | los recibos | según la prescripción de las obligaciones laborales (2 años) y previsionales (10 años), y pueden digitalizarse (art. 143 de la LCT, texto del art. 40 de la Ley 27.802) |

El plazo más largo manda: si un mismo registro sirve de prueba laboral y previsional, se guarda por el previsional (inferencia de esta base). Lo que se guarda tiene datos personales y, a veces, sensibles (obra social, embargos, cargas de familia); quién puede verlo está en [legajo](../Legajo/legajo.md#quién-ve-el-legajo) y el marco general en [privacidad de datos personales](../../Datos/Gobierno-y-calidad/privacidad-de-datos-personales.md).

> [!NOTE]
> Sin fuente todavía: el plazo de conservación del Reino Unido (la página probada no existía) y una lista agnóstica del contenido mínimo del registro.

## Del libro rubricado a la declaración al fisco

En la Argentina, el libro era el Libro Especial del art. 52 de la LCT o un registro de hojas móviles, y la autoridad del trabajo de cada provincia lo rubricaba (RG 5249/2022 para el libro; RG 5250/2022, arts. 6 y 7, y Guía 8 de ARCA para la rúbrica provincial, en [libro de sueldos digital](libro-de-sueldos-digital.md)). La tendencia en los ejemplos leídos es que el registro lo arme el fisco con lo que el empleador declara cada período. En el Reino Unido, el empleador informa cada pago en el momento ([cargas y declaraciones](cargas-y-declaraciones.md#la-declaración-periódica)). En la Argentina hubo dos pasos: primero el libro digital que arma ARCA con las liquidaciones del empleador, y después la Ley 27.802, según la cual la registración ante ARCA «será suficiente a todos los efectos». El detalle, y lo que todavía no está claro, está en [libro de sueldos digital](libro-de-sueldos-digital.md).

Para quien construye el sistema, el cambio no elimina el registro: lo traslada. El empleador sigue necesitando su propio historial por empleado, período y concepto para reliquidar, contestar un reclamo o rehacer una declaración (inferencia de esta base).
