---
resumen: >-
  La economía del comportamiento aporta al marketing hipótesis sobre cómo decide la gente (defaults, normas sociales, señuelos, escasez). Pero buena parte de sus efectos se achica o desaparece al corregir el sesgo de publicación o al replicarlos a escala.
estado: borrador
estabilidad: semi
fuentes:
  - "Mertens et al. (2022), PNAS 119(1), meta-análisis de nudges: https://pmc.ncbi.nlm.nih.gov/articles/PMC8740589"
  - "Mertens et al. (2022), respuesta a Maier et al.: https://pmc.ncbi.nlm.nih.gov/articles/PMC9351449"
  - "Maier et al. (2022), PNAS 119(31), No evidence for nudging after adjusting for publication bias: https://pmc.ncbi.nlm.nih.gov/articles/PMC9351501"
  - "DellaVigna y Linos, RCTs to Scale, NBER w27594 (2020); Econometrica 90(1) (2022): https://www.nber.org/papers/w27594"
  - "Klein et al. (2014), Many Labs 1, Social Psychology 45(3) (abstract): https://pure.psu.edu/en/publications/investigating-variation-in-replicability-a-many-labs-replication-/"
  - "Hagger et al. (2016), ego depletion multilab: https://research.tilburguniversity.edu/en/publications/a-multi-lab-pre-registered-replication-of-the-ego-depletion-effec/"
  - "Frederick, Lee y Baskin (2014), The Limits of Attraction, JMR: https://marketing.wharton.upenn.edu/wp-content/uploads/2016/10/The-Limits-of-Attraction.pdf"
  - "Huber, Payne y Puto (2014), JMR: https://people.duke.edu/~jch8/bio/Papers/HuberPaynePutoJMR%202014.pdf"
  - "Barton et al. (2022) y Ladeira et al. (2023), meta-análisis de escasez: https://research.monash.edu/en/publications/scarcity-tactics-in-marketing-a-meta-analysis-of-product-scarcity/"
  - "Bohner y Schlüter (2014), PLOS ONE, réplica del estudio de toallas: https://pmc.ncbi.nlm.nih.gov/articles/PMC4118982"
  - "Schimmack et al., Reconstruction of a Train Wreck (blog): https://replicationindex.com/2017/02/02/reconstruction-of-a-train-wreck-how-priming-research-went-of-the-rails/"
  - "Informe .investigacion/medicion-y-persuasion.md, sección P11 (2026-11-18)"
aliases: [behavioral economics, economía conductual, nudge, nudges, arquitectura de la elección, choice architecture, sesgos cognitivos, crisis de replicación]
creado: 2026-11-18
revisado:
---

# Economía del comportamiento en marketing

La economía del comportamiento aporta al marketing hipótesis sobre cómo decide la gente (defaults, normas sociales, señuelos, escasez). Pero buena parte de sus efectos se achica o desaparece al corregir el sesgo de publicación o al replicarlos a escala.

## Defaults y normas sociales

Los defaults son la categoría de mayor efecto en el meta-análisis de Mertens et al. (2022): d = 0.62 [0.50, 0.73]. La norma social también ayuda: Goldstein, Cialdini y Griskevicius (2008) aumentaron la reutilización de toallas de hotel, aunque las réplicas no confirmaron qué mensaje rinde más [S].

## Cuánto efecto queda al corregir el sesgo de publicación

> [!IMPORTANT]
> Disputado: ¿funcionan los nudges en promedio?
> - **Sí, con sesgo**: Mertens et al. reúnen más de 200 estudios y dan d = 0.43 sin corregir. Reconocen sesgo de publicación: d = 0.31 si es moderado y 0.08 si es severo.
> - **No en promedio**: Maier et al. corrigen el sesgo y obtienen 0.04 [0.00, 0.14]. Igual admiten heterogeneidad: algunos nudges podrían funcionar.

DellaVigna y Linos compararon 126 ensayos de dos Nudge Units de EE. UU., con 23 millones de personas. En revistas el efecto era de 8.7 puntos porcentuales; en las Nudge Units, de 1.4. El sesgo de publicación "can account for the full difference". Inferencia: a escala, serían 1 o 2 puntos.

## Los efectos que no se replicaron

| Efecto | Qué pasó | Fuente |
|---|---|---|
| Priming social | Many Labs 1 replicó 10 de 13 efectos; el priming con dinero y con bandera, no | Klein et al. 2014, solo abstract [M] |
| Ego depletion | d = 0.04 en 23 laboratorios; un multilab posterior halló d = 0.10 | Hagger et al. 2016 [S] |
| Señuelo (decoy) | Disputado: sin efecto en 19 estudios con estímulos naturales, sí con atributos numéricos; Huber, Payne y Puto sostienen que replica en las condiciones originales | Frederick, Lee y Baskin 2014; Huber, Payne y Puto 2014 [S] |
| Escasez | La escasez por exceso de demanda aumenta la compra; la urgencia, no. Mide intención, no ventas | Barton et al. 2022; Ladeira et al. 2023 [S] |

El capítulo de priming de Kahneman también está en disputa: un blog de Schimmack et al. da a sus estudios una potencia mediana observada del 57% [S].

Un efecto sin réplica que se sigue citando funciona como uno de los [mitos de marketing](../Fundamentos/mitos-de-marketing.md).

Los libros de Cialdini, Kahneman y Sutherland no se leyeron. Sutherland es practicante: sirve para generar hipótesis, no para decidir. La [respuesta directa](respuesta-directa.md) da el método para convertir un efecto de libro en un test propio.

> [!NOTE]
> Sin fuente todavía: réplicas directas de la escasez de Cialdini, el anclaje en Many Labs 1 y estos efectos en comercio argentino.

## Leer *RCTs to Scale*

- **[DellaVigna y Linos, RCTs to Scale](https://www.nber.org/papers/w27594)**: la comparación de 8.7 contra 1.4 puntos y el análisis del sesgo de publicación. Leer junto con Mertens y Maier.
