---
tema: Proyectos de inversión
para: entender cómo una empresa en marcha decide, aprueba, sigue y cierra una inversión en activos propios (una máquina, una línea, una obra, un sistema), para quien construye o implementa software de gestión y, en segundo lugar, para quien tiene que decidir la inversión sin ser financista
nivel: sabe de negocio y de software, no es financista ni contador; no se da por sabido qué es el valor actual neto, la tasa interna de retorno, una tasa de corte, una solicitud de inversión ni la obra en curso
escuela: las finanzas corporativas del flujo de fondos descontado, como la ordenan los libros de texto (presupuesto de capital), con la contabilidad de gestión para el control del gasto de capital; donde la práctica de las empresas se aparta del libro (el repago, las tasas de corte altas) se dice con su evidencia
fuera:
  - el registro contable del activo construido por la empresa (NIC 16, obra en curso, el asiento del alta y la amortización), que es de Contabilidad; acá se dice qué pasa en el proceso y se enlaza
  - cómo se consigue la plata para la inversión (préstamo, leasing, descuento) y cómo pesa en la caja, que es de Tesorería
  - el alta del equipo en el registro de activos, su mantenimiento y la decisión de reparar o reemplazar uno que ya anda, que son de Activos y mantenimiento
  - cómo se gestiona cualquier proyecto (encuadre, planificación, pronóstico, valor ganado, control de cambios, portafolio, lecciones aprendidas), que es de Gestión de proyectos; acá se toma lo propio de un proyecto de inversión
  - el recorrido de punta a punta de la compra a la baja del activo, que es de Procesos de negocio
  - fundar una empresa y conseguir su capital inicial, que es de Emprender
  - la valuación de empresas, las fusiones y la evaluación social de proyectos (la que hace el Estado con precios sociales)
fuentes: []
preguntas:
  - "Me piden una máquina que cuesta 30 millones y ahorra 8 por año durante cinco años: ¿cómo armo el flujo de fondos, con qué tasa lo descuento y qué hago con la amortización y los impuestos?"
  - "El VAN da positivo, pero la TIR es más baja que la de otra alternativa y el directorio pregunta en cuánto se recupera: ¿con qué criterio decido y por qué todos miran el repago?"
  - "Estoy diseñando el módulo de inversiones de un sistema de gestión: ¿qué tiene que registrar desde la solicitud hasta el alta del activo, y quién aprueba qué?"
  - "La obra ya gastó un 15 % más de lo aprobado y faltan dos meses: ¿cómo se tendría que haber visto antes y quién aprueba el exceso?"
  - "¿Cuándo deja de ser obra en curso y empieza a amortizarse, qué pasa con los costos que llegan después, y cómo sé si la inversión rindió lo que prometía?"
  - "En Argentina, con inflación, ¿evalúo en pesos o en dólares y con qué tasa, cómo pesa el ajuste por inflación impositivo y hay algún régimen que dé beneficios por invertir?"
aprobado: 2026-11-27
---

# Alcance: Proyectos de inversión

Proyectos de inversión es el tema del área «Gestión de la empresa» que trata la decisión de poner plata hoy en un activo propio para recibir beneficios durante años, y lo que pasa con esa decisión hasta que el activo queda andando: evaluarla, aprobarla dentro del presupuesto de capital, seguir el proyecto o la obra y cerrarla con el paso a activo y la revisión posterior. Sale del issue #176, que abrió la sesión de mantenimiento «Enlaces y alcances tras el software de gestión» (#123, PR #169) al ver que la decisión de invertir y la obra en curso no tenían nota de dominio. La persona decidió que va como tema nuevo y fijó el alcance y los límites en el issue (2026-11-27); el árbol de adentro lo propuso esta sesión y queda para revisar en el PR.

Es un tema agnóstico: vale para cualquier empresa en marcha, se sostiene sin software (una planilla y una carpeta de autorizaciones hacen lo mismo que un módulo de inversiones) y lo de Argentina va en una nota aparte. No nombra productos.

## Árbol

```
Proyectos-de-inversion/
  proyectos-de-inversion.md            el todo: invertir es cambiar plata de hoy por beneficios futuros; las cuatro etapas y sus vecinos; qué leer según lo que estés haciendo
  proyectos-de-inversion-en-argentina.md  inflación y tasas en la evaluación, pesos o dólares, ajuste por inflación impositivo, amortización impositiva y regímenes de promoción
  Evaluacion/                          la decisión de inversión
    evaluacion-de-la-inversion           entrada: de la idea al número, qué criterio usar y cómo se equivoca
    flujo-de-fondos-del-proyecto         flujos incrementales, inversión, capital de trabajo, valor residual, impuestos, costo hundido y costo de oportunidad
    valor-actual-neto                    descontar, sumar y decidir; el índice de rentabilidad
    tasa-interna-de-retorno              la tasa que anula el VAN, cuándo engaña y la TIR modificada
    periodo-de-repago                    en cuánto se recupera, simple y descontado; qué ignora y por qué se usa igual
    tasa-de-corte                        el costo de oportunidad del capital, el costo de capital y por qué las empresas usan tasas más altas
    analisis-de-sensibilidad             sensibilidad, escenarios, punto de equilibrio, simulación y la flexibilidad (opciones reales)
  Aprobacion/                          el presupuesto de capital y la autorización
    aprobacion-de-la-inversion           entrada: el ciclo del presupuesto de capital y los tipos de propuesta
    presupuesto-de-capital               el plan anual de inversiones, su relación con el presupuesto operativo y el racionamiento
    solicitud-de-inversion               qué lleva el pedido, niveles de autorización por monto y el umbral entre gasto e inversión
  Ejecucion/                           el seguimiento del proyecto o de la obra propia
    ejecucion-de-la-inversion            entrada: de la autorización al activo terminado
    seguimiento-de-la-inversion          aprobado, comprometido, incurrido y pagado; avance físico y financiero; pronóstico al terminar; desvíos y ampliación de la autorización
    obra-propia                          la obra hecha por la empresa: el proyecto como colector de costos, qué entra y qué no, los intereses
  Cierre/                              el cierre y el paso a activo
    cierre-de-la-inversion               entrada: cerrar la inversión, activarla y aprender
    activacion-de-la-obra                cuándo deja de ser obra en curso, la activación por partes, los costos tardíos y la obra abandonada
    revision-posterior                   comparar lo prometido con lo logrado: qué se mira, cuándo, quién y qué dice la evidencia
  Fundamentos/
    fundamentos-de-proyectos-de-inversion  de dónde viene, las tradiciones, cómo se divide, la práctica frente al libro y los errores comunes
    glosario-de-proyectos-de-inversion     los términos del tema, con su nombre en inglés
```

## Límites con los vecinos

Regla del mapa del área: cada dominio es dueño de un objeto y un verbo; un saber vive en un solo lugar y los demás enlazan. Proyectos de inversión es dueño de **la decisión de inversión y su ciclo** y de los verbos **evaluar, aprobar, seguir y cerrar una inversión**.

| Vecino | Proyectos de inversión es dueño de | El vecino es dueño de | Ejemplo de frontera |
|---|---|---|---|
| [Contabilidad](../Contabilidad/contabilidad.md) | cuándo el proyecto pide la activación y qué costos junta | el asiento del alta, la obra en curso como cuenta, la amortización y la baja ([activos fijos y amortización](../Contabilidad/Operaciones/activos-fijos-y-amortizacion.md)) | acá se dice que la obra está lista; allá se registra el bien de uso |
| [Tesorería](../Tesoreria/tesoreria.md) | el flujo de fondos del proyecto y la tasa con que se descuenta | cómo se consigue y cuánto cuesta la plata ([financiamiento](../Tesoreria/Financiamiento/financiamiento.md), [costo del financiamiento](../Tesoreria/Financiamiento/costo-del-financiamiento.md)), la proyección de caja | el VAN se calcula acá; el préstamo que la paga, allá |
| [Activos y mantenimiento](../Activos-y-mantenimiento/activos-y-mantenimiento.md) | decidir una inversión nueva | el registro del equipo, su mantenimiento y [reparar o reemplazar](../Activos-y-mantenimiento/Desempeno-de-los-activos/reparar-o-reemplazar.md) uno que ya anda | allá se decide que hay que reemplazar; acá se evalúa y se aprueba el reemplazo |
| [Gestión de proyectos](../Gestion-de-proyectos/gestion-de-proyectos.md) | lo propio de una inversión: el caso en números, la autorización por monto, la activación | el método para cualquier proyecto: [justificación](../Gestion-de-proyectos/Encuadre/justificacion.md), [medir el avance](../Gestion-de-proyectos/Seguimiento/medir-el-avance.md), [control de cambios](../Gestion-de-proyectos/Seguimiento/control-de-cambios.md), [portafolio](../Gestion-de-proyectos/Gobierno-y-cierre/portafolio.md) | el valor ganado se explica allá; acá, qué columnas sigue una inversión |
| [Procesos de negocio](../Procesos-de-negocio/procesos-de-negocio.md) | las etapas de la decisión hasta el activo andando | el recorrido [de la compra a la baja del activo](../Procesos-de-negocio/de-la-compra-a-la-baja-del-activo.md) | el recorrido empieza con «decidir la inversión», que se explica acá |
| [Compras y abastecimiento](../Compras-y-abastecimiento/compras-y-abastecimiento.md) | la autorización que habilita a comprar | la orden de compra del activo y la recepción | acá se aprueba el monto; allá se compra |
| [Emprender](../Emprender/emprender.md) | invertir en una empresa que ya opera | el plan financiero y el capital inicial de una que empieza | la pista es de Emprender; el VAN de una máquina, de acá |

## Supuestos

- **Nombre.** «Proyectos de inversión», como sugirió el pedido. «Inversiones» solo confundía con colocar excedentes, que es de Tesorería, y «presupuesto de capital» nombra una sola etapa.
- **Cuatro verticales, una por etapa.** Evaluación, Aprobación, Ejecución y Cierre siguen el orden de los libros de texto (proponer, evaluar, elegir, ejecutar, revisar) y el de APQC 9.4 y 10.1-10.2. Se cortan por etapa porque el objeto (la inversión) es uno solo y cambia de estado.
- **El costo de oportunidad no tiene nota propia**: va en el flujo de fondos (el activo propio que se usa) y en la tasa de corte (lo que rinde la plata en otro lado).
- **El riesgo del proyecto va en Evaluación**, en una sola nota de análisis de sensibilidad, porque en una empresa en marcha se resuelve dentro de la evaluación; las opciones reales se nombran ahí.
- **Desvíos y cambios en una sola nota** de seguimiento, porque la ampliación de la autorización es la consecuencia del desvío; el método general de control de cambios está en Gestión de proyectos.
- **Entradas con calificador.** Las entradas de las verticales llevan «-de-la-inversion» (y la activación, «-de-la-obra») porque `evaluacion.md`, `ejecucion.md` y `activacion.md` ya existen en otros temas y los nombres de archivo son únicos en la base.
- **Lo de Argentina, en una nota** en la raíz del tema, porque toca la evaluación (inflación, tasa, moneda) y el cierre (amortización impositiva).
- **El registro contable de la obra en curso** lo escribe en paralelo otra sesión en Contabilidad (#171, PR #180): las notas enlazan a `Contabilidad/Operaciones/activo-construido.md`, `activo-construido-en-argentina.md` y `arrendamientos.md`, que existen cuando se mergee ese PR.
