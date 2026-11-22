---
resumen: >-
  Los mitos de UX son reglas y cifras que circulan como hechos (tres clics, cinco usuarios, 7±2 opciones, "la gente no lee", un retorno de 100 a 1) sin estudio detrás o contra lo que miden los estudios. Cada mito tiene su origen, lo que dice la evidencia y la nota del tema donde se trata.
estado: vigente
estabilidad: semi
fuentes:
  - "NN/g, The 3-Click Rule for Navigation Is False: https://www.nngroup.com/articles/3-click-rule/"
  - "NN/g, Scrolling and Attention: https://www.nngroup.com/articles/scrolling-and-attention/"
  - "Nielsen, Why You Only Need to Test with 5 Users: https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/"
  - "Baymard Institute, metodología: https://baymard.com/research/methodology"
  - "Cowan (2001), The magical number 4 in short-term memory, Behavioral and Brain Sciences 24(1): https://memory.psych.missouri.edu/assets/doc/articles/2001/cowan-bbs-2001.pdf"
  - "Liu, Gori, Rioul, Beaudouin-Lafon y Guiard (2020), How Relevant is Hick's Law for HCI?, CHI 2020: https://researchportal.ip-paris.fr/en/publications/how-relevant-is-hicks-law-for-hci/ (abstract)"
  - "NN/g, How Little Do Users Read?, que cita a Weinreich et al., ACM TWEB (2008): https://www.nngroup.com/articles/how-little-do-users-read/"
  - "Nielsen (2001), First Rule of Usability? Don't Listen to Users: https://www.nngroup.com/articles/first-rule-of-usability-dont-listen-to-users/"
  - "MeasuringU, NPS y UX: https://measuringu.com/nps-ux/"
  - "Chartbeat según Time (2014): https://time.com/12933/what-you-think-you-know-about-the-web-is-wrong/ (resumen)"
  - "InVision, The business of user experience: https://invisionapp.com/blog/business-of-user-experience; Universidad de Washington: https://depts.washington.edu/ux/why-do-ux (solo como rastro del mito del retorno)"
  - "ISO 9241-210:2019, §3.15 (nota 2) y §5.6 (vista previa pública): https://cdn.standards.iteh.ai/samples/77520/8cac787a9e1549e1a7ffa0171dfa33e0/ISO-9241-210-2019.pdf"
  - "UX/.investigacion/posicion-contraria.md; UX/.investigacion/fundamentos.md, sección 0"
aliases: [mitos de UX, reglas falsas de UX, myths UX, tres clics, cinco usuarios, regla de los tres clics, 7±2, ROI de UX]
creado: 2026-11-22
revisado: 2026-11-22
---

# Mitos de UX

Los mitos de UX son reglas y cifras que circulan como hechos (tres clics, cinco usuarios, 7±2 opciones, "la gente no lee", un retorno de 100 a 1) sin estudio detrás o contra lo que miden los estudios. Cada mito tiene su origen, lo que dice la evidencia y la nota del tema donde se trata.

Un mito de UX suena a regla de diseño: un número redondo que circula sin que se cite la muestra. El campo no los trata en una sola nota; cada uno vive en la nota de su parte, y esta es el índice. Varias refutaciones vienen de un mismo instituto (NN/g), cuyos artículos no cuentan como evidencia independiente entre sí.

## De dónde viene cada mito y qué dice la evidencia

| Mito | De dónde viene | Qué dice la evidencia | Dónde se trata |
|---|---|---|---|
| "Todo debe estar a tres clics" | La referencia publicada más antigua que halló NN/g es el libro de Zeldman de 2001, *Taking Your Talent to the Web*, sin datos | NN/g: la regla "has not been supported by data in any published studies to date". Según NN/g, Porter (2003) halló que el abandono no aumenta con más de tres clics ni baja la satisfacción, y que importan las etiquetas, la orientación y el tiempo de carga. Es refutación de segunda mano: Porter no se leyó | [Navegación](../Arquitectura-de-informacion/navegacion.md) |
| "Nadie scrollea" (el fold) | No se rastreó el origen | NN/g, con eye-tracking propio: arriba del fold, 80% del tiempo de mirada en 2010 y 57% en 2018; abajo, 20% y 43%. En 2018, 74% del tiempo cayó en las dos primeras pantallas. Se scrollea, pero la atención decae rápido | Sin nota propia todavía; dónde cae la atención en una página está en [Jerarquía visual](../Diseno-visual/jerarquia-visual.md) |
| "Cinco usuarios alcanzan siempre" | Nielsen: con L = 31%, un usuario revela cerca de un tercio de los problemas | Nielsen pedía tres rondas de cinco con rediseño en el medio. Faulkner (2003), según resúmenes: con 60 participantes, grupos de cinco hallaron entre casi 100% y 55% de los problemas. Baymard usa 20 | [Test de usabilidad](../Evaluacion/test-de-usabilidad.md) |
| "Un menú no debe pasar de 7±2 opciones" | Miller (1956), sobre memoria a corto plazo | Cowan (2001) baja el límite a unos cuatro "chunks" y dice que el número de Miller fue "a rough estimate and a rhetorical device". Un menú visible se reconoce, no se recuerda | [Carga cognitiva](../Percepcion-y-decision/carga-cognitiva.md) |
| "Menos opciones, decisión más rápida" (ley de Hick) | Hick (1952), tiempo de reacción de elección | Liu et al. (2020, abstract): la ley "no apoya" el principio de "menos es mejor" y el paradigma estímulo-respuesta rara vez es relevante en tareas de HCI | [Leyes de Fitts y Hick](../Percepcion-y-decision/leyes-de-fitts-y-hick.md) |
| "La gente no lee" | Estudios de tiempo en página como el de Weinreich | Según NN/g, que cita a Weinreich et al. (2008): en una página de 593 palabras se alcanza a leer como máximo 28%, y 20% es más probable; se lee la mitad solo si la página tiene 111 palabras o menos | Sin nota propia todavía |
| "Los usuarios saben lo que quieren" | No se rastreó el origen | Nielsen (2001), en un artículo de opinión sin tabla de método: lo declarado está "3 steps removed from the truth"; la correlación entre desempeño y preferencia es 0,44 en aplicaciones de PC y 0,53 en sitios | [Entrevista de usuario](../Investigacion/entrevista-de-usuario.md) |
| "El NPS mide la UX" | MeasuringU cita a Reichheld (2006) por la capacidad predictiva de la intención de recomendar | MeasuringU: la facilidad de uso explica "between 30% and 50%" de la propensión a recomendar; el margen de error del NPS es "usually around twice as wide" que el de la media | [Métricas de UX](../Evaluacion/metricas-de-ux.md) |
| "Las mejores prácticas sirven para cualquier sitio" | Guías de institutos como Baymard | Baymard aclara que no busca "final statistical conclusions" porque cada sitio es distinto. Los casos en contra son anécdotas de vendedores de A/B, sin diseño publicado | [Métricas de UX](../Evaluacion/metricas-de-ux.md) y [Escuelas de UX](escuelas-de-ux.md) |
| "UX es diseño visual" | No se rastreó el origen | ISO 9241-210, nota 2 de §3.15: la UX resulta también de la marca, la funcionalidad, el rendimiento y el estado del usuario. No se buscó una fuente específica de este mito | [Qué es UX](que-es-ux.md) |
| "Usabilidad es facilidad de uso" | No se rastreó el origen; la norma lo llama concepción errónea común | ISO 9241-210 §5.6: "a common misconception that usability refers solely to making products easy to use" | [Qué es UX](que-es-ux.md) |
| "Cada dólar en UX devuelve 100" | Sin origen confirmado | Se atribuye a Gilb (fines de los 80), a un informe de Forrester de 2016 (de pago, sin cita), a Eckert y a la NASA (250 dólares); ninguna fuente primaria vista | Sin nota |
| "El diseño multiplica los ingresos" | McKinsey (2018) | Es correlación, no causalidad, y es autoinforme de consultora | [Escuelas de UX](escuelas-de-ux.md) |

## Dos lecturas cuando las fuentes no coinciden

> [!IMPORTANT]
> Sobre el fold, el eye-tracking de NN/g (más atención arriba) y la medición de Chartbeat citada por Time (que, según comentarios secundarios, en medios la mayoría de las visitas dura menos de 15 segundos de atención activa, 55% sobre 2.000 millones de visitas) no miden lo mismo: tareas guiadas contra tiempo activo en páginas de artículos. La cifra de Chartbeat llegó por comentarios y no por el texto original. Tanto "nadie scrollea" como "da igual dónde se pone cada cosa" son falsos; el tipo de página decide.

> [!IMPORTANT]
> Sobre cinco usuarios, la defensa de Nielsen (iterar, y los problemas graves y frecuentes aparecen antes) y las críticas de Spool y Schroeder y de Faulkner usan datos distintos. "Cinco" es una regla de iteración con p = 31% y usuarios homogéneos, no una garantía de cobertura; para métricas hacen falta más. Las cifras de Spool y Schroeder (35%) y de Faulkner se leyeron por resúmenes.

## Qué pedirle a una regla redonda

Ante una regla de diseño con número, se pide el estudio, la muestra y el tipo de página. Si no aparecen, se usa como hipótesis a testear y no como ley. Una guía puede eliminar una confusión real y aun así no mover la conversión de un sitio concreto: es inferencia de esta base, ninguna fuente la trata de frente. Cómo pesar la fuente está en [Fuentes de UX](fuentes-de-ux.md).

> [!NOTE]
> Sin fuente todavía: el estudio original de Porter (2003); los textos de Miller, Hick y Fitts; la cifra de Chartbeat sobre "66%" de atención abajo del fold, que no se confirmó en Time; el respaldo del "5% de aumento de conversión" que Baymard atribuye a sus guías; y la validación empírica de las heurísticas de Nielsen.

## Leer la refutación de los tres clics

- [NN/g, "The 3-Click Rule for Navigation Is False"](https://www.nngroup.com/articles/3-click-rule/): la sección de evidencia. Fijarse en que el estudio de origen es de una consultora y que la refutación es de segunda mano.
