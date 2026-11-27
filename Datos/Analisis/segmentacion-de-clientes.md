---
resumen: >-
  La segmentación de clientes es agrupar a los clientes que ya compraron según lo que hicieron
  (cuándo compraron por última vez, cuántas veces, cuánto gastaron) para tratar distinto a cada
  grupo. RFM es una técnica habitual para hacerlo con una tabla de ventas.
estado: vigente
estabilidad: estable
fuentes:
  - "IBM SPSS Statistics 23, RFM Analysis: https://www.ibm.com/support/knowledgecenter/SSLVMB_23.0.0/spss/rfm/rfm_intro.xml.html"
  - "Jan Roelf Bult y Tom Wansbeek, Optimal Selection for Direct Mail, Marketing Science 14(4):378-394, 1995 (solo abstract): https://ideas.repec.org/a/inm/ormksc/v14y1995i4p378-394.html"
  - "DMA (Reino Unido), Use RFM modelling to generate successful customer segments (según resumen): https://dma.org.uk/article/use-rfm-modelling-to-generate-successful-customer-segments"
  - "Amplitude, Segments and cohorts (actualizada 2026-10-29): https://amplitude.com/docs/analytics/segments/segments-and-cohorts"
  - "Userpilot y SendPulse, segmentos contra cohortes (blogs de proveedor, según resumen): https://userpilot.com/blog/?p=12946 ; https://sendpulse.com/en/support/glossary/cohort-analysis"
  - "Ejemplo de RFM con ntile corrido por la base en SQLite 3.53 el 2026-11-27"
  - "Datos/.investigacion/analisis.md"
aliases: [RFM, análisis RFM, RFM analysis, customer segmentation, segmentar clientes, recencia frecuencia monetario, segmento]
creado: 2026-11-27
revisado: 2026-11-27
---

# Segmentación de clientes

La segmentación de clientes es agrupar a los clientes que ya compraron según lo que hicieron
(cuándo compraron por última vez, cuántas veces, cuánto gastaron) para tratar distinto a cada
grupo. RFM es una técnica habitual para hacerlo con una tabla de ventas.

Es una técnica de la fase de analizar del [análisis](analisis.md), y trabaja sobre la base de
clientes propia. La [segmentación de mercado](../../Marketing/Mercado-y-cliente/segmentacion.md) de
Marketing es otra cosa: divide un mercado entero, con clientes y no clientes, por necesidad o
conducta, para decidir a quién apuntar y qué ofrecer. Esta divide a los que ya compraron, con los
datos que dejaron, para decidir a quién escribirle, a quién darle un beneficio o a quién intentar
recuperar.

## RFM: recencia, frecuencia y monto

RFM puntúa a cada cliente en tres ejes. La documentación de IBM los define así: recencia es el
tiempo desde la última compra, frecuencia es cuántas compras hizo, y monto es el «total amount
spent». IBM sostiene que «the most important factor in identifying customers who are likely to
respond to a new offer is recency».

Cada eje se divide en categorías; en un esquema de cinco, 5 es lo mejor y 1 lo peor. Los tres
puntajes se concatenan: el mejor cliente posible es 555, y un 155 es alguien que compraba mucho y
hace rato que no vuelve. IBM aclara que los datos tienen que estar a un cliente por fila: si hay
varias ventas por cliente, primero se resumen. La misma página la llama una «simple theory» y no
presenta una validación estadística.

Con una tabla de ventas, el cálculo es una agregación al grano cliente y tres funciones de
ventana (los conceptos están en [SQL para análisis](sql-para-analisis.md)):

```sql
WITH por_cliente AS (
  SELECT id_cliente,
         current_date - max(fecha) AS dias_desde_ultima,
         count(*)                  AS compras,
         sum(total)                AS gastado
  FROM ventas
  GROUP BY id_cliente
)
SELECT id_cliente,
       ntile(5) OVER (ORDER BY dias_desde_ultima DESC) AS r,  -- 5 = compró hace poco
       ntile(5) OVER (ORDER BY compras)               AS f,
       ntile(5) OVER (ORDER BY gastado)               AS m
FROM por_cliente;
```

## Dónde falla RFM

Los puntos de corte los elige el analista, y cambian quién queda en cada grupo. `ntile` reparte
las filas en cinco partes iguales aunque tengan el mismo valor: al correrlo la base sobre cinco
clientes, cuatro con una sola compra quedaron con puntajes de frecuencia distintos, del 1 al 4. En
un comercio donde la mayoría compró una sola vez, la frecuencia por quintiles no separa nada; cortes
fijos (1 compra, 2 a 3, 4 o más) suelen decir más (lectura de la base).

El monto suma: un cliente mayorista de una compra grande puede quedar arriba de uno que compra
todos los meses. Y RFM mira solo el pasado; no dice cuánto va a dejar un cliente, que es el valor
de vida del cliente (LTV) de la [economía unitaria](../../Marketing/Medicion/economia-unitaria.md).

> [!IMPORTANT]
> El origen de RFM está discutido. La DMA del Reino Unido dice que lo introdujeron Bult y Wansbeek
> en 1995; otras fuentes lo ubican antes, en el marketing directo, con Cullinan y con Hughes (1994),
> según resúmenes. El abstract de Bult y Wansbeek habla de un método para elegir a quién mandar
> correo que «explicitly accounts for the profit function», no de inventar RFM. La lectura prudente
> es que su aporte es la optimización; el origen no se verificó en una fuente primaria.

## Un segmento no es una cohorte

Las dos agrupan clientes, y las herramientas de producto las documentan en la misma página. Se
diferencian en el eje, según la lectura de la base de Amplitude, Userpilot y SendPulse:

| | Segmento | [Cohorte](../Analitica-de-producto/Cohortes/cohorte.md) |
|---|---|---|
| Agrupa por | Qué tipo de cliente es: un atributo o una conducta | Cuándo entró: un evento de entrada en una ventana de tiempo |
| La membresía | Cambia si cambia la conducta (un 555 puede volverse 155) | Queda fija desde la entrada (en el uso de esta base; Amplitude también tiene cohortes dinámicas) |
| Contesta | ¿A quién le hablo distinto? | ¿Los que entraron en agosto se quedan más que los de julio? |

Amplitude lo dice así: un segmento es «an advanced filter for analysis» y una cohorte es «an
audience», el conjunto de usuarios que cumplió condiciones en un rango de fechas; el segmento toma
las fechas del gráfico y la cohorte usa las suyas. Es la definición de un proveedor; en
epidemiología, cohorte tiene otro sentido, explicado en la nota de
[cohorte](../Analitica-de-producto/Cohortes/cohorte.md).

Se cruzan: se puede mirar la [retención por cohorte](../Analitica-de-producto/Retencion-y-churn/tasa-de-retencion-por-cohorte.md)
de cada segmento, o qué segmento RFM ocupa cada cohorte a los seis meses. Una cohorte armada por lo
que hicieron los usuarios, y no por cuándo llegaron, es una
[cohorte de comportamiento](../Analitica-de-producto/Cohortes/cohorte-de-comportamiento.md), que se
parece a un segmento pero conserva la fecha de entrada.

## Otras formas de agrupar clientes

Además de RFM se agrupa por valor de vida, por canal de adquisición, por producto o plan, por zona,
o con técnicas de agrupamiento estadístico que encuentran los grupos sin cortes fijados de antemano.

> [!NOTE]
> Sin fuente todavía: segmentación por valor de vida, por canal y por agrupamiento estadístico.
> Solo RFM y la diferencia con cohortes tienen fuentes en esta nota.

## Segmentar no prueba qué funciona con cada segmento

Que los clientes 555 respondan más a una promoción no dice que la promoción cause esas compras:
probablemente iban a comprar igual. Para saber cuánto agrega una acción sobre un segmento hace
falta un grupo de control dentro del segmento, que es la
[incrementalidad](../../Marketing/Medicion/incrementalidad.md). Encontrar segmentos es parte del
[análisis exploratorio](analisis-exploratorio.md); actuar sobre ellos y medir el efecto es otro
paso.

## Cómo segmentar una base de clientes con RFM

1. Llevá las ventas a una fila por cliente, con fecha de la última compra, cantidad de compras y total gastado.
2. Fijá la fecha de corte y excluí las ventas anuladas o devueltas.
3. Mirá la distribución de cada eje antes de cortar; si la mayoría compró una vez, usá cortes fijos para la frecuencia.
4. Puntuá cada eje y nombrá los grupos que importan para la decisión: los mejores, los que se están yendo, los nuevos.
5. Definí qué acción corresponde a cada grupo y guardá un grupo de control para medirla.
