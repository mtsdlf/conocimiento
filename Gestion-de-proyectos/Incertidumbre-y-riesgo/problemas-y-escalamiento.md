---
resumen: >-
  Un problema es un desvío que ya ocurrió o que el pronóstico da por seguro; se escala a quien tiene autoridad cuando el pronóstico dice que va a salir de la tolerancia acordada, con un informe que trae la causa, el impacto y opciones para decidir.
estado: vigente
estabilidad: semi
fuentes:
  - "PRINCE2, Manage by exception (resumen secundario): https://prince2.wiki/Manage_by_exception"
  - "Knowledge Train, Exception management (resumen secundario): https://knowledgetrain.co.uk/project-management/exception-management"
  - "Open Exam Prep, guía de estudio de PRINCE2 7, Manage by exception (resumen secundario): https://open-exam-prep.com/study-guides/prince2-7-foundation/prince2-7-principles/manage-by-exception"
  - "Anthropic, Building effective agents (según resumen): https://www.anthropic.com/research/building-effective-agents"
  - "Gestion-de-proyectos/.investigacion/planificacion-y-riesgo.md"
  - "Gestion-de-proyectos/.investigacion/personas-y-agentes.md"
aliases: [problema, issue, escalamiento, escalation, escalar, tolerancia, tolerance, informe de excepción, exception report, plan de excepción, exception plan]
creado: 2026-11-27
revisado: 2026-11-27
---

# Problemas y escalamiento

Un problema es un desvío que ya ocurrió o que el pronóstico da por seguro; se escala a quien tiene autoridad cuando el pronóstico dice que va a salir de la tolerancia acordada, con un informe que trae la causa, el impacto y opciones para decidir.

A diferencia de un [riesgo](riesgo.md), un problema ya no es una posibilidad. Puede venir de un riesgo que ocurrió, de un [supuesto](supuestos.md) que resultó falso o de algo que nadie previó. Si lo absorbe el [margen](margenes.md), lo resuelve el equipo; si no, se escala a quien [gobierna el proyecto](../Gobierno-y-cierre/gobierno-del-proyecto.md). Es parte de [Incertidumbre y riesgo](incertidumbre-y-riesgo.md).

## Tolerancias: hasta dónde se decide sin preguntar

Una tolerancia es el desvío que quien delega acepta sin que le consulten. La idea viene de PRINCE2. Según resúmenes del estándar, "A PRINCE2 project has defined tolerances for each project objective to establish limits of delegated authority". Las tolerancias se fijan para tiempo, costo, calidad, alcance, riesgo y beneficio; una guía de estudio agrega sostenibilidad en PRINCE2 7. Las fuentes secundarias no coinciden en si son seis o siete, y el manual oficial no se leyó.

Las tolerancias se anidan. Según un resumen, las de todo el proyecto las fija el nivel de la organización que lo encarga, y las de cada etapa, el comité del proyecto dentro de las anteriores. Al mudar una plataforma, la dirección puede aceptar un mes más y un 10 % más de costo para el proyecto entero, y el comité darle a quien conduce la etapa de migración una semana y un 3 %.

El principio general, delegar autoridad con límites y enterarse solo de lo que los excede, es la gestión por excepción. Cómo se aplica a la autonomía de un agente, y sus niveles, está en [niveles de autonomía](../Personas-y-agentes/niveles-de-autonomia.md).

## Se escala por pronóstico, no por desvío consumado

Mientras el pronóstico quede dentro de la tolerancia, no se escala nada. Según un resumen, la excepción se levanta cuando se pronostica que se va a violar la tolerancia, no cuando ya se violó. La diferencia es de tiempo; la lectura de esta base, sin fuente, es que escalar cuando el desvío ya pasó deja a quien decide sin opciones.

Por eso el escalamiento depende del [pronóstico](../Planificacion/pronostico.md) que se actualiza con el [seguimiento](../Seguimiento/medir-el-avance.md). Si el pronóstico no se recalcula, la tolerancia no sirve: nadie sabe que se va a salir hasta que se salió.

Escalar a tiempo también choca con la conducta. Quien conduce un proyecto tiende a demorar las malas noticias, como se ve en [informar el estado](../Seguimiento/informar-el-estado.md). Y quien decide tiende a seguir poniendo recursos en un proyecto que no rinde, como se ve en [cerrar o cancelar](../Gobierno-y-cierre/cerrar-o-cancelar.md). La lectura de esta base es que una tolerancia escrita antes de empezar saca parte de esa decisión del momento en que cuesta tomarla.

## El informe de excepción

Lo que sube tiene que dejar decidir. Según un resumen, el informe de excepción trae el pronóstico, la causa, el impacto en cada objetivo y al menos dos opciones con una recomendación. Quien lo recibe tiene tres salidas, según la misma fuente: aceptar una tolerancia mayor, reducir el alcance o pedir un plan de excepción que vaya más allá de la etapa. Una cuarta, parar el proyecto, está en [cerrar o cancelar](../Gobierno-y-cierre/cerrar-o-cancelar.md).

Un ejemplo. La migración de datos lleva el doble de lo previsto y el pronóstico dice que la etapa se pasa tres semanas de una tolerancia de una. El informe dice por qué (los datos viejos tienen formatos que nadie había relevado), qué arrastra (la fecha de corte y el costo del proveedor), y dos opciones: migrar solo los últimos cinco años y archivar el resto, o mover la fecha. Recomienda la primera.

> [!NOTE] Sin fuente todavía: un estudio con método sobre si la gestión por excepción mejora el resultado de los proyectos. Todo lo de PRINCE2 viene de resúmenes secundarios de un mismo estándar.

## Cuándo un agente sube a una persona

Con agentes, las tolerancias definen el margen de autonomía. La aplicación es de esta base, sin estudio que la evalúe: un agente decide solo mientras el pronóstico de gasto, de plazo y de confianza en la verificación quede dentro de lo acordado, y sube a una persona cuando sale.

Lo que cambia es el disparador. Con personas, según esta base, alguien tiene que notar el desvío y querer contarlo. Con un agente, el disparador se puede escribir como regla: tantos reintentos fallidos, tanto gasto, una prueba que no pasa o un cambio fuera de los archivos permitidos. La guía de Anthropic sobre agentes sugiere que pausen "for human feedback at checkpoints or when encountering blockers", según un resumen. El informe de excepción de un agente tiene las mismas piezas que el de una persona: qué pasó, qué arrastra y qué opciones hay.

El riesgo del otro lado es que la persona que recibe el escalamiento lo apruebe sin leerlo: el sesgo de automatización, en [niveles de autonomía](../Personas-y-agentes/niveles-de-autonomia.md). Si los escalamientos son muchos, la atención de quien decide se vuelve la restricción ([la atención humana como restricción](../Personas-y-agentes/la-atencion-humana-como-restriccion.md)), y conviene revisar si las tolerancias están bien puestas.

El recurso canónico es el manual de PRINCE2 7, en el principio de gestión por excepción y en el tema de progreso, que esta base no leyó. Fijarse en que se escala por pronóstico de violación, no por violación ocurrida.
