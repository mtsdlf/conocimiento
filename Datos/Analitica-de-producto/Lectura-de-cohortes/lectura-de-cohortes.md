---
resumen: >-
  Lectura de cohortes es la parte del análisis que muestra el resultado: la tabla de cohortes y
  la curva de retención, cómo se leen y cómo se arma la tabla desde una tabla de eventos.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Lectura de cohortes

Lectura de cohortes es la parte del análisis que muestra el resultado: la tabla de cohortes y
la curva de retención, cómo se leen y cómo se arma la tabla desde una tabla de eventos.

Dentro de [Analítica de producto](../analitica-de-producto.md), parte de [Datos](../../datos.md), pone una cohorte de [Cohortes](../Cohortes/cohortes.md) en cada fila y
una tasa de [Retención y churn](../Retencion-y-churn/retencion-y-churn.md) en cada celda. Es donde se
hace la comparación a la misma edad.

## La tabla y la curva muestran lo mismo

La tabla de cohortes pone una fila por cohorte y una columna por período desde la entrada, no por
fecha de calendario. Las cohortes nuevas todavía no vivieron los períodos tardíos, y la tabla toma
forma de triángulo. Se lee de tres formas: una fila muestra cómo decae una cohorte, una columna
compara las cohortes a la misma edad y una diagonal junta las cohortes en una misma fecha de
calendario.

La curva de retención dibuja cada fila como línea. Su forma es lo que importa: si se aplana, hay
un grupo para el que el producto tiene valor sostenido; si cae hacia cero, con el tiempo se van
todos. Un gráfico de usuarios activos no reemplaza a ninguna de las dos, porque mezcla todas las
cohortes.

## Armarla a mano

Cuando la herramienta de analítica no da la tabla, o se quiere controlar la definición, se calcula
desde una tabla de eventos con SQL o una planilla. Antes se escriben cuatro decisiones: el evento
de entrada, el evento de retorno, la granularidad y la forma de contar el retorno.

## Las tres notas de lectura

- [Tabla de cohortes](tabla-de-cohortes.md) — cómo se lee el triángulo por fila, columna y diagonal.
- [Curva de retención](curva-de-retencion.md) — qué dice la forma de la curva: si se aplana o cae a cero.
- [Armar una tabla de cohortes](armar-una-tabla-de-cohortes.md) — los pasos para calcularla desde una tabla de eventos.
