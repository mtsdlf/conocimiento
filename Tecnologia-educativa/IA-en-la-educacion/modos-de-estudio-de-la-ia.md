---
resumen: >-
  Ficha con los modos de estudio de los proveedores de modelos de lenguaje (Anthropic, OpenAI, Google) y el tutor Khanmigo, con qué hace cada uno y qué evidencia publicó, al 2026-11-27.
estado: borrador
estabilidad: volatil
fuentes:
  - "Anthropic, Introducing Claude for Education (2025-04-02): https://www.anthropic.com/news/introducing-claude-for-education"
  - "Claude Code, Output styles: https://code.claude.com/docs/en/output-styles"
  - "OpenAI, ChatGPT study mode: https://openai.com/index/chatgpt-study-mode/ (no se pudo leer); EdWeek: https://www.edweek.org/technology/what-teachers-should-know-about-chatgpts-new-study-mode-feature/2025/07"
  - "Google, Guided Learning: https://blog.google/outreach-initiatives/education/guided-learning/"
  - "Jurenka et al., LearnLM, arXiv 2407.12687: https://arxiv.org/abs/2407.12687"
  - "Khan Academy, blog (2026-05-06): https://blog.khanacademy.org/?p=21314"
  - "Oreopoulos y Low (2026), NBER w35620: https://www.nber.org/papers/w35620"
  - "Tecnologia-educativa/.investigacion/ia-practica-adaptativa-plataformas.md"
aliases: [study mode, learning mode, guided learning, modo estudio, modo aprendizaje, LearnLM, Khanmigo]
creado: 2026-11-27
revisado:
---

# Modos de estudio de la IA

Ficha con los modos de estudio de los proveedores de modelos de lenguaje (Anthropic, OpenAI, Google) y el tutor Khanmigo, con qué hace cada uno y qué evidencia publicó, al 2026-11-27.

Son implementaciones de [la IA como tutor](ia-como-tutor.md): intentan que el modelo guíe en lugar de servir de [atajo](ia-como-atajo.md).

Copiado de las páginas oficiales el 2026-11-27, salvo donde se indica. Los modos de los proveedores de modelos son instrucciones de sistema sobre un modelo general: cambian la conducta, no el modelo, y ninguno publicó evidencia de aprendizaje en lo verificado. Qué es una instrucción de sistema está en [prompt](../../IA/Contexto/prompt.md), del tema IA.

| Modo | Proveedor | Desde | Qué hace | Evidencia publicada |
|---|---|---|---|---|
| Learning mode (Claude for Education) | Anthropic | 2025-04-02 | Dentro de Projects, guía con preguntas como «How would you approach this problem?», usa preguntas socráticas y resalta principios. Después llegó como estilo «Learning» en Claude.ai (fecha no verificada en fuente primaria) | Ninguna: el anuncio no cita estudios |
| Estilo Learning de Claude Code | Anthropic | sin fecha verificada | Agrega bloques `Insight` y, ante una decisión de diseño real, deja `TODO(human)` en el archivo, pide la tarea y se detiene hasta que el usuario la termina. La documentación aclara: «An output style gives Claude instructions to follow. It doesn't guarantee that something always happens or never happens» | Ninguna |
| Study Mode | OpenAI | 2025-07-29 | Instrucciones de sistema escritas con docentes y especialistas; el usuario puede apagarlo. Según la prensa, OpenAI admite que puede comportarse de forma inconsistente (la página oficial no se pudo leer) | Ninguna verificada |
| Guided Learning (Gemini) | Google | 2025-08-06 | Preguntas abiertas, problemas partidos en pasos, respuestas multimedia y cuestionarios; en la app Gemini y compartible por Google Classroom | Ninguna en el anuncio |
| LearnLM | Google | v1 2024-05-21 | Modelo ajustado para pedagogía, no solo instrucciones. En Jurenka et al., educadores y alumnos prefirieron LearnLM-Tutor a un Gemini con instrucciones ajustadas en varias dimensiones pedagógicas | Preferencia de evaluadores, medida por el propio proveedor (preprint); ensayo con Eedi en [la IA como ayuda del docente](ia-como-ayuda-del-docente.md) |
| Khanmigo | Khan Academy | sin fecha verificada | Tutor de matemática escolar configurado para no dar respuestas | Pruebas A/B propias (abajo) y un ensayo externo de dos años: 0,06 a 0,08 desviaciones estándar por año (Oreopoulos y Low, NBER, sin revisión por pares) |

## Lo que movió resultados en Khanmigo

Khan Academy publicó el 2026-05-06 los resultados de unas 20 pruebas A/B hechas entre octubre de 2025 y abril de 2026, con más de 15 millones de conversaciones. Son pruebas de producto, sin revisión por pares, y miden el acierto en el ejercicio siguiente, no lo aprendido días después.

| Cambio | Resultado |
|---|---|
| Darle al tutor un resumen del historial reciente de problemas del alumno | +3,4 % de acierto en el ejercicio siguiente (608.000 conversaciones, 97,5 % de probabilidad de ser mejor) |
| Mostrarle los prerrequisitos que el alumno no domina | +2,7 % (1,36 millones de conversaciones) |
| Limitar al agente al trabajo del alumno | La mitad de respuestas regaladas |
| Poner en las instrucciones ejemplos de otros tipos de problema | Sin efecto |

Según el propio proveedor, lo que mueve resultados es darle al tutor contexto del alumno, no retocar las instrucciones. Es el modelo del estudiante de la [arquitectura de un tutor inteligente](../Tutores-inteligentes/arquitectura-de-un-tutor-inteligente.md), con otra tecnología.

> [!NOTE]
> Sin fuente todavía: la cifra de «+31 % frente a GPT-4o» que se le atribuye a LearnLM, el texto de las instrucciones de Study Mode que circuló filtrado y la fecha del estilo Learning en Claude.ai. Re-verificar esta ficha cada tres meses: los modos cambian con cada versión.
