---
resumen: >-
  El acceso a las cuentas del cliente es cómo entra quien arma o cuida una tienda a la tienda, el dominio, los pagos y las herramientas del comercio, y cómo sale. La regla que sostienen las plataformas y las guías de seguridad tiene tres partes: las cuentas quedan a nombre del comercio, el prestador entra con un usuario propio y con los permisos justos, y la autorización queda por escrito.
estado: borrador
estabilidad: semi
fuentes:
  - "Ley 26.388, art. 5 (art. 153 bis del Código Penal), Infoleg, leído el 2026-11-24: https://servicios.infoleg.gob.ar/infolegInternet/anexos/140000-144999/141790/norma.htm"
  - "Ley 26.388, reproducción de la Universidad Nacional del Comahue: https://ciberseguridad.uncoma.edu.ar/wp-content/uploads/2022/10/Ley26388-DelitosInformaticos.pdf"
  - "NIC Argentina, Registro de Dominios de Internet: aspectos básicos (2021): https://NIC.ar/sites/default/files/2021-06/Registro_de_Dominios_de_Internet-Aspectos_basicos.pdf"
  - "Shopify, Transferring store ownership: https://help.shopify.com/en/partners/building-stores-for-merchants/transferring-store-ownership"
  - "Shopify, Account security overview: https://help.shopify.com/en/manual/your-account/account-security/account-security-overview"
  - "Shopify Partner Program Agreement, actualizado el 27-02-2026 (lectura parcial, por resumen): https://www.shopify.com/partners/terms"
  - "NIST SP 800-53 rev. 5, controles AC-2 y AC-6 (catálogo OSCAL): https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json"
  - "NIST SP 800-63B-4 (2025): https://pages.nist.gov/800-63-4/sp800-63b.html"
  - "NCSC, Secure your important online accounts: https://www.ncsc.gov.uk/collection/small-organisations-guide-to-cyber-security/secure-your-important-online-accounts"
  - "CISA, Require strong passwords: https://www.cisa.gov/secure-our-world/require-strong-passwords"
  - "Hutt, Who owns your Shopify store code, eCommerce Fastlane (2026-09-29), práctica: https://ecommercefastlane.com/who-owns-your-shopify-store-code-agency-handover-checklist/"
  - "Emprender/.investigacion/acceso-a-las-cuentas-del-cliente.md"
  - "Emprender/.investigacion/contratos-y-datos-contraria.md"
aliases: [cuentas de colaborador, collaborator account, acceso de colaborador, acceso delegado, mínimo privilegio, least privilege, propiedad de las cuentas, offboarding de cliente, compartir contraseñas]
creado: 2026-11-24
revisado:
---

# Acceso a las cuentas del cliente

El acceso a las cuentas del cliente es cómo entra quien arma o cuida una tienda a la tienda, el dominio, los pagos y las herramientas del comercio, y cómo sale. La regla que sostienen las plataformas y las guías de seguridad tiene tres partes: las cuentas quedan a nombre del comercio, el prestador entra con un usuario propio y con los permisos justos, y la autorización queda por escrito.

Es la parte del [contrato de servicio](contrato-de-servicio.md) que más se toca en el día a día. Cómo da acceso cada plataforma, con sus pasos y sus límites, está en la ficha [accesos delegados por plataforma](accesos-delegados-por-plataforma.md). Lo que el prestador puede hacer con los datos que ve al entrar está en [tratamiento de datos por cuenta de otro](tratamiento-de-datos-por-cuenta-de-otro.md).

## Las cuentas son del comercio

La tienda, el dominio y la cuenta de cobro van a nombre del comercio desde el primer día. NIC Argentina lo dice para el dominio: «es necesario que tengas en tus manos su administración, así, siendo titular podrás realizar libremente cualquier trámite, como renovar, delegar o transferir tu dominio». Ninguna plataforma de tiendas lo dice con esas palabras, pero sus mecanismos empujan hacia lo mismo. Shopify no deja transferir una tienda en la que el socio solo es colaborador («You can't transfer a collaboration store»), y para pasar al comercio una tienda que armó el socio hay que desactivar antes Shopify Payments. Abrir los pagos a nombre del comercio desde el principio evita ese paso.

Hay cosas que en la práctica quedan a nombre del prestador: el repositorio del tema, apps instaladas desde su cuenta de socio o licencias pagadas con su tarjeta. Una guía de práctica de 2026 las trata como un riesgo para el comercio, porque dejan de andar cuando se corta la relación. No son un error si el contrato dice quién es el titular, quién paga y qué se transfiere al irse.

## Un usuario propio con los permisos justos

El prestador entra con su propio usuario, nunca con la contraseña del dueño. Shopify lo pide en su guía de seguridad («Don't share your username or password with anyone») y ofrece una cuenta de colaborador en la que el comercio elige los permisos. Tiendanube, Mercado Pago, Google y WordPress tienen usuarios con roles, como cuenta la [ficha](accesos-delegados-por-plataforma.md). El usuario propio deja registro de quién hizo qué, y se puede quitar sin cambiarle la contraseña al dueño.

Los permisos se dan para la tarea y nada más. Es el principio de mínimo privilegio, que el NIST formula así en su control AC-6: «allowing only authorized accesses for users [...] that are necessary to accomplish assigned organizational tasks». Para el cuidado mensual de una tienda alcanza casi siempre con gestionar productos, pedidos y diseño. Los pagos, la facturación y la gestión de usuarios quedan del lado del dueño (inferencia de la base sobre esa regla).

Cada usuario lleva segundo factor y su contraseña vive en un gestor. El NCSC británico dice que activar la verificación en dos pasos es «one of the most effective ways to protect online accounts», y CISA recomienda un gestor de contraseñas para toda la empresa. El NIST obliga a los sistemas a permitir los gestores («SHALL allow the use of password managers») y les prohíbe exigir cambios periódicos de contraseña si no hay señales de compromiso.

> [!IMPORTANT]
> No todo tiene acceso delegado. El email del comercio, algunos registradores de dominio y servicios chicos no ofrecen usuarios con roles, y no se encontró qué recomiendan las fuentes en ese caso. Si no queda otra que usar la contraseña del dueño, el control AC-2 del NIST pide cambiar las credenciales compartidas «when individuals are removed from the group». Aplicado acá: cambiarla cuando el prestador deja de trabajar con el comercio (inferencia de la base).

## Por qué la autorización va por escrito

Entrar a un sistema ajeno sin permiso, o con más permiso del dado, es delito en Argentina. El art. 153 bis del Código Penal, incorporado por la Ley 26.388, reprime con prisión de quince días a seis meses a quien «a sabiendas accediere por cualquier medio, sin la debida autorización o excediendo la que posea, a un sistema o dato informático de acceso restringido». Dos reproducciones de la norma (Infoleg y la Universidad Nacional del Comahue) coinciden en el texto. La palabra que importa es «excediendo». Una autorización escrita, con las cuentas y lo que se puede hacer en cada una, deja claro qué se autorizó si después hay una pelea. No se encontraron fallos sobre prestadores con acceso parcial.

Las plataformas piden lo mismo en sus términos. Según la parte leída del acuerdo de socios de Shopify (por resumen), el socio entra a una tienda solo para el trabajo que el comercio le encargó y responde por la seguridad de su cuenta y por lo que hagan sus empleados y subcontratistas.

## Cómo se sale

Al terminar, el acceso se quita y se deja constancia. El control AC-2 del NIST pide revisar las cuentas, notificar cuando los usuarios «are terminated or transferred» y alinear el proceso con la baja. El NCSC recomienda revisar cada pocos meses quién tiene acceso a las cuentas importantes. Para el prestador, salir bien es una lista corta (síntesis de la base sobre esas guías y la ficha):

1. Pasar al comercio lo que estaba a nombre del prestador y el contrato dice que se transfiere: apps, licencias, repositorio.
2. Quitar los usuarios propios de cada cuenta, o pedirle al comercio que los quite, y anotar la fecha.
3. Cambiar las contraseñas que se hayan compartido.
4. Devolver o destruir los datos personales que se exportaron, como manda la Ley 25.326 (ver [tratamiento de datos por cuenta de otro](tratamiento-de-datos-por-cuenta-de-otro.md#qué-pasa-con-los-datos-al-terminar)).

En Shopify el acceso de colaborador vence solo si nadie de la organización entra durante 90 días. Eso no reemplaza la baja explícita.

## Cómo falla

- **La tienda o el dominio a nombre del prestador.** El comercio no puede irse sin su permiso, y el prestador queda como dueño de algo que no le corresponde. En la práctica eso tensa la relación (no se encontraron casos argentinos documentados).
- **Una sola contraseña para todo el equipo.** No se sabe quién hizo qué, y sacar a una persona obliga a cambiarla en todos lados.
- **Permisos de dueño para todo.** Un error en el cuidado mensual llega a los pagos o a los usuarios.
- **Accesos que nadie quita.** Un año después, el prestador que ya no trabaja con el comercio sigue entrando, con el riesgo del «excediendo» del art. 153 bis.

## Lo que no se encontró

- Qué recomiendan las fuentes cuando una cuenta no tiene acceso delegado.
- Casos argentinos de disputas entre agencia y comercio por la propiedad de una tienda o un dominio.
- Fallos sobre el art. 153 bis aplicado a quien tenía autorización y la excedió en un trabajo.
- Una guía argentina de ciberseguridad para pymes leída entera. La de BA-CSIRT, de la Ciudad de Buenos Aires, solo se vio por resumen.

El recurso canónico para la regla general es la página del NCSC sobre cuentas importantes, que es corta y práctica. Para Shopify, la [página de colaboraciones](https://shopify.dev/docs/apps/build/dev-dashboard/stores/collaborations): fijate en quién define los permisos y en cómo se quita el acceso.
