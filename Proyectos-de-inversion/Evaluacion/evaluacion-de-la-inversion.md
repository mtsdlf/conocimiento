---
resumen: >-
  Evaluar una inversión es estimar la plata que entra y sale por hacerla, año por año, compararla con lo que rendiría esa plata en otro uso de riesgo parecido y decidir con un criterio que tenga en cuenta cuándo llega cada peso; el criterio de referencia es el valor actual neto, y la tasa interna de retorno y el repago se usan a su lado.
estado: vigente
estabilidad: estable
fuentes:
  - "OpenStax, Principles of Finance (2022), secciones 16.1 a 16.5 (leído por extractor): https://openstax.org/books/principles-finance/pages/16-why-it-matters"
  - "Damodaran, Applied Corporate Finance, 4.ª ed., presentaciones del cap. 5 «Measuring Returns on Investments» (leído): https://pages.stern.nyu.edu/~adamodar/pdfiles/acf4E/presentations/invretA.pdf"
  - "Graham y Harvey (2002), How do CFOs make capital budgeting and capital structure decisions?, Journal of Applied Corporate Finance 15(1), versión corta de su artículo de JFE 2001 (leído): https://people.duke.edu/~charvey/Research/Published_Papers/P76_How_do_CFOs.pdf"
  - "Graham (2022), Presidential Address: Corporate Finance and Reality, versión NBER w29841, Tabla I (leído en esa parte): https://nber.org/system/files/working_papers/w29841/w29841.pdf"
  - "Proyectos-de-inversion/.investigacion/evaluacion.md (2026-11-27)"
aliases: [evaluación de inversiones, evaluación de proyectos, evaluación de proyectos de inversión, investment appraisal, project appraisal, capital budgeting techniques, criterios de inversión, decisión de inversión]
creado: 2026-11-27
revisado: 2026-11-27
---

# Evaluación

Evaluar una inversión es estimar la plata que entra y sale por hacerla, año por año, compararla con lo que rendiría esa plata en otro uso de riesgo parecido y decidir con un criterio que tenga en cuenta cuándo llega cada peso; el criterio de referencia es el valor actual neto, y la tasa interna de retorno y el repago se usan a su lado.

Es la primera etapa de un [proyecto de inversión](../proyectos-de-inversion.md) y la que le da los números a todas las demás. Lo que sale de acá es el caso que se presenta en la [aprobación](../Aprobacion/aprobacion-de-la-inversion.md), la línea base que se sigue en la [ejecución](../Ejecucion/ejecucion-de-la-inversion.md) y lo prometido que mide la [revisión posterior](../Cierre/revision-posterior.md).

## La regla que ordena la evaluación

Damodaran la resume en tres pedidos: usar flujos de caja y no ganancias («You cannot spend earnings»), usar flujos incrementales, los que ocurren «as a consequence of the decision», y pesar más los que llegan antes. Las tres piezas de la vertical salen de ahí.

1. **El flujo de fondos del proyecto.** Qué plata entra y sale por hacerlo, contra no hacerlo. Es la parte donde más se equivoca la evaluación, y está en [flujo de fondos del proyecto](flujo-de-fondos-del-proyecto.md).
2. **La tasa con que se descuenta.** Lo que rendiría la plata en otro uso de riesgo parecido, o el mínimo que la empresa le pide a una inversión. Está en [tasa de corte](tasa-de-corte.md).
3. **El criterio que decide.** El [valor actual neto](valor-actual-neto.md) suma los flujos descontados; la [tasa interna de retorno](tasa-interna-de-retorno.md) busca la tasa que los deja en cero; el [periodo de repago](periodo-de-repago.md) cuenta cuántos años tarda en volver la plata.

Como el futuro no se conoce, la evaluación termina mirando cuánto tienen que fallar los supuestos para que la decisión cambie. Eso está en [análisis de sensibilidad](analisis-de-sensibilidad.md).

## Un mismo caso con los tres criterios

OpenStax usa un caso chico en todo su capítulo 16: una tienda de artículos deportivos evalúa una máquina de bordar de 16.000 dólares que deja 2.000 el primer año, 4.000 el segundo y 5.000 en cada uno de los cuatro siguientes, con un costo de la plata del 9 %.

| Criterio | Resultado | Lo que dice |
|---|---|---|
| Valor actual neto | 2.835,63 | La máquina deja más de lo que cuesta la plata; se compra |
| Tasa interna de retorno | 14,09 % | Rinde más que el 9 % que cuesta la plata |
| Índice de rentabilidad | 1,18 | Cada dólar invertido vuelve como 1,18 en valor actual |
| Repago simple | 4 años | La plata vuelve en el cuarto año, sin descontar |
| Repago descontado | 5,05 años | Descontando al 9 %, tarda un año más |

Las cuentas se rehicieron y cierran (el valor actual neto da 2.835,62 con redondeo). Acá los cinco criterios dicen que sí. Se separan cuando hay que elegir entre alternativas de distinto tamaño, cuando los flujos cambian de signo más de una vez o cuando el plazo de recupero manda; esos casos están en cada nota.

## Qué criterio usar

El valor actual neto es el que los libros recomiendan, porque mide en plata cuánto valor agrega la inversión y suma bien entre proyectos. La tasa interna de retorno da un porcentaje fácil de comparar, pero puede elegir mal entre alternativas excluyentes. El repago no mide valor, pero dice cuánto tiempo queda la plata inmovilizada.

En la práctica se usan juntos. En la encuesta de Graham y Harvey a 392 directores financieros, «74.9% of CFOs always or almost always used NPV and 75.7% always or almost always used IRR», y el repago fue el más usado después de esos dos (y de la tasa de corte, que la encuesta cuenta como técnica aparte), con 56,7 %. En la repetición de Graham (2022), el repago supera al valor actual neto en las empresas con ventas de menos de mil millones de dólares (66,40 % contra 40,22 %). Ese corte no equivale a pyme: es el que usa la encuesta.

> [!NOTE] Sin fuente todavía: una encuesta sobre qué criterios usan las pymes de América Latina o de la Argentina. Se buscó y no se encontró en esta investigación.

## Cómo se equivoca la evaluación

- **Mirar la ganancia contable en lugar de la plata.** La amortización baja la ganancia pero no saca plata; el [capital de trabajo](../../Tesoreria/Caja-y-liquidez/capital-de-trabajo.md) saca plata sin pasar por el resultado. Está en [flujo de fondos del proyecto](flujo-de-fondos-del-proyecto.md#de-la-ganancia-al-flujo).
- **Contar lo que ya se gastó.** Un estudio previo, una prueba de mercado, una obra a medias: no cambian con la decisión y no entran. Está en [flujo de fondos del proyecto](flujo-de-fondos-del-proyecto.md#lo-que-no-entra-el-costo-hundido).
- **Mezclar pesos de hoy con pesos de mañana.** Flujos nominales con una tasa real, o al revés, dan cualquier cosa. En un país con inflación es el error más caro; está en [flujo de fondos del proyecto](flujo-de-fondos-del-proyecto.md#pesos-de-hoy-o-pesos-de-cada-año) y en [proyectos de inversión en Argentina](../proyectos-de-inversion-en-argentina.md).
- **Creerle al pronóstico.** Quien propone quiere que se apruebe. La evidencia sobre cuánto se inflan los números está en [aprobación](../Aprobacion/aprobacion-de-la-inversion.md#por-qué-los-números-llegan-inflados).

## Lo que hay adentro de la evaluación

- [Flujo de fondos del proyecto](flujo-de-fondos-del-proyecto.md): los flujos incrementales, la inversión, el capital de trabajo, el valor residual, los impuestos y el ahorro fiscal de la amortización, el costo hundido y el costo de oportunidad.
- [Valor actual neto](valor-actual-neto.md): descontar, sumar y decidir; el índice de rentabilidad y cómo se elige entre alternativas.
- [Tasa interna de retorno](tasa-interna-de-retorno.md): la tasa que anula el valor actual neto, cuándo engaña y la tasa interna de retorno modificada.
- [Periodo de repago](periodo-de-repago.md): en cuánto se recupera, simple y descontado, qué ignora y por qué se usa igual.
- [Tasa de corte](tasa-de-corte.md): el costo de oportunidad del capital, el costo de capital y por qué las empresas piden más.
- [Análisis de sensibilidad](analisis-de-sensibilidad.md): sensibilidad, escenarios, punto de equilibrio, simulación y el valor de poder esperar o abandonar.
