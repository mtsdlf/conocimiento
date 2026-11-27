---
resumen: >-
  IA en la educación es la parte de la tecnología educativa que estudia qué pasa con el aprendizaje cuando entra un modelo de lenguaje. La evidencia se ordena por el rol que cumple la IA (tutor, ayuda de quien enseña o atajo que hace la tarea), porque el mismo modelo da resultados opuestos según el rol.
estado: borrador
estabilidad: semi
fuentes:
  - "Bastani et al. (2025), PNAS 122(26): https://ideas.repec.org/a/nas/journl/v122y2025pe2422633122.html"
  - "Kestin et al. (2025), Scientific Reports: https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/"
  - "Oreopoulos y Low (2026), NBER w35620: https://www.nber.org/papers/w35620"
  - "Wang et al., Tutor CoPilot, arXiv 2410.03017: https://arxiv.org/abs/2410.03017"
  - "Tecnologia-educativa/.investigacion/ia-practica-adaptativa-plataformas.md"
aliases: [AI in education, AIED, IA generativa en educación, ChatGPT en educación, tutores de IA, LLM en educación]
creado: 2026-11-27
revisado:
---

# IA en la educación

IA en la educación es la parte de la tecnología educativa que estudia qué pasa con el aprendizaje cuando entra un modelo de lenguaje. La evidencia se ordena por el rol que cumple la IA (tutor, ayuda de quien enseña o atajo que hace la tarea), porque el mismo modelo da resultados opuestos según el rol.

Dentro de [Tecnología educativa](../tecnologia-educativa.md) es la parte más nueva y la que más rápido cambia. Hereda de los [tutores inteligentes](../Tutores-inteligentes/tutores-inteligentes.md) la idea de guiar paso a paso y la [escalera de pistas](../Tutores-inteligentes/pistas-de-un-tutor-inteligente.md); se cruza con la [práctica adaptativa](../Practica-adaptativa/practica-adaptativa.md) cuando el tutor recibe el historial del alumno. Cómo funciona un modelo de lenguaje (que genera texto probable, no verdadero, y por qué alucina) no se explica acá: está en el tema [IA](../../IA/ia.md), sobre todo en [Modelos](../../IA/Modelos/modelos.md) y [alucinación](../../IA/Modelos/alucinacion.md).

## Por qué se divide por rol y no por producto

La IA generativa puede cumplir roles que ya existían, sin ser un mecanismo de aprendizaje nuevo. En el experimento de Bastani et al. (2025), el mismo modelo, GPT-4, subió el rendimiento durante la práctica en los dos grupos que lo usaron, y al sacarlo dejó a uno 17 % por debajo del control y al otro igual que el control. Lo que cambió fue el rol: en un grupo hacía la tarea, en el otro guiaba sin dar la respuesta. Es el [debate de los medios](../Medios-y-aprendizaje/debate-de-los-medios.md) con otra tecnología.

| Rol | Qué hace la IA | Qué muestra la evidencia | Nota |
|---|---|---|---|
| Tutor | Guía al alumno con preguntas y pistas, sin resolverle | Ganancias en estudios cortos con diseño cuidado; efectos chicos en el único ensayo largo | [La IA como tutor](ia-como-tutor.md) |
| Ayuda de quien enseña | Le sugiere a un tutor humano qué decir; no habla con el alumno | Positivo en dos estudios, ambos sin revisión por pares | [La IA como ayuda del docente](ia-como-ayuda-del-docente.md) |
| Atajo | Hace la tarea o el razonamiento por el alumno | Rinde más durante la tarea y aprende menos después | [La IA como atajo](ia-como-atajo.md) |

Aprender a programar con IA cruza los tres roles y es el caso más cercano a enseñar IT, así que tiene su propia nota: [aprender a programar con IA](aprender-a-programar-con-ia.md).

## Cuánto pesa la evidencia

Tres advertencias valen para todas las notas de la vertical:

1. Es escolar o universitaria. Matemática de secundaria, física de primer año, inglés en Nigeria, programación inicial. Ningún estudio leído es de adultos que aprenden un oficio técnico en su trabajo; llevarlo a ese caso es inferencia.
2. Mucho no tiene revisión por pares. Varios estudios son preprints de arXiv o documentos de trabajo del NBER o del Banco Mundial, y algunos tienen al proveedor del modelo como coautor. Cada nota lo marca.
3. Las herramientas envejecen rápido. Un estudio con un modelo de 2023 dice poco del modelo de hoy. Como hipótesis de esta base, la diferencia entre guiar y resolver se mantiene entre versiones; ningún estudio leído lo probó con modelos nuevos.

> [!NOTE]
> Sin fuente todavía: un metaanálisis general del uso de ChatGPT en el aprendizaje (se buscaba Wang y Fan, 2025). No se cita ninguno.

## Qué hay adentro de la IA en la educación

- [La IA como tutor](ia-como-tutor.md): los ensayos de Bastani, Kestin, De Simone y Oreopoulos y Low, y por qué el diseño y el uso pesan más que el modelo.
- [La IA como ayuda del docente](ia-como-ayuda-del-docente.md): Tutor CoPilot y el ensayo de Eedi, donde la IA le sugiere al tutor humano.
- [La IA como atajo](ia-como-atajo.md): la descarga cognitiva, el experimento de Bastani y los estudios de Gerlich y del MIT con sus límites.
- [Aprender a programar con IA](aprender-a-programar-con-ia.md): los estudios de novatos, la brecha que se ensancha y la ilusión de competencia, que es la [ilusión de saber](../../Ciencias-del-aprendizaje/Metacognicion-y-autorregulacion/ilusion-de-saber.md) de las Ciencias del aprendizaje.
- [Modos de estudio de la IA](modos-de-estudio-de-la-ia.md): ficha fechada con los modos de estudio de los proveedores de modelos y Khanmigo, el tutor con IA de Khan Academy, al 2026-11-27.
