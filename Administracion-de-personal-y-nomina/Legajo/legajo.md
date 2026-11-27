---
resumen: >-
  El legajo es el registro de cada persona que trabaja en la empresa: quién es, en qué puesto y con qué contrato trabaja, cuánto gana, qué documentos lo respaldan y cómo cambió cada dato con el tiempo. Es el dato maestro del tema: el tiempo trabajado, la liquidación y las cargas leen de él.
estado: vigente
estabilidad: estable
fuentes:
  - "Martin Fowler, Temporal Patterns: Time Narrative (Effectivity, Temporal Property, tiempo actual y tiempo de registro): https://martinfowler.com/eaaDev/timeNarrative.html"
  - "29 CFR 516.2, datos que se guardan por empleado (EE. UU.), vía Cornell LII: https://www.law.cornell.edu/cfr/text/29/516.2"
  - "29 CFR 516.5, conservación de registros de nómina, 3 años (EE. UU.): https://www.law.cornell.edu/cfr/text/29/516.5"
  - "29 CFR 516.6, conservación de registros complementarios, 2 años (EE. UU.): https://www.law.cornell.edu/cfr/text/29/516.6"
  - "ERPNext, Leave Application (la licencia como registro con fechas, como evidencia de práctica): https://docs.frappe.io/erpnext/user/manual/en/leave-application"
  - "Ley 27.802, texto del Boletín Oficial (arts. 20 y 40, que sustituyen los arts. 52 y 143 de la LCT): https://www.boletinoficial.gob.ar/detalleAviso/primera/339128/20260306"
  - "Datos/Gobierno-y-calidad/privacidad-de-datos-personales.md (arts. 2 y 4 de la Ley 25.326)"
  - "Administracion-de-personal-y-nomina/.investigacion/legajo-y-tiempo.md, componente A1"
  - "Administracion-de-personal-y-nomina/.investigacion/argentina-laboral.md"
aliases: [legajo del empleado, legajo personal, ficha del empleado, maestro de empleados, employee record, personnel file, employee master data, core HR]
creado: 2026-11-27
revisado: 2026-11-27
---

# Legajo

El legajo es el registro de cada persona que trabaja en la empresa: quién es, en qué puesto y con qué contrato trabaja, cuánto gana, qué documentos lo respaldan y cómo cambió cada dato con el tiempo. Es el dato maestro del tema: el tiempo trabajado, la liquidación y las cargas leen de él.

Es la primera vertical de [Administración de personal y nómina](../administracion-de-personal-y-nomina.md) y la que menos se mueve. Le da a [Tiempo y asistencia](../Tiempo-y-asistencia/tiempo-y-asistencia.md) el turno y el saldo de licencias de cada persona. A [Liquidación de sueldos](../Liquidacion-de-sueldos/liquidacion-de-sueldos.md) le da el sueldo, la categoría y las condiciones del contrato, y a [Cargas y declaraciones](../Cargas-y-declaraciones/cargas-y-declaraciones.md), los datos con que el empleador declara a cada uno ante la seguridad social. Como todo [dato maestro](../../Datos/Gobierno-y-calidad/datos-maestros.md), se carga una vez y los documentos lo referencian. Sin software, es la carpeta de cada empleado en un armario; con software, la tabla que leen todos los módulos.

## Qué datos lleva un legajo

Ninguna fuente leída da una lista agnóstica. La norma de Estados Unidos sirve de ejemplo: por cada empleado alcanzado por el salario mínimo y las horas extra, el empleador guarda, entre otros, el nombre legal, el domicilio, la fecha de nacimiento si tiene menos de 19 años, el sexo y la ocupación. También guarda la base de pago, las horas por día y por semana, lo ganado, el recargo por horas extra, los agregados y descuentos al sueldo, y la fecha y el período de pago (29 CFR 516.2).

Como criterio de esta base, los datos se ordenan por lo que hace cada uno en cinco grupos:

| Grupo | Ejemplos | Quién lo lee |
|---|---|---|
| Identidad | nombre, documento, domicilio, fecha de nacimiento, identificación ante la seguridad social | todos |
| Contrato | fecha de ingreso, [modalidad](modalidades-de-contratacion.md), jornada, fin del período de prueba | liquidación, tiempo |
| Puesto | [puesto, categoría, sector, jefe, centro de costo](puesto-y-estructura.md) | liquidación, contabilidad, aprobaciones |
| Pago | sueldo o tarifa, cuenta donde se acredita, conceptos fijos | liquidación |
| Fiscal y previsional | datos para la retención del impuesto, obra social o seguro de salud, cargas de familia | cargas y declaraciones |

En la Argentina, el recibo lleva el CUIL, la calificación profesional, la fecha de ingreso o la antigüedad reconocida y la tarea o categoría del trabajador (art. 140 LCT). Todo eso va en el legajo antes de liquidar. El detalle del país está en [relación laboral en la Argentina](relacion-laboral-en-argentina.md), y el contenido del recibo, en [liquidación en la Argentina](../Liquidacion-de-sueldos/liquidacion-en-argentina.md).

## Los documentos que respaldan el registro

El legajo guarda los datos y los papeles de donde salieron: el contrato firmado, la constancia del alta ante la seguridad social, los certificados médicos que justifican una licencia, las notificaciones de un cambio de puesto o de sueldo, la renuncia o el telegrama de despido. En los sistemas abiertos leídos, una licencia aprobada es un registro propio con empleado, tipo, fecha desde, fecha hasta y estado; no se guarda en un campo del empleado que se pisa.

> [!NOTE]
> Sin fuente todavía: una lista agnóstica de los documentos que integran un legajo y de cómo se archivan.

## La historia del legajo con sus dos fechas

Un sueldo, un puesto o una jornada tienen una sucesión de valores, cada uno desde una fecha. Fowler llama a esto una propiedad temporal, «an accessor that is parameterized by date»: en lugar de «cuál es el sueldo», se pregunta «cuál era el sueldo el 25 de febrero».

Fowler distingue dos tiempos. El tiempo actual es «the time something happened» (en el legajo, la fecha desde la que vale un cambio) y el tiempo de registro es «the time we knew about it» (la fecha en que se cargó). Su regla es que «bi-temporal information always needs both dates». El legajo necesita las dos porque los cambios llegan tarde a menudo.

Un caso: el 10 de mayo se firma un aumento que vale desde el 1 de marzo. El legajo lo registra con fecha del hecho 1 de marzo y fecha de registro 10 de mayo. Las dos fechas contestan dos preguntas:

- Qué sueldo correspondía en marzo: el nuevo, por la fecha del hecho. La [reliquidación](../Liquidacion-de-sueldos/retroactivos-y-reliquidaciones.md) lo usa para calcular la diferencia.
- Con qué sueldo se liquidó marzo: el viejo, porque al cerrar marzo el aumento no estaba registrado. Eso explica el recibo de marzo ya pagado y declarado.

Sin la fecha de registro, la segunda pregunta queda sin respuesta y la reliquidación no sabe cuánto se pagó de menos. Es inferencia de esta base sobre el patrón de Fowler. Cómo guarda una base de datos un cambio sin pisar el anterior está en [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md); cómo lo resuelve un software de gestión, en [fechas, vigencias y cierre](../../Software-de-gestion/Columnas-tecnicas/fechas-vigencias-y-cierre.md).

La vigencia vale igual para todos los datos que cambian: el [puesto](puesto-y-estructura.md), la [modalidad del contrato](modalidades-de-contratacion.md) y la jornada. Este tema registra el cambio con su fecha; un aumento se decide en [compensación e incentivos](../../Liderazgo-y-direccion/Gestion-de-personas/compensacion-e-incentivos.md).

## Quién ve el legajo

El legajo junta datos que la ley trata como sensibles. En la Argentina, la Ley 25.326 llama sensibles, entre otros, a la «afiliación sindical» y a la «información referente a la salud» (art. 2), y pide datos «adecuados, pertinentes y no excesivos» para su finalidad (art. 4 inc. 1); está en [privacidad de datos personales](../../Datos/Gobierno-y-calidad/privacidad-de-datos-personales.md). Según la lectura de esta base, un certificado médico con diagnóstico y una retención de cuota sindical aparecen en cualquier legajo argentino.

Como inferencia de esta base, el diseño separa lo que ve cada rol: el jefe ve el puesto y las licencias de su equipo, quien liquida ve el sueldo y los datos fiscales, y el diagnóstico de un certificado lo ve solo quien tiene que controlarlo.

> [!NOTE]
> Sin fuente todavía: una guía oficial sobre acceso al legajo y datos de salud del empleado (la guía de prácticas de empleo de la autoridad del Reino Unido no se pudo leer).

## Cuánto se guarda

Cada país fija el plazo de conservación; no hay un valor agnóstico. Dos ejemplos, cada uno con una sola fuente:

| País | Qué se guarda | Plazo | Norma |
|---|---|---|---|
| EE. UU. | registros de nómina y de empleados | «at least 3 years» desde la última anotación | 29 CFR 516.5 |
| EE. UU. | tarjetas de tiempo, tablas de tarifas, registros de descuentos | «at least 2 years» | 29 CFR 516.6 |
| Argentina | recibos de sueldo | según la prescripción laboral (2 años) y la previsional (10 años) | art. 143 LCT |
| Argentina | libros laborales anteriores a la Ley 27.802 | 10 años | art. 52 LCT |

El vencimiento de un plazo no obliga a borrar todo junto: el recibo argentino se guarda diez años por lo previsional aunque lo laboral prescriba a los dos (inferencia de esta base sobre el art. 143). En el otro sentido, la ley de datos personales pide destruir los datos «cuando hayan dejado de ser necesarios o pertinentes» (art. 4 inc. 7 de la Ley 25.326, según la [nota de privacidad](../../Datos/Gobierno-y-calidad/privacidad-de-datos-personales.md)).

## Cómo falla el legajo

Como criterio de esta base, el legajo falla de tres maneras, y las tres aparecen recién en el recibo:

1. Un dato que se pisa. El sueldo cambia sin fecha desde y el mes pasado queda liquidado con un valor que el sistema ya no tiene.
2. Una novedad que llega tarde sin fecha de registro. El aumento retroactivo se carga como si valiera desde hoy y la diferencia no se paga.
3. Un dato que vive en otro lado. El jefe o el centro de costo se escriben a mano en cada aprobación o asiento, y cada uno los escribe distinto.

## Qué hay en el legajo

- [Puesto y estructura](puesto-y-estructura.md): la persona frente al puesto que ocupa, la categoría, el sector, el jefe y el centro de costo.
- [Modalidades de contratación](modalidades-de-contratacion.md): plazo indeterminado, plazo fijo, eventual, tiempo parcial, período de prueba, y cuándo alguien es empleado y no independiente.
- [Ingreso y egreso](ingreso-y-egreso.md): el alta y la baja administrativas, y qué cambia la primera vez que una empresa contrata.
- [Búsquedas y postulantes](busquedas-y-postulantes.md): la búsqueda abierta y cada postulante como registro, antes de que exista el legajo.
- [Relación laboral en la Argentina](relacion-laboral-en-argentina.md): la Ley de Contrato de Trabajo, la registración, el período de prueba, los convenios, el certificado de trabajo y la primera contratación en el país, con los cambios de 2024 y 2026.
