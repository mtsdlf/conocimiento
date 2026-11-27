---
resumen: >-
  El balance es el estado que muestra, a una fecha, lo que la empresa controla (activo), lo que debe a terceros (pasivo) y lo que queda para sus dueños (patrimonio neto), separando lo corriente de lo no corriente.
estado: borrador
estabilidad: estable
fuentes:
  - "IFRS Foundation, NIC 1 Presentation of Financial Statements (página de la norma, según su resumen): https://www.ifrs.org/issued-standards/list-of-standards/ias-1-presentation-of-financial-statements/"
  - "KPMG, Current/non-current classification of liabilities (2024, según su resumen): https://kpmg.com/us/en/articles/2024/current-noncurrent-classification-liabilities-ias-amendments.html"
  - "BDO, IFRS in Practice: Classification of loans as current or non-current (junio de 2026, según su resumen): https://www.bdo.global/getmedia/b8866082-2b56-4ed8-9df2-600f56d20d1a/IFRS-IP_Classification-of-loans-as-current-or-non-current_June-2026.pdf?ext=.pdf"
  - "OpenStax, Principles of Financial Accounting (2019), 5.4 Appendix: Complete a Comprehensive Accounting Cycle for a Business: https://openstax.org/books/principles-financial-accounting/pages/5-4-appendix-complete-a-comprehensive-accounting-cycle-for-a-business"
  - "OpenStax, Principles of Financial Accounting (2019), 11.3 Explain and Apply Depreciation Methods: https://openstax.org/books/principles-financial-accounting/pages/11-3-explain-and-apply-depreciation-methods-to-allocate-capitalized-costs"
  - "Lev y Gu (2016), The End of Accounting and the Path Forward for Investors and Managers, Wiley (ficha del editor): https://www.stern.nyu.edu/experience-stern/faculty-research/baruch-lev-book-end-of-accounting"
  - "Fortune, reseña de The End of Accounting (22 de septiembre de 2016): https://fortune.com/2016/09/22/accounting-broken-baruch-lev/"
  - "CFA Institute, The End of Accounting? Not So Sure (1 de febrero de 2018, según su resumen): https://blogs.cfainstitute.org/blog/2018/02/01/the-end-of-accounting-not-so-sure/"
  - "CFA Institute, comentario sobre Penman, Accounting for Value (según su resumen): https://blogs.cfainstitute.org/?p=26536"
  - "Ocean Tomo, Intangible Asset Market Value Study (según su resumen): https://oceantomo.com/insights/ocean-tomo-releases-intangible-asset-market-value-study-interim-results-for-2020/"
  - "Contabilidad/.investigacion/estados-contables.md (2026-11-27)"
  - "Contabilidad/.investigacion/posicion-contraria.md (2026-11-27), secciones 4 y 5"
aliases: [balance general, estado de situación patrimonial, estado de situación financiera, balance sheet, statement of financial position, activo corriente, pasivo corriente, capital de trabajo, working capital, valor en libros, book value]
creado: 2026-11-27
revisado:
---

# Balance

El balance es el estado que muestra, a una fecha, lo que la empresa controla (activo), lo que debe a terceros (pasivo) y lo que queda para sus dueños (patrimonio neto), separando lo corriente de lo no corriente.

Es la [partida doble](../Registro/partida-doble.md) puesta en un solo cuadro: activo = pasivo + patrimonio neto. Cada asiento deja esa igualdad cerrada, así que el balance, que suma los saldos de todas las cuentas patrimoniales, también cierra. Es una foto a una fecha y no un período: lo que pasó entre dos balances lo cuentan el [estado de resultados](estado-de-resultados.md), el estado de cambios en el patrimonio (en la [entrada de la vertical](estados-contables.md)) y el [estado de flujo de efectivo](estado-de-flujo-de-efectivo.md).

## Las tres partes y cómo se ordenan

OpenStax presenta el balance clasificado con estos grupos, en este orden:

| Lado | Grupo | Qué junta |
|---|---|---|
| Activo | Activo corriente | lo que se va a convertir en caja o consumir en el corto plazo |
| Activo | Propiedad, planta y equipo | los bienes de uso, netos de su amortización acumulada |
| Activo | Intangibles | los derechos sin forma física que la empresa reconoce |
| Activo | Otros activos | lo que no entra en los anteriores |
| Pasivo | Pasivo corriente | lo que se cancela en el corto plazo |
| Pasivo | Pasivo a largo plazo | lo demás |
| Patrimonio neto | Capital y resultados acumulados | lo aportado por los dueños y lo ganado y no distribuido |

El capital de trabajo es el activo corriente menos el pasivo corriente. Mide con qué cuenta la empresa para pagar lo que vence pronto.

## El balance de Clip'em Cliff al 31 de agosto de 2019

OpenStax cierra su ciclo contable completo con este balance (cifras en dólares):

| Rubro | Importe |
|---|---|
| Activo total | 80.875 |
| Pasivo total | 11.000 |
| Patrimonio neto | 69.875 |
| Pasivo más patrimonio neto | 80.875 |

El patrimonio de $69.875 incluye los resultados acumulados de −$125 que vienen del estado de cambios en el patrimonio. Cómo llega ese número desde el resultado del mes está en la [entrada de la vertical](estados-contables.md).

## Qué decide si algo es corriente

Un pasivo es no corriente si la empresa tiene, al cierre, el derecho de postergar su cancelación al menos doce meses después de la fecha del balance. Así resumen KPMG y BDO las reformas de la NIC 1 de 2020, que rigen para los ejercicios que empiezan el 1 de enero de 2024 o después. Dos consecuencias:

- La intención de la gerencia no cambia la clasificación. Si la empresa tiene el derecho de postergar pero piensa pagar en seis meses, la deuda sigue siendo no corriente.
- De los convenios de un préstamo (covenants), solo afectan la clasificación los que hay que cumplir en la fecha de cierre o antes. Los que vencen después se revelan en las notas. La NIC 1 incorporó esto con la enmienda de octubre de 2022.

Según BDO, la NIIF 18, que reemplaza a la NIC 1 desde el 1 de enero de 2027, deja estos requisitos iguales. Es una sola fuente, secundaria.

> [!NOTE]
> Sin fuente todavía: el texto de los párrafos 54 a 80A de la NIC 1 (partidas mínimas del balance y criterios de activo y pasivo corriente, incluido el ciclo normal de operación). El texto de la norma requiere suscripción y no se leyó.

Para quien construye un sistema, la clasificación corriente o no corriente depende de un plazo y de un derecho al cierre, no de la cuenta en sí. Un préstamo a tres años tiene una porción que vence en los próximos doce meses. Un [plan de cuentas](../Registro/plan-de-cuentas.md) que fija la clasificación por cuenta no alcanza para separar esa porción; hace falta poder reclasificarla al cierre (inferencia sobre el diseño, no lo dicen las fuentes).

## Lo que el balance no dice

El balance no dice cuánto vale la empresa. Mide cada partida con una regla de reconocimiento, que en muchos casos es el costo. Según OpenStax, el valor en libros de un bien de uso es la parte de su costo que todavía no pasó a gasto por amortización, y la amortización no sigue el valor de mercado del bien. Un edificio comprado hace veinte años figura por lo que queda de su costo, no por lo que se pagaría hoy por él.

Ninguna fuente encontrada nombra el mito con esas palabras; se sostiene en lo que explican OpenStax sobre el valor en libros y Penman sobre su uso. Según un comentario del CFA Institute sobre *Accounting for Value*, Penman trata el valor en libros como el ancla de un modelo de valuación (el de resultado residual), que se completa con las ganancias futuras, y no como una tasación.

La diferencia más grande está en los intangibles. Ocean Tomo calcula el valor intangible de las empresas del S&P 500 como la capitalización de mercado menos el activo tangible neto. Con ese cálculo, el intangible sería el 17% del valor en 1975, el 68% en 1995, el 84% en 2015 y alrededor del 90% entre 2020 y 2025. Hay dos cuidados con esa cifra. Es un residuo (todo lo que no es activo tangible neto) y no una medición de intangibles. Y la publica una consultora que vende servicios de propiedad intelectual.

En una empresa de software, buena parte de ese residuo serían el código, la marca, la cartera de clientes y los datos propios, que en general no figuran en el balance (es la lectura del informe de investigación, no una cifra de fuente). Para quien vende o implementa un sistema: el balance de un cliente no es una tasación de su negocio.

> [!IMPORTANT]
> **Disputado: si los estados contables perdieron relevancia para valuar empresas.**
> - **Lev y Gu** (*The End of Accounting*, 2016) sostienen, según la ficha del editor, que los informes financieros se volvieron inútiles para las decisiones en el mercado de capitales, y proponen reemplazarlos por un informe de creación de valor (*Value Creation Report*). Según la reseña de Fortune, el libro estima que el poder explicativo de las ganancias sobre el valor de mercado pasó de un R cuadrado de 80% a 90% en los años cincuenta a uno de 45% a 55% en la década de 2010. La tabla original no se leyó.
> - **Las réplicas** dicen que la conclusión es apresurada. El CFA Institute, según su resumen, considera prematuras esas inferencias y cita trabajos según los cuales la relación entre ganancias y rendimientos se midió mal; un estudio asociado a Stanford halla que la relevancia de la información contable para el valor aumentó entre 1962 y 2014, y discute el R cuadrado de mínimos cuadrados ordinarios como medida de esa relevancia.
>
> No hay consenso.

Cómo se elige entre medir al costo o al valor razonable, y por qué esa elección también se discute, está en [normas contables](normas-contables.md). Cómo nace el número de cada bien de uso y su amortización acumulada está en [activos fijos y amortización](../Operaciones/activos-fijos-y-amortizacion.md).
