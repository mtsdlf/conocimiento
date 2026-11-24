---
resumen: >-
  Cómo da acceso a un tercero cada cuenta que usa una tienda pyme sin compartir la contraseña del dueño, consultado el 2026-11-24: Shopify, Tiendanube, WooCommerce, Google Search Console y Analytics, Mercado Pago, Meta y el dominio en NIC Argentina, con el rol que le conviene al prestador y cómo se quita.
estado: borrador
estabilidad: volatil
fuentes:
  - "Shopify, Collaborations (Dev Dashboard), consulta 2026-11-24: https://shopify.dev/docs/apps/build/dev-dashboard/stores/collaborations"
  - "Shopify, Collaborator accounts: https://help.shopify.com/en/partners/dashboard/managing-stores/collaborator-accounts"
  - "Shopify, Collaborator accounts (manual del comercio): https://help.shopify.com/en/manual/your-account/staff-accounts/collaborator-accounts"
  - "Tiendanube, Cómo agregar más usuarios para que administren mi tienda: https://ayuda.tiendanube.com/es_AR/123366-permisos-para-usuarios/como-agregar-mas-usuarios-para-que-administren-mi-tienda"
  - "WooCommerce, Roles and capabilities (según resumen): https://woocommerce.com/document/roles-capabilities/"
  - "Google, Search Console: permisos de usuarios: https://support.google.com/webmasters/answer/7687615?hl=en"
  - "Google, Analytics: roles y permisos: https://support.google.com/analytics/answer/9305587?hl=en"
  - "Mercado Pago Developers, Colaboradores: https://www.mercadopago.com.ar/developers/es/docs/collaborators"
  - "NIC Argentina, Registro de Dominios de Internet: aspectos básicos (2021): https://NIC.ar/sites/default/files/2021-06/Registro_de_Dominios_de_Internet-Aspectos_basicos.pdf"
  - "Emprender/.investigacion/acceso-a-las-cuentas-del-cliente.md"
aliases: [colaborador de Shopify, usuarios de Tiendanube, shop manager, colaboradores de Mercado Pago, apoderado de NIC Argentina, propietario delegado]
creado: 2026-11-24
revisado:
---

# Accesos delegados por plataforma

Cómo da acceso a un tercero cada cuenta que usa una tienda pyme sin compartir la contraseña del dueño, consultado el 2026-11-24: Shopify, Tiendanube, WooCommerce, Google Search Console y Analytics, Mercado Pago, Meta y el dominio en NIC Argentina, con el rol que le conviene al prestador y cómo se quita.

Implementa la regla de [acceso a las cuentas del cliente](acceso-a-las-cuentas-del-cliente.md): usuario propio, permisos justos y salida explícita. Las plataformas cambian estas pantallas seguido; antes de pedir un acceso, abrí la fuente viva de cada fila.

| Cuenta | Cómo entra el prestador | Rol que conviene | Cómo se quita | Fuente |
|---|---|---|---|---|
| Shopify | Desde su panel de socio pide acceso a la tienda con la URL `myshopify.com` y el código de colaborador de 4 dígitos que el comercio ve en Settings > Users > Security; el comercio aprueba y elige los permisos | Colaborador con los permisos de la tarea (no puede tener el rol Administrator) | El socio, con «Remove access», o el comercio desde sus usuarios; vence solo a los 90 días sin que nadie de la organización entre | Documentación de Shopify |
| Tiendanube | El comercio lo agrega como usuario en Configuración > Usuarios y notificaciones; el email no puede estar asociado a otra tienda | Permisos por área, si el plan lo permite; en planes sin esa opción el acceso es total | El comercio, desde la misma pantalla; el primer usuario no se puede quitar | Ayuda de Tiendanube |
| WooCommerce (WordPress) | El dueño del sitio le crea un usuario | Shop Manager, que gestiona la tienda sin editar código; Administrator solo si hace falta tocar el sitio | Borrar el usuario | Documentación de WooCommerce (por resumen) |
| Google Search Console | Un propietario lo agrega por email | Usuario completo; propietario delegado solo si tiene que gestionar usuarios o verificar | El propietario lo quita | Ayuda de Google |
| Google Analytics | Un administrador lo agrega a la cuenta o la propiedad | Editor o Analista según la tarea; rige el permiso más amplio que tenga | Un administrador lo quita | Ayuda de Google |
| Mercado Pago | El titular lo invita desde Tu cuenta > Gestionar colaboradores; «Cada persona invitada crea su propia cuenta y contraseña» | Una función con permisos acotados; Administrador de la cuenta da acceso total | Desde la misma sección (por resumen; la documentación leída no lo describe) | Mercado Pago Developers |
| Meta (portfolio comercial) | El comercio agrega el portfolio del prestador como socio y le asigna activos | Acceso parcial a los activos de la tarea | El comercio quita al socio y se revoca todo lo compartido | Solo fuentes de terceros; la ayuda de Meta no se pudo leer |
| Dominio .ar (NIC Argentina) | El titular designa un apoderado en Trámites a Distancia, con Clave Fiscal nivel 2 o más | Apoderado solo si tiene que hacer trámites; para apuntar el dominio a la tienda alcanza con que el titular cambie la delegación | El titular revoca el apoderamiento | NIC Argentina (documento de 2021) |

Lo que varía entre fuentes:

- **Mercado Pago:** la documentación para desarrolladores dice que el invitado puede tener una cuenta de Mercado Pago o de Mercado Libre; el blog de México y un resumen dicen que el correo no puede estar vinculado a otra cuenta. Hay que probarlo en la cuenta argentina.
- **Shopify, segundo factor:** según un resumen de su ayuda, el comercio no puede exigirle el segundo factor a un colaborador; la página para socios pide que entren con «a secure sign-in method, such as a passkey or two-step authentication».

> [!NOTE]
> Sin fuente todavía: cómo entra un socio del programa de Tiendanube a la tienda de un cliente (la ayuda solo explica cómo da acceso a su propio equipo), la lista oficial de permisos de Tiendanube, la ayuda oficial de Meta sobre socios, los roles de WordPress en su documentación primaria, y los registradores de dominios .com.
