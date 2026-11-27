Fecha de lectura: 2026-11-27. Material de alto riesgo (ley). Segunda ronda.

Marcas: [L] = leído por mí en la fuente primaria; [S] = leído en una fuente oficial pero secundaria (compilación o texto no auténtico); [M] = de memoria, no verificado. Si tus marcas significan otra cosa, remapealas. Copias de trabajo en `/tmp/claude-1000/-home-dela-repos-personal-conocimiento/cfb247c6-67ae-4161-949e-87e8ed3a86d4/scratchpad/ar-ronda2/`. No llamé a ningún web service de ARCA. Todo es documento publicado.

## Resumen

| Punto | Estado |
|---|---|
| 1a. Códigos de IVA 2,5 % y 5 % | ABIERTO |
| 1b. Tipos de tributos | CERRADO |
| 2. Ley 27.743 art. 99 y RG 1415 | CERRADO |
| 3. RG 830, mínimo | CERRADO |
| 3. RG 830, datos del certificado | ABIERTO |
| 4. RG 2854 y RG 5762 | CERRADO |
| 5. ARBA DN B 1/04 | CERRADO |
| 6. AGIP | ABIERTO |
| 7. Comisión Arbitral | CERRADO en atribución de ingresos, ABIERTO en percepción |
| 8. Editoriales (IVA) | CERRADO, y corrige el dato de la nota |

## 1. Códigos de FEParamGetTiposIva y FEParamGetTiposTributos

### 1a. Códigos de IVA para 2,5 % y 5 %: ABIERTO

- En el manual WSFEv1 solo aparecen Id 4 = 10.5% y Id 5 = 21% en los ejemplos de Factura A. Ningún Id 8 ni 9.
- En los manuales WSMTXCA (v25 y la versión RG 2904) la respuesta de `consultarAlicuotasIVA` de ejemplo trae solo 0 %, 10.5 %, 21 % y 27 %, con los códigos 3, 4, 5 y 6. Es un ejemplo, no la tabla completa.
- El manual WSBFEV1 v3.0 y el WSMTXCA no dicen nada de 2,5 % ni de 5 %.
- La tabla 3=0, 4=10.5, 5=21, 6=27, 8=5, 9=2.5 queda solo como [M], sin cita publicada.
- Qué busqué:
  - grep en `w.txt`, en WSMTXCA v25, en `wsmtxca-RG-2904` y en WSBFEV1 v3.0.
  - La página `https://www.afip.gob.ar/fe/ayuda/tablas.asp`: lista tablas de comprobantes, monedas, países y otras, pero ninguna de alícuotas de IVA.
  - RG 4597 en la biblioteca de ARCA (Libro IVA Digital): no trae la tabla de alícuotas.
  - Las URL del diseño de registro del Libro IVA Digital dan 404 o página vacía.
  - No pude usar la búsqueda web (cupo agotado).

### 1b. Tipos de tributos: CERRADO [L]

Fuente: `https://www.afip.gob.ar/fe/documentos/otros_Tributos.xlsx`, enlazada desde la página de tablas de factura electrónica de ARCA (`https://www.afip.gob.ar/fe/ayuda/tablas.asp`). La hoja se llama "Otros Tributos". Cada código con su descripción literal y la observación de la planilla:

| Código | Descripción | Observación |
|---|---|---|
| 01 | Impuestos nacionales | |
| 02 | Impuestos provinciales | |
| 03 | Tributos municipales | |
| 04 | Impuestos internos | |
| 05 | IIBB | |
| 6 | Percepción de IVA | |
| 7 | Percepción de IIBB | |
| 8 | Percepciones por Tributos Municipales | |
| 09 | Otras Percepciones | |
| 10 | Impuesto interno a nivel item | Sólo Controladores Fiscales |
| 13 | Percepción de IVA a no Categorizado | Solo FE |
| 14 | Retención IIGG - RG 830 | Liquidaciones Pecuarias |
| 15 | Retención IVA - RG 3873 | Liquidaciones Pecuarias |
| 16 | Pago a cuenta IVA - RG 3873 | Liquidaciones Pecuarias |
| 17 | Percepción IVA RG 3873 | Liquidaciones Pecuarias |
| 18 | Retención IVA – RG 2616/2009 | Liquidaciones Pecuarias |
| 19 | Retención Ganancias – RG 2616/2009 | Liquidaciones Pecuarias |
| 99 | Otros | |

- El manual WSFEv1 solo documenta la estructura de la respuesta (Id, Desc, FchDesde, FchHasta), no la lista.
- El 99 exige `<Desc>` (error 10042 en el manual).
- Esta planilla es la tabla publicada, no la respuesta en vivo del servicio.

## 2. Ley 27.743 art. 99 y RG 1415

### 2a. Ley 27.743: CERRADO [L]

Fuente: `https://servicios.infoleg.gob.ar/infolegInternet/anexos/400000-404999/401268/norma.htm` (InfoLEG, norma 401268). Es el Título VII "Régimen de Transparencia Fiscal al Consumidor". Cito el art. 99 literal:

> "Artículo 99.- Todos aquellos sujetos que realicen ventas, locaciones de obra o prestaciones de servicios a consumidores finales deberán indicar, en la publicación de los precios de los respectivos bienes o prestaciones, el importe final que deba abonar el consumidor final. Además, deberán indicar el importe neto sin la incidencia del Impuesto al Valor Agregado (IVA) y de los demás impuestos nacionales indirectos que incidan en los precios, el cual deberá estar acompañado de la leyenda “PRECIO SIN IMPUESTOS”.
>
> Las facturas o tickets o comprobantes fiscales similares emitidos por las operaciones a que hace referencia el párrafo anterior deberán detallar el importe discriminado del Impuesto al Valor Agregado y de los demás impuestos nacionales indirectos que incidan en los precios con el objetivo que todos los consumidores finales tengan conocimiento del importe pagado en concepto de esos impuestos en cada operación realizada.
>
> El incumplimiento de las obligaciones mencionadas en los párrafos anteriores estará sujeto a la sanción establecida en el artículo 40 de la ley 11.683 (...)
>
> La Administración Federal de Ingresos Públicos deberá dictar las normas reglamentarias y complementarias que sean necesarias para que dichas obligaciones se efectivicen a partir del 1° de enero de 2025.
>
> Se invita a las provincias y a la Ciudad Autónoma de Buenos Aires a dictar las respectivas normas para que los consumidores finales tengan conocimiento de la incidencia del Impuesto sobre los Ingresos Brutos y de los respectivos tributos municipales (...)"

El art. 98 sustituye, con efectos desde el 1/1/2025, el primer párrafo del art. 39 de la ley de IVA:

> "Cuando un responsable inscripto realice ventas, locaciones o prestaciones de servicios gravadas a consumidores finales, deberá discriminar en la factura o documento equivalente el gravamen que recae sobre la operación, el cual se calculará aplicando sobre el precio neto indicado en el artículo 10, la alícuota correspondiente (...). El mismo criterio se aplicará con sujetos cuyas operaciones se encuentran exentas, incluyendo a aquellos que revistan la condición de inscriptos en el Régimen Simplificado para Pequeños Contribuyentes (...)"

### 2b. RG 1415 y su modificación por la RG 5614/2024: CERRADO

La RG 1415 figura "Estado de la Norma: Vigente" (B.O. 13/01/2003). Fuente [L]: `https://biblioteca.afip.gob.ar/dcp/REAG01001415_2003_01_07`, Anexo II, Apartado A, Título IV, con la nota "(inciso a) sustituido por Resolución General N° 5614)":

> "a) Emisor responsable inscripto en el impuesto al valor agregado: 1. En el caso de operaciones gravadas efectuadas con sujetos responsables inscriptos en el gravamen o adheridos al Régimen Simplificado (Monotributo), deberá discriminarse: 1.1. La alícuota a que está sujeta la operación. 1.2. El monto del impuesto resultante. 1.3. El monto de los restantes tributos que no integren el precio neto gravado. 1.4. El importe de la percepción que resulte procedente. 2. De tratarse de operaciones gravadas efectuadas con sujetos exentos, no alcanzados o consumidores finales frente al impuesto al valor agregado deberá discriminarse el impuesto que recae sobre la operación."
>
> "b) Emisor adherido al Régimen Simplificado (Monotributo): en ningún caso corresponderá efectuar discriminación alguna del impuesto al valor agregado (...)"

Fuente [L]: RG ARCA 5614/2024 (B.O. 13/12/2024), `https://www.argentina.gob.ar/normativa/nacional/` (copia local `r5614.txt`):

- Agrega el inciso f) del Título III del Apartado A, Anexo II: "se deberá consignar en el comprobante el importe de los 'Otros Impuestos Nacionales Indirectos' que inciden en los precios".
- El Apartado B, inc. g) exige, en el espacio inferior izquierdo: "Título 'Régimen de Transparencia Fiscal al Consumidor (Ley 27.743)'. Debajo del mismo se mostrará el dato 'IVA Contenido' (...) y debajo el dato 'Otros Impuestos Nacionales Indirectos', cada uno con su correspondiente valor."
- Art. 6, gradualidad: las "empresas grandes" discriminan IVA e impuestos internos desde el 1/1/2025. Para el resto, el cumplimiento es voluntario desde el 1/1/2025 y obligatorio desde el 1/4/2025.
- Consecuencia: para el consumidor final, el IVA "contenido" va discriminado en las facturas A y B. Para el receptor responsable inscripto o monotributista, se discrimina alícuota e impuesto.
- Aviso: la biblioteca de ARCA lista una RG 5866/2026 como texto relacionado de la RG 1415 (Anexo 4, vigencia). No la leí.

## 3. RG 830 (Ganancias)

Fuente [L]: `https://biblioteca.afip.gob.ar/dcp/REAG01000830_2000_04_26`. Emitida el 26/04/2000, B.O. 28/04/2000, "Estado de la Norma: Vigente". Última modificada por las RG 5322/2023, 5423/2023, 5740/2025 y 5822/2026. Ninguna aparece como fuente del art. 29.

### Importe mínimo: CERRADO

> "Texto vigente según Resolución General Nº 4525/2019 AFIP ARTICULO 29.- Cuando por aplicación de las disposiciones de esta Resolución General, resultara un importe a retener inferior a DOSCIENTOS CUARENTA PESOS ($ 240.-), no corresponderá efectuar retención. El importe señalado se elevará a MIL VEINTE PESOS ($ 1.020.-) cuando se trate de alquileres de inmuebles urbanos percibidos por beneficiarios no inscriptos en el gravamen."

Versiones anteriores: $20 / $100 originales, $90 / $450 (RG 3884/2016), $150 / $650 (RG 4245/2018).

### Constancia o certificado de retención: PARCIAL

- El art. 33 (texto según RG 924/2000) dice: "Los importes a deducir en concepto de retenciones (33.1.) serán los que resulten de los 'Certificados de Retención' (33.2.). Dicha constancia sólo podrá ser sustituida por el comprobante que acredite la obligación de informar a este Organismo su falta de entrega (33.3.)".
- La nota 33.2 dice: "Emitidos de conformidad con la Resolución General N° 738 y sus modificaciones (SICORE), mediante la aplicación que la misma aprueba."
- Los datos del certificado no están en la RG 830. Los fija el sistema SICORE (hoy RG 2233 y SIRE, RG 3726, según la RG 5762 art. 15).
- ABIERTO: el contenido de los datos del certificado. Busqué en la RG 830, sus notas y la RG 5762. No leí la RG 2233 ni la RG 3726.

## 4. RG 2854 (retención de IVA)

Fuente [L]: `https://biblioteca.afip.gob.ar/dcp/REAG01002854_2010_06_22`. Texto actualizado, "Estado de la Norma: Vigente", en vigencia desde el 01/07/2010. Las modificatorias listadas llegan hasta la RG 5724/2025, 5799/2025, 5837/2026 y 5897/2026. Estas cuatro tocan los Anexos de nóminas. La RG 5762 no está entre las modificatorias.

### Mínimo del art. 12: CERRADO

> "Texto vigente según Resolución General Nº 3887/2016 AFIP Art. 12. -En las operaciones realizadas con los sujetos indicados en el inciso a) del Artículo 4º, no corresponderá practicar retención cuando el importe a retener resulte igual o inferior a CUATROCIENTOS PESOS ($ 400.-)."

El texto original era $160. El inciso a) del art. 4 son los "responsables inscriptos en el impuesto al valor agregado".

### RG 5762/2025: CERRADO [L]

Fuente: `https://biblioteca.afip.gob.ar/dcp/REAG01005762_2025_09_24`. Es un caso a parte, no una modificación.

- Emitida el 24/09/2025, B.O. 25/09/2025, en vigencia desde el 01/12/2025.
- Sustituye la RG 1575 (facturas A con leyenda "OPERACIÓN SUJETA A RETENCIÓN").
- Su Título III crea un régimen propio de retención de IVA y Ganancias para esas facturas. El art. 13 dice: IVA "el CIEN POR CIENTO (100%) de la alícuota" y Ganancias "el SEIS POR CIENTO (6%)".
- El art. 12 exceptúa "operaciones alcanzadas por regímenes de retención especiales".
- El art. 15 remite el certificado a SICORE (RG 2233) o SIRE (RG 3726).
- El art. 30 deroga las RG 1575, 1672, 1681, 1934, 1941, 2499, 4627, 5569 y 5716, el Título V de la RG 4597 y el Capítulo B del Título V de la RG 5003. No nombra la RG 2854.
- Conclusión: la RG 2854 sigue vigente y la RG 5762 no la modificó ni derogó.

## 5. ARBA, DN Serie B 1/04

Fuente [S]: `https://web.arba.gov.ar/sites/default/files/2025-04/DN%20B%201-2004%20Texto%20vigente.pdf` (107 pp., publicado en abril de 2025 por el Departamento de Información Legal y Técnica de ARBA). El propio PDF aclara que es un texto "con fines de orientación y difusión" y que solo el Boletín Oficial de la Provincia es auténtico. La compilación puede no recoger cambios posteriores a abril de 2025. Todo CERRADO salvo esa reserva.

**Art. 322 (exclusiones)** (texto según RN 27/2018):

> "Se encuentran excluidos como sujetos pasibles de percepción y de retención de los regímenes generales: a) El Estado Nacional, los Estados Provinciales, la Ciudad Autónoma de Buenos Aires y las Municipalidades (...). b) Los sujetos desgravados o no alcanzados por el gravamen. c) Los que desarrollen las actividades comprendidas en los artículos 192 y 193 del Código Fiscal (...). d) Los que hubieren obtenido una reducción total de alícuotas (...) (alícuota cero “0”), conforme (...) la Resolución Normativa Nº 64/10 y modificatorias. (...) Adicionalmente, y sólo con relación a los regímenes especiales de percepción (...), se encuentran excluidos: 1) Los sujetos exentos. 2) Los que desarrollen las actividades comprendidas en los artículos 191 inciso a), b) y c) y 195 del Código Fiscal (...)."

**Art. 342 (monto sujeto a percepción):**

> "La percepción debe calcularse aplicando la alícuota correspondiente respecto de alguna de las siguientes alternativas: 1) Sobre el monto total de la operación que surja de la factura o documento equivalente pudiendo detraerse, según corresponda, los siguientes conceptos: a) Las percepciones que se hubieren efectuado por aplicación de otros regímenes nacionales, provinciales y municipales. b) Los conceptos a que se refieren los artículos 148 inciso a) y 149 inciso a) del Código Fiscal. 2) Sobre el monto total de la operación (...) pudiendo detraerse (...): a) El Impuesto al Valor Agregado, cuando el adquirente, locatario o prestatario revista la condición de responsable inscrito ante dicho gravamen. b) El Impuesto Interno (...) ley nacional 24.674 (bebidas alcohólicas) (...). c) (...) (bebidas analcohólicas, jarabes, extractos y concentrados) (...). d) Las percepciones (...) de otros regímenes (...). e) Los conceptos a que se refiere el artículo 149 inciso a) del Código Fiscal."

**Monto mínimo de percepción, art. 343** (según RN 18/2023):

> "A los efectos de practicar la percepción, el importe establecido de conformidad al artículo anterior deberá ser igual o superior a la suma de PESOS TRES MIL QUINIENTOS ($ 3.500). Las operaciones realizadas por el sistema de comercialización denominado “Venta Directa” (...) no se encuentran sujetas a monto mínimo."

Retención, por comparación: art. 410, mínimo $19.000, y art. 428, "No corresponderá realizar retención cuando el pago que se efectúe sea inferior a PESOS DIECINUEVE MIL ($ 19.000)", ambos según RN 18/2023.

## 6. AGIP: ABIERTO

- Lo único que tengo es el Anexo I de la Res. 296/2019 (el PDF tiene fecha de 2019), con el art. 34 original:
  > "Se fija en Pesos tres mil ($3.000) el monto mínimo sujeto a retención y en Pesos quinientos ($500) el monto mínimo sujeto a percepción establecido para los Regímenes Generales de Retención y de Percepción. Excluyese de la aplicación de los montos mínimos a los regímenes particulares normados en el Título IV."
- Ese art. 1 también fija el universo de agentes: ingresos superiores a $200.000.000 y tributo superior a $12.000.000. Es texto de 2019 y no lo puedo dar por vigente. Marca [S] de baja confianza.
- Qué busqué:
  - agip.gob.ar es una SPA que carga el contenido por JavaScript, y la API pública (`/api/pages/regulations/...`) devolvió listas vacías.
  - No encontré resolución posterior ni texto ordenado.
  - El Boletín Oficial porteño no es buscable sin búsqueda web (cupo agotado).
  - Sin verificar: no sé si hay una resolución 2023-2026 que reemplace o actualice la 296/2019.

## 7. Comisión Arbitral: CERRADO en atribución de ingresos, ABIERTO en percepción

Fuente [L]: sitio oficial `https://www.ca.gob.ar/resoluciones-comarb/category/...` (la descarga redirige a `/images/boletin_oficial/resoluciones/rg/aviso_323968.pdf` para la RG 9/2025).

Ninguna RG de la Comisión Arbitral que leí dice en qué jurisdicción puede percibir el agente. Cada jurisdicción lo define en su norma local.

**RG CA 5/2021** (10/03/2021), Comercialización por medios electrónicos. Art. 2:

> "El sustento territorial del vendedor de los bienes o del prestador y/o locador de los servicios, a los efectos de la atribución de ingresos previstas en el inciso b), in fine, del artículo 2° del Convenio Multilateral, se configurará en la jurisdicción del domicilio del adquirente de los bienes, obras o servicios, siempre que exista presencia digital en la misma."

El art. 3 define los cuatro parámetros de "presencia digital". El art. 4 remite a la RG 14/2017 para el domicilio del adquirente, y el art. 5 deroga la RG 83/2002.

**RG CA 14/2017**, art. 1 inc. a):

> "Los ingresos por venta de bienes (...) serán atribuidos a la jurisdicción correspondiente al domicilio del adquirente, entendiéndose por tal el lugar del destino final donde los mismos serán utilizados, transformados o comercializados por aquél."

Si no se puede establecer el destino final, aplica un orden de prelación: sucursal que originó la compra, actividad principal, depósito donde se entregaron los bienes, sede administrativa. Su estado actual no lo verifiqué, porque el ordenamiento RG CA 17/2024 no lo pude leer completo.

**RG CA 9/2025 (SIRCIP)**, 09/04/2025. Visto: "Las normas de las jurisdicciones que establecen regímenes de percepción en el Impuesto sobre los Ingresos Brutos, para quienes revistan o asuman la calidad de contribuyentes comprendidos en el régimen del Convenio Multilateral". Es un sistema informático, no una pauta territorial:

- Art. 1: aprueba el SIRCIP "en cumplimiento de los regímenes de percepción del Impuesto sobre los Ingresos Brutos establecidos por las jurisdicciones adheridas".
- Art. 2: el universo de agentes son los "designados y notificados por las jurisdicciones adheridas, en cumplimiento de las normas locales".
- Anexo I, A) 1: "Los sujetos alcanzados por el régimen contarán con el detalle de las percepciones que le han sido efectuadas en la factura o documento equivalente".
- Anexo I, A) 2: las percepciones "deberán agruparse por mes calendario y deducirse en los anticipos correspondientes (...) y los coeficientes de distribución que le corresponda entre las jurisdicciones adheridas".
- Anexo II, C: los sumarios los pueden sustanciar solo "las jurisdicciones en las que el agente resulte obligado a actuar como tal".

Las RG 1/2024 a 17/2024 no tienen ninguna sobre percepciones en ventas interjurisdiccionales. La RG 6/2025 (SIRPEI) es solo para aduana.

- ABIERTO: ninguna RG fija la jurisdicción de la percepción. Busqué en los listados de RG de 2020 a 2026 y leí las que tratan percepción o sustento territorial. Falta confirmar el ordenamiento actualizado (RG CA 17/2024 y la posterior de 2025/2026).

## 8. Ley de IVA, artículo sin número a continuación del art. 28: CERRADO, y el dato de la nota está desactualizado

Fuente [L]: `https://servicios.infoleg.gob.ar/infolegInternet/anexos/40000-44999/42701/texact.htm` (InfoLEG, texto actualizado del Decreto 280/97). Los tramos de $ 63.000.000 y $ 126.000.000 no son los vigentes. Esos importes figuran en una copia vieja de la ley en `ar-fe/ley/iva.txt`, que todavía trae el párrafo de ventas al 50 %. Esa copia no es la actual.

En el texto actualizado el artículo está "sustituido por art. 92 de la Ley N° 27.467 B.O. 4/12/2018" y, después, sus párrafos fueron sustituidos por la Ley 27.701. La nota de InfoLEG dice: "(Primer párrafo sustituido por art. 97 de la Ley N° 27.701 B.O. 1/12/2022 con efectos para los hechos imponibles que se perfeccionen a partir del 1º de enero de 2023 .)".

Las tablas están en imágenes dentro de InfoLEG (`ley27701-5.jpg` y `ley27701-6.jpg`). Las leí así:

| Importe de facturación de los 12 meses, sin IVA | Alícuota |
|---|---|
| Igual o inferior a $ 250.000.000 | 2,5 % |
| Superior a $ 250.000.000 hasta $ 500.000.000 | 5 % |
| Superior a $ 500.000.000 hasta $ 1.000.000.000 | 10,5 % |
| Superior a $ 1.000.000.000 | 21,0 % |

Actualización desde 2024:

> "A partir del 1° de enero de 2024, los montos de facturación indicados en el primer y segundo párrafo del presente artículo se actualizarán conforme la variación operada en el límite de ventas totales anuales aplicables a las medianas empresas del Tramo 2 correspondientes al sector servicios, en los términos del artículo 2° de la ley 24.467 y sus modificatorias, y sus normas reglamentarias y complementarias. (Párrafo sustituido por art. 98 de la Ley N° 27.701 B.O. 1/12/2022 .)"

Lo que dice el texto actualizado sobre el alcance:

- El artículo ahora cubre las locaciones de espacios publicitarios en diarios, revistas y publicaciones periódicas, en el primer párrafo.
- También cubre las ediciones periodísticas digitales de información en línea, en el segundo párrafo.
- Para ambos el criterio es la facturación de los últimos 12 meses, evaluada por cuatrimestre calendario.
- Los servicios de distribución, clasificación, reparto y devolución de esas publicaciones, prestados a sujetos de producción editorial, van al 50 % de la alícuota general del art. 28.
- No encontré en ese texto el párrafo de "ventas de diarios, revistas y publicaciones periódicas al 50 %".

Para el monto exacto vigente hoy hace falta el límite de ventas de Tramo 2 sector servicios (Res. SEPYME aplicable). No lo busqué: los 250M/500M/1.000M son la base 2023 y los valores 2026 son otros.

## Abiertos

- **1a**: sin tabla publicada que dé los códigos de IVA 2,5 % y 5 % (en WSFEv1, WSMTXCA, WSBFEV1, tablas de FE y RG 4597).
- **3 (certificado)**: no leí SICORE ni SIRE (RG 2233 y RG 3726).
- **6**: AGIP sin texto vigente ni resolución posterior. La API de agip.gob.ar no sirvió y el Boletín Oficial porteño no se puede buscar sin búsqueda web.
- **7**: ninguna RG de la Comisión Arbitral sobre en qué jurisdicción se percibe, y falta el ordenamiento RG CA actualizado.

Archivos principales leídos:
- `.../ar-ronda2/rg830.txt`
- `.../ar-ronda2/rg2854b.txt`
- `.../ar-ronda2/rg1415.txt`
- `.../ar-ronda2/r5614.txt`
- `.../ar-ronda2/arba/dn.txt`
- `.../ar-ronda2/ca/r5.txt`
- `.../ar-ronda2/ca/r14.txt`
- `.../ar-ronda2/ca/rg9p.txt`
- `.../ar-ronda2/ot/otros.xlsx`
- `.../ar-ronda2/iva_texact.txt`
- `.../ar-ronda2/img/5.jpg`
