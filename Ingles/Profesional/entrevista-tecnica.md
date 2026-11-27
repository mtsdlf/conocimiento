---
resumen: >-
  La entrevista técnica en inglés evalúa, además de lo técnico, cómo se comunica el razonamiento:
  contar experiencias pasadas con estructura en la parte behavioral y pensar en voz alta, pedir
  aclaraciones y explicar tradeoffs en el coding y el system design.
estado: vigente
estabilidad: semi
fuentes:
  - "Meta Careers, Preparing for your software engineering interview at Meta: https://www.metacareers.com/blog/preparing-for-your-software-engineering-interview-at-meta/"
  - "Amazon, Leadership Principles: https://atoz.amazon/en-us/discover/leadership-principles"
  - "Tech Interview Handbook, Behavioral interviews: https://www.techinterviewhandbook.org/behavioral-interview/"
  - "Tech Interview Handbook, Behavioral interview questions: https://www.techinterviewhandbook.org/behavioral-interview-questions/"
  - "Tech Interview Handbook, Coding interview prep: https://www.techinterviewhandbook.org/coding-interview-prep/"
  - "Tech Interview Handbook, System design: https://www.techinterviewhandbook.org/system-design/"
  - "Alex Xu, A framework for system design interviews (ByteByteGo), vía resúmenes de terceros: https://bytebytego.com/courses/system-design-interview/a-framework-for-system-design-interviews"
  - "Sackett, Zhang, Berry y Lievens (2022), Journal of Applied Psychology 107(11), 2040-2068, vía artículo en Industrial and Organizational Psychology: https://www.cambridge.org/core/product/A20984B138319E3D432E643978BF026D/core-reader"
  - "Behroozi et al. (2020), Does stress impact technical interview performance?, ESEC/FSE, vía metadatos: https://2020.esec-fse.org/details/fse-2020-papers/140/Does-Stress-Impact-Technical-Interview-Performance-"
  - "Huang, Frideger y Pearce (2013), Journal of Applied Psychology 98(6), vía resumen de la BPS: https://www.bps.org.uk/research-digest/non-native-accent-makes-it-harder-get-hired-or-funded"
  - "Hosoda y Stone-Romero (2010), Journal of Managerial Psychology 25(2), vía metadatos: https://www.emeraldinsight.com/doi/pdfplus/10.1108/02683941011019339"
  - "Munro y Derwing, retrospectiva de 2020, Journal of Second Language Pronunciation, vía resumen: https://benjamins.com/catalog/jslp.20038.mun"
aliases:
  - Technical interview
  - Behavioral interview
  - Entrevista de trabajo en inglés
  - STAR
  - System design interview
creado: 2026-11-27
revisado: 2026-11-27
---

# Entrevista técnica

La entrevista técnica en inglés evalúa, además de lo técnico, cómo se comunica el razonamiento: contar experiencias pasadas con estructura en la parte behavioral y pensar en voz alta, pedir aclaraciones y explicar tradeoffs en el coding y el system design.

Las guías de las empresas y del Tech Interview Handbook describen tres formatos, que suelen combinarse: una entrevista **behavioral** sobre experiencias pasadas, una de **coding** (resolver un problema escribiendo código) y, para perfiles con más experiencia, una de **system design** (diseñar un sistema con varios componentes). Cada formato pide un inglés distinto. Cómo se arma la historia profesional que se cuenta es tema de [Presentación profesional](../../Presentacion-profesional/Posicionamiento/historia-profesional.md); acá va cómo se dice.

## Pensar en voz alta: lo que se evalúa es el proceso

La guía oficial de Meta para entrevistas de ingeniería lo dice directo: "We pay a lot of attention to the way you solve problems", y "Thinking out loud gives the interviewer insight into your thinking process." También pide "Be sure to ask clarifying questions", porque el entrevistador suele conocer el problema lo bastante como para dar información que destrabe. El Tech Interview Handbook, una guía escrita por practicantes, pone la comunicación primera entre cuatro criterios de evaluación del coding: hacer preguntas aclaratorias y comunicar el enfoque y los tradeoffs con claridad. Los otros tres son resolver el problema, la competencia técnica y probar el código contra casos normales y de borde.

Para un hispanohablante, la dificultad es hacer dos cosas a la vez: resolver y narrar en una segunda lengua. Eso es carga cognitiva, y por eso conviene que las frases de narrar estén [automatizadas](../Adquisicion/automatizacion.md) antes de la entrevista. Un repertorio corto alcanza. Las frases que siguen son ejemplos propios; ninguna guía leída trae una lista:

| Para | Frase |
|---|---|
| Aclarar el problema | *Before I start, can I ask a couple of questions about the input?* / *Can I assume the list fits in memory?* |
| Anunciar el plan | *Let me start with a brute-force approach, and then we can optimize.* |
| Ganar tiempo sin silencio | *Let me think about this for a second.* / *I'm trying to figure out the edge cases.* |
| Explicar un tradeoff | *This is faster, but it uses more memory. Given the constraints, I'd go with…* |
| Probar | *Let me walk through an example to check it.* |
| Reconocer un error | *Actually, that's not right. Let me fix the loop condition.* |

Ganar tiempo y reparar un malentendido en general están en [Interacción](../Discurso/interaccion.md).

## El system design: acordar antes de diseñar

El system design es una conversación más que un examen. Alex Xu, autor del libro que el Tech Interview Handbook recomienda como introducción, propone cuatro pasos, según resúmenes de su curso: entender el problema y fijar el alcance, proponer un diseño de alto nivel y lograr acuerdo, profundizar en las partes críticas y cerrar. Los tiempos que se le atribuyen varían entre resúmenes; el orden es lo estable. Como inferencia propia, el primer paso es casi todo inglés: preguntar cuántos usuarios hay, qué tiene que pasar si un componente falla y qué queda fuera. Abrir con la [respuesta primero](../Discurso/estructura-del-argumento.md#respuesta-primero-con-una-advertencia) y anunciar la estructura (*I'll start with the high-level design, then go deeper into the storage layer*) sirve más que el vocabulario técnico.

## La behavioral: STAR como andamio

Las preguntas behavioral piden una experiencia real: *Tell me about a time when you had a conflict with a co-worker*, *What was the most difficult bug that you fixed in the past 6 months?*, *How have you handled criticism of your work?* (ejemplos del Tech Interview Handbook). Meta recomienda contestarlas con el método **STAR**: *Situation, Task, Actions, Results*. Pide también ser honesto: hablar de un fracaso no se castiga, y lo que se valora es qué se aprendió. El Tech Interview Handbook suma un quinto paso, *Reflection*, para perfiles senior, y aconseja preparar de tres a cinco historias de alto impacto en vez de memorizar respuestas.

Amazon dice que usa sus Leadership Principles "every day", y hoy son 16 (fuentes viejas listan 14). Entre ellos están *Customer Obsession*, *Ownership*, *Dive Deep* y *Have Backbone; Disagree and Commit*. Como inferencia propia, para una entrevista en Amazon conviene tener una historia para los principios más relevantes del puesto.

Quien traduce del castellano suele cometer tres errores (una inferencia propia, sin estudio detrás): contar en plural (*we did*) cuando la pregunta es qué hiciste vos (*I*), pasar mucho tiempo en la situación y poco en la acción, y no cerrar con un resultado medible. El pasado simple manda en la narración y el [present perfect](../Gramatica/present-perfect.md) aparece al cerrar (*Since then, we've used that approach in every project*).

> [!IMPORTANT]
> **¿STAR está validado?** Lo que tiene evidencia es la entrevista **estructurada** del lado del entrevistador: las mismas preguntas para todos y una rúbrica. En la revisión de Sackett y colegas (2022) quedó como el predictor de desempeño con la validez media más alta, .42. Nada de lo encontrado muestra que enseñarle STAR al candidato mejore su resultado. STAR sirve para ordenar el relato, pero no es una fórmula probada, y no toda entrevista es estructurada.

## Lo que el inglés no controla

Dos hallazgos ponen límites a lo que se puede preparar.

**El estrés pesa.** En un ensayo aleatorizado con 48 estudiantes, que te observe un entrevistador mientras resolvés redujo el rendimiento a menos de la mitad (Behroozi et al., 2020, según la ficha del congreso). La entrevista de pizarrón está discutida como instrumento. Practicar en voz alta y con alguien mirando acerca las condiciones del ensayo a las de la entrevista; no hay estudio que mida cuánto ayuda.

**El acento se juzga.** Hay sesgo contra el acento no nativo en la selección. Huang, Frideger y Pearce (2013) hicieron dos experimentos, uno de contratación y otro de inversión; en el de inversión, los emprendedores con acento no nativo tuvieron menos chances de ser financiados, efecto que pasaba por la "habilidad política" que se les atribuía, según el resumen de la BPS. Hosoda y Stone-Romero (2010) encontraron una brecha mayor en puestos de mucha comunicación, con candidatos simulados. Del otro lado, Munro y Derwing muestran que acento e inteligibilidad son dimensiones en parte independientes: se puede tener acento marcado y que te entiendan bien. El sesgo es del que escucha y no se corrige perdiendo el acento; lo que sí está en manos del candidato es que lo entiendan sin esfuerzo ([Pronunciación](../Pronunciacion/pronunciacion.md)). Qué predice de verdad un proceso de selección está en [Qué predice la selección](../../Presentacion-profesional/Seleccion/que-predice-la-seleccion.md) y los sesgos, en [Sesgos en la selección](../../Presentacion-profesional/Seleccion/sesgos-en-la-seleccion.md).

## Cómo prepararla en dos semanas

1. Escribí tres a cinco historias con STAR y contalas en voz alta, cada una tres veces con menos tiempo, como en el [4/3/2](../Practica/fluidez.md).
2. Resolvé un problema de coding por día narrando todo en inglés, y grabate ([Grabarse y medirse](../Practica/grabarse-y-medirse.md)).
3. Hacé al menos dos simulacros con otra persona mirando, idealmente alguien que te corrija ([Conversación con corrección](../Practica/conversacion-con-correccion.md)).
4. Prepará dos o tres preguntas para el final sobre el equipo y el trabajo; el Tech Interview Handbook tiene una página aparte sobre eso, que todavía no se leyó.
5. Revisá cómo se dicen los términos que vas a usar ([Vocabulario técnico](vocabulario-tecnico.md)).

> [!NOTE]
> Sin fuente todavía: frases modelo de una guía oficial para pedir aclaraciones y para narrar el razonamiento, y la página oficial de Google sobre cómo entrevista hoy (solo se vieron fuentes de 2014).
