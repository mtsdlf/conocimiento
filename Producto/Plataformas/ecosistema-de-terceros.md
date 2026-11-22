---
resumen: >-
  El ecosistema de terceros es el conjunto de empresas y desarrolladores que construyen sobre una plataforma con las interfaces que ella abre, como las apps que un comerciante instala en su tienda online. La plataforma gana alcance cuando abre y pierde control si abre de más, y esa tensión ordena qué abre, cuánto cobra y qué se guarda para sí.
estado: vigente
estabilidad: semi
fuentes:
  - "Ahmad Ghazawneh y Ola Henfridsson (2013), Balancing platform control and external contribution in third-party development: the boundary resources model, Information Systems Journal 23(2):173-192: https://www.uio.no/studier/emner/matnat/ifi/IN4150/h22/literature/lecture-3/ghazaw~1.pdf (leído en pasajes)"
  - "Geoffrey Parker y Marshall Van Alstyne (2018), Innovation, Openness, and Platform Control, Management Science 64(7):3015-3032, DOI 10.1287/mnsc.2017.2757: https://pubsonline.informs.org/doi/pdf/10.1287/mnsc.2017.2757 (fragmentos del abstract vía buscador); versión 2007: https://dspace.mit.edu/handle/1721.1/65369 (según resumen)"
  - "Annabelle Gawer y Michael Cusumano (2014), Industry Platforms and Ecosystem Innovation, JPIM 31(3):417-433: https://dspace.mit.edu/handle/1721.1/98590 (solo abstract)"
  - "Shopify, Revenue share for Shopify App Store developers (documentación oficial): https://shopify.dev/docs/apps/launch/distribution/revenue-share (según resumen)"
  - "Comisión Europea, caso Amazon Marketplace, comunicado IP/22/4522: https://ec.europa.eu/commission/presscorner/api/files/document/print/it/ip_22_4522/IP_22_4522_EN.pdf (según resumen)"
  - "Thomas Eisenmann, Geoffrey Parker y Marshall Van Alstyne (2006), Strategies for Two-Sided Markets, HBR 84(10):92-101: https://www.kth.se/social/files/546b8e7ef2765474dd3f23fe/4.Eisenmann+et+al+(2006).pdf (leído en pasajes)"
  - "Parker, Van Alstyne y Choudary, Platform Revolution (2016), caps. 7 y 8, apertura y gobernanza (no leídos; índice: https://toc.uni.li/FLMF051021.pdf)"
  - "Producto/.investigacion/plataformas.md"
  - "Producto/.investigacion/posicion-contraria.md (afirmación 6)"
aliases: [third-party ecosystem, ecosistema de apps, app store, tienda de apps, recursos de frontera, boundary resources, apertura de plataforma, platform openness, sherlocking]
creado: 2026-11-22
revisado: 2026-11-22
---

# Ecosistema de terceros

El ecosistema de terceros es el conjunto de empresas y desarrolladores que construyen sobre una plataforma con las interfaces que ella abre, como las apps que un comerciante instala en su tienda online. La plataforma gana alcance cuando abre y pierde control si abre de más, y esa tensión ordena qué abre, cuánto cobra y qué se guarda para sí.

Es el tercer lado de una [plataforma](plataformas.md) de tiendas online: los desarrolladores vienen porque hay comerciantes, y los comerciantes se quedan porque las apps resuelven lo que la plataforma no trae. Es un caso del [efecto de red](efecto-de-red.md) cruzado. Gawer y Cusumano (2014), según su abstract, llaman plataforma industrial o externa a la que sirve de base a innovadores de afuera; la que solo comparte piezas entre productos propios es interna.

## Abrir y controlar a la vez: resourcing y securing

Una plataforma abre su ecosistema con recursos de frontera: kits de desarrollo (SDK), APIs y documentación. Ghazawneh y Henfridsson (2013) describen dos procesos que actúan sobre esos recursos y tiran en sentidos contrarios:

| Proceso | Definición de los autores | Qué hace la plataforma |
|---|---|---|
| Resourcing | "The process by which the scope and diversity of a platform is enhanced" | publica APIs y herramientas para que otros agreguen funciones |
| Securing | "The process by which the control of a platform and its related services is increased" | revisa, restringe o cierra lo que los terceros pueden hacer |

Su caso es el iPhone. Apple publicó el SDK en 2008 y abrió la App Store con revisión de cada aplicación. A principios de 2009 había "25 000 applications, 50 000 registered developers and 800 million user downloads". La revisión fue criticada por "a notable number of third-party developers" por estar "too single-handedly focused on Apple's business interests". Es una plataforma de dispositivos y no de comercio; la analogía con una plataforma de tiendas vale por la tensión entre control y aporte, no por el mercado.

La calidad también puede llevar a cerrar. Según Eisenmann et al., las consolas filtran a los desarrolladores porque "developers cannot afford to offer titles with marginal quality". Un listado de apps abierto a cualquiera arriesga lo mismo (lectura de la base).

## Cuánto abrir: lo que modelan Parker y Van Alstyne

Parker y Van Alstyne (2018) tratan a la plataforma como una "microeconomy" y preguntan "how open should that economy be?". Según los fragmentos del abstract leídos, cerrar aumenta la capacidad de la plataforma de cobrar el acceso, y abrir aumenta la capacidad de los desarrolladores de construir. El modelo caracteriza un grado de apertura óptimo y cuánto debería durar la propiedad intelectual de lo que construyen los terceros.

En la versión de 2007, según un resumen, comparan a un planificador social con un dueño privado. El planificador abriría antes y más. El dueño privado se acerca a ese comportamiento cuando controla la innovación que viene después. Es un modelo teórico, no un estudio de plataformas reales.

## El reparto de ingresos con los desarrolladores

La comisión de la tienda de apps es la parte que la plataforma se queda de lo que cobran los desarrolladores. El ejemplo documentado es el de Shopify, según un resumen de su documentación oficial:

- No cobra nada sobre el primer USD 1.000.000 de ingresos brutos de por vida de un desarrollador, y cobra 15% sobre lo que pase de ahí.
- Eso vale para desarrolladores bajo ciertos umbrales; quien los supera paga 15% sobre todo.
- En 2021 el umbral se reiniciaba cada año y la tasa bajó de 20% a 15%; después pasó a contarse de por vida.
- Para el umbral de por vida, "revenue earned before January 1, 2025 doesn't count".

> [!IMPORTANT]
> El esquema se puede leer como subsidio al lado de los desarrolladores, en el sentido de [mercado de dos lados](mercado-de-dos-lados.md): la plataforma cobra poco a quien trae apps para atraer y retener comerciantes. También se puede leer como una política de precios sin esa intención. La documentación solo da las reglas, no el motivo, y no se encontró un estudio que compare comisiones entre tiendas de apps.

Estas cifras cambian seguido y convendría llevarlas en una ficha fechada cuando haya una comparación de comisiones.

## Cuando la plataforma absorbe lo que hicieron otros

El riesgo mayor para un desarrollador es que la plataforma lance como función propia lo que su app ya resolvía. La teoría es el envolvimiento de Eisenmann et al., explicado en [mercado de dos lados](mercado-de-dos-lados.md#el-envolvimiento-cuando-otra-plataforma-te-mete-en-su-paquete): quien tiene la base de usuarios puede ofrecer la función dentro de su paquete. En la jerga se lo llama "sherlocking", pero no se encontró fuente académica con ese nombre.

El único caso regulatorio documentado en los informes es de un marketplace, no de una tienda de apps. La Comisión Europea abrió en julio de 2019 una investigación a Amazon por el uso de datos no públicos de vendedores independientes en su propio negocio de venta. Le envió un pliego de cargos el 10 de noviembre de 2020. En diciembre de 2022 aceptó compromisos obligatorios: cinco años para lo referido a datos y siete para la Buy Box y Prime. Las fuentes no coinciden en el día exacto de diciembre, 20 o 22. Todo esto se leyó por resúmenes del comunicado.

La lección para una plataforma de tiendas es una inferencia: los datos que la plataforma ve de comerciantes y desarrolladores la ponen en ventaja para competirles, y esa ventaja ya fue objeto de regulación en un caso.

> [!NOTE] Sin fuente todavía: casos documentados de una plataforma de comercio que reemplazó apps de terceros con funciones propias, estudios empíricos sobre apps copiadas, y evidencia sobre calidad y concentración de ingresos de los desarrolladores en tiendas de apps de comercio.

Para la versión de escuela sobre apertura y gobernanza, *Platform Revolution* dedica los capítulos 7 y 8; no se leyeron. Las reglas de quién entra y cómo se resuelven los conflictos quedan para una nota de gobernanza que todavía no existe.
