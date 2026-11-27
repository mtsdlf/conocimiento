---
tema: IA
para: construir productos con un modelo de IA adentro (AI engineering), para quien programa y para quien se prepara para un puesto de AI engineer
nivel: programa y conoce lo básico de servicios y APIs; no sabe cómo funciona un modelo por dentro
escuela: AI engineering centrado en evaluación (Chip Huyen, AI Engineering, 2025) como perspectiva, con lo que cambió después integrado en cada nota
fuera:
  - entrenar un modelo desde cero y la matemática del aprendizaje profundo, que solo se explican lo necesario para entender por qué el modelo emite lo que emite
  - ML clásico (modelos tabulares, features, reentrenamiento), que iría en Datos
  - la arquitectura general de software (características, estilos, sistemas distribuidos, aislar lo no determinista, costo y latencia como característica), que vive en Arquitectura
  - las herramientas de quien programa con agentes de código, que viven en Desarrollo
  - el mercado laboral de AI engineering, que vive en Presentacion-profesional
fuentes: []
preguntas:
  - Quiero meter un LLM en un producto, ¿cómo sé si el caso de uso vale y qué tiene que lograr el primer hito?
  - Si la salida cambia en cada corrida, ¿cómo sé si el sistema anda? ¿Cuándo me sirve un modelo como juez?
  - ¿Mejoro el prompt, sumo RAG o hago finetuning?
  - ¿Por qué el modelo alucina, y qué hago contra eso en cada capa?
  - ¿Cómo bajo el costo y la latencia de un modelo en producción?
  - Me preparo para un puesto de AI engineer, ¿qué tengo que entender y en qué orden?
aprobado: 2026-11-27
---

# Alcance: IA

El tema IA explica cómo se construye un producto con un modelo de IA adentro: qué es el modelo y por
qué emite lo que emite, cómo se le da contexto y herramientas, cuándo se lo ajusta, cómo se evalúa y
cómo se opera en producción. Sale de una conversación del 2026-11-27 en la que se pidió rehacer el
tema desde cero con *AI Engineering* de Chip Huyen como perspectiva e inspiración, no como índice ni
como resumen: el árbol lo arma esta base. El libro no estuvo disponible entero; se trabajó con su
índice público, los posts de la autora, los papers que cita y fuentes posteriores.

El tema reemplaza al `IA/` anterior (seis notas de 2026-10, archivadas en `Archivo/IA/`) y absorbe
las verticales Sistemas con modelos y Evaluación y observabilidad, que estaban en Arquitectura.

## Árbol

El árbol sigue las partes de un sistema con un modelo adentro: el modelo, lo que entra en su
contexto, las herramientas con las que actúa, el ajuste de sus pesos, la evaluación que decide y la
operación en producción. `←` marca una nota que viene de Arquitectura.

```
IA/
  ia.md                          el todo: qué es AI engineering, sus partes y cómo se conectan
  planificar-una-aplicacion      si el caso de uso vale, qué esperar, hitos y mantenimiento
  prompt-rag-o-finetuning        ← la decisión entre dar contexto y ajustar el modelo
  Modelos/                       qué es el modelo y por qué emite lo que emite
    modelo-base                  de modelo de lenguaje a modelo base, también multimodal
    token-y-embedding            la unidad con la que el modelo lee y escribe, y su representación
    transformer                  atención, ventana de contexto y mixture of experts
    preentrenamiento             datos, escala y leyes de escala
    post-entrenamiento           ajuste supervisado y ajuste por preferencias
    muestreo                     cómo se elige el próximo token; salidas estructuradas
    razonamiento                 cómputo en la inferencia y modelos de razonamiento
    alucinacion                  por qué emite falso con forma correcta
    modelos-disponibles          ficha fechada: familias, abiertos y cerrados
  Contexto/                      todo lo que entra en la ventana del modelo
    prompt                       instrucciones, roles, ejemplos y versionado
    ingenieria-de-contexto       qué entra en la ventana y cómo se degrada con contextos largos
    contexto-y-rag               ← traer información externa al prompt
    recuperacion                 búsqueda léxica, por embeddings e híbrida; reranking y partición
    memoria                      lo que persiste entre turnos y sesiones
    inyeccion-de-prompt          el contexto como superficie de ataque y sus defensas
  Agentes/                       el modelo que actúa con herramientas
    agente                       ← qué es y cuándo alcanza un flujo fijo
    uso-de-herramientas          llamadas a funciones y MCP
    patrones-de-flujo            cadena, ruteo, paralelo, orquestador y evaluador
    planificacion                cómo un agente descompone una tarea y se corrige
    fallas-de-agentes            cómo falla un agente y cómo se evalúa
    versiones-de-mcp             ficha fechada: versiones de la especificación de MCP
    benchmarks-de-agentes        ficha fechada: SWE-bench, τ-bench, GAIA y otros
  Ajuste/                        cambiar los pesos del modelo
    finetuning                   cuándo sí, cuándo no y qué cuesta
    peft-y-lora                  ajustar pocos parámetros
    destilacion                  un modelo chico que imita a uno grande
    datos-para-ajustar           calidad, cobertura, cantidad, anotación y limpieza
    datos-sinteticos             datos generados con modelos y sus riesgos
  Evaluacion/                    medir si el sistema hace lo que tiene que hacer
    evaluacion                   ← el bucle que va de la traza a la mejora
    evals                        ← conjuntos de casos y niveles de prueba
    analisis-de-errores          ← leer trazas a mano para saber qué medir
    metricas-de-evaluacion       exactas, de similitud y de modelado de lenguaje
    ia-como-juez                 ← un modelo que califica a otro
    benchmarks-y-eleccion-de-modelo   qué dicen los rankings públicos y cómo se elige un modelo
    benchmarks-vigentes          ficha fechada: rankings y benchmarks públicos
    feedback-de-usuario          ← las señales del uso como dato
  Produccion/                    operar el sistema
    sistemas-con-modelos         ← las capas que se suman alrededor del modelo
    guardrails                   controles sobre lo que entra y lo que sale
    herramientas-de-guardrails   ficha fechada: clasificadores y bibliotecas de guardrails
    router-y-gateway-de-modelos  ←
    cache-de-modelos             ←
    inferencia                   métricas de inferencia y cómo se optimiza el modelo y el servicio
    apis-de-batch-y-motores-de-inferencia   ficha fechada
    observabilidad-de-modelos    ←
    plataformas-de-ia            ← ficha fechada
  Fundamentos/
    historia-de-la-ia-generativa de los modelos de lenguaje a los modelos base
    ai-engineering-y-ml-engineering   en qué se diferencia el oficio
    bibliografia-de-ia
```

## Supuestos

- El tema sigue en la carpeta `IA/`; el título de la entrada es IA y "AI engineering" va en sus aliases.
- Las notas que vienen de Arquitectura conservan `vigente` si solo cambian de lugar y de enlaces; las que se reescriben vuelven a `borrador`.
- Las notas sobre RDFS, OWL y el patrón "el LLM emite, el reasoner verifica" quedan archivadas; pueden volver como parte de `guardrails`.
- Al escribir se sumaron cinco fichas fechadas (versiones de MCP, benchmarks de agentes, benchmarks vigentes, herramientas de guardrails y APIs de batch y motores de inferencia), para que las notas de arriba no nombren productos.
- Lo que cambió después del libro (modelos de razonamiento, ingeniería de contexto, MCP, agentes de código) se integra en cada nota, fechado y con su fuente.
