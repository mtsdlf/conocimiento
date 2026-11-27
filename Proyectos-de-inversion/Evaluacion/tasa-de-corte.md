---
resumen: >-
  La tasa de corte es el rendimiento mínimo que una empresa le pide a una inversión para aceptarla, y la que usa para descontar su flujo de fondos. En teoría es el costo de oportunidad del capital, lo que rendiría esa plata en otro uso de riesgo parecido; en la práctica, las empresas usan tasas varios puntos más altas que su costo de capital, y por qué lo hacen está en discusión.
estado: vigente
estabilidad: semi
fuentes:
  - "OpenStax, Principles of Finance (2022), 16.2 y 16.3 (leído por extractor): https://openstax.org/books/principles-finance/pages/16-2-net-present-value-npv-method"
  - "Damodaran, Applied Corporate Finance, 4.ª ed., presentaciones del cap. 4 «Risk Measurement and Hurdle Rates» (leído en las partes de costo de capital y tasa de corte): https://pages.stern.nyu.edu/~adamodar/pdfiles/acf4E/presentations/hurdlerate.pdf"
  - "Graham y Harvey (2002), Journal of Applied Corporate Finance 15(1) (leído): https://people.duke.edu/~charvey/Research/Published_Papers/P76_How_do_CFOs.pdf"
  - "Graham (2022), Presidential Address: Corporate Finance and Reality, versión NBER w29841, sección II.B y Figura 3 (leído en esa parte): https://nber.org/system/files/working_papers/w29841/w29841.pdf"
  - "Jagannathan, Matsa, Meier y Tarhan (2016), Why do firms use high discount rates?, Journal of Financial Economics 120(3), 445-463 (solo el resumen): https://ideas.repec.org/a/eee/jfinec/v120y2016i3p445-463.html"
  - "Jagannathan, Meier y Tarhan (2011), The cross-section of hurdle rates for capital budgeting, NBER WP 16770, sin revisión por pares (leído en resumen e introducción): https://www.nber.org/papers/w16770.pdf"
  - "Proyectos-de-inversion/.investigacion/evaluacion.md y posicion-contraria-y-fundamentos.md (2026-11-27)"
aliases: [tasa de corte, hurdle rate, tasa de descuento, discount rate, tasa mínima atractiva de rendimiento, TREMA, MARR, minimum acceptable rate of return, rendimiento requerido, required rate of return, costo de capital, cost of capital, WACC, costo promedio ponderado del capital, costo de oportunidad del capital, opportunity cost of capital, prima por riesgo]
creado: 2026-11-27
revisado: 2026-11-27
---

# Tasa de corte

La tasa de corte es el rendimiento mínimo que una empresa le pide a una inversión para aceptarla, y la que usa para descontar su flujo de fondos. En teoría es el costo de oportunidad del capital, lo que rendiría esa plata en otro uso de riesgo parecido; en la práctica, las empresas usan tasas varios puntos más altas que su costo de capital, y por qué lo hacen está en discusión.

Es la segunda pieza de la [evaluación](evaluacion-de-la-inversion.md): el [valor actual neto](valor-actual-neto.md) descuenta con ella y la [tasa interna de retorno](tasa-interna-de-retorno.md) se compara contra ella. Un mismo [flujo de fondos](flujo-de-fondos-del-proyecto.md) puede dar un VAN positivo al 9 % y negativo al 15 %, así que elegir la tasa es casi tan importante como estimar el flujo.

## Lo que rendiría la plata en otro lado

La plata que se pone en una máquina deja de estar disponible para otra cosa: pagar deuda, repartir a los socios, colocarla o hacer otro proyecto. Lo que rendiría en el mejor de esos usos, con un riesgo parecido, es el costo de oportunidad del capital. Una inversión tiene que rendir al menos eso para que valga la pena.

OpenStax dice que se debería descontar con «the firm's cost to attract capital». Damodaran lo describe como «a composite cost to the firm of raising financing to fund its projects»: la empresa se financia con deuda y con capital de los socios, y su costo de capital es el promedio ponderado de los dos (en inglés, WACC). El costo de la deuda se puede leer en lo que cobra el banco; está en [costo del financiamiento](../../Tesoreria/Financiamiento/costo-del-financiamiento.md). El costo del capital propio no se lee en ningún lado: es lo que los socios esperan ganar por el riesgo que corren, y se estima.

Damodaran fija qué tasa va con qué flujo: si el flujo es para los accionistas, después de la deuda, la tasa es el costo del capital propio; si es para toda la empresa, la tasa es el costo de capital. La segunda es la que usa el ejemplo de [flujo de fondos del proyecto](flujo-de-fondos-del-proyecto.md#el-financiamiento-va-en-la-tasa-no-en-el-flujo).

## Cómo se estima en la práctica

Según Graham y Harvey, el 73,5 % de los directores financieros estimaba el costo del capital propio con el modelo CAPM, que suma a la tasa libre de riesgo (lo que rinde un bono del Estado en la misma moneda) una prima según cuánto se mueve la acción con el mercado. Cerca del 60 % usaba «a single company-wide discount rate to evaluate a new investment project, even though different projects are likely to have different risk characteristics»; a la vez, el 51 % decía usar siempre o casi siempre una tasa ajustada al riesgo del proyecto.

Usar una sola tasa para todo tiene un costo. Una ampliación de lo que la empresa ya sabe hacer y un producto nuevo en un mercado nuevo no tienen el mismo riesgo; con la misma tasa, el segundo parece mejor de lo que es y el primero peor. Es una lectura de esta base sobre la observación de Graham y Harvey.

Una pyme que no cotiza no tiene una acción con la que estimar el CAPM. Lo habitual es partir de lo que la plata de los socios podría rendir en otro lado y sumarle una prima por el riesgo del negocio y del proyecto (inferencia de esta base, sin una fuente con método). En un país con inflación, la tasa tiene que estar en la misma moneda y la misma unidad que el flujo: [proyectos de inversión en Argentina](../proyectos-de-inversion-en-argentina.md).

> [!NOTE] Sin fuente todavía: un método con fuente para estimar la tasa de corte de una empresa que no cotiza, y la tasa mínima atractiva de rendimiento (TREMA) como la define la ingeniería económica.

## Las empresas piden más que su costo de capital

Graham (2022) resume veinte años de encuestas: «hurdle rates on average have built in a 6% 'buffer' above the cost of capital». En la encuesta de 2022, la tasa de corte promedio era 15 % y el costo de capital promedio 9 %. El margen podría ser mayor: según una encuesta de 2017 que cita, «only 1-in-5 companies say they accept all projects whose expected return exceeds the stated hurdle rate». Las tasas además casi no se mueven: cerca del 60 % de las empresas norteamericanas cambió su tasa de corte una vez o ninguna en diez años.

Jagannathan, Matsa, Meier y Tarhan encuentran lo mismo con otro método: tasas que «average twice the firms' cost of financial capital». Poterba y Summers ya habían documentado, según los cita el documento de trabajo de 2011 de Jagannathan, Meier y Tarhan, «an average real hurdle rate of 12.2%» cuando la inflación esperada era de alrededor de 5 %.

La consecuencia, en palabras de Graham: «standard textbook logic is that setting a hurdle rate higher than the cost of capital may cause firms to pass up value-creating projects».

> [!IMPORTANT]
> **Por qué las empresas usan tasas altas está en disputa, y cada explicación cambia si es un error.**
> - **Restricciones operativas.** Jagannathan y coautores (2016) encuentran evidencia «consistent with operational constraints»: las empresas con tasas altas tienen balances fuertes, poca deuda y mucha caja, y parecen reservar la capacidad de su gente para mejores oportunidades. Si la escasa es la gente y no la plata, una tasa alta raciona lo que de verdad falta. Se leyó solo el resumen.
> - **El valor de esperar.** En la versión de trabajo de 2011, los mismos autores explicaban la diferencia por la opción de postergar la inversión: el costo de capital real era «about half of the value of the hurdle rate». Es otra explicación, en un trabajo sin revisión por pares.
> - **Desconfianza del pronóstico.** Graham propone que el margen es conservador si las empresas subestiman lo que puede salir mal, y que evita tener que dar marcha atrás. Si los flujos de las propuestas vienen inflados, como se ve en [aprobación](../Aprobacion/aprobacion-de-la-inversion.md#por-qué-los-números-llegan-inflados), subir la tasa es una corrección tosca.
> - **Error.** La lectura de los libros: se pierden proyectos que convenían.

La lectura de esta base: subir la tasa mezcla en un solo número el costo de la plata, el riesgo del proyecto y la desconfianza en quien lo propone. Es más claro descontar al costo de capital ajustado por el riesgo del proyecto y tratar las otras dos cosas por separado, con el [análisis de sensibilidad](analisis-de-sensibilidad.md) y la [revisión posterior](../Cierre/revision-posterior.md). Si la empresa usa una tasa alta igual, conviene que sepa cuánto de esa tasa es costo de la plata y cuánto es colchón.
