---
resumen: >-
  En la Argentina la norma le pide a un sistema de gestión que autorice cada comprobante ante ARCA por web service, con contingencia por CAEA, que se integre con el controlador fiscal si lo hay, que entregue libros y regímenes de información en los formatos del fisco y que aplique las alícuotas de los padrones de cada provincia. No se encontró una norma que obligue a homologar el software: lo que se homologa es el controlador fiscal.
estado: vigente
estabilidad: volatil
fuentes:
  - "Software-de-gestion/.investigacion/normativa-argentina.md (2026-11-27)"
  - "ARCA, manual WSFEv1 «RG 4291 – Proyecto FE v4.8», versión anticipada, «Revisión correspondiente al 1 de Diciembre de 2026» (lo que rige desde esa fecha), publicada en la ayuda de factura electrónica: https://www.arca.gob.ar/fe/ayuda/documentos/wsfev1-RG-4291.pdf"
  - "ARCA, manual del desarrollador WSAA, publicación 20.2.19: https://www.arca.gob.ar/ws/WSAA/WSAAmanualDev.pdf"
  - "ARCA, WSAA y certificados: https://www.arca.gob.ar/ws/documentacion/wsaa.asp y https://www.arca.gob.ar/ws/documentacion/certificados.asp"
  - "ARCA, puntos de venta: https://www.arca.gob.ar/facturacion/documentos/puntos-de-venta.pdf"
  - "ARCA, entorno de prueba y homologación externa: https://www.afip.gob.ar/fe/ayuda/entorno-prueba.asp y https://www.arca.gob.ar/fe/ayuda/webservice.asp"
  - "ARCA, catálogo de web services: https://www.arca.gob.ar/ws/documentacion/catalogo.asp"
  - "RG ARCA 5782/2025, B.O. 30/10/2025: https://www.boletinoficial.gob.ar/pdf/aviso/primera/333664/20251030"
  - "RG ARCA 5785/2025, B.O. 03/11/2025: https://www.boletinoficial.gob.ar/pdf/aviso/primera/333886/20251103"
  - "ARCA, contingencias: https://arca.gob.ar/fe/emision-autorizacion/contingencias.asp"
  - "RG AFIP 4892/2020: https://www.argentina.gob.ar/normativa/nacional/norma-345661/texto"
  - "ARCA, especificaciones del QR: https://www.afip.gob.ar/fe/qr/documentos/QRespecificaciones.pdf"
  - "RG AFIP 3561/2013, texto actualizado: https://www.argentina.gob.ar/normativa/nacional/norma-223930/texto"
  - "RG ARCA 5614/2024, B.O. 13/12/2024: https://www.boletinoficial.gob.ar/pdf/aviso/primera/318151/20241213"
  - "RG ARCA 5801/2025, B.O. 16/12/2025 (por el lector de la página): https://www.boletinoficial.gob.ar/detalleAviso/primera/336276/20251216"
  - "RG ARCA 5705/2025: https://www.argentina.gob.ar/normativa/nacional/norma-413494/texto"
  - "RG ARCA 5707/2025: https://www.boletinoficial.gob.ar/pdf/aviso/primera/326299/20250617"
  - "ARCA, importación de comprobantes en IVA Simple: https://arca.gob.ar/iva/iva-simple/especificaciones-especiales.asp"
  - "ARBA, Resolución Normativa 38/2025: https://www.arba.gov.ar/archivos/Tramites/RN%2038-2025.pdf"
  - "KPMG Argentina, novedades tax 05/02/2026 (por resumen): https://kpmg.com/ar/es/home/media/novedades-tax/2026/02/05-de-febrero.html"
  - "Ley 19.550, art. 61: https://servicios.infoleg.gob.ar/infolegInternet/anexos/25000-29999/25553/texact.htm"
  - "RG IGJ 15/2024, resolución y considerandos (sin el Anexo A): https://www.boletinoficial.gob.ar/pdf/aviso/primera/310531/20250613"
aliases: [software de gestión en Argentina, ERP en Argentina, requisitos fiscales de un sistema, localización fiscal argentina, homologación de software, homologación de software de gestión, contingencia de factura electrónica, WSAA, FECompConsultar, QR de la factura electrónica, padrón de alícuotas]
creado: 2026-11-27
revisado: 2026-11-27
---

# Software de gestión en la Argentina

En la Argentina la norma le pide a un sistema de gestión que autorice cada comprobante ante ARCA por web service, con contingencia por CAEA, que se integre con el controlador fiscal si lo hay, que entregue libros y regímenes de información en los formatos del fisco y que aplique las alícuotas de los padrones de cada provincia. No se encontró una norma que obligue a homologar el software: lo que se homologa es el controlador fiscal.

> [!WARNING]
> Ley y dinero: esto no reemplaza a un contador ni a un abogado tributarista. Las normas se leyeron el 2026-11-27 y cambian varias veces por año; antes de construir, se lee la versión vigente del manual y de la norma.

Tres siglas se usan en toda la nota: ARCA es el fisco nacional (la Agencia de Recaudación y Control Aduanero, que reemplazó a la AFIP por el Decreto 953/2024, como cuenta [impuestos en Argentina](../Impuestos/impuestos-en-argentina.md#arca-el-fisco-nacional)); el CAE es el código de autorización electrónico que ARCA le da a cada comprobante en el momento, y el CAEA es un código que se pide por anticipado para una quincena y se informa después ([factura electrónica de ARCA](../Comercio-electronico/Normativa/factura-electronica-de-arca.md)).

Las reglas en sí viven en sus temas: quién factura y con qué letra, en [factura electrónica de ARCA](../Comercio-electronico/Normativa/factura-electronica-de-arca.md); el IVA, en [IVA en Argentina](../Impuestos/Impuestos-al-consumo/iva-en-argentina.md); los regímenes de recaudación, en [retenciones y percepciones en Argentina](../Impuestos/Recaudacion-en-la-fuente/retenciones-y-percepciones-en-argentina.md); el mapa de impuestos, en [impuestos en Argentina](../Impuestos/impuestos-en-argentina.md). En qué paso de cada recorrido cae cada control está en [procesos de negocio en la Argentina](../Procesos-de-negocio/procesos-de-negocio-en-argentina.md). Acá va lo que cada regla le cambia al diseño del sistema, ordenado por la [columna técnica](Columnas-tecnicas/columnas-tecnicas.md) a la que toca.

## El comprobante con CAE como documento

El comprobante electrónico es un [documento con estados](Columnas-tecnicas/documento-y-estados.md) que el sistema no confirma solo: lo confirma ARCA al darle el CAE. Sin CAE no tiene efectos frente a terceros, según la nota de factura electrónica de ARCA, que cita el art. 12 de la RG 4291. Lo general del [comprobante fiscal](../Impuestos/Cumplimiento/comprobante-fiscal.md) (numeración sin huecos, corrección por nota de crédito) vale igual; lo propio de ARCA, según el manual del WSFEv1 v4.8, es esto:

- **La numeración es por tipo de comprobante y punto de venta.** El ejemplo del manual numera «Facturas A, punto de venta 1». Que la correlatividad se lleve por ese par es inferencia de esta base sobre el ejemplo y sobre el método FECompUltimoAutorizado, que pide los dos datos.
- **Los puntos de venta se habilitan por modalidad y no se comparten**: uno para web services, otro para controlador fiscal, otro para exportación, otro para CAEA (puntos de venta de ARCA).
- **Correlatividad numérica y de fecha.** Si en un lote se rechaza un comprobante, los siguientes quedan «no procesado» y hay que corregir y reenviar.
- **Aprobado con observaciones no es rechazado.** Un comprobante con observaciones recibe CAE; uno con un error «excluyente», no. El sistema necesita un estado para cada caso.
- **El QR.** La RG 4892/2020 obliga a quien autoriza por web service a imprimir un QR que no reemplaza ni tapa los datos exigidos; rigió escalonado entre el 1/3/2021 y el 1/6/2021. La especificación de ARCA fija qué codifica (CUIT, punto de venta, tipo, número, importe, moneda, cotización y el código de autorización), con un campo `tipoCodAut` que distingue CAE («E») de CAEA («A»). Su ejemplo todavía usa el dominio viejo de AFIP, mientras el texto fija `https://www.arca.gob.ar/fe/qr/`: vale el texto.
- **La condición frente al IVA del receptor** viaja en cada pedido; desde el 01/12/2026 el web service rechaza el comprobante sin ese dato (manual v4.8, que remite a la RG 5616). El dato sale de los [datos maestros](Columnas-tecnicas/datos-maestros-y-partes.md) del cliente.

### Qué hacer ante un time-out

Si el pedido de CAE no tiene respuesta, el sistema no sabe si ARCA autorizó el comprobante. Reenviarlo da «un error de consecutividad» si ya figura emitido. El manual indica consultar con FECompConsultar (tipo, punto de venta y número), que devuelve lo enviado con su CAE y vencimiento, y FECompUltimoAutorizado para saber dónde quedó la numeración. La consecuencia de diseño, en lectura de esta base, es que la emisión se reintenta consultando antes de reenviar, como en una operación con [clave de idempotencia](../Arquitectura/Sistemas-distribuidos/clave-de-idempotencia.md). Hay una sola fuente: el manual.

### El CAEA pasó a ser la contingencia

Desde el 1 de junio de 2026, la RG 5782/2025 reserva el CAEA para las contingencias del Título III de la RG 4290; antes algunos inscriptos lo usaban como modalidad principal. La RG 5785/2025 lo hace «primera opción de contingencia» para quien factura por web service y pide usar las contingencias «solo» con excepcionalidad. Coinciden la norma, la página de contingencias de ARCA y el manual. Para un sistema, el CAEA es un modo de operación aparte, con su propio punto de venta y su cola de rendición:

| Qué | Regla | Fuente |
|---|---|---|
| Un CAEA por contribuyente y quincena | del 1 al 15 y del 16 a fin de mes; se pide desde los cinco días corridos anteriores | RG 5782, art. 4 |
| Puntos de venta propios | asociados al mismo domicilio que la modalidad principal | RG 5782, art. 5; manual v4.6 |
| Rendición | cada comprobante con fecha y hora de generación, y los puntos sin uso, hasta el octavo día corrido posterior al fin del período | RG 5782, art. 6 |
| Pérdida de la excepcionalidad | 5 % o más de comprobantes por excepción, o contingencia que supera el 5 % de la disponibilidad mensual, dos meses seguidos o tres alternados | página de ARCA; el artículo no se encontró en una norma leída |

Si no se puede usar CAEA, ARCA ordena seguir con el controlador fiscal, «Comprobantes en línea» o CAI. Ninguna norma leída dice cómo detectar que el servicio «no responde»: es una decisión del sistema.

## Fechas, vigencias y plazos que controla el sistema

Varias reglas son de [fechas y vigencias](Columnas-tecnicas/fechas-vigencias-y-cierre.md):

- La fecha del comprobante admite 5 días antes o después de la generación para productos, sin salir del mes, y 10 días para servicios (manual v4.8, campo CbteFch).
- El ticket de acceso dura «alrededor de 12 horas», y pedir otro para el mismo servicio dentro de un lapso preventivo falla: el manual del WSAA pide reusarlo hasta que venza y sincronizar el reloj por NTP, porque un reloj corrido hace rechazar el ticket.
- Las quincenas del CAEA y su rendición al octavo día, de la tabla de arriba.
- Las alícuotas de Ingresos Brutos de cada cliente o proveedor tienen vigencia: cambian con cada padrón (sección siguiente).
- Los manuales de ARCA fechan cada versión con su entrada en vigencia (v4.6 el 01/08/2026, v4.8 el 01/12/2026): el sistema tiene que estar listo para el campo nuevo antes de esa fecha.

## Lo que se integra con ARCA y con las provincias

Todo esto es [integración](Columnas-tecnicas/integracion-y-migracion.md) con un sistema que el desarrollador no controla.

**Autenticación.** El sistema firma un pedido con un certificado digital y el WSAA devuelve un ticket válido para un solo servicio. Los certificados de prueba se gestionan aparte de los de producción. Cuando el sistema factura por cuenta de un cliente, el cliente le delega el servicio con el Administrador de Relaciones de Clave Fiscal.

**Ambiente de homologación.** ARCA da un entorno de pruebas con sus propias URL y certificados de testing. No certifica nada: es un lugar para probar.

**Padrones de ARCA.** Los web services de constancia de inscripción y de padrón devuelven los datos de un CUIT y sirven para validar la condición frente al IVA al dar de alta un cliente (catálogo de ARCA).

**Controlador fiscal.** Es un equipo homologado por ARCA, provisto solo por empresas autorizadas (RG 3561, arts. 1 y 2); la RG 5614 lo repite en sus considerandos citando a la primera, así que cuenta como una sola fuente. El sistema de gestión le manda la venta y el equipo imprime. Esa conexión va por el protocolo de cada fabricante y ninguna norma leída la regula.

**Padrones de percepciones y retenciones de Ingresos Brutos.** Cada provincia asigna a cada contribuyente una alícuota y la publica en un padrón ([Ingresos Brutos](../Impuestos/Impuestos-al-consumo/ingresos-brutos.md)). Según la RN 38/2025 de ARBA, esas alícuotas se publican en el sitio de ARBA o en el de la Comisión Arbitral «para su consulta por parte de los contribuyentes y los agentes de recaudación», y ARBA puede asignarlas por solicitud del contribuyente. Santa Fe publica el suyo «mensualmente», según un resumen de KPMG. El sistema de un [agente de recaudación](../Impuestos/Recaudacion-en-la-fuente/agente-de-recaudacion.md) baja el padrón, guarda la alícuota de cada sujeto con su vigencia y la aplica al facturar o al pagar (inferencia de esta base). Para ARBA hay una sola fuente primaria leída.

## Libros y regímenes de información como reportes

Lo que el fisco pide en archivo son [reportes legales](Columnas-tecnicas/reportes-operativos-y-legales.md) que salen de la base del sistema. Lo general está en [registros fiscales](../Impuestos/Cumplimiento/registros-fiscales.md).

| Régimen | Quién | Qué le pide al sistema | Norma |
|---|---|---|---|
| IVA Simple (F. 2051, Portal IVA) | responsables inscriptos, desde el período noviembre 2025 | ARCA ya tiene lo emitido con CAE; el sistema importa compras y ajustes con los diseños de registro del micrositio de IVA: archivos ANSI, cabecera y alícuotas por separado, en el mismo orden | RG 5705, arts. 3 y 8; RG 5707 |
| Libro de IVA Digital | sujetos exentos en IVA, con excepciones | presentarlo dentro de los primeros 15 días corridos del mes siguiente, aun «SIN MOVIMIENTO» | RG 5707, art. 1, vigente desde el 1/12/2025 |
| SICORE y SIRE | agentes de retención y percepción; SIRE obligatorio para los regímenes de IVA desde el 1/4/2027 | informar cada retención y percepción practicada | [retenciones y percepciones en Argentina](../Impuestos/Recaudacion-en-la-fuente/retenciones-y-percepciones-en-argentina.md#cómo-informa-el-agente-sicore-y-sire) |
| Reportes del controlador fiscal | quien usa controlador | Cinta Testigo Digital (F. 8010) y Resumen de Totales (F. 8011) cada mes, aun sin ventas | RG 5801/2025 |
| Libros contables digitales | sociedades | cada operación individualizada, con sus cuentas, y verificable después | Ley 19.550, art. 61 |
| Libro de sueldos digital | empleadores | la liquidación en un archivo de ancho fijo con conceptos asociados a la grilla de ARCA | [libro de sueldos digital](../Administracion-de-personal-y-nomina/Cargas-y-declaraciones/libro-de-sueldos-digital.md) |

El Libro de IVA Digital no desapareció con IVA Simple: la RG 5705 no deroga la RG 4597, y la RG 5707 deja obligados a los exentos. Las dos normas se leen juntas.

Para los libros contables, el art. 61 permite llevarlos en registros digitales y el diario con asientos globales de hasta un mes ([libros contables en Argentina](../Contabilidad/Registro/libros-contables-en-argentina.md#libros-en-computadora-y-registros-digitales)). La RG IGJ 15/2024 admite, en sus considerandos, conservar el soporte como «archivos identificados con un hash» y aclara que se conserva el soporte y no los servidores. Es el único texto leído que nombra el hash; su Anexo A no se leyó.

## Qué preguntarle a un proveedor

Las reglas de arriba se vuelven preguntas al [elegir un sistema](Implementacion/elegir-un-sistema.md). La lista es lectura de esta base: ninguna fuente leída la arma, y cada pregunta sale de una sección de esta nota.

1. ¿Autoriza por web service con certificado propio de la empresa o por delegación, y quién renueva el certificado?
2. ¿Qué hace ante un time-out: consulta el comprobante antes de reenviar, o reenvía?
3. ¿Opera con CAEA como contingencia, con su punto de venta propio y la rendición de cada quincena dentro del plazo?
4. ¿Ya manda la condición frente al IVA del receptor, y de dónde la toma?
5. ¿Se integra con el controlador fiscal, si la empresa lo usa?
6. ¿Baja y aplica los padrones de Ingresos Brutos de las provincias donde opera la empresa, con la vigencia de cada alícuota?
7. ¿Genera IVA Simple o el Libro de IVA Digital, según corresponda, y los regímenes de SICORE o SIRE si la empresa es agente?
8. ¿Cómo y en cuánto tiempo actualiza el producto cuando ARCA cambia una resolución o una versión del manual?
9. ¿Lleva los libros contables y de sueldos con los requisitos de los registros digitales?

En la demo guionada conviene pedir que emita en el ambiente de homologación una factura, una nota de crédito y un comprobante con rechazo.

## No hay homologación de software de gestión

No se encontró ninguna norma que exija homologar o certificar un software de gestión o de facturación. Es ausencia de evidencia, no evidencia de ausencia: se buscó en el sitio de ARCA y con un buscador, y la única verificación firme sería consultar a ARCA o a un tributarista. Tres cosas se confunden con eso:

- la homologación del **controlador fiscal**, que es del equipo y de su proveedor (RG 3561);
- el **ambiente de homologación** de los web services, que es un entorno de pruebas;
- la **«homologación externa»**, nombre que ARCA le da a la publicación anticipada de manuales para desarrolladores; la página no dice que certifique nada.

ARCA controla al contribuyente: que tenga el certificado y el punto de venta correctos y que respete la correlatividad, con sanciones para él (RG 5785, art. 25). En lectura de esta base, el riesgo del proveedor del sistema es contractual y de reputación.

> [!NOTE] Sin fuente todavía: el texto actualizado de las RG 4290 (Título III), 4291 y 1415, y la conservación de comprobantes electrónicos; una norma que fije el 1/12/2026 para la condición frente al IVA del receptor; el formato y el calendario de los padrones de ARBA, AGIP y las demás provincias; el manual oficial de constatación de comprobantes recibidos y una API de «Mis Comprobantes»; el listado de controladores homologados y cómo se integra un sistema con ellos; el Anexo A de la RG IGJ 15/2024 y las normas de la CNV y de los registros provinciales.

El recurso canónico para quien programa es el manual del WSFEv1 en la ayuda de factura electrónica de ARCA: el historial de versiones (qué rige desde cuándo), «Operatoria ante errores» y la sección del CAEA. Para la autenticación, el §10 del manual del WSAA.
