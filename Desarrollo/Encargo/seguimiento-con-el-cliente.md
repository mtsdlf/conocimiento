---
resumen: >-
  El seguimiento con el cliente es cómo se le muestra el avance de un encargo mientras dura:
  software andando que el cliente inspecciona para decidir qué sigue, aceptaciones por incremento
  y un pronóstico basado en lo terminado. Es la parte del encargo con menos fuentes; casi todo lo
  que se dice de cadencia y formato es práctica de la escuela.
estado: borrador
estabilidad: semi
fuentes:
  - "Schwaber y Sutherland, The Scrum Guide (2020), Sprint Review y Product Goal: https://scrumguides.org/scrum-guide.html"
  - "Arbogast, Larman y Vodde (2012), Agile Contracts Primer v5, Acceptance y Payment: http://www.agilecontracts.org/agile_contracts_primer.pdf"
  - "Fowler, The Purpose of Estimation, leído: https://martinfowler.com/bliki/PurposeOfEstimation.html"
  - "Entrevista a Vasco Duarte sobre NoEstimates, InfoQ, leída: https://www.infoq.com/articles/book-review-noestimates"
  - "DORA, State of AI-assisted Software Development 2025: https://dora.dev/dora-report-2025/"
  - "Desarrollo/.investigacion/encargo.md"
aliases: [seguimiento del proyecto, reporte de avance, informe de estado, status report, demo, revisión con el cliente, sprint review, gestión de expectativas]
creado: 2026-11-27
revisado:
---

# Seguimiento con el cliente

El seguimiento con el cliente es cómo se le muestra el avance de un encargo mientras dura: software andando que el cliente inspecciona para decidir qué sigue, aceptaciones por incremento y un pronóstico basado en lo terminado. Es la parte del encargo con menos fuentes; casi todo lo que se dice de cadencia y formato es práctica de la escuela.

Es el punto donde el ciclo técnico le devuelve algo al cliente. Lo que se muestra es cada incremento del [plan de entregas](plan-de-entregas.md), con la evidencia que produjo [Verificación](../Verificacion/verificacion.md); lo que sale es una aceptación (ver [alcance y aceptación](alcance-y-aceptacion.md)), una corrección de rumbo o un pedido nuevo que va a [cambios de alcance](cambios-de-alcance.md). El plan dice qué se corta y en qué orden; el seguimiento, cómo se muestra y se mide.

## La demostración sirve para decidir

El *Scrum Guide* da el propósito de la revisión con los interesados: «The purpose of the Sprint Review is to inspect the outcome of the Sprint and determine future adaptations». El equipo «presents the results of their work to key stakeholders and progress toward the Product Goal is discussed». Da el qué, no la cadencia ni el formato para un cliente externo.

La lectura de esta base es que la demostración es una reunión de decisión y no de informe: el cliente usa lo que se construyó y sale diciendo qué acepta, qué corrige y qué cambia de orden. Mostrar software andando temprano tiene un apoyo indirecto en que el sobreoptimismo es el problema central de la estimación (Jørgensen, en [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md#por-qué-el-precio-cerrado-tiende-a-perder-plata)), pero ningún estudio midió el efecto de las demostraciones ni de la participación del cliente.

> [!NOTE]
> Sin fuente todavía: cada cuánto conviene mostrar avance a un cliente externo y en qué formato, cómo se gestionan sus expectativas, y estudios sobre el efecto de las demostraciones. El principio del Manifiesto Ágil sobre el software que funciona como medida de progreso no se leyó en su fuente. El PMBOK 7 tiene dominios de interesados y de incertidumbre que no se pudieron abrir.

## La evidencia de avance se vuelve contractual

El *Agile Contracts Primer* ata cada iteración a una aceptación contra pruebas acordadas y propone pagar cada iteración aceptada. Con eso, la evidencia de avance deja de ser un informe y pasa a ser lo que dispara el cobro. En criterio de esta base, es la forma más honesta de seguimiento que se encontró: lo que se mostró y se aceptó es avance, y lo demás no.

## Mostrar cuándo se termina sin porcentajes

Para la pregunta de cuándo, hay dos formas que se apoyan en lo terminado. Duarte propone contar los ítems entregados contra lo que queda y proyectar el ritmo histórico; la previsión probabilística hace lo mismo con una simulación sobre el ritmo medido, como cuenta [estimación](estimacion.md#pronosticar-por-ritmo). Las dos tienen evidencia débil, pero muestran una distribución de fechas basada en datos del propio proyecto.

El plan sigue sirviendo como referencia. Fowler dice que «a plan acts as a baseline to help assess changes»: muestra qué se movió y ayuda a decidir qué hacer.

En criterio de esta base, pierden peso el informe semanal con un porcentaje de avance y el gráfico de puntos quemados como evidencia para el cliente. La evidencia es software corriendo y ritmo medido en ítems entregados. Que la velocidad no sirve como medida de productividad tiene respaldo, como cuenta [estimación](estimacion.md#lo-que-pierde-peso-y-con-qué-respaldo); el porcentaje de avance no se encontró evaluado.

## Los riesgos con el cliente

Qué riesgos se miran con el cliente y cuándo no tiene nota propia. El informe de la vertical propuso dejarlo acá mientras sea chico. Las fuentes lo reparten entre el seguimiento, la estimación (la cola de proyectos que se disparan) y los cambios (el alcance que crece).

> [!NOTE]
> Sin fuente todavía: cómo se lleva un registro de riesgos con un cliente de proyecto a medida, quién es dueño de cada riesgo y cada cuánto se revisa. Lo único que el informe de la vertical dejó como recomendación, que los reportes se apoyen en ítems terminados y en riesgos con dueño y no en porcentajes, es práctica de la escuela sin fuente que lo mida.

## Qué cambia cuando construye un agente

El riesgo nuevo es cantidad sin dirección: muchas rebanadas chicas que nadie del cliente revisa. La lectura de esta base es que la demostración frecuente es lo que deja corregir el rumbo antes de que se acumule código, y que conviene decirle al cliente qué hizo un agente y cómo se verificó; el detalle de qué verifica una persona está en [verificar lo que hizo un agente](../Verificacion/verificar-lo-que-hizo-un-agente.md). No hay fuente específica para el cliente.

Según el resumen de DORA 2025, las ganancias locales de productividad de la IA se pierden en lo que viene después de escribir el código (integrar, desplegar, operar). Para el seguimiento, en criterio de esta base, eso quiere decir que lo que se muestra al cliente tiene que estar desplegado, no solo en una rama. Las métricas de entrega que propone DORA están en [métricas DORA](../../DevOps/Cultura-y-medicion/metricas-dora.md).

Para leer: el *Scrum Guide*, sección Sprint Review, para el propósito de la demostración, y el *Primer*, secciones Acceptance y Payment, para volver contractual esa evidencia. Fijate en que el cliente decida sobre algo que corre.
