---
resumen: >-
  El presupuesto de capital es el plan de inversiones de la empresa para un período, normalmente un año: qué proyectos entran, por cuánto y en qué orden, con el total que la empresa está dispuesta a poner. Cuando las propuestas buenas piden más plata que la disponible, se ordenan por lo que dejan por cada peso invertido y no por su valor actual neto solo.
estado: vigente
estabilidad: estable
fuentes:
  - "OpenStax, Principles of Finance (2022), 16.4 y 16.5, índice de rentabilidad y racionamiento de capital (leído por extractor): https://openstax.org/books/principles-finance/pages/16-5-choosing-between-projects"
  - "OpenStax, Principles of Managerial Accounting (2019), 11.1 (leído): https://openstax.org/books/principles-managerial-accounting/pages/11-1-describe-capital-investment-decisions-and-how-they-are-applied"
  - "GAO, Executive Guide: Leading Practices in Capital Decision-Making, GAO/AIMD-99-32 (diciembre de 1998), práctica 5 (leído): https://www.gao.gov/assets/aimd-99-32.pdf"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 9.4.1.2 (leído): https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Jagannathan, Matsa, Meier y Tarhan (2016), Why do firms use high discount rates?, Journal of Financial Economics 120(3), 445-463 (solo el resumen): https://ideas.repec.org/a/eee/jfinec/v120y2016i3p445-463.html"
  - "Temple University, Policy 04.32.01 Approval of Capital Expenditures (enero de 2026), como ejemplo de práctica (leído): https://secretary.temple.edu/sites/secretary/files/policies/04.32.01.pdf"
  - "University of Chicago, Policy 1301, Project Planning, Approvals and Controls, como ejemplo de práctica (leído en fragmentos): https://policies.uchicago.edu/2017/06/20/policy-1301-project-planning-approvals-and-contorls"
  - "Proyectos-de-inversion/.investigacion/aprobacion-y-ejecucion.md (2026-11-27), componente 2"
aliases: [presupuesto de capital, capital budget, plan de inversiones, plan anual de inversiones, capex plan, presupuesto de inversiones, racionamiento de capital, capital rationing, índice de rentabilidad, profitability index]
creado: 2026-11-27
revisado: 2026-11-27
---

# Presupuesto de capital

El presupuesto de capital es el plan de inversiones de la empresa para un período, normalmente un año: qué proyectos entran, por cuánto y en qué orden, con el total que la empresa está dispuesta a poner. Cuando las propuestas buenas piden más plata que la disponible, se ordenan por lo que dejan por cada peso invertido y no por su valor actual neto solo.

Es el centro de la [aprobación](aprobacion-de-la-inversion.md): junta las propuestas evaluadas y fija el monto de cada una, que después se autoriza con la [solicitud de inversión](solicitud-de-inversion.md). APQC lo nombra en 9.4.1.2 «Develop and approve capital expenditure plans and budgets». En inglés «capital budgeting» nombra a veces todo el tema (evaluar, elegir, controlar) y a veces solo este plan; acá se usa en el segundo sentido.

## El plan de capital al lado del presupuesto operativo

El presupuesto operativo planea lo que se gasta para mantener andando la empresa en el año; el de capital, lo que se pone en activos que duran más. OpenStax separa los dos gastos: «An operating expense is a regularly-occurring expense used to maintain the current operations of the company». El presupuesto maestro de la empresa, con su mitad operativa y su mitad financiera, está en [presupuesto](../../Contabilidad/Contabilidad-de-gestion/presupuesto.md); el de capital alimenta a la mitad financiera (los activos del balance proyectado) y a la proyección de caja, porque cada inversión es una salida de plata con fecha.

Los dos se tocan por tres lados, según una lectura de esta base:

- **La amortización.** Cada inversión que entra suma amortización al presupuesto operativo de los años siguientes.
- **Los costos de operar lo nuevo.** Una máquina trae mantenimiento, energía y gente; si el presupuesto operativo no los incluye, el proyecto arranca en desvío.
- **La caja.** El total del plan y sus fechas van a la [proyección de caja](../../Tesoreria/Caja-y-liquidez/proyeccion-de-caja.md), y si no alcanza, al [financiamiento](../../Tesoreria/Financiamiento/financiamiento.md).

## Cuando la plata no alcanza

La GAO lo da como normal: las organizaciones ordenan proyectos «because the number of requested projects exceeds available funding». OpenStax trata esa situación, que en finanzas se llama racionamiento de capital, en su sección 16.5: los gerentes enfrentan «a budget that restricts the amount of capital that they may invest», y el objetivo es «to maximize the total NPV of the firm's projects while remaining within budget constraints».

Para eso no sirve ordenar por VAN de mayor a menor. OpenStax lo muestra con una fábrica que tiene 200 millones para invertir y siete proyectos con VAN positivo que piden 430 millones:

| Proyecto | Inversión | VAN | Índice de rentabilidad | ¿Entra? |
|---|---|---|---|---|
| A | 150 | 60 | 1,40 | Sí |
| E | 30 | 11 | 1,37 | Sí |
| F | 20 | 7 | 1,35 | Sí |
| D | 50 | 15 | 1,30 | No |
| B | 100 | 25 | 1,25 | No |
| G | 10 | 2 | 1,20 | No |
| C | 70 | 10 | 1,14 | No |

Ordenados por el índice de rentabilidad (el valor actual de lo que entra sobre lo que se invierte, explicado en [valor actual neto](../Evaluacion/valor-actual-neto.md#el-índice-de-rentabilidad)), entran A, E y F, que usan los 200 millones y suman 78 millones de VAN. Por VAN solo, después de A (60) vendría B (25), que no entra en lo que queda; con A y D se llega a 75. E y F juntos dejan 18 por los mismos 50 millones con que D deja 15. La cuenta de la alternativa por VAN es de esta base.

El índice ordena bien cuando los proyectos se pueden sumar sin que uno dependa del otro y la restricción es un solo monto. Si hay proyectos excluyentes, dependencias o límites en varios años, el orden por índice ya no garantiza el mejor conjunto (lectura de esta base; OpenStax no lo trata).

> [!NOTE] Sin fuente todavía: la distinción entre racionamiento duro (la empresa no consigue más plata) y blando (la dirección se pone un tope a sí misma) en una fuente leída.

## Plata, gente y proyectos fuera de ciclo

El tope de plata no es el único. Según Jagannathan y coautores, muchas empresas con caja de sobra se racionan por la gente que tiene que llevar los proyectos, y lo hacen subiendo la [tasa de corte](../Evaluacion/tasa-de-corte.md#las-empresas-piden-más-que-su-costo-de-capital). Cuántos proyectos puede llevar una organización a la vez y por qué cargarla al máximo demora todo está en [portafolio](../../Gestion-de-proyectos/Gobierno-y-cierre/portafolio.md).

Un plan anual deja afuera lo que aparece en el medio del año: un equipo que se rompe, una oportunidad. Dos políticas de universidades sirven como ejemplo de práctica. La de Chicago incluye en el presupuesto de capital aprobado por su directorio una reserva para proyectos fuera de ciclo («Off-Cycle Contingency Allowance»). La de Temple pide, antes de cada ejercicio, una solicitud por el total del mantenimiento esencial con un monto que no se puede superar («not to exceed») e informes periódicos al directorio.

## Cómo falla

- **El plan como techo que hay que gastar.** Si lo que no se gasta se pierde el año siguiente, las áreas gastan para no perderlo. Es un riesgo general de los presupuestos, que se discute en [presupuesto](../../Contabilidad/Contabilidad-de-gestion/presupuesto.md#cómo-el-presupuesto-se-vuelve-un-contrato-que-se-negocia).
- **Todo por igual.** Si las obligatorias, los reemplazos y las apuestas nuevas compiten en una sola lista, las obligatorias desplazan sin discusión y las apuestas nuevas se comparan con reemplazos de riesgo bajo. Es la razón de [clasificar las propuestas](aprobacion-de-la-inversion.md#no-todas-las-propuestas-piden-lo-mismo).
- **Real lejos de lo presupuestado.** APQC tiene una medida para eso, el gasto de capital real del año sobre el presupuestado (medida 100009, citada en [de la compra a la baja del activo](../../Procesos-de-negocio/de-la-compra-a-la-baja-del-activo.md#qué-se-mide-del-recorrido-entero)); sin valores de referencia.
