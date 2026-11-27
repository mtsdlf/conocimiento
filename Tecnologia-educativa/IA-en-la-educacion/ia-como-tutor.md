---
resumen: >-
  La IA como tutor es un modelo de lenguaje configurado para guiar al alumno con preguntas y pistas sin darle la respuesta. Los ensayos cortos con diseño cuidado muestran ganancias; el único ensayo largo muestra efectos chicos, que sus autores atribuyen al poco uso.
estado: borrador
estabilidad: semi
fuentes:
  - "Bastani, H. et al. (2025), PNAS 122(26), antes SSRN «Generative AI Can Harm Learning»: https://ideas.repec.org/a/nas/journl/v122y2025pe2422633122.html; resumen de Wharton: https://knowledge.wharton.upenn.edu/article/without-guardrails-generative-ai-can-harm-education/"
  - "Kestin, G. et al. (2025), Scientific Reports (publicado 2025-06-03): https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/"
  - "De Simone, M. et al. (2025), Banco Mundial, Policy Research Working Paper 11125: https://econpapers.repec.org/RePEc:wbk:wbrwps:11125; blog: https://blogs.worldbank.org/en/education/From-chalkboards-to-chatbots-Transforming-learning-in-Nigeria"
  - "Oreopoulos, P. y Low, C. (2026), NBER Working Paper w35620: https://www.nber.org/papers/w35620"
  - "Tecnologia-educativa/.investigacion/ia-practica-adaptativa-plataformas.md"
aliases: [AI tutor, tutor de IA, LLM tutor, tutor con modelo de lenguaje, Khanmigo, GPT Tutor, tutor socrático con IA]
creado: 2026-11-27
revisado:
---

# La IA como tutor

La IA como tutor es un modelo de lenguaje configurado para guiar al alumno con preguntas y pistas sin darle la respuesta. Los ensayos cortos con diseño cuidado muestran ganancias; el único ensayo largo muestra efectos chicos, que sus autores atribuyen al poco uso.

Es la versión con IA del [tutor inteligente](../Tutores-inteligentes/tutores-inteligentes.md): la misma idea de guiar paso a paso, con un modelo que conversa en lugar de un modelo del dominio programado a mano. Su opuesto es [la IA como atajo](ia-como-atajo.md), con el mismo modelo.

## Los cuatro ensayos

| Estudio | Diseño | Resultado | Estado |
|---|---|---|---|
| Bastani et al. (2025) | Experimento de campo, casi 1.000 alumnos de secundaria, matemática (en Turquía, según el resumen de Wharton) | Durante la práctica, +48 % con un chat tipo ChatGPT y +127 % con un tutor con guardas. Sin la IA: el grupo del chat, 17 % por debajo del control; el del tutor, igual al control | Con revisión por pares (*PNAS*) |
| Kestin et al. (2025) | Ensayo cruzado, física de primer año en Harvard, otoño de 2023, 194 alumnos analizados | Tutor con GPT-4 frente a clase de [aprendizaje activo](../../Didactica/Aprendizaje-activo-e-indagacion/aprendizaje-activo.md): mediana del postest 4,5 contra 3,5 (pretest 2,75); ganancia mediana «more than double»; efecto 0,63 en la regresión, 0,73 a 1,3 desviaciones estándar en la cuantílica; mediana de 49 minutos en la tarea | Con revisión por pares (*Scientific Reports*) |
| De Simone et al. (2025) | Ensayo aleatorizado en Edo, Nigeria, seis semanas de inglés extraescolar con Microsoft Copilot (GPT-4) | +0,23 desviaciones estándar en inglés, el resultado principal; +0,31 en la evaluación total (inglés, conocimiento de IA y habilidades digitales) | Documento de trabajo del Banco Mundial, sin revisión por pares en lo verificado |
| Oreopoulos y Low (2026) | Ensayo por conglomerados de dos años, 18 escuelas medias de Tennessee, Khanmigo configurado para no dar respuestas, en matemática remedial | +1,3 percentiles por trimestre: 0,06 a 0,08 desviaciones estándar por año, y 0,14 implícitos para un año de uso activo | Documento de trabajo del NBER, sin revisión por pares |

Cada uno tiene límites que cambian cómo se lo lee. Kestin et al. es una sola asignatura, un solo tema y una sola vez, sin retención a largo plazo; la precisión del tutor dependió de soluciones escritas de antemano por los docentes, y armar la plataforma llevó «several months». En De Simone et al., la asistencia fue irregular por inundaciones y huelgas, y el tamaño de la muestra (800 alumnos, según el buscador) no se cotejó en la fuente; el blog del Banco Mundial redondea el efecto a «about 0.3», que es la cifra total y no la de inglés.

## El diseño decide si suma o resta

Bastani et al. compara dos diseños con el mismo modelo y mide después sin IA. El tutor con guardas tenía instrucciones de no dar la respuesta; el chat abierto, no. En los registros, la mayoría de los alumnos del chat pedía la respuesta, y aprendieron menos que quienes nunca usaron IA. El título cambió al publicarse: el preprint decía que la IA generativa puede dañar el aprendizaje, y la versión de *PNAS* agrega «without guardrails».

En Kestin et al. el tutor tuvo contenido experto (las soluciones de los docentes) además de las instrucciones. Es el equivalente del modelo del dominio de la [arquitectura de un tutor inteligente](../Tutores-inteligentes/arquitectura-de-un-tutor-inteligente.md), como lectura de esta base.

## El uso decide cuánto suma

Oreopoulos y Low es el único ensayo largo de la serie y da el efecto más chico. Su explicación es el uso: el 96 % de los alumnos probó el tutor, pero el mediano le escribió en cerca de un tercio de los días de práctica y solo en el 17 % de las sesiones en que se equivocó, y la mayoría de los mensajes eran respuestas peladas o clics en sugerencias. El resumen concluye que lo difícil es que lo usen, no darles acceso. Según su resumen, tal como lo leyó la investigación de esta base, el efecto fue parecido al de la práctica de Khan Academy sin IA.

> [!IMPORTANT]
> **El tutor de IA enseña mucho (Kestin et al.; De Simone et al.).** Efectos de 0,23 a más de 0,6 desviaciones estándar, en semanas o en una sola clase.
>
> **El tutor de IA enseña poco a escala (Oreopoulos y Low).** 0,06 a 0,08 desviaciones estándar por año en un ensayo de dos años.
>
> Los contextos difieren: universitarios motivados con una tarea corta y contenido preparado, o un programa de seis semanas, frente a escolares en recuperación de matemática durante dos años y con uso escaso. Se parece al patrón que separa los metaanálisis de los [tutores inteligentes](../Tutores-inteligentes/evidencia-de-los-tutores-inteligentes.md) del ensayo a escala de Pane.

## Qué cambia al diseñar un tutor con IA

Lo que sostienen estos estudios, como lectura de esta base:

1. Que no dé la respuesta. Sin esa guarda, el tutor se vuelve un atajo y resta (Bastani).
2. Que tenga el contenido correcto. Soluciones escritas por quien enseña, no solo lo que el modelo sabe (Kestin).
3. Que conozca al alumno. En las pruebas propias de Khan Academy, lo que movió resultados fue darle al tutor el historial reciente del alumno, no retocar las instrucciones; está en la ficha de [modos de estudio de la IA](modos-de-estudio-de-la-ia.md).
4. Que se use. Un tutor disponible que nadie consulta no enseña (Oreopoulos y Low). El uso se diseña como parte de la clase, como en [acceso y uso de la tecnología](../Medios-y-aprendizaje/acceso-y-uso-de-la-tecnologia.md).

Ninguno de estos estudios es de adultos que aprenden IT. El caso más cercano, el de quienes aprenden a programar, está en [aprender a programar con IA](aprender-a-programar-con-ia.md).
