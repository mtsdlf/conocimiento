---
tipo: concepto
resumen: >-
  "El LLM emite, el reasoner verifica" es un patrón en el que un LLM produce afirmaciones y un
  verificador simbólico las chequea contra una ontología, con tres veredictos: marcar, rechazar
  o reparar.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - https://arxiv.org/abs/2402.01817
  - https://arxiv.org/abs/2305.12295
  - https://www.w3.org/TR/owl2-primer/
aliases: [LLM emits reasoner checks, LLM-Modulo, verificación neuro-simbólica, capa de ontología]
parte_de: [guardrails]
requiere: [guardrails, inferencia-rdfs-y-owl]
relacionado: []
---

# El LLM emite, el reasoner verifica

"El LLM emite, el reasoner verifica" es un patrón en el que un LLM produce afirmaciones y un
verificador simbólico las chequea contra una ontología, con tres veredictos: marcar, rechazar
o reparar.

## Por qué importa

Un esquema y un validador atrapan valores mal formados o fuera de rango. No atrapan una
afirmación coherente campo por campo pero imposible en el dominio. Kambhampati y otros (2024)
sostienen que un LLM autorregresivo no puede verificarse a sí mismo; la garantía tiene que venir
de un verificador externo y correcto.

## Cómo funciona

1. El LLM traduce su respuesta a afirmaciones estructuradas (tripletas sujeto–propiedad–objeto
   o hechos tipados).
2. Esas afirmaciones se suman a la ontología del dominio.
3. Un reasoner busca inconsistencias (ver [[inferencia-rdfs-y-owl]]).
4. Según el resultado y el costo del error, el sistema emite un veredicto:
   - **marcar**: la afirmación pasa con una advertencia para revisión humana; sirve cuando el
     chequeo es dudoso o el error es barato;
   - **rechazar**: no entra al sistema; sirve cuando la inconsistencia es segura y no hay forma
     de corregirla;
   - **reparar**: el error del reasoner vuelve al LLM como nuevo prompt, y la respuesta corregida
     se verifica otra vez; tras un número fijo de intentos fallidos, se rechaza.

Reparar tiene precedentes. En Logic-LM (Pan y otros, 2023), el LLM formaliza el problema, un
solver deduce y los mensajes de error del solver guían la corrección; los autores reportan
un 39 % de mejora promedio sobre el LLM con prompting estándar, en cinco datasets de razonamiento
lógico. LLM-Modulo llama a lo mismo "back-prompting": las críticas
de los verificadores se juntan y vuelven al LLM.

Los tres veredictos como esquema son síntesis propia. En la literatura citada solo aparece el
ciclo de reparación.

## Ejemplo

Un LLM afirma que un fondo es "renta fija" y que "invierte solo en acciones". La ontología
declara las dos clases disjuntas. El reasoner informa la inconsistencia y el sistema le pide al
LLM que corrija una de las dos.

## No confundir con

Pedirle al mismo LLM que revise su respuesta no es este patrón: el verificador no es
independiente. Tampoco detecta omisiones: con OWL, por mundo abierto, un dato que el LLM no
emitió no cuenta como error.

## Relaciones

- Parte de y requiere: [[guardrails]] — es su capa de ontología, la última de la pila.
- Requiere: [[inferencia-rdfs-y-owl]] — qué puede deducir y qué no un reasoner.
