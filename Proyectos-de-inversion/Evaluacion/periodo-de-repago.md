---
resumen: >-
  El periodo de repago es el tiempo que tarda una inversión en devolver, con sus flujos, la plata que se puso; el repago descontado hace la misma cuenta con los flujos traídos a hoy. No mide cuánto valor agrega y no mira lo que llega después, pero es el criterio que más usan las empresas chicas, y hay razones para eso.
estado: borrador
estabilidad: estable
fuentes:
  - "OpenStax, Principles of Finance (2022), 16.1 Payback Period Method (leído por extractor): https://openstax.org/books/principles-finance/pages/16-1-payback-period-method"
  - "OpenStax, Principles of Finance (2022), 16.4 Alternative Methods, sobre el repago descontado (leído por extractor): https://openstax.org/books/principles-finance/pages/16-4-alternative-methods"
  - "Graham y Harvey (2002), How do CFOs make capital budgeting and capital structure decisions?, Journal of Applied Corporate Finance 15(1), con la nota 7 (leído): https://people.duke.edu/~charvey/Research/Published_Papers/P76_How_do_CFOs.pdf"
  - "Graham (2022), Presidential Address: Corporate Finance and Reality, versión NBER w29841, sección II y Tabla I (leído en esa parte): https://nber.org/system/files/working_papers/w29841/w29841.pdf"
  - "Boyle y Guthrie (2006), Payback without apology, Accounting and Finance 46(1), 1-10 (solo el resumen): https://ideas.repec.org/a/bla/acctfi/v46y2006i1p1-10.html"
  - "Proyectos-de-inversion/.investigacion/evaluacion.md y posicion-contraria-y-fundamentos.md (2026-11-27)"
aliases: [repago, periodo de repago, período de recupero, plazo de recuperación, payback, payback period, repago descontado, discounted payback, recupero de la inversión]
creado: 2026-11-27
revisado:
---

# Periodo de repago

El periodo de repago es el tiempo que tarda una inversión en devolver, con sus flujos, la plata que se puso; el repago descontado hace la misma cuenta con los flujos traídos a hoy. No mide cuánto valor agrega y no mira lo que llega después, pero es el criterio que más usan las empresas chicas, y hay razones para eso.

Es la pregunta que hace un directorio antes que ninguna otra: «¿en cuánto se recupera?». En la [evaluación](evaluacion-de-la-inversion.md) va al lado del [valor actual neto](valor-actual-neto.md), que dice cuánto agrega, y de la [tasa interna de retorno](tasa-interna-de-retorno.md), que dice cuánto rinde.

## Cómo se calcula

Se suman los flujos año por año hasta que el acumulado cubre la inversión. OpenStax lo define como «how long it will take for a company to make enough free cash flow from the investment to recover the initial cost». Con la máquina de bordar de 16.000 dólares:

| Año | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Flujo | −16.000 | 2.000 | 4.000 | 5.000 | 5.000 | 5.000 |
| Saldo acumulado | −16.000 | −14.000 | −10.000 | −5.000 | 0 | 5.000 |

«Thus, the payback period for the embroidery machine is four years.» Si el saldo se cruza a mitad de un año, se suele interpolar: lo que falta dividido por el flujo de ese año.

El repago descontado hace lo mismo con los flujos descontados a la tasa de corte. Al 9 %, a la máquina le faltan 145,72 al final del quinto año y el sexto trae 2.981,34 de hoy: 5 + 145,72 / 2.981,34 = 5,05 años. Descontar alarga el repago, porque los flujos lejanos valen menos.

## Lo que el repago no ve

OpenStax enumera cuatro defectos.

- **No descuenta.** El repago simple «ignores the time value of money»: un peso del año 1 y uno del año 5 valen lo mismo. El repago descontado lo corrige.
- **No tiene una vara objetiva.** No hay «a clearly defined acceptance or rejection criterion»: un tope de cuatro años es una decisión de la empresa, sin base financiera.
- **No mira lo que llega después.** «Cash flows after the payback period are ignored.» Dos proyectos que se recuperan en cinco años parecen iguales aunque uno siga dando plata diez años más y el otro se termine ahí.
- **No ajusta por riesgo.** Un flujo seguro y uno dudoso cuentan igual.

La consecuencia es que el repago puede rechazar inversiones de largo plazo que agregan valor, y aprobar inversiones que se pagan rápido y no dejan nada después.

## Por qué se usa igual

Según Graham y Harvey, el repago fue el criterio más usado después del VAN y la TIR (la encuesta cuenta también la tasa de corte como técnica aparte), con 56,7 % de directores financieros que lo usaban siempre o casi siempre, y lo llaman sorprendente porque los libros marcan sus defectos «for decades». Las empresas chicas lo usaban «almost as frequently as they used NPV or IRR», y entre ellas lo usaban más los directores generales de más edad, con más años en el cargo y sin posgrado en administración. En la repetición de 2022, entre las empresas de menos de mil millones de dólares de ventas, el repago (66,40 %) supera con holgura al VAN (40,22 %).

Para eso hay tres explicaciones, y no se excluyen:

> [!IMPORTANT]
> **Si el repago es un error o una respuesta razonable está en disputa.**
> - **Liquidez.** Graham y Harvey proponen que puede ser útil «for severely capital-constrained firms»: si el proyecto no devuelve plata pronto, la empresa puede quebrar antes de cobrar el resto. Pero en su misma nota 7 dicen que «we find no direct evidence that companies are more likely to use payback when they are capital-constrained or financially distressed».
> - **Incertidumbre.** Boyle y Guthrie sostienen, según su resumen, que con tasas de interés inciertas una inversión irreversible que se recupera despacio tiene que superar una vara más alta que una que se recupera rápido, y que el repago puede ser «an intuitive response to correctly perceived costs and benefits». Graham y Harvey citan a McDonald, para quien las reglas toscas como el repago «often resemble the solutions produced by optimal decision rules» cuando la inversión tiene opciones. El artículo de Boyle y Guthrie se leyó solo en su resumen.
> - **Simplicidad y falta de formación.** Graham (2022) recoge, de las respuestas abiertas, «liquidity needs, a lack of sophistication, and a preference for simple decision-making».

La lectura de esta base es práctica: el repago dice cuánto tiempo queda la plata inmovilizada y cuánto tiempo hay para que el pronóstico falle, que es información que el VAN no muestra. Usado al lado del VAN, como tope de riesgo, sirve. Usado solo, deja afuera lo que más valor puede agregar.

## Qué guardar en un sistema

Si un sistema de gestión calcula el repago, conviene que guarde el flujo año por año y no solo el resultado, y que muestre el simple y el descontado juntos. Es una inferencia de esta base: con el flujo guardado, la [revisión posterior](../Cierre/revision-posterior.md) puede comparar el repago prometido con el real.
