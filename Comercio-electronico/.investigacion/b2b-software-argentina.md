# Quién atiende al B2B en Argentina: software, precios y reseñas

Fecha de consulta: 2026-11-22. Ficha de insumo para `software-b2b-en-argentina`. Escala Admiralty entre paréntesis. Marcas de lectura: [L] texto completo leído con navegador real (script del repo, texto crudo de la página), [L-r] página leída a través de un lector que la resume (el texto literal citado viene de ahí, no verificado contra el crudo), [M] metadatos/listado, [S] resumen del buscador. Todo precio publicado por la empresa es dato con interés comercial.

Límites de esta pasada: se agotó el presupuesto compartido de búsquedas web (200) a mitad del trabajo, así que varias fichas quedaron sin buscar (ver HUECOS). Reddit bloqueó el acceso automatizado.

## 1. Mapa de modelos y quién entra en cada uno

| Modelo | Quién (verificado) | Lista por cliente | Cuenta corriente | App de vendedor / offline | Portal B2B / autoservicio | Precio publicado |
|---|---|---|---|---|---|---|
| Capa mayorista de una tienda | Tiendanube (función nativa, beta) | Sí: "tablas de precios", 1 / 3 / ilimitadas según plan | No mencionada | No | Sí: el cliente inicia sesión y ve su precio; autorregistro | Planes ARS (ver 2.1) |
| Capa mayorista de una tienda (app de terceros) | Mayorista Pro (app de la tienda de apps de Tiendanube) | Grupos de revendedores (1 o hasta 10) | No mencionada | No | Sí | ARS 19.990 / 34.990 por mes |
| Plataforma B2B vertical | VentasxMayor | Sí, por cliente | "Condiciones comerciales por cliente" | Sí: usuarios de vendedor con cartera propia (sin mención de offline en lo leído) | Sí: tienda mayorista y portal de clientes | USD 99/mes, solo Estados Unidos (ver 2.2) |
| ERP con comercial | Dux Software | "Lista de precio" en sus pantallas; portal de clientes | Sí (cobranzas, cuentas por cliente en pantallas de demo) | No encontrado en lo leído | "Portal de clientes" en la lista de funciones | ARS desde 36.000 + IVA/mes |
| ERP con comercial | Contabilium | No encontrado en la página de precios | No encontrado | No | No | ARS desde 122.000 + IVA/mes |
| Contabilidad/gestión | Colppy | "Lista de precios" desde plan Full | No encontrado | App iOS/Android de tablero y facturación, "1 punto de venta" desde Full | No | ARS desde 128.500 + IVA/mes |
| ERP con comercial | Tango (Axoft) | Dato de producto no leído | No leído | "Tango Ventas Mobile" en Google Play (100+ descargas) | Tango Tiendas (para tienda online, gratis para quien ya tiene Tango Gestión [S]) | Solo cotización (no publicado) |
| App de preventa de ERP regional | SID Preventa, Preventa Móvil VAITS, Keuken Preventa, SEN Preventa, Preventa Fácil, DistribuApp, SuperventaMóvil | SID: "Listas de Precio x Cliente" | SID: "facturas pendientes de pago y realizar su cobranza" | Sí (Preventa Fácil: "pedidos de modo offline") | No | No publicado |

## 2. Fichas por actor con precios literales

### 2.1 Tiendanube: capa mayorista nativa

- La función existe como "ventas mayoristas y minoristas" y todavía figura como beta: «Algunas funciones aún no están disponibles en esta fase beta». Está en https://ayuda.tiendanube.com/es_AR/ventas-mayoristas/que-es-y-como-configurar-la-funcion-de-ventas-mayoristas-y-minoristas-de-tiendanube (Última actualización: 19/10/2026) [L] (A2: la leyó una vez y la otra página del mismo centro de ayuda la confirma).
- Qué ofrece: «Visualizar precios exclusivos y reglas específicas por perfil de cliente (minorista o mayorista)», «Permitir que los mayoristas se registren automáticamente con acceso automático a la lista de precios», «Establecer valores mínimos de pedido exclusivamente para mayoristas» [L] (A2).
- Disponibilidad: «Esta funcionalidad no está disponible para los planes Inicial (gratuito) y Esencial.» [L] (A2).
- Tablas por plan, según la FAQ https://ayuda.tiendanube.com/es_AR/ventas-mayoristas/preguntas-frecuentes-sobre-ventas-mayoristas-y-minoristas-por-tiendanube (Última actualización: 26/03/2026) [L-r]: Inicial y Esencial «No disponible»; Impulso «Incluye 1 tabla de precios»; Escala «Permite gestionar hasta 3 tablas de precios»; Evolución «Acceso a tablas de precios ilimitadas» (B2). La página comercial https://www.tiendanube.com/soluciones/ventas-mayoristas [L] repite la grilla: Impulso 1, Escala 3 (la fila de Evolución quedó cortada en la lectura) y dice «Sin costos extra: la funcionalidad de venta por mayor ya está incluida en los planes Impulso, Escala y Tiendanube Evolución.» (A2).
- Límites declarados: promociones y envío gratis creados desde el administrador solo aplican a tiendas minoristas; las estadísticas de ventas no separan mayorista de minorista; los medios de pago y envío son los mismos que en minorista salvo configuración específica por tabla [L] / [L-r]. «De momento, no es posible eliminar la tabla de precios» [L]. Si se desactiva una tabla, «los clientes volverán a ver el precio minorista» [L-r]. Quien no inicia sesión ve el precio minorista [L].
- ERP: «Las tablas de precios aún no se integran, pero sí los hacen pedidos y productos.» y dice tener priorizado crear APIs públicas para integrarlas con apps de facturación [L-r] (A3: es relevante porque limita el cruce con Dux/Tango).
- Planes y precios de la vista por defecto de https://www.tiendanube.com/planes-y-precios [L]: Inicial gratis; Esencial «$27.999 ARS /mes»; Impulso «$79.999 ARS /mes» (marcado "MÁS ELEGIDO"); Escala «$244.999 ARS /mes»; Evolución «A consultar». Hay un selector Mensual/Anual con «-25%» (la página no dice si los precios llevan IVA) (A2 para el dato de la empresa; dato con interés comercial). Menciona «más de 180 mil vendedores en Latinoamérica».
- Observación para el análisis: lo mayorista se paga subiendo de plan. El escalón que lo habilita (Impulso) cuesta ARS 79.999/mes en la vista leída, casi 3 veces el plan Esencial. Para más de una lista (por ejemplo, distribuidor y mayorista y revendedor) hace falta Escala a ARS 244.999/mes.

### 2.2 Apps de la tienda de apps de Tiendanube

- Mayorista Pro https://www.tiendanube.com/tienda-aplicaciones-nube/mayorista-pro [L-r]: Básico «ARS 19.990 por mes, con 1 grupo de revendedores»; Pro «ARS 34.990 por mes, con hasta 10 grupos, mínimos por categoría y CUIT validado»; prueba de 7 días; «Se cobran junto con el plan de Tiendanube». Hasta 6 tramos de descuento por cantidad, grilla por talle y color, pedido mínimo en unidades y monto. Calificación: «Esta app aún no tiene evaluaciones» (0 evaluaciones). Es decir: no hay reseñas que leer. Es un costo adicional al plan (A2 precio; reseñas: dato 1 de que no hay).
- "Preventa y Avisos de Stock" (OsieckiApps) https://www.tiendanube.com/tienda-aplicaciones-nube/preventaapp [L]: $16.900/mes, 5.0 con 2 evaluaciones. No es preventa de vendedores en calle sino reserva de productos sin stock; se lista por el nombre que se presta a confusión al buscar "preventa".
- Integraciones de gestión en la tienda de apps: "Dux Software ERP" («Sincronizá precios stock y facturación automáticamente») y "Odoo by Devoo" aparecen en la portada de https://www.tiendanube.com/tienda-aplicaciones-nube?q=mayorista [L] (la búsqueda por "mayorista" no filtró; solo se leyó la portada, que dice «más de 700 apps»). No se pudo abrir la ficha de Dux (URL adivinada, 404) (HUECO).
- Tango Tiendas / "Tango eCommerce" en la tienda de apps: según el buscador, integración gratis para usuarios de Tango Gestión [S] (C3).

### 2.3 VentasxMayor

- Producto: «B2B ecommerce platform for wholesalers and distributors»; «More than 500 manufacturers, importers and distributors sell wholesale with VentasxMayor» (afirmación propia, no verificada) https://www.ventasxmayor.com [L] (B4).
- Funciones relevantes: listas por cliente («Per-customer price lists», «Per-customer commercial terms»), pedidos mínimos «by amount or units», venta por unidad, caja o bulto, preventa («Pre-orders: sell now, deliver later»), descuentos por volumen, importación de pedidos desde Excel, Mercado Pago integrado, "Customer portal: their orders and reorder", integración con ERP y «Open API» https://ventasxmayor.com/pricing [L].
- Equipo de ventas: «Unlimited sales rep users, each with their own login and customer portfolio» y «Each rep sees only their portfolio» https://ventasxmayor.com/sellers [L]. No se leyó nada sobre modo sin conexión.
- Precio publicado: «ONE PLAN US$ 99.00 /month Tax not incl.», «Implementation included», «No lock-in · No sales commissions»; pero la letra chica dice «Rates apply only in the United States and are subject to updates with 30 days' pri[or notice]» (https://ventasxmayor.com/pricing [L]) (B3). El sitio ofrece selector de país con Argentina («Parece que estás en Argentina. ¿Querés cambiar al sitio de Argentina?»), pero las rutas /ar, /ar/precios, /costo respondieron 404 desde el lector: no se pudo ver el precio para Argentina (HUECO). La FAQ dice «A single fixed monthly price, with no per-sale commissions or hidden costs. Setting up your store is free.» (resumen de lector [L-r]).
- Ejemplos de tiendas que dicen usarlo, con dominios `.com.ar`: mercadodediseño.com.ar, allimitebikes.com.ar, melymayorista.com.ar, watermelonmayorista.com.ar (lista de la portada [L], interés comercial).
- Hay una sección "Compare platforms" https://ventasxmayor.com/compare-with-us que no se leyó: es comparativa hecha por el propio vendedor (HUECO de lectura).

### 2.4 Dux Software (ERP argentino)

Página https://www.duxsoftware.com.ar [L] (precios con interés comercial, A2 para el dato publicado): «Desde $36.000 +IVA por mes». Planes: Inicial $36.000 (hasta 250 comprobantes/mes, 1 tienda online integrada); Estándar $75.300 (1.500 comprobantes, 3 tiendas); Pro $111.200 (5.000 comprobantes, 4 tiendas, API); Full $150.300 (ilimitados, 5 tiendas, API). Todos: «Incluye 1 usuario administrador» y «soporte 24/7». «+4.800 clientes nos eligen desde 2017». Funciones listadas: registro de ventas, POS, facturación electrónica, catálogo, "Portal de clientes", picking, informes por vendedor y cliente. Integraciones: Mercado Libre, Tienda Nube, Woocommerce, Shopify, Prestashop, Empretienda, VTEX. No apareció una app de preventa propia ni cuenta corriente por cliente en el texto de planes (HUECO; hay "cobranzas" en la portada). Los testimonios de la página son del propio vendedor (no se cuentan como reseñas).

### 2.5 Contabilium

https://contabilium.com/ar/planes [L], «Pago mensual / Pago anual -10%»: Standard «$ 122.000 + IVA por mes» (hasta 1.500 comprobantes, 5.000 SKU, 2 usuarios, 3 cuentas integradas con TiendaNube, Mercado Libre, Mercado Pago); Pro «$ 179.000 + IVA» (5.000 comprobantes, 10 usuarios, 4 cuentas); Full «$ 245.000 + IVA» (10.000 comprobantes, usuarios ilimitados, 5 cuentas); Enterprise a medida. Extras: Capacitaciones «$55.500 + IVA», Punto de venta extra «$28.000 + IVA». Lista un rubro «Mayoristas y distribuidores». No apareció preventa ni portal B2B (A2 precio; el resto HUECO).

### 2.6 Colppy

https://www.colppy.com/precios/ [L]: Essential «$128.500 por mes + IVA» (300 comprobantes), Platinum «$189.500» (1.000), Full «$261.500» (3.000; suma «Lista de precios», "App iOS y Android: acceso completo y 1 punto de venta"), Enterprise «$310.900» (7.000). Colppy Plus (con sueldos) «$154.500 por mes + IVA». Enfocado en contabilidad y facturación, no en distribución. «Sin cargo los primeros 7 días» (A2).

### 2.7 Tango (Axoft)

- No publica precio de Tango Gestión: solo cotización o partner (B3: dos fuentes lo sugieren; no se leyó una página oficial de precios). Una guía de la competencia estima «aprox. $638.880 por mes con IVA» (comparador de un rival, C5, no verificable) [S].
- Modalidades de licencia según un formulario de un consejo profesional: venta perpetua con actualización anual opcional, alquiler mensual local y suscripción online mensual [S] (C3).
- Apps móviles en Google Play (todas de Axoft S.A.): Tango Ventas Mobile (100+ descargas, sin calificación visible), Tango Colectora (5.0), Tango connect (4.9, 20 opiniones, 5 K+), Tango nexo (3.2, 39 opiniones, 10 k+), TFactura.io (2.9, 80 opiniones, 10 k+) [M]. Tango Tiendas y Tango Nexo como portal: https://www.tangonexo.com [L] (módulos: clientes, ecommerce, cobranzas, reportes, fichadas, backup).

### 2.8 Apps de preventa en Google Play (Argentina, consulta 2026-11-22)

Datos de las fichas leídas con navegador real [L], tienda en `es_AR`:

| App | Desarrollador | Descargas | Calificación | Detalle |
|---|---|---|---|---|
| SuperventaMóvil: toma pedidos | Mobilenik | 10 k+ | 4.2, 50 opiniones | agenda y ruta, pedido y factura en el sitio, tracking en mapa |
| SID Preventa | WebcronInfo | 1 K+ | 4.5, 26 opiniones | hoja de ruta, «Listas de Precio x Cliente», cobranza de facturas pendientes, «bulto cerrado» |
| Preventa Móvil VAITS | VAITS SRL | 1 K+ | sin calificación | se integra a su ERP |
| Keuken Preventa | Soluciones Informáticas KeuKen | 500+ | sin calificación | pedidos para «cualquier distribuidora», tracking de vendedores |
| Preventa Fácil | Grupo NeoSistemas | 100+ | sin calificación | «pedidos de modo offline», actualizada 19 nov 2026 |
| DistribuApp: Pedidos y Reparto | NeuralAsync | 50+ | sin calificación | preventa, reparto y cobro |
| SEN Preventa | SEN Software | 1+ | sin calificación | para clientes de su ERP |
| Tango Ventas Mobile | Axoft | 100+ | sin calificación | |
| Mercos (Brasil), «Vendas e Pedidos B2B» | Simplest Software | 100 k+ | no leída | aparece en Play Argentina; no se leyeron reseñas |
| Kyte: POS, inventario y tienda | Kyte | 1 M+ | 4.4, 24 mil | POS minorista, no B2B; precios en USD (Kyte 19,99 / 29,99 / 39,99 por mes, https://www.kyteapp.com/pricing [L]) |

Patrón: casi todas son «la app del ERP de un proveedor chico» que exige tener ese ERP («iPreventa... REQUIERE que Vd. disponga TAMBIÉN del ERP iX_Distribución», ficha de App Store https://apps.apple.com/us/app/ipreventa/id514362812 [L], origen español: no es dato argentino). Ninguna publica precio. Descargas bajas (decenas a miles) sugiere mercado fragmentado en software local (B3: inferencia mía).

App Store: Tango connect «has not received enough ratings or reviews to display an overview» https://apps.apple.com/np/app/tango-connect/id1518091726 [L].

## 3. Reseñas leídas una por una

Fuente: diálogo "Ver todas las opiniones" de Google Play, tienda `es_AR`, leído con navegador real el 2026-11-22. Limitación: el diálogo cargó solo parte de las opiniones (orden «Más relevantes», sin filtrar por estrellas ni por fecha; las estrellas de cada reseña no se extrajeron) y mezcla reseñas de 2016 a 2026. Se leyeron TODAS las que cargaron: SuperventaMóvil 25, SID Preventa 5, TFactura.io 49, Tango nexo 13, Tango connect 2; total 94 reseñas. Las respuestas del desarrollador no se cuentan. Calificación general en cada ficha (A2): ver tabla 2.8. Codificación mía, una reseña puede tener dos temas. Las demás apps de preventa de 2.8 no muestran reseñas.

### 3.1 Conteo por tema

| Tema | SuperventaMóvil (25) | SID (5) | TFactura.io (49) | Tango nexo (13) | Tango connect (2) |
|---|---|---|---|---|---|
| Se cae / errores / se cuelga | 2 | 0 | 8 | 5 | 0 |
| No se instala / compatibilidad con Android | 0 | 0 | 21 | 0 | 0 |
| Alta, login y primer uso (curva de uso) | 5 | 1 | 4 | 3 | 0 |
| Lentitud | 1 | 0 | 2 | 3 | 0 |
| Falta de función | 3 | 0 | 3 | 1 | 0 |
| Precio / cobro mensual | 0 | 0 | 3 | 0 | 0 |
| Soporte (queja) | 0 | 0 | 0 | 0 | 0 |
| Sincronización stock/factura | 0 | 0 | 0 | 0 | 0 |
| Offline | 0 | 0 | 0 | 0 | 0 |
| Listas por cliente | 0 | 0 | 0 | 0 | 0 |
| Cuenta corriente | 0 | 0 | 0 | 0 | 0 |
| Positiva sin queja | 13 | 4 | 12 | 3 | 2 |

Lectura: en lo que alcanzó a cargarse, nadie nombra offline, listas por cliente, cuenta corriente ni sincronización. Los usuarios de apps móviles de gestión se quejan de que la app no funciona (instalación, cuelgues, login), no de la profundidad comercial. Eso es dato 2 sobre estas apps, no sobre el uso de preventa en general: la muestra es chica y viene de apps de Play, y el comprador del ERP no suele reseñar en Play (C4). La ausencia de un tema es ausencia en esta muestra, no prueba de que no importe.

### 3.2 Citas literales

TFactura.io (Axoft) https://play.google.com/store/apps/details?id=com.tangofactura [L]:
- Errores y curva: «Malo , muchas fallas que nunca corrigen... Si rotas la pantalla se reinicia la aplicación y perdes tooodo lo que hiciste. Si a esto le sumas el insufrible lag qué tienen los servidores de Tango se vuelve prácticamente inusable.» (16-ago-2024).
- Precio: «Un disgusto que hace DOS AÑOS que pago mensualmente para que este software siga ocupando espacio en mi celu» (misma reseña). «Hola , entendi mal , o cobran x mes para tener la aplicacion ? Le doy 3 estrellas» (9-ago-2020). «Buen costo» (26-may-2021).
- Instalación: «Tengo Android 12 y no puedo instalar la app» (18-feb-2022); «No se puede ni instalar en el celular Samsung A72» (27-abr-2022). La empresa respondió (22-jul-2022): «Ya esta resuelto el problema!». Fueron 21 reseñas de este tipo entre feb y jul de 2022.
- Teclado: «no aparece el teclado cuando seleccionas para modificar la descripción de la factura... osea no se puede usar.» (22-jun-2021). Respuesta: «Tuvimos que re hacer toda la aplicacion de nuevo.»
- Falta de función: «solamente le faltaría el poder enviar los archivos desde cualquier app» (WhatsApp; la empresa respondió que lo resolvió, 12-may-2020). «No puedo crear mi empresa. Me pide declaración de ingresos brutos en caba. Yo soy de Misiones.» (17-abr-2021).
- Login: «Una estrella es mucho!... Ni siquiera guarda el loggin.» (17-jul-2025).
- Positiva: «Excelente aplicación. Muy recomendable para facturar con las aplicaciones de Mercado Libre y Tienda Nube.» (15-abr-2020).

Tango nexo https://play.google.com/store/apps/details?id=com.axoft.nexo_app_v2 [L]:
- «Malisima, lenta, se cuelga si te vas a otra app, muy mal diseñada» (31-jul-2023); «continuamente tildada, una experiencia horrible» (27-sep-2024).
- Falta de función: «no puedo seleccionar la opción de clientes en la aplicación, usaría la página web pero tampoco funciona bien ni permite realizar los pagos» (10-jul-2025).
- Login: «No se puede acceder desde la cuenta de Gmail, al querer ingresar por medio de Gmail, se cuelga la aplicación» (4-mar-2021); «No me deja entrar con una cuenta .hotmail» (2-jun-2021).
- Curva: «Horrible no se entiende nada» (25-sep-2024).

SuperventaMóvil https://play.google.com/store/apps/details?id=com.mobilenik.svm [L]:
- Falta de función: «solo faltan algunos ajustes y complementos, como mejorar el filtrado de productos vendidos... y poder identificar en las listas los clientes ya trabajados y los que faltan en la ruta» (22-may-2025); «Para tomar pedidos de la misma familia de productos hay que entrar y salir lo que hace muy lerdo el proceso de carga del pedido» (7-dic-2019); «Seria de gran ayuda poder acceder de manera más directa a la info de los art. Y sus precios» (26-abr-2021).
- Alta y uso: «No puedo hacer una prueba solo puedo ingresar a página principal» (29-may-2021); «Mire me pide un código» (8-mar-2017; la empresa explicó el «Company ID» recibido al registrarse); «La aplicación no está activa.» (11-jun-2023, de una cuenta que se identifica como distribuidora); «Hola ! No se puede actualizar» (2-mar-2022).
- Positivas, por ejemplo: «Excelente. Me ayudó a tener organizados los pedidos y clientes.» (17-jun-2020).

SID Preventa https://play.google.com/store/apps/details?id=webcroninfo.sidventas [L]: «El mejor sistema operativo de preventa que utilice» (18-jul-2025); «Hola alguien me diría como se usa» (1-may-2024).

Tango connect https://play.google.com/store/apps/details?id=com.axoft.connect [L]: solo 2 reseñas de texto, «Excelente» (24-jul-2020) y «ganar» (22-may-2026).

### 3.3 Reseñas que no se pudieron leer

- Tiendanube: Mayorista Pro no tiene evaluaciones; no se encontraron fichas de otras apps mayoristas (Atacarejo, etc.) por la caída del buscador.
- Capterra, GetApp, G2: https://www.capterra.es/software/1030880/tango-factura devolvió 403 (Cloudflare) y G2 403. No se leyeron (HUECO).
- Reddit: bloqueo de seguridad de red al lector (HUECO). Foros de Tango, grupos públicos y reclamos en Defensa del Consumidor: no se buscaron.

## 4. Lo que la evidencia dice y lo que no

1. Ofrecer precio mayorista como función de tienda ya es estándar entre las plataformas locales de tienda: Tiendanube lo trae nativo desde el plan de ARS 79.999 (Impulso) y lo limita por cantidad de tablas (A2). Falta, según su propia ayuda, la integración de las tablas con ERPs y facturadores (B3).
2. Las plataformas "B2B puro" (VentasxMayor) cubren listas por cliente, equipo de vendedores y portal, pero el precio publicado que se pudo leer es de EE. UU. (USD 99/mes, sin comisión). El precio para Argentina es un HUECO (B3).
3. Los ERPs argentinos publican precios por cantidad de comprobantes y no por usuario: Dux ARS 36.000 a 150.300 + IVA, Contabilium 122.000 a 245.000 + IVA, Colppy 128.500 a 310.900 + IVA (A2, todos con interés comercial, vigentes al 2026-11-22). Tango no publica precios (B3).
4. La preventa en calle está servida por muchas apps chicas atadas a un ERP regional, sin precio público y con pocas reseñas (A3). Los 94 comentarios leídos no se quejan de profundidad comercial sino de instalación, cuelgues y alta (A3; sesgo de muestra explicado en 3.1).
5. Tango y Mercos (Brasil) están presentes en Google Play Argentina; Tango Ventas Mobile tiene 100+ descargas y Mercos 100 k+ en la ficha global (M, B3).

## 5. Recursos canónicos propuestos

- Capacidades y límites de la capa mayorista de una tienda: ayuda de Tiendanube sobre ventas mayoristas, artículos «¿Qué es y cómo configurar...?» y la FAQ https://ayuda.tiendanube.com/es_AR/ventas-mayoristas . Fijarse en la fecha de actualización, la nota de beta y la grilla de tablas por plan.
- Planes de la tienda: https://www.tiendanube.com/planes-y-precios (la fila de cada plan; el precio cambia con inflación, citar siempre fecha).
- Plataforma B2B vertical: https://ventasxmayor.com/pricing (qué se incluye, con su letra chica de país) y /sellers (modelo de vendedor con cartera).
- ERP con comercial: https://www.duxsoftware.com.ar , https://contabilium.com/ar/planes , https://www.colppy.com/precios/ . Fijarse en el eje de cobro (comprobantes, usuarios, cuentas integradas).
- Apps de preventa: fichas de Google Play (`id=webcroninfo.sidventas`, `id=com.mobilenik.svm`, etc.), en la lista de funciones y en «Calificaciones y opiniones».
- Nota metodológica para la ficha: consultar siempre la tienda en `es_AR` y fechar la consulta; los precios de ERP argentinos se desactualizan por inflación en meses.

## 6. HUECOS

- Empretienda (¿modo mayorista?): el sitio rechazó la conexión (error de red) desde empretienda.com.ar y /precios. No se sabe si lo tiene.
- Shopify en Argentina (B2B de Shopify, precio en USD) y WooCommerce con plugins mayoristas: no se leyeron (se agotó el presupuesto de búsqueda).
- VentasxMayor: precio para Argentina, la sección "Compare platforms" y si la app de vendedor trabaja sin conexión.
- Precios de Tango Gestión, Xubio (URL de precios 404), Bsale (timeout), Pedix (404), Mercos Argentina (403), Flexxus, bcn, Finnegans, Bejerman, Sistemas Bit, America Software, Repzo, Pepperi: no leídos.
- Dux: si tiene app de preventa y cuenta corriente por cliente, y si el "Portal de clientes" es B2B; no se pudo abrir su ficha en la tienda de apps de Tiendanube.
- Apps de preventa en App Store de Argentina: solo se leyó iPreventa (España) y Tango connect.
- Reseñas: Capterra/GetApp/G2 bloqueados; Reddit bloqueado; foros de Tango y Defensa del Consumidor no consultados; el diálogo de Play cargó solo parte de las opiniones, sin orden por fecha ni filtro de 1 a 3 estrellas, por lo que las "40 más recientes de 1 a 3 estrellas" no se cumplieron; Kyte (260 reseñas cargadas) no se codificó por ser POS minorista y no B2B; Mercos y las apps de preventa chicas sin reseñas visibles.
- Calificación por estrellas de cada reseña individual: no extraída.
- Datos de mercado (cuántos comercios usan cada uno): solo cifras de autor: «+4.800 clientes» (Dux), «más de 500» (VentasxMayor), «más de 180 mil» (Tiendanube).
- Instrucciones dentro de páginas web: ninguna detectada.
