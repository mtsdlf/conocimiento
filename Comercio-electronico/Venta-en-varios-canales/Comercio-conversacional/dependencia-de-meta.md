---
resumen: >-
  El comercio conversacional corre entero sobre plataformas de Meta, que fija precios, reglas, límites y bloqueos sin negociación: entre agosto de 2023 y octubre de 2026 cerró las tiendas de Instagram en Argentina, cambió tres veces qué mensajes son gratis, apagó dos APIs, prohibió en la API los asistentes de IA de propósito general y empezó a cobrar su propio agente. Quien construye encima depende de un solo tercero.
estado: borrador
estabilidad: semi
fuentes:
  - "Meta, precios de WhatsApp Business Platform: https://developers.facebook.com/docs/whatsapp/pricing (leída; A1)"
  - "Meta, pricing para AI Providers, developers.facebook.com (por extracto; A1)"
  - "Meta, anuncio del 3/4/2025 sobre difusiones pagas, about.fb.com (por extracto; A1)"
  - "Meta, fin de la On-Premises API, developers.facebook.com (según el buscador; A1)"
  - "TechCrunch, 18/10/2025, 13/1/2026 y 15/1/2026, sobre la prohibición de asistentes de IA de propósito general (según el buscador; B1)"
  - "La Nación, 3/8/2026: https://www.lanacion.com.ar/tecnologia/usuarios-en-todo-el-mundo-reportan-que-su-cuenta-de-whatsapp-fue-bloqueada-sin-previo-aviso-nid03082026/ (por extracto; B2)"
  - "iProfesional, 3/8/2026: https://www.iprofesional.com/tecnologia/461427-whatsapp-suspendio-miles-cuentas-genero-caos-usuarios-dependen-app (según el buscador; C3)"
  - "Tiendanube, ayuda Argentina, Instagram y Facebook Shopping (por extracto; B2)"
  - "Comercio-electronico/.investigacion/conversacional-meta-precios-y-terminos.md"
  - "Comercio-electronico/.investigacion/conversacional-resenas.md"
aliases: [riesgo de plataforma, platform risk, dependencia de un tercero, cambios de Meta, baneo de WhatsApp]
creado: 2026-11-22
revisado:
---

# Dependencia de Meta

El comercio conversacional corre entero sobre plataformas de Meta, que fija precios, reglas, límites y bloqueos sin negociación: entre agosto de 2023 y octubre de 2026 cerró las tiendas de Instagram en Argentina, cambió tres veces qué mensajes son gratis, apagó dos APIs, prohibió en la API los asistentes de IA de propósito general y empezó a cobrar su propio agente. Quien construye encima depende de un solo tercero.

Es el riesgo que atraviesa todo el [comercio conversacional](comercio-conversacional.md). La misma lógica, con otro dueño, aparece en la [competencia con la plataforma](../../../Producto/Plataformas/competencia-con-la-plataforma.md) de los marketplaces.

## Los cambios, con fecha

| Fecha | Cambio | A quién golpeó |
|---|---|---|
| 10/8/2023 | Fin de las tiendas y etiquetas de producto de Instagram y Facebook en Argentina, Chile y Colombia | comercios y plataformas de tiendas con el catálogo conectado |
| 4/12/2024 | Cierre de la Instagram Basic Display API | widgets y apps de terceros |
| 1/11/2024 | Los mensajes de servicio de la API pasan a ser gratis | — (a favor) |
| 1/4/2025 | Pausa de las plantillas de marketing a números de EE. UU., vigente al 2026-11-22 | marcas y proveedores con clientes en EE. UU. |
| 3/4/2025 | Las difusiones de la app gratis pasan a pagarse; límites a cuántos mensajes de marketing recibe cada usuario | comercios que promocionaban gratis desde la app |
| 1/7/2025 | La API pasa de cobrar por conversación a cobrar por mensaje; la utilidad dentro de la ventana pasa a ser gratis | todo intermediario: rehacer facturación y presupuestos |
| 7/10/2025 | Los límites de envío pasan del número al portafolio de la empresa | intermediarios que repartían números |
| 23/10/2025 | Fin de la API instalada en servidores propios (On-Premises) | quien no había migrado a la de Meta |
| 15/1/2026 | Prohibición de los asistentes de IA de propósito general en la API (para cuentas nuevas desde el 15/10/2025); los asistentes de OpenAI, Copilot y Perplexity salieron de WhatsApp. Los bots de atención de un comercio siguen permitidos. Quedaron exceptuados por orden de sus reguladores Italia, Brasil, el Espacio Económico Europeo (11/3/2026) y Turquía (15/10/2026); Argentina no | empresas de IA sobre WhatsApp |
| 1/7/2026 | Meta empieza a cobrar su propio agente de IA, en uso desde antes de junio, y en su documentación lo compara en precio contra los de terceros, con tarifas de Brasil | proveedores de bots e IA: Meta compite en su propio canal |
| 3/8/2026 | Bloqueos masivos de cuentas; Meta dijo «A veces nos equivocamos». La nota leída no habla de cuentas de empresa; el vínculo con los comercios lo dan las reseñas | pymes que atienden por WhatsApp |
| 15/9/2026 | Meta lanza la suscripción Meta One, con insignia, créditos de difusión y agente; no dice si reemplaza a Meta Verified | quien pagaba la verificación |
| 1/10/2026 | Vuelve el cobro del servicio (con 1.000 gratis por número) y de la utilidad dentro de la ventana; sin medio de pago cargado, se cortan los mensajes de servicio | comercios e intermediarios con mucha atención |

Meta avisa con anticipación: desde septiembre de 2025 solo cambia precios el 1/1, 1/4, 1/7 o 1/10, con un mes de aviso para una tarifa, tres para sumar algo al modelo y seis para cambiar el modelo. Ese calendario vale para los precios; los cierres, las prohibiciones y los bloqueos no lo siguen. Y el aviso no cambia la asimetría: la regla la escribe un solo lado.

## Cómo pega en cada uno

- **En el comercio**, el golpe más directo es perder el número. En 180 reseñas negativas argentinas de la app de 2026 hay 31 bloqueos, con relatos de un número de cinco años perdido y de clientes y ventas que se fueron con él ([quejas](quejas-de-los-comercios-que-venden-por-chat.md#bloqueos-del-número)). La apelación se hace desde el portafolio de negocio, sin resultado garantizado. La prensa menciona fallos judiciales argentinos contra Meta por cuentas bloqueadas que no se pudieron leer.
- **En el intermediario**, el golpe es de modelo: cada cambio de cobro obliga a reescribir precios y contratos, y un cambio de términos puede dejar fuera una categoría entera, como pasó con los asistentes de IA de propósito general. Un proveedor de Bélgica escribió en el foro de desarrolladores de Meta, en julio de 2026, que con el cobro de los mensajes de servicio ya no podía defender el precio ante sus clientes (leído por extracto).
- **En quien compite con Meta**, el riesgo es que Meta haga lo mismo: su agente de IA en WhatsApp e Instagram compite con los bots de terceros, y Meta lo cobra por tokens desde el 1/7/2026; en Argentina sale más caro por mensaje que una respuesta de servicio.

## Lo que no cambia

El canal sigue siendo donde están los compradores: los vendedores lo usan porque «ya lo tiene todo el mundo instalado», como dice una reseña positiva. Nada de lo leído indica que un comercio pueda dejar de atender por WhatsApp sin perder ventas, ni que exista un canal alternativo con esa llegada en Argentina; la dependencia es del comercio tanto como de quien le vende herramientas.

> [!NOTE] Sin fuente todavía: casos argentinos con pérdidas medidas por un cambio de Meta, el texto de los fallos judiciales por bloqueos y los requisitos para ser proveedor de la API.
