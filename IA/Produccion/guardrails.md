---
resumen: >-
  Los guardrails son los controles que se ponen sobre lo que entra al modelo, lo que sale de él y
  las acciones que dispara, cada uno para un tipo de falla que los otros no atrapan; bajan el
  riesgo sin eliminarlo, y cada capa se paga en latencia y en pedidos legítimos bloqueados.
estado: borrador
estabilidad: semi
fuentes:
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/ToC.md
  - https://raw.githubusercontent.com/chiphuyen/aie-book/main/chapter-summaries.md
  - https://raw.githubusercontent.com/GenAI-Security-Project/GenAI-LLM-Top10/main/README.md
  - https://www.helpnetsecurity.com/2026/08/06/owasp-2026-llm-top-10-released/
  - https://genai.owasp.org/llm-top-10/
  - https://genai.owasp.org/llmrisk/llm01-prompt-injection/
  - https://arxiv.org/abs/2501.18837
  - https://arxiv.org/abs/2504.00441
  - https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks
  - https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
  - https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - https://pydantic.dev/docs/validation/latest/concepts/validators/
  - https://www.w3.org/TR/shacl/
  - https://www.w3.org/TR/owl2-primer/
  - https://blog.premai.io/production-llm-guardrails-nemo-guardrails-ai-llama-guard-compared
aliases: [guardrails de LLM, guardrail, barandas, LLM guardrails, guardrail stack, pila de guardrails, moderación]
creado: 2026-11-27
revisado:
---

# Guardrails

Los guardrails son los controles que se ponen sobre lo que entra al modelo, lo que sale de él y
las acciones que dispara, cada uno para un tipo de falla que los otros no atrapan; bajan el
riesgo sin eliminarlo, y cada capa se paga en latencia y en pedidos legítimos bloqueados.

Existen porque un [modelo base](../Modelos/modelo-base.md) genera texto probable, no correcto
ni seguro, y lo que entra en su ventana puede venir de alguien que quiere torcerlo. Son el paso 2 de la arquitectura de Huyen, "Put in Guardrails" (*AI Engineering*,
cap. 10, según el índice del libro), dentro de las capas que se suman alrededor del modelo en
[Sistemas con modelos](sistemas-con-modelos.md). Según el resumen del capítulo, "guardrails can be
implemented in the inference service, the model gateway, or as a standalone component": pueden ser parte
del [gateway](router-y-gateway-de-modelos.md), del servicio de [inferencia](inferencia.md) o una
pieza propia.

## Tres puntos de control: entrada, salida y acciones

- **Entrada**, antes del modelo: pedidos fuera del alcance del producto, intentos de
  [inyección de prompt](../Contexto/inyeccion-de-prompt.md) (directa, del usuario, o indirecta,
  escondida en una página, un mail o un documento que el sistema lee) e información privada que no
  debería llegar al modelo ni a un proveedor.
- **Salida**, después del modelo: forma incorrecta, valores imposibles, afirmaciones falsas,
  contenido dañino, datos que no debían salir.
- **Acciones**, cuando un [agente](../Agentes/agente.md) puede escribir afuera (mandar un mail,
  cobrar, borrar): qué herramientas tiene, con qué permisos y qué pide aprobación humana. OWASP
  pone la "Excessive Agency" tercera en su lista de 2026 (abajo).

## Qué atrapa cada capa

Cada capa atrapa una clase de error que la anterior deja pasar. Las cuatro primeras filas vienen de
una nota anterior de esta base, armada con la documentación de Anthropic, Pydantic y el W3C; las
dos últimas, de OWASP y de la guía de Anthropic sobre jailbreaks. Juntarlas en una pila es lectura
de esta base.

| Capa | Qué atrapa | Cómo se implementa |
|---|---|---|
| Prompt | Nada de forma garantizada: orienta | Instrucciones que permiten decir "no sé" ("Allow Claude to say 'I don't know'") y piden citas para cada afirmación, según la guía de Anthropic sobre alucinaciones |
| Esquema | Salida mal formada: campos faltantes, tipos equivocados | [Salidas estructuradas](../Modelos/muestreo.md) con un JSON Schema |
| Validación | Valores mal: fuera de rango, una regla de negocio rota | Validadores en el código, con reintento si fallan |
| Dominio | Afirmaciones bien formadas y plausibles, pero imposibles en el dominio | Reglas del dominio o, si el dominio tiene una ontología formal, un validador de ontologías |
| Clasificador | Contenido dañino, pedidos fuera de alcance, intentos de jailbreak, en la entrada o en la salida | Un modelo chico o una API de moderación que devuelve un veredicto |
| Control de acciones | Una acción dañina aunque el modelo haya sido engañado | Mínimo privilegio, aprobación humana para lo de alto riesgo |

Un caso: al extraer pacientes de un informe, el esquema asegura que `edad` sea un entero, la
validación rechaza `edad: 212` y solo una regla de dominio rechaza "8 años, embarazo de riesgo,
jubilado", donde cada campo es válido por separado.

Según la guía de Anthropic sobre alucinaciones, esas técnicas "significantly reduce
hallucinations, they don't eliminate them entirely", y según su documentación de salidas
estructuradas el esquema garantiza la forma, no que los valores sean correctos. La capa de dominio
es una opción para dominios que tienen reglas formales (con SHACL u OWL, por ejemplo), no un paso
general: en lo leído de Huyen y de Anthropic no aparece.

## OWASP pone seguridad y corrección en la misma lista

OWASP publicó el OWASP Top 10 for LLM Applications, edición 2026; su repositorio la fecha el 4 de
agosto de 2026, y el comunicado oficial de lanzamiento es del 1 de septiembre (este último visto
solo por buscador). La lista sale del README del repositorio; Help Net Security confirma los
movimientos que nombra.

| 2026 | Riesgo | Posición en 2025 |
|---|---|---|
| LLM01 | Prompt Injection | 1 |
| LLM02 | Sensitive Information Disclosure | 2 |
| LLM03 | Excessive Agency | 6 |
| LLM04 | Supply Chain | 3 |
| LLM05 | Data and Model Poisoning | 4 |
| LLM06 | Unbounded Consumption | 10 |
| LLM07 | Misinformation | 9 |
| LLM08 | Hidden Context Exposure (antes System Prompt Leakage) | 7 |
| LLM09 | Vector and Embedding Weaknesses | 8 |
| LLM10 | Improper Output Handling | 5 |

Según Help Net Security, la inyección de prompt ahora cubre ataques entre modalidades, con
imágenes o audio. La lista borra una separación que se suele hacer entre guardrails de seguridad
(resistir abusos) y de corrección (no equivocarse en usos legítimos): Misinformation y Improper
Output Handling son fallas de corrección y figuran como riesgos de seguridad. En la práctica, la
misma pila cubre las dos (lectura de esta base).

## Por qué el último eslabón es el control de acciones

La evidencia sugiere que no hay una defensa completa contra la inyección de prompt; las fuentes y
sus límites están en [Inyección de prompt](../Contexto/inyeccion-de-prompt.md). Por eso el último
eslabón de la pila es el control de acciones y no otro filtro: diseñar para contener el daño
cuando el modelo sea engañado, no para que nunca lo sea (lectura de esta base).

> [!IMPORTANT]
> Contrapunto con una sola fuente sobre la dureza de los filtros. Anthropic reporta, para sus Constitutional Classifiers,
> más de 3.000 horas estimadas de red teaming sin encontrar un jailbreak universal contra un
> clasificador temprano (preprint del propio proveedor, leído por su abstract). Se refiere a
> jailbreaks para obtener contenido dañino, no a inyección en agentes, así que no contradice
> la evidencia sobre inyección: muestra que un clasificador puede ser duro de romper en un problema más acotado.

## Lo que cuesta cada capa: latencia y bloqueos de más

Cada guardrail suma tiempo y bloquea algún pedido legítimo. Hay una sola fuente que mide varios
productos con método, y no es neutral: Kumar et al. ("No Free Lunch with Guardrails", preprint de
2025) construyen un guardrail propio y lo comparan con los demás. Según su abstract, "there is no
free lunch with guardrails; strengthening security often comes at the cost of usability".

La latencia depende de cuántas veces llama cada capa a un modelo; las cifras publicadas, que van
de décimas de segundo a varios segundos y vienen de resultados de buscador sin verificar, están en
la ficha de abajo.

Para el costo en bloqueos hay un dato de producción, otra vez del proveedor: los Constitutional
Classifiers sumaron 0,38 % de rechazos absolutos en tráfico real y 23,7 % de sobrecosto de
inferencia, según su abstract. Y una cuenta de un blog técnico muestra por qué apilar empeora:
si cada guarda deja pasar bien el 90 % de los pedidos legítimos y fallan de forma independiente,
cinco en serie bloquean por error alrededor del 41 % (1 − 0,9⁵ ≈ 0,41).

Por inferencia de esta base: cada capa entra cuando la medición la pide y se evalúa con [evals](../Evaluacion/evals.md) que incluyen pedidos legítimos parecidos a los
peligrosos, para medir los bloqueos de más y no solo los aciertos. La
[observabilidad](observabilidad-de-modelos.md) registra qué bloqueó cada guardrail, que es lo que
permite ver un falso positivo en producción.

## Cómo se combinan las capas

La guía de Anthropic sobre jailbreaks recomienda combinar estrategias, con estas piezas:

- un pre-filtro con un modelo chico que devuelve un veredicto en salida estructurada
  ("harmlessness screens");
- validar la entrada y endurecer las instrucciones de sistema;
- para el contenido no confiable, las defensas de diseño de [Inyección de prompt](../Contexto/inyeccion-de-prompt.md).

Los titulares de mitigación de OWASP para la inyección (solo se leyeron esos) suman mínimo
privilegio, aprobación humana y pruebas adversariales.

> [!NOTE]
> Sin fuente todavía: cómo se detectan y se redactan datos personales en la entrada y la salida
> (qué herramientas, con qué precisión). Solo consta que "Sensitive Information Disclosure" es
> LLM02 en 2025 y en 2026.

Clasificadores, frameworks y APIs de moderación concretos, con sus fechas, están en la ficha
[Herramientas de guardrails](herramientas-de-guardrails.md).

El recurso canónico es el [OWASP Top 10 for LLM Applications, edición 2026](https://raw.githubusercontent.com/GenAI-Security-Project/GenAI-LLM-Top10/main/README.md)
para el mapa de riesgos (LLM01, LLM02, LLM03 y LLM10 primero) y la guía de Anthropic
["Mitigate jailbreaks and prompt injections"](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)
para el cómo: fijarse en qué riesgos se mitigan con un filtro y cuáles solo con mínimo privilegio
y aprobación humana.
