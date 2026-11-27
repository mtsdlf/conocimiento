# Investigación: Pago de sueldos en Argentina (Tesorería)

Fecha de lectura: 2026-11-27. Capa cruda, sin frontmatter. Marcas: [L] leído en la fuente (texto completo o la parte citada), [M] solo metadatos o resumen del extractor de páginas, [S] resumen secundario o del buscador.
Puntajes 1 a 3 en autoridad / profundidad / ejemplos / unicidad.

Nota de método: los PDF del BCRA, la Ley 27.802 del Boletín Oficial, la LCT de InfoLEG, el Decreto 380/2001 de la biblioteca de ARCA y las RG del calendario se bajaron con curl y se leyeron con pdftotext o quitando el HTML (marca [L]). La cuota de búsquedas web se agotó a mitad del trabajo; lo que no se pudo ubicar por URL directa está en «Huecos». No repito lo que ya está en `Administracion-de-personal-y-nomina/Liquidacion-de-sueldos/liquidacion-en-argentina.md` (art. 124, 126, 128, inembargabilidad) ni en `Tesoreria/tesoreria-en-argentina.md` (transferencias inmediatas, límites UVA); solo lo confirmo o lo corrijo donde hace falta.

## 0. Fuentes (tabla)

| # | Fuente | Tipo | Aut/Prof/Ej/Uni | Marca | URL |
|---|---|---|---|---|---|
| F1 | BCRA, texto ordenado «Depósitos de ahorro, cuenta sueldo y especiales», al 29/10/26 (última comunicación «A» 8498) | primaria | 3/3/2/3 | [L] sección 2 completa, puntos 1.8, 1.10.3, 4.10, 4.11 y la tabla de origen de la sección 2 | https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-depaho.pdf |
| F2 | BCRA, Comunicación «A» 8460 del 24/07/2026 (cuenta sueldo en dólares) | primaria | 3/2/1/3 | [L] | https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8460.pdf |
| F3 | BCRA, Comunicación «A» 8479 del 11/09/2026 (hojas del TO y aclaraciones) | primaria | 3/1/1/2 | [L] la carta; el anexo son las hojas ya leídas en F1 | https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A8479.pdf |
| F4 | BCRA, Comunicación «A» 6042 del 12/08/2016, «Portabilidad y competencia» | primaria | 3/3/1/3 | [L] puntos 1 a 6 | https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A6042.pdf |
| F5 | BCRA, Comunicación «A» 5091 del 24/06/2010 (adecuación a la Ley 26.590) | primaria | 3/2/1/2 | [L] carta y puntos 1 a 4; el anexo (sección 2 de 2010) no se leyó | https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A5091.pdf |
| F6 | BCRA, Comunicación «A» 5827 del 10/11/2015 | primaria | 3/1/1/1 | [L] encabezado | https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A5827.pdf |
| F7 | BCRA, texto ordenado «Sistema Nacional de Pagos – Transferencias», al 07/08/2025 (última «A» 8295; la sección 1 en versiones de la «A» 7175, 07/12/2020) | primaria | 3/3/2/3 | [L] sección 1 (transferencias en lote) | https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-snp-tr.pdf |
| F8 | BCRA, texto ordenado «Transferencias – Normas complementarias» (última «A» 8477, 08/09/26; secciones 5 y 6 en versión «A» 8399, vigencia 13/02/2026) | primaria | 3/3/2/3 | [L] puntos 3.4.2, 3.4.3.3, 5.1.2.1, 6.1, 6.2 | https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-snp-tr-nc.pdf |
| F9 | Ley 27.802 de Modernización Laboral, Boletín Oficial 06/03/2026 | primaria | 3/3/2/3 | [L] arts. 35, 41, 56, 133, 166 y 197 a 216 (derogaciones) | https://www.boletinoficial.gob.ar/detalleAviso/primera/339128/20260306 |
| F10 | LCT 20.744, texto actualizado de InfoLEG (ya con la 27.802) | primaria consolidada | 3/3/2/1 | [L] arts. 122, 123, 124, 125, 126, 128, 129, 132 bis, 137, 155, 255 bis, 276, 277 y la nota de antecedentes del DNU 70/2023 | https://servicios.infoleg.gob.ar/infolegInternet/anexos/25000-29999/25552/texact.htm |
| F11 | Decreto 407/2026, InfoLEG | primaria | 3/2/1/2 | [L] búsqueda en el texto completo de «124», «cuenta sueldo», «acreditación»; arts. 17 a 23 | https://servicios.infoleg.gob.ar/infolegInternet/anexos/425000-429999/426270/norma.htm |
| F12 | Decreto 380/2001 (reglamentación del impuesto a los débitos y créditos), texto de la biblioteca de ARCA con las modificaciones hasta el Decreto 475/2026 | primaria consolidada | 3/3/1/3 | [L] arts. 1, 2, 3, 7, 8 y 10 completos (versión «según Decreto N° 475/2026») | https://biblioteca.afip.gob.ar/dcp/DEC_C_000380_2001_03_29 |
| F13 | RG AFIP 4172-E, Boletín Oficial 26/12/2017 (agenda general de vencimientos desde 2018) | primaria | 3/2/2/3 | [L] arts. 1 a 5 | https://www.boletinoficial.gob.ar/detalleAviso/primera/176672/20171226 |
| F14 | Anexo original de la RG 4172 (copia en PDF del Consejo Profesional de Salta) | primaria en sitio de terceros | 2/3/2/2 | [L] acápite XVII (F. 931) y apartado C (SICORE) | https://www.consejosalta.org.ar/wp-content/uploads/Res_AFIP_4172.pdf |
| F15 | RG AFIP 4186-E (05/01/2018, BO 08/01/2018), modifica el Anexo de la RG 4172 | primaria | 3/2/2/3 | [L] art. 1 punto 2 (acápite XVII inc. a) | https://www.argentina.gob.ar/normativa/nacional/norma-305593/texto |
| F16 | RG AFIP 4354 (07/12/2018, BO 10/12/2018), modifica el Anexo de la RG 4172 | primaria | 3/2/2/3 | [L] punto 13 (SICORE inc. a) | https://www.argentina.gob.ar/normativa/nacional/norma-317309/texto |
| F17 | argentina.gob.ar, ARCA, «Vencimientos» (instantánea de noviembre de 2026) | primaria (calendario) | 3/1/2/2 | [L] empleadores y autónomos de noviembre | https://www.argentina.gob.ar/node/437875 |
| F18 | Ley 23.551 de Asociaciones Sindicales, texto actualizado de InfoLEG | primaria | 3/2/1/3 | [L] art. 38 | https://servicios.infoleg.gob.ar/infolegInternet/anexos/20000-24999/20993/texact.htm |
| F19 | Ley 27.742 (Bases), InfoLEG | primaria | 3/2/1/2 | [L] arts. 99 y 100 | https://servicios.infoleg.gob.ar/infolegInternet/anexos/400000-404999/401266/norma.htm |
| F20 | Forbes Argentina, «Pago de sueldos: el Gobierno le abre las puertas a las fintech pero deja un vacío clave» (11/12/2025) | secundaria | 2/2/1/2 | [M] leído con el extractor de páginas | https://www.forbesargentina.com/negocios/pago-sueldos-gobierno-le-abre-puertas-fintech-pero-deja-vacio-clave-n83201 |
| F21 | Resultados del buscador sobre vencimientos de enero y junio de 2026 (iProfesional, Canal 26, argentina.gob.ar) y sobre cuenta sueldo en dólares (iProfesional, Los Andes, El Economista, 24/07/2026) | secundaria | 1/1/1/1 | [S] | https://www.iprofesional.com/impuestos/445422-arca-vencimientos-autonomos-empleadores-monotributistas-enero-2026 ; https://www.iprofesional.com/finanzas/460713-cuentas-sueldo-dolares-ya-habilitadas-cobrar-salarios-sin-costos-julio-2026 |
| F22 | Enlace interno: art. 124, 126, 128, embargos | repo | | [L] | `Administracion-de-personal-y-nomina/Liquidacion-de-sueldos/liquidacion-en-argentina.md` |
| F23 | Enlace interno: transferencias, punto 1.2.3 | repo | | [L] | `Tesoreria/tesoreria-en-argentina.md` |

Nota de independencia: casi todo es fuente oficial y no hay dos independientes entre sí para la misma afirmación. El TO del BCRA (F1) incorpora las comunicaciones F2 a F5, así que coinciden por construcción; InfoLEG (F10) reproduce el Boletín Oficial (F9). Donde los dos se leyeron (art. 124), el texto es idéntico. Las fechas del F. 931 tienen dos fuentes oficiales que no se derivan una de otra en el mismo sentido: la norma (F13 + F15) y el calendario publicado (F17); para noviembre de 2026 no coinciden (ver sección 3). Las fuentes secundarias (F20, F21) solo dan contexto y no sostienen ninguna cifra.

## 1. La cuenta sueldo según el BCRA

Frontera: el texto del art. 124 y la eliminación del cobro en efectivo ya están en F22. Acá va lo que regula el BCRA.

Quién la abre y quién elige el banco
- Las entidades «que posean cajeros automáticos deberán abrir estas cuentas a solicitud de los empleadores alcanzados por la obligación de abonar las remuneraciones a su personal mediante la acreditación en cuenta conforme a lo dispuesto por el Ministerio de Trabajo, Empleo y Seguridad Social, en el marco de lo establecido por el artículo 124» de la LCT. [F1, 2.1, primer párrafo] [L]
- También se usa para los trabajadores no alcanzados por la LCT del art. 1 de la Ley 26.704 (casas particulares, Ley 26.844; trabajo agrario, Ley 26.727), para el SIPA y las pensiones no contributivas, y para provincias y CABA adheridas. [F1, 2.1 a) a c)] [L]
- Portabilidad: «Las entidades financieras también podrán abrir estas cuentas a solicitud de los trabajadores [...] no requiriéndose la intervención del empleador en el proceso de apertura». Si el trabajador ya tiene caja de ahorros en pesos puede pedir su «transformación en cuenta sueldo» (y en dólares, si esa es la moneda del sueldo). Asignada la CBU, «será responsabilidad del trabajador proveer de dicha información al empleador». [F1, 2.1, últimos párrafos] [L]
- La comunicación que lo introdujo es la **«A» 6042 del 12/08/2016** («Portabilidad y competencia»), puntos 2 y 3; el punto 5 la aplica «para los trabajadores que inicien una nueva relación laboral como así también para aquellos que, sin cambiar de empleador, opten por percibir sus remuneraciones en una cuenta sueldo abierta en otra entidad financiera». [F4] [L]
- Verificación de números: la **«A» 5827** (10/11/2015) no es de cuenta sueldo, es «Márgenes de capital. Normas sobre "Distribución de resultados"». [F6] [L] La **«A» 5091** (24/06/2010) es la adecuación a la Ley 26.590: sustituyó la sección 2, vigencia 12/07/10, ordenó reintegrar las comisiones cobradas desde el 14/05/10 y convertir en «cuenta sueldo» las cuentas donde ya se cobraba; prohibió usar «sueldo» o «remuneraciones» en cuentas que no lo son. [F5] [L] La portabilidad es de la 6042, no de la 5091 ni de la 5827.
- Plazo para cambiar de banco: el TO no fija ninguno. Solo dice que el trabajador abre la cuenta y le pasa la CBU al empleador. [F1, 2.1] [L] No encontré norma que fije en cuántos días el empleador debe empezar a acreditar en la cuenta nueva (Huecos).
- Datos que da el empleador: apellido y nombre, CUIL y domicilio de cada trabajador; si la abre el trabajador, presenta además certificado de trabajo, recibo de sueldo o información de ARCA. Puede designar cotitular (cónyuge, conviviente o familiar directo). [F1, 2.2.1] [L]
- Una vez acreditados los fondos, el trabajador puede transferirlos a otras cuentas propias «cualquiera sea la entidad». [F1, 2.2, último párrafo] [L]

Moneda (cambio de 2026)
- La **«A» 8460 (24/07/2026)** incorporó «al dólar estadounidense como moneda admitida» para la cuenta sueldo. El efectivo en dólares es obligatorio en la sucursal de radicación y, si hay billetes, en las demás sucursales y cajeros; la gratuidad «alcanza hasta el monto de las acreditaciones derivadas de la relación laboral acumulando los importes no retirados sin límite de tiempo». [F2] [L]
- La **«A» 8479 (11/09/2026)** aclara que «las cuentas sueldo podrán estar nominadas en pesos o en dólares estadounidenses, de acuerdo con la moneda establecida para el pago de las remuneraciones». [F3] [L] Así quedó en el TO, 2.2.1 (versión «A» 8479, vigencia 12/09/2026). [F1] [L]

Qué se puede acreditar
- Remuneraciones normales y habituales y otros conceptos de la relación laboral, asignaciones familiares, prestaciones de la seguridad social y de la Ley 24.557 (ART). [F1, 2.3.1] [L]
- También reintegros fiscales, promocionales, comerciales o de salud, y préstamos. [F1, 2.3.1, segundo párrafo] [L]

Qué incluye gratis
- Sin cargos ni comisiones por apertura, mantenimiento, movimientos de fondos y consulta de saldos, «aun los que se verifiquen por el uso de cajeros automáticos de distintas entidades y/o redes del país», siempre que el uso se ajuste a 2.3 y «hasta el monto de las acreditaciones derivadas de la relación laboral [...] acumulando los importes no retirados sin límite de tiempo». [F1, 2.6] [L]
- Extracciones en todos los cajeros del país «sin límites de importe (salvo los que expresamente se convengan por razones de seguridad y/o resulten de restricciones operativas del equipo) ni de cantidad de extracciones, ni distinción alguna entre clientes y no clientes»; por ventanilla (punto 4.11); compras y retiros en comercios con débito; pago de impuestos y servicios por canales electrónicos o débito automático «sin límite de adhesiones»; transferencias electrónicas. [F1, 2.3.2.1 a 2.3.2.5] [L]
- Tarjeta de débito: rige el punto 1.8 (para titular y cotitular), que da sin costo una tarjeta de débito optativa y los reemplazos por desmagnetización, deterioro (uno por año) o seguridad. [F1, 2.4.1 y 1.8] [L]
- Resumen semestral sin cargo y ticket de cajero con saldo y últimos diez movimientos. [F1, 2.5] [L]
- Si en la cuenta conviven fondos de otro origen, «las extracciones que se realicen afecten en primer término los importes de esa relación» (la laboral). [F1, 2.6, segundo párrafo] [L]

Qué no puede hacer el banco
- «Los movimientos –cualquiera sea su naturaleza– en estas cuentas no podrán generar saldo deudor». [F1, 2.3] [L]
- Servicios adicionales (paquetes, etc.) solo si el trabajador los pide «fehacientemente»; no pueden exigirse como condición, y sus comisiones solo por uso efectivo. [F1, 2.12] [L]
- El único débito que el TO autoriza por iniciativa del banco es el redondeo: puede adelantar hasta $ 99,99 para que se retire todo el saldo por cajero y descontarlo «del próximo haber acreditado». [F1, 2.3.2.1] [L] El resto de los débitos que lista 2.3.2 son a opción del trabajador. La lectura de que no hay otros débitos permitidos es mía (el TO no lo dice con esas palabras).

Cierre y fin de la relación laboral
- El cierre lo comunica el empleador o el trabajador si la abrió el empleador; si la abrió el trabajador, solo él. Se hace efectivo «luego de transcurridos 180 días corridos, contados desde la fecha de la última acreditación de fondos o de la comunicación –la que sea posterior–», y en ese lapso sigue la gratuidad del 2.6. Si había servicios adicionales cuyo costo cambia con la desvinculación, hay que avisarle antes al titular. [F1, 2.8.1] [L]
- Los fondos que queden después del cierre pasan a saldos inmovilizados. [F1, 2.8, último párrafo] [L]
- **El TO no dice que la cuenta sueldo «se convierte en caja de ahorro común»** al cesar la relación: dice que se cierra a los 180 días. Busqué «transform», «convers» y «reconver» en todo el texto: la única transformación es la inversa (caja de ahorro a cuenta sueldo, 2.1). Si algún banco la convierte, es práctica comercial, no norma del BCRA. [F1] [L]

Cuenta de la seguridad social
- En pesos, en la sucursal pagadora, a nombre del beneficiario, con apoderado o con representante legal; una sola cuenta por beneficiario y entidad; tarjeta magnética sin cargo; cierre según el ente pagador o a los 730 días sin acreditaciones. [F1, 2.2.2, 2.4.2, 2.8.2] [L]

Ley 27.802 y billeteras (CVU)
- El art. 124 vigente dice «acreditación en cuenta abierta a su nombre en entidad bancaria o en institución de ahorro oficial» (texto del art. 35 de la Ley 27.802, BO 06/03/2026, vigente desde la publicación). [F9, F10] [L] No menciona proveedores de servicios de pago ni cuentas de pago.
- El proyecto enviado al Congreso sí los incluía: según Forbes, el art. 124 del proyecto agregaba «Proveedores de Servicios de Pago (PSP) habilitados por el BCRA para tal actividad», y el DNU 70/2023 exigía autorización «caso por caso». [F20] [M] El texto sancionado no los tiene. Que el DNU 70/2023 había sustituido antes el art. 124 lo confirma la nota de antecedentes de InfoLEG («Artículo 124 sustituido por art. 72 del Decreto N° 70/2023 B.O. 21/12/2023»); el texto del DNU no lo leí. [F10] [L]
- El TO del BCRA al 29/10/26 no menciona cuentas de pago, CVU ni billeteras en la sección 2. [F1] [L] Las únicas comunicaciones de 2026 en la tabla de origen de 2.1 y 2.2 son la «A» 8460 y la «A» 8479 (dólares). [F1, tabla de origen] [L]
- Reglamentación del art. 124: el Decreto 407/2026 no lo reglamenta (no aparecen «124», «cuenta sueldo» ni «acreditación» en su texto). [F11] [L] No encontré otro decreto ni resolución de 2026 que lo haga (Huecos).
- Conclusión para la nota: en noviembre de 2026 el sueldo se acredita en cuenta sueldo de banco (pesos o dólares) y no en billetera; el trabajador puede después transferirlo a donde quiera (2.2). Lectura de esta base sobre F1, F9 y F10.

## 2. La acreditación

Canal del lote (cómo llega la plata)
- Las transferencias en lote pueden ser por «Pago de sueldos», «Pagos previsionales», «Asignaciones familiares», «Embargos sobre haberes por orden judicial», «Pago a proveedores» y «Entre clientes o clientes y terceros». Cada una debe llevar nombre o razón social y CUIT del ordenante, la CBU y el CUIT/CUIL/CDI del beneficiario, importe y moneda. [F7, 1.2] [L]
- Para el producto de sueldos, la entidad originante abre una «cuenta cobertura» y transfiere por el MEP a su cámara (CEC) el total de la presentación; «La falta de cobertura [...] producirá que la CEC no ingrese la/s presentación/es en el proceso de compensación y liquidación de ese día». [F7, 1.2.1] [L]
- Plazo: «Día D: las entidades originantes envían las transferencias [...]. Día D: se realiza la compensación en las CEC, la liquidación en el BCRA y la acreditación en las cuentas de las entidades receptoras. Día D+1: al inicio del día, el beneficiario tiene disponibles los fondos en su cuenta». [F7, 1.2.1] [L]
- Horario: «Será de libre acuerdo entre las partes, cliente y entidad originante, el momento en que el primero debe entregar a la segunda la información y fondos». Los horarios límite los fija cada CEC; quien se atrasa «deberá esperar hasta el día hábil siguiente». [F7, 1.2.1 y 1.3.1.3] [L] No hay una hora fijada por el BCRA para el cliente; la fija el convenio con el banco.
- Moneda: el punto 1.2.3 dice que se compensan en 24 horas las de sueldos, previsionales, asignaciones, embargos y minoristas «nominadas en pesos», y en 48 horas solo las de «Pago a proveedores y entre clientes o clientes y terceros, nominadas en moneda extranjera». [F7, 1.2.3] [L] **Corrección para F23**: la frase de `tesoreria-en-argentina.md` («los pagos en lote, como sueldos o proveedores, se compensan en 24 horas en pesos y 48 en moneda extranjera») generaliza de más; el texto no incluye sueldos en el lote en moneda extranjera. El TO de transferencias es del 07/08/2025, anterior a la cuenta sueldo en dólares (A 8460), así que cómo se acredita un sueldo en dólares por lote no está escrito ahí (Huecos).
- Si el empleador y el trabajador están en el mismo banco, el lote no pasa por la cámara: es un movimiento interno. Inferencia mía, no lo dice F7.

Prueba de pago
- «La documentación obrante en el banco o la constancia que éste entregare al empleador constituirá prueba suficiente del hecho de pago». [F10, art. 125] [L] Los recibos pueden digitalizarse con igual validez (texto de la Ley 27.802). [F9] [L]

Comisiones al empleador
- Las transferencias en lote son gratuitas para el ordenante solo si es microempresa, hasta 7.500 UVA en pesos (6.000 dólares o euros) por mes, moneda y proveedor de cuenta; también si ordenante y receptor son la misma persona o si el ordenante es usuario de servicios financieros (persona humana). [F8, 5.1.2.1 ii) y 6.1.1] [L]
- Fuera de eso el banco puede cobrar, pero «los precios no podrán ser definidos como porcentajes de los montos transferidos», y se permiten comisiones «por cobertura geográfica entre entidades y a los clientes por los valores que se acuerden». [F8, 6.1.2] [L]
- Además puede cobrar los «servicios adicionales para facilitar la carga masiva de dichas transacciones [...] (y en tanto no se cobren por importes que tengan relación con los montos transferidos)». [F1, 4.10.1] [L] Ese es el lugar normativo del cargo por el servicio de pago de haberes.
- Al trabajador no se le puede cobrar nada por la cuenta (2.6, sección 1).

Convenio de pago de haberes
- El TO no regula un contrato tipo entre empleador y banco; da por supuesto que el banco abre las cuentas «a solicitud de los empleadores» y que el empleador entrega el texto de las condiciones al trabajador cuando la abrió él (2.9). [F1, 2.1 y 2.9] [L] El contenido del convenio (formato del archivo, horario de corte, débito de la cuenta del empleador, fecha valor) es de cada banco (Huecos).

## 3. El calendario

Sueldo mensual
- Sin cambios: cuatro días hábiles para mensual o quincenal y tres para semanal, desde el vencimiento del período (art. 128); el mensualizado cobra «al vencimiento de cada mes calendario» (art. 126). [F10] [L] Ya está en F22.
- El pago debe hacerse «en días hábiles». [F10, art. 129] [L]
- Para tesorería, como lectura de esta base: si el lote se acredita en D+1 (F7), los fondos tienen que estar en el banco y el archivo entregado a más tardar el día hábil anterior al cuarto día hábil.

Aguinaldo (SAC)
- Art. 122: «dos (2) cuotas: la primera de ellas con vencimiento el 30 de junio y la segunda con vencimiento el 18 de diciembre de cada año», sobre el 50 % de la mayor remuneración mensual del semestre; la segunda se estima y la diferencia se integra al sueldo de diciembre. Texto de la Ley 27.073 (BO 20/1/2015). **La Ley 27.802 no lo cambió**: InfoLEG no tiene nota de la 27.802 en el art. 122 y el texto de la ley no lo sustituye ni habla de pagarlo en cuotas. [F9, F10] [L]
- Art. 123: en la extinción, se paga la parte proporcional del semestre. [F10] [L]
- El 18/12/2026 cae viernes (cuenta mía). El art. 122 da una fecha de vencimiento, no los cuatro días hábiles del art. 128; si se le aplica ese plazo no lo dice el texto (Huecos).

Vacaciones
- Art. 155, último párrafo: «La retribución correspondiente al período de vacaciones deberá ser satisfecha a la iniciación del mismo». [F10] [L]
- La Ley 27.802 (art. 41, nuevo art. 154) permite fraccionar las vacaciones de común acuerdo en tramos de no menos de siete días y pide avisar la fecha de inicio por escrito con 30 días. [F9] [L] Cada tramo es una salida de caja al inicio del tramo, lectura mía a partir del art. 155.

Liquidación final
- Art. 255 bis: las remuneraciones e indemnizaciones de la extinción «se efectuará dentro de los plazos previstos en el artículo 128 computados desde la fecha de extinción de la relación laboral» (cuatro días hábiles). [F10] [L]

Feriados y días hábiles
- ARCA: si un vencimiento «coincida con un día feriado o inhábil, la misma, así como las posteriores, se trasladarán correlativamente al o a los días hábiles inmediatos siguientes». [F13, art. 2] [L]
- El calendario de feriados de 2026 no se leyó (Huecos).

F. 931 (aportes y contribuciones)
- La RG 4172 fija desde 2018 las fechas generales, entre ellas las de la RG 3834 (texto RG 712), art. 15: la del F. 931 de empleadores. [F13, art. 1 punto 3 y art. 3] [L] El anexo original decía días 7, 8 y 9. [F14] [L]
- La **RG 4186** (BO 08/01/2018) los sustituyó: «PRESENTACIÓN DDJJ F. 931 y PAGO»: terminación de CUIT 0, 1, 2 y 3, día **9**; 4, 5 y 6, día **10**; 7, 8 y 9, día **11**; «ENERO A DICIEMBRE», del mes siguiente al devengado. [F15] [L]
- El calendario publicado lo confirma para junio de 2026 (9, 10 y 11) y para enero (9, 12 y 13, con el fin de semana). [F21] [S]
- **Noviembre de 2026 no coincide**: el calendario de ARCA dice «Empleadores - 11 de noviembre. Presentación y pago de declaración jurada»: 0-1-2-3 el 11/11/2026, 4-5-6 el 12/11/2026, 7-8-9 el 13/11/2026; los autónomos también se corrieron (5, 11 y 12 de noviembre). [F17] [L] La página no cita la norma del corrimiento; puede ser un traslado por días inhábiles o una prórroga (la misma página tiene una cuenta regresiva a la llegada del Papa el 8/11/2026), pero no lo verifiqué (Huecos).
- Lo que entra en el F. 931 (aportes del trabajador retenidos, contribuciones patronales, ART, obra social) y desde cuándo se suma el FAL (devengado diciembre de 2026, según `argentina-laboral.md`) no se volvió a leer acá.

SICORE (retenciones de Ganancias y otras)
- Apartado C del Anexo de la RG 4172, RG 2233 art. 2: inc. a) «Ingreso de las retenciones practicadas desde el día 1 al 15, ambos inclusive»; inc. b) «Información e ingreso de las retenciones y/o percepciones practicadas». [F14] [L]
- Fechas del inc. a), según la RG 4354: enero a noviembre (excepto febrero) días **21, 22 y 23**; febrero y diciembre días **20, 21 y 22** (terminaciones 0-3, 4-6, 7-9). [F16] [L]
- Fechas del inc. b): días **9, 10 y 11** del mes siguiente, enero a diciembre. [F14] [L] No vi una norma posterior que lo cambie, pero tampoco leí el anexo consolidado (Huecos).
- Diciembre de 2026, cuenta mía con esas reglas: el pago quincenal de SICORE vence el 21/12 (lunes) para las terminaciones 0-3; el F. 931 de noviembre vence el 9, 10 y 11 de diciembre (miércoles a viernes), salvo traslados. El SAC vence el viernes 18. Son tres salidas en diez días.
- Qué tramo usa la retención de Ganancias sobre sueldos (cuarta categoría, RG 4003) y si el ingreso quincenal del inc. a) es obligatorio para todo agente o solo por encima de cierto monto: no lo leí (Huecos).

Cuota sindical y obra social
- Art. 38 de la Ley 23.551: los empleadores son «agente de retención» de las cuotas de afiliación u otros aportes de los trabajadores a sindicatos con personería gremial, cuando lo disponga una resolución del Ministerio de Trabajo (tácita si no se pronuncia en 30 días). Si el empleador no retiene o no paga «en tiempo propio» lo retenido, pasa a ser «deudor directo» y «La mora en tal caso se producirá de pleno derecho». La Ley 27.802 no modificó el art. 38 (no figura entre los artículos de la 23.551 que sustituye: 20 bis, 20 ter, 23, 29, 44 inc. c, 50, 52, 53 bis, 54, 55 y 59). [F18, F9] [L]
- Tope de 2 % para aportes convencionales a sindicatos (afiliados o no), excluidas las cuotas de afiliación; 0,5 % para cámaras empresarias. [F9, art. 133, nuevo art. 9 de la Ley 14.250] [L]
- Plazo de depósito de la cuota sindical (Decreto 467/88): no lo pude leer (Huecos). La obra social va en el F. 931; no lo verifiqué en una norma leída acá (Huecos).

## 4. Impuesto a los débitos y créditos y la cuenta sueldo

- Alícuota general: «SEIS POR MIL (6‰) para los créditos y del SEIS POR MIL (6‰) para los débitos». [F12, art. 7] [L]
- **No hay un inciso que nombre la «cuenta sueldo».** Busqué «sueldo» en todo el Decreto 380/2001 consolidado: solo aparece en el inciso de Transferencias 3.0, y para excluir: la exención de las cuentas de los participantes de esos esquemas no alcanza «las cuentas que estos últimos participantes utilicen para efectuar sus propias transacciones (pago de proveedores y de sueldos, entre otras)». [F12, art. 10] [L]
- Lo que exime al trabajador es:
  - el inc. **u)**: «Los débitos y créditos en cuentas de caja de ahorro abiertas en instituciones regidas por la Ley de Entidades Financieras, excepto cuando resulten de aplicación las disposiciones del artículo 3°»; [F12, art. 10 u)] [L]
  - el inc. **h)**, si cobra en cuenta corriente: «Los débitos y créditos efectuados en la cuenta corriente de los empleados en relación de dependencia, jubilados o pensionados, correspondientes a sus remuneraciones, hasta del monto mensual acreditado». [F12, art. 10 h)] [L]
  - La cuenta sueldo está en el TO de «Depósitos de ahorro» y le aplican supletoriamente las normas de la caja de ahorros (F1, 2.13); que el inc. u) la alcance es lectura de esta base, no texto del decreto.
- El empleador: el débito de su cuenta corriente para pagar sueldos no tiene exención en el art. 10 leído; queda en la regla general del art. 1 («créditos y débitos —de cualquier naturaleza— efectuados en cuentas abiertas en las entidades») al 6‰. [F12, arts. 1 y 7] [L] Es lectura de esta base: no encontré un texto que diga en positivo «el débito por sueldos está gravado»; lo que hay es la ausencia de exención y la exclusión expresa del inciso de Transferencias 3.0.
- Exenciones del art. 10 modificadas en 2026: el Decreto 408/2026 exime las cuentas de los FCI y fideicomisos del FAL de la Ley 27.802, y el Decreto 475/2026 tocó otros incisos (PSP, transportadoras de caudales, tarjetas). Ninguno trata los sueldos. [F12] [L]
- Cuenta de pago de persona humana usada solo por medios electrónicos: exenta (inciso agregado por el Decreto 301/21). [F12] [L] Hoy no aplica al cobro del sueldo, porque el sueldo no se acredita en cuenta de pago (sección 1).

## 5. Si no se paga en plazo

- Mora automática: «La mora en el pago de las remuneraciones se producirá por el solo vencimiento de los plazos señalados en el artículo 128 de esta ley, y cuando el empleador deduzca, retenga o compense todo o parte del salario, contra las prescripciones de los artículos 131, 132 y 133». No cambió con la 27.802. [F10, art. 137] [L]
- Actualización: los créditos laborales se actualizan por IPC nivel general del INDEC «con más una tasa de interés del tres por ciento (3%) anual, desde que cada suma sea debida y hasta el momento del efectivo pago» (art. 276, sustituido por el art. 54 de la 27.802). [F10] [L]
- Pago en juicio: por depósito en la cuenta sueldo del trabajador, si está disponible; las sentencias condenatorias pueden pagarse «en hasta un máximo de seis (6) cuotas mensuales consecutivas» (grandes empresas) o «doce (12)» (MiPyMEs), ajustadas por el art. 276. Costas de primera instancia con tope del 25 % del monto. (art. 277, sustituido por el art. 56 de la 27.802). [F9, F10] [L]
- Recargo del 50 % de la Ley 25.323: **ya no existe**. La Ley 27.742 dice «Derógase la ley 25.323» (art. 100) y también deroga los arts. 43 a 48 de la Ley 25.345 (art. 99). [F19] [L]
- Sanción del art. 132 bis (aportes retenidos y no depositados al extinguirse la relación: una remuneración mensual por mes hasta acreditar el depósito): InfoLEG todavía muestra el texto, pero con la nota «Artículo 43 de la Ley N° 25.345 derogado por art. 56 del Decreto N° 70/2023», y la Ley 27.742 art. 99 derogó también el art. 43 de la 25.345, que es el que incorporó el 132 bis. [F10, F19] [L] Si el artículo sigue vigente es dudoso; no usarlo sin verificar (Huecos).
- Cuota sindical retenida y no depositada: el empleador es deudor directo y la mora es de pleno derecho (art. 38 Ley 23.551). [F18] [L]
- Intereses de ARCA por pagar tarde el F. 931 o el SICORE (intereses resarcitorios de la Ley 11.683 y su tasa vigente): no se leyeron (Huecos).
- Embargos: la inembargabilidad ya está en F22. Lo que agrega el lado bancario: el lote de transferencias tiene un concepto propio, «Embargos sobre haberes por orden judicial», con el mismo plazo de 24 horas que los sueldos [F7, 1.2 y 1.2.1] [L]; y la cuenta sueldo no puede quedar en saldo deudor [F1, 2.3] [L]. No encontré en el TO una regla sobre cómo traba el banco un embargo sobre el saldo de la cuenta sueldo (Huecos).

## Huecos

- Resolución del Ministerio de Trabajo a la que remite el punto 2.1 del TO (qué empleadores están «alcanzados por la obligación» y desde cuándo); después de la Ley 27.802 la obligación es general, pero no leí la resolución ni sé si sigue vigente.
- Plazo para que el empleador empiece a acreditar en la cuenta sueldo que eligió el trabajador (portabilidad): no está en la «A» 6042 ni en el TO.
- Reglamentación del art. 124 nuevo: no la encontré; el Decreto 407/2026 no lo trata. No hay comunicación del BCRA de 2026 que habilite cuentas de pago para sueldos; el TO de «Servicios de pago» no se pudo bajar (la URL que probé devolvió una página HTML).
- Cómo se acredita por lote un sueldo en dólares: el TO de transferencias (07/08/2025) no lo prevé en el punto 1.2.3; puede haber una comunicación posterior a la «A» 8460 que no leí.
- Contenido típico del convenio de pago de haberes (horario de corte, débito de la cuenta del empleador, fecha valor, cargo por cuenta o por archivo): es de cada banco; no leí ninguno.
- Si al SAC del 18 de diciembre se le aplican los cuatro días hábiles del art. 128.
- Calendario de feriados nacionales de 2026 (ley y decretos de feriados puente).
- Por qué los vencimientos del F. 931 de noviembre de 2026 cayeron el 11, 12 y 13 y no el 9, 10 y 11: falta la norma (traslado o prórroga). Fechas de diciembre de 2026 no confirmadas en el calendario de ARCA.
- Anexo consolidado de la RG 4172 con todas sus modificaciones posteriores a 2018 (pudo haber más cambios en el F. 931 o en el SICORE).
- SICORE para sueldos: qué tramo aplica a la retención de cuarta categoría (RG 4003 y RG 2233 art. 2; no se pudieron leer).
- Plazo de depósito de la cuota sindical retenida (Decreto 467/88; la URL de InfoLEG probada no tenía el texto) y si la obra social sale toda por el F. 931.
- Tasa de intereses resarcitorios de ARCA vigente en noviembre de 2026.
- Vigencia del art. 132 bis LCT después del DNU 70/2023 y de la Ley 27.742.
- Embargo sobre el saldo de la cuenta sueldo: cómo lo traba el banco y si hay norma del BCRA.
- No leí el texto del DNU 70/2023 art. 72 (la versión anterior del art. 124 con los PSP); lo que digo de él sale de Forbes [M].
