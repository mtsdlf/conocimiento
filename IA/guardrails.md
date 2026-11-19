---
resumen: >-
  Los guardrails de un LLM son capas que se apilan sobre su salida, y cada una atrapa errores que
  la anterior no puede: prompt, esquema, validación y ontología.
estado: borrador
estabilidad: estable
creado: 2026-10-03
fuentes:
  - https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
  - https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - https://pydantic.dev/docs/validation/latest/concepts/validators/
  - https://www.w3.org/TR/owl2-primer/
  - https://www.w3.org/TR/shacl/
aliases: [guardrails, guardrail stack, pila de guardrails, guardrails de LLM]
---

# Guardrails de LLM

Los guardrails de un LLM son capas que se apilan sobre su salida, y cada una atrapa errores que
la anterior no puede: prompt, esquema, validación y ontología.

## Por qué cada tipo de error necesita su capa

Un [LLM](llm.md) produce texto probable, no texto correcto. Si su salida alimenta un sistema (una base,
una API, una decisión), cada tipo de error necesita un control distinto. Pensarlos como pila
dice qué capa falta cuando un error llega a producción.

## Qué atrapa cada capa

| Capa | Qué atrapa | Herramientas típicas |
|---|---|---|
| Prompt | Nada de forma garantizada: orienta | Instrucciones de sistema, ejemplos |
| Esquema | Salida mal formada: forma incorrecta, campos faltantes | Structured outputs, tool use con JSON Schema |
| Validación | Valores mal: fuera de rango, regla de negocio rota | Pydantic, reintentos |
| Ontología | Afirmaciones bien formadas y plausibles, pero imposibles en el dominio | RDFS, OWL, SHACL, un reasoner |

- **Prompt**: la guía de Anthropic sobre alucinaciones recomienda permitir "no sé" y exigir
  citas, y aclara que esas técnicas reducen los errores pero no los eliminan.
- **Esquema**: con structured outputs, la respuesta de Claude siempre cumple el JSON Schema
  declarado (decodificación restringida). La misma documentación dice que eso no garantiza que
  los valores sean correctos, y que no soporta restricciones como `minimum` o `maxLength`.
- **Validación**: un validador de Pydantic revisa un campo o la relación entre campos y, si
  falla, levanta `ValidationError`. El error se puede devolver al modelo para reintentar.
- **Ontología**: un reasoner chequea la afirmación contra lo que el dominio permite; es el
  patrón [El LLM emite, el reasoner verifica](llm-emite-reasoner-verifica.md).

## Un informe de pacientes, capa por capa

Un LLM extrae pacientes de un informe. El esquema asegura que `edad` es un entero. La
validación rechaza `edad: 212`. Solo la ontología rechaza "paciente de 8 años, embarazo de
riesgo, jubilado", donde cada campo es válido por separado y la combinación es imposible.

## Guardrails de seguridad y guardrails de corrección

Los guardrails de **seguridad** (filtrar contenido dañino, resistir jailbreaks) protegen de
usos indebidos. Esta pila protege de salidas incorrectas en usos legítimos; las dos conviven.
