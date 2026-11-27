---
tema: Administración de personal y nómina
para: entender qué registra y qué calcula una empresa sobre la gente que trabaja en ella (el legajo, el tiempo trabajado y las ausencias, la liquidación del sueldo y lo que se les debe a terceros por cada nómina), para quien construye software de gestión y, en segundo lugar, para quien lo vende o lo implementa
nivel: sabe de software y de negocio, no es liquidador de sueldos ni abogado laboralista; no se da por sabido qué es un concepto de liquidación, un aporte o una licencia paga
escuela: neutral; el dominio se cuenta como registro y cálculo, y las decisiones sobre las personas quedan en Liderazgo y dirección
fuera:
  - decidir sobre las personas (cómo seleccionar, cuánto pagar o aumentar, cómo evaluar, por qué se va la gente y cómo se despide), que es Liderazgo-y-direccion/Gestion-de-personas; acá solo se registra y se liquida lo que allá se decide
  - el asiento contable de sueldos y cargas, que está en Contabilidad/Operaciones (sección «Cómo se registran los sueldos»); acá, el cálculo que lo alimenta
  - los gastos de empleados, anticipos y rendiciones, que están en Contabilidad/Operaciones/gastos-y-rendiciones
  - el impuesto a las ganancias como impuesto (alícuotas, categorías, declaración de la empresa), que va al tema Impuestos; acá, el empleador como agente de retención sobre el sueldo
  - la ejecución del pago y la posición de caja, que van al tema Tesorería y finanzas de la empresa en marcha; acá, qué se paga a quién y cuándo vence
  - la carga de horas por proyecto y su facturación, que va al tema Servicios profesionales y proyectos; acá, la asistencia y la jornada
  - el recorrido de punta a punta de la contratación a la baja (hire-to-retire), que va al tema Procesos de negocio
  - cómo lo resuelve un software (datos maestros, documento y estados, fechas y vigencias, permisos, auditoría como columnas técnicas), que va al tema Software de gestión
  - capacitación, evaluación del desempeño, planes de carrera, clima y beneficios como política, salud y seguridad en el trabajo como disciplina, relaciones sindicales y negociación colectiva
  - productos de nómina o de RR. HH., comparativas y precios
fuentes: []
preguntas:
  - "Tengo que diseñar el legajo de un sistema: ¿qué datos lleva un empleado, cuáles cambian con el tiempo y cómo guardo que el sueldo o el puesto cambiaron desde una fecha?"
  - "¿Cómo pasa una marcación del reloj o una licencia aprobada a ser un número en el recibo de sueldo?"
  - "¿Qué es un concepto de liquidación, por qué importa el orden en que se calculan y qué diferencia hay entre remunerativo y no remunerativo?"
  - "Se firmó un aumento retroactivo a tres meses atrás: ¿cómo se reliquida sin tocar lo que ya se pagó y se declaró?"
  - "¿Qué le debe el empleador a terceros por cada nómina (aportes, contribuciones, retenciones) y qué tiene que declarar?"
  - "Voy a contratar a la primera persona de una empresa argentina: ¿qué tengo que dar de alta, qué cargas pago y qué tiene que llevar el recibo?"
aprobado:
---

# Alcance: Administración de personal y nómina

El tema cubre el dominio de negocio que lleva el módulo de personal y nómina de un software de gestión (lo que el mercado llama HCM en su parte administrativa, más la liquidación de sueldos): el registro del empleado, el tiempo que trabaja y las ausencias, la liquidación de su sueldo y lo que el empleador les debe a la seguridad social y al fisco por cada nómina. Sale del mapa «el mundo del software de gestión» (issue #94) y de sus decisiones: forma del árbol (#95), taxonomías externas (#96), columnas técnicas (#97), huecos (#104), límites entre dominios (#98), procesos de punta a punta (#99), verticales de Software de gestión (#100) y orden de armado (#101). Es la sesión 10 de 16 (issue #117). El árbol general y los límites los aprobó la persona en el mapa; el árbol de este tema lo propone esta sesión sin esperar respuesta, por indicación de quien la abrió, y queda para revisar en el PR.

Es un tema agnóstico: lo que dice vale para cualquier país y cualquier producto, sin nombrar proveedores, y se sostiene sin software (un legajo en carpeta, una planilla de asistencia y un recibo hecho a mano hacen lo mismo). Lo propio de la Argentina va en notas aparte, dentro de la vertical que toca cada una.

## Límites con los vecinos

Cada dominio es dueño de un objeto y un verbo (decisión de #98). Este tema es dueño del **legajo**, de **la asistencia y las licencias** y de **la liquidación**, con los verbos **registrar** y **liquidar**: quién trabaja acá, en qué condiciones, cuánto tiempo trabajó y cuánto se le paga y se les paga a terceros por eso.

| Vecino | Es dueño de | La frontera con este tema |
|---|---|---|
| [Gestión de personas](../Liderazgo-y-direccion/Gestion-de-personas/gestion-de-personas.md), en Liderazgo y dirección | decidir: seleccionar, evaluar, cuánto pagar, cómo despedir | Allá se decide un aumento; acá se registra con su fecha de vigencia y se liquida. Allá, cómo seleccionar; acá, la búsqueda y el postulante como registro. Allá, por qué se va la gente; acá, la baja y la liquidación final |
| [Contabilidad](../Contabilidad/contabilidad.md) | el asiento de sueldos y cargas, los gastos de empleados y su rendición | La nómina liquidada es el documento que dispara el asiento; el asiento y su devengamiento son de allá ([operaciones](../Contabilidad/Operaciones/operaciones.md)). Los anticipos de gastos, en [gastos y rendiciones](../Contabilidad/Operaciones/gastos-y-rendiciones.md); los adelantos de sueldo, acá |
| Impuestos (no armado) | los impuestos como tales y la declaración de la empresa | Acá, el empleador como agente de retención del impuesto sobre el sueldo y las cargas sociales; las alícuotas del impuesto y la declaración de la empresa, allá |
| Tesorería y finanzas de la empresa en marcha (no armado) | pagar y cuidar la caja | Acá, cuánto se paga a cada uno y cuándo vence cada carga; la transferencia y la posición de caja, allá |
| Servicios profesionales y proyectos (no armado) | la carga de horas por proyecto y su facturación | La asistencia dice que alguien trabajó ocho horas; en qué proyecto y a quién se le facturan, allá |
| Procesos de negocio (no armado) | el recorrido de la contratación a la baja | Cada paso se explica acá; la cadena entera, allá |
| Software de gestión (no armado) | las columnas técnicas | Acá, que un sueldo cambia desde una fecha; cómo se modela una vigencia o un registro que no se edita, allá y en [registro de movimientos](../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md) |
| [Emprender](../Emprender/emprender.md) | las decisiones de una vez de una empresa que empieza | La primera contratación (hacerse empleador) se explica acá y Emprender la enlaza |
| [Datos/Gobierno-y-calidad](../Datos/Gobierno-y-calidad/privacidad-de-datos-personales.md) | la privacidad de los datos personales en general | Acá, qué datos sensibles tiene un legajo y quién los ve; el marco general, allá |

Los temas que todavía no existen se nombran sin enlace; la sesión 16 del mapa los enlaza.

## Árbol

```
Administracion-de-personal-y-nomina/
  administracion-de-personal-y-nomina.md   el todo: los cuatro objetos, el ciclo mensual y los vecinos; qué leer según lo que estés haciendo
  Legajo/                                  quién trabaja y en qué condiciones
    legajo                                   entrada: el registro del empleado, sus documentos y su historia con vigencias
    puesto-y-estructura                      persona frente a puesto, categoría, sector, jefe y centro de costo
    modalidades-de-contratacion              indeterminado, plazo fijo, eventual, tiempo parcial, período de prueba; empleado o independiente
    ingreso-y-egreso                         el alta y la baja administrativas, y la primera contratación
    busquedas-y-postulantes                  la búsqueda y el postulante como registro
    relacion-laboral-en-argentina            LCT, registración, modalidades, convenios y encuadre, certificado de trabajo, hacerse empleador
  Tiempo-y-asistencia/                     cuánto se trabajó y cuánto se faltó
    tiempo-y-asistencia                      entrada: del turno a la novedad que llega a la liquidación
    jornada-y-turnos                         jornada, turnos, horas extra y banco de horas
    registro-de-asistencia                   marcaciones, ausencias, tardanzas y su conciliación con el turno
    licencias-y-ausencias                    tipos de licencia, saldos y devengamiento de vacaciones, solicitud y aprobación
    jornada-y-licencias-en-argentina         jornada legal, horas extra, vacaciones por antigüedad, licencias de la LCT, feriados
  Liquidacion-de-sueldos/                  cuánto se le paga a cada uno
    liquidacion-de-sueldos                   entrada: el ciclo (novedades, cálculo, control, cierre, pago, contabilización)
    conceptos-de-liquidacion                 haberes y deducciones, base de cálculo, orden, proporcionales, remunerativo
    recibo-de-sueldo                         qué lleva el comprobante, conformidad y entrega
    retroactivos-y-reliquidaciones           pagar diferencias de un período cerrado sin editarlo
    liquidacion-final                        lo que se paga al terminar la relación
    liquidacion-en-argentina                 aguinaldo, recibo de la LCT, plazo de pago, sumas no remunerativas, indemnización, embargos
  Cargas-y-declaraciones/                  lo que se les debe a terceros por cada nómina
    cargas-y-declaraciones                   entrada: aportes, contribuciones y retenciones; la declaración periódica
    aportes-y-contribuciones                 lo retenido al empleado y lo que paga el empleador; bases y topes; seguro de accidentes
    retencion-de-impuestos-sobre-sueldos     el empleador como agente de retención del impuesto sobre la renta del empleado
    libro-de-sueldos                         el registro obligatorio de la nómina y cuánto se guarda
    cargas-sociales-en-argentina             SIPA, obra social, PAMI, ART, seguro de vida y la declaración mensual
    ganancias-sobre-sueldos-en-argentina     cuarta categoría, deducciones del empleado y liquidación anual
    libro-de-sueldos-digital                 el libro del art. 52 en su versión digital de ARCA y su paso a la declaración
  Fundamentos/
    fundamentos-de-administracion-de-personal  entrada: historia, cómo dividen el dominio los marcos, posiciones contrarias y mitos
    glosario-de-administracion-de-personal     los términos del tema con su nombre en inglés
    fuentes-de-administracion-de-personal      dónde se produce el saber del dominio y qué leer
```

## Supuestos

- **Cuatro verticales, por objeto.** Legajo, Tiempo y asistencia, Liquidación de sueldos, y Cargas y declaraciones. Siguen el orden en que se usa la información cada mes (quién es, cuánto trabajó, cuánto cobra, cuánto se les debe a terceros) y calcan cómo cortan los productos abiertos (empleado, asistencia y turnos, licencias, nómina, impuestos y beneficios) y lo que APQC pone en 7.0 y en 9.5. SHRM divide el saber de RR. HH. de otra forma (personas, organización, lugar de trabajo) porque incluye la parte que acá es de Liderazgo.
- **Cargas y declaraciones se separa de la liquidación.** Liquidar es calcular lo de cada empleado; las cargas son la obligación del empleador frente a terceros, con su propia declaración y su propio vencimiento. Se puede unir a Liquidación si queda flaca.
- **El pago de sueldos no tiene nota propia**: va como sección de la entrada de Liquidación (medio de pago, adelantos, embargos), porque la ejecución del pago es de Tesorería.
- **La primera contratación**, que el mapa pasa de Emprender a este tema, va como sección de `ingreso-y-egreso` (lo general) y de `relacion-laboral-en-argentina` (los trámites del país).
- **Los convenios colectivos** van dentro de `relacion-laboral-en-argentina` (el encuadre del empleado) y se usan en `liquidacion-en-argentina` (la escala).
- **Lo de Argentina, en seis notas**, cada una en la vertical que toca. La Ley 27.802 de Modernización Laboral (marzo de 2026) cambió parte de la Ley de Contrato de Trabajo y su constitucionalidad sigue en discusión judicial: cada nota dice qué texto usa y a qué fecha.
- **Después de investigar** (2026-11-27): el árbol se mantuvo. La Ley 27.802 cambió el art. 52 de la LCT y el Decreto 407/2026 dejó de exigir libros laborales, mientras las resoluciones de ARCA del libro de sueldos digital siguen vigentes: la tensión queda a la vista en `libro-de-sueldos-digital` y no se resolvió. El Fondo de Asistencia Laboral rige desde el 1 de diciembre de 2026 (Decreto 1228/2026); algunas fuentes secundarias dan otra fecha, y se siguió el decreto.
- **Huecos que quedan para otra pasada**: la cuota de la ART, el seguro de vida obligatorio, los topes de la base imponible y el vencimiento de la declaración mensual en la Argentina; el plazo del alta temprana; las proporciones embargables del Decreto 484/87; las sumas no remunerativas de convenio; un ciclo de liquidación agnóstico con fuente (el de la nota es síntesis de la base); el orden de cálculo de los conceptos y el divisor de los proporcionales; los informes del Auditor General de Canadá sobre Phoenix, APQC 7.4/8.0, Payroll.org y los libros de texto de RR. HH., que no se pudieron leer.
- **Fuera**: capacitación, evaluación, carrera, clima y beneficios como política (son decisiones de Liderazgo o temas propios), salud y seguridad en el trabajo como disciplina, y las relaciones sindicales.
