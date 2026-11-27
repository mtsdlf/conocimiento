---
resumen: >-
  La evaluación diagnóstica averigua qué sabe alguien antes de enseñarle, para decidir por dónde empezar. Las técnicas con más respaldo son inferir por prerrequisitos y preguntar por el primer paso de la solución; preguntarle a la persona cuánto sabe orienta, pero no alcanza.
estado: borrador
estabilidad: semi
fuentes:
  - "Kalyuga y Sweller (2004), Measuring knowledge to optimize cognitive load factors during instruction, Journal of Educational Psychology 96, 558-568 (abstract): https://doi.org/10.1037/0022-0663.96.3.558"
  - "Kalyuga y Sweller (2005), Rapid dynamic assessment of expertise to improve the efficiency of adaptive e-learning, ETR&D 53, 83-93 (abstract): https://doi.org/10.1007/BF02504800"
  - "Cosyn, Doble, Falmagne et al. (2013), cap. 2 de Knowledge Spaces: Applications in Education, Springer: https://www.mheducation.com/content/dam/mhe/research/prek-12/essa-tier-4/aleks-assessing-learning-space.pdf"
  - "Dunning, Heath y Suls (2004), Flawed self-assessment, Psychological Science in the Public Interest 5(3), 69-106 (abstract): https://doi.org/10.1111/j.1529-1006.2004.00018.x"
  - "Sitzmann, Ely, Brown y Bauer (2010), Self-assessment of knowledge, Academy of Management Learning & Education 9(2) (abstract y primeras páginas): https://www.gwern.net/doc/psychology/cognitive-bias/illusion-of-depth/2010-sitzmann.pdf"
  - "Evaluacion-educativa/.investigacion/adaptativa-calificacion-programa.md"
  - "Evaluacion-educativa/.investigacion/propositos-instrumentos-validez.md"
aliases: [evaluación de entrada, evaluación de ubicación, prueba de nivel, placement test, diagnostic assessment, diagnóstico de entrada]
creado: 2026-11-27
revisado:
---

# Evaluación diagnóstica

La evaluación diagnóstica averigua qué sabe alguien antes de enseñarle, para decidir por dónde empezar. Las técnicas con más respaldo son inferir por prerrequisitos y preguntar por el primer paso de la solución; preguntarle a la persona cuánto sabe orienta, pero no alcanza.

Es uno de los tres [propósitos](propositos.md) de la evaluación y el que menos literatura propia tiene: el campo lo trata como un uso de la evaluación formativa o sumativa. Lo que sí hay viene de dos lados, la [evaluación adaptativa](../Evaluacion-adaptativa/evaluacion-adaptativa.md) y la teoría de la carga cognitiva. El porqué de diagnosticar (que lo que ayuda a un novato estorba a un experto) es de las [ciencias del aprendizaje](../../Ciencias-del-aprendizaje/ciencias-del-aprendizaje.md).

## Preguntar por el primer paso

Kalyuga y Sweller (2004) probaron una medida rápida: mostrar un problema y pedir solo el primer paso de la solución. El novato arranca por el principio; el que sabe salta pasos intermedios. Según el abstract, con álgebra y geometría de 9.º y 10.º grado, la medida rápida dio «a highly significant correlation (up to .92)» con las pruebas tradicionales, y redujo el tiempo de prueba por factores de 4,9 y 2,5.

En un segundo estudio, Kalyuga y Sweller (2005) usaron esas pruebas rápidas para adaptar un tutor de álgebra. El grupo con instrucción adaptada mostró, según el abstract, «higher knowledge and cognitive efficiency gains» que el control. La razón de adaptar es el efecto de inversión de la experticia: los ejemplos resueltos y la guía que le sirven al novato dejan de servirle al experto.

> [!WARNING]
> Circula otra cifra para el mismo método, «2,8 veces menos tiempo y correlación de 0,72». Viene de otro trabajo de Kalyuga, con aritmética en octavo grado, no del artículo de 2004. Cada cifra va con su estudio.

Todos estos estudios son con escolares y materiales de matemática. Que el método sirva para diagnosticar a un adulto que aprende un oficio técnico es una inferencia; no se encontró validación en capacitación de informática.

## Inferir por prerrequisitos

Si alguien resuelve un problema que requiere tres cosas, probablemente sabe las tres; si falla una base, probablemente no sabe lo que se apoya en ella. Esa regla es la idea central de los [espacios de conocimiento](../Evaluacion-adaptativa/espacios-de-conocimiento.md): ordenar los temas en un grafo de prerrequisitos y buscar la frontera, lo que la persona «is ready to learn» (Cosyn et al., 2013).

La regla no necesita muestras grandes ni estadística, a diferencia de la [teoría de respuesta al ítem](../Evaluacion-adaptativa/teoria-de-respuesta-al-item.md). Lo costoso es construir el grafo y las preguntas. Su riesgo es dar por sabido algo que no se demostró; los sistemas que la usan marcan esos temas como completados «condicionalmente» y retroceden si la persona se traba.

Aplicado a mano, un diagnóstico para un grupo chico puede hacerse así (inferencia de esta base a partir de las fuentes, no un procedimiento validado):

1. Listá los temas del curso y qué requiere cada uno.
2. Elegí de 5 a 10 preguntas ordenadas por dificultad, que cubran las ramas del grafo.
3. Preguntá primero por los temas altos; un acierto da por probables sus bases.
4. Ante un error, bajá a los prerrequisitos de ese tema.
5. Tratá lo inferido como provisorio y confirmalo en las primeras clases.

## Por qué la autoevaluación no alcanza

Preguntar «¿cuánto sabés de esto?» es barato y sirve para orientar, no para saltear contenido. Dunning, Heath y Suls (2004) concluyen que la correlación entre la autoevaluación y el desempeño es «moderate to meager» en muchos dominios, y que la gente tiende a sobrestimarse. En capacitación, el metaanálisis de Sitzmann et al. (2010) encontró que el conocimiento autoevaluado se relaciona más con la motivación y la satisfacción que con el aprendizaje, donde la relación fue moderada. Según el mismo trabajo, «nearly a third» de los estudios de evaluación de capacitación tomaron el conocimiento autoevaluado como prueba de aprendizaje.

La versión popular de que los que menos saben se sobrestiman más está en disputa; ver [sobreconfianza](../../Psicologia/Juicio-y-decision/sobreconfianza.md).

## Cómo falla un diagnóstico

- **Se usa para acreditar.** Una prueba de cinco preguntas da una ubicación probable, no una certificación; la [validez](../Validez-confiabilidad-y-equidad/validez.md) depende del uso.
- **Infiere sin confirmar.** Dar por sabido lo inferido y no revisarlo cuando la persona se traba.
- **Mide lo que no importa.** Preguntas fáciles de corregir (definiciones) en lugar de lo que el curso pide hacer.

> [!NOTE] Sin fuente todavía: una validación de diagnósticos de entrada en capacitación de adultos o en cursos de informática; toda la evidencia leída es escolar.
