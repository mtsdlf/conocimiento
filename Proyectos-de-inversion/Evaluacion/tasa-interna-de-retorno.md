---
resumen: >-
  La tasa interna de retorno (TIR) es la tasa de descuento con la que el valor actual neto de una inversión da cero; si es mayor que la tasa de corte, la inversión se acepta. Da un porcentaje fácil de comparar, pero puede tener más de una solución, ignora el tamaño del proyecto y puede elegir mal entre alternativas excluyentes.
estado: vigente
estabilidad: estable
fuentes:
  - "OpenStax, Principles of Finance (2022), 16.3 Internal Rate of Return (IRR) Method (leído por extractor): https://openstax.org/books/principles-finance/pages/16-3-internal-rate-of-return-irr-method"
  - "OpenStax, Principles of Finance (2022), 16.4 Alternative Methods, sobre la TIR modificada (leído por extractor): https://openstax.org/books/principles-finance/pages/16-4-alternative-methods"
  - "OpenStax, Principles of Finance (2022), 16.5 Choosing between Projects (leído por extractor): https://openstax.org/books/principles-finance/pages/16-5-choosing-between-projects"
  - "Graham y Harvey (2002), Journal of Applied Corporate Finance 15(1) (leído): https://people.duke.edu/~charvey/Research/Published_Papers/P76_How_do_CFOs.pdf"
  - "Proyectos-de-inversion/.investigacion/evaluacion.md (2026-11-27), componente 3"
aliases: [TIR, tasa interna de retorno, tasa interna de rendimiento, internal rate of return, IRR, TIR modificada, TIRM, modified internal rate of return, MIRR, TIR múltiples, multiple IRR]
creado: 2026-11-27
revisado: 2026-11-27
---

# Tasa interna de retorno

La tasa interna de retorno (TIR) es la tasa de descuento con la que el valor actual neto de una inversión da cero; si es mayor que la tasa de corte, la inversión se acepta. Da un porcentaje fácil de comparar, pero puede tener más de una solución, ignora el tamaño del proyecto y puede elegir mal entre alternativas excluyentes.

Usa el mismo [flujo de fondos del proyecto](flujo-de-fondos-del-proyecto.md) que el [valor actual neto](valor-actual-neto.md), pero en lugar de fijar la tasa y calcular plata, busca la tasa. En la [evaluación](evaluacion-de-la-inversion.md) se la usa casi tanto como al VAN: en la encuesta de Graham y Harvey, el 75,7 % de los directores financieros la usaba siempre o casi siempre.

## La tasa que deja el VAN en cero

OpenStax la define como «the discount rate that sets the present value of the cash inflows» igual al de las salidas, con la regla: «If the IRR is greater than the cost of capital, a project should be accepted». Se calcula probando tasas hasta que el VAN da cero; una planilla o una calculadora financiera lo hacen solas.

Para la máquina de bordar del ejemplo (16.000 dólares de inversión, 2.000, 4.000 y cuatro años de 5.000), la TIR es 14,09 %. Como el costo de la plata es 9 %, se acepta, igual que con el VAN. En el gráfico del VAN según la tasa, la curva cruza el cero en ese punto; OpenStax: «The IRR is about, but not exactly, 14%». La cuenta se rehízo y da 14,09 %.

La TIR se lee como un rendimiento («la máquina rinde 14 %»), y por eso convence. Pero no es la rentabilidad contable de la máquina ni lo que va a ganar la empresa: es la tasa que iguala los flujos supuestos con la inversión.

## Cuándo la TIR elige mal

OpenStax da tres problemas.

- **Ignora el tamaño.** «The IRR converts the cash flows to percentages and ignores differences in the size or scale of projects.» En su caso, una máquina de 16.000 tiene TIR de 14,10 % y VAN de 2.835,62; otra de 25.000 tiene TIR de 13,20 % y VAN de 3.970,67. La TIR elige la chica; el VAN, la grande, que deja más plata. Con proyectos excluyentes manda el VAN.
- **Puede tener más de una solución.** Pasa «when negative cash flows occur in more than one period in the project»: una obra que pide plata al principio, deja plata en el medio y pide plata de nuevo al final para desmantelar. OpenStax da un caso de instalación olímpica con flujos de −350, +950 y −620 millones; el VAN es negativo a tasas bajas, positivo en el medio y negativo de nuevo a tasas altas. OpenStax no da las dos tasas; resolviendo la cuenta, esta base obtiene unas 9,2 % y 62,2 %. Con dos TIR, la regla de «mayor que la tasa de corte» no dice nada.
- **Supone que todo se reinvierte a la misma tasa.** «The IRR assumes that the cash flows are reinvested at the internal rate of return when they are received.» Un proyecto con TIR de 40 % supone que cada peso que devuelve se vuelve a poner al 40 %, lo que rara vez pasa.

## La TIR modificada

La TIR modificada corrige los dos últimos problemas. Lleva todas las entradas hasta el último año capitalizándolas a la tasa de corte, trae las salidas a hoy con la misma tasa y busca la tasa que iguala las dos puntas. Para la máquina de bordar, las entradas capitalizadas al 9 % suman 31.595,22 al año 6 (esta base obtiene unos 31.589 con redondeo distinto), y 16.000 = 31.595,22 / (1 + i)^6 da i = 12 %.

Según OpenStax, tiene una sola solución y evita el supuesto de reinversión, pero sigue sin ver el tamaño: sirve para aceptar o rechazar, no para ordenar proyectos de distinto monto.

## Cuándo sirve

Con un proyecto solo, con flujos que cambian de signo una vez (primero se pone, después se recibe), la TIR y el VAN dicen lo mismo. La TIR agrega un dato útil: cuánto margen hay entre lo que rinde el proyecto y la tasa de corte. Un proyecto con TIR de 14 % contra una tasa de corte de 9 % aguanta más errores que uno con TIR de 10 %. Es una lectura de esta base; la prueba completa de cuánto aguanta está en [análisis de sensibilidad](analisis-de-sensibilidad.md).
