---
resumen: >-
  Un centro de costo es una parte de la empresa cuyo responsable responde solo por los costos; junto con los centros de ingreso, de utilidad y de inversión forma la contabilidad por responsabilidad, que reparte costos indirectos entre áreas y se lleva como dimensión de cada movimiento.
estado: borrador
estabilidad: semi
fuentes:
  - "OpenStax, Principles of Accounting, Volume 2: Managerial Accounting (2019), sección 9.3: https://openstax.org/books/principles-managerial-accounting/pages/9-3-describe-the-types-of-responsibility-centers"
  - "OpenStax, ídem, sección 9.4: https://openstax.org/books/principles-managerial-accounting/pages/9-4-describe-the-effects-of-various-decisions-on-performance-evaluation-of-responsibility-centers"
  - "Lumen Learning (SUNY), Managerial Accounting, Step Method of Allocation: https://courses.lumenlearning.com/suny-managacct/chapter/step-method-of-allocation/"
  - "Robert S. Kaplan, One Cost System Isn't Enough, Harvard Business Review, enero de 1988: https://eclass.aueb.gr/modules/document/file.php/LOXR285/Harvard%20Business%20Review%20-%20One%20Cost%20System%20isn%27t%20Enough.pdf"
  - "Documentación de producto de dos sistemas de gestión sobre plan de cuentas, dimensiones financieras y contabilidad analítica (citada en Contabilidad/.investigacion/contabilidad-de-gestion.md, sección 5)"
  - "Contabilidad/.investigacion/contabilidad-de-gestion.md"
aliases: [centro de responsabilidad, contabilidad por responsabilidad, centro de utilidad, centro de beneficio, centro de inversión, prorrateo, reparto de costos indirectos, método escalonado, precio de transferencia, contabilidad analítica, dimensión, cost center, profit center, investment center, responsibility accounting, step-down allocation, transfer pricing, analytic accounting, financial dimension]
creado: 2026-11-27
revisado:
---

# Centros de costo

Un centro de costo es una parte de la empresa cuyo responsable responde solo por los costos; junto con los centros de ingreso, de utilidad y de inversión forma la contabilidad por responsabilidad, que reparte costos indirectos entre áreas y se lleva como dimensión de cada movimiento.

La contabilidad por responsabilidad dice quién responde por cada número. El [presupuesto](presupuesto.md) se arma y se compara por centro, y los [sistemas de costeo](sistemas-de-costeo.md) usan el reparto entre centros para llegar al costo de cada producto.

## Cuatro tipos de centro según lo que se le pide al responsable

Según OpenStax (sección 9.3), la contabilidad por responsabilidad asigna cada segmento de la empresa a una persona o un grupo que responde por él. El tipo de centro depende de qué se le pide a esa persona:

| Centro | El responsable responde por | Ejemplo de Apparel World (OpenStax 9.3) |
|---|---|---|
| De costo | los costos | limpieza: gastó US$ 19.725 contra US$ 18.745 presupuestados, US$ 980 (5,2 %) de más |
| De ingreso | los ingresos | |
| De utilidad | ingresos y costos | ropa de niños: ganó US$ 32.647 contra US$ 28.756 presupuestados, US$ 3891 (13,5 %) de más |
| De inversión | la utilidad y el capital invertido | retorno sobre la inversión del 25,9 % en ropa de niños (US$ 3891 ÷ US$ 15.000) y del 3,9 % en ropa de mujeres (US$ 2533 ÷ US$ 65.000) |

La regla que ordena la evaluación es la de controlabilidad: según OpenStax (sección 9.4), a cada responsable se lo evalúa solo por las decisiones que controla. Los costos que le asignan desde otras áreas no los controla y no deberían pesar en su evaluación.

## Repartir los costos de los departamentos de servicio

Los departamentos de servicio (mantenimiento, administración, sistemas) no fabrican ni venden; sus costos se reparten entre los departamentos operativos para llegar al costo completo. Hay tres métodos, según el curso de Lumen Learning y los títulos de sus capítulos (solo se leyó el escalonado):

- Directo: reparte cada servicio solo entre los operativos e ignora lo que los servicios se prestan entre sí.
- Escalonado: reparte los servicios en orden, a los operativos y a los servicios que siguen; lo que ya se repartió no vuelve.
- Recíproco: reconoce los servicios cruzados en las dos direcciones y se resuelve con ecuaciones simultáneas.

El ejemplo del método escalonado, de Lumen, empieza con cuatro departamentos:

| Departamento | Costo propio | Horas-máquina | Empleados |
|---|---|---|---|
| Mantenimiento (servicio) | US$ 8000 | 1000 | 100 |
| Administración (servicio) | US$ 4000 | 2000 | 200 |
| Operativo 1 | US$ 32.000 | 1500 | 250 |
| Operativo 2 | US$ 36.000 | 2500 | 150 |

Primer paso: mantenimiento se reparte por horas-máquina de los otros tres, US$ 8000 ÷ 6000 = US$ 1,3333 por hora. A administración le tocan US$ 2667, al operativo 1 US$ 2000 y al operativo 2 US$ 3333. Segundo paso: administración, que ahora suma US$ 4000 + US$ 2667 = US$ 6667, se reparte por empleados de los operativos (400): US$ 4167 al operativo 1 y US$ 2500 al operativo 2. Resultado final: operativo 1, US$ 38.167; operativo 2, US$ 41.833. Suman US$ 80.000, lo mismo que los cuatro costos de partida: el reparto mueve costos entre departamentos sin crearlos ni perderlos.

El orden importa, porque el primer servicio que se reparte le pasa costo al segundo y no al revés. Para quien construye un sistema, la elección del método es una elección de algoritmo (inferencia de la base): el directo se resuelve en una pasada, el escalonado en cadena y el recíproco como sistema de ecuaciones. En los tres, la regla de reparto (base, porcentajes, orden) es un dato que cambia con el tiempo y conviene guardar con su vigencia.

## Precios de transferencia entre centros de la misma empresa

Cuando un segmento le «vende» a otro de la misma empresa, el precio de esa venta interna es un precio de transferencia. Según OpenStax (sección 9.4), hay tres enfoques: precio de mercado, precio basado en el costo (variable, total o costo más un margen) y precio negociado entre las dos partes. En el ejemplo de Regal Paper, la división papel puede transferir a US$ 12 (lo que cobra afuera) o a costo más 20 %, US$ 8 × 120 % = US$ 9,60. Sin capacidad ociosa, según la fuente, el precio pasa a ser el costo más el margen de contribución: US$ 8 + US$ 4 = US$ 12. El precio elegido mueve utilidad de un centro al otro sin cambiar la de la empresa (inferencia de la base), y por eso pesa en la evaluación de cada responsable.

## Por qué los centros de costo van en dimensiones y no en el plan de cuentas

En la documentación de los dos productos de gestión revisados, no se crea una cuenta contable por centro de costo. El [plan de cuentas](../Registro/plan-de-cuentas.md) se diseña para los informes a las autoridades y a los dueños, y lo condicionan la norma y el país. El centro de costo, el departamento o el proyecto se cargan como dimensiones (etiquetas adicionales) en cada movimiento: una cuenta de gastos puede llevar a la vez departamento, centro de costo y propósito, y un mismo comprobante puede repartir su importe entre varios centros por porcentajes.

Ninguna fuente de contabilidad de gestión leída lo establece como regla; lo sostiene la documentación de productos de software, y es la práctica de esos productos. La razón de fondo es inferencia de la base a partir de Kaplan (1988): el plan de cuentas sirve a la función regulada, la de informar afuera, y la gestión necesita cortes que cambian con la organización. Con dimensiones, reorganizar los departamentos no obliga a tocar las cuentas ni los saldos legales, y el mismo gasto se puede mirar por centro, por proyecto y por producto a la vez.

Para el registro, eso pide tres cosas (inferencia de la base): que cada movimiento pueda llevar sus dimensiones, que se pueda exigir una dimensión en ciertas cuentas (un gasto sin centro no entra en ningún presupuesto) y que el reparto por porcentajes quede guardado junto al movimiento. El modelo técnico está en [registro de movimientos](../../Bases-de-datos/Modelos-de-datos/registro-de-movimientos.md).

> [!NOTE]
> Sin fuente todavía: una fuente de contabilidad (un libro de texto o un organismo profesional), independiente de la documentación de productos, que trate las dimensiones frente al plan de cuentas.
