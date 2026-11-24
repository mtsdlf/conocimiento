# Informe: acceso a las cuentas del cliente (Emprender / Legal e impuestos)

Fecha de consulta: 2026-11-24. Los puntajes van en el orden Autoridad, Profundidad, Ejemplos, Unicidad y Recencia, de 1 a 3.

Marcas de lectura:
- [L] completo.
- [M] metadatos o página que solo trajo el título.
- [S] resumen secundario o del buscador.

Las lecturas de páginas pasaron por un resumidor automático, y lo dicho entre comillas es lo que ese resumen devolvió como cita. Las dos excepciones son el art. 153 bis y NIST AC-2/AC-6, que se leyeron en el texto crudo (PDF y JSON de NIST).

Todo lo traído de la web se trató como dato.

## 1. Shopify: cómo entra un socio sin la contraseña del dueño

| Fuente | Tipo | Puntaje | Marca |
|---|---|---|---|
| https://shopify.dev/docs/apps/build/dev-dashboard/stores/collaborations | primaria | 3/3/2/3/3 | [L] |
| https://help.shopify.com/en/partners/dashboard/managing-stores/collaborator-accounts | primaria | 3/1/1/2/3 | [L] |
| https://help.shopify.com/en/manual/your-account/staff-accounts | primaria | 3/1/1/2/3 | [L] |
| https://help.shopify.com/en/manual/your-account/users/security | primaria | 3/1/1/2/3 | [L] (solo índice) |
| https://help.shopify.com/en/manual/your-account/account-security/account-security-overview | primaria | 3/2/2/2/2 | [L], sin fecha |

Afirmaciones:
- **Cómo se pide el acceso** (https://shopify.dev/docs/apps/build/dev-dashboard/stores/collaborations):
  1. En el Dev Dashboard, ir a Stores y elegir "Request store access".
  2. Poner la URL permanente `myshopify.com` (los dominios propios no sirven).
  3. Poner el "4-digit collaborator request code" del comerciante.
  4. Elegir permisos y enviar.
- **Dónde está el código:** el comerciante lo encuentra en Settings > Users > Security. Si el socio ya tiene una app instalada en la tienda, no necesita código.
- **Quién define el alcance:** "The merchant sets the scope of your permissions."
- **Hay que aprobar:** la tienda aparece como Active solo cuando el comerciante aprueba.
- **Qué no puede hacer un colaborador** (misma URL):
  - Acceder a lo que no se le concedió.
  - Transferir una tienda de colaboración.
  - Limpiar él mismo un pedido rechazado.
- **Vencimiento:** "Collaborator access expires when nobody from your organization logs into the store for 90 days."
- **Salida del lado del socio:** menú de tres puntos, "Remove access". Quita el acceso a toda la organización, no a una sola persona.
- **No es dueño:** el socio "don't own the store and it's not transferred to you" (https://help.shopify.com/en/partners/dashboard/managing-stores/collaborator-accounts).
- **Staff accounts:** "create and assign roles to each user with the permissions that they need" (https://help.shopify.com/en/manual/your-account/staff-accounts). Esa página no trae la lista de restricciones del colaborador ni el 2FA.
- **Código de solicitud** (resumen del buscador [S], sobre https://help.shopify.com/en/manual/your-account/users/security):
  - Se puede regenerar y el viejo deja de funcionar.
  - Se puede desactivar, y entonces "allows anyone to request access".
  - El 2FA no se puede activar por el staff; cada uno lo configura en su cuenta.
  - Ese resumen dice que la imposición a toda la organización no alcanza a los colaboradores.
- **Buenas prácticas de Shopify** (https://help.shopify.com/en/manual/your-account/account-security/account-security-overview):
  - "Don't share your username or password with anyone."
  - Invitar al personal como usuarios, no darles el login propio.
  - Revisar cuentas de staff y colaboradores y reducir permisos a lo necesario.
  - Usar una contraseña distinta por cuenta y un gestor de contraseñas.

## 2. Tiendanube y WooCommerce/WordPress

| Fuente | Tipo | Puntaje | Marca |
|---|---|---|---|
| https://ayuda.tiendanube.com/es_AR/123366-permisos-para-usuarios/como-agregar-mas-usuarios-para-que-administren-mi-tienda | primaria | 3/2/2/2/2 | [L], sin fecha visible |
| https://ayuda.tiendanube.com/es_AR/mi-cuenta-socios/como-agregar-usuarios-para-que-administren-mi-panel-de-socio | primaria | 3/2/1/2/2 | [L] |
| https://ayuda.tiendanube.com/que-permisos-puedo-asignar-a-los-usuarios-de-mi-tiendanube | primaria | 3/?/?/2/? | [S], no se abrió |
| https://woocommerce.com/document/roles-capabilities/ | primaria | 3/2/1/2/2 | [S] |

Tiendanube:
- **Cómo se agrega un usuario:** Configuración > Usuarios y notificaciones > Agregar. Se pone el email y Tiendanube envía un link para completar nombre, apellido y contraseña. Luego se eligen los permisos "si tu plan lo permite" (artículo de la tabla). Un email ya asociado a otra tienda no sirve, porque "solo es posible agregarlo en una única Tiendanube".
- **Plan:** el artículo dice que, "dependiendo del plan que uses", se pueden asignar permisos distintos. En planes sin esa opción, quizá solo exista acceso total (esa lectura viene de [S]).
- **Acceso total:** existe ese perfil y recibe siempre los emails de facturación y vencimiento. Esos emails "no pueden ser desactivados".
- **Permisos por área** [S]: Estadísticas, Ventas, Productos, Diseño, Planes y pagos y Facturación.
- **No se puede quitar al primer usuario** [S]: es el contacto principal de la tienda.
- **El 2FA** de quien invita le pide el código al enviar la invitación.
- **Panel de socio:** el artículo del panel NO explica cómo el socio entra a la tienda del cliente. Solo explica cómo el socio da a su propio equipo acceso a tiendas específicas con usuario propio. Las secciones "Datos de registro", "Datos bancarios", "Comisiones" y "Gestión de datos" son solo para administradores del panel.
- **Cómo entra un socio a la tienda de un cliente:** no se encontró la fuente. Queda como hueco.

WooCommerce/WordPress:
- Administrator: WooCommerce le agrega dos capacidades, "manage WooCommerce" y "view WooCommerce reports" [S].
- Shop Manager: gestiona la tienda y a los clientes. Solo puede editar usuarios cuyos roles estén en la lista editable. No edita archivos ni código [S].
- Discrepancia: guías de terceros (Kinsta, GoDaddy) lo comparan con Editor o dicen que recibe todos los roles de Woo. Prima la documentación de woocommerce.com.
- La página de roles de developer.wordpress.org dio 404 y no se leyó. Falta la fuente primaria de WordPress para Administrator.
- Para el socio: crear un usuario nombrado con el rol mínimo, y Administrator solo si hace falta. Esto es una inferencia de las fuentes, no una cita.

## 3. Otras cuentas

| Fuente | Tipo | Puntaje | Marca |
|---|---|---|---|
| https://support.google.com/webmasters/answer/7687615?hl=en | primaria | 3/3/1/2/3 | [L], sin fecha ("©2026 Google") |
| https://support.google.com/analytics/answer/9305587?hl=en | primaria | 3/3/1/2/3 | [L] |
| https://www.mercadopago.com.ar/developers/es/docs/collaborators | primaria | 3/2/1/2/3 | [L] |
| https://www.mercadopago.com.mx/blog/perfiles-para-empleados-cuenta-negocio | primaria (blog oficial, México) | 2/1/1/1/2 | [S] |
| https://www.facebook.com/business/help/2169003770027706 y /1717412048538897 | primaria | 3/?/?/2/? | [M], solo el título |
| https://support.chatarchitect.com/... y https://www.leadsie.com/blog/give-meta-business-portfolio-access | secundaria (terceros) | 1/2/2/1/2 | [S] |

Google Search Console (https://support.google.com/webmasters/answer/7687615?hl=en):
- Owner: "full control over properties". Agrega y quita usuarios.
- El owner puede ser verificado (con token) o delegado (lo otorga otro owner, sin token).
- Full user: "view rights to all data and can take some actions". No agrega ni quita usuarios.
- Restricted user: "simple view rights on most data".
- Asociado: no ve los datos, solo hace ciertas acciones, como vincular una cuenta de Chrome Web Store.
- Solo un owner (o el de una propiedad padre) agrega usuarios full o restringidos.
- Límites: 100 no-owners por propiedad. Hasta 500 owners verificados más delegados.
- Para la agencia conviene Full user, o owner delegado solo si hace falta verificar o gestionar usuarios. Es inferencia mía.

Google Analytics (https://support.google.com/analytics/answer/9305587?hl=en):
- Roles de mayor a menor: Administrator (gestiona usuarios), Editor (configuración sin gestionar usuarios), Marketer, Analyst, Viewer.
- Se asignan a nivel cuenta o propiedad. Los roles se heredan de cuenta a propiedad.
- Rige el permiso más amplio que tenga el usuario.

Mercado Pago:
- Existe la herramienta "Colaboradores" (https://www.mercadopago.com.ar/developers/es/docs/collaborators). "Cada persona invitada crea su propia cuenta y contraseña".
- Perfiles predefinidos: Cajero (solo cobros y posventa), Encargado de cobros y Administrador de la cuenta (acceso total).
- Hay permisos de integración en tres niveles: gestionar, editar y ver. Sin al menos uno, el colaborador no ve las integraciones.
- Se crean funciones en "Tu cuenta > Gestionar colaboradores" > "Crear rol", y luego se invita por correo.
- La página no describe cómo se elimina a un colaborador. El buscador [S] dice que se quita desde la misma sección.
- Discrepancia entre fuentes:
  - La documentación de developers dice que el invitado "puede tener una cuenta de Mercado Pago o de Mercado Libre".
  - El blog de México y el resumen [S] dicen que el correo no debe estar vinculado a otra cuenta.
  - Hay que probarlo en la UI argentina.
- Resumen [S]: la invitación vence a los 7 días.
- "Operadores" como término no se confirmó. La fuente usa "colaboradores".

Meta Business (portfolio comercial):
- No se pudo leer la ayuda oficial: solo salió el título "Agregar personas a un portfolio comercial y asignar un activo comercial".
- Fuentes de terceros [S]:
  - Business settings > Partners > Add, con el ID del portfolio de la agencia.
  - Dos niveles: partial access y full control.
  - Quitar al socio revoca el acceso a todo lo compartido.
- Es un hueco de fuente primaria. Hay que abrir la ayuda de Meta en el navegador.

## 4. Dominio y NIC Argentina

| Fuente | Tipo | Puntaje | Marca |
|---|---|---|---|
| https://NIC.ar/sites/default/files/2021-06/Registro_de_Dominios_de_Internet-Aspectos_basicos.pdf | primaria, de 2021 | 3/2/1/2/1 | [L], leído con pdftotext |
| https://www.cscglobal.com/cscglobal/pdfs/AR_portal_instructions_Generate_a_New_Relationship_at_AFIP-NIC.ar-SPANISH.pdf | secundaria (CSC) | 1/2/2/1/1 | [S] |

- **Titularidad** (PDF de NIC): "¿Por qué es importante que seas titular de tu dominio de Internet? Un dominio es tu identidad en Internet. Por este motivo, es necesario que tengas en tus manos su administración, así, siendo titular podrás realizar libremente cualquier trámite, como renovar, delegar o transferir tu dominio."
- **Persona autorizada:** el término de NIC es "apoderado". Dice: "En caso de querer que otra persona realice trámites en tu representación, tenés que designarla como apoderada en Trámites a Distancia." El ingreso es con Clave Fiscal nivel 2 o superior.
- **Transferencia:** "te permite otorgarle/pasarle tu dominio a otro usuario u otra usuaria para que sea su nuevo/a titular".
- **Delegación de DNS:** es un trámite distinto de la titularidad. Los datos de delegación "permanecen intactos" en una transferencia.
- **Contactos "alternativos" o "administrador":** no confirmados. La lista del PDF no los trae.
- **El flujo de CSC** [S] (relación en AFIP con "Trámites a Distancia") es de terceros y de años anteriores. Hay que verificarlo contra la plataforma vigente.
- **Registradores comerciales** (dominios .com): no se investigaron.

## 5. Seguridad: fuentes de organismos

| Fuente | Tipo | Puntaje | Marca |
|---|---|---|---|
| NIST SP 800-53 r5, catálogo OSCAL en https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json (texto de AC-2 y AC-6) | primaria | 3/3/1/3/2 | [L] parcial (AC-2 y AC-6) |
| https://pages.nist.gov/800-63-4/sp800-63b.html | primaria | 3/3/1/3/3 | [L] los primeros 100 000 de 289 336 caracteres |
| https://www.ncsc.gov.uk/collection/small-organisations-guide-to-cyber-security/secure-your-important-online-accounts | primaria | 3/2/2/2/2 | [L] |
| https://www.cisa.gov/secure-our-world/require-strong-passwords | primaria | 3/2/1/2/3 | [L] |
| Guía BA-CSIRT para PyMEs y comercios electrónicos (https://buenosaires.gob.ar/sites/default/files/2025-12/Gu%C3%ADa%20para%20PyMEs%2C%20emprendimientos%20y%20comercios%20electr%C3%B3nicos.pdf) | primaria (gobierno de la Ciudad) | 2/?/?/3/3 | [S] |

- **Mínimo privilegio:** NIST AC-6: "Employ the principle of least privilege, allowing only authorized accesses for users (or processes acting on behalf of users) that are necessary to accomplish assigned organizational tasks."
- **Gestión de cuentas:** NIST AC-2 pide:
  - Asignar responsables de las cuentas.
  - Monitorear el uso.
  - Notificar cuando los usuarios "are terminated or transferred".
  - "Review accounts for compliance".
  - Cambiar los autenticadores de cuentas compartidas "when individuals are removed from the group".
  - Alinear el proceso con la baja de personal.
- **NIST 800-63B (publicado 2025-08-26):**
  - "Verifiers SHALL allow the use of password managers and autofill functionality."
  - "subscribers are responsible for protecting their authentication secrets and not disclosing them to others."
  - "Verifiers and CSPs SHALL NOT require subscribers to change passwords periodically."
  - El cambio es obligatorio si hay evidencia de compromiso.
- **NCSC:**
  - "Turning on 2SV is one of the most effective ways to protect online accounts when passwords are still in use."
  - "Any type of 2SV is better than none."
  - Quitar o deshabilitar cuentas sin uso.
  - Revisar quién tiene acceso a las cuentas importantes cada pocos meses.
- **CISA:**
  - Contraseñas de al menos 16 caracteres y únicas.
  - "always use phishing-resistant MFA along with strong passwords".
  - Gestor de contraseñas para toda la empresa.
  - No tiene guía explícita sobre compartir contraseñas.
- **Argentina:** BA-CSIRT recomienda gestores y activar MFA [S]. No se encontró guía de la Dirección Nacional de Ciberseguridad. INCIBE no se consultó.

## 6. Propiedad de las cuentas

| Fuente | Tipo | Puntaje | Marca |
|---|---|---|---|
| https://help.shopify.com/en/partners/building-stores-for-merchants/transferring-store-ownership | primaria | 3/2/1/2/3 | [L] |
| https://www.shopify.com/partners/terms (Partner Program Agreement, "Last updated February 27, 2026") | primaria | 3/3/1/3/3 | [L] primeros 100 000 de 148 858 caracteres |

- **Qué pasa al transferir** (página de transferencia de Shopify): "After the transfer, the merchant owns the store and it leaves your organization." El socio pierde el control y los beneficios de promociones o prueba gratuita. Shopify Payments, Balance, Credit o Capital activos bloquean la transferencia.
- **Colaboración no es propiedad:** "You can't transfer a collaboration store." Si el comerciante quiere ceder la propiedad, la inicia aparte.
- **Detalles del flujo de transferencia** [S]:
  - La transferencia pendiente vence a los 7 días.
  - Tras transferir, el socio queda de colaborador sin acceso a información financiera.
- **Pagos:** Shopify Payments debe desactivarse antes de transferir. Por eso conviene que el comerciante abra los pagos a su nombre desde el inicio.
- **No encontré** una advertencia explícita de Shopify del tipo "la agencia no debería ser dueña de la tienda". La página describe el mecanismo, no da el motivo. Lo mismo vale para Mercado Pago, Tiendanube y el dominio.
- **El motivo** viene de NIC Argentina: es "necesario que tengas en tus manos su administración", porque el titular "podrá realizar libremente cualquier trámite".

## 7. Riesgo legal: art. 153 bis del Código Penal (Ley 26.388)

| Fuente | Tipo | Puntaje | Marca |
|---|---|---|---|
| https://servicios.infoleg.gob.ar/infolegInternet/anexos/140000-144999/141790/norma.htm (Infoleg) | primaria | 3/3/1/2/2 | [L] |
| https://ciberseguridad.uncoma.edu.ar/wp-content/uploads/2022/10/Ley26388-DelitosInformaticos.pdf (Universidad Nacional del Comahue) | reproducción de la norma | 2/3/1/2/2 | [L], con pdftotext |
| https://boletinoficial.buenosaires.gob.ar/normativaba/norma/119328 (Ciudad de Buenos Aires) | reproducción de la norma | 2/3/1/2/2 | [L] |

Texto literal, art. 5 de la Ley 26.388, que incorpora el 153 bis:
> "Artículo 153 bis: Será reprimido con prisión de quince (15) días a seis (6) meses, si no resultare un delito más severamente penado, el que a sabiendas accediere por cualquier medio, sin la debida autorización o excediendo la que posea, a un sistema o dato informático de acceso restringido."
> "La pena será de un (1) mes a un (1) año de prisión cuando el acceso fuese en perjuicio de un sistema o dato informático de un organismo público estatal o de un proveedor de servicios públicos o de servicios financieros."

- **Dos fuentes:** el texto coincide en Infoleg, en el PDF de la Universidad del Comahue (texto crudo) y en la normativa de la Ciudad. Las tres reproducen la misma norma, pero son sitios distintos.
- **Dato de la ley:** sancionada el 4 de junio de 2008 y promulgada de hecho el 24 de junio de 2008 (Infoleg, resumen del resumidor). El Boletín Oficial no apareció en la lectura.
- **Cuidado con la cita:** el texto es "sin la debida autorización" y lleva "a sabiendas". Un resumen de un modelo la citó de memoria como "sin autorización", y otro dio "uno a doce meses". El texto crudo confirma "un (1) mes a un (1) año".
- **Qué muestra:** el tipo penal depende de la autorización y del exceso sobre ella. Por eso conviene dejarla por escrito, con el alcance de cuentas y permisos.
- **Salvedad:** no hallé jurisprudencia propia sobre agencias. Los resultados traían fallos sobre redes sociales de exparejas. No se busca doctrina sobre "exceder" la autorización dada por un comerciante.

## 8. Términos de las plataformas

Partner Program Agreement de Shopify (https://www.shopify.com/partners/terms, "Last updated February 27, 2026"):
- §2.5(10): el socio "may only access Merchant Stores" para el trabajo que el comerciante autorizó, y solo con herramientas listadas por Shopify. Es lectura del resumidor y falta confirmar la redacción exacta.
- §2.5(5): "Partner is responsible for keeping its Partner Account password secure." También: "Each Partner Account login should be associated with a single user."
- §2.5(6) y §9.13: el socio responde por empleados, agentes, subcontratistas y proveedores de servicios.
- §9.15: usar datos del comerciante para IA exige "the relevant Merchant's prior written consent".
- Parte B §5 y §6: una tienda de desarrollo pasa a ser de comerciante por "the transfer by the VAP of ownership". Shopify puede retener la transferencia.
- Las cláusulas están citadas del resumidor y no se verificó el texto literal. Faltan los últimos 48 858 caracteres del documento.

Términos de Tiendanube, Mercado Pago, Google y Meta sobre el socio: no se leyeron. Quedan como hueco.

## 9. Recursos canónicos propuestos

- **Shopify, acceso:** https://shopify.dev/docs/apps/build/dev-dashboard/stores/collaborations. Fijarse en el código de 4 dígitos, el vencimiento a los 90 días y "Remove access".
- **Shopify, términos:** https://www.shopify.com/partners/terms, §2.5 y §9.13. Fijarse en la fecha de última actualización.
- **Shopify, propiedad:** https://help.shopify.com/en/partners/building-stores-for-merchants/transferring-store-ownership. Fijarse en los pagos activos y en "You can't transfer a collaboration store".
- **Tiendanube:** el artículo de agregar usuarios. Fijarse en el plan, en que cada email sirve para una sola tienda y en que el usuario principal es no removible.
- **Google:** https://support.google.com/webmasters/answer/7687615 (owner delegado vs full user) y https://support.google.com/analytics/answer/9305587.
- **Mercado Pago:** https://www.mercadopago.com.ar/developers/es/docs/collaborators. Fijarse en la función "Administrador de la cuenta" y en los permisos de integración.
- **NIC.ar:** el PDF "Registro de Dominios de Internet - Aspectos básicos", secciones 2.1 y apoderamiento. Verificar el instructivo vigente en nic.ar.
- **Seguridad:** NIST SP 800-53 AC-2 y AC-6 (ya en el catálogo OSCAL), NIST SP 800-63B y la página del NCSC sobre cuentas importantes.
- **Legal:** Infoleg, Ley 26.388, art. 5, para el texto literal.

## 10. Huecos

- **Tiendanube:**
  - Cómo entra un socio del Partners Program a la tienda del cliente.
  - La lista oficial de permisos (el artículo "qué permisos puedo asignar..." no se abrió).
  - No hay fecha de última actualización en ningún artículo.
- **WordPress y hosting:** falta la documentación primaria de roles de WordPress y no se investigó el hosting.
- **Meta Business:** no se leyó la ayuda oficial. Todo lo de socios y activos viene de terceros [S].
- **Mercado Pago:**
  - El procedimiento oficial de baja de un colaborador.
  - El requisito del correo de la persona invitada: hay discrepancia entre fuentes.
  - No hay fuente sobre propiedad de la cuenta ni sobre qué pasa si el titular la cierra.
- **NIC Argentina:**
  - Los contactos "alternativos" y "administrador" no figuran. Solo se confirmó "apoderado" vía TAD.
  - No se leyó el instructivo vigente de apoderamiento (el PDF de 2021 solo lo menciona).
- **Registradores comerciales:** no investigados.
- **Argentina, ciberseguridad:** no hay guía de la Dirección Nacional de Ciberseguridad. BA-CSIRT es un resumen del buscador. INCIBE sin consultar.
- **Términos de plataformas:** solo Shopify, y con la mitad final sin leer. Faltan Tiendanube, Mercado Pago, Google y Meta.
- **Registro de accesos:** Shopify menciona un historial de logins y un activity log, pero esas páginas no se abrieron.
- **Casos reales:** no encontré casos ni advertencias documentadas de agencias que retuvieran cuentas. Eso necesitaría otra ronda.
- **Jurisprudencia 153 bis:** nada aplicado a agencias o proveedores con acceso parcial.

No escribí archivos en el repo. En el scratchpad bajé el catálogo OSCAL de NIST para leer AC-2 y AC-6.
