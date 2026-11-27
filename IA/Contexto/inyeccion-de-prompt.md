---
resumen: >-
  La inyección de prompt es un ataque en el que un texto que entra en la ventana del modelo (escrito
  por el usuario o escondido en un documento, una página o un resultado de herramienta) le da
  instrucciones que la aplicación no quería. No hay defensa completa: se diseña el sistema para que
  un modelo engañado no pueda hacer daño.
estado: borrador
estabilidad: semi
fuentes:
  - https://raw.githubusercontent.com/GenAI-Security-Project/GenAI-LLM-Top10/main/README.md
  - https://www.helpnetsecurity.com/2026/08/06/owasp-2026-llm-top-10-released/
  - https://genai.owasp.org/llmrisk/llm01-prompt-injection/
  - https://genai.owasp.org/llmrisk/llm072025-system-prompt-leakage/
  - https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection
  - https://arxiv.org/abs/2302.12173
  - https://simonwillison.net/2022/Sep/12/prompt-injection/
  - https://simonwillison.net/2023/Apr/25/dual-llm-pattern/
  - https://simonwillison.net/2025/Apr/11/camel/
  - https://simonwillison.net/2025/Jun/13/prompt-injection-design-patterns/
  - https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
  - https://arxiv.org/abs/2503.18813
  - https://arxiv.org/abs/2506.08837
  - https://arxiv.org/abs/2404.13208
  - https://arxiv.org/abs/2510.09023
  - https://www.anthropic.com/research/prompt-injection-defenses
  - https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks
  - "Huyen, AI Engineering (O'Reilly, 2025), cap. 5, de «Defensive Prompt Engineering» p. 235 a «Defenses Against Prompt Attacks» p. 248 (solo índice)"
aliases: [prompt injection, inyección indirecta, indirect prompt injection, lethal trifecta, extracción de prompt, system prompt leakage, hidden context exposure]
creado: 2026-11-27
revisado:
---

# Inyección de prompt

La inyección de prompt es un ataque en el que un texto que entra en la ventana del modelo (escrito
por el usuario o escondido en un documento, una página o un resultado de herramienta) le da
instrucciones que la aplicación no quería. No hay defensa completa: se diseña el sistema para que
un modelo engañado no pueda hacer daño.

Es el riesgo propio de la vertical [Contexto](contexto.md): todo lo que se pone en la ventana para
ayudar al modelo (un [RAG](contexto-y-rag.md), la [memoria](memoria.md), lo que devuelve una
herramienta) es también un canal por el que un tercero le habla. Los filtros que corren en producción sobre lo que entra y lo que sale están en
[Guardrails](../Produccion/guardrails.md).

## Directa o indirecta

Simon Willison propuso el nombre en septiembre de 2022, por analogía con la inyección SQL: en los dos
casos se arma una orden concatenando texto no confiable. Hay dos formas:

- **Directa**: el usuario escribe la instrucción. OWASP: "A user's prompt alters the model's
  behavior".
- **Indirecta**: la instrucción viene escondida en contenido que el modelo procesa, como una página,
  un mail o un archivo. Según OWASP, el texto no tiene que ser visible para una persona, alcanza con
  que el modelo lo lea. Greshake et al. (2023) la formalizaron: según su abstract, el atacante planta
  instrucciones en datos que el modelo probablemente recupere, y lo demostraron contra un buscador
  comercial con chat.

En lectura de esta base, la indirecta es la que más importa en un producto: el atacante no necesita
ser usuario.

OWASP pone la inyección de prompt primera en su Top 10. La versión vigente es el OWASP Top 10 for
LLM Applications, edición 2026, fechada en agosto de 2026 en su repositorio (el detalle, en
[Guardrails](../Produccion/guardrails.md)); según Help Net Security, la inyección sigue primera y
ahora incluye ataques que llegan en imágenes o audio. La página de detalle leída es la de la edición
2025.

## Por qué no hay defensa completa

Cinco fuentes independientes lo sostienen:

1. **OWASP**: "it is unclear if there are fool-proof methods of prevention for prompt injection", y
   ni RAG ni finetuning lo resuelven del todo.
2. **NCSC** (Reino Unido, diciembre de 2025): los modelos actuales "simply do not enforce a security
   boundary between instructions and data inside a prompt", y "there's a good chance prompt injection
   will never be properly mitigated".
3. **Willison** (2025): "we still don't know how to 100% reliably prevent this from happening", y
   detectar el 95% de los ataques es "very much a failing grade".
4. **Nasr et al.** (preprint de 2025, según su abstract): con atacantes que se adaptan a la defensa,
   pasaron 12 defensas publicadas con tasa de éxito "above 90% for most", cuando esas defensas habían
   reportado casi cero.
5. **Anthropic** (noviembre de 2025), sobre su agente de navegador: después de sus mejoras, su
   propio atacante, con 100 intentos por entorno, tuvo éxito entre 1,4% y 2,4% según el modelo, y
   8,0% en uno de ellos sin las salvaguardas. Lo llama "far from a solved problem" y dice que 1% "still represents
   meaningful risk". Son cifras del laboratorio contra su propio atacante.

La razón de fondo la da el NCSC: la inyección SQL se puede mitigar bien con consultas
parametrizadas, que separan la consulta de los datos; dentro de un prompt esa separación no existe,
y el modelo es un "inherently confusable deputy". Huyen coincide: según el resumen de su cap. 5,
ninguna medida de seguridad es infalible.

## Las defensas de diseño: limitar lo que puede hacer un modelo engañado

Lo que se diseña es qué pasa cuando el modelo sea engañado. Quienes lideran el Top 10 de OWASP, según
Help Net Security: "Build the system around it, so
that when the model is fooled, and it will be, nothing important breaks". OWASP y el NCSC coinciden en
estas medidas:

| Medida | OWASP | NCSC |
|---|---|---|
| Mínimo privilegio: el modelo que lee contenido de alguien no tiene más permisos que ese alguien | sí | sí: "should hold no more privilege than that party" |
| Los controles que importan van en código determinista, fuera del modelo | sí | sí |
| Separar y marcar el contenido no confiable como datos | sí | sí, por ejemplo con etiquetas XML |
| Aprobación humana para acciones de alto riesgo | sí | (no lo nombra en lo leído) |
| Registrar entradas, salidas y llamadas a herramientas | (no en lo leído) | sí |

Anthropic, para la inyección indirecta, pide poner el contenido no confiable solo en los resultados
de herramientas y limitar el acceso a datos y acciones. Cómo se limitan las herramientas de un agente se ve en
[Uso de herramientas](../Agentes/uso-de-herramientas.md).

### La trifecta letal

La trifecta letal (*lethal trifecta*) es como Willison resumió en 2025 cuándo un agente puede robar
datos: cuando junta "Access to your private
data", "Exposure to untrusted content" y "The ability to externally communicate". Su regla: "The only
way to stay safe there is to avoid that lethal trifecta combination entirely". Es el marco de un solo
autor, no un estándar; sirve para revisar un diseño: si el agente tiene las tres, se le saca una.

### Patrones que restringen al agente después de leer

Según la reseña de Willison (fuente secundaria: el paper no se abrió), un paper de 14 autores de
junio de 2025 propone seis patrones (selector de acciones, planificar y
después ejecutar, map-reduce con modelos, doble modelo, código y después ejecución, y minimizar el
contexto) con una idea común, citada vía Willison: "once an LLM agent has ingested untrusted input,
it must be constrained so that it is impossible for that input to trigger any consequential
actions". Es una sola fuente.

El patrón de **doble modelo** es de Willison (2023): un modelo con herramientas solo ve entrada
confiable, y otro, sin herramientas, procesa el contenido no confiable. El propio autor admite que no es confiable al 100%.

**CaMeL** (Google DeepMind y ETH, 2025) lo lleva más lejos: el modelo privilegiado escribe un
programa, y cada variable lleva etiquetas de origen y permisos con las que las políticas autorizan o
bloquean acciones. Según su abstract, resuelve 77% de las tareas de AgentDojo con seguridad
demostrable, contra 84% sin defensa. Willison lo llama "the first credible prompt injection
mitigation I've seen" y anota el costo: mantener políticas y aprobaciones que cansan.

## La defensa en el modelo y en los filtros

OpenAI propuso la jerarquía de
instrucciones (2024): entrenar al modelo para que priorice las instrucciones privilegiadas sobre las
del usuario y las de terceros; según su abstract, mejora la robustez "with minimal loss in standard
capabilities". Es una sola fuente, del laboratorio: baja la probabilidad, no reemplaza el diseño.

> [!IMPORTANT]
> Si los filtros y detectores de inyección sirven está en discusión. OWASP los incluye entre las
> mitigaciones. El NCSC pide no depender de listas de frases prohibidas y desconfiar de productos
> que prometen detener la inyección, y Willison considera insuficiente cualquier detector que falle
> en un 5%. Nasr et al. muestran que defensas que reportaban casi cero fallan con un atacante que se
> adapta. Lectura de esta base que las une: un filtro sube el costo del ataque y es una capa más,
> nunca la garantía. Cómo se ponen esos filtros en producción, en
> [Guardrails](../Produccion/guardrails.md).

## El prompt de sistema no es un secreto

Un atacante puede hacer que el modelo repita su prompt de sistema. OWASP lo trataba en la edición
2025 como "System Prompt Leakage"; según Help Net Security, en la de 2026 pasó a llamarse "Hidden
Context Exposure". La página
leída, la de 2025, dice que el prompt de sistema "should not be treated as a secret or as a security
control": no lleva credenciales ni datos de conexión, y los permisos se controlan fuera del modelo.
Es una sola fuente con esa recomendación. Huyen trata el tema en el cap. 5 (p. 236) y junta
jailbreak e inyección en una sección (p. 238), según el índice.

> [!NOTE]
> Sin fuente todavía: una definición primaria que separe jailbreak (saltarse las reglas del modelo)
> de inyección de prompt (que el modelo siga instrucciones ajenas a la aplicación), y un estudio sobre
> envenenamiento de la [memoria](memoria.md) de un agente.

## Qué leer sobre inyección de prompt

Para decidir, la nota del [NCSC](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection),
la mejor explicación corta de por qué no es inyección SQL, y
["The lethal trifecta"](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) de Willison.
Para auditar, el [Top 10 de OWASP 2026](https://raw.githubusercontent.com/GenAI-Security-Project/GenAI-LLM-Top10/main/README.md)
y la página de [LLM01](https://genai.owasp.org/llmrisk/llm01-prompt-injection/). Para diseñar, el
paper de [patrones de diseño](https://arxiv.org/abs/2506.08837) y [CaMeL](https://arxiv.org/abs/2503.18813).
En todos, fijarse en que la defensa limita permisos, acciones y canales de salida.
