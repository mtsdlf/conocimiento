---
tema: Software de gestión
para: entender cómo está hecho, cómo se clasifica, cómo se elige e implanta y cómo se vende el software que lleva los dominios de una empresa (ERP, CRM y sus vecinos), para quien construye software de gestión y, en segundo lugar, para quien lo vende o lo implementa
nivel: entiende de software y de negocio en general; el saber de cada dominio (qué es un asiento, una orden de compra, una liquidación) se da por leído en su tema del área «Gestión de la empresa», y acá se explica solo lo que es del software
escuela: neutral; las categorías se cuentan como las cortan el mercado y las normas (ISA-95 para la frontera entre el negocio y la planta), las columnas técnicas desde los patrones de análisis de Fowler con REA como posición contraria, y la implantación desde la literatura académica de sistemas de información (Markus y Tanis, Soh, Brehm), con las cifras de fracaso de consultoras marcadas como tales
fuera:
  - el saber de cada dominio (contabilidad, impuestos, tesorería, compras, inventario, cadena de suministro, producción, relación con clientes, servicio al cliente, personal y nómina, servicios profesionales, activos y mantenimiento) — en su tema del área «Gestión de la empresa»; acá se enlaza
  - los recorridos que cruzan dominios (del pedido al cobro, de la compra al pago y los otros seis) — Procesos-de-negocio; acá se cuenta solo cómo un producto los lleva entre módulos
  - la inteligencia de negocio (el almacén de datos, los tableros, la capa semántica, lo que junta varias fuentes o mucha historia para decidir) — Datos/Visualizacion-y-BI, que la sesión 15 del mapa amplía con «BI sobre el software de gestión»
  - los patrones de sistemas distribuidos (multi-tenancy, outbox, saga, idempotencia) — Arquitectura; los modelos de datos y las transacciones — Bases-de-datos
  - el sistema de gestión aplicado al comercio (módulos de una pyme minorista, conexión con tiendas y marketplaces, fichas con precios de los sistemas argentinos) — Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion
  - el modelo de negocio del software en general (SaaS, software con servicios) — Emprender/Modelo-de-negocio; las plataformas y su ecosistema de terceros en general — Producto/Plataformas; los costos de cambio — Estrategia-competitiva
  - el análisis de competidores concretos y la comparación de productos — Estrategia-competitiva y el repo de la empresa que decide
  - cómo se lleva un proyecto en general — Gestion-de-proyectos; cómo se hace un encargo de desarrollo a medida — Desarrollo/Encargo
fuentes: []
preguntas:
  - "Voy a construir un sistema de gestión para pymes: ¿qué piezas de diseño tiene que tener sí o sí, sea cual sea el rubro, y dónde está explicado cada dominio que va a llevar?"
  - "¿Qué diferencia hay entre un ERP, un CRM, un MES y un sistema de servicio de campo, dónde termina cada uno y cuándo conviene una suite en lugar de varios sistemas conectados?"
  - "Un cliente quiere cambiar de sistema: ¿cómo se elige uno sin quedar atado a la demo del vendedor, qué datos se migran y cómo se pone en marcha sin frenar la facturación?"
  - "¿Por qué personalizar un ERP sale caro después, y cómo se decide entre adaptar el proceso o adaptar el software?"
  - "¿De qué vive una empresa que hace software de gestión, cuánto se queda un partner y cuánto termina pagando el que compra más allá de la licencia?"
  - "Tengo que vender o construir un sistema para empresas en la Argentina: ¿qué le exige la normativa al sistema (factura electrónica, libros digitales, percepciones y retenciones) y qué tiene de propio el mercado local?"
aprobado:
---

# Alcance: Software de gestión

El tema cubre el software que lleva los dominios de una empresa: cómo se clasifica (ERP, CRM, HCM, MES y los demás), qué piezas de diseño comparte todo producto de la clase, cómo se elige y se implanta en una empresa, y cómo se vende y quién gana qué. Sale del mapa «el mundo del software de gestión» (issue #94) y de sus decisiones: forma del árbol (#95, que fija que ERP y CRM son una forma de empaquetar software y no un saber), taxonomías externas (#96), columnas técnicas (#97), límites entre dominios (#98), procesos de punta a punta (#99), verticales y componentes de este tema (#100), orden de armado (#101) y huecos del árbol (#104). Es la sesión 14 de 16 (issue #121): los doce temas de dominio y Procesos de negocio ya están escritos, y este tema los enlaza.

Es un tema agnóstico: lo que dice de cómo está hecho, cómo se elige y cómo se implanta un software de gestión es cierto sin nombrar proveedores. Va en el área Industrias de `conocimiento.md`, junto a Comercio electrónico, y no en Gestión de la empresa: describe una industria, la de quien hace y vende este software, y enlaza los dominios de los que está hecha en lugar de contenerlos. Lo propio de la Argentina va en dos notas aparte: lo que la norma le pide a un sistema y lo propio del mercado local.

## Límites con los vecinos

Este tema es dueño del **producto** (cómo se empaqueta el saber de un dominio en una categoría de software), de las **columnas técnicas** (las piezas de diseño comunes a todo software de gestión), de la **implantación** (llevar un producto a una empresa) y del **mercado** (cómo se vende y se cobra). El saber que existe sin software vive en su dominio, y el recorrido que cruza dominios, en Procesos de negocio.

| Vecino | Es dueño de | La frontera con este tema |
|---|---|---|
| [Contabilidad](../Contabilidad/contabilidad.md) | la partida doble, el plan de cuentas, el devengado, los estados, el control interno | Allá, qué es un asiento y por qué no se borra; acá, la regla que convierte un documento en asiento y la fecha de bloqueo como pieza del sistema. Los controles sobre sistemas los define Contabilidad; acá se dice cómo los resuelve el producto |
| [Impuestos](../Impuestos/impuestos.md) | la obligación, el cálculo, el comprobante fiscal y los registros fiscales | Allá, qué dato lleva una factura y qué libro pide el fisco; acá, la alícuota como dato con vigencia, el motor que la aplica y la conexión con el fisco |
| [Tesorería](../Tesoreria/tesoreria.md) | la caja, el crédito, la cobranza y los pagos | El software de tesorería no es categoría propia del tema: va dentro del ERP |
| [Relación con clientes](../Relacion-con-clientes/relacion-con-clientes.md) | el cliente, la oportunidad, el presupuesto y el pedido de venta | Allá, los datos y estados del pedido; acá, el CRM como categoría y dónde termina frente al módulo de ventas del ERP |
| [Servicio al cliente](../Servicio-al-cliente/servicio-al-cliente.md) | el caso, el escalamiento y los niveles de servicio | Allá, el caso; acá, la mesa de ayuda como categoría |
| [Inventario y depósitos](../Inventario-y-depositos/inventario-y-depositos.md) | lo que pasa dentro del depósito | Allá, las existencias y la preparación; acá, el WMS como categoría y las cantidades con unidad como columna |
| [Compras y abastecimiento](../Compras-y-abastecimiento/compras-y-abastecimiento.md) | el proveedor y la orden de compra | Allá, el costo total de adquisición de cualquier compra; acá, el costo total de un software para quien lo compra |
| [Cadena de suministro y logística](../Cadena-de-suministro-y-logistica/cadena-de-suministro-y-logistica.md) | el pronóstico, el S&OP, el transporte y el despacho | Allá, el plan y el transporte; acá, la planificación de la cadena y el TMS como categorías |
| [Producción](../Produccion/produccion.md) | la lista de materiales, el MRP, la orden de producción, la calidad | Allá, ISA-95 como marco del dominio; acá, el MES como producto y su frontera con el ERP |
| [Administración de personal y nómina](../Administracion-de-personal-y-nomina/administracion-de-personal-y-nomina.md) | el legajo, la asistencia y la liquidación | Allá, la liquidación; acá, el HCM como categoría |
| [Servicios profesionales y proyectos](../Servicios-profesionales-y-proyectos/servicios-profesionales-y-proyectos.md) | el proyecto, las horas, la facturación del proyecto | Allá, el dominio; acá, el PSA como categoría |
| [Activos y mantenimiento](../Activos-y-mantenimiento/activos-y-mantenimiento.md) | el registro del equipo, la orden de trabajo, el servicio de campo | Allá, el dominio; acá, el EAM, el CMMS y el software de servicio de campo como categorías |
| [Procesos de negocio](../Procesos-de-negocio/procesos-de-negocio.md) | el recorrido de punta a punta, los traspasos y sus medidas | Allá, el recorrido que existe sin software; acá, el documento con estados y la integración entre módulos que lo llevan |
| [Datos](../Datos/datos.md) (Visualización y BI) | el análisis, el almacén de datos y los tableros | Los reportes que el sistema saca de su propia base y tiene que entregar (libros, listados del día) son de acá; lo que junta fuentes o historia para decidir es de Datos, que se amplía con «BI sobre el software de gestión» (sesión 15, todavía no escrita) |
| [Comercio electrónico](../Comercio-electronico/comercio-electronico.md) | vender online, con sus plataformas y su normativa | Allá, el sistema de gestión de un comercio, su conexión con la tienda y las fichas de los sistemas argentinos con precios; acá, el software de gestión de cualquier rubro |
| [Arquitectura](../Arquitectura/arquitectura.md) y [Bases de datos](../Bases-de-datos/bases-de-datos.md) | los patrones de sistemas distribuidos y los modelos de datos | Multi-tenancy, outbox, saga y el registro de movimientos se explican allá; acá se dice cuándo los usa un software de gestión |
| [Emprender](../Emprender/emprender.md), [Producto](../Producto/producto.md) y [Estrategia competitiva](../Estrategia-competitiva/estrategia-competitiva.md) | el SaaS como modelo, las plataformas, los costos de cambio | Allá, en general; acá, lo propio de este mercado: licencia y mantenimiento, canal de partners, localización |

## Árbol

```
Software-de-gestion/
  software-de-gestion.md                 el todo: qué es, las cinco verticales y cómo se conectan; qué leer según lo que estés haciendo
  software-de-gestion-en-argentina.md    lo que la normativa argentina le exige a un sistema: comprobante electrónico, controlador fiscal, libros y registros digitales, padrones y regímenes de información
  Fundamentos/
    fundamentos-de-software-de-gestion.md  (entrada) de dónde viene, las posiciones en disputa y cómo leer la evidencia
    historia-del-software-de-gestion.md    de MRP a MRP II, ERP, ERP en la nube y composable
    glosario-de-software-de-gestion.md     términos con su nombre en inglés
    fuentes-de-software-de-gestion.md      bibliografía comentada por vertical
    mitos-del-software-de-gestion.md       lo que se repite sin evidencia
  Categorias-de-producto/
    categorias-de-producto.md            (entrada) administrativo frente a operativo, suite frente a lo mejor de cada clase
    escalones-por-tamano.md              del facturador al ERP de una empresa grande
    erp.md                               el ERP como categoría
    crm.md                               automatización de ventas, atención y marketing
    hcm.md                               administración de personal, nómina y talento
    scm-wms-y-tms.md                     planificación de la cadena, depósito y transporte
    mes.md                               la ejecución en planta y su frontera con el ERP, con la gestión de calidad
    servicio-de-campo-y-mesa-de-ayuda.md la atención después de la venta y el técnico en la calle
    psa.md                               el software de las firmas de servicios profesionales
    eam-y-cmms.md                        gestión de activos y de mantenimiento
    software-por-rubro.md                vertical frente a horizontal
  Columnas-tecnicas/
    columnas-tecnicas.md                 (entrada) las once columnas y lo que no es columna
    datos-maestros-y-partes.md
    documento-y-estados.md
    registro-de-movimientos-y-dimensiones.md
    fechas-vigencias-y-cierre.md
    cantidades-unidades-y-monedas.md
    estructura-de-la-organizacion.md
    permisos-y-separacion-de-funciones.md
    auditoria-de-cambios.md
    integracion-y-migracion.md
    configurar-o-personalizar.md
    reportes-operativos-y-legales.md
  Implementacion/
    implementacion.md                    (entrada) el ciclo de una implantación y cómo falla
    elegir-un-sistema.md                 método general, sin nombrar productos
    analisis-de-brechas.md               adaptar el proceso o el software
    migracion-de-datos.md                qué se migra y cómo se comprueba
    puesta-en-marcha.md                  de una vez, por fases o en paralelo
    partners-de-implementacion.md        quién implanta y con qué contrato
    despues-de-la-puesta-en-marcha.md    estabilización, soporte y actualizaciones
  Mercado-y-economia/
    mercado-y-economia.md                (entrada) cómo se vende y quién gana qué
    licencia-y-suscripcion.md
    canal-de-partners.md
    ecosistema-de-extensiones.md
    economia-del-proveedor.md
    costo-total-para-quien-compra.md
    donde-entra-un-software-nuevo.md
    mercado-en-argentina.md              lo propio del mercado local; lo fiscal en Impuestos
```

## Supuestos

- Las cinco verticales y sus componentes vienen decididos en #100; el árbol de adentro (nombres de archivo, qué va en cada nota, dónde van las notas de Argentina) lo propone esta sesión sin esperar respuesta, por indicación de quien la abrió, y queda para revisar en el PR.
- No se nombran productos ni proveedores en ninguna nota. #100 da lugar a una vertical de mercado «sin análisis de competidores», y la ficha con los sistemas argentinos, sus precios y sus reseñas ya existe en Comercio electrónico: la nota de mercado argentino la enlaza en lugar de repetirla.
- Lo de la Argentina va en dos notas: una en la raíz del tema, con lo que la norma le exige a un sistema (cruza varias columnas técnicas), y otra en Mercado y economía. Las dos enlazan a Impuestos, Contabilidad y Administración de personal en lugar de repetir la norma.
- Reportes queda como columna angosta (decisión de #100). BI no tiene nota de categoría: enlaza a Datos.
- Multi-tenancy no es columna (decisión de #97): la nota de estructura de la organización lo enlaza para marcar la diferencia con varias empresas.
- Las investigaciones de #96 y #97 se copiaron enteras a `.investigacion/` como parte de la capa cruda del tema.
