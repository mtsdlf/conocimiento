---
resumen: >-
  El modelo de dominio es la representación compartida de los conceptos y las reglas del negocio
  para el que se construye, con un vocabulario que se usa igual en la conversación con el cliente,
  en las especificaciones y en el código.
estado: borrador
estabilidad: estable
fuentes:
  - https://martinfowler.com/bliki/UbiquitousLanguage.html
  - https://martinfowler.com/bliki/BoundedContext.html
  - https://www.eventstorming.com/
  - https://www.domainlanguage.com/ddd/reference/
  - "Eric Evans, Domain-Driven Design (Addison-Wesley, 2003), partes I y IV (no leído): https://www.domainlanguage.com/ddd/"
  - https://www.thoughtworks.com/radar/languages-and-frameworks/github-spec-kit
  - https://arxiv.org/abs/2602.20478
  - https://arxiv.org/pdf/2603.26244
  - https://dev.to/dbrown/ai-coding-assistants-and-the-erosion-of-ubiquitous-language-301a
  - https://dev.to/aws/your-agent-keeps-using-that-word--4g36
  - https://dev.to/vasyltretiakov/rails-not-rules-enforcing-a-coding-agents-domain-vocabulary-with-checks-3ea4
  - https://learn.chatgpt.com/guides/best-practices
aliases: [domain model, lenguaje ubicuo, ubiquitous language, contexto delimitado, bounded context, contexto acotado, Event Storming, glosario del dominio, DDD]
creado: 2026-11-27
revisado:
---

# Modelo de dominio

El modelo de dominio es la representación compartida de los conceptos y las reglas del negocio para el que se construye, con un vocabulario que se usa igual en la conversación con el cliente, en las especificaciones y en el código.

Corre por debajo de toda [Definición](definicion.md): la [especificación](especificacion.md), las [historias](historia-de-usuario.md) y los [criterios de aceptación](criterios-de-aceptacion.md) se escriben con sus palabras. Viene del diseño guiado por el dominio (DDD) de Eric Evans, que en Arquitectura se trata como escuela para decidir dónde van los límites del sistema ([DDD: el límite lo pone el dominio](../../Arquitectura/Fundamentos/escuelas-de-arquitectura.md#ddd-el-límite-lo-pone-el-dominio)). Acá interesa su otra mitad: el lenguaje.

## Un lenguaje común con el cliente

Fowler resume el lenguaje ubicuo de Evans como "building up a common, rigorous language between developers and users", basado en el modelo de dominio que usa el software. Si el cliente dice "pedido" y el código dice `Order` en un módulo y `Purchase` en otro, cada conversación necesita una traducción, y, según esta base, cada traducción es un lugar donde puede perderse una regla. El ejemplo es ilustrativo.

Criterio de esta base: el lenguaje lo pone el negocio. Qué es un "cliente", cuándo un "pedido" pasa a estar "confirmado", qué diferencia hay entre "devolución" y "cancelación" lo sabe quien trabaja en el negocio, y se aprende hablando con esa persona. Por eso el modelo de dominio se arma en el [acuerdo inicial](../Encargo/acuerdo-inicial.md) y en las conversaciones que siguen, no en el código.

## Una palabra, un significado, dentro de un contexto

El ejemplo típico es la palabra "cliente", que significa cosas distintas según el área (blogs de practicantes; la fuente primaria es Evans, que no se leyó). DDD no fuerza un modelo único. Según Fowler, "DDD deals with large models by dividing them into different Bounded Contexts", y dentro de cada contexto delimitado el modelo funciona como lenguaje ubicuo entre quienes desarrollan y quienes conocen el dominio.

Criterio de esta base: el glosario de un proyecto define cada término dentro de su contexto, y dos contextos pueden tener el mismo término con definiciones distintas. Esta base los toma como candidatos a límites de módulos, que se tratan en [modularidad](../../Arquitectura/Modularidad/modularidad.md).

## Descubrir el dominio con Event Storming

Event Storming, de Alberto Brandolini, es "a flexible workshop format for collaborative exploration of complex business domains". Se usa para entender un negocio existente, probar un modelo o diseñar servicios nuevos, y entre sus resultados declarados está marcar los límites de la arquitectura para que el sistema pueda evolucionar.

> [!NOTE]
> Sin fuente todavía: los niveles de Event Storming (panorama, proceso y diseño de software) y su notación de notas de colores. La página oficial no los describe y el libro de Brandolini no se leyó.

## El glosario como contexto del agente

Con agentes de código, el glosario del dominio deja de ser una nota para personas y pasa a ser contexto que el agente carga. Las guías de los fabricantes no lo llaman DDD, pero dicen lo mismo: el agente necesita lo que no se ve en el código, y según OpenAI "A short, accurate AGENTS.md is more useful than a long file full of vague rules". Cómo se le da ese contexto al agente está en [contexto del repositorio](../Construccion/contexto-del-repositorio.md), y el mecanismo general, en [contexto y RAG](../../Arquitectura/Sistemas-con-modelos/contexto-y-rag.md).

El tamaño compite con el resto del contexto. El Radar de Thoughtworks, sobre una herramienta de especificación, dice que su archivo de principios del proyecto sirve cuando cubre el contexto de dominio, pero avisa de "instruction bloat" y después "context rot". Un preprint de caso único (Vasilopoulos, un sistema de 108.000 líneas) propone separar una memoria que se carga siempre de especificaciones que se cargan a pedido.

Practicantes proponen tres mecanismos: una regla en el archivo de contexto que prohíba términos fuera del glosario, el glosario en un formato que se pueda leer por programa, y un chequeo automático del vocabulario en vez de una instrucción en prosa. Un preprint sobre DDD con modelos de lenguaje parte de que el modelo extraiga y defina el vocabulario a partir de los requisitos (según su resumen).

> [!IMPORTANT]
> Que un glosario del dominio mejore lo que produce un agente es, por ahora, anecdótico: lo sostienen blogs de practicantes y preprints de un solo caso, sin estudio controlado. El criterio de esta base es un glosario corto, con los términos que el agente puede confundir, cada uno definido en su contexto, y un chequeo cuando la confusión es cara.

## Cómo se ve un modelo de dominio que funciona

Una prueba simple, que propone esta base: alguien del negocio lee un criterio de aceptación y lo entiende sin traducción, y alguien que lee el código encuentra las mismas palabras en las clases y las funciones. Cuando un término nuevo aparece en una conversación, entra al glosario antes que al código. Cuando el código usa un término que el cliente no reconoce, es una señal de que el modelo se desvió o de que falta una pregunta.
