---
resumen: >-
  El software por rubro (vertical) es el software de gestión hecho para una industria, con sus procesos y su normativa; el horizontal lleva funciones que sirven a cualquier empresa, como la contabilidad o el personal. Es una distinción del mercado que ninguna fuente leída define con criterios.
estado: borrador
estabilidad: semi
fuentes:
  - "Gartner, Magic Quadrant for Cloud ERP for Product-Centric Enterprises y su par para empresas de servicios, octubre de 2025 (resumen): https://www.gartner.com/en/documents/7058198"
  - "Gartner, división del ERP en administrativo y operativo, según una nota de un proveedor de suite que la cita (resumen): https://www.netsuite.com/portal/resource/articles/erp/how-does-netsuite-fit-gartners-definition-of-postmodern-erp.shtml"
  - "Light, Holland, Kelly y Willis (2000), «Best of Breed IT Strategy: An Alternative to ERP Systems», ECIS 2000 (abstract leído): https://aisel.aisnet.org/ecis2000/180"
  - "Loh y Ching (2004), «Critical elements for a successful ERP implementation in SMEs», International Journal of Production Research 42(17):3433-3455 (solo la cita; no leído): https://doi.org/10.1080/00207540410001671679"
  - "Software-de-gestion/.investigacion/fundamentos-y-categorias.md (2026-11-27)"
aliases: [software por rubro, software vertical, vertical software, ERP vertical, ERP sectorial, software de industria, industry-specific software, software horizontal, horizontal software, vertical frente a horizontal]
creado: 2026-11-27
revisado:
---

# Software por rubro

El software por rubro (vertical) es el software de gestión hecho para una industria, con sus procesos y su normativa; el horizontal lleva funciones que sirven a cualquier empresa, como la contabilidad o el personal. Es una distinción del mercado que ninguna fuente leída define con criterios.

Es un corte que atraviesa las [categorías de producto](categorias-de-producto.md): hay ERP horizontales y ERP para una industria, CRM genéricos y CRM para inmobiliarias. No se encontró una fuente académica ni una norma que defina «vertical» y «horizontal» para el software de gestión, así que la nota se apoya en cómo usa el mercado las palabras y en inferencias de esta base, marcadas como tales.

## Lo administrativo es horizontal, lo operativo es del rubro

La distinción más útil sale del corte entre lo [administrativo y lo operativo](categorias-de-producto.md#administrativo-frente-a-operativo). En la lectura de esta base, la contabilidad, los impuestos, la tesorería, las compras y la nómina funcionan casi igual en una fábrica, una clínica y una consultora: son horizontales, y lo que cambia es el país. Lo operativo es lo que depende del negocio, y ahí aparece el rubro: la orden de producción de una fábrica, la historia clínica de una clínica, la obra de una constructora, la hora imputada de una consultora.

Los analistas cortan el ERP en dos rubros gruesos. Según resúmenes, Gartner publicó en octubre de 2025 un cuadrante de ERP para empresas centradas en el producto y otro para empresas centradas en el servicio. En la lectura de esta base, es una partición vertical de primer nivel: la mitad administrativa es la misma y la operativa cambia.

Varias categorías de este tema son, en los hechos, verticales de un rubro amplio (lectura de esta base):

| Categoría | Rubro que la sostiene |
|---|---|
| [MES](mes.md) | La manufactura |
| [PSA](psa.md) | Las firmas que venden horas de gente por proyecto |
| [EAM y CMMS](eam-y-cmms.md) | Las empresas con muchos equipos que mantener |
| [Servicio de campo](servicio-de-campo-y-mesa-de-ayuda.md) | Las que instalan y reparan equipos en casa del cliente |
| El sistema de gestión del comercio | El comercio minorista y mayorista, con su punto de venta y su tienda en línea; está en [sistemas de gestión en el comercio](../../Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion/sistemas-de-gestion.md) |

## Cómo se arma un producto vertical

Hay dos caminos, y los dos se ven en el mercado (lectura de esta base, sin fuente que los mida):

1. Un producto entero para el rubro. Trae el núcleo administrativo y la parte operativa propia de la industria, con su vocabulario. Gana en ajuste y pierde en tamaño de mercado.
2. Un horizontal con una capa de rubro. Un ERP general al que un partner o el propio proveedor le suma módulos de la industria. Es el mismo debate de [suite o lo mejor de cada clase](categorias-de-producto.md#suite-o-lo-mejor-de-cada-clase) dentro de una sola empresa: Light y otros (2000) argumentan, según su abstract, que los paquetes de un solo proveedor «often fail to fit specific organizational and industry needs».

En los dos casos, la frontera entre lo horizontal y lo del rubro es una integración, y la regla es la misma que entre categorías: decidir qué sistema manda en cada dato ([integración y migración](../Columnas-tecnicas/integracion-y-migracion.md)).

## Para quien construye: dónde está la ventaja

En la lectura de esta base, el rubro es la puerta de entrada más común para un software nuevo. El núcleo administrativo está resuelto por muchos y es caro de reescribir por la normativa de cada país; la parte operativa de un rubro chico suele estar mal servida por los horizontales. El riesgo es el inverso: un vertical sin buen núcleo administrativo termina integrándose con un ERP o reescribiendo la contabilidad. El análisis de por dónde entrar a este mercado está en [dónde entra un software nuevo](../Mercado-y-economia/donde-entra-un-software-nuevo.md).

> [!NOTE] Sin fuente todavía: una definición con criterios de software vertical y horizontal, y un estudio con método que compare su adopción o su resultado por industria. El candidato a leer es Loh y Ching (2004), sobre implantaciones de ERP en pymes, visto solo como cita.
