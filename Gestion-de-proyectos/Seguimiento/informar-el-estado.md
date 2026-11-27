---
resumen: >-
  Informar el estado es darle a quien decide lo que necesita para decidir: dónde está el trabajo, cuándo se pronostica que termina, qué se sale de la tolerancia y qué decisión se le pide. Su falla típica es el sesgo de reportar en verde, el mum effect, que, por inferencia de la base, se contrarresta armando el informe con datos y no con la palabra de una sola persona.
estado: borrador
estabilidad: semi
fuentes:
  - "Keil, Smith, Iacovou y Thompson (2014), The Pitfalls of Project Status Reporting, MIT Sloan Management Review (leído entero; síntesis de los autores, no artículo con revisión): https://sloanreview.mit.edu/article/the-pitfalls-of-project-status-reporting"
  - "Smith, Keil y Depledge (2001), Keeping Mum as the Project Goes Under: Toward an Explanatory Model, Journal of Management Information Systems 18(2): 189-227 (abstract): https://jmis-web.org/articles/885"
  - "PRINCE2, exception report (resumen secundario; el manual no se leyó): https://prince2.wiki/management-products/exception-report"
  - "PRINCE2 7, manage by exception (resumen secundario): https://open-exam-prep.com/study-guides/prince2-7-foundation/prince2-7-principles/manage-by-exception"
  - "Stray, Moe y Sjøberg, estudio de stand-ups (según un resumen): https://arxiv.org/pdf/1808.07650.pdf"
  - "Encuesta a 221 desarrolladores sobre stand-ups (según un resumen): https://core.ac.uk/works/72981633"
  - "Gestion-de-proyectos/.investigacion/seguimiento.md"
  - "Gestion-de-proyectos/.investigacion/posicion-contraria.md"
aliases: [informe de estado, status report, reporte de avance, reporte por excepción, exception report, highlight report, mum effect, efecto silencio, sesgo de reportar en verde, watermelon reporting, semáforo]
creado: 2026-11-27
revisado:
---

# Informar el estado

Informar el estado es darle a quien decide lo que necesita para decidir: dónde está el trabajo, cuándo se pronostica que termina, qué se sale de la tolerancia y qué decisión se le pide. Su falla típica es el sesgo de reportar en verde, el mum effect, que, por inferencia de la base, se contrarresta armando el informe con datos y no con la palabra de una sola persona.

El informe va hacia arriba, a quien patrocina o gobierna el proyecto ([gobierno del proyecto](../Gobierno-y-cierre/gobierno-del-proyecto.md)). Toma sus datos de [medir el avance](medir-el-avance.md) y de lo [aceptado con evidencia](aceptar-con-evidencia.md), y su pronóstico de [pronóstico](../Planificacion/pronostico.md).

## Lo que tiene que poder leer quien decide

Un informe sirve si quien lo lee puede decidir algo con él. Como inferencia de esta base, eso pide cuatro cosas:

1. Dónde está: lo terminado y aceptado, no lo "casi listo".
2. Cuándo termina: un pronóstico en rango, con la fecha de antes al lado si cambió.
3. Qué se sale de la tolerancia: plazo, costo, alcance o riesgo que exceden lo que quien lleva el proyecto puede resolver solo.
4. Qué se le pide: la decisión concreta, con opciones.

> [!NOTE] Sin fuente todavía: evidencia de que algún formato de informe (semáforo, por excepción, tablero) mejore las decisiones. La lista de arriba no sale de un estudio.

## El sesgo de reportar en verde

Las personas que llevan un proyecto en problemas tienden a no transmitir las malas noticias, o a suavizarlas. La literatura de sistemas de información lo llama *mum effect*. Smith, Keil y Depledge (2001) armaron y probaron en un experimento un modelo de esa reticencia en proyectos que se descontrolan: variaron el impacto de no reportar y la mala conducta observada, y el modelo explicó una parte significativa de la varianza (según el abstract).

Keil, Smith, Iacovou y Thompson (2014) resumieron 14 estudios suyos de unos 15 años, con entrevistas, encuestas y experimentos. En 56 gerentes de proyectos de software, con sus registros, los reportes estaban sesgados el 60 % de las veces, y el sesgo era más del doble de probable hacia lo optimista que hacia lo pesimista. Es una síntesis de los propios autores en una revista de gestión, sin todos los números por estudio.

Los factores que encontraron:

- la autoimagen y la rendición de cuentas de quien reporta;
- el miedo a represalias ("career suicide", dijo un entrevistado);
- rasgos individuales, como ser optimista y ambicioso;
- el clima de trabajo y la cultura (en las culturas colectivistas se ocultaba por más tiempo);
- la desconfianza, que auditar de forma agresiva profundizaba;
- patrocinadores poderosos, que reducían la franqueza.

Entre practicantes circula el nombre "watermelon reporting" para el informe verde por fuera y rojo por dentro. Es jerga sin fuente: no se encontró el origen del término ni un estudio sobre su frecuencia. La evidencia es la del mum effect.

## Cómo se arma un informe que no dependa de una sola voz

Si el sesgo viene de la persona que reporta, auditarla más no es una salida clara: según Keil y otros, auditar de forma agresiva profundizó la desconfianza, uno de los factores. Lo que sigue es inferencia de esta base. El informe se arma con datos que no pasan por la voluntad de quien lleva el trabajo: piezas aceptadas, tiempo de entrega, edad de lo que sigue abierto. La persona agrega lo que los datos no dicen y la decisión que pide.

El clima también cuenta (el miedo a represalias figura entre los factores de Keil y otros). Inferencia de la base: si dar una mala noticia temprano trae castigo, llega tarde; la creencia de que se puede admitir un error sin castigo está en [seguridad psicológica](../../Liderazgo-y-direccion/Equipos-y-cultura/seguridad-psicologica.md).

## El reporte por excepción

PRINCE2 propone gestionar por excepción. El comité del proyecto fija tolerancias y quien lleva el proyecto trabaja dentro de ellas sin pedir permiso. Cuando pronostica que va a salirse de una tolerancia, antes de que pase, levanta un informe de excepción que pide dirección e incluye opciones. Aparte, un informe periódico cuenta cómo va. Esto sale de resúmenes secundarios que coinciden entre sí; el manual no se leyó, y los resúmenes no coinciden en la lista de áreas de tolerancia.

El reporte por excepción ahorra atención a quien decide, pero presupone que alguien reporta la excepción, y el mum effect sugiere que esa voz tiende a callar. Inferencia de la base: por eso conviene que el disparo salga de los datos cuando se pueda: el pronóstico cruza la fecha tope, el costo cruza el margen. Cuándo sube algo a una persona está en [problemas y escalamiento](../Incertidumbre-y-riesgo/problemas-y-escalamiento.md), y los márgenes, en [márgenes](../Incertidumbre-y-riesgo/margenes.md).

## Las reuniones de estado pierden peso, con poca evidencia

La reunión en la que cada uno cuenta cómo va es una forma habitual de informar el estado. Lo que se estudió son las reuniones diarias de pie de los equipos ágiles: las usa el 87 % de quienes aplican ágil, en una encuesta de 221 desarrolladores, y las actitudes están polarizadas (según un resumen). Lo que más pesa en contra es usarlas para reportar estado al jefe; lo que más pesa a favor es compartir información y resolver problemas.

Sobre las reuniones de estado como tales no se encontraron estudios. Que pierdan peso es una apuesta de este tema, reunida en [lo que pierde peso](../Fundamentos/lo-que-pierde-peso-en-gestion-de-proyectos.md). La cadencia de revisiones de una empresa está en [ritmo operativo](../../Liderazgo-y-direccion/Ejecucion/ritmo-operativo.md), y cómo se conduce una reunión, en [reuniones](../../Liderazgo-y-direccion/Ejecucion/reuniones.md).

## Qué cambia cuando ejecutan agentes

Un agente también reporta su propio estado, y su "listo" puede no ser cierto: las mediciones están en [aceptar con evidencia](aceptar-con-evidencia.md). La diferencia con una persona es que el agente puede dejar registro de cada paso, así que el informe podría armarse con lo que hizo y no con lo que dice que hizo.

Como inferencia de esta base, el informe útil con agentes cuenta tres cosas que antes no hacían falta: cuántas piezas esperan revisión humana, cuánto se gastó en ejecución y qué excepciones subieron los agentes. La primera podría explicar los atrasos, como hipótesis ([la atención humana como restricción](../Personas-y-agentes/la-atencion-humana-como-restriccion.md)).

Mostrarle el avance a un cliente de software es otro asunto, con sus propias reglas: está en [seguimiento con el cliente](../../Desarrollo/Encargo/seguimiento-con-el-cliente.md). La entrada de la vertical es [Seguimiento](seguimiento.md).
