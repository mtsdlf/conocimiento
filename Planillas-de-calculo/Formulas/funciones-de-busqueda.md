---
resumen: >-
  Las funciones de búsqueda traen un dato de otra tabla a partir de una clave: el precio de un
  producto por su código, el nombre de un cliente por su CUIT. Hay tres formas de hacerlo,
  BUSCARV, INDICE con COINCIDIR y BUSCARX, y difieren en hacia dónde buscan, qué hacen si no
  encuentran y en qué versiones existen.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft, Función BUSCARV: https://support.microsoft.com/es-es/office/buscarv-función-buscarv-0bbc8083-26fe-4963-8ab8-93a18ad188a1 (según un resumen de la página)"
  - "Microsoft, VLOOKUP function: https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1 (según un resumen de la página)"
  - "Microsoft, Función BUSCARX: https://support.microsoft.com/es-es/office/buscarx-función-buscarx-b7fd680e-6d10-43e6-84f9-88eae8bf5929 (según un resumen de la página)"
  - "Microsoft, XLOOKUP function: https://support.microsoft.com/en-us/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929"
  - "Microsoft Excel Blog, Announcing XLOOKUP (2019-08-28): https://techcommunity.microsoft.com/blog/excelblog/announcing-xlookup/811376 (según un resumen)"
  - "Google, XLOOKUP: https://support.google.com/docs/answer/12405947 (según un resumen)"
  - "Exceljet, XLOOKUP function: https://exceljet.net/functions/xlookup-function (según un resumen)"
  - "Exceljet, INDEX function: https://exceljet.net/functions/index-function (según un resumen)"
  - "Planillas-de-calculo/.investigacion/modelo-y-formulas.md, sección 2.2; Planillas-de-calculo/.investigacion/posicion-contraria-y-fundamentos.md, B2"
aliases: [BUSCARV, VLOOKUP, BUSCARX, XLOOKUP, INDICE, INDEX, COINCIDIR, MATCH, buscar en otra tabla, lookup]
creado: 2026-11-27
revisado:
---

# Funciones de búsqueda

Las funciones de búsqueda traen un dato de otra tabla a partir de una clave: el precio de un
producto por su código, el nombre de un cliente por su CUIT. Hay tres formas de hacerlo,
BUSCARV, INDICE con COINCIDIR y BUSCARX, y difieren en hacia dónde buscan, qué hacen si no
encuentran y en qué versiones existen.

Es la operación que más se repite en una planilla de negocio: la lista de ventas tiene el código
del producto y la lista de precios tiene el precio, y hay que juntarlas. En una base de datos lo
mismo se hace con un [JOIN](../../Bases-de-datos/SQL/join.md); en la planilla, con una fórmula por
fila. Si las dos listas son archivos que llegan todos los meses, conviene juntarlas con
[Power Query](../Datos-en-la-planilla/power-query.md) en lugar de fórmulas.

## BUSCARV busca en la primera columna y devuelve hacia la derecha

BUSCARV (VLOOKUP) recorre la primera columna de un rango hasta encontrar el valor y devuelve lo
que está en la columna número N de ese rango. La sintaxis que da Microsoft es
`BUSCARV(valor_buscado, matriz_buscar_en, indicador_columnas, [ordenado])`; en una planilla en
castellano con coma decimal los argumentos se separan con `;`:

```
=BUSCARV(A2; Precios!A:C; 3; FALSO)
```

Trae, para el código de A2, lo que está en la tercera columna de la hoja Precios. Tiene cuatro
trampas, todas documentadas por Microsoft:

- **La coincidencia aproximada es la predeterminada.** Si se omite el cuarto argumento, BUSCARV
  "assumes the first column in the table is sorted" y, si no encuentra el valor exacto, devuelve
  el de la fila anterior sin avisar. Para buscar códigos, clientes o productos hay que poner
  `FALSO` (o 0) siempre.
- **Solo devuelve hacia la derecha.** La clave tiene que estar en la primera columna del rango.
  Si el código está en la columna C y el nombre en la B, BUSCARV no sirve.
- **El número de columna es fijo.** Si alguien inserta una columna en la lista de precios, el `3`
  sigue apuntando a la tercera, que ahora es otra. Si el número supera las columnas del rango, da
  #¡REF!.
- **Números guardados como texto y espacios de más** hacen que no encuentre el valor aunque se
  vea igual en pantalla. Es un problema de [tipos de dato](../Modelo-de-la-planilla/tipos-de-dato.md).

Cuando no encuentra el valor, BUSCARV da #N/A (en algunas páginas de Microsoft en castellano, #N/D); cómo leer ese error está en
[errores de fórmula](../Modelo-de-la-planilla/errores-de-formula.md).

## INDICE y COINCIDIR separan dónde buscar de qué devolver

COINCIDIR (MATCH) dice en qué posición de una columna está un valor; INDICE (INDEX) devuelve lo
que hay en una posición de otra columna. Juntas hacen lo que BUSCARV sin sus límites: buscan
hacia la izquierda, en dos direcciones (fila y columna) y con varios criterios. El ejemplo
literal de Exceljet, en inglés:

```
=INDEX(B5:E13,MATCH(G6,B5:B13,0),3)
```

En castellano, para traer el nombre (columna B) de un producto cuyo código está en la columna C:

```
=INDICE(Productos!B:B; COINCIDIR(A2; Productos!C:C; 0))
```

El `0` de COINCIDIR pide coincidencia exacta, igual que el `FALSO` de BUSCARV. Según Exceljet,
INDICE no es una función volátil, así que no recalcula de más (los volátiles están en
[errores de fórmula](../Modelo-de-la-planilla/errores-de-formula.md#el-recálculo-y-las-funciones-volátiles)).

## BUSCARX hace todo en una sola función

BUSCARX (XLOOKUP) recibe la columna donde buscar y la columna que devolver por separado, busca
exacto por defecto y deja decir qué mostrar si no encuentra. La sintaxis de Microsoft en
castellano es:

```
=BUSCARX(valor_buscado; matriz_buscada; matriz_devuelta; [si_no_se_encuentra]; [modo_de_coincidencia]; [modo_de_búsqueda])
```

Los modos de coincidencia son 0 exacta (predeterminado), -1 exacta o la menor siguiente, 1 exacta
o la mayor siguiente y 2 con comodines. Los de búsqueda son 1 desde el primero, -1 desde el
último, y 2 y -2 binaria, que exige la columna ordenada. Si no encuentra y falta el cuarto
argumento, da #N/A. Microsoft la recomienda en la página de BUSCARV porque "works in any direction
and returns exact matches by default".

```
=BUSCARX(A2; Productos!C:C; Productos!B:B; "Sin código")
```

Exceljet advierte tres cosas: devuelve un solo resultado (para traer todas las coincidencias está
FILTRAR, en [matrices dinámicas](matrices-dinamicas.md)); poner `""` en si_no_se_encuentra
esconde el #N/A y con él los códigos mal cargados; y las dos matrices de distinto tamaño dan
#¡VALOR!.

| | BUSCARV | INDICE + COINCIDIR | BUSCARX |
|---|---|---|---|
| Coincidencia por defecto | aproximada | la que diga COINCIDIR (0 = exacta) | exacta |
| Busca hacia la izquierda | no | sí | sí |
| Se rompe si se inserta una columna | sí | no | no |
| Qué muestra si no encuentra | #N/A | #N/A | #N/A o lo que diga el cuarto argumento |
| Existe en versiones viejas de Excel | sí | sí | no |

## El debate es de compatibilidad, no de potencia

> [!IMPORTANT]
> BUSCARX hace todo lo que hace INDICE con COINCIDIR en una fórmula más legible, y Microsoft la
> recomienda. El argumento a favor de seguir con INDICE y COINCIDIR es que BUSCARX no existe en
> Excel 2016 ni 2019: según la página de Microsoft, un libro con BUSCARX abierto en una de esas
> versiones muestra los resultados guardados, pero al volver a escribir la fórmula da #¿NOMBRE?.
> La misma página se contradice: su lista de versiones incluye Excel 2016 y 2019, y una nota dice
> "XLOOKUP is not available in Excel 2016 and Excel 2019". Exceljet la da para "Excel 2021+ and
> Excel 365". Qué versión tiene cada quien se resuelve en la
> [ficha de equivalencias](equivalencias-de-funciones.md).

La regla práctica que sale de ahí es una inferencia: si todos los que abren el archivo tienen
Microsoft 365 o Excel 2021 en adelante, o Google Sheets, BUSCARX; si el archivo circula entre
computadoras con versiones viejas, INDICE y COINCIDIR. BUSCARV queda para planillas heredadas,
siempre con `FALSO`.

> [!NOTE]
> Sin fuente todavía: los argumentos concretos de quienes defienden INDICE y COINCIDIR más allá
> de la compatibilidad (el hilo "XLOOKUP - don't take the bait" de Microsoft Tech Community no se
> leyó), y casos documentados de errores de BUSCARV en planillas de stock o precios.

## En Google Sheets las tres existen

Sheets tiene VLOOKUP, INDEX, MATCH y XLOOKUP. XLOOKUP llegó en el anuncio de Google Workspace del
24 de agosto de 2022 y su sintaxis es
`XLOOKUP(search_key, lookup_range, result_range, missing_value, match_mode, search_mode)`, con las
mismas opciones predeterminadas que en Excel. En Sheets no hay problema de versiones: todos usan
la misma, así que BUSCARX es la opción directa. Para traer el dato desde otro archivo de Sheets
hace falta IMPORTRANGE, que está en la [ficha de equivalencias](equivalencias-de-funciones.md).
