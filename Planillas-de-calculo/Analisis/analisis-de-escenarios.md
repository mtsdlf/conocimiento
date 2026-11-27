---
resumen: >-
  El análisis de escenarios prueba qué pasaría con un resultado (margen, ganancia, stock) si cambian
  los supuestos de la planilla: Buscar objetivo encuentra la entrada que da un resultado buscado,
  Tabla de datos y el Administrador de escenarios comparan varias combinaciones, y Solver optimiza
  con restricciones.
estado: borrador
estabilidad: estable
fuentes:
  - "Microsoft, Introduction to What-If Analysis: https://support.microsoft.com/en-US/excel/introduction-to-what-if-analysis"
  - "Microsoft, Define and solve a problem by using Solver: https://support.microsoft.com/en-us/office/define-and-solve-a-problem-by-using-solver-5d1a388f-079d-43ac-a7eb-f63e45925040"
  - "Google Workspace Updates, Goal Seek add-on for Sheets (2019-10-09): https://workspaceupdates.googleblog.com/2019/10/goal-seek-addon-sheets9.html"
  - "Google Workspace Marketplace, SolveSheet: https://workspace.google.com/marketplace/app/solvesheet/678357015177"
aliases: [what-if analysis, análisis de hipótesis, análisis Y si, qué pasaría si, Goal Seek, Buscar objetivo, Data Table, Tabla de datos, Scenario Manager, Administrador de escenarios, Solver]
creado: 2026-11-27
revisado:
---

# Análisis de escenarios

El análisis de escenarios prueba qué pasaría con un resultado (margen, ganancia, stock) si cambian
los supuestos de la planilla: Buscar objetivo encuentra la entrada que da un resultado buscado,
Tabla de datos y el Administrador de escenarios comparan varias combinaciones, y Solver optimiza
con restricciones.

Todas estas herramientas cambian celdas de entrada y miran una celda de resultado. Por eso
necesitan una planilla con los supuestos separados en celdas propias (precio, costo, unidades), como
pide [entradas, cálculo y salidas](../Diseno-de-planillas/entradas-calculo-salidas.md): si el precio
está escrito dentro de una fórmula, no hay celda que variar. El modelo financiero que suele estar
detrás (costos, punto de equilibrio, plan) está en [Finanzas](../../Emprender/Finanzas/finanzas.md).

## Cuatro herramientas, cuatro preguntas

En Excel, las tres primeras están juntas en el menú What-If Analysis de la pestaña Data. Solver es
otra herramienta: un complemento aparte. Microsoft fija un límite para cada una, y los límites dicen
cuándo usar cuál:

| Herramienta | Pregunta | Límite según Microsoft |
|---|---|---|
| Buscar objetivo (Goal Seek) | ¿qué precio me da un margen del 30 %? | "Goal Seek works with only one variable input value." |
| Tabla de datos (Data Table) | ¿cómo cambia la ganancia con cinco precios y cuatro volúmenes? | "A Data Table cannot accommodate more than two variables." |
| Administrador de escenarios (Scenario Manager) | ¿cómo queda el año en el caso optimista, el probable y el pesimista? | "A Scenario can have multiple variables, but it can only accommodate up to 32 values." |
| Solver | ¿cuánto produzco de cada producto para ganar lo máximo con la materia prima que tengo? | "You can specify up to 200 variable cells" |

La Tabla de datos de esta nota es una grilla de resultados y no tiene relación con la
[tabla estructurada](../Datos-en-la-planilla/tabla-estructurada.md) ni con la
[tabla dinámica](tabla-dinamica.md).

## Buscar objetivo: una entrada, un resultado buscado

Buscar objetivo trabaja al revés de una fórmula. La fórmula va del precio al margen; Buscar objetivo
parte del margen que se quiere y prueba valores de una sola celda (el precio) hasta llegar. Sirve
para preguntas de un número: el precio que cubre los costos, las unidades que hay que vender para
llegar al punto de equilibrio, la cuota que entra en un presupuesto.

Su límite es ese: una sola entrada. Si la pregunta es "qué precio y qué volumen", ya no alcanza.

## Tabla de datos y escenarios: comparar varias combinaciones

La Tabla de datos calcula el resultado para muchos valores de una o dos entradas y los muestra en una
grilla: precios en las filas, volúmenes en las columnas, ganancia en cada cruce. Se ve de una vez
dónde la ganancia pasa de negativa a positiva. Más de dos variables no entran.

El Administrador de escenarios guarda juegos de valores con nombre (optimista, probable, pesimista)
sobre varias celdas de entrada y arma un resumen que los compara. Admite muchas variables, pero no
más de 32 valores en total por escenario. Según una guía de terceros, sin confirmar con Microsoft,
el informe de resumen no se actualiza solo después de editar los escenarios: hay que generarlo de
nuevo.

> [!NOTE]
> Sin fuente todavía: el Administrador de escenarios y la Tabla de datos paso a paso, con un ejemplo
> leído en la fuente.

## Solver: optimizar con restricciones

Solver busca el mejor valor de una celda objetivo (máximo, mínimo o un valor dado) cambiando varias
celdas de decisión, sin pasarse de unas restricciones. Un caso de negocio chico: cuántas unidades
hacer de cada producto para ganar lo máximo, sin usar más harina de la que hay en stock ni más horas
de horno de las disponibles.

Lo que dice Microsoft sobre cómo se usa:

- **Hay que activarlo**: es un complemento. En Excel para la web no hay complementos, así que hace
  falta la versión de escritorio.
- **La celda objetivo** debe contener una fórmula, y se pueden marcar "up to 200 variable cells".
- **Restricciones**: <=, =, >=, int (entero), bin (binario, 0 o 1) y dif (todos distintos). Las tres
  últimas solo se aplican sobre celdas de decisión.
- **Tres métodos**: GRG Nonlinear, para problemas "smooth nonlinear"; Simplex LP, para problemas
  "linear"; y Evolutionary, para los "non-smooth".

Con precios y costos unitarios fijos, la ganancia es una suma de cantidades por márgenes, así que el
problema del ejemplo es lineal; elegir Simplex LP para él es inferencia de esta nota, no algo que diga
Microsoft.

## Qué hay en Google Sheets

En Sheets no se encontró ninguna de estas herramientas como función propia. Google anunció el 9 de octubre de
2019 un complemento de Buscar objetivo (Goal Seek) para Sheets, según el resumen del anuncio; no se
encontró una versión nativa posterior. No se encontró un Solver de Google; lo que aparece son complementos de terceros en el
Marketplace de Workspace, con límites distintos. Según sus fichas, Optimization Solver admite hasta
50 variables de decisión, y SolveSheet cobra su solver no lineal y resuelve el modelo en un servicio
externo.

> [!WARNING]
> Un complemento de terceros puede mandar los datos de la hoja fuera de ella para resolverlos, como
> declara SolveSheet. Si la planilla tiene costos, márgenes o datos de clientes, conviene leer qué
> permisos pide el complemento antes de instalarlo, o resolver el modelo en Excel.

La Tabla de datos de dos variables se puede imitar en Sheets con fórmulas que calculen el resultado
para cada cruce de una grilla, aunque eso es una inferencia y no una función documentada.

## Qué leer

"Introduction to What-If Analysis" de Microsoft; fijate en los tres límites (32 valores, dos
variables, una variable), porque dicen cuándo pasar de una herramienta a otra. Para Solver, "Define
and solve a problem by using Solver", en la parte de los tres métodos y el tope de 200 celdas. Para
Sheets no hay un recurso de Google que cubra el tema.
