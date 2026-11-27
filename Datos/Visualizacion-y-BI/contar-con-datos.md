---
resumen: >-
  Contar con datos es presentar un hallazgo para que alguien que no hizo el análisis entienda qué
  pasó y qué conviene hacer: una idea principal, el gráfico que la muestra y lo justo de contexto.
estado: vigente
estabilidad: semi
fuentes:
  - "Cole Nussbaumer Knaflic, Storytelling with Data (Wiley, 2015), solo la ficha: https://oreilly.com/library/view/storytelling-with-data/9781119002253"
  - "Storytelling with Data, página de los libros: https://www.storytellingwithdata.com/books"
  - "Resumen secundario de los seis pasos de Knaflic (según el buscador): https://www.goodreads.com/notes/27156297-storytelling-with-data/1987374-bryan-tanner"
  - "Datos/.investigacion/metricas-y-visualizacion.md (sección 6)"
aliases: [storytelling con datos, data storytelling, presentar hallazgos, comunicar datos]
creado: 2026-11-27
revisado: 2026-11-27
---

# Contar con datos

Contar con datos es presentar un hallazgo para que alguien que no hizo el análisis entienda qué
pasó y qué conviene hacer: una idea principal, el gráfico que la muestra y lo justo de contexto.

Es el paso de comunicar del proceso de [Análisis](../Analisis/analisis.md) y el tercer uso de un
gráfico en [Visualización y BI](visualizacion-y-bi.md), distinto de vigilar con un
[tablero](tablero.md). Un tablero se mira muchas veces y no tiene conclusión; un hallazgo se
cuenta una vez y la tiene.

## Los seis pasos de Knaflic

La referencia más usada es *Storytelling with Data* (2015) de Cole Nussbaumer Knaflic. Su sitio
describe "our proven, simple process for creating a clear and well-designed graph from selecting
the chart type to thinking like a designer". Un resumen secundario lo da en seis pasos, que no se
confirmaron en el texto del libro:

1. Entender el contexto: quién es la audiencia y qué tiene que hacer.
2. Elegir un visual efectivo.
3. Eliminar el desorden.
4. Dirigir la atención a lo que importa.
5. Pensar como diseñador.
6. Contar una historia.

El segundo paso es [elegir un gráfico](elegir-un-grafico.md). El tercero y el cuarto van juntos: lo
que no ayuda a ver la idea se saca o se pasa a gris, y lo que la muestra se destaca con un color o
un rótulo (lectura de la base).

> [!NOTE]
> Sin fuente todavía: los seis pasos y los nombres de los capítulos de Knaflic leídos en el libro.

## La conclusión va primero

Quien no hizo el análisis quiere saber qué se encontró y qué se le pide, no recorrerlo. Por
eso el hallazgo se dice en la primera oración, y lo que lo sostiene va debajo, agrupado en pocas
razones. El recorrido del análisis (qué tablas, qué limpieza, qué se probó y no sirvió) queda para
quien lo pregunte. Es la estructura de pirámide que se asocia a Barbara Minto.

> [!NOTE]
> Sin fuente todavía: la estructura de pirámide de Minto aplicada a presentar hallazgos no se leyó en
> una fuente primaria.

## Decir qué afirma el número

Contar bien un hallazgo incluye decir hasta dónde llega. La mayoría de los números de un análisis
son descriptivos: dicen qué pasó, no por qué. «Las ventas subieron 12 % la semana de la promoción»
es un hecho; «la promoción subió las ventas 12 %» es una afirmación causal que pide otra evidencia (ejemplo de la base).
La diferencia está en [correlación y causalidad](../Estadistica/correlacion-y-causalidad.md).

Con muestras chicas, un cambio puede ser ruido, y un número sin rango da una seguridad que no tiene.
Cómo se expresa esa incertidumbre está en [muestreo e inferencia](../Estadistica/muestreo-e-inferencia.md).
Y si el número es una métrica, la definición que se usó va en una nota al pie: así nadie compara
contra otra cifra que se llama igual y se calcula distinto (lectura de la base).

## Cómo se arma la presentación de un hallazgo

1. Escribí en una oración qué encontraste y qué le pedís a quien lo lee. Si no entra en una oración,
   todavía no sabés qué querés decir.
2. Escribí quién lo va a leer, qué sabe y qué puede decidir.
3. Elegí el único gráfico que muestra la idea. Un hallazgo, un gráfico.
4. Poné como título del gráfico la conclusión, no el nombre de los datos: «Los clientes de marzo
   vuelven menos que los de enero», no «Retención por cohorte».
5. Sacá lo que no ayuda: líneas de fondo, leyendas que se pueden rotular directo, decimales de más.
6. Destacá lo que importa con un color; el resto, en gris.
7. Agregá debajo las dos o tres razones o datos que sostienen la idea, y qué no se puede afirmar.
8. Cerrá con la decisión o el próximo paso que proponés.

Los pasos son de la base, a partir de los de Knaflic y de la estructura de la conclusión primero.

## Cuatro formas de perder al lector

- Mostrar todo lo que se exploró, en el orden en que se hizo, y dejar que el lector saque la
  conclusión.
- Un gráfico que muestra los datos sin decir qué hay que ver en ellos.
- Afirmar una causa donde hay una coincidencia, o presentar como seguro un cambio que puede ser
  ruido.
- Contar el número sin su definición, y que otra persona lo contradiga con una cifra calculada de
  otra forma.

La lista es de la base.

La referencia es el libro de Knaflic, que se recomienda empezar por el contexto (quién es la
audiencia, qué tiene que hacer y cuál es la idea principal), según un resumen y sin haberlo leído.
Conviene confirmar ahí los pasos y los capítulos.
