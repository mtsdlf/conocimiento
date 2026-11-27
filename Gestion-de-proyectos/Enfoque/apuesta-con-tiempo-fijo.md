---
resumen: >-
  Una apuesta con tiempo fijo decide primero cuánto tiempo vale un trabajo y después recorta el alcance para que entre, en lugar de estimar el alcance y aceptar el plazo que salga. Según los practicantes, funciona cuando quien pide acepta recortar; no hay estudios con método que midan si rinde más que estimar y comprometer.
estado: vigente
estabilidad: semi
fuentes:
  - "Singer, Shape Up (Basecamp), cap. 3, Set Boundaries (página leída): https://basecamp.com/shapeup/1.2-chapter-03"
  - "Singer, Shape Up, glosario, scope hammering (según resumen del buscador): https://basecamp.com/shapeup/4.5-appendix-06"
  - "Críticas a fijar tiempo y alcance variable (según resumen del buscador): https://www.prodpad.com/?p=85944"
  - "Parkinson (1955), Parkinson's Law, The Economist (según la ficha de Wikipedia): https://en.wikipedia.org/wiki/Parkinson%27s_law"
  - "Newport, Revisiting Parkinson's Law (según resumen): https://calnewport.com/revisiting-parkinsons-law/"
  - "PMI, Critical chain project management investigation (según resumen): https://www.pmi.org/learning/library/critical-chain-project-management-investigation-6380"
  - "Gestion-de-proyectos/.investigacion/enfoque.md"
aliases: [tiempo fijo y alcance variable, fixed time variable scope, apetito, appetite, timebox, caja de tiempo, scope hammering]
creado: 2026-11-27
revisado: 2026-11-27
---

# Apuesta con tiempo fijo

Una apuesta con tiempo fijo decide primero cuánto tiempo vale un trabajo y después recorta el alcance para que entre, en lugar de estimar el alcance y aceptar el plazo que salga. Según los practicantes, funciona cuando quien pide acepta recortar; no hay estudios con método que midan si rinde más que estimar y comprometer.

Es uno de los [enfoques](enfoque.md) entre los que se [elige](elegir-un-enfoque.md). Invierte el orden del [enfoque predictivo](enfoque-predictivo.md): allá el alcance queda fijo y el plazo se mueve; acá el plazo queda fijo y lo que se mueve es el alcance. La idea viene de Shape Up, el método de producto de Basecamp, que se trata en [Shape Up](../../Producto/Planificacion-y-entrega/shape-up.md); esta nota la generaliza a otros trabajos por analogía, sin estudios que lo respalden fuera del software.

## Apetito en lugar de estimación

El apetito es, en palabras de Singer, "the amount of time we want to spend on a project, as opposed to an estimate". La diferencia es de orden: las estimaciones "start with a design and end with a number", y los apetitos "start with a number and end with a design". Shape Up llama al principio "fixed time, variable scope" y lo considera "key to successfully defining and shipping projects".

El apetito es una decisión de valor: pregunta cuánto vale esto para quien lo pide. Cuánto tarda algo se responde con un [pronóstico](../Planificacion/pronostico.md); cuánto vale, con la [justificación](../Encuadre/justificacion.md) del trabajo.

## Recortar antes de empezar

Lo que distingue a la apuesta de una simple caja de tiempo es cuándo se recorta. En un enfoque iterativo, cada vuelta tiene un largo fijo y el alcance se ajusta entregando por tandas. En la apuesta, el alcance se recorta antes de empezar, para que el problema entero quepa en el tiempo elegido, y durante la ejecución se sigue recortando. El glosario de Shape Up llama a ese recorte "scope hammering": cuestionar con fuerza un diseño o un caso de uso hasta que lo que queda entra en la caja (según un resumen).

Singer advierte contra las bolsas de pedidos sueltos ("grab-bags"): una apuesta tiene que ser un problema con forma, no una lista de cosas a hacer en el mismo plazo. La explicación que sigue es de la base, no de Singer: un problema acotado se puede recortar con criterio; una lista solo se puede cortar por la mitad.

## Un caso fuera del software

Ejemplo inventado para ilustrar, no un caso medido.

Una organización tiene que hacer su primer encuentro anual con clientes. El apetito es de seis semanas de trabajo de dos personas, porque es lo que vale un evento que todavía no probó nada. Con ese número, se recorta antes de empezar: un solo lugar ya conocido, una jornada en vez de dos y sin transmisión en vivo. Si a la cuarta semana el catering se complica, se cambia a algo más simple; la fecha no se mueve.

## Por qué fijar el tiempo podría rendir

La justificación habitual es que el trabajo se estira hasta llenar el tiempo disponible. Esa observación abre el ensayo de Parkinson de 1955 en The Economist, pero su tema real era el crecimiento de la burocracia y era una sátira, según la ficha de Wikipedia; las fuentes discrepan en la fecha. Newport sostiene que la versión aplicada a una persona no está en el ensayo. No se cita a Parkinson como si midiera algo.

Goldratt da una razón vecina en la cadena crítica: el síndrome del estudiante (empezar tarde) y la ley de Parkinson esconden holgura en cada estimación, según un resumen del PMI. Inferencia de la base, no de Goldratt ni de Basecamp: fijar el tiempo y recortar el alcance atacaría esa holgura sin pedir estimaciones más exactas.

> [!NOTE]
> Sin fuente todavía: no se encontró ningún estudio con método que mida si fijar el tiempo y recortar el alcance da mejores resultados que estimar y comprometer alcance. Lo que hay son testimonios de practicantes y la lógica de Goldratt.

## Dónde no sirve

- **Contratos que fijan funcionalidades.** Según la crítica (por un resumen), es difícil aplicarla cuando el contrato fija qué se entrega; que recortar alcance sea entonces incumplir es deducción de la base. Un [proyecto a precio cerrado](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md) necesita otra forma de manejar la variación.
- **Leerla como tiempo fijo y alcance fijo.** La crítica advierte que puede leerse así: se fija la fecha y se sigue esperando todo. Sin la decisión explícita de recortar, es un plazo apretado con otro nombre.
- **Alcance que no se puede partir.** Inferencia de la base, sin fuente: una habilitación legal o una migración que solo vale completa no tiene versión recortada útil.

## Apetito cuando ejecutan agentes

Inferencia de esta base: si un agente ejecuta, el apetito deja de medirse en horas de ejecución y pasa a medirse en la capacidad humana de especificar y revisar. Seis semanas de un agente valen poco si nadie puede mirar lo que produce. Recortar el alcance sigue siendo una decisión humana, porque decide qué vale; el agente puede proponer recortes, pero no elegir cuál se acepta. El presupuesto que se le da a un agente es un apetito chico, y se trata en [delegar a un agente](../Personas-y-agentes/delegar-a-un-agente.md).
