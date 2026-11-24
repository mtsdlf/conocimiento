# Rubros: conteo propio de locales y empresas con datos abiertos (consulta 2026-11-22)

Hecho por quien coordina la vertical Rubros, para dar a cada rubro un piso de abajo hacia arriba. Lectura [L]: los CSV se descargaron enteros y se sumaron con un script; las sumas son propias. Mismo método que `b2b-conteo-propio.md`.

## Fuentes

| # | Fuente | Qué es | Calif. |
|---|---|---|---|
| R1 | CEP XXI, Ministerio de Economía, «Distribución geográfica de los establecimientos productivos», https://cdn.produccion.gob.ar/cdn-cep/establecimientos-productivos/Datos_por_departamento_y_actividad.csv, con el diccionario https://cdn.produccion.gob.ar/cdn-cep/establecimientos-productivos/actividades_establecimientos.csv | Locales (establecimientos) de empresas con al menos un asalariado registrado, y su empleo, por actividad CLAE a 6 dígitos; años 2021 y 2022 | A2 (oficial; método no leído) |
| R2 | CEP XXI, «Empleadores del sector privado que declararon trabajadores (CLAE a 3 dígitos)», https://cdn.produccion.gob.ar/cdn-cep/datos-por-actividad/empleadoras/empleadoras_privadas_por_clae3.csv | Empresas empleadoras por subgrupo CLAE, serie mensual hasta 2023-10 | A1 |

Límite de las dos: cuentan solo a quien tiene empleados registrados. Los monotributistas sin empleados, que en comercio son mayoría por CUIT (ver `tamano-local-y-gestion.md`), quedan afuera.

## Locales de empresas empleadoras, 2022 (2021 entre paréntesis)

| Rubro | Clases CLAE sumadas | Locales 2022 | Puestos 2022 |
|---|---|---|---|
| Gastronomía | 561011, 561012, 561013, 561014, 561019, 561020, 561030, 561040 | 25.134 (21.685) | 179.657 |
| Autopartes al por menor | 453210, 453220, 453291, 453292 | 6.541 (6.263) | 23.835 |
| Ferretería y construcción al por menor | 475210 a 475290 | 14.102 (13.312) | 60.014 |
| Farmacia | 477310 | 10.385 | 52.366 |
| Óptica y fotografía | 477410 | 2.225 | 5.826 |
| Indumentaria | 4771xx | 17.894 (16.433) | — |
| Calzado | 477220, 477230 | 3.898 | 14.701 |
| Alimentos en comercios especializados | 4721xx | 25.257 (23.713) | — |
| Mascotas y veterinaria | 477470 | 1.913 | 5.005 |
| Muebles, colchones | 475410, 475420 | 2.528 | 7.774 |

Detalle por clase, 2022 (locales; puestos):

- Gastronomía: con servicio de mesa 561019 10.350 (72.077); restaurantes y cantinas sin espectáculo 561011 4.888 (42.152); fast food y al paso 561013 3.273 (36.778); heladerías 561030 2.962 (11.606); comidas para llevar (rotiserías, casas de empanadas) 561020 1.836 (5.230); bares 561014 1.222 (7.169); con espectáculo 561012 587 (4.373); ambulantes 16. Fuera de la suma: comidas para empresas y eventos 562010 2.086; cantinas en empresas 462; comidas n.c.p. 469.
- Autopartes: partes nuevas n.c.p. 453291 4.665 (14.785); cámaras y cubiertas 453210 1.462 (7.723); baterías 453220 309 (930); usados 453292 105 (397). Fuera de la suma: al por mayor 453100 2.146 (15.436); motos y sus partes 454010 1.325 (6.552).
- Ferretería y construcción: ferretería y materiales eléctricos 475230 4.950 (15.520); materiales de construcción n.c.p. 475290 4.542 (27.370); pinturas 475240 2.175 (8.523); maderas 475220 776; plomería y gas 475250 535; aberturas 475210 467; cristales y cerramientos 475260 388; revestimientos 475270 269. Fuera: al por mayor de ferretería 466330 1.399 y de artículos para la construcción 466399 1.132 (ver `b2b-conteo-propio.md`).
- Alimentos especializados: panaderías 472171 5.162; n.c.p. 472190 5.205; carnicerías 472130 4.638; almacén y dietética 472120 4.182; verdulerías 472160 1.694; granja 472140 1.494; fiambrerías 472112 1.107.
- Otros: perfumería 477320 2.614; ortopedia 477330 857.

## Empresas empleadoras por subgrupo (R2), octubre

| Subgrupo | 2019 | 2023 |
|---|---|---|
| 453 Partes y accesorios de vehículos (mayor y menor) | 6.925 | 7.414 |
| 454 Motocicletas | 1.019 | 1.109 |
| 472 Alimentos, bebidas y tabaco en comercios especializados | 22.329 | 23.598 |
| 475 Artículos de uso doméstico (incluye ferretería, construcción, electro y muebles) | 18.989 | 20.116 |
| 477 Otros minoristas especializados (incluye ropa, farmacia, óptica) | 40.195 | 40.500 |
| 561 Expendio de comidas y bebidas | 19.600 | 20.117 |
| 562 Comidas para empresas y eventos | 1.487 | 1.534 |

Cuenta propia: en gastronomía hay 1,25 locales por empresa (25.134 / 20.117, años distintos: 2022 y 2023), lo que es coherente con un rubro de un solo local con algunas cadenas. La suba de 21.685 a 25.134 locales entre 2021 y 2022 (+16%) es la salida de la pandemia, no una tendencia (inferencia).

## Corrección posterior

La pasada de refutación (`rubros-refutacion.md`) recalculó las sumas: los puestos de ferretería y construcción son 60.014 (se había escrito 53.044) y los de gastronomía 179.657 (se había escrito 179.687). Se corrigieron en la tabla de arriba; los locales coinciden.
