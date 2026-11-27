---
resumen: >-
  Ficha con los modos de estudio de los proveedores de modelos de lenguaje (Anthropic, OpenAI, Google) y el tutor Khanmigo, con qué hace cada uno y qué evidencia publicó, al 2026-11-27.
estado: vigente
estabilidad: volatil
fuentes:
  - "Anthropic, Introducing Claude for Education (2025-04-02): https://www.anthropic.com/news/introducing-claude-for-education (leída 2026-11-27)"
  - "Bonifacic, I. (2025-08-14), Anthropic brings Claude's learning mode to regular users and devs, Engadget: https://www.engadget.com/ai/anthropic-brings-claudes-learning-mode-to-regular-users-and-devs-170018471.html (prensa, texto completo)"
  - "Claude Code, Output styles: https://code.claude.com/docs/en/output-styles (leída 2026-11-27)"
  - "OpenAI, Introducing study mode (2025-07-29): https://openai.com/index/chatgpt-study-mode/ (leída 2026-11-27); EdWeek: https://www.edweek.org/technology/what-teachers-should-know-about-chatgpts-new-study-mode-feature/2025/07"
  - "Willison, S. (2025-07-29), OpenAI: Introducing study mode: https://simonwillison.net/2025/Jul/29/openai-introducing-study-mode/ (texto completo; prompt obtenido por el autor, no publicado por OpenAI)"
  - "Google, Guided Learning in Gemini (2025-08-06): https://blog.google/outreach-initiatives/education/guided-learning/ (leída 2026-11-27)"
  - "Jurenka et al., LearnLM, arXiv 2407.12687: https://arxiv.org/abs/2407.12687"
  - "LearnLM Team, Google (2024, v3 2025-08-22), LearnLM: Improving Gemini for Learning, arXiv 2412.16429: https://arxiv.org/abs/2412.16429 (abstract)"
  - "Khan Academy, blog (2026-05-06): https://blog.khanacademy.org/?p=21314 (leída 2026-11-27)"
  - "Khanmigo, Pricing: https://www.khanmigo.ai/pricing (leída 2026-11-27)"
  - "Oreopoulos y Low (2026), NBER w35620: https://www.nber.org/papers/w35620"
  - "Tecnologia-educativa/.investigacion/ia-practica-adaptativa-plataformas.md"
  - "Tecnologia-educativa/.investigacion/fuentes-ia-y-practica-adaptativa-2026-11.md"
aliases: [study mode, learning mode, guided learning, modo estudio, modo aprendizaje, LearnLM, Khanmigo]
creado: 2026-11-27
revisado: 2026-11-27
---

# Modos de estudio de la IA

Ficha con los modos de estudio de los proveedores de modelos de lenguaje (Anthropic, OpenAI, Google) y el tutor Khanmigo, con qué hace cada uno y qué evidencia publicó, al 2026-11-27.

Son implementaciones de [la IA como tutor](ia-como-tutor.md): intentan que el modelo guíe en lugar de servir de [atajo](ia-como-atajo.md).

Copiado de las páginas oficiales el 2026-11-27 y re-verificado el mismo día, salvo donde se indica. Los modos de los proveedores de modelos son instrucciones de sistema sobre un modelo general: cambian la conducta, no el modelo, y ninguno publicó evidencia de aprendizaje en lo verificado. Qué es una instrucción de sistema está en [prompt](../../IA/Contexto/prompt.md), del tema IA.

| Modo | Proveedor | Desde | Qué hace | Evidencia publicada |
|---|---|---|---|---|
| Learning mode (Claude for Education) | Anthropic | 2025-04-02 | Dentro de Projects, guía con preguntas como «How would you approach this problem?», usa preguntas socráticas y resalta principios. El 2025-08-14 llegó a todos los usuarios de Claude.ai como estilo «Learning», según la prensa (Engadget); no se encontró el anuncio de Anthropic | Ninguna: el anuncio no cita estudios |
| Estilo Learning de Claude Code | Anthropic | 2025-08-14, según la prensa | Agrega bloques `Insight` y, ante una decisión de diseño real, deja `TODO(human)` en el archivo, pide la tarea y se detiene hasta que el usuario la termina. La documentación aclara: «An output style gives Claude instructions to follow. It doesn't guarantee that something always happens or never happens» | Ninguna |
| Study Mode | OpenAI | 2025-07-29 | Instrucciones de sistema escritas «in collaboration with teachers, scientists, and pedagogy experts»; el usuario puede apagarlo. Al lanzarse llegó a los planes Free, Plus, Pro y Team, con Edu anunciado «in the next few weeks». OpenAI admite «some inconsistent behavior and mistakes across conversations» | Ninguna verificada: OpenAI dice que trabaja con expertos de la SCALE Initiative de Stanford |
| Guided Learning (Gemini) | Google | 2025-08-06 | Preguntas abiertas, problemas partidos en pasos, respuestas con imágenes, videos y cuestionarios; en la app Gemini y compartible por Google Classroom. Google dice que lleva a Gemini las capacidades de LearnLM | Ninguna en el anuncio |
| LearnLM | Google | v1 2024-05-21 | Modelo ajustado para pedagogía, no solo instrucciones. En Jurenka et al., educadores y alumnos prefirieron LearnLM-Tutor a un Gemini con instrucciones ajustadas en varias dimensiones pedagógicas. En el informe de diciembre de 2024, expertos prefirieron LearnLM en escenarios de aprendizaje con una fuerza de preferencia media de +31 % frente a GPT-4o, +11 % frente a Claude 3.5 Sonnet y +13 % frente al Gemini 1.5 Pro del que partió | Preferencia de evaluadores, medida por el propio proveedor (preprints, según su resumen); no es aprendizaje medido. Ensayo con Eedi en [la IA como ayuda del docente](ia-como-ayuda-del-docente.md) |
| Khanmigo | Khan Academy | 2023, según el blog de Khan Academy («Three years ago», en mayo de 2026) | Tutor de matemática escolar configurado para no dar respuestas. Al 2026-11-27: gratis para docentes; USD 4 por mes o 44 por año para personas («For you») y familias; escuelas y distritos, a cotizar | Pruebas A/B propias (abajo) y un ensayo externo de dos años: 0,06 a 0,08 desviaciones estándar por año (Oreopoulos y Low, NBER, sin revisión por pares) |

## Lo que movió resultados en Khanmigo

Khan Academy publicó el 2026-05-06 los resultados de unas 20 pruebas A/B hechas entre octubre de 2025 y abril de 2026, con más de 15 millones de conversaciones. Son pruebas de producto, sin revisión por pares, y miden el acierto en el ejercicio siguiente, no lo aprendido días después.

| Cambio | Resultado |
|---|---|
| Darle al tutor un resumen del historial reciente de problemas del alumno | +3,4 % de acierto en el ejercicio siguiente (608.000 conversaciones, 97,5 % de probabilidad de ser mejor) |
| Mostrarle los prerrequisitos que el alumno no domina | +2,7 % (1,36 millones de conversaciones) |
| Limitar al agente al trabajo del alumno | La mitad de respuestas regaladas |
| Poner en las instrucciones ejemplos de otros tipos de problema | Sin efecto |

Según el propio proveedor, lo que mueve resultados es darle al tutor contexto del alumno, no retocar las instrucciones. Es el modelo del estudiante de la [arquitectura de un tutor inteligente](../Tutores-inteligentes/arquitectura-de-un-tutor-inteligente.md), con otra tecnología.

## Las instrucciones de Study Mode

OpenAI no publicó las instrucciones de Study Mode. Simon Willison le pidió a ChatGPT que las copiara y obtuvo el mismo texto en varios intentos, lo que según él indica que es el real. Entre otras reglas, dice «Guide users, don't just give answers» y «DO NOT DO THE USER'S WORK FOR THEM. Don't answer homework questions». Es lo que el modelo devolvió, no un documento de OpenAI.

Re-verificar esta ficha cada tres meses: los modos cambian con cada versión.

> [!NOTE]
> Sin fuente todavía: el anuncio de Anthropic del estilo Learning en Claude.ai (la fecha sale de la prensa) y su estado actual. Según resultados del buscador, el centro de ayuda de Claude anunció que los estilos pasan a ser skills y que Learning queda como skill; la página dio 404 el 2026-11-27 y no se pudo leer.
