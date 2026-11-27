---
resumen: >-
  Lo que la Argentina le agrega al registro de clientes, al presupuesto y al pedido de venta: la clave fiscal y la condición frente al IVA del cliente, que deciden la factura; las reglas de la oferta, el presupuesto y la seña; la leyenda de los documentos que no son factura; el precio final al consumidor; la moneda pactada, y los datos personales de clientes e interesados.
estado: vigente
estabilidad: volatil
fuentes:
  - "ARCA, Clases de comprobantes a emitir (leída 2026-11-27): https://www.arca.gob.ar/facturacion/regimen-general/comprobantes.asp"
  - "ARCA, Monotributo, comprobantes: https://www.arca.gob.ar/facturacion/monotributo/comprobantes.asp"
  - "RG ARCA 5616/2024, B.O. 18/12/2024: https://www.argentina.gob.ar/normativa/nacional/norma-407369/texto"
  - "RG ARCA 5824/2026, B.O. 13/02/2026: https://www.argentina.gob.ar/normativa/nacional/norma-423160/texto"
  - "RG ARCA 5762/2025 (texto no leído; error al abrirlo): https://www.argentina.gob.ar/normativa/nacional/norma-417981/texto"
  - "C5N, 28/11/2025, sobre el fin de la factura M: https://www.c5n.com/economia/como-es-la-nueva-forma-facturacion-arca-monotributistas-problemas-n222161"
  - "Ley 24.240 de Defensa del Consumidor, texto consolidado en InfoLEG: https://servicios.infoleg.gob.ar/infolegInternet/anexos/0-4999/638/texact.htm"
  - "Código Civil y Comercial de la Nación, texto consolidado en InfoLEG: https://servicios.infoleg.gob.ar/infolegInternet/anexos/235000-239999/235975/texact.htm"
  - "RG AFIP 1415/2003, texto del B.O. del 13/01/2003 (copia de la UNC): https://www.unc.edu.ar/sites/default/files/RG-AFIP-01415-03.pdf"
  - "ARCA, Situaciones especiales de emisión de comprobantes: https://www.arca.gob.ar/facturacion/comprobantes/situaciones-especiales.asp"
  - "ARCA, Tipos de comprobantes: https://www.arca.gob.ar/facturacion/comprobantes/tipos.asp"
  - "Resolución 4/2025 de la Secretaría de Industria y Comercio, B.O. 17/01/2025: https://www.boletinoficial.gob.ar/detalleAviso/primera/319787/20250117"
  - "Guía oficial de exhibición de precios (Res. 4/2025): https://argentina.gob.ar/sites/default/files/exhibicion_de_precios_resolucion_4_2025_0.pdf"
  - "RG ARCA 5614/2024, B.O. 13/12/2024: https://www.argentina.gob.ar/normativa/nacional/norma-407183/texto"
  - "Ley 25.326 de Protección de Datos Personales, InfoLEG: https://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/texact.htm"
  - "Ley 26.951, Registro Nacional No Llame, B.O. 5/08/2014 (copia del texto): https://www.casi.com.ar/sites/default/files/ley26951-pdf.pdf"
  - "Marval O'Farrell Mairal, DNU 70/2023 y moneda extranjera (según resumen): https://www.marval.com/Publicacion/dnu-702023-15745"
  - "Relacion-con-clientes/.investigacion/argentina.md"
aliases: [CUIT del cliente, condición frente al IVA, condición IVA del receptor, documento no válido como factura, presupuesto en la ley de defensa del consumidor, seña, precio final al consumidor, transparencia fiscal al consumidor]
creado: 2026-11-27
revisado: 2026-11-27
---

# Relación con clientes en la Argentina

Lo que la Argentina le agrega al registro de clientes, al presupuesto y al pedido de venta: la clave fiscal y la condición frente al IVA del cliente, que deciden la factura; las reglas de la oferta, el presupuesto y la seña; la leyenda de los documentos que no son factura; el precio final al consumidor; la moneda pactada, y los datos personales de clientes e interesados.

Es dinero y ley, y cambia seguido: la nota es una copia al 27 de noviembre de 2026 de normas que se leyeron por partes, con un lector que devuelve citas cortas. Casi todo descansa en el texto de la norma y en páginas de ARCA, que no son fuentes independientes entre sí. No reemplaza a un contador ni a un abogado. El concepto general de cada objeto está en [Registro del cliente](Registro-del-cliente/registro-del-cliente.md), [Presupuesto](Presupuesto/presupuesto.md) y [Pedido de venta](Pedido-de-venta/pedido-de-venta.md).

## Qué datos fiscales guarda la ficha del cliente

La condición del cliente frente al IVA decide qué clase de comprobante se le emite, así que es un dato del registro del cliente y no de la factura. Según la matriz de ARCA:

| Quien vende es | Al cliente que es | Emite |
|---|---|---|
| Responsable inscripto | Responsable inscripto o monotributista | A |
| Responsable inscripto | Consumidor final, exento o no alcanzado | B |
| Monotributista o exento | Cualquiera | C |
| Cualquiera | Del exterior (exportación) | E |

La clase M ya no figura. ARCA dice que la RG 5762 la reemplazó desde el 1 de diciembre de 2025 por una variante de la A con la leyenda «Operación sujeta a retención»; una nota de prensa lo menciona, sin citar la resolución. El texto de la RG 5762 no se pudo abrir.

Desde la RG 5616/2024, la factura electrónica tiene que «identificar la condición ante el impuesto al valor agregado del cliente». La [nota de factura electrónica de ARCA](../Comercio-electronico/Normativa/factura-electronica-de-arca.md) registra que, según el manual de ARCA y la prensa, el pedido de autorización se rechaza sin ese dato desde el 1 de diciembre de 2026; no se encontró la norma que fije esa fecha.

Para un consumidor final, la RG 5824/2026 pide identificar al comprador con DNI, CUIL o CDI cuando el importe es igual o superior a «PESOS DIEZ MILLONES ($10.000.000.-)»; el nombre y el domicilio pueden ir como «NR» (no registrado). La CDI es la clave de identificación que ARCA da a quien no tiene CUIT ni CUIL. Según su art. 2, la regla aplica a operaciones concertadas desde el 1 de julio de 2026. Por debajo de ese monto no hace falta identificar al consumidor, salvo que quien vende necesite la CUIT del comprador para deducir el gasto en Ganancias, caso en que se pide sin importar el monto.

De ahí sale lo que la ficha del cliente tiene que tener, que es lectura de la base sobre esas normas: tipo y número de identificación (CUIT, CUIL, CDI o DNI), razón social o nombre, condición frente al IVA (el dato, no la letra del comprobante, que se deduce) y domicilio fiscal. La condición se puede consultar con el servicio de constancia de inscripción de ARCA, que según su catálogo reemplazó al padrón anterior (una sola fuente, por buscador).

> [!NOTE] Sin fuente todavía: la tabla oficial de códigos de condición frente al IVA del receptor, y qué devuelve el servicio de constancia de inscripción.

## El presupuesto como oferta

El Código Civil y Comercial trata al presupuesto dirigido a un cliente como una oferta. El art. 972 la define como «la manifestación dirigida a persona determinada o determinable, con la intención de obligarse». El art. 974 dice que «La oferta obliga al proponente, a no ser que lo contrario resulte de sus términos, de la naturaleza del negocio o de las circunstancias del caso». Según el art. 978, la aceptación tiene que expresar «la plena conformidad con la oferta»: si el cliente cambia algo, eso es una contraoferta. Entre ausentes, el contrato se perfecciona cuando la aceptación «es recibida por el proponente durante el plazo de vigencia de la oferta» (art. 980). Por eso la [vigencia del presupuesto](Presupuesto/vigencia-y-aceptacion.md) no es un detalle de formato.

Si el cliente es consumidor, se suma la Ley 24.240. Su art. 21 abre «En los supuestos contemplados en el artículo anterior», que trata los materiales de una reparación: rige para el presupuesto de una reparación o servicio técnico, no para cualquier presupuesto. Exige un contenido mínimo: identificación del prestador, descripción del trabajo, de los materiales y sus precios y de la mano de obra, el tiempo de realización, si hay garantía y su alcance, el plazo para aceptar el presupuesto y los números de inscripción impositiva y previsional. El art. 22 obliga a avisar al consumidor antes de un costo adicional que no pudo incluirse.

Quién es consumidor lo define el art. 1 de la ley y el art. 1092 del Código: quien adquiere bienes o servicios «como destinatario final». Los servicios de profesionales liberales con título y matrícula quedan afuera, salvo su publicidad (art. 2). Si una empresa que compra algo para usar en su negocio es consumidora es materia de interpretación; no se leyó doctrina ni jurisprudencia, así que no hay que darlo por sentado en ningún sentido.

> [!WARNING] El texto de la Ley 24.240 publicado en argentina.gob.ar es el original de 1993 y trae una exclusión de quienes compran para «procesos de producción» que el texto consolidado de InfoLEG no tiene. Esta nota usa el de InfoLEG.

## La seña

La seña es una forma frecuente de aceptar un presupuesto (ver [vigencia y aceptación](Presupuesto/vigencia-y-aceptacion.md)). El art. 1059 del Código dice que «se interpreta como confirmatoria del acto, excepto que las partes convengan la facultad de arrepentirse». Si se pactó el arrepentimiento, quien entregó la seña la pierde, y quien la recibió «debe restituirla doblada». Según el art. 1060, si la seña es de la misma especie que lo que se debe (plata a cuenta de plata), cuenta como parte del pago cuando el contrato se cumple.

## La leyenda de lo que no es factura

Un presupuesto, una nota de pedido o una orden de trabajo no son comprobantes fiscales. La RG 1415/2003 dice que «se identificarán con la letra "X" y con la leyenda "DOCUMENTO NO VALIDO COMO FACTURA"», ubicadas en el centro de la parte de arriba, y que se guardan a disposición del fisco «durante un período de DOS (2) años». La página vigente de ARCA repite la regla. El remito lleva la misma leyenda con la letra «R», según el texto de 2003; es un documento del despacho, no de este tema.

El texto leído es el original de 2003. La RG 1415 se modificó muchas veces, y no se verificó contra una versión consolidada que el apartado siga igual.

## Precio final y moneda

Al consumidor se le muestra el precio final. La Resolución 4/2025 dice que el precio exhibido «corresponderá al importe total y final que deba abonar el consumidor», y desde el 1 de abril de 2025 exige mostrar, en letra menor, el importe sin impuestos nacionales con la leyenda «PRECIO SIN IMPUESTOS NACIONALES». Rige para la exhibición en comercios y para la publicidad. En los comprobantes, la RG 5614/2024 pide discriminar el IVA contenido bajo la leyenda «Régimen de Transparencia Fiscal al Consumidor (Ley 27.743)». Si alcanza a los monotributistas está en discusión: el texto leído no los excluye, y la prensa y un consejo profesional dicen que ARCA los excluyó en sus preguntas frecuentes, que no se pudieron ver.

Entre empresas no se encontró una norma que obligue a presupuestar con IVA incluido. Presupuestar «más IVA» es práctica, y quien construye el sistema tiene que guardar en cada presupuesto si los precios incluyen impuestos (ver [precio y descuentos](Presupuesto/precio-y-descuentos.md)).

La moneda pactada obliga. El art. 765 del Código, en el texto que le dio el DNU 70/2023, dice: «El deudor solo se libera si entrega las cantidades comprometidas en la moneda pactada». Un estudio jurídico señala que hay debate sobre los contratos anteriores al decreto. Al consumidor, según la guía oficial de la Resolución 4/2025, el precio se muestra en pesos y se puede mostrar además en otra moneda. Si la factura es en moneda extranjera, la RG 5616 pide consignar el tipo de cambio usado.

> [!NOTE] Sin fuente todavía: qué cotización usar entre el presupuesto, el pedido y la factura. La práctica es fijar en el presupuesto la fuente y el momento de la cotización.

## Datos personales de clientes e interesados

Un registro de clientes y contactos es una base de datos personales. Lo general (consentimiento, derechos de acceso y supresión, transferencia al exterior) está en [privacidad de datos personales](../Datos/Gobierno-y-calidad/privacidad-de-datos-personales.md), y lo legal de llamar en frío, en [primer contacto](../Ventas/Prospeccion/primer-contacto.md). Este tema agrega tres cosas:

- **Inscripción ante la AAIP** (Agencia de Acceso a la Información Pública, la autoridad de datos personales): el art. 21 de la Ley 25.326 obliga a inscribir las bases privadas «destinado[s] a proporcionar informes». Si una base de clientes que no da informes a terceros tiene que inscribirse no quedó resuelto en esta investigación.
- **Cliente o interesado cambia qué se puede hacer.** La Ley 26.951 (Registro No Llame) prohíbe llamar a los inscriptos para ofrecer o vender, pero exceptúa, en su art. 8 d, a quien tiene una relación contractual vigente, si la llamada se refiere «al objeto estricto del vínculo». Un cliente con contrato y un [interesado](Seguimiento-comercial/interesado.md) no están en la misma situación. La ley habla de servicios de telefonía; cómo se aplica a la mensajería no se verificó.
- **Guardar de dónde salió cada contacto** y si aceptó recibir publicidad. Es práctica sugerida por la base para poder responder un pedido de acceso o de baja, no una norma con esos términos.
