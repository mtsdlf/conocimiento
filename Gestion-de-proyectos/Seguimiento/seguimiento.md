---
resumen: >-
  El seguimiento es saber cómo va un trabajo y cuándo hay que intervenir: se mira cuánto trabajo hay en curso, se mide el avance con datos y no con impresiones, se acepta lo hecho por la evidencia, se deciden los cambios y se informa a quien decide.
estado: vigente
estabilidad: estable
fuentes:
  - "Little (2011), Little's Law as Viewed on Its 50th Anniversary, Operations Research 59(3): https://people.cs.umass.edu/~emery/classes/cmpsci691st/readings/OS/Littles-Law-50-Years-Later.pdf"
  - "Christensen y Templin (2002), EAC Evaluation Methods: Do They Still Work?, Acquisition Review Quarterly: https://webharvest.gov/peth04/20041015060742/http:/www.dau.mil/pubs/arq/2002arq/ChrisSP2.pdf"
  - "Keil, Smith, Iacovou y Thompson (2014), The Pitfalls of Project Status Reporting, MIT Sloan Management Review: https://sloanreview.mit.edu/article/the-pitfalls-of-project-status-reporting"
  - "METR (2025), Recent Frontier Models Are Reward Hacking (laboratorio, sin revisión de pares): https://metr.org/blog/2025-06-05-recent-reward-hacking"
  - "Gestion-de-proyectos/.investigacion/seguimiento.md"
  - "Gestion-de-proyectos/.investigacion/posicion-contraria.md"
aliases: [monitoreo y control, monitorear y controlar, progreso y controles, project monitoring and control, tracking, seguimiento del proyecto]
creado: 2026-11-27
revisado: 2026-11-27
---

# Seguimiento

El seguimiento es saber cómo va un trabajo y cuándo hay que intervenir: se mira cuánto trabajo hay en curso, se mide el avance con datos y no con impresiones, se acepta lo hecho por la evidencia, se deciden los cambios y se informa a quien decide.

Dentro del tema, el seguimiento mide lo que producen [Personas y agentes](../Personas-y-agentes/personas-y-agentes.md) y devuelve dos cosas. A [Planificación](../Planificacion/planificacion.md) le actualiza el [pronóstico](../Planificacion/pronostico.md) con lo que ya se terminó. A [Incertidumbre y riesgo](../Incertidumbre-y-riesgo/incertidumbre-y-riesgo.md) le pasa los desvíos, que suben a [Gobierno y cierre](../Gobierno-y-cierre/gobierno-y-cierre.md) cuando exceden la tolerancia. Contra qué se mide lo fija [Encuadre](../Encuadre/encuadre.md): el [resultado y su criterio de terminado](../Encuadre/resultado-y-terminado.md) y la línea base del [alcance](../Encuadre/alcance.md).

## Dos tradiciones que miden cosas distintas

El campo clásico llama a esta parte "monitorear y controlar" (PMBOK) o "progreso" (PRINCE2), y junta medir, informar y controlar cambios contra un plan. La otra tradición viene de la teoría de colas y de Kanban (Little, Reinertsen, Vacanti). No mide cuánto del plan se cumplió, sino cuánto trabajo hay adentro, cuánto sale y cuánto tarda cada pieza.

La escuela de este tema toma el flujo como lente principal. Por eso [trabajo en curso y colas](trabajo-en-curso-y-colas.md) es la pieza de base, y el valor ganado entra en [medir el avance](medir-el-avance.md) como la otra familia de medidas, útil cuando hay una línea base de alcance fija. Las dos familias responden preguntas distintas y presuponen proyectos distintos: un proyecto puede usar las dos, pero sus cifras no se combinan en una sola medida.

La base teórica del flujo es firme: la ley de Little es un teorema. La evidencia de que limitar el trabajo en curso mejore proyectos reales es débil, con estudios de caso de una sola empresa y resultados mixtos. El detalle y la disputa están en [trabajo en curso y colas](trabajo-en-curso-y-colas.md).

## El reporte de quien hizo el trabajo no alcanza

Una falla importante del seguimiento está en la información que recibe. Las personas que llevan un proyecto en problemas tienden a callar o suavizar las malas noticias: es el *mum effect*, con sus cifras en [informar el estado](informar-el-estado.md). Un agente de IA puede dar por terminada una tarea que no cumplió y, en una medición de METR, reconocerlo si se le pregunta después: las mediciones de laboratorio están en [aceptar con evidencia](aceptar-con-evidencia.md).

De ahí salen dos reglas de la vertical. Lo hecho se da por hecho por lo que muestra contra el criterio de terminado, no por lo que dice quien lo hizo. Y el informe para quien decide se arma con datos que no dependen de una sola voz.

## Qué cambia cuando ejecutan agentes

Con agentes, el registro del avance puede salir solo: un agente corre sobre software y cada paso suyo puede dejar rastro, con su consumo de tokens. Las herramientas que lo capturan están en la [ficha de herramientas](herramientas-de-seguimiento.md). Lo que empeora es la confianza en el "listo": el reporte del agente es una afirmación más, que hay que comprobar.

La cola que decide el ritmo pasa a ser la de revisión humana. Un equipo puede lanzar diez tareas a agentes en una mañana y tardar una semana en aceptarlas. Esa lectura es inferencia de esta base, y el mecanismo está en [la atención humana como restricción](../Personas-y-agentes/la-atencion-humana-como-restriccion.md).

## Dónde termina esta vertical

- Las métricas de entrega de software (las de DORA) y el mapa del flujo de valor de un cambio hasta producción son del tema DevOps: [métricas DORA](../../DevOps/Cultura-y-medicion/metricas-dora.md) y [flujo de valor](../../DevOps/Cultura-y-medicion/flujo-de-valor.md).
- Mostrarle el avance a un cliente de software está en [seguimiento con el cliente](../../Desarrollo/Encargo/seguimiento-con-el-cliente.md), y sus pedidos nuevos en [cambios de alcance](../../Desarrollo/Encargo/cambios-de-alcance.md).
- Revisar el código que escribió un agente está en [verificar lo que hizo un agente](../../Desarrollo/Verificacion/verificar-lo-que-hizo-un-agente.md).
- La cadencia de revisiones de una empresa y cómo se conduce una reunión están en [ritmo operativo](../../Liderazgo-y-direccion/Ejecucion/ritmo-operativo.md) y [reuniones](../../Liderazgo-y-direccion/Ejecucion/reuniones.md).

## Las piezas del seguimiento

- [Trabajo en curso y colas](trabajo-en-curso-y-colas.md) — la ley de Little, el límite de trabajo en curso y por qué una cola llena alarga todo; leerla primero.
- [Medir el avance](medir-el-avance.md) — las dos familias de medidas: tiempo de entrega y rendimiento, por un lado, y valor ganado, por el otro, con cuándo sirve cada una.
- [Aceptar con evidencia](aceptar-con-evidencia.md) — dar algo por hecho por lo que muestra, y por qué el reporte de una persona o de un agente no alcanza.
- [Control de cambios](control-de-cambios.md) — qué hacer cuando cambia lo pedido a mitad de camino, con la poca evidencia que hay.
- [Informar el estado](informar-el-estado.md) — qué tiene que poder leer quien decide, el sesgo de reportar en verde y el reporte por excepción.
- [Herramientas de seguimiento](herramientas-de-seguimiento.md) — ficha con categorías de herramientas y ejemplos, copiada el 2026-11-27.
