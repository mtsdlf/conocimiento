---
resumen: >-
  Lo que cruza todo el tema de proyectos de inversión: cómo se divide el campo, las tradiciones que lo estudian (las finanzas corporativas, la contabilidad de gestión y la ingeniería económica), dónde la práctica de las empresas se aparta del libro, los errores más comunes y qué leer para cada parte.
estado: borrador
estabilidad: estable
fuentes:
  - "OpenStax, Principles of Finance (2022), cap. 16, esquema del capítulo (leído): https://openstax.org/books/principles-finance/pages/16-why-it-matters"
  - "OpenStax, Principles of Managerial Accounting (2019), 11.1 (leído): https://openstax.org/books/principles-managerial-accounting/pages/11-1-describe-capital-investment-decisions-and-how-they-are-applied"
  - "OpenStax, Principles of Managerial Accounting (2019), 11.4 (leído por extractor): https://openstax.org/books/principles-managerial-accounting/pages/11-4-use-discounted-cash-flow-models-to-make-capital-investment-decisions"
  - "APQC, Process Classification Framework 7.4 (agosto de 2024), 9.4 y 10.1 a 10.2 (leído): https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "GAO, Executive Guide: Leading Practices in Capital Decision-Making, GAO/AIMD-99-32 (diciembre de 1998) (leído en partes): https://www.gao.gov/assets/aimd-99-32.pdf"
  - "Damodaran, Applied Corporate Finance, 4.ª ed., presentaciones de los caps. 4 a 6 (leído): https://pages.stern.nyu.edu/~adamodar/New_Home_Page/ACF4E/appldCF4E.htm"
  - "Graham (2022), Presidential Address: Corporate Finance and Reality, versión NBER w29841 (leído en la sección de presupuesto de capital): https://nber.org/system/files/working_papers/w29841/w29841.pdf"
  - "Huikku (2009), Post-Completion Auditing of Capital Investments and Organizational Learning, tesis doctoral (leído en introducción y resumen): https://epub.lib.aalto.fi/pdf/diss/a347.pdf"
  - "Proyectos-de-inversion/.investigacion/posicion-contraria-y-fundamentos.md (2026-11-27)"
aliases: [fundamentos de proyectos de inversión, fundamentos del presupuesto de capital, capital budgeting foundations, escuelas de evaluación de proyectos, mitos de la evaluación de proyectos, bibliografía de proyectos de inversión]
creado: 2026-11-27
revisado:
---

# Fundamentos de proyectos de inversión

Lo que cruza todo el tema de proyectos de inversión: cómo se divide el campo, las tradiciones que lo estudian (las finanzas corporativas, la contabilidad de gestión y la ingeniería económica), dónde la práctica de las empresas se aparta del libro, los errores más comunes y qué leer para cada parte.

No es una etapa más: reúne lo que hace falta para leer las cuatro etapas de la [entrada del tema](../proyectos-de-inversion.md). Los términos están en el [glosario](glosario-de-proyectos-de-inversion.md).

## Cómo se divide el campo

Cada fuente corta el campo según lo que le interesa:

| Fuente | Qué cubre | Qué deja afuera |
|---|---|---|
| OpenStax, *Principles of Finance*, cap. 16 | Los criterios: repago, VAN, TIR, métodos alternativos, elegir entre proyectos | Cómo se arma el flujo, cómo se aprueba y cómo se sigue |
| OpenStax, *Principles of Managerial Accounting*, cap. 11 | Los pasos de la decisión, con la decisión que descarta y la que ordena (11.1) | La amortización y los impuestos en el flujo, que en 11.4 deja para cursos avanzados |
| APQC 9.4 y 10.1 a 10.2 | Los procesos: planificar y aprobar, contabilizar el proyecto, cerrarlo y medir el retorno; diseñar y construir | El cálculo |
| GAO, guía de decisiones de capital | Doce prácticas en cinco principios: atar la inversión a los objetivos, evaluar y elegir «using an investment approach», equilibrar el control del presupuesto con la flexibilidad, gestionar el proyecto y evaluar los resultados para aprender | El cálculo detallado |

El árbol de esta base sigue el orden de APQC y de la GAO (evaluar, aprobar, ejecutar, cerrar) y mete los criterios de OpenStax en la evaluación. Por qué está cortado así está en el [alcance](../ALCANCE.md).

## Tres tradiciones que se tocan poco

- **Las finanzas corporativas.** Estudian qué inversión agrega valor, con el flujo de fondos descontado: la regla del VAN, el costo de capital, el riesgo. Es la tradición de OpenStax y de Damodaran, y la que domina las notas de [evaluación](../Evaluacion/evaluacion-de-la-inversion.md).
- **La contabilidad de gestión.** Estudia cómo se controla el gasto de capital dentro de la organización: la aprobación, el seguimiento y la revisión posterior. La tesis de Huikku, base de la [revisión posterior](../Cierre/revision-posterior.md), es de esta tradición.
- **La ingeniería económica.** Compara alternativas técnicas con costos a lo largo de la vida del activo: el costo del ciclo de vida y el costo anual equivalente. En esta base aparece en [reparar o reemplazar](../../Activos-y-mantenimiento/Desempeno-de-los-activos/reparar-o-reemplazar.md), con el manual del NIST.

Las tres llegan a las mismas cuentas por caminos distintos. La gestión de proyectos aporta una cuarta mirada, sobre cómo se lleva la obra, que está en [Gestión de proyectos](../../Gestion-de-proyectos/gestion-de-proyectos.md). Queda afuera la evaluación social de proyectos, la que hace el Estado con precios sociales.

> [!NOTE] Sin fuente todavía: la historia del presupuesto de capital (Fisher, 1930; Dean, 1951; Lorie y Savage, 1955; Hirshleifer, 1958). Los textos no se consiguieron en esta investigación y no se afirma nada sobre ellos.

## Dónde la práctica se aparta del libro

Las encuestas de Graham y Harvey (2001) y de Graham (2022) son la fuente más usada para saber qué hacen las empresas. Muestran tres distancias con los libros, cada una con su nota:

- **El repago se usa más de lo que el libro aconseja**, sobre todo en las empresas chicas: [periodo de repago](../Evaluacion/periodo-de-repago.md#por-qué-se-usa-igual).
- **Las tasas de corte están unos seis puntos por encima del costo de capital** y casi no se mueven: [tasa de corte](../Evaluacion/tasa-de-corte.md#las-empresas-piden-más-que-su-costo-de-capital).
- **Muchas empresas usan una sola tasa para todos los proyectos**, aunque tengan riesgos distintos: [tasa de corte](../Evaluacion/tasa-de-corte.md#cómo-se-estima-en-la-práctica).

Graham propone leer estas distancias como reglas simples y conservadoras que responden a límites reales (de plata, de tiempo, de gente, de confianza en el pronóstico), y no solo como errores. Cuánto de cada cosa es error y cuánto es respuesta razonable sigue en discusión.

## Errores comunes

| Se cree | Lo que pasa | Dónde se explica |
|---|---|---|
| La amortización es plata que sale | Es un reparto contable de una salida que ya pasó; solo cuenta su efecto en los impuestos | [Flujo de fondos del proyecto](../Evaluacion/flujo-de-fondos-del-proyecto.md#de-la-ganancia-al-flujo), [activos fijos y amortización](../../Contabilidad/Operaciones/activos-fijos-y-amortizacion.md#la-amortización-no-aparta-plata) |
| Lo que ya se gastó tiene que recuperarse | Un costo hundido no cambia con la decisión y no entra | [Flujo de fondos del proyecto](../Evaluacion/flujo-de-fondos-del-proyecto.md#lo-que-no-entra-el-costo-hundido) |
| Lo que la empresa ya tiene es gratis para el proyecto | Cuesta lo que rendiría en su mejor otro uso | [Flujo de fondos del proyecto](../Evaluacion/flujo-de-fondos-del-proyecto.md#lo-que-sí-entra-aunque-no-sea-un-pago-el-costo-de-oportunidad) |
| Los intereses del préstamo van en el flujo | Si se descuenta con el costo de capital, ya están en la tasa; ponerlos en el flujo los cuenta dos veces | [Flujo de fondos del proyecto](../Evaluacion/flujo-de-fondos-del-proyecto.md#el-financiamiento-va-en-la-tasa-no-en-el-flujo) |
| La TIR es lo que rinde el proyecto y elige igual que el VAN | Puede tener dos soluciones, ignora el tamaño y supone reinvertir a la misma tasa | [Tasa interna de retorno](../Evaluacion/tasa-interna-de-retorno.md#cuándo-la-tir-elige-mal) |
| Con inflación, cualquier tasa sirve si se hace la cuenta | Flujo nominal con tasa real, o al revés, da cualquier cosa | [Proyectos de inversión en Argentina](../proyectos-de-inversion-en-argentina.md#pesos-de-cada-año-pesos-de-hoy-o-dólares) |
| La obra empieza a amortizarse cuando se termina de pagar | Empieza cuando está disponible para usar | [Activación de la obra](../Cierre/activacion-de-la-obra.md#lista-para-usar-no-terminada-de-pagar-ni-usada-por-primera-vez) |

Las fuentes de cada fila están en su nota; esta tabla no agrega afirmaciones. Que estos errores sean «comunes» es una lectura de esta base, salvo el del costo hundido, que Damodaran describe como un hallazgo de la investigación del comportamiento.

## Qué leer para cada parte

- **Para los criterios**: OpenStax, *Principles of Finance*, capítulo 16, de acceso abierto. Leé 16.2 y 16.5; fijate en el caso en que la máquina más cara tiene menos TIR y más VAN.
- **Para el flujo de fondos**: las presentaciones de Damodaran de los capítulos 5 y 6 de *Applied Corporate Finance*, en su sitio. Fijate en los tres pasos de la ganancia al flujo, el capital de trabajo que sale y vuelve, y la regla de los costos hundidos.
- **Para la tasa de corte y la práctica**: Graham (2022), sección II, con su Tabla I y su Figura 3.
- **Para la aprobación y el seguimiento**: la guía GAO/AIMD-99-32, prácticas 4, 5, 9 y 11, con sus casos de empresas y gobiernos.
- **Para la activación**: la NIC 16, párrafos 16 a 22 y 55, y la NIC 23, párrafos 17 a 25, en el sitio de la IFRS Foundation.
- **Para la revisión posterior**: la tesis de Huikku (2009), de acceso abierto, en su introducción, que resume la literatura.
