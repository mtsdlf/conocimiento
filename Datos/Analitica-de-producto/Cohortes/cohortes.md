---
resumen: >-
  Cohortes es la parte del análisis que define a quién se sigue: grupos fijos de usuarios que
  comparten un evento de entrada en el mismo período, y por qué se los compara a la misma edad.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Cohortes

Cohortes es la parte del análisis que define a quién se sigue: grupos fijos de usuarios que
comparten un evento de entrada en el mismo período, y por qué se los compara a la misma edad.

Dentro de [Analítica de producto](../analitica-de-producto.md), parte de [Datos](../../datos.md), la cohorte es la unidad de todo lo demás. Le da a
[Retención y churn](../Retencion-y-churn/retencion-y-churn.md) el denominador de cada métrica, y la
[Lectura de cohortes](../Lectura-de-cohortes/lectura-de-cohortes.md) pone una cohorte en cada fila de la tabla.

## Un grupo fijo por evento y fecha de entrada

Una cohorte se define con un evento de entrada (registrarse, hacer la primera compra, usar una
función) y la ventana en que ocurrió. Quien cumple las dos queda en la cohorte, haga lo que haga
después. Eso la separa de un segmento, que agrupa por un atributo en el momento de la consulta y
cambia de miembros cuando cambia el atributo.

Según el evento de entrada hay dos tipos. La de adquisición agrupa por cuándo llegó cada usuario y
es la cohorte por defecto. La de comportamiento agrupa por lo que hizo, y se compara dentro de una
misma cohorte de adquisición para no mezclar épocas.

## Por qué se compara a la misma edad

Comparar las cohortes en el mismo período desde su entrada (todas en su semana 4, por ejemplo) deja
una sola diferencia entre ellas: la época en que llegaron. El
[análisis de cohortes](analisis-de-cohortes.md) explica por qué eso evita el efecto de mezcla de
los promedios, con los pasos y un ejemplo. Lo que se ve son diferencias, no causas: que los que
hicieron una acción retengan más es una correlación hasta que un experimento lo pruebe.

## Las cuatro notas de cohortes

- [Cohorte](cohorte.md) — qué es una cohorte y en qué se diferencia de un segmento; se lee primero.
- [Cohorte de adquisición](cohorte-de-adquisicion.md) — agrupar por cuándo llegó cada usuario; la cohorte por defecto.
- [Cohorte de comportamiento](cohorte-de-comportamiento.md) — agrupar por lo que hizo; para buscar qué acciones van con
  quedarse.
- [Análisis de cohortes](analisis-de-cohortes.md) — por qué se comparan cohortes a la misma edad en vez de promedios.
