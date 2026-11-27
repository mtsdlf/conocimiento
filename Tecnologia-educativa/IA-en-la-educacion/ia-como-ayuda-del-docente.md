---
resumen: >-
  La IA como ayuda del docente es un modelo de lenguaje que le sugiere a un tutor humano qué decir o le redacta los mensajes para que los apruebe, sin hablar directo con el alumno. Los dos ensayos que lo prueban dan resultados positivos, pero ninguno tiene revisión por pares.
estado: borrador
estabilidad: semi
fuentes:
  - "Wang et al., Tutor CoPilot, arXiv 2410.03017 (v3 2026-10-10): https://arxiv.org/abs/2410.03017"
  - "J-PAL, Human-AI cooperation to improve tutoring in the United States: https://www.povertyactionlab.org/evaluation/human-ai-cooperation-improve-tutoring-united-states"
  - "LearnLM Team y Eedi (2025), arXiv 2512.23633: https://arxiv.org/abs/2512.23633"
  - "Tecnologia-educativa/.investigacion/ia-practica-adaptativa-plataformas.md"
aliases: [Tutor CoPilot, IA para tutores, human-in-the-loop tutoring, IA que asiste al docente, copiloto del docente]
creado: 2026-11-27
revisado:
---

# La IA como ayuda del docente

La IA como ayuda del docente es un modelo de lenguaje que le sugiere a un tutor humano qué decir o le redacta los mensajes para que los apruebe, sin hablar directo con el alumno. Los dos ensayos que lo prueban dan resultados positivos, pero ninguno tiene revisión por pares.

Es el rol intermedio entre [la IA como tutor](ia-como-tutor.md), donde el modelo habla con el alumno, y la [tutoría](../../Didactica/Tutoria-y-mentoria/tutoria.md) humana sola, que cubre Didáctica. La persona queda en el medio y filtra lo que dice el modelo.

## Tutor CoPilot: sugerencias en vivo para tutores con poca experiencia

Wang et al. (Stanford) probaron en un ensayo aleatorizado una herramienta que le sugiere al tutor humano, durante la sesión en vivo, cómo responder. El efecto fue de +4 puntos porcentuales en el dominio de los temas (p < 0,01) y de +9 puntos con los tutores peor calificados. Según J-PAL, la aprobación de las pruebas de salida de cada sesión fue de 66 % contra 62 %. El costo, unos 20 dólares por tutor al año.

El tamaño del estudio no coincide entre fuentes: la versión de arXiv dice 900 tutores y 1.800 alumnos; J-PAL dice 783 tutores (388 con la herramienta y 395 de control) y 1.013 alumnos, de marzo a mayo de 2024. No midió pruebas estandarizadas. Es un documento de trabajo, sin revisión por pares en lo verificado.

## Eedi: el modelo redacta, el tutor aprueba

En el ensayo exploratorio del equipo de LearnLM (Google) y Eedi, con 165 alumnos de cinco escuelas secundarias del Reino Unido, el modelo redactaba cada mensaje y un tutor humano lo aprobaba o lo corregía. El 76,4 % de los mensajes se aprobó sin cambios o con cambios mínimos. En problemas nuevos de los temas siguientes, los alumnos acertaron el 66,2 % con el sistema contra el 60,7 % con el tutor humano solo, 5,5 puntos de diferencia. Es un preprint sin revisión por pares y el proveedor del modelo es coautor.

## Por qué el rol intermedio funciona, y qué lo hace frágil

Lo que tienen en común los dos estudios, como lectura de esta base: el beneficio mayor aparece donde el humano sabe menos (los tutores peor calificados en Tutor CoPilot), y el humano cumple la función de [guarda](ia-como-tutor.md#el-diseño-decide-si-suma-o-resta), la restricción que impide darle la respuesta al alumno, que en el tutor de IA cumplen las instrucciones. Es una forma de escalar a tutores con poca formación, no de reemplazarlos.

Es frágil por la evidencia: dos estudios, ninguno con revisión por pares, uno con coautoría del proveedor, resultados medidos en pruebas cercanas a la sesión y no en exámenes externos, y todos escolares. Para capacitar adultos (por ejemplo, un mentor técnico que usa IA para preparar su retroalimentación) no hay estudios; la extensión es inferencia.
