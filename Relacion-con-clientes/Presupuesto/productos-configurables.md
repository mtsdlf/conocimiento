---
resumen: >-
  Un producto configurable es el que el cliente arma eligiendo opciones dentro de una familia, y presupuestarlo pide un configurador: reglas que dicen qué opciones son compatibles, qué precio tiene la variante elegida y cuánto tarda en entregarse. Los proveedores de software usan el término CPQ (configure, price, quote); la academia lo estudia como configuración de producto.
estado: borrador
estabilidad: estable
fuentes:
  - "Forza y Salvador (2006), Product Information Management for Mass Customization, Palgrave Macmillan, caps. 1, 2 y 5 (leído un 25 %): https://vdoc.pub/documents/product-information-management-for-mass-customization-connecting-customer-front-office-and-back-office-for-fast-and-efficient-customization-5rgv091itko0"
  - "Felfernig, Hotz, Bagley y Tiihonen (2014), Knowledge-Based Configuration: From Research to Business Cases, Morgan Kaufmann (solo la ficha): https://shop.elsevier.com/books/knowledge-based-configuration/felfernig/978-0-12-415817-7"
  - "Sinz y Haag (eds.), ECAI 2006 Workshop on Configuration, Proceedings (prefacio): https://fmv.jku.at/ecai-config-ws-2006/W16.pdf"
  - "Microsoft Dynamics 365, Create a sales order for a configurable product (según su resumen): https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/tasks/create-sales-order-configurable-product"
  - "SCOR 6.0 Quick Reference, D2.2 «Receive, Configure, Enter and Validate Order»: https://www2.isye.gatech.edu/~lfm/8851/Sources/SCOR/SCORv6quickref.pdf"
  - "Relacion-con-clientes/.investigacion/presupuesto-y-pedido.md (sección C)"
aliases: [CPQ, configure price quote, configurador, configurador de producto, product configurator, configuración de producto, product configuration, variante, mass customization, personalización masiva]
creado: 2026-11-27
revisado:
---

# Productos configurables

Un producto configurable es el que el cliente arma eligiendo opciones dentro de una familia, y presupuestarlo pide un configurador: reglas que dicen qué opciones son compatibles, qué precio tiene la variante elegida y cuánto tarda en entregarse. Los proveedores de software usan el término CPQ (configure, price, quote); la academia lo estudia como configuración de producto.

Un [presupuesto](presupuesto.md) común tiene renglones con productos que ya existen en el catálogo. Uno de un producto configurable tiene que armar primero el producto: una cocina a medida, una máquina con motor y accesorios a elección, un servidor con memoria y discos elegidos, un servicio con módulos que se suman. Cada combinación es una variante, y no todas las combinaciones existen o son posibles.

## Qué es configurar, según la investigación

Forza y Salvador (2006), que estudian la personalización masiva, definen ofrecer variedad por configuración como darle al cliente la posibilidad de personalizar el producto. El proceso de configurar va desde juntar lo que el cliente necesita hasta emitir la documentación del producto, y tiene dos mitades:

- **La configuración comercial**: describir el producto que el cliente está dispuesto a comprar.
- **La configuración técnica**: todas las actividades que generan la documentación de la variante.

Que la comercial ocurra durante el presupuesto y la técnica después del pedido, en Producción (con la lista de materiales y las instrucciones de fabricación como ejemplos de esa documentación), es criterio de la base.

Para los mismos autores, el precio y un plazo de entrega indicativo son resultados fundamentales de la configuración comercial. Y poner el precio es más difícil, porque cada variante tiene su costo. De ahí sale la razón por la que configurador, precio y presupuesto van juntos: el cliente no puede aceptar una variante sin saber cuánto sale y cuándo llega.

También sostienen que la configurabilidad no es propiedad de un producto sino de una familia de productos. Lo que se modela no es cada variante, sino la familia con sus opciones y sus reglas.

## Por qué hacen falta reglas

La variedad crece rápido: un producto con diez opciones de tres valores cada una tiene casi 60.000 combinaciones, y muchas no se pueden fabricar o no tienen sentido (la cuenta es aritmética, no de una fuente). El prefacio de las actas del taller de configuración de ECAI 2006 dice que hacen falta modelos de representación del conocimiento potentes para captar la variedad y la complejidad de los productos configurables. Un configurador guarda tres tipos de regla (la lista es criterio de la base):

1. **Compatibilidad**: qué opciones van juntas y cuáles se excluyen.
2. **Precio**: cuánto suma o resta cada opción, o cómo se calcula el precio de la variante.
3. **Plazo**: qué opciones alargan la entrega, porque piden fabricar o comprar algo.

El libro de referencia técnica sobre estas reglas es *Knowledge-Based Configuration* (Felfernig, Hotz, Bagley y Tiihonen, 2014), pendiente de lectura: de él solo se leyó la ficha.

> [!NOTE] Sin fuente todavía: una cita sobre reglas de compatibilidad y paquetes (bundles) del libro de Felfernig y otros, y un umbral de cuándo conviene un configurador frente a una lista de productos con variantes.

## Cómo se ve en el presupuesto y en el pedido

En los sistemas de gestión, la configuración vive en el renglón: un ERP de un proveedor grande ofrece configurar el renglón de un presupuesto o de un pedido solo para artículos que tienen un modelo de configuración activo, según su resumen. SCOR 6.0 lo pone en el proceso de entrega de productos hechos contra pedido: D2.2 «Receive, Configure, Enter and Validate Order», donde configurar es parte de recibir el pedido.

Lo que sigue es inferencia de la base. La variante elegida tiene que viajar intacta del presupuesto al [pedido de venta](../Pedido-de-venta/pedido-de-venta.md) y de ahí a Producción, que la convierte en lista de materiales. Si la variante se reescribe a mano en el pedido, se pierde la garantía de que es posible. Y la fecha que se le promete depende de la capacidad, no solo del stock, que es el caso de capable-to-promise que se explica en [fecha prometida](../Pedido-de-venta/fecha-prometida.md).

## Cuándo no hace falta

Si las opciones son pocas y todas compatibles, alcanza con productos con variantes (talle y color) o con renglones opcionales que el cliente marca. Un sistema abierto tiene «productos opcionales» en sus plantillas de presupuesto; que funcionen sin reglas de compatibilidad es inferencia de la base. El configurador se justifica cuando hay reglas de compatibilidad o cuando el precio no es la suma de las partes. Esto es criterio de la base.

«CPQ» no apareció en ninguna fuente primaria o académica leída: el término lo usan los proveedores para el software que junta las tres cosas, y no se leyó una definición. En la base se usa «configurador» para la pieza y «producto configurable» para lo que se vende.
