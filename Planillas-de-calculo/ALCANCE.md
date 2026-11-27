---
tema: Planillas de cálculo
para: usar una planilla para trabajar en un negocio (costos, stock, ventas, clientes) sin que se rompa; lo leen Matías y Fer y quien arme planillas para un comercio
nivel: se da por sabido abrir una planilla y escribir una fórmula simple
escuela:
fuera:
  - "Modelado financiero en profundidad (flujo de caja, valuación): Emprender/Finanzas/ para lo conceptual"
  - "Programación de macros en detalle: solo qué son, cuándo convienen y por dónde empezar"
  - "Análisis estadístico y visualización en general: Datos/"
fuentes: []
preguntas:
  - "¿Cómo armo una planilla de costos que otro pueda tocar sin romperla?"
  - "Tengo dos planillas con clientes y quiero cruzarlas: ¿BUSCARV, BUSCARX o Power Query?"
  - "Tengo un año de ventas en filas: ¿cómo veo cuánto vendí por mes y por producto?"
  - "La fórmula da #N/A o un número raro: ¿cómo encuentro el error?"
  - "¿Excel o Google Sheets para un comercio chico, y qué cambia entre los dos?"
  - "¿Cuándo una planilla dejó de alcanzar y hay que pasar a una base de datos?"
aprobado: 2026-11-27
---

# Alcance: Planillas de cálculo

Planillas de cálculo explica cómo se usa una planilla (Excel, Google Sheets) para trabajar en un
negocio: el modelo de celdas, las fórmulas, los datos, el análisis, el diseño que no se rompe y la
automatización justa. Salió de una conversación del 2026-11-27, con uso general en un negocio y
Excel y Sheets a la par.

## Árbol

```
Planillas-de-calculo/
  planillas-de-calculo.md     el todo, con «Qué leer según lo que estés haciendo»
  cuando-pasar-a-una-base     el puente hacia Bases-de-datos
  ficha: aplicaciones de planillas   Excel, Google Sheets, LibreOffice Calc; límites y versiones
  Modelo-de-la-planilla/      cómo piensa una planilla
    celda-y-referencia        relativas, absolutas, rangos con nombre
    tipos-de-dato             número, texto, fecha como número; formato contra valor
    errores-de-formula        #N/A, #¡REF!, #¡VALOR!, circulares; recálculo
  Formulas/
    funciones-logicas         SI, Y, O, SI.CONJUNTO, SI.ERROR
    funciones-de-busqueda     BUSCARV, INDICE y COINCIDIR, BUSCARX
    sumar-y-contar-con-condiciones   SUMAR.SI.CONJUNTO, CONTAR.SI.CONJUNTO
    texto-y-fechas            partir, unir, limpiar texto; calcular con fechas
    matrices-dinamicas        FILTRAR, ORDENAR, UNICOS, LET, LAMBDA
    ficha: equivalencias de funciones   castellano e inglés, Excel y Sheets
  Datos-en-la-planilla/
    datos-ordenados           una fila, un registro; una columna, una variable
    tabla-estructurada        tablas con nombre que crecen solas
    validacion-de-datos       listas desplegables y reglas
    power-query               importar, limpiar y combinar sin fórmulas
  Analisis/
    tabla-dinamica            resumir por categorías y períodos
    graficos-en-la-planilla   qué gráfico y cómo se arma
    analisis-de-escenarios    qué pasaría si, buscar objetivo, Solver
  Diseno-de-planillas/
    entradas-calculo-salidas  la estructura que separa supuestos de cálculos
    errores-en-planillas      cuánto fallan las planillas, con casos y estudios
    revisar-una-planilla      rastrear precedentes, auditar antes de confiar
  Automatizar-y-compartir/    macros y scripts, y trabajar varios sobre el mismo archivo
    macros                    VBA y Office Scripts en Excel
    apps-script               automatizar Google Sheets
    compartir-y-colaborar     permisos, coautoría, historial de versiones
  Fundamentos/
    glosario-de-planillas
    fuentes-de-planillas
```

## Supuestos

- Los nombres de funciones van en castellano con el inglés al lado, porque la persona trabaja en
  castellano y la documentación y los foros suelen estar en inglés.
- Limpieza de datos y elegir un gráfico en general están en Datos (otra rama al 2026-11-27); acá va
  lo propio de la planilla y se enlaza cuando las dos ramas estén en `main`.
- La vertical de automatización se llama `Automatizar-y-compartir/` porque compartir y colaborar no es
  automatizar, pero no da para una vertical propia (lo señaló la investigación).
- El límite de Google Sheets es de 20 millones de celdas desde septiembre de 2026, no los 10 millones
  que se suponían al planear.
