---
resumen: >-
  Un supuesto es algo que el plan da por cierto sin haberlo comprobado; se trata escribiéndolo, buscando los que nadie dijo (el premortem es la técnica más conocida) y probando primero los que, si son falsos, tiran abajo más trabajo.
estado: borrador
estabilidad: semi
fuentes:
  - "Klein (2007), Performing a Project Premortem, Harvard Business Review 85(9):18-19: https://comprobo24.github.io/assignments/performing_a_project_premortem.pdf"
  - "Mitchell, Russo y Pennington (1989), J. Behavioral Decision Making 2(1):25-38 (según un resumen del abstract): https://colab.ws/articles/10.1002%2Fbdm.3960020103"
  - "Veinott, Klein y Wiggins (2010), vía Psychology Today (resumen secundario): https://www.psychologytoday.com/ie/blog/seeing-what-others-dont/202101/the-pre-mortem-method"
  - "Gestion-de-proyectos/.investigacion/planificacion-y-riesgo.md"
aliases: [supuesto, assumption, assumptions, registro de supuestos, assumption log, premortem, pre-mortem, prospective hindsight, retrospectiva prospectiva]
creado: 2026-11-27
revisado:
---

# Supuestos

Un supuesto es algo que el plan da por cierto sin haberlo comprobado; se trata escribiéndolo, buscando los que nadie dijo (el premortem es la técnica más conocida) y probando primero los que, si son falsos, tiran abajo más trabajo.

Un supuesto se diferencia de un [riesgo](riesgo.md) en que nadie lo ve como incierto: el plan se apoya en él sin decirlo. Cuando resulta falso, aparece de golpe como un [problema](problemas-y-escalamiento.md), muchas veces tarde. Es una de las cuatro formas de lo incierto de [Incertidumbre y riesgo](incertidumbre-y-riesgo.md).

## Los supuestos que nadie escribió

Los supuestos peligrosos son los implícitos. Al organizar un evento se escribe "el salón tiene capacidad para 300", pero nadie escribe que el proveedor de sonido trabaja ese fin de semana o que los asistentes llegan en transporte público. Al mudar una plataforma, el plan supone que ningún sistema externo lee la base vieja directamente; si uno lo hace, aparece el día del corte.

Escribirlos es el primer paso, según esta base, y el más barato. Un registro de supuestos es una lista con cada supuesto, de qué parte del plan depende, cómo se comprobaría y cuándo.

> [!NOTE] Sin fuente todavía: estudios con método sobre el registro de supuestos y sobre probar supuestos temprano como práctica de proyecto.

## El premortem

El premortem es una técnica conocida para hacer visibles los supuestos. Klein (2007) lo describe así:

1. Antes de arrancar, el equipo imagina que el proyecto ya fracasó.
2. Cada persona escribe, por su cuenta, por qué fracasó.
3. Quien conduce pide a cada miembro, empezando por el director del proyecto, que lea una razón de su lista, y sigue la ronda hasta agotarlas.
4. Con la lista completa, se revisa el plan.

La gracia es que da permiso para decir lo que en una reunión de planificación sonaría a falta de compromiso. Según un resumen secundario, Veinott, Klein y Wiggins (2010) encontraron que imaginar que el plan ya falló redujo la confianza en él más que analizar pros y contras.

> [!IMPORTANT]
> La cifra con que se suele vender el premortem no está verificada.
> - **Klein (2007)**: "Research conducted in 1989 by Deborah J. Mitchell, of the Wharton School; Jay Russo, of Cornell; and Nancy Pennington, of the University of Colorado, found that prospective hindsight—imagining that an event has already occurred—increases the ability to correctly identify reasons for future outcomes by 30%".
> - **El trabajo original**: según un resumen de su abstract, en el experimento 1 de Mitchell, Russo y Pennington (1989) el marco temporal, futuro o pasado, tuvo poco efecto, y lo que más pesó fue la certeza sobre el resultado. El 30 % no aparece en ese resumen.
> - **Estado**: el 30 % es una cifra atribuida por Klein y no verificada en el original. No hay estudio con método que mida el efecto del premortem sobre el resultado de un proyecto.

## Probar primero lo que más trabajo tira abajo

Un supuesto escrito se prueba antes de apoyarle más trabajo encima. El orden lo da cuánto trabajo depende de él y cuánto cuesta probarlo. Antes de migrar todos los datos se migra una muestra; antes de contratar el salón se confirma el sonido. Esa es la lógica del [enfoque iterativo](../Enfoque/enfoque-iterativo.md) y de las [etapas con puntos de control](../Enfoque/etapas-y-puntos-de-control.md): cada tramo compra información barata antes de comprometer lo caro.

Los supuestos del caso de negocio son, a juicio de esta base y sin fuente, los más caros de descubrir tarde, porque de ellos depende si el proyecto vale la pena. Se revisan en [justificación](../Encuadre/justificacion.md).

## Los supuestos que rellena un agente

La lectura de esta base, sin fuente que la mida, es que un agente que recibe un encargo incompleto completa lo que falta con lo que le parece razonable y sigue, y que los supuestos implícitos del encargo son lo primero que un agente rellena en silencio. Por eso conviene pedirle que liste los supuestos que usó junto con lo que entrega, y revisar esa lista antes que el entregable.

La otra respuesta está arriba del encargo: escribir la intención y los límites de modo que dejen pocos huecos ([delegar a un agente](../Personas-y-agentes/delegar-a-un-agente.md)). Para software, cómo se escribe una especificación que un agente pueda seguir está en [especificación](../../Desarrollo/Definicion/especificacion.md).

El recurso canónico es Klein (2007), dos páginas con los pasos del ejercicio. Fijarse en que la cifra del 30 % no se pudo verificar en el trabajo original.
