---
resumen: >-
  Los términos que usan las notas de desarrollo de software, cada uno con una definición de una
  línea y la nota del tema donde se explica.
estado: borrador
estabilidad: semi
fuentes:
  - "Las notas del tema que enlaza cada término, con sus propias fuentes"
  - "Desarrollo/.investigacion/fundamentos.md, sección 5"
  - https://basecamp.com/shapeup/0.3-chapter-01
  - https://scrumguides.org/scrum-guide.html
  - https://en.wikipedia.org/wiki/Accelerate_(book)
  - https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
  - https://simonwillison.net/2025/Mar/19/vibe-coding/
  - https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes
  - https://agents.md/
  - https://dora.dev/research/2025/dora-report/
aliases: [glosario, términos de desarrollo de software, vocabulario del proceso de desarrollo]
creado: 2026-11-27
revisado:
---

# Glosario de desarrollo

Los términos que usan las notas de desarrollo de software, cada uno con una definición de una línea y la nota del tema donde se explica.

Las definiciones son generales; las citas, las cifras y los desacuerdos viven en la nota de cada término. Algunas definiciones salen de resúmenes secundarios que hay que revisar contra el original antes de pasar a vigente.

## El ciclo con el cliente

| Término | Qué es | Dónde se explica |
|---|---|---|
| Acuerdo inicial | Lo que se entiende con el cliente antes de construir: el problema, el resultado buscado y quién decide | [Acuerdo inicial](../Encargo/acuerdo-inicial.md) |
| Lean Inception | Taller de una semana que termina en un MVP entendido por todos | [Acuerdo inicial](../Encargo/acuerdo-inicial.md) |
| Alcance | Qué entra en el encargo y qué no | [Alcance y aceptación](../Encargo/alcance-y-aceptacion.md) |
| Validación | Comprobar que lo construido es lo que el cliente necesitaba | [Verificación](../Verificacion/verificacion.md#verificar-contra-lo-definido-validar-contra-lo-que-se-necesitaba) |
| Definición de terminado | Lo que todo incremento cumple para darse por hecho (probado, revisado, desplegado); distinta de los criterios de aceptación, que son de cada incremento | [Alcance y aceptación](../Encargo/alcance-y-aceptacion.md#qué-quiere-decir-terminado) |
| Apetito | El tiempo que se quiere gastar en un trabajo, fijado antes de diseñarlo y no como estimación (Shape Up) | [Estimación](../Encargo/estimacion.md) |
| Precio cerrado | Contrato con alcance y precio fijados de antemano | [Modelos de contrato y cobro](../Encargo/modelos-de-contrato-y-cobro.md) |
| Tiempo y materiales | Contrato que cobra el tiempo trabajado | [Modelos de contrato y cobro](../Encargo/modelos-de-contrato-y-cobro.md) |
| Incremento | Una parte del sistema que el cliente puede ver y usar | [Plan de entregas](../Encargo/plan-de-entregas.md) |
| Circuit breaker (Shape Up) | Regla que cancela por defecto lo que no sale en un ciclo en vez de extenderlo; no confundir con el patrón de resiliencia de Arquitectura | [Cambios de alcance](../Encargo/cambios-de-alcance.md) |
| Traspaso | Entregar el código, los accesos, la documentación y la operación a quien va a mantener el sistema | [Traspaso](../Encargo/traspaso.md) |

## Definir lo que se construye

| Término | Qué es | Dónde se explica |
|---|---|---|
| Especificación | Descripción escrita de lo que el software debe hacer, insumo principal de un agente | [Especificación](../Definicion/especificacion.md) |
| Desarrollo guiado por especificaciones | Escribir la especificación antes del código y dársela al agente como fuente de verdad | [Escuelas de desarrollo](escuelas-de-desarrollo.md) |
| Spec-first, spec-anchored, spec-as-source | Los tres niveles de Böckeler: la especificación se usa y se descarta, se mantiene, o es lo único que se edita | [Especificación](../Definicion/especificacion.md#los-tres-niveles-del-desarrollo-guiado-por-especificaciones) |
| Historia de usuario | Descripción breve de una necesidad desde quien la tiene | [Historia de usuario](../Definicion/historia-de-usuario.md) |
| Criterio de aceptación | Condición verificable con la que se decide que algo está terminado | [Criterios de aceptación](../Definicion/criterios-de-aceptacion.md) |
| Contrato de terminado | La prueba o el chequeo de pasa o falla que dice cuándo una tarea está hecha; con agentes, lo que el agente corre para saber si terminó | [Criterios de aceptación](../Definicion/criterios-de-aceptacion.md#el-criterio-que-un-agente-ejecuta) |
| Dado, cuando, entonces | Forma de escribir un ejemplo: estado inicial, acción y resultado observable (Gherkin) | [Criterios de aceptación](../Definicion/criterios-de-aceptacion.md) |
| Descomposición en tareas | Partir el trabajo en tareas que se hacen y se verifican solas | [Descomposición en tareas](../Definicion/descomposicion-en-tareas.md) |
| Lenguaje ubicuo | El vocabulario del negocio, igual en la conversación, las notas y el código | [Modelo de dominio](../Definicion/modelo-de-dominio.md) |
| Dar forma (shaping) | Acotar un trabajo (límites, riesgos, solución a grandes rasgos) antes de dárselo al equipo | [Dar forma a una solución](../../Producto/Descubrimiento/dar-forma-a-una-solucion.md) |

## Construir con agentes

| Término | Qué es | Dónde se explica |
|---|---|---|
| Agente de código | Programa que, con un modelo de lenguaje, lee el repositorio, edita archivos y corre comandos y pruebas en bucle | [Agente de código](../Construccion/agente-de-codigo.md) |
| Contexto del repositorio | Lo que un agente tiene que saber del proyecto y no se ve en el código: reglas, comandos, convenciones | [Contexto del repositorio](../Construccion/contexto-del-repositorio.md) |
| AGENTS.md | Formato abierto de archivo con instrucciones del proyecto para agentes, "README for agents" | [Contexto del repositorio](../Construccion/contexto-del-repositorio.md) |
| Plantilla de proyecto | Punto de partida versionado para que todo proyecto arranque igual | [Plantilla de proyecto](../Construccion/plantilla-de-proyecto.md) |
| Vibe coding | Construir software con un modelo de lenguaje sin revisar el código que escribe (definición de Willison) | [Escuelas de desarrollo](escuelas-de-desarrollo.md#cuánto-se-revisa-lo-que-escribe-el-modelo-las-posturas-sobre-ia) |
| Augmented coding | Programar con IA cuidando el código, las pruebas y la complejidad (Beck) | [Escuelas de desarrollo](escuelas-de-desarrollo.md#cuánto-se-revisa-lo-que-escribe-el-modelo-las-posturas-sobre-ia) |
| Integración continua | Integrar y verificar los cambios seguido en una rama común | [Integración continua](../../DevOps/Integracion-y-entrega/integracion-continua.md) |
| Trunk-based development | Todos integran en una sola rama, con ramas de vida corta | [Trunk-based development](../../DevOps/Ramas-y-versiones/trunk-based-development.md) |

## Verificar lo construido

| Término | Qué es | Dónde se explica |
|---|---|---|
| Verificación | Comprobar que lo construido cumple lo especificado | [Verificación](../Verificacion/verificacion.md) |
| Pirámide de pruebas | Modelo de cuántas pruebas conviene tener en cada nivel | [Pirámide de pruebas](../Verificacion/piramide-de-pruebas.md) |
| TDD | Escribir una prueba que falla, hacerla pasar y refactorizar | [TDD](../Verificacion/tdd.md) |
| Revisión de código | Lectura de un cambio por otra persona, otro agente o una herramienta antes de integrarlo | [Revisión de código](../Verificacion/revision-de-codigo.md) |
| Prueba de mutación | Introducir fallas a propósito en el código para ver si las pruebas las detectan | [Verificar lo que hizo un agente](../Verificacion/verificar-lo-que-hizo-un-agente.md) |
| Complacencia con el código generado | Aceptar lo que escribe la IA sin verificarlo | [Verificar lo que hizo un agente](../Verificacion/verificar-lo-que-hizo-un-agente.md) |
| Cobertura | Proporción del código que ejecutan las pruebas; señal de lo no probado, no objetivo de calidad | [Lo que pierde peso](lo-que-pierde-peso-en-desarrollo.md) |

## Mantener y hacer evolucionar

| Término | Qué es | Dónde se explica |
|---|---|---|
| Deuda técnica | Costo futuro de los atajos de diseño de hoy | [Deuda técnica](../Evolucion/deuda-tecnica.md) |
| Refactorizar | Cambiar la estructura interna del código sin cambiar su comportamiento observable | [Refactorizar](../Evolucion/refactorizar.md) |
| Código heredado | Código que se recibe sin haberlo escrito; para Feathers, código sin pruebas | [Sistema heredado](../Evolucion/sistema-heredado.md) |
| Prueba de caracterización | Prueba que fija lo que hace hoy un código heredado antes de tocarlo | [Sistema heredado](../Evolucion/sistema-heredado.md) |
| Migración | Cambio de dependencias, versiones o forma del código en muchos lugares a la vez | [Migraciones y actualizaciones](../Evolucion/migraciones-y-actualizaciones.md) |

## Escuelas, procesos y medición

| Término | Qué es | Dónde se explica |
|---|---|---|
| Cascada (waterfall) | Secuencia de fases sin retorno; el nombre es posterior a Royce (1970) | [Escuelas de desarrollo](escuelas-de-desarrollo.md#la-cascada-y-el-malentendido-de-royce) |
| Sprint | Contenedor de tiempo fijo de Scrum | [Escuelas de desarrollo](escuelas-de-desarrollo.md) |
| Puntos de historia (story points) y velocidad (velocity) | Estimación relativa del esfuerzo y cuántos puntos completa un equipo por ciclo | [Lo que pierde peso](lo-que-pierde-peso-en-desarrollo.md) |
| Límite de trabajo en curso (WIP) | Tope a cuántas cosas se trabajan a la vez, para que el flujo no se trabe | [Flujo de valor](../../DevOps/Cultura-y-medicion/flujo-de-valor.md) |
| Retroalimentación | Información rápida sobre si lo hecho funciona; uno de los cinco principios de Farley | [Escuelas de desarrollo](escuelas-de-desarrollo.md) |
| Empirismo | Decidir con evidencia observada y no con opinión (Farley) | [Escuelas de desarrollo](escuelas-de-desarrollo.md) |
| Cohesión y acoplamiento | Cuánto pertenecen juntas las partes de un módulo, y cuánto cambia uno cuando cambia otro | [Modularidad](../../Arquitectura/Modularidad/modularidad.md) |
| Métricas DORA | Indicadores de velocidad y estabilidad de la entrega de software | [Métricas DORA](../../DevOps/Cultura-y-medicion/metricas-dora.md) |
| Amplificador (DORA 2025) | La lectura de DORA de que la IA magnifica lo que la organización ya hace bien y lo que hace mal | [Escuelas de desarrollo](escuelas-de-desarrollo.md) |
| SWEBOK | La guía del cuerpo de conocimiento de la ingeniería de software de la IEEE Computer Society; la v4, de octubre de 2024, tiene 18 áreas | [Fundamentos de desarrollo](fundamentos-de-desarrollo.md) |
