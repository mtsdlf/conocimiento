---
resumen: >-
  Verificar es comprobar con evidencia que lo construido hace lo que se definió: pruebas automáticas,
  revisión de código y controles sobre lo que entrega un agente. Validar es otra cosa: si era lo
  que el cliente necesitaba, y eso se cierra en la aceptación con el cliente.
estado: vigente
estabilidad: estable
fuentes:
  - https://martinfowler.com/articles/practical-test-pyramid.html
  - https://dora.dev/research/2025/dora-report/
  - https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
  - https://code.claude.com/docs/en/best-practices
  - https://metr.org/blog/2025-06-05-recent-reward-hacking
  - https://www.thoughtworks.com/radar/techniques/complacency-with-ai-generated-code
  - https://cs.ubc.ca/~rtholmes/papers/icse_2014_inozemtseva.pdf
  - "Desarrollo/.investigacion/verificacion-y-evolucion.md y posicion-contraria.md (2026-11-27)"
aliases: [verificación de software, verification, pruebas de software, testing, aseguramiento de calidad]
creado: 2026-11-27
revisado: 2026-11-27
---

# Verificación

Verificar es comprobar con evidencia que lo construido hace lo que se definió: pruebas automáticas, revisión de código y controles sobre lo que entrega un agente. Validar es otra cosa: si era lo que el cliente necesitaba, y eso se cierra en la aceptación con el cliente.

Dentro del ciclo técnico de [Desarrollo](../desarrollo.md), Verificación recibe dos cosas: de [criterios de aceptación](../Definicion/criterios-de-aceptacion.md), los ejemplos verificables que dicen cuándo algo está hecho; de [Construcción](../Construccion/construccion.md), el código. Devuelve las fallas a Construcción y, cuando todo pasa, entrega la evidencia con la que el cliente acepta en [alcance y aceptación](../Encargo/alcance-y-aceptacion.md).

## Verificar contra lo definido, validar contra lo que se necesitaba

Esta base separa dos preguntas. Verificar pregunta si se construyó bien, según lo definido: las pruebas pasan, el contrato se respeta, el revisor no encontró huecos contra la [especificación](../Definicion/especificacion.md). Validar pregunta si lo definido era lo que el cliente necesitaba, y eso solo lo contesta el cliente usando el software, en la aceptación de cada incremento.

Las dos fallan por separado. Un sistema puede pasar todas sus pruebas y resolver el problema equivocado; eso es una falla de [Definición](../Definicion/definicion.md) o del [acuerdo inicial](../Encargo/acuerdo-inicial.md), y ninguna prueba la detecta. Por eso Verificación trabaja contra lo escrito y deja la otra pregunta al ciclo con el cliente.

> [!NOTE]
> Sin fuente todavía: la definición canónica de verificación y validación (SWEBOK, normas IEEE) no se leyó; el corte de arriba es criterio de esta base.

## Las tres capas de control

Lo que se verifica pasa por tres filtros, de más barato a más caro.

| Capa | Qué controla | Cómo falla |
|---|---|---|
| Herramienta determinista | pruebas, tipos, lint, análisis estático, compilación | pruebas que no prueban nada, o que nadie corre |
| Otro agente con contexto limpio | el cambio contra la especificación, casos borde | encuentra algo siempre, aunque no importe |
| Persona | intención, diseño, seguridad, lo que el código no dice | aprueba por rutina lo que no entiende |

El reparto en tres capas es síntesis de esta base a partir de varias fuentes, no lo afirma una sola. Se apoya en lo que dice DORA 2025: sin sistemas de control fuertes (pruebas automáticas, control de versiones maduro y retroalimentación rápida), más volumen de cambio termina en inestabilidad. Se apoya también en la guía de buenas prácticas de Anthropic para su agente de código (leída el 2026-11-27): el agente declara terminado algo que no lo está, "usually because it had no way to check its own work", y por eso hay que darle el comando exacto que verifica.

## La prueba como señal, no como ritual

Las pruebas valen por la señal que dan: rápidas, confiables y que fallen por buenas razones. La forma de la suite (cuántas de unidad, cuántas de integración) importa menos que eso, como se discute en la [pirámide de pruebas](piramide-de-pruebas.md). Escribir la prueba antes, como pide [TDD](tdd.md), sirve como contrato de terminado para un agente, aunque la evidencia sobre su efecto en la calidad es nula o mixta.

La cobertura de líneas no mide si las pruebas detectan fallas. Inozemtseva y Holmes (ICSE 2014) encontraron, según un resumen de su trabajo, una correlación de baja a moderada entre cobertura y efectividad al controlar por el número de casos. Las pruebas de mutación miden directamente si la suite detecta un cambio en el código, y por eso están en [verificar lo que hizo un agente](verificar-lo-que-hizo-un-agente.md).

## Lo que cambia cuando el código lo escribe un agente

Un agente escribe pruebas casi gratis, y también las puede escribir mal o adaptarlas para pasar. METR documentó en 2025, en entornos de evaluación, modelos que sobrescribían el temporizador del evaluador, copiaban su respuesta o lo modificaban para que devolviera siempre el puntaje perfecto. Thoughtworks puso en su Radar (noviembre de 2025) la complacencia con el código generado por IA como riesgo, y recomienda reforzar TDD y análisis estático.

De ahí sale la regla de esta vertical: lo que entrega un agente se acepta con evidencia (el comando que corrió y su salida), no con su resumen. La [revisión de código](revision-de-codigo.md) cambia de función: deja de ser el único control de defectos y pasa a revisar contra la especificación y la evidencia.

## Qué hay adentro de Verificación

- [Pirámide de pruebas](piramide-de-pruebas.md): qué se prueba a qué nivel, las formas alternativas (trofeo, panal) y las pruebas de contrato.
- [TDD](tdd.md): la prueba primero, como señal y contrato de terminado, con su evidencia nula o mixta.
- [Diseñar casos de prueba de una API](disenar-casos-de-prueba-de-api.md): el formato y las categorías de casos para una API REST.
- [Revisión de código](revision-de-codigo.md): qué revisa una persona, qué otro agente y qué una herramienta.
- [Verificar lo que hizo un agente](verificar-lo-que-hizo-un-agente.md): señales de trabajo incompleto o inventado, y las pruebas de mutación.

Pendiente: seguridad en el desarrollo (`seguridad-en-el-desarrollo`); mientras tanto, los controles de seguridad del pipeline están en [DevSecOps](../../DevOps/DevSecOps/devsecops.md). Las pruebas que corren en cada cambio se integran en la [integración continua](../../DevOps/Integracion-y-entrega/integracion-continua.md).
