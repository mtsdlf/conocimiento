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

- [LLM](llm.md) — qué es un modelo de lenguaje grande y por qué su salida no viene garantizada; se
  lee primero.
- [Mixture of experts](mixture-of-experts.md) — cómo MoE suma parámetros sin sumar cómputo por token.

## Acotar la salida

- [Guardrails de LLM](guardrails.md) — las cuatro capas (prompt, esquema, validación, ontología) y qué atrapa cada
  una.
- [El LLM emite, el reasoner verifica](llm-emite-reasoner-verifica.md) — la capa de ontología: el LLM afirma, un reasoner marca,
  rechaza o repara.
- [Inferencia en RDFS y OWL](inferencia-rdfs-y-owl.md) — qué deduce un reasoner RDFS u OWL y por qué el mundo abierto
  limita lo que chequea.
