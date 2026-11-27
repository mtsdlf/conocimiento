---
resumen: >-
  Un proveedor de software de gestión vive de cuatro líneas: la licencia nueva, el soporte de lo ya vendido, la suscripción en la nube y los servicios. En los informes anuales de los proveedores más grandes, la licencia nueva es la línea chica y el negocio es la base instalada que paga todos los años.
estado: vigente
estabilidad: semi
fuentes:
  - "Informe anual 2024 (Form 20-F) de uno de los proveedores de ERP más grandes del mundo, ejercicio al 2024-12-31: https://www.sec.gov/Archives/edgar/data/1000184/000110465925017815/sap-20241224x20f.htm (leídas las tablas de ingresos y costos y la sección de resultados)"
  - "Informe anual 2025 (Form 10-K) de otro proveedor grande de software de empresa, ejercicio al 2025-05-31: https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/orcl-20250531.htm (leídos los apartados de negocio y la proporción de ingresos; no las tablas en dólares)"
  - "Fernando Suarez, Michael Cusumano y Steven Kahl (2013), Services and the business models of product firms, Management Science 59(2):420-435 (según su abstract): https://dspace.mit.edu/handle/1721.1/87623"
  - "Software-de-gestion/.investigacion/mercado-y-economia.md (2026-11-27), sección 2"
aliases: [economía del proveedor de ERP, ERP vendor economics, mezcla de ingresos, revenue mix, base instalada, installed base, ingreso más predecible, more predictable revenue, ingresos de soporte, support revenue]
creado: 2026-11-27
revisado: 2026-11-27
---

# Economía del proveedor

Un proveedor de software de gestión vive de cuatro líneas: la licencia nueva, el soporte de lo ya vendido, la suscripción en la nube y los servicios. En los informes anuales de los proveedores más grandes, la licencia nueva es la línea chica y el negocio es la base instalada que paga todos los años.

Es el lado del proveedor en [Mercado y economía](mercado-y-economia.md). Lo que el cliente paga en cada línea, y en qué unidad, está en [licencia y suscripción](licencia-y-suscripcion.md). Los márgenes del SaaS en general y los servicios a pérdida de un proveedor de CRM están en [SaaS](../../Emprender/Modelo-de-negocio/saas.md#la-economía-margen-alto-servicios-a-pérdida); acá va solo lo que muestran los proveedores de software de gestión.

## La mezcla de ingresos de un proveedor grande

El informe anual 2024 de uno de los proveedores de ERP más grandes del mundo separa sus ingresos por línea, en millones de euros:

| Línea | 2022 | 2023 | 2024 | Costo 2024 | Margen bruto 2024 |
|---|---|---|---|---|---|
| Nube | 11.426 | 13.664 | 17.141 | 4.660 | 72,8 % (cálculo de esta base) |
| Licencias | 2.056 | 1.764 | 1.399 | 1.262 (licencias y soporte juntos) | 90,1 % (cálculo de esta base, licencias y soporte juntos) |
| Soporte | 11.909 | 11.496 | 11.290 | | |
| Servicios | 4.128 | 4.283 | 4.346 | 3.321 | 23,6 % (dato del informe) |
| Total | 29.520 | 31.207 | 34.176 | | |

Tres cosas salen de la tabla. El soporte de lo ya vendido pesa unas ocho veces la licencia nueva (cálculo de esta base: 11.290 contra 1.399). La licencia nueva cae año a año mientras crece la nube, que según el informe superó al soporte en 2023. Y el proveedor llama «more predictable revenue» a la suma de nube y soporte: en 2024 fue 28.431 millones, el 83 % del total, contra 81 % en 2023.

El informe anual 2025 de otro proveedor grande de software de empresa no aísla el ERP, pero muestra la misma forma. La nube fue el 43 % de sus ingresos (37 % el año anterior), la nube más el soporte de licencias y las licencias sumaron el 86 %, los servicios el 9 % y el hardware el 5 %, sobre un total de USD 57.399 millones. No publica una tasa de renovación: dice que «Substantially all license support customers renew their support contracts with us upon expiration».

Cada cifra tiene una sola fuente, pero es la primaria: el informe del propio emisor ante el regulador. Las definiciones de cada línea cambian entre proveedores, así que las líneas no se comparan entre informes sin leer sus notas contables.

## Por qué el soporte es el negocio

El soporte deja margen alto porque la versión nueva se escribe una vez y se cobra a toda la base. La lectura de esta base es que eso explica tres conductas del proveedor:

- Retener vale más que vender. Si casi todos renuevan, cada cliente nuevo es una renta de años. Es el mecanismo de «barato para entrar, caro para quedarse» de los [costos de cambio](../../Estrategia-competitiva/Fuentes-de-ventaja/costos-de-cambio.md), que en un software de gestión son altos porque el cliente migró datos, adaptó procesos y entrenó gente ([migración de datos](../Implementacion/migracion-de-datos.md)).
- Pasar la base a la nube es el plan. La caída de licencias y el salto de la nube en la tabla muestran a un proveedor que convierte su propia base instalada. El cliente que pasa de soporte a suscripción sigue pagando todos los años, ahora por más cosas.
- Los servicios no son el negocio. Dejan un margen de 23,6 % en el proveedor de la tabla, positivo pero lejos del 90 % de licencias y soporte. Por eso los grandes proveedores dejan buena parte de la implantación a su [canal de partners](canal-de-partners.md).

El caso de la tabla es de un proveedor con décadas de base instalada. Un proveedor nuevo no tiene esa base: vive de la licencia o la suscripción del año y paga el costo de conseguir cada cliente, como explica [SaaS](../../Emprender/Modelo-de-negocio/saas.md#cómo-crece-el-costo-de-adquisición-y-la-retención). El patrón no se traslada sin más a uno chico.

## Cuánto servicio conviene vender

Un proveedor de software de gestión casi siempre vende algo de servicio: implantar, migrar, capacitar, adaptar. Suarez, Cusumano y Kahl (2013), con empresas de software empaquetado entre 1990 y 2006, hallaron según su abstract una relación convexa: las empresas casi solo de producto son las más rentables, sumar servicios baja el margen operativo y, pasado cierto punto, cuando los servicios son la mayoría de las ventas, vuelve a subir. El umbral no se leyó. El detalle está en [modelos de negocio de software](../../Emprender/Modelo-de-negocio/modelos-de-negocio-de-software.md#los-híbridos-software-con-servicios-y-software-con-pagos).

Para un proveedor chico de software de gestión, la lectura de esta base es que el servicio es inevitable al principio, porque el cliente no se implanta solo, y conviene que sea un medio para vender la suscripción y no la línea principal. Si los servicios crecen más rápido que el software, el proveedor se está volviendo una consultora; [servicios habilitados por tecnología](../../Emprender/Modelo-de-negocio/servicios-habilitados-por-tecnologia.md) trata ese otro modelo.

> [!NOTE] Sin fuente todavía: una tasa de renovación del soporte publicada por algún proveedor de ERP; la mezcla de ingresos de un proveedor mediano o chico; evidencia empírica de costos de cambio en ERP.

Para leer más, el informe 20-F del proveedor de la tabla: la nota de ingresos por tipo y la tabla de costos, para derivar el margen de cada línea, y la definición de «more predictable revenue» en la sección de resultados.
