---
resumen: >-
  La planificación de la cadena es la parte que decide, por período, cuánto se va a vender y cuánto hace falta tener, comprar, producir y mandar a cada lugar. Se arma como una jerarquía de planes: arriba, pocos números por familia y a meses o años; abajo, muchos números por artículo, lugar y semana.
estado: borrador
estabilidad: estable
fuentes:
  - "APQC, Process Classification Framework 7.4 (2024), categoría 4.1 «Plan for and align supply chain resources» y sus niveles 4.1.2 y 4.1.5: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Gershwin, S. B., Material Requirements Planning, diapositivas de MIT 2.853/2.854 (publicadas en MIT OCW, otoño de 2016), diapositivas 8 y 38 a 43: https://ocw.mit.edu/courses/2-854-introduction-to-manufacturing-systems-fall-2016/4eec617bb52d64f4ea1bed6d9905bc00_MIT2_854F16_MatrialRequire.pdf"
  - "CSCMP, Supply Chain Management Terms and Glossary (2013), entradas forecast, demand planning, S&OP y DRP (copia no oficial): https://www.cisco-eagle.com/uploads/cscmp/cscmp-glossary.pdf"
  - "Cadena-de-suministro-y-logistica/.investigacion/planificacion.md (sección 1), planificacion-3.md y fundamentos-y-contraria-2.md (secciones 2.1 y 10)"
aliases: [planificación, planificación de la cadena de suministro, supply chain planning, planificación de la demanda, demand planning, jerarquía de planes, planning hierarchy, horizonte de planificación, planning horizon, empujar y tirar, push y pull]
creado: 2026-11-27
revisado:
---

# Planificación

La planificación de la cadena es la parte que decide, por período, cuánto se va a vender y cuánto hace falta tener, comprar, producir y mandar a cada lugar. Se arma como una jerarquía de planes: arriba, pocos números por familia y a meses o años; abajo, muchos números por artículo, lugar y semana.

Es la primera de las cinco partes de [Cadena de suministro y logística](../cadena-de-suministro-y-logistica.md). Le dice a la [Red de distribución](../Red-de-distribucion/red-de-distribucion.md) cuánto mover y adónde, y fija cuánto comprar y cuánto producir, que ejecutan Compras y abastecimiento y Producción (temas todavía no armados). Recibe de [Despacho y entrega](../Despacho-y-entrega/despacho-y-entrega.md) lo entregado y lo devuelto, que es la historia con la que se pronostica.

## El mapa de procesos: APQC 4.1

El marco de procesos de APQC (versión 7.4) junta casi toda la vertical en la categoría 4.1, «Plan for and align supply chain resources». De sus procesos de nivel 3, son de este tema 4.1.2 «Manage demand for products», que cubre el [pronóstico de demanda](pronostico-de-demanda.md) y el [error de pronóstico](error-de-pronostico.md), y 4.1.5 «Plan distribution requirements» con las restricciones de 4.1.6, que son la [planificación de la distribución](planificacion-de-la-distribucion.md). Los de materiales y plan maestro (4.1.1, 4.1.3 y 4.1.4) son de Producción. El reparto proceso por proceso está en [marcos de la cadena de suministro](../Fundamentos/marcos-de-la-cadena-de-suministro.md#el-pcf-de-apqc-proceso-por-proceso).

Adentro de 4.1.2, APQC lista en este orden: «Develop baseline demand forecasts», «Collaborate demand with customers», «Develop demand consensus forecast», «Determine available to promise», «Monitor activity against demand forecast», «Evaluate and revise demand forecasting approach» y «Measure demand forecast accuracy». El disponible para prometer de esa lista está en Inventario, en [disponible para prometer](../../Inventario-y-depositos/Existencias/disponible-para-prometer.md).

APQC no tiene un proceso llamado S&OP. Lo más cercano es 4.1.2.3, el pronóstico de consenso. El [plan de ventas y operaciones](plan-de-ventas-y-operaciones.md) viene de los cuerpos de certificación y de la bibliografía, y el glosario del CSCMP sí lo define. El reparto es corte de la base, no de APQC.

## La jerarquía de planes y su horizonte

Los planes se encadenan de arriba hacia abajo. Las diapositivas de MIT 2.854 lo resumen en tres ideas: «Higher levels deal with longer time scales and more of the system (scope)», «Higher levels use more aggregated (coarse-grained) models» y «Higher levels send production targets down to lower levels».

| Nivel | Horizonte y detalle, según la fuente | Plan | Dónde está |
|---|---|---|---|
| Largo plazo | «six months to five years», recalculado de «1/month to 1/year», con detalle de «part family» (MIT) | pronóstico agregado, recursos, plan agregado | [pronóstico de demanda](pronostico-de-demanda.md), [plan de ventas y operaciones](plan-de-ventas-y-operaciones.md) |
| Plazo intermedio | gestión de la demanda, que «converts long range forecast and actual orders into detailed forecast» (MIT) | plan maestro y capacidad gruesa (MIT); el MRP lo ubica acá la base | Producción, todavía no armado |
| Plazo intermedio, sin fábrica | por artículo, depósito y semana | plan de distribución (DRP) | [planificación de la distribución](planificacion-de-la-distribucion.md) |
| Corto plazo | plan diario y control de planta (MIT) | qué se despacha o produce hoy | Producción; en lo de este tema, [despacho](../Despacho-y-entrega/despacho.md) |

La fila del DRP no está en las diapositivas de MIT, que son de una fábrica; la ubica la base en el mismo nivel que el MRP porque usa la misma cuenta. Para el S&OP, la única cifra de horizonte con fuente es de 18 meses, de un caso (está en su nota).

> [!NOTE] Sin fuente todavía: una jerarquía de planes con horizontes de un libro de texto de cadena de suministro (Chopra y Meindl o el diccionario de ASCM). La tabla usa las diapositivas de MIT, que miran una fábrica.

Los niveles fallan en las costuras. MIT lo dice así: «The high level and low level models sometimes don't match». Un plan agregado por familia puede sumar bien y no poder bajarse a artículos, y un evento real puede dejar viejo el objetivo de arriba (lectura de la base).

## Quién planifica qué

- El pronóstico lo hacen ventas y un planificador de la demanda; el glosario del CSCMP llama a esa función demand planning: «identifying, aggregating, and prioritizing, all sources of demand». Ver [pronóstico de demanda](pronostico-de-demanda.md).
- El plan agregado lo acuerdan ventas, operaciones y finanzas en el S&OP, que según el CSCMP busca «agree on a single plan/forecast that can be used to drive the entire business». Ver [plan de ventas y operaciones](plan-de-ventas-y-operaciones.md).
- El plan por artículo lo calcula el sistema y lo revisa un planificador: el plan maestro y el MRP en Producción, el DRP en este tema.
- La compra y la orden quedan para Compras y abastecimiento: el plan dice cuánto y cuándo; a quién y a qué precio, no.

## Dónde corta con Producción y con Inventario

Con Producción, el S&OP fija cuánto producir por familia y por mes; el plan maestro lo baja a artículos y semanas, y el MRP lo explota en componentes con la lista de materiales. El plan maestro y el MRP son de Producción, todavía no armado. El DRP usa la misma cuenta de neteo, pero entre depósitos en lugar de entre niveles de una lista de materiales.

Con Inventario, la reposición va artículo por artículo y mira la posición de stock, con [punto de pedido](../../Inventario-y-depositos/Reposicion/punto-de-pedido.md) y [lote económico](../../Inventario-y-depositos/Reposicion/lote-economico.md): ver [reposición](../../Inventario-y-depositos/Reposicion/reposicion.md). Este tema planifica por períodos hacia adelante y para varios lugares a la vez. El colchón contra el error del pronóstico se calcula allá, en [stock de seguridad](../../Inventario-y-depositos/Reposicion/stock-de-seguridad.md); el error se mide acá.

## Empujar o tirar

El plan por períodos de esta vertical empuja: MIT llama «Push system» a aquel «in which material is loaded based on planning or forecasts, not on current demand», y pone al MRP de ejemplo. El punto de pedido de Inventario tira. Las dos lógicas y la discusión entre escuelas están en [Fundamentos](../Fundamentos/fundamentos-de-cadena-de-suministro.md#empujar-o-tirar).

## Cómo falla la planificación

- Se planifica con un número sin error declarado. Todo plan parte de un pronóstico; si nadie mide cuánto se equivoca, el colchón queda a ojo. Ver [error de pronóstico](error-de-pronostico.md).
- Cada eslabón pronostica lo que le piden, no lo que se vende. La variabilidad crece aguas arriba: es el [efecto látigo](efecto-latigo.md).
- Ventas y operaciones tienen números distintos. Es el problema que el S&OP quiere resolver con un plan único.

## Lo que un sistema guarda para planificar

APQC deja ver los objetos comunes: un pronóstico base y uno de consenso (dos versiones del mismo número), el disponible para prometer, un plan de materiales «unconstrained» y otro «constrained», el plan de distribución por destino y los datos maestros de planificación («Maintain master data»). Los ERP abiertos consultados guardan el pronóstico y el plan maestro como documentos separados y encadenados, el segundo generado del primero, y no tienen un objeto para la reunión de acuerdo entre áreas. La cantidad por lugar y estado, que es la entrada de todos los planes, es de [Inventario y depósitos](../../Inventario-y-depositos/inventario-y-depositos.md).

## Qué hay en Planificación

- [Pronóstico de demanda](pronostico-de-demanda.md): los métodos (de referencia, suavizado, juicio), la demanda intermitente, la jerarquía y por qué la venta no es la demanda.
- [Error de pronóstico](error-de-pronostico.md): sesgo, MAE, MAPE, MASE y la señal de seguimiento; qué mide cada una y para qué sirve medir.
- [Plan de ventas y operaciones](plan-de-ventas-y-operaciones.md): el S&OP, su ciclo mensual, quién decide, la evidencia sobre su efecto y cómo se distingue del presupuesto y del plan maestro.
- [Planificación de la distribución](planificacion-de-la-distribucion.md): el DRP, la tabla por período y cómo los pedidos de cada depósito se vuelven necesidades del central.
- [Efecto látigo](efecto-latigo.md): por qué los pedidos varían más que las ventas a medida que se sube por la cadena, sus cuatro causas, sus remedios y cuánto se lo encuentra en los datos.
