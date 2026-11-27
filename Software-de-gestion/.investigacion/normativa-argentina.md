# Normativa argentina que le exige algo a un sistema de gestión (investigación cruda)

Fecha de lectura: 2026-11-27. Material de alto riesgo (ley). Marcas: [L] texto completo leído, [M] metadatos o abstract, [S] resumen del buscador o secundario. Puntajes 1 a 3 en autoridad / profundidad / ejemplos / unicidad (A/P/E/U). Todo lo que vino de la web se trató como dato. Los PDF se bajaron y se leyeron con `pdftotext` (copias en la carpeta temporal de la sesión, no en el repo).

Convención de fuentes: «primaria» = texto de la norma o documento técnico de ARCA; «secundaria» = lo demás.

## 0. Qué ya está escrito en el repo (no repetir) y qué es propio de este tema

| Nota existente | Ya dice | Qué queda para el tema Software de gestión |
|---|---|---|
| `Comercio-electronico/Normativa/factura-electronica-de-arca.md` | quién tiene que facturar (RG 5893/2026), letras A/B/C/E, clase M reemplazada, circuito WSAA→WSFEv1 con ticket de 12 h, CAEA excepcional desde 1/6/2026 (RG 5782), WSMTXCA/WSFEX/WSCT nombrados, transparencia fiscal (RG 5614), condición IVA del receptor (RG 5616; fecha 1/12/2026 sin norma leída), manual v4.7 y v4.8 | el detalle técnico por componente de un sistema: numeración y correlatividad, qué hacer ante time-out, contingencia completa (RG 5785), QR, hostnames, WSAA en detalle, puntos de venta por modalidad |
| `Impuestos/Cumplimiento/comprobante-fiscal.md` y `registros-fiscales.md` | lo general (numeración, nota de crédito, clearance, SAF-T, libros de IVA, lista de «qué tiene que poder emitir un sistema» marcada como inferencia) | lo argentino concreto de esa lista, con norma |
| `Impuestos/Impuestos-al-consumo/iva-en-argentina.md` | IVA Simple (RG 5705/2025) «reemplazó al libro de IVA digital» | ver corrección en 5.2: el Libro de IVA Digital sigue vigente para sujetos exentos |
| `Impuestos/Recaudacion-en-la-fuente/retenciones-y-percepciones-en-argentina.md` | SICORE, SIRE (RG 5921/2026), SIRCREB/SIRTAC, padrones de Convenio Multilateral | padrones provinciales de IIBB (ARBA, AGIP): solo hay fuente parcial |
| `Contabilidad/Registro/libros-contables-en-argentina.md` | CCyC 320 y ss., Ley 19.550 art. 61 de forma general; declara «sin fuente» las resoluciones de IGJ | acá se leyó el texto del art. 61 y los considerandos de la RG IGJ 15/2024 |
| `Administracion-de-personal-y-nomina/.../libro-de-sueldos-digital.md` | LSD, Ley 27.802, fin de la rúbrica en CABA | no se investigó de nuevo; solo enlazar |
| `Procesos-de-negocio/procesos-de-negocio-en-argentina.md` | el cierre mensual y los vencimientos | nada propio |

## 1. Web services de comprobante electrónico (WSAA, WSFEv1, WSFEX, WSMTXCA, WSCT)

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Manual WSFEv1 «RG 4291 – Proyecto FE v4.8», «Revisión correspondiente al 1 de Diciembre de 2026», 10.555 líneas de texto: https://www.arca.gob.ar/fe/ayuda/documentos/wsfev1-RG-4291.pdf | primaria | 3/3/3/3 | [L] (historial, URLs, métodos, CAEA, operatoria ante errores; no se leyeron los 10.000 renglones de códigos de error uno por uno) |
| Página ARCA «Webservices de factura electrónica» (lista de manuales): https://www.arca.gob.ar/ws/documentacion/ws-factura-electronica.asp | primaria | 3/1/2/2 | [L] |
| Manual del desarrollador WSAA, «Publicación 20.2.19»: https://www.arca.gob.ar/ws/WSAA/WSAAmanualDev.pdf | primaria | 3/3/3/3 | [L] parcial (arquitectura, errores 10.5-10.7) |
| Página ARCA WSAA: https://www.arca.gob.ar/ws/documentacion/wsaa.asp ; certificados: https://www.arca.gob.ar/ws/documentacion/certificados.asp | primaria | 3/2/1/2 | [L] |
| Manual WSFEXv1 V3.1.1: https://www.arca.gob.ar/ws/documentacion/manuales/WSFEX-Manualparaeldesarrollador_V3.1.1_ARCA.pdf | primaria | 3/3/3/3 | [L] parcial (historial, URLs, métodos de último comprobante) |
| Manual WSMTXCA V 0.25.8: https://www.arca.gob.ar/fe/ayuda/documentos/wsmtxca-RG-2904.pdf | primaria | 3/3/3/3 | [L] parcial (índice, URLs) |
| Puntos de venta (modalidades): https://www.arca.gob.ar/facturacion/documentos/puntos-de-venta.pdf (PDF creado 2024-12-20) | primaria | 3/2/1/3 | [L] |
| Entorno de prueba: https://www.afip.gob.ar/fe/ayuda/entorno-prueba.asp ; Homologación externa: https://www.arca.gob.ar/fe/ayuda/webservice.asp | primaria | 3/1/1/2 | [L] |
| Catálogo de otros WS de negocio: https://www.arca.gob.ar/ws/documentacion/catalogo.asp | primaria | 3/2/1/2 | [L] |
| Cronograma TLS: https://www.arca.gob.ar/ws/documentacion/cronograma-TLS.asp | primaria | 3/1/1/2 | [L] |

### Afirmaciones (cada una con su fuente)

Versiones y fechas vigentes de los manuales
- La página de ARCA lista: WSFEv1 manual V. 4.7; WSFEXV1 V. 3.1.1; WSCT V.1.6.4; WSMTXCA V 0.25.8; WSBFEV1 V. 3.0; WSSEG V.0.9. No da fechas, las manuales se atan a una RG (WSFEv1 a la RG 4.291, WSMTXCA a la RG 2.904, WSFEXV1 a las RG 2.758 y 4.401). Fuente: página de ARCA arriba.
- El manual v4.8, que está en «homologación externa» y no en la lista principal, trae un historial con fecha de entrada en vigencia por versión: 4.1 (01/12/2025, reemplazo de la clase M), 4.3 (01/06/2026, tipos 63 y 64), 4.4 (01/07/2026, entidades financieras y seguros por RG 5866), 4.6 (01/08/2026, cambios del CAEA por RG 5782), 4.7 (01/09/2026, seguros de caución), 4.8 (01/12/2026): «Será obligatorio el campo Condición Frente al IVA del receptor, atento a la entrada en vigencia reglamentada por la Resolución General N°5616. [...] los códigos de error 10245 para CAE y 825 para CAEA quedaran en desuso». Fuente: manual v4.8. Esto confirma por una fuente primaria técnica la fecha del 1/12/2026 que la nota del repo daba solo por manual y prensa; sigue sin leerse una norma que la fije.
- El manual WSFEXV1 3.1.1 es del 18-08-2025 (3.0.0 del 17-03-2025; 3.1.0 del 10-08-2025). Fuente: historial del manual WSFEX.
- Hay diferencia entre la página de ARCA (lista v4.7) y la ayuda de factura electrónica (v4.8). Dos documentos de ARCA, no discrepan: el 4.8 es el adelanto de lo que rige desde 1/12/2026.

Autenticación (WSAA)
- El cliente firma un pedido (TRA) con un certificado digital; el WSAA devuelve un ticket de acceso (TA) con Token y Sign, válido para un solo servicio de negocio, y el cliente envía Token y Sign en cada pedido. Fuente: manual WSAA 20.2.19, §3.
- El TA dura alrededor de 12 horas («alrededor de 12 horas», `expirationTime` lo dice; los ejemplos del manual muestran generación 10:11 y expiración 22:11). El manual avisa que pedir otro TA para el mismo servicio dentro de un lapso preventivo falla con «El CEE ya posee un TA valido para el acceso al WSN solicitado»; el lapso es «10 MINUTOS EN EL WSAA DE TESTING Y 2 MINUTOS EN EL DE PRODUCCION» y puede cambiar sin aviso. Conclusión que el manual da: pedir un TA y reutilizarlo hasta que expire. Fuente: manual WSAA §10.6.
- Hay que sincronizar el reloj, con NTP contra «time.afip.gob.ar» o similar, o el TA se rechaza por tiempo de expiración. Fuente: manual WSAA §10.7.
- URLs: homologación `https://wsaahomo.afip.gov.ar/ws/services/LoginCms`; producción `https://wsaa.afip.gov.ar/ws/services/LoginCms`. Fuente: página WSAA de ARCA.
- Certificados de homologación se gestionan con WSASS, con clave fiscal de «persona física (no de persona jurídica)»; los de producción, con «Administración de Certificados Digitales» y el «Administrador de Relaciones de Clave Fiscal». Hay cadenas de certificación de homologación 2014-2024 y 2022-2034, y de producción 2016-2024 y 2024-2035. Fuente: página de certificados de ARCA. La delegación a un tercero se hace con el Administrador de Relaciones (documento «ADMINREL.DelegarWS.pdf», no leído).
- Seguridad de transporte: ARCA anuncia la baja de TLS 1.0 y 1.1 y pide TLS 1.2; las fechas figuran «Próximamente» para siete hosts (entre ellos servicios1.afip.gob.ar) y no menciona WSAA ni WSFEv1 por nombre. Fuente: cronograma TLS. (Fecha de lectura: 2026-11-27.)

WSFEv1: URLs y métodos
- Homologación `https://wswhomo.afip.gov.ar/wsfev1/service.asmx`, producción `https://servicios1.afip.gov.ar/wsfev1/service.asmx`. Contactos en el propio manual: wsfev1@arca.gov.ar (funcional, homologación), sri@arca.gov.ar (producción), facturaelectronica@arca.gov.ar (normativa). Fuente: manual v4.8.
- Métodos para CAE: FECAESolicitar. Para CAEA: FECAEASolicitar, FECAEAConsultar, FECAEASinMovimientoInformar, FECAEARegInformativo, FECAEASinMovimientoConsultar. Comunes: FEParamGet* (tipos de comprobante, concepto, documento, IVA, moneda, opcionales, tributos, puntos de venta, cotización, actividades, condición IVA del receptor), FEDummy (estado de la infraestructura), FECompUltimoAutorizado, FECompTotXRequest, FECompConsultar. Fuente: manual v4.8, §2.4.1.
- WSFEXV1: homologación `https://wswhomo.afip.gov.ar/wsfexv1/service.asmx`, producción `https://servicios1.afip.gov.ar/wsfexv1/service.asmx`; exige un `Id` de requerimiento por pedido (método FEXGetLast_ID) y tiene FEXGetLast_CMP para el último comprobante. Fuente: manual WSFEX.
- WSMTXCA es otro protocolo y otros hosts: homologación `https://fwshomo.afip.gov.ar/wsmtxca/services/MTXCAService`, producción `https://serviciosjava.afip.gob.ar/wsmtxca/services/MTXCAService`. Fuente: manual WSMTXCA. Alcance: sujetos incluidos en la RG 2.904 (comprobantes con codificación de producto); punto de venta propio «Factura Electrónica - Codificación de Producto - Webservices». Fuente: manual WSMTXCA y puntos de venta.

Numeración, correlatividad y fechas
- «debe existir correlatividad numérica y de fecha»: si en un lote de 100 facturas la 101 se rechaza, las siguientes quedan «no procesado» y hay que corregir y reenviar. Fuente: manual v4.8, «Operatoria ante errores».
- Hay una numeración por tipo de comprobante y punto de venta (el ejemplo del manual usa «Facturas A, punto de venta 1», comprobantes 51 a 150); FECompUltimoAutorizado devuelve el último autorizado dado tipo y punto. Fuente: manual v4.8. Inferencia de la base: la correlatividad es por par (tipo, punto de venta).
- Fecha del comprobante: para concepto productos (1) hasta 5 días anteriores o posteriores a la fecha de generación, sin exceder el mes de presentación; para servicios o productos y servicios (2 o 3), hasta 10 días anteriores o posteriores. Fuente: manual v4.8, campo CbteFch.
- Los puntos de venta se habilitan por modalidad y no se comparten: «Factura Electrónica - RI IVA - Aplicativo y Webservices», «... Monotributo - Webservices», «Comprobantes de Exportación - Webservices», «Controlador Fiscal» (RG 3561), «Codificación de Producto - Webservices» (RG 2904), «Seguros de Caución - Webservices» (RG 2668), «Factuweb» (CAI manual, autoimpresor o imprenta), «Liquidaciones Electrónicas de Servicios Públicos» (RG 3571). Fuente: puntos-de-venta.pdf de ARCA. El método FEParamGetPtosVenta lista los puntos habilitados para CAE y CAEA.
- Un pedido puede traer varios comprobantes: existe el recuperador de cantidad máxima por pedido (FECompTotXRequest). Fuente: manual v4.8.

Qué pasa si no hay respuesta (time-out)
- El manual describe el caso: el cliente manda la solicitud, espera y vence el time-out; no sabe si el servicio asignó el CAE. Si reenvía, «WsfeV1 devolvería un error de consecutividad», porque la factura ya figura emitida. «Para estos casos, se utiliza el método FECompConsultar» (tipo, punto de venta, número), que devuelve lo enviado más el CAE y su vencimiento; FECompUltimoAutorizado sirve para saber dónde quedó. Fuente: manual v4.8, «Operatoria con errores de comunicación». Esto es lo propio de un sistema: la emisión tiene que ser reintentable por consulta antes que por reenvío (inferencia de la base).
- Un comprobante aprobado «con observaciones» recibe CAE; uno rechazado por validación «excluyente» no. Fuente: manual v4.8.

Condición IVA del receptor (RG 5616/2024)
- Campo `CondicionIVAReceptorId` en cada comprobante; método FEParamGetCondicionIvaReceptor para los valores. Era opcional desde el 6/4/2025 y pasa a rechazar la emisión sin el dato desde el 01/12/2026. Fuente: manual v4.8.

### Recurso canónico del componente
Manual WSFEv1 v4.8 (ayuda de factura electrónica de ARCA). Qué parte: el historial de modificaciones (para saber qué rige desde cuándo), «Operatoria ante errores» (reintentos y consecutividad), la sección del CAEA. En qué fijarse: la fecha de «revisión» de cada versión y que el manual lista cambios por RG. Para autenticación: manual WSAA, §10.

## 2. CAE frente a CAEA y contingencia

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| RG ARCA 5782/2025, B.O. 30/10/2025 (texto del aviso): https://www.boletinoficial.gob.ar/pdf/aviso/primera/333664/20251030 | primaria | 3/3/2/3 | [L] |
| RG ARCA 5785/2025, B.O. 03/11/2025: https://www.boletinoficial.gob.ar/pdf/aviso/primera/333886/20251103 | primaria | 3/3/2/3 | [L] |
| ARCA, «Contingencias»: https://arca.gob.ar/fe/emision-autorizacion/contingencias.asp | primaria | 3/2/2/2 | [L] |
| Manual WSFEv1 v4.8, secciones CAEA | primaria | 3/3/3/2 | [L] parcial |
| RG 4290 (Título III, contingencias) texto | primaria | — | no leída (hueco) |

Dos fuentes independientes de la misma regla: el texto de la RG 5782 (norma) y la página de ARCA (comunicación institucional, que repite la norma) más el manual (técnico). La norma manda; las otras dos coinciden.

### Afirmaciones
- «Establecer un procedimiento excepcional de emisión de comprobantes electrónicos para ser utilizado ante las contingencias previstas en el Título III de la Resolución General N° 4.290» y el comprobante lleva el CAEA «en reemplazo del [CAE] a que se refiere el artículo 14 de la RG 4.291» (art. 1, RG 5782). Vigencia: «1 de junio de 2026» (art. 9). Considerandos: el CAEA estaba habilitado como «modalidad principal de emisión» para ciertos responsables inscriptos; se lo reserva como excepción.
- Un único CAEA por contribuyente, válido para dos períodos: del 1 al 15 y del 16 al último día de cada mes; se solicita desde los CINCO (5) días corridos anteriores al inicio del período o dentro del período en que se use (art. 4). Se pide por web service (art. 2). Alcanza a facturas y recibos A (incluidas las leyendas «PAGO EN CBU INFORMADA» y «OPERACIÓN SUJETA A RETENCIÓN»), B y C, y sus notas de crédito y débito (art. 3).
- Hay que habilitar «puntos de venta específicos» para CAEA, «asociados al mismo domicilio de la modalidad de emisión principal» (art. 5).
- Rendición: informar por cada punto de venta, con fecha y hora de generación de cada comprobante, y los puntos de venta no utilizados; «desde el día inmediato siguiente al del inicio del período y hasta el octavo día corrido posterior al de su finalización» (art. 6). Esto es el «régimen de información posterior» del CAEA. Se hace con FECAEARegInformativo o FECAEASinMovimientoInformar (manual v4.8).
- RG 5785 (vigencia 1/6/2026): el CAEA es «primera opción de contingencia» cuando se factura por web service (art. 16 a), RG 4290 sustituido), y las modalidades de contingencia «solo deben ser utilizadas en condiciones de excepcionalidad» (art. 18). ARCA puede no dar CAEA a quien omita rendirlos o omita presentar el F. 2051 de IVA (art. 25 a), dar CAI parcial, o exigir comprobantes electrónicos a quien usa controlador fiscal y omite sus reportes; y puede habilitar solo clases A con leyenda a quien incumpla en 2 meses consecutivos o 3 alternados de los últimos 12.
- Según ARCA, la excepcionalidad se pierde si durante dos meses consecutivos o tres alternados de un año los comprobantes emitidos por excepción (CAEA o CAI) son 5 % o más del total de la sucursal, o el tiempo de contingencia con CAEA supera el 5 % de la disponibilidad mensual de los servicios de ARCA por sucursal; las fallas atribuibles a ARCA no cuentan. La consecuencia: ARCA puede obligar a un controlador fiscal y el contribuyente no podrá emitir comprobantes electrónicos por un año calendario. Fuente: página de contingencias de ARCA (no hallado el artículo exacto en una norma leída: hueco menor).
- Orden de contingencia por web service según ARCA: primero CAEA (RG 5782); si no se puede, controlador fiscal de nueva tecnología (RG 3561), «Comprobantes en Línea» (incluido Facturador Móvil) o CAI (solo autoimpresores, RG 100). Fuente: página de contingencias.
- Cambios técnicos del CAEA en el manual v4.6 (01/08/2026): «Todos los puntos de venta CAEA pasarán a ser considerados como Contingencia»; deben vincularse a un domicilio con CAE o controlador fiscal; el campo `CbteFchHsGen` pasa a ser obligatorio. FECAEASolicitar rechaza la solicitud si el domicilio no tiene un punto de venta CAE o controlador fiscal de nueva tecnología como modalidad principal (código 15016) y observa a quien debe rendiciones de «2 quincenas consecutivas o 4 alternadas» (código 15014). Fuente: manual v4.8.
- Inferencia de la base: para un sistema el CAEA cambia de «alternativa de diseño» a «modo de contingencia» con su propia cola de rendición; no hay una regla en la norma sobre cómo detectar «servicio no responde».

### Recurso canónico
RG 5782/2025 (arts. 4 a 6) y RG 5785/2025 (arts. 15, 16, 18, 25 de la RG 4290). En qué fijarse: el octavo día corrido para rendir y el control de excepcionalidad de la página de contingencias. Hueco: texto actualizado del Título III de la RG 4290.

## 3. QR obligatorio (RG 4892/2020)

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| RG AFIP 4892/2020 (texto en argentina.gob.ar): https://www.argentina.gob.ar/normativa/nacional/norma-345661/texto | primaria | 3/2/1/3 | [L] por resumen del lector del texto (artículos 1 a 5); el texto original no se abrió aparte |
| ARCA, «Especificaciones del QR incluido en las facturas electrónicas» (PDF, creado 2025-02-03): https://www.afip.gob.ar/fe/qr/documentos/QRespecificaciones.pdf | primaria | 3/3/3/3 | [L] |
| Página «Vigencia y aplicación» del QR: https://www.afip.gob.ar/fe/qr/vigencia-y-aplicacion.asp | primaria | — | solo en resultados del buscador [S] |

### Afirmaciones
- Quienes autorizan comprobantes electrónicos según la RG 4.291 deben incluir un QR; este «codificará los datos indicados en el micrositio»; no puede tapar los datos exigidos ni los reemplaza; con «Comprobantes en línea» o «Facturador Móvil» lo agrega ARCA (arts. 1 a 3). Vigencia desde la publicación (B.O. 24/12/2020); para quien factura por web service, escalonado según operaciones netas de IVA de 2020: más de $ 10.000.000 desde 1/3/2021; más de $ 2.000.000 hasta $ 10.000.000 desde 1/4/2021; más de $ 500.000 hasta $ 2.000.000 desde 1/5/2021; todos los demás desde 1/6/2021 (art. 5).
- Especificación técnica (versión 1 del JSON): el QR codifica `{URL}?p={JSON en Base64}` con `{URL}=https://www.arca.gob.ar/fe/qr/`; campos obligatorios `ver`, `fecha` (RFC 3339), `cuit` (11 dígitos), `ptoVta` (hasta 5), `tipoCmp` (hasta 3), `nroCmp` (hasta 8), `importe` (13 enteros y 2 decimales, en la moneda del comprobante), `moneda` (3 caracteres), `ctz` (hasta 6 decimales; 1 si es pesos), `tipoCodAut` («E» para CAE, «A» para CAEA), `codAut` (14 dígitos); «de corresponder» `tipoDocRec` y `nroDocRec`. Fuente: PDF de especificaciones.
- Observación: el PDF de especificaciones de 2025 sigue mostrando como ejemplo la URL `https://www.afip.gob.ar/fe/qr/?p=...` mientras en el texto fija `https://www.arca.gob.ar/fe/qr/`. Hay que tomar el dominio del texto de la especificación, no del ejemplo (dato a comprobar al probar el QR).

### Recurso canónico
PDF «Especificaciones del QR» de ARCA. En qué fijarse: la lista de campos y que `tipoCodAut` distingue CAE de CAEA.

## 4. Controlador fiscal (RG 3561/2013 y modificatorias)

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| RG 3561 texto actualizado (argentina.gob.ar): https://www.argentina.gob.ar/normativa/nacional/norma-223930/texto | primaria | 3/2/1/3 | [L] parcial (arts. 1, 2, 3, 15, 21-30); «Texto actualizado» sin saber hasta qué modificatoria |
| RG ARCA 5614/2024, B.O. 13/12/2024: https://www.boletinoficial.gob.ar/pdf/aviso/primera/318151/20241213 | primaria | 3/3/3/2 | [L] |
| RG ARCA 5801/2025, B.O. 16/12/2025 (reportes mensuales): https://www.boletinoficial.gob.ar/detalleAviso/primera/336276/20251216 | primaria | 3/2/2/3 | [L] por el lector de la página (no se abrió el PDF aparte) |
| ARCA, FE vs. CF: https://www.arca.gob.ar/facturacion/comprobantes/fe-vs-cf.asp | primaria | 3/1/1/1 | [L] |
| Resultados del buscador sobre homologaciones recientes (RG 5728/2025 Kretz, RG 5647/2025, RG 3792/2015, RG 4206/2018) | mixta | 1/1/2/1 | [S] |

### Afirmaciones
- «Los contribuyentes y responsables [...] deberán utilizar el equipamiento electrónico denominado "Controlador Fiscal" homologado por este Organismo» (art. 1). «La obligación de utilizar "Controladores Fiscales", se cumplirá únicamente por medio de algún equipamiento electrónico que haya sido homologado por este Organismo mediante resolución general, el que será provisto a los usuarios exclusivamente por las empresas proveedoras que esta Administración Federal autorice y su red de comercialización» (art. 2, texto actualizado). Fuente: RG 3561. Una sola fuente de ese texto; la RG 5614 (considerandos) lo repite: «la homologación de los equipos y la autorización de los respectivos proveedores serán dispuestas por este Organismo». Dos fuentes, pero una cita a la otra: tratar como una.
- Distingue equipos de «nueva tecnología» (código de registro de seis letras) y de «vieja tecnología» (art. 15); la comercialización de los de vieja tecnología tuvo plazo (art. 30). Lista de equipos homologados publicada en el sitio de ARCA (art. 29). Procedimiento de homologación por fases con intervención del INTI (art. 28, fragmento).
- Cuándo se usa en lugar de la factura electrónica: ARCA dice que RI, exentos y monotributistas «deben utilizar controlador fiscal y/o emitir factura electrónica» y que pueden elegir una modalidad o combinarlas; las MiPyME que operan con una empresa grande o MiPyME adherida a Factura de Crédito Electrónica MiPyMEs deben emitir solo factura electrónica. Fuente: página FE vs. CF (no incorpora RG 5893, ver la nota del repo).
- Transparencia fiscal en el controlador: los de tipo caja registradora «podrán continuar [...] en la medida que se actualice el firmware» para incluir «TRANSPARENCIA FISCAL», «IVA Contenido» y «Otros Impuestos Nacionales Indirectos»; las impresoras fiscales ya homologadas pueden usar líneas libres hasta actualizar (arts. 3 y 4, RG 5614).
- Cambio 2025-2026: la RG 5801/2025 reemplaza el reporte semanal por el mensual, obligatorio aun sin ventas: Cinta Testigo Digital (F. 8010) y Resumen de Totales (F. 8011), vencimiento el 5 del mes siguiente para IVA y exentos y el 7 para el RS; rige desde el 16/12/2025 y alcanza a los reportes de enero de 2026 en adelante; hay que presentar el último reporte antes de dar de baja un equipo. Fuente: RG 5801 (por el lector de la página).
- La RG 5785 (art. 25 c) permite a ARCA exigir comprobantes electrónicos a quien omita los reportes del controlador. Fuente: RG 5785.
- ¿Sigue vigente en 2024-2026? Sí: no hay norma leída que lo derogue; ARCA lo modificó en 2024 (RG 5614) y en 2025 (RG 5801), y sigue homologando modelos por RG (ejemplos por buscador, [S]). La RG 5893/2026 (fuente del repo) lo mantiene como alternativa. Hueco: no se leyó el texto consolidado completo.
- Para el software de gestión: el controlador es un equipo, no un programa; el sistema de gestión se integra con el controlador por el protocolo de cada fabricante, y esa integración no está regulada por una norma leída (hueco). Lo regulado es el equipo, su proveedor y sus reportes.

### Recurso canónico
RG 3561, arts. 1, 2 y 15 (quién debe, qué es homologado, nueva frente a vieja tecnología) más RG 5801/2025 (reportes). Hueco: el listado vigente de equipos homologados en el sitio de ARCA.

## 5. Libro de IVA Digital, IVA Simple y regímenes de información

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| RG ARCA 5707/2025, B.O. 02/06/2025: https://www.boletinoficial.gob.ar/pdf/aviso/primera/326299/20250617 | primaria | 3/3/2/3 | [L] |
| RG ARCA 5705/2025, B.O. 02/06/2025: https://www.argentina.gob.ar/normativa/nacional/norma-413494/texto | primaria | 3/3/2/3 | [L] |
| ARCA, importación de comprobantes en IVA Simple: https://arca.gob.ar/iva/iva-simple/especificaciones-especiales.asp | primaria | 3/2/3/3 | [L] |
| ARCA, catálogo de WS (padrón y constancia de inscripción) | primaria | 3/2/1/2 | [L] |
| Afip SDK (docs de tercero) sobre WSCDC: https://docs.afipsdk.com/paso-a-paso/web-services/constatacion-de-comprobantes | secundaria (producto comercial) | 1/1/2/1 | [S] |
| RG 4597/2019 texto original | primaria | — | no leída (se leyó su modificación 5707) |

### 5.1 Qué dice la norma sobre el formato y la importación
- RG 5705, art. 3: el «Portal IVA» tiene un módulo de «Registración Electrónica de Operaciones», que pone a disposición «los comprobantes emitidos y recibidos registrados en la base de datos» de ARCA; los datos «deberán ser validados» por el contribuyente, «permitiéndose el ingreso de ajustes, modificaciones, incorporaciones y/o eliminaciones, ya sea mediante carga manual o importación de datos». Obligatorio desde el período noviembre 2025 (art. 8); la declaración jurada es el F. 2051 por Portal IVA con clave fiscal nivel 3 (art. 2).
- RG 5707, art. 8 de la RG 4597 sustituido: «Para la registración de los comprobantes de operaciones mediante la importación de datos se deberán observar los diseños de registro que se especifican en el micrositio "IVA"». Fuente: RG 5707.
- Formato según ARCA: archivos en formato ANSI; `.txt` de hasta 10 MB o `.zip` de hasta 10 MB con el `.txt` de hasta 70 MB sin comprimir; un archivo de «Cabecera» y uno de «Alícuotas» por tipo de operación (compras, importación de bienes, importación de servicios, TurIVA, bienes usados); los registros de comprobantes y alícuotas en el mismo orden; en comprobantes B o C la cantidad de alícuotas debe ser 0; en importación de bienes se registra el Despacho de Importación, no la factura del exterior; hay que indicar si los importes están en pesos o en moneda original. Fuente: página de especificaciones de IVA Simple.
- Un buscador sugirió que los diseños tienen 325 posiciones para compras y 266 para ventas [S]: no se verificó en el PDF oficial; no usar.

### 5.2 Corrección a una nota del repo: el Libro de IVA Digital sigue vigente, para otros
- La RG 5707/2025 (art. 1, que sustituye el art. 2 de la RG 4597) dice que «se encuentran obligados a registrar electrónicamente sus operaciones mediante el "Libro de IVA Digital" los sujetos exentos en el impuesto al valor agregado», con excepciones (reparticiones del Estado, directores de S.A., monotributistas, etc.). Presentación dentro de los primeros QUINCE (15) días corridos del mes siguiente, aun sin operaciones («SIN MOVIMIENTO»). Vigencia: 1/12/2025 (la derogación del Título II, IVA Simplificado, desde el 1/7/2025). Fuente: RG 5707.
- La RG 5705 no abroga la RG 4597 (su lista de normas abrogadas es 715, 765, 826, 1.045, 1.479, 1.625, 1.723, 1.950, 2.030, 2.035, 2.171, 2.210, 4.591, 4.629, 4.777, 5.591 y 5.658, art. 7). Para períodos junio a octubre 2025, quien optó por el F. 2051 quedó exento del Libro de IVA Digital (art. 8).
- Lo que dice `iva-en-argentina.md` («IVA Simple reemplazó al libro de IVA digital») es cierto para los responsables inscriptos desde noviembre 2025; no lo es para los sujetos exentos, a los que la RG 5707 deja obligados. Leer las dos normas juntas. Dos fuentes primarias que se complementan.

### 5.3 Regímenes de información y «lo que ARCA ya tiene»
- Lo que se emite con CAE ya está en ARCA y IVA Simple parte de esa base (RG 5705, art. 3 a). Un sistema no tiene que volver a «subir» las ventas emitidas por web service, pero sí cargar o importar las compras y los ajustes.
- SICORE y SIRE (retenciones y percepciones): ver `retenciones-y-percepciones-en-argentina.md` (RG 2233, RG 3726, RG 4523, RG 5921/2026 con SIRE obligatorio para IVA desde 1/4/2027). No se reinvestigó.
- «Constatación de comprobantes»: ARCA ofrece una consulta para comprobar si un comprobante recibido está autorizado (página «Constatación de comprobantes», https://serviciosweb.afip.gob.ar/genericos/comprobantes/Default.aspx); existe además un WS (WSCDC; manual v2 por Afip SDK [S], sin abrir). Hueco: no se leyó el manual de ARCA ni se encontró una API oficial para bajar «Mis Comprobantes».
- Servicios de padrón por web service: Constancia de Inscripción (v4.1; desde 11/2/2026 `getPersona_v2` agrega `fechaSolicitud`), Alcance 4 (v1.3, con datos de prueba), Alcance 10 (v1.2), Alcance 13 (v1.4), Alcance 100 (v2.1); Alcance 5 y Padrón nivel 3 y 10 deprecados. Fuente: catálogo de ARCA. Sirven para validar CUIT y condición frente al IVA del cliente al darlo de alta.

### Recurso canónico
RG 5707/2025 (art. 1, puntos 1, 5, 7, 9) más RG 5705/2025 (arts. 2, 3, 8). En qué fijarse: quién sigue obligado al Libro de IVA Digital y que la importación debe seguir los diseños de registro del micrositio de ARCA.

## 6. Padrones de alícuotas de Ingresos Brutos (ARBA, AGIP, Convenio Multilateral)

Una sola fuente primaria de peso para ARBA, otra parcial para CABA; el tema queda como hueco abierto.

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| ARBA, Resolución Normativa 38/2025 (31/12/2025): https://www.arba.gov.ar/archivos/Tramites/RN%2038-2025.pdf | primaria | 3/2/1/3 | [L] (considerandos y arts. 1-2) |
| Alícuotas de recaudación: ARBA RN 2/2013 (mecanismo de cálculo): https://www.arba.gov.ar/archivos/Tramites/RN%202-2013.pdf | primaria | — | [M] solo por buscador |
| KPMG Argentina, novedades tax 05/02/2026 (Santa Fe, PARP, RGAPI 37/2025): https://kpmg.com/ar/es/home/media/novedades-tax/2026/02/05-de-febrero.html | secundaria (consultora con interés comercial) | 2/1/1/2 | [S] |
| Resoluciones de AGIP (Res. 296/2019 y otras) | primaria | — | [M], no leídas |

- Según los considerandos de la RN 38/2025 de ARBA, en los regímenes en que el agente aplica alícuotas «calculadas y asignadas a cada contribuyente por esta Agencia de Recaudación», «dichas alícuotas son incorporadas en los padrones que se publican en el sitio oficial de internet [...] (www.arba.gob.ar) o de la Comisión Arbitral del Convenio Multilateral (www.ca.gob.ar), según el caso, para su consulta por parte de los contribuyentes y los agentes de recaudación». La misma norma crea un mecanismo alternativo, por solicitud del contribuyente por Autogestión, para que ARBA asigne las alícuotas (mínimas en acreditaciones bancarias, y las que permitan migrar el nivel hacia los regímenes con padrón). Consecuencia para un sistema: la alícuota de un cliente o proveedor cambia por decisión de ARBA, no solo por cambio de datos del contribuyente.
- Santa Fe: según KPMG [S], se creó el Padrón de Alícuotas de Retención/Percepción (PARP), «publicado mensualmente» y de consulta obligatoria para los agentes (RGAPI 37/2025, no leída).
- SIRCREB: padrón mensual, TXT en zip, publicado «el penúltimo día hábil del mes anterior» (RG CA 6/2023, Anexo I, p. 2; dato ya en `retenciones-y-percepciones-en-argentina.md`).
- Un resultado de buscador sobre ARBA indica archivos de DDJJ de agentes en TXT/zip con diseño de registro A-122R vigente desde 1/3/2026 [S, no abierto]: no usar.
- Hueco: el formato del archivo de padrón de ARBA, el sitio y el calendario de publicación de AGIP, y las provincias restantes. No se encontró la especificación técnica.

## 7. Libros contables en soporte digital (Ley 19.550 art. 61, IGJ)

### Fuentes

| Fuente | Tipo | A/P/E/U | Marca |
|---|---|---|---|
| Ley 19.550 t.o. 1984, art. 61 (InfoLEG): https://servicios.infoleg.gob.ar/infolegInternet/anexos/25000-29999/25553/texact.htm | primaria | 3/3/2/3 | [L] el artículo 61 completo |
| RG IGJ 15/2024 (considerandos), B.O. 16/07/2024: https://www.boletinoficial.gob.ar/pdf/aviso/primera/310531/20250613 | primaria | 3/2/2/3 | [L] resolución y considerandos; **no** el Anexo A |
| RG IGJ 11/2026, B.O. 22/09/2026: https://www.colegio-escribanos.org.ar/noticias/2026_09_22_Res-Gral-11-26.pdf | primaria (copia de un colegio profesional) | 3/1/2/2 | [L] parcial (arts. 52 y siguientes, mención del Título IX) |
| Buscador: RG IGJ 5/2026, 7/2026, 9/2026 (trámites digitales) | secundaria | — | [S] |

### Afirmaciones
- Art. 61 (sustituido por el art. 21 de la Ley 27.444, B.O. 18/6/2018): «Podrá prescindirse del cumplimiento de las formalidades impuestas por los artículos 73, 162, 213, 238 y 290 de la presente ley, como así también de las impuestas por los artículos 320 y subsiguientes del Código Civil y Comercial de la Nación para llevar los libros societarios y contables por Registros Digitales mediante medios digitales de igual manera y forma que los registros digitales de las Sociedades por Acciones Simplificadas instituidos por la ley 27.349». «El libro diario podrá ser llevado con asientos globales que no comprendan períodos mayores de un (1) mes». «El sistema de contabilización debe permitir la individualización de las operaciones, las correspondientes cuentas deudoras y acreedoras y su posterior verificación, con arreglo al artículo 321 del [CCyC]». La CNV dicta la norma para las sociedades bajo su control; los registros públicos deben implementar «un sistema al solo efecto de comprobar el cumplimiento del tracto registral».
- Lo que esto le pide a un sistema, solo con el texto de la ley: que cada operación se pueda individualizar y verificar después, con sus cuentas deudoras y acreedoras. «Inalterabilidad» y «rúbrica digital» están en otras normas: el CCyC art. 324 («la inalterabilidad de las registraciones», ya leído en `libros-contables-en-argentina.md`) y, para las sociedades, la reglamentación de IGJ y de cada Registro Público (no leída).
- RG IGJ 15/2024, considerando 42: en los casos de sustitución de libros por «ordenadores, medios mecánicos o magnéticos», la obligación de conservar en la sede social «se refiere al soporte en que se vuelque la información y no a los servidores en que se procese la misma»; se admite como soporte de conservación «archivos identificados con un hash», porque los CD/DVD ya no se consiguen. También elimina la presentación bianual de la información de medios mecánicos y mantiene la anual (considerando 43). Es el único texto leído que menciona el hash.
- RG IGJ 11/2026 menciona un «Libro digital conforme el Título IX» y dice que el acta digital «suscripta mediante firma digital por la totalidad de los participantes» se tiene por documentación auténtica; el texto de ese Título IX no se leyó.
- Sobre los demás libros digitales (SAS, Ley 27.349): no se leyó. Libros de sueldos: ver nota existente.

### Recurso canónico
Ley 19.550 art. 61 + RG IGJ 15/2024 (Anexo A, Título IX, no leído). Hueco: el Anexo A. Además, las exigencias para sociedades de jurisdicciones provinciales, y las de la CNV.

## 8. ¿Existe homologación obligatoria de software de gestión en Argentina?

Hallazgo: no se encontró ninguna norma que exija homologar o certificar un software de gestión o de facturación. Lo que existe y se confunde con eso, son tres cosas distintas:

| Cosa | Qué es | Fuente |
|---|---|---|
| Homologación de controladores fiscales | del equipo (hardware con firmware) y de su proveedor, por RG de ARCA; vigencia máxima de 5 años según un texto sobre la norma [S] | RG 3561 arts. 1, 2, 28-29 [L]; RG 5614 considerandos [L] |
| «Ambiente de homologación» de los web services | un entorno de pruebas, con certificados de testing (WSASS), sin certificación del producto | páginas «Entorno de prueba» y WSAA de ARCA [L] |
| «Homologación externa» de ARCA | nombre que ARCA le da a la publicación de los manuales de adecuación para desarrolladores (aquí, los de la RG 5616/2024) | https://www.arca.gob.ar/fe/ayuda/webservice.asp [L]: la página no dice si es obligatoria ni que certifique nada |

- Lo que ARCA sí controla del lado del emisor: que el contribuyente (no el software) tenga el certificado asociado al servicio y un punto de venta de la modalidad correcta; que respete la correlatividad; y que cumpla la norma, que le impone sanciones al contribuyente (RG 5785, art. 25). Un sistema no recibe un sello.
- Alcance de la ausencia: la afirmación «no existe» se apoya en no haber hallado la norma, no en una norma que lo diga. Se buscó en el sitio de ARCA y con el buscador (una sola ronda amplia más las páginas de ARCA arriba). Declarar: **ausencia de evidencia, no evidencia de ausencia**. Una sola vía de verificación posible: consultar a ARCA o a un abogado tributarista. Hay excepciones en otros ámbitos que no se investigaron (por ejemplo, software para juegos de azar o depositarios fieles: ARCA tiene registros de proveedores de sistemas de transmisión en otras áreas; el buscador devolvió esa página: https://www.afip.gob.ar/juegosdeazar/registro-informacion/sistema-transmision/proveedores.asp, sin leerla).
- Inferencia de la base (no de una norma): el riesgo del proveedor de software es contractual y reputacional, y el cliente (el contribuyente) es quien responde ante ARCA.

## 9. Cambios 2024-2026 que tocan al sistema (cronología)

| Fecha | Cambio | Fuente | Marca |
|---|---|---|---|
| 24/10/2024 (B.O. 25/10/2024) | Decreto 953/2024: disuelve la AFIP y crea la ARCA; la ARCA mantiene la misma CUIT y asume sus competencias | https://www.argentina.gob.ar/normativa/nacional/decreto-953-2024-405666 | [S] (por buscador; no se abrió el decreto; sí se leyó que las RG de 2024 en adelante lo citan en sus fundamentos) |
| 13/12/2024 | RG 5614: «Ley N° 27.743, Título VII - Régimen de Transparencia Fiscal al Consumidor»; art. 99 de la ley: discriminar IVA y demás impuestos nacionales indirectos; desde 1/1/2025 para empresas grandes, desde 1/4/2025 obligatorio para el resto; art. 7: referencias a la AFIP se entienden hechas a ARCA | https://www.boletinoficial.gob.ar/pdf/aviso/primera/318151/20241213 | [L] |
| 18/12/2024 | RG 5616: condición IVA del receptor | nota del repo; manual v4.8 | ver §1 |
| 15/4/2025 | web service nuevo obligatorio por RG 5616 (dato del repo, sin releer) | repo | — |
| 27/5/2025 | RG 5700: consumidor final identificado (dato del repo) | repo | — |
| 2/6/2025 | RG 5705 (IVA Simple) y RG 5707 (Libro de IVA Digital solo para exentos) | ver §5 | [L] |
| 1/12/2025 | clase M reemplazada (RG 5762) | repo; manual v4.8 | — |
| 16/12/2025 | RG 5801: reportes mensuales de controladores fiscales | ver §4 | [L] |
| 30/10 y 3/11/2025, vigencia 1/6/2026 | RG 5782 y 5785: CAEA solo contingencia | ver §2 | [L] |
| 1/7/2026 y 1/9/2026 | RG 5866 (entidades financieras) y seguros de caución en WSFEv1 | manual v4.8 | [L] solo mención; la RG 5866 no se leyó |
| 1/11/2026 | RG 5893: obligación de facturar a monotributistas | nota del repo | no releída |
| 1/12/2026 | condición IVA del receptor obligatoria en el web service | manual v4.8 | [L] |
| 1/4/2027 | SIRE obligatorio para retenciones y percepciones de IVA (RG 5921/2026) | nota del repo | no releída |

Dato de método: la Ley 27.743, art. 99, está citado en los considerandos de la RG 5614 (único texto leído). La ley en sí no se abrió.

## 10. Divisiones del tema frente a cómo divide el campo

El árbol propone una nota única «software-de-gestion-en-argentina» para la normativa. La normativa se divide en el campo (y en ARCA) por régimen (comprobantes, libros, información, controlador fiscal), no por «sistema». Lo que sí es propio del tema es el cruce: qué tiene que hacer el sistema ante cada régimen. Sugerencia: una nota con una tabla régimen → qué le exige al sistema → norma, y enlaces a las notas de dominio. No hay nada que sea de «normativa de software» como cuerpo aparte: tampoco hay, que se haya encontrado, ni homologación ni registro de software.

## 11. Huecos (lo que no se encontró o no se leyó)

1. Texto actualizado de la RG 4291, la RG 4290 (Título III de contingencias) y la RG 1415 (requisitos del comprobante, conservación de comprobantes electrónicos): no leídos. La conservación de comprobantes electrónicos (plazo y forma) no se investigó.
2. Una norma que fije el 1/12/2026 para la condición IVA del receptor: solo el manual de ARCA y la RG 5616 por la nota del repo.
3. Fecha exacta de RG 5616 y de las demás RG que cita el repo: no se releyeron.
4. Manual WSAA: 20.2.19, ARCA no publica fecha en su página; ticket de 12 h es lo que el manual dice «alrededor de». No se verificó la vigencia actual del lapso de 2 minutos.
5. Padrones de IIBB de ARBA y AGIP: formato, calendario, certificados de exclusión; Santa Fe y otras provincias por fuente secundaria.
6. Anexo A, Título IX de la RG IGJ 15/2024 (libros digitales y su rúbrica); RG IGJ 5/2026, 7/2026 y 9/2026 solo por buscador; CNV.
7. Si existe un registro o requisito para el software de gestión: no se encontró; no está probada su ausencia (ver §8).
8. API oficial de «Mis Comprobantes» y manual WSCDC de ARCA.
9. Controlador fiscal: listado de equipos homologados, costos y cómo se integra un sistema; el texto consolidado de la RG 3561.
10. Decreto 953/2024 y Ley 27.743: solo vía considerandos y buscador.
11. Cuántos sistemas o contribuyentes usan WSFEv1: no se buscó.
12. RG 5866/2026, RG 5893/2026 y RG 5921/2026: no releídas en esta pasada.
