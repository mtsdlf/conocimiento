---
resumen: >-
  El BI de gestión en la Argentina tiene que resolver la inflación: un peso de hace dos años no
  vale lo que un peso de hoy, los estados contables se reexpresan por inflación desde 2018, y
  muchas empresas miran también sus números en dólares. El BI necesita el índice por mes, la fecha
  de origen de cada partida y una regla escrita de qué tipo de cambio usa cada vista.
estado: vigente
estabilidad: semi
fuentes:
  - "CPCECABA, Resolución Técnica 6, texto ordenado (con la JG 539/18): https://consejo.org.ar/storage/attachments/01_RT%206.pdf-R1cZ0V8jtI.pdf"
  - "CPCECABA, Resolución C.D. 107/2018, que adopta la Resolución JG FACPCE 539/18: https://consejo.org.ar/storage/attachments/ResolucionCD107.pdf-7tClFYvNUW.pdf"
  - "CNV, Resolución General 777/2018 (Boletín Oficial, 28/12/2018): https://www.boletinoficial.gob.ar/pdf/aviso/primera/199000/20181228"
  - "IFRS Foundation, NIC 29 Financial Reporting in Hyperinflationary Economies, edición 2026, párrafos 3, 7, 8 y 34: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias29.html"
  - "IFRS Foundation, NIC 21, edición 2026, párrafos 26, 38 y 43: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias21.html"
  - "BCRA, Comunicación A 3500 (2002): https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A3500.pdf"
  - "BCRA, nota de prensa del 4/12/2025 sobre la nueva metodología del tipo de cambio de referencia: https://www.bcra.gob.ar/noticias/con-el-aporte-de-los-principales-actores-del-mercado-el-bcra-aprobo-una-nueva-metodologia-para-el-calculo-del-tipo-de-cambio-de-referencia-a-3500/"
  - "BCRA, serie del tipo de cambio de referencia A 3500: https://www.bcra.gob.ar/tipo-cambio-referencia-comunicacion-a-3500-tcnpm/"
  - "Datos/.investigacion/bi-gestion-conciliacion-moneda.md (2026-11-27)"
aliases: [BI con inflación, ajuste por inflación en el BI, reexpresión en el BI, moneda homogénea en el BI, pesos constantes, BI en dólares, moneda dual, tipo de cambio de referencia]
creado: 2026-11-27
revisado: 2026-11-27
---

# BI de gestión en la Argentina

El BI de gestión en la Argentina tiene que resolver la inflación: un peso de hace dos años no vale lo que un peso de hoy, los estados contables se reexpresan por inflación desde 2018, y muchas empresas miran también sus números en dólares. El BI necesita el índice por mes, la fecha de origen de cada partida y una regla escrita de qué tipo de cambio usa cada vista.

Es lo local del [BI sobre el software de gestión](bi-sobre-software-de-gestion.md). La norma contable vive en otros temas: el ajuste por inflación, su historia legal y el índice están en [el ajuste por inflación](../../../Contabilidad/Estados-contables/normas-contables-en-argentina.md#el-ajuste-por-inflación), en Contabilidad, y el ajuste impositivo, que es otro, en [Ganancias en la Argentina](../../../Impuestos/Impuestos-a-la-renta/ganancias-en-argentina.md). Lo que le exige la norma argentina al sistema de gestión está en [software de gestión en la Argentina](../../../Software-de-gestion/software-de-gestion-en-argentina.md).

## Por qué un gráfico en pesos nominales engaña

Con inflación alta, comparar ventas en pesos de un año con las del anterior mide sobre todo la inflación. Un tablero que muestra las ventas mensuales de cuatro años en pesos nominales dibuja una curva que sube aunque se venda lo mismo o menos (lectura de esta base). La NIC 29 lo dice para los estados contables: en una economía hiperinflacionaria, solo son útiles «if they are expressed in terms of the measuring unit current at the end of the reporting period», y los comparativos del período anterior también se reexpresan (párrafos 7, 8 y 34).

La FACPCE declaró el contexto de inflación desde el 1 de julio de 2018. Según la Resolución C.D. 107/2018 del consejo profesional de la Ciudad de Buenos Aires, que adopta la JG 539/18, la FACPCE concluyó que la tasa acumulada de inflación de los últimos tres años «supera el 100 %»; el anexo dispone que los estados contables cerrados desde esa fecha «deberán reexpresarse de acuerdo con el procedimiento establecido en la RT N° 6». La fecha no es la misma para todos: la CNV la fijó para los estados que cierren «a partir del 31 de diciembre de 2018 inclusive». Desde entonces, el balance que el BI tiene que poder conciliar está reexpresado.

## Lo que la RT 6 le pide a los datos

El procedimiento de la RT 6 se apoya en tres piezas, y el BI tiene que tener las tres como datos:

1. La fecha de origen de cada partida. Lo que ya está en moneda de cierre no se reexpresa; lo demás se reexpresa según su fecha de origen. La RT 6 llama anticuación a descomponer el saldo de una cuenta por momento de origen, y dice que «es razonable agrupar las partidas por mes de origen». En el BI, el mes del hecho ya está en la [dimensión de fecha](dimensiones-conformadas.md#el-calendario-y-los-períodos-fiscales); lo que hace falta es que los saldos no monetarios (un bien de uso, el stock, el capital) conserven el mes de origen y no solo el total.
2. El índice por mes. La serie combina el IPC Nacional del INDEC con el IPIM de la FACPCE, y la publica la FACPCE cada mes. En el BI es una tabla con un valor por mes, como la de tipos de cambio.
3. El coeficiente. «Los coeficientes aplicables a las distintas partidas resultan de dividir el valor del índice correspondiente a la fecha de cierre por el valor del índice correspondiente a la fecha o período de origen de la partida». Las del mes de cierre no se reexpresan, porque el coeficiente es uno.

Con esas tres piezas, el BI puede mostrar cualquier serie en moneda de un mismo mes. Un caso (ejemplo de esta base, con índices inventados): si el índice de enero vale 100 y el de diciembre 130, una venta de 1.000 pesos de enero equivale a 1.300 pesos de diciembre, y se compara con una venta de diciembre sin ajustar.

La reexpresión del balance la hace Contabilidad, y el BI no la reemplaza. Lo que hace el BI es leer las cifras reexpresadas para conciliar, y reexpresar las series de gestión (ventas, márgenes, gastos por centro de costo) con el mismo índice, para que el tablero y el balance hablen de la misma moneda (lectura de esta base). La JG 539/18 admite simplificar: reexpresar las partidas de resultados «incluso mediante la aplicación de coeficientes de reexpresión anuales». En un BI de gestión, el coeficiente mensual es más fiel y no cuesta más, porque los hechos ya traen el mes (lectura de esta base).

## Pesos constantes o dólares

Muchas empresas miran también la gestión en dólares, y la norma contable da lugar a eso solo en parte. La NIC 21 permite presentar los estados «in any currency (or currencies)» (párrafo 38), pero en una economía hiperinflacionaria pide reexpresar primero (párrafo 43) y después convertir todos los importes, resultados incluidos, «at the closing rate at the date of the most recent statement of financial position» (párrafo 42). Y la NIC 29 no permite presentar la información reexpresada como suplemento de estados sin reexpresar. Un tablero de gestión no es un estado contable, así que la empresa puede elegir su vista; esa distinción es lectura de esta base, no de la norma.

| Vista | Qué muestra bien | Dónde engaña |
|---|---|---|
| Pesos nominales | lo que dice cada factura; cuadra con el sistema documento por documento | cualquier comparación entre meses |
| Pesos constantes de un mes | la evolución real; cuadra con el balance reexpresado | depende del índice, que se publica con atraso |
| Dólares | la comparación con precios y costos que se fijan en dólares | depende del tipo de cambio elegido, y con brechas entre tipos cambia la conclusión |

La NIC 29 cuenta, entre los indicadores de hiperinflación, que la población «regards monetary amounts not in terms of the local currency but in terms of a relatively stable foreign currency». La vista en dólares responde a esa práctica, pero no la convierte en una medida contable (lectura de esta base).

Si se elige la vista en dólares, hace falta decidir qué tipo de cambio. El BCRA publica cada día hábil un tipo de cambio de referencia del segmento mayorista, regido por la Comunicación A 3500, con una serie histórica descargable. Desde el 1 de enero de 2026 se calcula con una metodología que se apoya en «operaciones concretas y ponderadas por volumen», según su nota de prensa. Para varios tipos disponibles, la NIC 21 (párrafo 26) da un criterio: el tipo al que se podrían haber cancelado los flujos. Un tablero de gestión en dólares que convierte cada venta al tipo de su fecha hace otra cosa que el párrafo 42: responde cuántos dólares valía cada venta cuando se hizo, sin reexpresar (lectura de esta base). Las dos vistas son válidas si la regla está escrita, como pide [multiempresa y moneda en el BI](multiempresa-y-moneda-en-el-bi.md#la-regla-de-conversión-del-grupo).

> [!NOTE]
> Sin fuente todavía:
> - Una fuente primaria sobre la práctica de llevar la gestión en dólares en la Argentina y sobre los tipos de cambio que no son el oficial; solo hay prensa y blogs.
> - El texto de la Comunicación A del BCRA con la fórmula nueva del tipo de referencia; se leyó la nota de prensa.
> - Dónde vive hoy el procedimiento de reexpresión con la RT 54 vigente (las fechas de vigencia de la RT 54 difieren entre fuentes, y no se leyó su texto). Es el mismo hueco que marca [Contabilidad](../../../Contabilidad/Estados-contables/normas-contables-en-argentina.md#el-ajuste-por-inflación).

## Cómo falla

- El crecimiento que es inflación. El tablero muestra ventas en pesos nominales de varios años y alguien lo lee como crecimiento.
- Dos índices. El BI reexpresa con un índice y Contabilidad con otro, y el margen reexpresado no cuadra con el balance.
- El dólar de hoy sobre pesos viejos. Las ventas de hace dos años, en pesos nominales y sin reexpresar, se convierten al tipo de hoy.
- El stock sin mes de origen. El BI guarda el saldo de stock pero no cuándo entró cada partida, y no puede reexpresarlo como el balance.
- El mes que falta. El índice del último mes todavía no se publicó y el tablero lo completa con el anterior sin avisar.
