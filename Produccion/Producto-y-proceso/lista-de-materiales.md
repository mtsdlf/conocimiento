---
resumen: >-
  La lista de materiales dice qué componentes, y en qué cantidad, hacen falta para fabricar una cantidad base de un producto. Cada componente puede tener su propia lista, y la cadena de listas forma el árbol del producto, que el MRP explota y el costo estándar recorre nivel por nivel.
estado: borrador
estabilidad: estable
fuentes:
  - "Documentación de un sistema comercial, «Bill of materials (BOM)» y fórmulas (página del 2025-07-10): https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/bill-of-material-bom"
  - "Manual de Bill of Materials de un sistema abierto: https://docs.frappe.io/erpnext/user/manual/en/bill-of-materials"
  - "Documentación de listas de materiales de otro sistema abierto (v18.0), variantes y subproductos: https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/manufacturing/basic_setup/bill_configuration.html"
  - "Glosario de un sistema comercial, lista fantasma («Paraphrased from the APICS Dictionary, Eighth Edition»): https://docs.infor.com/csi/9.01.x/en-us/csbiolh/lsm1454143871331.html"
  - "Manual de listas de materiales de otro sistema comercial (fantasma, modelo y clase de opción): https://docs.oracle.com/cd/A60725_05/html/comnls/us/bom/bomov02.htm"
  - "IISE Magazine (2021-03), terminología IISE de «phantom assembly»: https://www.iise.org/iemagazine/2021-03/html/sanchez/sanchez.html"
  - "Ayuda de un sistema comercial, código de nivel más bajo (resumen del buscador): https://docs.infor.com/csb/9.01.x/en-us/csbiolh/mergedprojects/sl_invprod/fields/l/low_level_code_item_master_general.htm"
  - "Ayuda de otro sistema comercial, «Low-Level Code» (resumen del buscador): https://docs.oracle.com/en/applications/jd-edwards/supply-chain-manufacturing/9.2/eoarp/low-level-code.html"
  - "Ayuda de un sistema comercial, «Bills of Material: Cost Calculation» (factor de merma, resumen del buscador): https://help.myob.com.au/advanced/Docs/Published/UserGuide/BOM_Cost_Calculation.html"
  - "Ejemplo de lista indentada de una lámpara, paquete de investigación operativa (datos de entrada): https://support.sas.com/documentation/onlinedoc/or/ex_code/131/bom8.html"
  - "Solucionario de preguntas de discusión sobre MRP, curso IE 314, KSU: https://faculty.ksu.edu.sa/sites/default/files/mrp.pdf"
  - "Produccion/.investigacion/producto-y-proceso.md (2026-11-27), sección 1; costos.md, sección 1"
aliases: [lista de materiales, LdM, bill of materials, BOM, bill of material, estructura de producto, product structure, lista multinivel, multilevel BOM, lista explotada, indented BOM, merma, scrap factor, rendimiento, yield, lista fantasma, phantom BOM, blow-through, lista de planificación, planning BOM, lista modular, modular BOM, super bill, lista configurable, lista de ingeniería, EBOM, lista de fabricación, MBOM, código de nivel más bajo, low-level code, subproducto, by-product, coproducto, co-product]
creado: 2026-11-27
revisado:
---

# Lista de materiales

La lista de materiales dice qué componentes, y en qué cantidad, hacen falta para fabricar una cantidad base de un producto. Cada componente puede tener su propia lista, y la cadena de listas forma el árbol del producto, que el MRP explota y el costo estándar recorre nivel por nivel.

Es uno de los dos datos maestros de [Producto y proceso](producto-y-proceso.md); el otro es la [ruta de fabricación](ruta-de-fabricacion.md), que dice cómo se hace. Cada renglón apunta a un [artículo](../../Inventario-y-depositos/Existencias/articulo.md), con su código y su unidad: la lista no crea artículos, los relaciona. Un sistema comercial la define así: «A bill of materials (BOM) defines the components that are required in order to produce a product. The components can be raw materials, semi-finished products, or ingredients».

## Un nivel por lista, un árbol por producto

Cada lista describe un solo nivel: el producto y sus componentes directos. El mismo sistema comercial lo dice: «A single BOM describes a single level», y los componentes «might have their own BOMs».

Un ejemplo publicado con una lámpara muestra el árbol. La lámpara LA01 lleva una base B100, una pantalla S100 y un conjunto de zócalo A100, una unidad de cada uno. La base lleva, entre otras cosas, 4 tornillos 1400. El zócalo lleva un subconjunto 1500, que a su vez lleva 2 tornillos 1400. El mismo tornillo aparece en dos ramas y a dos profundidades distintas.

| Nivel | Artículos (cantidad por unidad del padre) |
|---|---|
| 0 | LA01 |
| 1 | B100 (1), S100 (1), A100 (1) |
| 2 | bajo B100: 1100 (1), 1200 (1), 1300 (1), 1400 (4); bajo A100: 1500 (1), 1600 (1), 1700 (1) |
| 3 | bajo 1100: 2100 (26); bajo 1500: 1400 (2); bajo 1700: 2200 (12), 2300 (1) |

Los niveles son cuenta de la base sobre los datos de la fuente. Una lámpara lleva 6 tornillos 1400: 4 en la base y 2 en el zócalo. Esa suma de todas las ramas es la lista explotada, la que ve el depósito al preparar el material.

Las cantidades se refieren a una cantidad base del producto, que va en la cabecera: un sistema abierto pide la «quantity of the Item that will be manufactured from this Bill of Materials». Una lista de pintura puede estar hecha para 100 litros y una de muebles para una unidad; la orden escala desde esa base.
## Merma del componente y rendimiento de la salida

Son dos conceptos que los sistemas guardan por separado. La merma del componente dice que se consume más de lo que queda en el producto, como el recorte de una chapa. Se guarda como porcentaje por renglón. Un sistema comercial calcula la cantidad a costear como «Qty. Required * (1 + Scrap Factor)»: con 2 kg por unidad y 5 % de merma, se consumen 2,1 kg (cuenta de la base).

El rendimiento mira la salida: de lo que entra, sale menos producto que lo teórico. Un sistema comercial pone en cada versión de fórmula el «yield», junto con los coproductos y subproductos. Un sistema abierto llama pérdida de proceso a la parte del mismo producto que se pierde, y la resta de lo producido.

> [!NOTE] Sin fuente todavía: las definiciones de «yield» y «scrap factor» del diccionario de APICS (ASCM), y si el campo considera la merma del componente y el rendimiento como dos conceptos o como uno.

La merma real de cada orden, y la diferencia con la de la lista, se registran en [consumo y declaración](../Ejecucion-en-planta/consumo-y-declaracion.md).

## Lista fantasma: el subconjunto que no se guarda

Una lista fantasma describe un subconjunto que se arma en la línea y entra enseguida en el producto de arriba, sin pasar por el depósito. Según el glosario de un sistema comercial, que parafrasea el diccionario de APICS (octava edición), se construye físicamente pero no se almacena, y el MRP pasa sus necesidades directo a sus componentes. Sinónimos: «blow-through», «transient bill of material», «pseudo bill of material».

La terminología del IISE la llama una técnica «used primarily for transient (non-stocked) sub-assemblies», y un solucionario de un curso de MRP la resume así: «A phantom bill of material is a subassembly that exists only on the production line».

Sirve para que el diseño tenga un nivel con nombre propio sin que la planta haga una orden ni un movimiento de stock por él (lectura de la base). Un sistema comercial advierte contra el abuso: «you should avoid deep hierarchies of phantoms», porque afecta el rendimiento del cálculo. Las fuentes no coinciden en las operaciones: una dice que las operaciones del fantasma se suman a la ruta del padre; las demás solo hablan de materiales.

## Lista de planificación, modular y variantes

Una lista de planificación no describe cómo se arma nada: sirve para calcular. Un sistema comercial dice que con ella «The demand of components and ingredients is calculated based on the demand of the finished products».

Las listas modulares y configurables aparecen cuando el producto se arma con opciones: un mueble en tres medidas y cuatro terminaciones. En un sistema comercial, el modelo y sus clases de opción entran en la lista de arriba como fantasmas. Un sistema abierto resuelve las variantes con una sola lista: si el renglón no indica variante, «the component is used in all product variants»; si indica una, solo entra en esa. Las estrategias en que aparecen estas listas están en [fabricar para stock o contra pedido](../Planificacion-de-la-produccion/fabricar-para-stock-o-contra-pedido.md).

> [!NOTE] Sin fuente todavía: definiciones del campo de lista de planificación, lista modular, «super bill» y lista configurable, y cómo se planifican las opciones con porcentajes en ensamble contra pedido.

## Lista de ingeniería y lista de fabricación

Ingeniería y planta pueden necesitar estructuras distintas. Un sistema comercial distingue cinco tipos de lista: borrador, ingeniería, planificación, producción y costeo. La de ingeniería agrupa el producto en módulos de diseño, y «the engineering BOM must be converted to an actual production BOM» antes de fabricar. El mismo sistema aclara que «In simple implementations, a planning BOM, production BOM, and costing BOM can be modeled as one BOM».

Los dos sistemas abiertos leídos manejan una sola lista, con un tipo (fabricar o kit); la separación aparece donde hay gestión de cambios formal. El riesgo de tener dos es que se separen sin que nadie lo note (inferencia de la base); cómo se controla está en [cambios de ingeniería](cambios-de-ingenieria.md).

## Código de nivel más bajo

El código de nivel más bajo es el nivel más profundo en que aparece un artículo en todas las listas vigentes. Un sistema comercial lo define como «the lowest level at which the item appears in all current, job, and production schedule bills of material», y agrega que «A low-level code of 0 indicates that the item is an end item». Según otra ayuda de sistema, representa «the sequence in which items are run through MRP».

En la lámpara, el tornillo 1400 aparece en el nivel 2 y en el 3: su código es 3 (cuenta de la base). El [MRP](../Planificacion-de-la-produccion/mrp.md) no lo calcula hasta terminar todos los niveles de arriba, y así netea una sola vez las necesidades de las dos ramas. Se deriva de las listas y se recalcula cuando una cambia.

## Subproducto y coproducto como datos de la lista

Algunas listas tienen más de una salida. Un sistema abierto define el subproducto como «a residual product that is created during production in addition to the main product», con producto, cantidad, unidad y, opcionalmente, la operación donde aparece. Su ejemplo es el residuo («Mush») que sale de moler la uva al hacer vino tinto. Un sistema comercial dice que la fórmula «describes co-products and by-products».

En la lista, entonces, una salida extra es un renglón más, del lado de lo que sale. Cómo se registra en la planta lo que efectivamente salió está en [consumo y declaración](../Ejecucion-en-planta/consumo-y-declaracion.md); qué pasa con su valor en el costo, en [costo estándar del producto](../Costos-de-produccion/costo-estandar-del-producto.md).

> [!NOTE] Sin fuente todavía: la distinción del campo entre coproducto y subproducto, y sus consecuencias en el costeo. Los sistemas leídos usan los dos términos sin definir la diferencia.

## Qué guarda una lista de materiales

| Parte | Datos |
|---|---|
| Cabecera | producto, cantidad base y unidad, tipo (fabricar o kit; ingeniería, planificación o producción), fantasma sí o no, estado (borrador, enviada, cancelada), activa y por defecto, versión y vigencia desde y hasta (a veces por cantidad o por planta) |
| Renglón de componente | artículo, cantidad, unidad, porcentaje de merma, operación de la ruta donde se consume, no explotar, variantes a las que aplica, lista por defecto del subconjunto, depósito de origen |
| Salidas extra | coproductos y subproductos con artículo, cantidad, unidad y operación; pérdida de proceso |
| Derivados | lista explotada, código de nivel más bajo y costo de la lista; se calculan, no se cargan |

Campos de dos sistemas abiertos y uno comercial. La versión y la vigencia las administra [cambios de ingeniería](cambios-de-ingenieria.md).

La lista de repuestos de una máquina es otra cosa: está en [jerarquía de activos](../../Activos-y-mantenimiento/Registro-de-activos/jerarquia-de-activos.md#componentes-y-lista-de-repuestos-del-equipo).
