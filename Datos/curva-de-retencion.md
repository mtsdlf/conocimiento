---
tipo: concepto
resumen: >-
  Una curva de retención grafica, para una cohorte, el porcentaje que sigue activo en cada
  período desde su entrada; su forma (si cae a cero o se aplana) dice si el producto retiene a
  alguien a largo plazo.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - https://www.brucehardie.com/papers/021/sbg_2006-05-30.pdf
  - https://www.itl.nist.gov/div898/handbook/apr/section2/apr215.htm
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC5045282/
aliases: [retention curve, curva de supervivencia]
parte_de: []
requiere: [tasa-de-retencion-por-cohorte]
relacionado: [tabla-de-cohortes]
---

# Curva de retención

Una curva de retención grafica, para una cohorte, el porcentaje que sigue activo en cada
período desde su entrada; su forma (si cae a cero o se aplana) dice si el producto retiene a
alguien a largo plazo.

## Por qué importa

Una curva que se aplana muestra que hay un grupo de usuarios para el que el producto tiene valor
sostenido. Una que cae hacia cero dice que con el tiempo se van todos, y que crecer en
adquisición solo llena un balde agujereado.

## Cómo funciona

El eje X es el período desde la entrada (día, semana, mes); el eje Y, la
[tasa de retención por cohorte](tasa-de-retencion-por-cohorte.md), que empieza en 100 %. Se dibuja
una curva por cohorte, o un promedio ponderado por tamaño. Casi siempre hay una caída fuerte al
principio, de gente que probó y no volvió, y después una pendiente más suave.

Entre dos cohortes, la curva que queda más arriba retiene mejor. La que se aplana antes o en un
nivel más alto indica un producto que encuentra antes a su público.

En estadística es una curva de supervivencia: la proporción que no se fue, en función del
tiempo. Las cohortes que todavía no llegaron a un período son datos censurados y se excluyen de
ese punto.

## Ejemplo

Cohorte de enero: 100 %, 35 %, 25 %, 22 %, 21 %, 21 %. La curva se aplana cerca de 21 %: uno de
cada cinco usuarios se queda.

## No confundir con

Un gráfico de usuarios activos en el tiempo (DAU o MAU) mezcla todas las cohortes. Puede subir
aunque cada curva de retención caiga a cero, si la adquisición crece más rápido.

## Relaciones

- Requiere: [Tasa de retención por cohorte](tasa-de-retencion-por-cohorte.md) — es lo que se grafica.
- Relacionado: [Tabla de cohortes](tabla-de-cohortes.md) — la misma información en forma de tabla.
