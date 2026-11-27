---
resumen: >-
  El repaso espaciado con software es usar un programa de tarjetas que estima cuándo se va a olvidar cada dato y lo vuelve a preguntar cerca de ese momento. Automatiza espaciar y recuperar de memoria; un metaanálisis en estudiantes de salud respalda el espaciado digital, y la evidencia de los algoritmos mide cuánto predicen el olvido y no cuánto se aprende.
estado: borrador
estabilidad: estable
fuentes:
  - "Martinengo, L. et al. (2024), J Med Internet Res 26:e57760, publicado 2024-10-10: https://pmc.ncbi.nlm.nih.gov/articles/PMC11502984/"
  - "Deng, F., Gluckstein, J. A. y Larsen, D. P. (2015), Perspectives on Medical Education 4(6):308-313: https://pubmed.ncbi.nlm.nih.gov/26498443/"
  - "Manual de Anki, What spaced repetition algorithm does Anki use: https://docs.ankiweb.net/faqs/what-spaced-repetition-algorithm"
  - "Manual de Anki, Deck options: https://docs.ankiweb.net/deck-options.html"
  - "Benchmark de open-spaced-repetition: https://expertium.github.io/Benchmark.html (comunidad del proyecto, sin fecha)"
  - "Tecnologia-educativa/.investigacion/ia-practica-adaptativa-plataformas.md"
aliases: [spaced repetition software, SRS, tarjetas de memoria, flashcards, repetición espaciada con software, retención deseada, desired retention, programador de repasos]
creado: 2026-11-27
revisado:
---

# Repaso espaciado con software

El repaso espaciado con software es usar un programa de tarjetas que estima cuándo se va a olvidar cada dato y lo vuelve a preguntar cerca de ese momento. Automatiza espaciar y recuperar de memoria; un metaanálisis en estudiantes de salud respalda el espaciado digital, y la evidencia de los algoritmos mide cuánto predicen el olvido y no cuánto se aprende.

El mecanismo psicológico (por qué espaciar y testearse retienen más que releer) está en [práctica espaciada y recuperación](../../Psicologia/Aprendizaje-y-memoria/practica-espaciada-y-recuperacion.md) y no se repite acá. Esta nota trata lo que agrega el software; los programas de tarjetas concretos, como Anki, están en la ficha de [herramientas de práctica adaptativa](herramientas-de-practica-adaptativa.md).

## Cómo decide el programa cuándo preguntar

Cada tarjeta tiene una pregunta y una respuesta. El programa la muestra, la persona intenta recordar y después califica cuánto le costó. Con esa calificación, el programa calcula el próximo intervalo: si se recordó fácil, el intervalo se alarga mucho; si se olvidó, vuelve a empezar corto.

Hay dos familias de reglas para calcular ese intervalo:

- Reglas fijas con un factor de facilidad. Cada tarjeta tiene un multiplicador que sube o baja según las respuestas, con un piso para que no se achique de más. Es la lógica de los algoritmos derivados de SuperMemo.
- Un modelo de la memoria ajustado a cada persona. El programa estima para cada tarjeta tres cosas (cuán probable es recordarla hoy, cuánto dura en memoria y cuán difícil es) y ajusta los parámetros con el historial de repasos de quien la usa. Esas tres estimaciones forman el modelo de tres componentes que el proyecto FSRS atribuye a Piotr Woźniak, creador de SuperMemo.

Los algoritmos concretos, sus versiones y los valores por defecto están en la ficha de [herramientas de práctica adaptativa](herramientas-de-practica-adaptativa.md).

## La retención deseada: la perilla que se elige

Con un modelo de la memoria, en lugar de intervalos se elige qué probabilidad de recordar se quiere tener al momento del repaso. Pedir más retención obliga a repasar antes y más seguido. El programa de tarjetas de la [ficha](herramientas-de-practica-adaptativa.md) trae 90 % por defecto, que su manual llama «a good balance», y advierte que más del 97 % sobrecarga de repasos. El modelo además necesita historia: con «less than a few hundred» repasos, según el mismo manual, el ajuste suele andar mal.

## Qué dice la evidencia

| Pregunta | Evidencia | Qué vale |
|---|---|---|
| ¿Ayuda el espaciado digital? | Metaanálisis de Martinengo et al. (2024): 23 estudios, 3.371 participantes de ciencias de la salud. Conocimiento frente a educación masiva en línea: diferencia de medias estandarizada 0,32 (IC 95 % 0,13 a 0,51, 9 estudios, certeza moderada); retención: 0,38; cambio de conducta clínica frente a nada: 0,67 (en el texto, 0,63, con 2 estudios) | Es evidencia del espaciado, no de un programa. 19 de los 23 estudios tenían riesgo de sesgo incierto o alto, hubo mucha heterogeneidad y ninguno justificó el intervalo elegido |
| ¿Se asocia el uso de tarjetas con mejores notas? | Deng, Gluckstein y Larsen (2015): 72 estudiantes de medicina de una institución; cada 1.700 tarjetas únicas en un programa de repaso o 445 preguntas de práctica se asociaron con un punto más en el examen Step 1, controlando por el examen de ingreso y otras variables; las tarjetas comerciales prehechas no predijeron | Correlacional y exploratorio: quien más usa puede ser quien más estudia |
| ¿Qué algoritmo predice mejor el olvido? | Un benchmark público de la comunidad de un algoritmo abierto, con casi 350 millones de repasos: el modelo de la memoria ajustado supera a la regla fija en casi todos los usuarios (las cifras, en la [ficha](herramientas-de-practica-adaptativa.md)) | Mide predicción, no aprendizaje. La regla fija no fue diseñada para dar probabilidades, y el autor advierte: «There is no way to have a truly fair, no caveats, comparison» |

Según el manual del programa, el modelo ajustado «reportedly requires fewer reviews» que la regla fija. Si es así, la ventaja de un mejor algoritmo es de eficiencia (menos repasos para la misma retención), no de cuánto se aprende. Es una inferencia de esta base a partir del manual.

Estudios posteriores sobre el uso de tarjetas digitales dan resultados mixtos, mayormente observacionales y autorreportados; se vieron solo resúmenes y no se citan cifras.

## Cómo falla

Como lectura de esta base, a partir de lo anterior: el software programa bien el repaso, pero no decide qué vale la pena memorizar ni garantiza que se entienda lo que se memoriza. Las tarjetas sirven para datos, vocabulario y definiciones, que es donde está la evidencia (estudiantes de salud, vocabulario de idiomas en [repetición espaciada](../../Ingles/Adquisicion/repeticion-espaciada.md)). Para habilidades que se aprenden resolviendo problemas, el repaso espaciado se hace con ejercicios, que es lo que intentan los [sistemas adaptativos](sistemas-adaptativos.md).
