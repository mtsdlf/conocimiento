---
tipo: concepto
resumen: >-
  Un LLM (modelo de lenguaje grande) es una red neuronal entrenada para predecir el siguiente
  token de un texto sobre un corpus masivo; genera respuestas encadenando esas predicciones.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - https://arxiv.org/abs/1706.03762
  - https://arxiv.org/abs/2005.14165
  - https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
aliases: [LLM, large language model, modelo de lenguaje grande, modelo de lenguaje]
parte_de: [conceptos-ia]
requiere: []
relacionado: []
---

# LLM

Un LLM (modelo de lenguaje grande) es una red neuronal entrenada para predecir el siguiente
token de un texto sobre un corpus masivo; genera respuestas encadenando esas predicciones.

## Por qué importa

Un mismo LLM resuelve tareas distintas sin reentrenarlo: la tarea se describe en texto, con
instrucciones y algunos ejemplos. GPT-3, con 175 mil millones de parámetros, mostró en 2020 que
escalar el modelo mejora ese aprendizaje con pocos ejemplos dentro del mismo prompt
(few-shot; Brown y otros). Por eso un LLM
sirve como pieza general dentro de un sistema: extraer datos, clasificar, redactar, llamar
herramientas.

## Cómo funciona

El texto se parte en **tokens** (fragmentos de palabra). El modelo recibe los tokens anteriores
y calcula una distribución de probabilidad sobre el siguiente; se elige uno, se agrega al texto
y se repite. Es un modelo **autorregresivo**: cada token depende de los que ya emitió.

La arquitectura dominante es el **Transformer** (Vaswani y otros, 2017), que reemplaza la
recurrencia por mecanismos de atención: cada token "mira" a los demás para decidir qué peso
darles. Eso permite entrenar en paralelo sobre corpus enormes.

Lo que el modelo optimiza es que el texto sea probable, no que sea verdadero. Por eso puede
producir afirmaciones falsas con forma correcta, lo que se llama **alucinación**. Según la guía
"Reduce hallucinations" de Anthropic, técnicas como permitir "no sé" o exigir citas textuales las reducen, pero no las
eliminan.

## Ejemplo

Se le pide a un LLM que extraiga el monto de una factura. Devuelve `"total": 1520`. El número
tiene la forma esperada, pero nada en el modelo garantiza que sea el de la factura: hay que
verificarlo afuera.

## No confundir con

Un **chatbot** o asistente (una aplicación) no es el LLM: es el LLM más instrucciones de sistema,
herramientas y filtros alrededor. Tampoco es una base de datos: no recupera hechos guardados, los
regenera desde lo que aprendió.

## Relaciones

- Parte de: [[conceptos-ia]] — Mapa del Tema IA.
- Base de: [[mixture-of-experts]] — una arquitectura para hacer LLM más grandes sin más cómputo
  por token.
- Base de: [[guardrails]] — las capas que acotan lo que un LLM emite, justamente porque no
  garantiza que sea correcto.
