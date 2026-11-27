---
resumen: >-
  Los controles sobre los sistemas son las actividades de control que cuidan la tecnología con que se registra (quién entra, quién cambia los programas, cómo se opera y qué queda anotado de cada acción), para que los controles automáticos y los datos contables sean confiables.
estado: vigente
estabilidad: estable
fuentes:
  - "COSO, Internal Control — Integrated Framework, Executive Summary (2013), principio 11: https://www.coso.org/_files/ugd/3059fc_1df7d5dd38074006bce8fdf621a942cf.pdf"
  - "John White, How to use COSO to assess IT controls, Journal of Accountancy (1 de mayo de 2014): https://www.journalofaccountancy.com/issues/2014/may/coso-it-controls-20138951"
  - "GAO, Standards for Internal Control in the Federal Government (Green Book), principio 11, párrafos 11.05 a 11.16, citados en Indiana State Board of Accounts, cap. 14 Information Technology Controls: https://secure.in.gov/sboa/files/CH14-Information-Technology-Controls_9-25.pdf"
  - "IIA, GTAG 8 Auditing Application Controls (2007), según su resumen y la cita del manual de Indiana"
  - "OpenStax, Principles of Financial Accounting (2019), 8.6, ejemplo de Feeter Plumbing: https://openstax.org/books/principles-financial-accounting/pages/8-6-define-the-purpose-of-a-bank-reconciliation-and-prepare-a-bank-reconciliation-and-its-associated-journal-entries"
  - "Contabilidad/.investigacion/control-interno.md, sección «Ampliación para controles sobre sistemas» (2026-11-27)"
aliases: [controles generales de tecnología, controles generales de TI, IT general controls, ITGC, technology general controls, controles de aplicación, application controls, pista de auditoría, audit trail, bitácora]
creado: 2026-11-27
revisado: 2026-11-27
---

# Controles sobre los sistemas

Los controles sobre los sistemas son las actividades de control que cuidan la tecnología con que se registra (quién entra, quién cambia los programas, cómo se opera y qué queda anotado de cada acción), para que los controles automáticos y los datos contables sean confiables.

COSO les dedica un principio propio, el 11 de sus 17: "The organization selects and develops general control activities over technology to support the achievement of objectives." Está dentro del componente de actividades de control, al lado de la [separación de funciones](separacion-de-funciones.md), las [autorizaciones](autorizaciones.md) y las [conciliaciones](conciliaciones.md); el marco entero está en [control interno](control-interno.md). Es la nota que más le sirve a quien construye un sistema de gestión, porque describe, por inferencia de la base, lo que un auditor va a mirar del sistema y no de la contabilidad.

## Controles generales y controles de aplicación

La Green Book de la GAO, el marco de control interno del gobierno federal de Estados Unidos, distingue dos tipos de control en un sistema de información. Los controles generales "are the policies and procedures that apply to all or a large segment of an entity's information systems". Los de aplicación "are incorporated directly into computer applications to achieve validity, completeness, accuracy, and confidentiality of transactions and data during application processing".

| | Controles generales | Controles de aplicación |
|---|---|---|
| Alcance | Todo el sistema o una parte grande | Un proceso o una pantalla |
| Ejemplos | Quién tiene usuario, cómo se aprueba un cambio al programa, las copias de respaldo | Rechazar una factura duplicada, exigir que el asiento balancee, bloquear un pago sin aprobación |
| Qué aseguran | Que los controles de aplicación sigan funcionando | Que cada operación entre completa, exacta y válida |

Los dos dependen uno del otro. Un control de aplicación como «no se paga una factura sin aprobar» vale lo que vale el control general que impide que alguien lo desactive o que modifique el programa sin pasar por una revisión. En un artículo del Journal of Accountancy, John White compara los controles generales con un paraguas que protege a los de aplicación.

La Green Book da tres objetivos para lo que procesa un sistema. Completitud: las operaciones que ocurren "are recorded and not understated". Exactitud: se registran "at the correct amount in the right account (and on a timely basis)". Validez: lo registrado representa "economic events that actually occurred".

## Los cuatro frentes del principio 11

Según White, que transcribe los puntos de foco de COSO, el principio 11 pide cuatro cosas: entender cuánto dependen los procesos del negocio de la tecnología, y controlar la infraestructura, la gestión de la seguridad y la adquisición, el desarrollo y el mantenimiento de la tecnología. Las secciones que siguen los ordenan en accesos, cambios a los programas y operación, un agrupamiento habitual que no es literal de COSO; el registro de quién hizo qué los atraviesa a todos.

### Accesos

La gestión de la seguridad cubre, según la Green Book, los derechos de acceso "including who has the ability to execute transactions", y esos controles "support appropriate segregation of duties". En concreto pide tres cosas:

- Que cada usuario autorizado tenga una identificación propia: "providing a unique user identification or token to authorized users".
- Que el acceso se limite a las funciones que corresponden a cada puesto.
- Que los permisos se actualicen "promptly" cuando alguien cambia de puesto o se va, porque las amenazas internas "may come from former or disgruntled employees".

El manual de control de Indiana, que aplica estas normas a los sistemas contables del estado, agrega que el acceso se restringe al mínimo que la persona necesita y que la gerencia revisa y aprueba los permisos en forma periódica. Un usuario compartido entre varias personas rompe todo lo anterior: nadie puede decir quién hizo qué.

### Cambios a los programas

Un programa que calcula mal o que se saltea un control produce asientos equivocados sin que nadie los toque a mano. Por eso la Green Book pide controlar la adquisición, el desarrollo y el mantenimiento de la tecnología. El control de cambios "may involve requiring authorization of change requests; reviewing the changes, approvals, and testing results". Su propósito, en sus palabras, es que estos controles "prevent unauthorized programs or modifications to existing programs".

### Operación

La operación cubre la infraestructura y la rutina: que el sistema esté disponible y que los procesos programados corran. La Green Book incluye en el mantenimiento de la infraestructura "backup and recovery procedures, as well as continuity of operations plans". El manual de Indiana pide documentar que los procesos diarios, mensuales y de cierre "are performed correctly and completely" y que las copias de respaldo se completen bien.

## El registro de quién hizo qué

Entre los objetivos de los controles de aplicación, la guía GTAG del IIA, citada en el manual de Indiana, incluye que "A record is maintained to track the process of data from input to storage and to the eventual output". Esa pista de auditoría guarda, para cada acción, quién la hizo, cuándo y qué cambió. La Green Book lo liga a la integridad de la información, que incluye "nonrepudiation and authenticity": que nadie pueda negar después una acción que hizo.

La contabilidad ya tenía esa regla antes de los sistemas: un asiento no se borra, se corrige con otro. El ejemplo sale de la conciliación de Feeter Plumbing que trae OpenStax. El cheque n.º 5386 se había anotado por 1,760 cuando era de 2,000. El asiento original (reconstruido por la base; la fuente solo trae el error y su corrección) queda como estaba:

| Cuenta | Debe | Haber |
|---|---|---|
| Gasto por cuotas | 1,760 | |
| Banco | | 1,760 |

Y la corrección se registra aparte, por la diferencia:

| Cuenta | Debe | Haber |
|---|---|---|
| Gasto por cuotas | 240 | |
| Banco | | 240 |

Si el sistema hubiera permitido editar el primer asiento a 2,000, el saldo sería el mismo, pero se perdería que hubo un error, cuándo se descubrió y quién lo corrigió. Esa pérdida es lo que la pista de auditoría evita. La misma idea, aplicada a cualquier saldo en una base de datos, es el [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md); la regla contable está en [asiento y libros](../Registro/asiento-y-libros.md).

## Lo que un sistema de gestión tiene que poder hacer

Las fuentes describen controles, no funciones de un producto. Traducidos a lo que un sistema contable tiene que poder registrar, impedir o emitir, en lectura propia:

| El sistema tiene que poder | Control que sostiene | Fuente del control |
|---|---|---|
| Identificar a cada usuario por separado, sin cuentas compartidas | Acceso | Green Book 11.14 |
| Asignar permisos por función y negar combinaciones incompatibles | Acceso y separación de funciones | Green Book 11.12; manual de Indiana |
| Emitir la lista de quién tiene qué permiso, para revisarla | Revisión periódica de accesos | manual de Indiana |
| Dar de baja o cambiar permisos el día que alguien cambia de puesto | Acceso | Green Book 11.14 |
| Guardar quién creó, aprobó, modificó o anuló cada registro, y cuándo | Pista de auditoría | GTAG, vía manual de Indiana |
| Corregir con un asiento nuevo en lugar de editar o borrar | Integridad del registro | Green Book 11.11 |
| Registrar quién desactivó un control o forzó una excepción | Anulaciones (overrides) | GTAG, vía manual de Indiana |
| Rechazar duplicados y cuadrar los totales entre módulos | Controles de aplicación | GTAG, vía manual de Indiana |
| Guardar qué versión del programa estaba activa y quién aprobó cada cambio | Cambios a los programas | Green Book 11.15 |

Las anulaciones merecen una línea propia. En el informe de la ACFE de 2024, la anulación de controles existentes por parte de quien tiene autoridad fue la segunda debilidad más citada en los fraudes, con el 19% de los casos ([auditoría y fraude](auditoria-y-fraude.md)). Un sistema donde el administrador puede saltearse una aprobación sin dejar rastro reproduce esa debilidad. Cómo las resuelve un software de gestión está en sus columnas técnicas: [permisos y separación de funciones](../../Software-de-gestion/Columnas-tecnicas/permisos-y-separacion-de-funciones.md), [auditoría de cambios](../../Software-de-gestion/Columnas-tecnicas/auditoria-de-cambios.md) y [documento y estados](../../Software-de-gestion/Columnas-tecnicas/documento-y-estados.md#las-aprobaciones).

> [!NOTE] Sin fuente todavía: el texto completo de los puntos de foco de COSO para el principio 11 y de la GTAG 8 del IIA; acá vienen de un artículo del Journal of Accountancy y de la cita de un manual estatal. La Green Book tiene una revisión de 2025 que no se leyó.
