---
resumen: >-
  Una correlación dice que dos cosas varían juntas; una causa, que cambiar una cambia la otra. Pasar
  de la primera a la segunda exige comparar con lo que habría pasado sin el cambio, el contrafactual,
  y eso solo lo da bien un grupo de control.
estado: borrador
estabilidad: estable
fuentes:
  - "Miguel Hernán y James Robins, Causal Inference: What If (Chapman & Hall/CRC, 2020; versión web © 2026), parte I (solo la página del libro): https://miguelhernan.org/whatifbook"
  - "Scott Cunningham, Causal Inference: The Mixtape, cap. 9, Difference-in-Differences (según su resumen): https://mixtape.scunning.com/09-difference_in_differences"
  - "Ron Kohavi, Diane Tang y Ya Xu, Trustworthy Online Controlled Experiments (Cambridge UP, 2020), sitio del libro: https://experimentguide.com/"
  - "Adrian Barnett, Jolieke van der Pols y Annette Dobson, Regression to the mean: what it is and how to deal with it, Int J Epidemiol 34(1), 215-220, 2005 (abstract): https://pubmed.ncbi.nlm.nih.gov/15333621/"
  - "Datos/.investigacion/estadistica.md"
aliases: [correlación no implica causalidad, causalidad, inferencia causal, causal inference, contrafactual, confusor, diferencias en diferencias, difference-in-differences]
creado: 2026-11-27
revisado:
---

# Correlación y causalidad

Una correlación dice que dos cosas varían juntas; una causa, que cambiar una cambia la otra. Pasar de la primera a la segunda exige comparar con lo que habría pasado sin el cambio, el contrafactual, y eso solo lo da bien un grupo de control.

Casi todo lo que muestra un tablero son correlaciones: las ventas subieron el mes en que se lanzó la campaña, los clientes que usan la app compran más. La pregunta que importa para decidir es causal: si se hace X, ¿cambia Y? Entre una y otra hay tres trampas, y cada una tiene nombre.

## Tres razones por las que dos cosas se mueven juntas sin causarse

- Un confusor: una tercera variable mueve a las dos. En diciembre suben a la vez la publicidad y las ventas, y las dos responden a las fiestas.
- La causa al revés: los clientes que compran mucho descargan la app porque ya compran mucho, no al revés.
- La selección: el grupo que recibió el cambio era distinto desde antes. Quienes usaron un cupón ya eran clientes más activos.

A eso se suma el azar, que en datos chicos produce correlaciones que desaparecen al mes siguiente, y la [regresión a la media](sesgos.md#regresión-a-la-media). Los tres primeros ejemplos son ilustraciones de la base, no casos de una fuente.

## El contrafactual y el grupo de control

La causa de un cambio es la diferencia entre lo que pasó y lo que habría pasado sin él. Lo segundo no se observa nunca: es el contrafactual. La parte I de *Causal Inference: What If* de Hernán y Robins, la que no usa modelos, trata esa idea y la comparabilidad de los grupos (lectura de la base: solo se vio la página del libro, no el texto).

Un experimento con reparto al azar resuelve el problema. Si los clientes se reparten al azar entre recibir y no recibir el cambio, los dos grupos son iguales en todo salvo en el cambio, y la diferencia en el resultado es su efecto. Es el [experimento A/B](../../Producto/Medicion/experimento-ab.md) en producto y la prueba de [incrementalidad](../../Marketing/Medicion/incrementalidad.md) en marketing. Kohavi, Tang y Xu mantienen, según el sitio de su libro, una lista de afirmaciones causales de estudios observacionales que después refutaron experimentos controlados.

> [!NOTE]
> Sin fuente todavía: el contenido de esa lista de Kohavi (la página no abrió) y una fuente de referencia para la frase «correlación no implica causalidad» como error de quien aprende.

## Diferencias en diferencias, cuando no se puede sortear

Muchas veces no hay experimento: la promoción ya se hizo, o se aplicó a todas las sucursales de una provincia. Los métodos cuasi-experimentales buscan un grupo de comparación que haga de contrafactual. El más usado en negocio es diferencias en diferencias.

Compara el cambio en el tiempo del grupo que recibió el tratamiento con el cambio del grupo que no lo recibió. El efecto es la diferencia entre los dos cambios; Cunningham lo resume como «four averages and three subtractions». Funciona si se cumple un supuesto: sin el tratamiento, los dos grupos habrían seguido tendencias paralelas. Ese supuesto no se puede probar; se examina con evidencia indirecta, como ver si antes del tratamiento ya iban paralelos.

Un ejemplo inventado: la promoción se hizo en la sucursal A y no en la B. A pasó de 100 a 130 ventas diarias; B, de 90 a 105. A creció 30 y B 15; el efecto estimado es 30 − 15 = 15 ventas diarias, no 30. Vale si A y B venían moviéndose igual antes de la promoción.

## Las ventas subieron después de una promoción: ¿la causó?

Es la pregunta más común de un comercio, y no hay una fuente que la trate como caso. Lo que sigue es razonamiento de la base, armado con las piezas de esta nota y de [sesgos](sesgos.md).

Comparar el mes de la promoción con el mes anterior mezcla el efecto con todo lo demás que cambió. Antes de atribuirle la suba, conviene descartar cinco explicaciones:

1. Estacionalidad: ¿el mismo mes del año pasado también subió? Comparar contra el mismo período del año anterior, no contra el mes previo.
2. Tendencia: si las ventas ya venían subiendo, la promoción se lleva un crédito que no es suyo.
3. Regresión a la media: si la promoción se lanzó porque el mes anterior fue malo, el siguiente tiende a ser mejor sin hacer nada.
4. Compras adelantadas: la promoción puede traer compras que igual iban a ocurrir. Mirar las semanas posteriores: si caen por debajo de lo normal, parte de la suba era adelanto.
5. Otra causa simultánea: una campaña, un competidor que cerró, un feriado largo.

Si la promoción se puede repetir, la respuesta firme es un experimento: aplicarla a una parte de los clientes o de las sucursales elegida al azar. Si no, lo mejor disponible es diferencias en diferencias contra una sucursal, un segmento o un canal que no la tuvo. Aun así, la conclusión dice «compatible con un efecto de tal tamaño», no «la promoción causó».

## Leer a Hernán y Robins y a Cunningham

Los dos libros son gratis en la web. De Hernán y Robins conviene la parte I, sin modelos, para la idea de contrafactual, de confusor y de grupos comparables. Para la práctica, el capítulo 9 de Cunningham, sobre diferencias en diferencias. En los dos, fijarse en que los métodos sin sorteo viven de supuestos que no se pueden comprobar con los datos (lectura de la base).
