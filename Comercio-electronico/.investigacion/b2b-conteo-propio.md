# B2B: conteo propio de empresas y locales mayoristas con datos abiertos (consulta 2026-11-22)

Hecho por quien escribe la vertical, para llenar el hueco 1 de `b2b-cifras.md` (cuántas empresas de la división 46). Lectura [L]: los CSV se descargaron enteros y se sumaron con un script; las sumas son propias.

## Fuentes

| # | Fuente | Qué es | Calif. |
|---|---|---|---|
| D1 | CEP XXI, Ministerio de Economía, «Empleadores del sector privado que declararon trabajadores (CLAE a 3 dígitos)», https://cdn.produccion.gob.ar/cdn-cep/datos-por-actividad/empleadoras/empleadoras_privadas_por_clae3.csv (dataset https://datos.produccion.gob.ar/dataset/cantidad-de-empleadores-que-declararon-trabajadores-por-sector-de-actividad) | Serie mensual 2007-01 a 2023-10 (último mes del archivo) de empresas privadas con al menos un asalariado registrado en el SIPA, por subgrupo CLAE | A1 (oficial; cruza con F1 de `b2b-cifras.md` en el total de empresas) |
| D2 | Ídem, CLAE a 2 dígitos: https://cdn.produccion.gob.ar/cdn-cep/datos-por-actividad/empleadoras/empleadoras_privadas_por_clae2.csv | Igual, por división | A1 |
| D3 | CEP XXI, «Distribución geográfica de los establecimientos productivos», datos por departamento y actividad: https://cdn.produccion.gob.ar/cdn-cep/establecimientos-productivos/Datos_por_departamento_y_actividad.csv, con su diccionario de actividades https://cdn.produccion.gob.ar/cdn-cep/establecimientos-productivos/actividades_establecimientos.csv y metodología https://cdn.produccion.gob.ar/cdn-cep/establecimientos-productivos/Metodologia_establecimiento_productivos.pdf (metodología no leída) | Locales (establecimientos) de empresas empleadoras y su empleo, años 2021 y 2022, por actividad CLAE a 6 dígitos | A2 |

## Empresas empleadoras (D1, D2)

Octubre de cada año, empresas privadas con asalariados registrados.

| División | 2019 | 2022 | 2023 |
|---|---|---|---|
| Total de la economía | 554.529 | 540.167 | 543.769 |
| 46 Comercio al por mayor | 32.055 | 33.848 | 34.525 |
| 47 Comercio al por menor | 106.741 | 106.367 | 109.418 |
| 45 Vehículos (venta y reparación) | 16.343 | 16.235 | 16.538 |
| Industria manufacturera (10 a 33) | 52.492 | 52.495 | 53.284 |
| Alimentos y bebidas (10 y 11) | 13.345 | 13.534 | 13.913 |

Subgrupos de la división 46, octubre de 2023 (2019 y 2021 entre paréntesis). Los nombres de cada subgrupo salen de las actividades de 6 dígitos del diccionario de D3.

| Subgrupo | Qué incluye (de las actividades de 6 dígitos) | Empresas 2023 |
|---|---|---|
| 461 | en comisión o consignación (cereales, ganado, combustibles) | 3.302 (3.198; 3.222) |
| 462 | materias primas agropecuarias y animales vivos | 800 (717; 779) |
| 463 | alimentos, bebidas y tabaco (incluye golosinas para kioscos y supermercados mayoristas) | 8.896 (7.997; 8.281) |
| 464 | artículos de uso doméstico y personal (ropa, calzado, farmacia, perfumería, librería, limpieza, juguetes, electro) | 8.449 (7.927; 7.903) |
| 465 | máquinas, equipos e informática | 4.227 (4.038; 4.131) |
| 466 | especializada: ferretería, construcción, combustibles, metales, químicos, agroinsumos | 5.671 (5.215; 5.399) |
| 469 | no especializada (mercancías n.c.p.) | 3.180 (2.963; 3.045) |
| 463 a 469 | lo que se vende a comercios e industrias, sin el agro en consignación | 30.423 (28.140; 28.759) |

Cuentas propias: la división 46 creció 7,7% en empresas entre octubre de 2019 y octubre de 2023, mientras el total de la economía bajó 1,9%. La razón entre empresas mayoristas y minoristas es 1 a 3,2.

## Locales (D3), 2022

Toda la división 46: 46.251 locales y 389.728 puestos (2021: 44.472 y 371.670). Promedio 8,4 puestos por local (cuenta propia). Por subgrupo, 2022: 461 5.397; 462 1.200; 463 11.152; 464 11.438; 465 5.588; 466 7.454; 469 4.022.

Las 12 actividades de 6 dígitos con más locales en 2022 (locales; puestos):

| Actividad | Locales | Puestos |
|---|---|---|
| 469090 mercancías n.c.p. | 3.853 | 27.917 |
| 463199 productos alimenticios n.c.p. | 2.609 | 21.937 |
| 461011 cereales y oleaginosas en comisión | 1.876 | 26.642 |
| 466330 ferretería y materiales eléctricos | 1.399 | 9.342 |
| 464310 productos farmacéuticos (droguerías) | 1.278 | 25.641 |
| 464129 prendas y accesorios de vestir | 1.214 | 4.660 |
| 465990 máquinas y equipos n.c.p. | 1.187 | 8.961 |
| 463140 frutas y hortalizas frescas | 1.167 | 11.823 |
| 466399 artículos para la construcción | 1.132 | 9.943 |
| 463160 chocolates, golosinas y productos para kioscos | 1.007 | 11.133 |
| 464320 cosméticos y perfumería | 941 | 8.535 |
| 463219 bebidas alcohólicas | 856 | 11.317 |

Otras: 464920 productos de limpieza 675 locales; 463220 bebidas sin alcohol 623; 463180 supermercados mayoristas de alimentos 618 locales con 16.815 puestos; 465100 informática 611.

## Cruce con el OEDE (D4), 2024

D4: Ministerio de Trabajo, OEDE, «Estadísticas sobre empresas y empleo asalariado registrado por sector económico», serie anual 1996-2024: https://www.argentina.gob.ar/sites/default/files/nacional_serie_empresas_2.xlsx, enlazada desde https://www.argentina.gob.ar/trabajo/estadisticas/oede-estadisticas-nacionales (descargado y leído celda por celda; A1). Misma fuente administrativa (SIPA), pero empresas activas en algún momento del año y clasificación CIIU rev. 3.

| Rama CIIU rev. 3 | 2022 | 2023 | 2024 |
|---|---|---|---|
| 51 Comercio al por mayor, total | 34.395 | 35.050 | 35.379 |
| grandes | 1.610 | 1.714 | 1.744 |
| medianas | 2.911 | 2.941 | 3.035 |
| pequeñas | 10.381 | 10.742 | 10.832 |
| micro | 19.493 | 19.653 | 19.768 |
| 52 Comercio al por menor | 112.230 | 115.080 | 113.303 |
| 15 Alimentos (industria) | 14.305 | 14.741 | 14.795 |

Cuadro 3 (2 dígitos) y Cuadro 9 (2 dígitos por tamaño). El criterio de tamaño es el del OEDE (no se leyó su definición). Cuenta propia: en 2024, el 95% de las empresas mayoristas son micro, pequeñas o medianas (33.635 de 35.379) y el 56% son micro.

Cruce: OEDE 2023 da 35.050 mayoristas y el CEP XXI de octubre de 2023, 34.525. Coinciden en un 1,5%, y la diferencia es esperable porque el OEDE cuenta a las activas en cualquier trimestre del año.

## Cruces

- Supermercados mayoristas: 618 locales en D3 (todas las empresas empleadoras con esa actividad principal) contra 188 bocas del panel de INDEC en agosto de 2026 (30 empresas grandes). No se contradicen: el panel de INDEC es de cadenas; D3 cuenta también a los autoservicios mayoristas chicos y es de 2022.
- Golosinas: 1.007 locales de distribuidoras de golosinas y productos para kioscos (D3, 2022) para unos 90.000 kioscos registrados (NielsenIQ, 2024): unos 90 kioscos por local mayorista, cuenta propia de orden de magnitud.
- Total de empresas: 543.769 en octubre de 2023 (D2) contra 536.000 en 2021 (F1 de `b2b-cifras.md`): mismo universo SIPA, coinciden.

## Huecos

- Mayoristas sin empleados registrados (monotributistas y autónomos): D1 y D3 no los cuentan. El Censo Económico 2020/21 contó 1.138.346 monotributistas en todas las actividades, sin apertura leída.
- Tamaño por empleo dentro de la división 46: no está en D1; solo el promedio por local de D3.
- El archivo D1 termina en octubre de 2023; no se encontró una versión más nueva.
- Las empresas se clasifican por su actividad principal: un fabricante que vende a comercios cuenta como industria, y una cadena minorista con un mayorista adentro cuenta como minorista.
