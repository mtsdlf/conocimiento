---
resumen: >-
  Con el criterio de esta base, en UX las normas y los papers con método mandan sobre los institutos con método declarado, y estos sobre los blogs y las consultoras con autoinforme. Las guías de plataforma y los sistemas de diseño públicos sirven como ejemplo de práctica, no como evidencia. La norma ISO 9241 es de pago; WCAG, la mayoría de los artículos de NN/g y Atomic Design son gratuitos.
estado: borrador
estabilidad: semi
fuentes:
  - "Hornbæk, Sander, Bargas-Avila y Simonsen (2014), Is once enough? On the extent and content of replications in human-computer interaction, CHI 2014, DOI 10.1145/2556288.2557004: https://research.google.com/pubs/archive/42512.pdf"
  - "Baymard Institute, metodología: https://baymard.com/research/methodology; About: https://baymard.com/about"
  - "Kohavi y Thomke, The Surprising Power of Online Experiments, HBR, 2017: https://web-docs.stern.nyu.edu/executive/The%20Surprising%20Power%20of%20Online%20Experiments.pdf"
  - "NN/g, Why You Only Need to Test with 5 Users: https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/"
  - "NN/g, How Little Do Users Read?: https://www.nngroup.com/articles/how-little-do-users-read/"
  - "NN/g, Data Tables, 2022: https://www.nngroup.com/articles/data-tables/"
  - "ISO 9241-210:2019, ficha oficial: https://www.iso.org/standard/77520.html"
  - "W3C, WCAG 2.2: https://www.w3.org/TR/WCAG22/"
  - "Frost, Atomic Design: https://atomicdesign.bradfrost.com/"
  - "UX/.investigacion/fundamentos.md, sección 5; UX/.investigacion/posicion-contraria.md"
aliases: [peso de las fuentes, jerarquía de evidencia en UX, tipos de fuente, evidencia en UX, qué es de pago en UX]
creado: 2026-11-22
revisado:
---

# Fuentes de UX

Con el criterio de esta base, en UX las normas y los papers con método mandan sobre los institutos con método declarado, y estos sobre los blogs y las consultoras con autoinforme. Las guías de plataforma y los sistemas de diseño públicos sirven como ejemplo de práctica, no como evidencia. La norma ISO 9241 es de pago; WCAG, la mayoría de los artículos de NN/g y Atomic Design son gratuitos.

Buena parte de la evidencia cuantitativa reunida para esta base viene de institutos (NN/g, Baymard) que venden cursos, informes o auditorías, y el campo académico replica poco. Por eso importa preguntar de quién es la fuente, con qué método y qué gana con la conclusión.

## Cómo se pesa una fuente

Ninguna fuente leída da pesos por tipo: la tabla es criterio de esta base, no un hallazgo.

| Tipo | Ejemplos | Sirve para | Peso | Por qué |
|---|---|---|---|---|
| Normas | ISO 9241-210 (definiciones y proceso); WCAG 2.2 (accesibilidad) | Definir y exigir | Alto en definiciones | Las mantiene un organismo; la norma de proceso no trae cifras de beneficio |
| Papers revisados por pares | Mathur et al. (2019), CSCW; Luguri y Strahilevitz (2021); Liu et al. (2020), CHI | Qué se sabe con método | Alto en rigor | Muestras y métodos visibles; pero el campo replica poco |
| Libros canónicos | Norman; Garrett; Rogers, Sharp y Preece | Vocabulario y marcos | Alto como marco | Evidencia dispar; casi todos se leyeron por ficha |
| Institutos con método declarado | Baymard; NN/g; MeasuringU | Regularidades de uso y guías prácticas | Medio-alto | Método propio y no revisado por pares; venden lo que investigan |
| Libros de autores que miden en grande | Kohavi, Tang y Xu (A/B) | Experimentación | Alto en su tema | Escriben desde empresas con miles de experimentos; la cifra clave viene de los mismos autores |
| Consultoras con autoinforme | McKinsey, Design Index | Hipótesis | Bajo-medio | Correlación; conflicto de interés declarado en [Escuelas de UX](escuelas-de-ux.md) |
| Practicantes | deceptive.design; blogs de diseñadores | Cómo se hace en la práctica | Medio | Opinión de practicantes; se marcan como tales |
| Blogs de vendedores de experimentación | Optimizely, Kameleoon | Anécdotas | Bajo | Interés propio y casos sin diseño publicado |
| Guías de plataforma y sistemas de diseño públicos | GOV.UK, Carbon | Ejemplo de práctica | Bajo como evidencia | Muestran decisiones, no resultados |

Las cifras de un instituto pesan según su método. Baymard declara el suyo: 822 guías destiladas de más de 34.000 problemas observados en 25 rondas de test, con sesiones de una hora, y aclara que no busca "final statistical conclusions". NN/g declara el método por artículo. Los artículos de NN/g sobre un mismo tema comparten instituto, método e interés comercial, y cuentan como una fuente, no como varias independientes.

## Qué es de pago y qué es gratuito

| Fuente | Acceso |
|---|---|
| ISO 9241-210 | De pago; la vista previa gratuita llega hasta §5.7 y el índice |
| WCAG 2.2 y sus documentos Understanding | Gratuitos, en el sitio del W3C |
| NN/g | Los artículos son gratuitos; los informes y cursos son de pago (no verificado) |
| Baymard | Parcialmente gratuito: unos 470 artículos (la página también dice 450+), que cubren "about 5%" de los hallazgos; la biblioteca Premium, la auditoría y la capacitación son de pago, sin precio publicado |
| Kohavi, Tang y Xu | De pago; la versión digital cuesta 45 USD según la ficha |
| *Atomic Design* | Gratis en línea; el libro en papel dejó de venderse y el ebook es de pago (cerca de 10 USD) |

Las cifras de Baymard son de autodescripción, sin verificación de terceros.

## Cuál manda cuando dos fuentes chocan

Este orden es un criterio de esta base, no de las fuentes.

1. Si una fuente tiene datos con método y la otra opinión, manda la de datos.
2. Si chocan dos con datos, se mira de qué muestra sale cada una: el tipo de página, el país, el tamaño del sitio.
3. Si el choque es de definiciones, ninguna manda; se aclara qué llama cada una con cada palabra.
4. Si una es de un instituto con producto a la venta, se busca una segunda independiente o se dice que hay una sola.

Dos casos reales de choque. NN/g defiende el test cualitativo con pocos usuarios y Kohavi dice que hay que medir; son complementarios, porque cada una responde otra pregunta (ver [Escuelas de UX](escuelas-de-ux.md)). Y sobre cuánta atención hay arriba del fold, el eye-tracking de NN/g con tareas y el tiempo activo en páginas de medios de Chartbeat no miden lo mismo, así que el tipo de página decide (ver [Mitos de UX](mitos-de-ux.md)).

## El campo replica poco

Hornbæk et al. (CHI 2014) examinaron cuatro medios de publicación, con 891 artículos, y hallaron que el 3% intentaba replicar un resultado anterior. Las replicaciones solían confirmar lo anterior, pero trataban la replicación como confirmar o no confirmar, rara vez analizaban tamaños de efecto o comparaban en detalle. Leído: el abstract y la introducción. Esta base lee que eso baja el peso de cualquier cifra aislada de un solo estudio.

Dos datos de muestra que anotan las fuentes: el estudio de lectura de Weinreich et al. usó participantes muy alfabetizados, y Baymard recluta con pago de hasta 100 USD (300 USD en B2B y perfiles difíciles de reclutar).

> [!NOTE]
> Sin fuente todavía: un estudio sobre sesgo de laboratorio con estudiantes en HCI; una auditoría independiente de NN/g o de Baymard (que sean autoinforme es una observación estructural de esta base, no un hallazgo documentado); y la validación empírica de las heurísticas de Nielsen.

## Leer a Hornbæk et al. sobre cuánto se replica

- [Hornbæk, Sander, Bargas-Avila y Simonsen (2014)](https://research.google.com/pubs/archive/42512.pdf): el abstract y la introducción, para el 3% y para cómo tratan la replicación. Fijarse en que la cita correcta es CHI 2014, y en que hay cuatro autores.
