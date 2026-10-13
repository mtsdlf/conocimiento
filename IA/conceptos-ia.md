---
tipo: mapa
resumen: >-
  Mapa del Tema IA: cómo funcionan los modelos de lenguaje y cómo se acota lo que emiten, para
  quien diseña sistemas con LLM.
estado: borrador
estabilidad: semi
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
parte_de: [conocimiento]
---

# IA

Mapa del Tema IA: cómo funcionan los modelos de lenguaje y cómo se acota lo que emiten, para
quien diseña sistemas con LLM.

## Modelos

- [[llm]] — qué es un modelo de lenguaje grande y por qué su salida no viene garantizada; se
  lee primero.
- [[mixture-of-experts]] — cómo MoE suma parámetros sin sumar cómputo por token.

## Acotar la salida

- [[guardrails]] — las cuatro capas (prompt, esquema, validación, ontología) y qué atrapa cada
  una.
- [[llm-emite-reasoner-verifica]] — la capa de ontología: el LLM afirma, un reasoner marca,
  rechaza o repara.
- [[inferencia-rdfs-y-owl]] — qué deduce un reasoner RDFS u OWL y por qué el mundo abierto
  limita lo que chequea.
