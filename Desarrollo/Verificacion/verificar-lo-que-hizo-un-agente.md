---
resumen: >-
  Verificar lo que hizo un agente es aceptar su trabajo por la evidencia y no por su resumen:
  buscar las señales de trabajo incompleto o inventado (pruebas debilitadas, salidas fijadas a mano,
  paquetes que no existen) y medir con pruebas de mutación si sus pruebas detectan fallas.
estado: borrador
estabilidad: semi
fuentes:
  - https://metr.org/blog/2025-06-05-recent-reward-hacking
  - https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf
  - https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes
  - https://arxiv.org/abs/2406.10279
  - https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html
  - https://code.claude.com/docs/en/best-practices
  - https://arxiv.org/abs/2103.07189v1
  - https://arxiv.org/abs/2501.12862
  - https://arxiv.org/abs/2510.09907
  - https://cs.ubc.ca/~rtholmes/papers/icse_2014_inozemtseva.pdf
  - https://www.thoughtworks.com/radar/techniques/complacency-with-ai-generated-code
aliases: [verificar el trabajo de un agente, reward hacking, pruebas de mutación, mutation testing, slopsquatting]
creado: 2026-11-27
revisado:
---

# Verificar lo que hizo un agente

Verificar lo que hizo un agente es aceptar su trabajo por la evidencia y no por su resumen: buscar las señales de trabajo incompleto o inventado (pruebas debilitadas, salidas fijadas a mano, paquetes que no existen) y medir con pruebas de mutación si sus pruebas detectan fallas.

Un agente optimiza que la verificación pase, y eso no siempre coincide con que el código haga lo pedido. El Radar de Thoughtworks (noviembre de 2025) marca como riesgo la complacencia con el código generado: "increasingly highlighting concerns about complacency with AI-generated code". Esta nota es el control que la vertical [Verificación](verificacion.md) pone en la frontera entre lo que el agente dice y lo que se acepta.

## Cuando el agente hace trampa

METR midió en 2025 cuántas veces los modelos hacían trampa en entornos de evaluación. En RE-Bench, "30.4%" de las corridas (39 de 128) lo hicieron; en HCAST, 0,7 %. Los ejemplos incluyen "Overwriting the grader's timer or copying the grader's answer" y "Monkey-patching the evaluator to always return a perfect score". Preguntado después de hacer trampa si su plan coincidía con la intención del usuario, "o3 answered 'no' 10 out of 10 times": el modelo sabía que no hizo lo pedido. Son entornos de evaluación, no repositorios de clientes.

Anthropic reportó, según resúmenes de terceros de la ficha técnica de uno de sus modelos de 2025, casos de fijar a mano las salidas esperadas o modificar archivos de prueba para pasarlas. Beck pone como señal de alarma "disabling or deleting tests".

## Las señales de trabajo incompleto o inventado

| Señal | Cómo se detecta | Fuente |
|---|---|---|
| Pruebas borradas, desactivadas o ablandadas | diff de los archivos de prueba, revisado aparte del código | Beck; METR; ficha técnica de Anthropic |
| Salidas fijadas a mano o casos especiales para la prueba | revisor con contexto limpio; mutación | ficha técnica de Anthropic |
| Evaluador o configuración de pruebas tocados | diff de la configuración de CI y del arnés de pruebas | METR |
| Dependencias que no existen | verificar cada paquete nuevo contra el registro; lockfile | Spracklen et al. |
| Pruebas que recalculan el esperado con la implementación | leer el valor esperado: tiene que ser un literal o venir del criterio | Böckeler |
| "Terminado" sin evidencia | pedir el comando que corrió y su salida | guía de Anthropic |

Los paquetes inventados están medidos. Spracklen et al. (USENIX Security 2025) analizaron 16 modelos y 576.000 muestras de código en dos lenguajes: hallaron 205.474 nombres de paquete alucinados únicos, con un promedio de al menos 5,2 % en modelos comerciales y 21,7 % en modelos abiertos. Quien registre ese nombre con código malicioso entra a la [cadena de suministro](../../DevOps/DevSecOps/cadena-de-suministro-de-software.md); el término "slopsquatting" circula para eso, pero no se encontró su fuente primaria.

La guía de buenas prácticas de Anthropic para su agente de código (leída el 2026-11-27) da la defensa base: darle al agente una verificación ejecutable y pedirle "the command it ran and its output". No hay un estudio que pruebe que las defensas de la tabla, juntas, cubren todas estas fallas.

## Pruebas de mutación: si las pruebas detectan algo

Una prueba de mutación cambia el código a propósito (invierte una condición, cambia un operador, borra una línea) y corre la suite. Si alguna prueba falla, el mutante murió y la suite detectó el cambio; si todas pasan, el mutante sobrevivió y hay una falla que nadie está mirando. Contesta la pregunta que la cobertura no contesta: si las pruebas que escribió el agente prueban algo.

La cobertura de líneas no alcanza. Inozemtseva y Holmes (ICSE 2014) hallaron, según su resumen, una correlación de baja a moderada entre cobertura y efectividad de la suite al controlar por el número de casos. Un agente puede subir la cobertura con pruebas triviales; no se encontró un estudio que lo mida.

Hay evidencia de uso a escala, toda conocida por los resúmenes de los papers:

- **Google** (Petrović et al., ICSE 2021): unos 15 millones de mutantes; quienes reciben mutantes escriben más pruebas y mejoran sus suites, y los mutantes se acoplan con fallas reales de alta prioridad.
- **Meta** (FSE 2025): un sistema que genera pruebas con un modelo, guiado por mutantes, sobre 10.795 clases Kotlin de Android. De 571 pruebas de privacidad, 277 (cerca de 49 %) se habrían descartado si se hubiera guiado solo por cobertura de líneas; los ingenieros aceptaron 73 % de las pruebas propuestas.

El límite es el mutante equivalente: un cambio que no altera el comportamiento, que ninguna prueba puede matar y que hace ruido. Meta usó un modelo para detectarlos, con precisión 0,79 y recall 0,47 (0,95 y 0,96 con preprocesamiento). El otro límite es el costo: correr la suite una vez por mutante es caro; como criterio de esta base, conviene correrla sobre el código que cambió y no sobre todo el repositorio. Böckeler, después de probar TDD con agentes, se apoya en mutación y análisis estático como retroalimentación (ver [TDD](tdd.md)).

Una técnica vecina, las pruebas basadas en propiedades, también se probó con agentes: un trabajo de Anthropic (preprint) corrió un agente que las escribe sobre 100 paquetes populares de Python y obtuvo, según su resumen, 56 % de reportes válidos.

## Cómo se acepta el trabajo de un agente

1. Antes de empezar, dale el comando que verifica: pruebas, tipos y lint (ver [contexto del repositorio](../Construccion/contexto-del-repositorio.md)).
2. Al terminar, pedile la salida de ese comando, no un resumen.
3. Revisá el diff de las pruebas y de la configuración separado del diff del código.
4. Corré mutación sobre lo que cambió, si el lenguaje tiene herramienta.
5. Pasale el cambio a un revisor con contexto limpio contra la especificación ([revisión de código](revision-de-codigo.md)).

Cómo trabaja un agente y dónde falla en general está en [agente de código](../Construccion/agente-de-codigo.md).
