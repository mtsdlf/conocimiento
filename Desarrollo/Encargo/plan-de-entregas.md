---
resumen: >-
  El plan de entregas corta el alcance acordado en incrementos que el cliente puede ver y usar, y
  decide en qué orden llegan. Cada incremento es una o más rebanadas verticales desplegadas, de modo que se pueda aceptar, cobrar y corregir el rumbo antes de seguir.
estado: borrador
estabilidad: estable
fuentes:
  - "Schwaber y Sutherland, The Scrum Guide (2020), Increment: https://scrumguides.org/scrum-guide.html"
  - "Caroli, Lean Inception (martinfowler.com), paso de secuencia y MVP canvas: https://www.martinfowler.com/articles/lean-inception"
  - "Singer, Shape Up, cap. 2 y glosario: https://basecamp.com/shapeup/1.1-chapter-02 ; https://basecamp.com/shapeup/4.5-appendix-06"
  - "Arbogast, Larman y Vodde (2012), Agile Contracts Primer v5, aceptación y pago por iteración: http://www.agilecontracts.org/agile_contracts_primer.pdf"
  - "METR (2025), Measuring AI Ability to Complete Long Tasks (según su resumen): https://arxiv.org/abs/2503.14499"
  - "Desarrollo/.investigacion/encargo.md"
aliases: [plan de entregas, release planning, planificación de entregas, incremento, increment, walking skeleton, esqueleto andante]
creado: 2026-11-27
revisado:
---

# Plan de entregas

El plan de entregas corta el alcance acordado en incrementos que el cliente puede ver y usar, y decide en qué orden llegan. Cada incremento es una o más rebanadas verticales desplegadas, de modo que se pueda aceptar, cobrar y corregir el rumbo antes de seguir.

Toma el [alcance](alcance-y-aceptacion.md) y lo ordena en el tiempo. Cada incremento pasa al ciclo técnico, donde [Definición](../Definicion/definicion.md) lo parte en tareas con la [descomposición en tareas](../Definicion/descomposicion-en-tareas.md), y vuelve al encargo para mostrarse en el [seguimiento](seguimiento-con-el-cliente.md) y aceptarse. El plan dice qué se corta y en qué orden; cómo se muestra el avance es del seguimiento. Cómo conviven las fechas firmadas con un roadmap está en [roadmap](../../Producto/Planificacion-y-entrega/roadmap.md#el-roadmap-cuando-el-cliente-paga-por-fechas-y-alcance).

## Un incremento tiene que poder usarse

El *Scrum Guide* pone la condición: «In order to provide value, the Increment must be usable». Para un encargo, la lectura de esta base es que usable quiere decir desplegado en un entorno donde el cliente lo prueba, no solo pasado por las pruebas en una rama. Lo que no se puede usar no se puede aceptar, y lo que no se acepta no se cobra en un contrato que paga por iteración aceptada, el sistema que el *Agile Contracts Primer* llama el más popular.

## Cortar en vertical

Cada incremento se arma con una o más rebanadas verticales desplegadas: cortes que cruzan la interfaz, la lógica y los datos de una función angosta. Qué es una rebanada, cómo se parte y las voces en contra del corte vertical están en [descomposición en tareas](../Definicion/descomposicion-en-tareas.md#rebanadas-verticales-y-no-capas). Un plan por capa técnica (primero toda la base de datos, después toda la lógica, al final la interfaz) no deja nada que el cliente pueda usar hasta el final.

El incremento más chico que cruza todas las capas y se despliega se suele llamar *walking skeleton*, término de Cockburn que Patton usa como primer corte del [mapa de historias](../Definicion/historia-de-usuario.md#el-mapa-de-historias). La cita, la columna vertebral del mapa y los cortes de entrega de lado a lado están en [dar forma a una solución](../../Producto/Descubrimiento/dar-forma-a-una-solucion.md).

> [!NOTE]
> Sin fuente todavía: la definición de *walking skeleton* en el texto de Cockburn (la dirección probada no respondió); la que se cita llega a través de Patton.

## En qué orden llegan los incrementos

Dos fuentes dan formas de ordenar, sin reglas cerradas. Lean Inception tiene un paso para secuenciar las funciones sobre los recorridos de usuario, del que sale el MVP canvas: la primera entrega es la que deja entender el producto mínimo. Shape Up ordena por lotes de tiempo: ciclos de seis semanas o lotes chicos de una a dos semanas, y un proyecto que no termina en su ciclo se cancela por defecto (*circuit breaker*) en lugar de extenderse.

En criterio de esta base, el orden en un encargo responde a tres preguntas, en este orden: qué rebanada deja al cliente usar algo real más temprano, qué rebanada despeja el riesgo técnico más grande (una integración con un sistema del cliente, un dato que nadie vio) y qué depende de qué. La primera entrega conviene que sea delgada y llegue hasta producción, porque es la que prueba el camino entero de despliegue; el despliegue en sí es de [entrega continua](../../DevOps/Integracion-y-entrega/entrega-continua.md).

## Qué cambia cuando construye un agente

El corte vertical gana peso. Una rebanada fina es una unidad que un agente puede construir y que una persona puede verificar corriéndola; una tarea por capa no se puede ver andando. Es una tesis de [descomposición en tareas](../Definicion/descomposicion-en-tareas.md). La única evidencia cercana es la de METR sobre el horizonte de tareas: según su resumen, los agentes completan las tareas largas con mucha menos frecuencia que las cortas. Es apoyo para preferir tareas chicas, no un método de planificación.

Armar el esqueleto se volvió barato, porque la estructura inicial la genera un agente a partir de una [plantilla de proyecto](../Construccion/plantilla-de-proyecto.md). Lo que sigue costando es que ese esqueleto llegue a un despliegue real con los accesos, los entornos y los datos del cliente. Esto es lectura de esta base, sin fuente que lo mida.

## Cómo falla un plan de entregas

- Fases por capa: meses de base de datos y servicios sin nada que el cliente pueda tocar. En criterio de esta base, es de lo que [pierde peso](../Fundamentos/lo-que-pierde-peso-en-desarrollo.md).
- Incrementos que pasan las pruebas pero viven en una rama, y el cliente nunca los usa.
- La primera entrega deja el despliegue para el final, y el primer contacto con producción llega cuando ya no hay margen.
- Muchas rebanadas chicas que nadie del cliente revisa: el agente produce rápido y el rumbo se corrige tarde (ver [seguimiento con el cliente](seguimiento-con-el-cliente.md)).
