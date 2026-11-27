---
tema: Contabilidad
para: entender cómo una empresa registra lo que le pasa y lo convierte en información, para quien construye software de gestión y, en segundo lugar, para quien lo vende o lo implementa
nivel: sabe de negocio y de software, no es contador; no se da por sabido el débito y el crédito ni cómo se lee un balance
escuela: la contabilidad patrimonial de partida doble con base de devengado, como la enseñan los libros de texto y la ordenan las NIIF; REA y la contabilidad de triple entrada aparecen como posición contraria
fuera:
  - el cierre de período como recorrido entre áreas (del registro al balance, record-to-report), que va al tema Procesos de negocio; acá queda cómo se registran los ajustes de cierre
  - la plata real de la empresa en marcha (cobrar, pagar, posición de caja, financiarse), que va al tema Tesorería y finanzas de la empresa en marcha; la conciliación bancaria es de acá y Tesorería la enlaza
  - la pista, el consumo mensual y el capital inicial de una empresa que empieza, que se quedan en Emprender/Finanzas
  - los impuestos (IVA, Ganancias, Ingresos Brutos, factura electrónica), que van al tema Impuestos; acá solo cómo se registran
  - la liquidación de sueldos, el legajo y las licencias, que van a Administración de personal y nómina; acá solo el asiento de sueldos
  - el plan de mantenimiento y la orden de trabajo de un activo, que van a Activos y mantenimiento; acá su amortización
  - el conteo y la ubicación del stock, que van a Inventario y depósitos; acá su valuación y el costo de lo vendido
  - cómo lo resuelve un software (el registro de movimientos como columna técnica, las reglas de contabilización, la fecha de bloqueo), que va al tema Software de gestión y a Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md
  - la economía unitaria (CAC, LTV), que vive en Marketing/Medicion
  - la auditoría como profesión y la contabilidad pública (gubernamental)
fuentes: []
preguntas:
  - "Estoy diseñando cómo un sistema registra una venta a 60 días: ¿qué asientos salen al facturarla y al cobrarla, y por qué el resultado aparece antes que la plata?"
  - "¿Qué es un plan de cuentas, cómo se arma y qué no conviene meterle (clientes, centros de costo, proyectos)?"
  - "¿Cómo se registra la compra de una máquina y su amortización, y qué pasa si se vende antes de terminar de amortizarla?"
  - "¿Qué tiene que impedir el registro para que una misma persona no pueda dar de alta un proveedor, aprobar la factura y pagarla, y cómo se concilia el banco?"
  - "¿Cuánto hay que vender para no perder plata, y por qué el costeo variable y el de absorción dan resultados distintos?"
  - "En Argentina, ¿qué libros contables son obligatorios, qué normas contables se aplican y qué pasa con el ajuste por inflación?"
aprobado: 2026-11-27
---

# Alcance: Contabilidad

Contabilidad es el primer tema del área «Gestión de la empresa»: cómo una empresa que ya opera registra lo que le pasa, lo resume en estados contables, lo usa para decidir y lo controla. Sale del mapa del mundo del software de gestión (issue #94) y de sus decisiones: «Forma del árbol» (#95), «Huecos del árbol» (#104), «Límites entre dominios vecinos» (#98), «Procesos de punta a punta» (#99) y «Orden de armado» (#101). Es la sesión 1 de 16 (issue #108). El árbol general y los límites los aprobó la persona en el mapa (2026-11-27); el árbol de adentro del tema lo propuso quien escribe y queda para revisar en el PR.

Es un tema agnóstico: cierto en cualquier empresa y cualquier producto, se sostiene sin software y lo de Argentina va en notas aparte (`libros-contables-en-argentina` y `normas-contables-en-argentina`). No nombra productos.

## Árbol

```
Contabilidad/
  contabilidad.md                 el todo: qué es, de qué está hecha, sus vecinos; qué leer según lo que estés haciendo
  Registro/                       cómo un hecho económico se vuelve un asiento (dueña del «cómo registrar»)
    registro-contable               entrada: del hecho al asiento y del asiento al saldo
    partida-doble                   la ecuación contable, débito y crédito, por qué cada hecho toca dos cuentas
    plan-de-cuentas                 la lista de cuentas, sus niveles y lo que no va en ella
    asiento-y-libros                el asiento, el diario, el mayor, el balance de sumas y saldos, corregir sin borrar
    devengado                       registrar cuando pasa y no cuando se cobra: caja frente a resultado
    cuentas-corrientes              los auxiliares de clientes y proveedores, la cuenta de control y la antigüedad de saldos
    libros-contables-en-argentina   qué libros pide el Código Civil y Comercial, rúbrica y medios digitales
  Operaciones/                    cómo se registra cada hecho habitual
    operaciones                     entrada: los ciclos que llegan al registro y el documento que dispara cada asiento
    ingresos-y-cuentas-a-cobrar     reconocer un ingreso, facturar, cobrar, notas de crédito, incobrables, ingresos diferidos
    compras-y-cuentas-a-pagar       la factura del proveedor, el cruce de tres vías visto desde el registro, lo recibido sin facturar, el pago
    gastos-y-rendiciones            gastos de empleados, anticipos, rendiciones y fondo fijo
    costo-de-lo-vendido             inventario permanente o periódico, métodos de valuación, valor neto de realización
    activos-fijos-y-amortizacion    capitalizar o gastar, vida útil, métodos de amortización, baja y resultado de venta
    moneda-extranjera               moneda funcional, conversión y diferencia de cambio
  Estados-contables/              cómo el registro se resume en información para afuera
    estados-contables               entrada: el juego completo, para quién y cómo se conectan
    balance                         el estado de situación patrimonial: activo, pasivo y patrimonio
    estado-de-resultados            ingresos, costos y gastos de un período, por naturaleza o por función
    estado-de-flujo-de-efectivo     de dónde vino y a dónde fue la caja; método directo e indirecto
    ajustes-de-cierre               devengamientos, diferimientos, previsiones y el cierre de las cuentas de resultado
    normas-contables                marco conceptual, NIIF, NIIF para las PYMES, normas locales, consolidación
    normas-contables-en-argentina   FACPCE y sus resoluciones técnicas, NIIF para cotizantes, ajuste por inflación
  Contabilidad-de-gestion/        la contabilidad para decidir adentro
    contabilidad-de-gestion         entrada: en qué se diferencia de la financiera
    costos-y-costeo                 clasificar costos; absorción, variable, por órdenes, por procesos, estándar y ABC
    punto-de-equilibrio             margen de contribución, punto de equilibrio y margen de seguridad (recibe de Emprender)
    presupuesto                     presupuesto maestro y flexible, desvíos, y la crítica de Beyond Budgeting
    centros-de-costo                centros de responsabilidad, prorrateo de indirectos y por qué van en dimensiones
  Control-interno/                cómo se cuida que el registro diga la verdad
    control-interno                 entrada: COSO, controles preventivos y detectivos, la empresa chica
    separacion-de-funciones         autorizar, registrar, custodiar; combinaciones incompatibles y controles compensatorios
    conciliaciones                  la conciliación bancaria paso a paso y la del auxiliar con el mayor
    autorizaciones                  niveles de aprobación, matriz de autorizaciones, numeración correlativa
    auditoria-y-fraude              auditoría interna y externa, el triángulo del fraude y cómo se detecta
  Fundamentos/
    fundamentos-de-contabilidad     entrada: historia, escuelas y posiciones contrarias, mitos
    glosario-de-contabilidad        los términos del tema, con su sinónimo en inglés
    fuentes-de-contabilidad         dónde se produce el saber contable y qué leer
```

## Límites con los vecinos

Regla del mapa (#98): cada dominio es dueño de un objeto y un verbo; un saber vive en un solo lugar y los demás enlazan.

| Vecino | Contabilidad es dueña de | El vecino es dueño de | Ejemplo de frontera |
|---|---|---|---|
| Tesorería y finanzas de la empresa en marcha | registrar lo devengado y conciliar el banco | la plata real: cobrar, pagar, posición de caja, financiamiento | el pago a un proveedor lo ejecuta Tesorería; el asiento y la conciliación son de acá |
| `Emprender/Finanzas` | caja frente a resultado y punto de equilibrio (los recibe) | la pista, el consumo mensual y el capital inicial | Emprender enlaza `devengado` y `punto-de-equilibrio` en lugar de explicarlos |
| Impuestos | el asiento de un impuesto (IVA débito y crédito, provisión de Ganancias) | qué se paga, cuándo y cómo se declara | la alícuota del IVA es de Impuestos; la cuenta «IVA crédito fiscal» es de acá |
| Compras y abastecimiento | la factura del proveedor y la cuenta a pagar | el pedido y la recepción que coincide con lo pedido | el cruce de tres vías termina en Compras; el pasivo nace acá |
| Inventario y depósitos | la valuación del stock y el costo de lo vendido | contar, ubicar y mover | la diferencia de inventario la cuenta Inventario y la registra Contabilidad |
| Relación con clientes | la factura, la cuenta a cobrar y el ingreso | el presupuesto y el pedido de venta | el pedido no genera asiento; la factura sí |
| Administración de personal y nómina | el asiento de sueldos y cargas | el legajo, las licencias y la liquidación | el recibo de sueldo es de allá; su devengamiento, de acá |
| Activos y mantenimiento | el alta del activo, la amortización y la baja | el plan preventivo y la orden de trabajo | una reparación que alarga la vida útil se capitaliza acá |
| Procesos de negocio | cómo se registra cada paso | el recorrido entero (del registro al balance, del pedido al cobro) | el calendario del cierre es del proceso; el asiento de ajuste, de acá |
| Software de gestión | el saber contable, que existe sin software | el registro de movimientos, las reglas de contabilización y la fecha de bloqueo como columnas técnicas | la partida doble se explica acá; cómo se modela en una base, allá |

## Supuestos

- **Cinco verticales.** Registro, Operaciones, Estados contables, Contabilidad de gestión y Control interno. Sigue la división de los libros de texto (contabilidad financiera y de gestión) y de APQC 9.0 (9.1 gestión, 9.2 ingresos, 9.3 contabilidad general y reportes, 9.4 activos fijos, 9.6 cuentas a pagar y gastos, 9.8 controles internos).
- **Gastos y rendiciones, control interno y amortización entran acá**, como pidió el mapa (#104).
- **El cierre no es vertical.** Queda como proceso en Procesos de negocio (#99); acá van los ajustes de cierre como componente de Estados contables.
- **Contabilidad de gestión entra en el tema** aunque el mapa no la nombra, porque APQC 9.1 la pone en finanzas y el punto de equilibrio que recibe de Emprender es de ella. Si se prefiere un tema propio, se puede mover sin tocar las otras verticales.
- **Lo de Argentina, en dos notas**: los libros obligatorios (en Registro) y las normas contables con el ajuste por inflación (en Estados contables). Lo impositivo de Argentina va al tema Impuestos.
- **Consolidación de varias empresas** va como sección de `normas-contables` y no como nota propia.
- **Sueldos** no tiene nota: su asiento va como sección de `operaciones`, porque el detalle es de Administración de personal y nómina.
- **Pendientes para otra sesión**: cuando existan Tesorería, Impuestos, Inventario y Procesos de negocio, sus enlaces se suman a las notas de acá; `Emprender/Finanzas` pasa a enlazar `devengado` y `punto-de-equilibrio` en la sesión 16 (#101).
