---
resumen: >-
  Un ADR (architecture decision record) es un texto corto, guardado junto al código, que registra
  una decisión de arquitectura con su contexto, lo que se decidió y sus consecuencias, para que se
  pueda entender y revisar después.
estado: vigente
estabilidad: estable
fuentes:
  - https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions
  - https://adr.github.io/
  - https://adr.github.io/madr/
  - https://nealford.com/books/SAF2e.html
aliases: [architecture decision record, registro de decisión de arquitectura, MADR, decision log]
creado: 2026-11-27
revisado: 2026-11-27
---

# ADR

Un ADR (architecture decision record) es un texto corto, guardado junto al código, que registra
una decisión de arquitectura con su contexto, lo que se decidió y sus consecuencias, para que se
pueda entender y revisar después.

## El problema que resuelve: el porqué se pierde

El código muestra qué se eligió, pero no por qué (motivación según esta base). Quien llega después ve una cola de mensajes donde
esperaba una llamada directa, y no sabe si fue una decisión pensada o un accidente; la cambia y
rompe algo, o no se anima a tocarla. El ADR guarda la razón en el mismo repositorio, donde la
encuentra quien toca el código. adr.github.io define la decisión arquitectónica como "a justified
design choice that addresses a functional or non-functional requirement", y llama "decision log" al
conjunto de ADRs de un sistema.

## La forma de Nygard

Michael Nygard popularizó el formato en "Documenting Architecture Decisions" (15 de noviembre de
2011). Lo describe como "a short text file", con cinco partes:

| Parte | Qué dice |
|---|---|
| Title | La decisión, en pocas palabras |
| Context | Las fuerzas en juego: qué pasa, qué restricciones hay |
| Decision | Lo que se decidió |
| Status | En qué estado está la decisión |
| Consequences | Lo que cambia después, lo bueno y lo malo |

Dos reglas lo mantienen útil: "The whole document should be one or two pages long", y "ADRs will
be numbered sequentially and monotonically". Que una decisión aceptada no se edite y que, si cambia, se escriba otra que la
reemplaza, es práctica habitual que esta base adopta; no la sacamos de las fuentes leídas.
Según adr.github.io, Mark Richards también parte de la plantilla de Nygard.

## MADR: sumar las opciones consideradas

MADR ("Markdown Architectural Decision Records", que se pronuncia "matter") es una plantilla que
mantiene la comunidad de ADR, con más secciones que la de Nygard. Sus secciones obligatorias son Context and Problem
Statement, Considered Options y Decision Outcome; opcionales, Decision Drivers, Pros and Cons of the
Options, More Information, y dentro del resultado, Consequences y Confirmation. Un encabezado
opcional registra estado, fecha y quién decidió, a quién se consultó y a quién se informó.

La diferencia que importa con Nygard: MADR pide las opciones que se descartaron y por qué. Según esta base,
eso evita repetir la misma discusión. adr.github.io lista otros formatos, como el
Y-statement de Zdun y otros, y menciona una comparación de siete plantillas presentada en WICSA
2015.

## Qué se registra en un sistema con modelos

Un ADR sirve igual para elegir un [estilo](../Estilos/elegir-un-estilo.md) que para las decisiones
propias de un sistema con un modelo adentro: qué modelo se usa, con qué umbral se acepta una
[evaluación](../../IA/Evaluacion/evals.md), por qué se sumó
[RAG](../../IA/Contexto/contexto-y-rag.md) o por qué no se hizo
[fine-tuning](../../IA/prompt-rag-o-finetuning.md). Esas decisiones envejecen rápido
(observación de esta base, porque los modelos cambian); la sección Confirmation de MADR, que dice cómo se va a verificar la
decisión, encaja con una evaluación o una [fitness function](../Caracteristicas/fitness-function.md)
(esta conexión es inferencia de esta base). Un buen candidato a ADR es cada pieza que se suma siguiendo
[Empezar simple](empezar-simple.md): qué medición la justificó.

> [!NOTE] Sin fuente todavía: el capítulo "Architectural Decisions" de Richards y Ford (no se pudo
> leer), con lo que dice sobre ADRs y los antipatrones de decisión.

## Qué leer

El post de Nygard de 2011: es corto, gratis y se lee en cinco minutos. Fijarse en Context, Decision
y Consequences, en el largo de una o dos páginas y en la numeración. Después, la plantilla MADR en
adr.github.io/madr, mirando Considered Options y Confirmation.
