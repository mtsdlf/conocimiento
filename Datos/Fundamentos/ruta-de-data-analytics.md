---
resumen: >-
  La ruta de Data Analytics es el orden para aprender el análisis de datos con las notas de la base
  (Análisis, Estadística, Analítica de producto y Visualización y BI, con la ingeniería como
  panorama), practicado sobre las ventas de una tienda online chica.
estado: borrador
estabilidad: semi
fuentes:
  - "Coursera, Google Data Analytics Professional Certificate: https://www.coursera.org/professional-certificates/google-data-analytics"
  - "Microsoft, Study guide for Exam PL-300 (skills measured as of April 20, 2026): https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300"
  - "Datos/.investigacion/fundamentos.md, sección 5"
  - "Datos/.investigacion/estadistica.md, sección 1 (el caso de ticket promedio contra mediana)"
aliases: [ruta de datos, aprender data analytics, cómo aprender análisis de datos, ejercicios de datos]
creado: 2026-11-27
revisado:
---

# Ruta de Data Analytics

La ruta de Data Analytics es el orden para aprender el análisis de datos con las notas de la base
(Análisis, Estadística, Analítica de producto y Visualización y BI, con la ingeniería como
panorama), practicado sobre las ventas de una tienda online chica.

Es para quien sabe usar una planilla y no sabe SQL ni estadística. El orden sigue al de los dos
programas que se revisaron: el certificado de Google de Data Analytics empieza por preguntar,
preparar y limpiar, sigue con analizar y visualizar, y deja la programación para el curso 7 de 9.
La certificación de BI de Microsoft le da entre el 25 y el 30 % del examen a preparar datos. Pasar de ahí a
este orden es lectura de la base.

## El orden de lectura

1. El modelo mental. [Datos](../datos.md) para el recorrido del dato y
   [Análisis](../Analisis/analisis.md) para el proceso: pregunta, preparar, limpiar, analizar,
   comunicar y actuar. Después, [pregunta de análisis](../Analisis/pregunta-de-analisis.md) y
   [tipos de analítica](../Analisis/tipos-de-analitica.md).
2. Análisis. [Limpieza de datos](../Analisis/limpieza-de-datos.md), [SQL para
   análisis](../Analisis/sql-para-analisis.md), [análisis
   exploratorio](../Analisis/analisis-exploratorio.md) y [segmentación](../Analisis/segmentacion-de-clientes.md).
3. Estadística. [Estadística descriptiva](../Estadistica/estadistica-descriptiva.md),
   [muestreo e inferencia](../Estadistica/muestreo-e-inferencia.md),
   [correlación y causalidad](../Estadistica/correlacion-y-causalidad.md), [sesgos](../Estadistica/sesgos.md) y
   [significancia](../Estadistica/significancia.md).
4. Analítica de producto. [Definición de métrica](../Analitica-de-producto/definicion-de-metrica.md),
   [embudo](../Analitica-de-producto/embudo.md) y, como práctica larga, el recorrido [Análisis de
   cohortes desde cero](recorrido-analisis-de-cohortes.md).
5. Visualización y BI. [Elegir un gráfico](../Visualizacion-y-BI/elegir-un-grafico.md),
   [tablero](../Visualizacion-y-BI/tablero.md), [capa semántica](../Visualizacion-y-BI/capa-semantica.md)
   y [contar con datos](../Visualizacion-y-BI/contar-con-datos.md).
6. La ingeniería, de panorama. Las entradas de [Modelado y
   almacenamiento](../Modelado-y-almacenamiento/modelado-y-almacenamiento.md), [Ingesta y
   transformación](../Ingesta-y-transformacion/ingesta-y-transformacion.md) y [Gobierno y
   calidad](../Gobierno-y-calidad/gobierno-y-calidad.md), sin los componentes. Alcanza con saber de
   dónde viene la tabla que te dan y por qué a veces llega mal.

## El caso: octubre en una tienda chica

Los pasos de abajo usan esta tabla. Es un ejemplo inventado: diez filas de pedidos de una tienda
online que vende por su web y por Instagram, montos en pesos.

| pedido | fecha | cliente | canal | monto | estado |
|---|---|---|---|---|---|
| 1001 | 2026-10-02 | C01 | instagram | 18.000 | pagado |
| 1002 | 2026-10-03 | C02 | web | 22.000 | pagado |
| 1003 | 2026-10-05 | C03 | web | 15.000 | pagado |
| 1003 | 2026-10-05 | C03 | web | 15.000 | pagado |
| 1004 | 2026-10-09 | C01 | instagram | 20.000 | pagado |
| 1005 | 2026-10-12 | C04 | web | 160.000 | pagado |
| 1006 | 2026-10-15 | C05 | instagram | 17.000 | anulado |
| 1007 | 2026-10-20 | C02 | web | 25.000 | pagado |
| 1008 | 2026-10-24 | C06 | instagram | 19.000 | pagado |
| 1009 | 2026-10-28 | C07 | web | 21.000 | pagado |

## Paso 1: predecí antes de calcular

Leé [estadística descriptiva](../Estadistica/estadistica-descriptiva.md). Sin hacer cuentas: ¿el
ticket promedio de octubre va a quedar arriba o abajo de la mediana? ¿Cerca o lejos? Anotá tu
respuesta y por qué.

<details>
<summary>Respuesta</summary>

Muy arriba. Con los pedidos válidos (ver paso 2), el promedio es 37.500 y la mediana 20.500. El
pedido 1005, de 160.000, tira el promedio hacia arriba; la mediana depende solo de los valores del
medio y no se entera. Siete de los ocho pedidos válidos están entre 15.000 y 25.000: «el cliente
típico gasta 37.500» sería falso. Con datos sesgados así conviene informar la mediana, o el promedio
con y sin el atípico.

</details>

## Paso 2: un ejemplo resuelto

La dueña pregunta «¿cuánto vendimos en octubre?», porque quiere decidir si sigue pagando publicidad.

1. La pregunta. Se convierte en una [pregunta de análisis](../Analisis/pregunta-de-analisis.md)
   con su decisión: ventas de octubre por canal, para comparar con lo gastado en cada uno.
2. La métrica. Se fija una [definición](../Analitica-de-producto/definicion-de-metrica.md):
   ventas del mes = suma de los montos de pedidos pagados, cada pedido una sola vez, por fecha de
   pedido.
3. La limpieza. La [limpieza](../Analisis/limpieza-de-datos.md) encuentra el pedido 1003 dos
   veces y el 1006 anulado. Quedan ocho pedidos.
4. El cálculo. Con [SQL](../Analisis/sql-para-analisis.md), sobre una tabla `ventas`:

   ```sql
   SELECT canal, SUM(monto) AS ventas, COUNT(*) AS pedidos
   FROM (SELECT DISTINCT pedido, canal, monto FROM ventas WHERE estado = 'pagado') AS p
   GROUP BY canal;
   ```

   Da web 243.000 en 5 pedidos e Instagram 57.000 en 3. Total: 300.000.
5. El resultado. Sumar la columna entera daba 332.000: un 10,7 % de más por un duplicado y una
   anulación. Se muestra con un gráfico de barras desde cero ([elegir un
   gráfico](../Visualizacion-y-BI/elegir-un-grafico.md)) y la definición escrita al pie.

## Paso 3: el mismo caso, cambiado

La dueña lee «web 243.000, Instagram 57.000» y concluye que la web vende cuatro veces más y que
tiene que cortar Instagram. Leé [segmentación](../Analisis/segmentacion-de-clientes.md) y [correlación y
causalidad](../Estadistica/correlacion-y-causalidad.md). ¿Qué le contestás?

<details>
<summary>Respuesta</summary>

Dos cosas. Primero, un solo pedido mayorista (1005) es dos tercios de lo que vendió la web. Sin él,
web vendió 83.000 en 4 pedidos e Instagram 57.000 en 3: por pedido, la mediana es 21.500 contra
19.000. La diferencia se achica a casi nada. Segundo, aun con una diferencia real, la tabla es
descriptiva: no dice que Instagram no genere ventas. Puede que alguien vea el producto en Instagram y
compre por la web. Saber qué ventas causa un canal es
[incrementalidad](../../Marketing/Medicion/incrementalidad.md), en Marketing. Con ocho pedidos,
además, cualquier diferencia puede ser azar ([muestreo e
inferencia](../Estadistica/muestreo-e-inferencia.md)).

</details>

## Paso 4: uno para hacer solo

Con la tabla original, contestá: ¿qué porcentaje de los clientes de octubre compró más de una
vez? Escribí primero la definición (qué es un cliente, qué cuenta como compra), después calculá.
Como segunda parte, proponé el [tablero](../Visualizacion-y-BI/tablero.md) de una pantalla para
la dueña: tres números y un gráfico.

<details>
<summary>Respuesta</summary>

Definición: cliente = quien tiene al menos un pedido pagado en octubre; compró más de una vez = dos o
más pedidos pagados distintos. Clientes: C01, C02, C03, C04, C06 y C07 (C05 solo tiene un pedido
anulado). Repitieron C01 y C02. Resultado: 2 de 6, un 33 %.

Las trampas: sin limpiar, C03 parece repetir por el duplicado y C05 cuenta como cliente, y da 3 de 7,
un 43 %. Y un mes no alcanza para hablar de retención: hay que seguir a los clientes de octubre en
noviembre y diciembre, que es el [análisis de cohortes](../Analitica-de-producto/Cohortes/analisis-de-cohortes.md).

Un tablero posible: ventas del mes con la definición al pie, mediana del pedido, porcentaje que
repite, y barras de ventas por canal, marcando aparte los pedidos mayoristas. Para que otra persona
calcule los tres números igual, la definición vive en la [capa
semántica](../Visualizacion-y-BI/capa-semantica.md) y no en cada planilla.

</details>

## Al terminar

Quien termina la ruta puede tomar una tabla de pedidos, acordar qué pregunta contesta, limpiarla,
calcular una métrica con su definición escrita y decir qué afirma un número y qué no. El paso
siguiente es practicar un análisis entero con el recorrido [Análisis de cohortes desde
cero](recorrido-analisis-de-cohortes.md). Para medir un producto digital después de eso, la
[medición de Producto](../../Producto/Medicion/medicion-de-producto.md) y el [experimento
A/B](../../Producto/Medicion/experimento-ab.md).

> [!NOTE]
> Sin fuente todavía: qué datasets abiertos usan los programas para practicar, y si la ruta coincide
> con lo que piden los avisos de trabajo de analista en Argentina.
