# Informe: Proyectos de inversión en Argentina, evaluación y registro (fecha de consulta 2026-11-27)

Dos límites de método. Se agotó el presupuesto de búsquedas web de la sesión, así que usé solo lectura directa de URL. Y no hay segunda fuente independiente para casi nada: las normas las leí en InfoLEG, ARCA y el Boletín Oficial no abrieron, y lo que dicen los medios sobre el RIMI es secundario. Cuando hay una sola fuente lo digo.

Convención de marcas: [L] texto completo o artículo completo, [M] metadatos, [S] resumen secundario o del buscador. En los puntajes, A es autoridad, P profundidad, E ejemplos, U unicidad y R recencia, cada uno de 1 a 3.

## Componente 1. Inflación y tasas en la evaluación

| Fuente | Tipo | Marca | A/P/E/U/R |
|---|---|---|---|
| BCRA API de estadísticas v4.0, https://api.bcra.gob.ar/estadisticas/v4.0/monetarias?limit=1000 | primaria | [L] parcial (solo se leyeron las primeras ~100.000 de 345.797 caracteres) | 3/2/1/3/3 |
| BCRA, REM, https://www.bcra.gob.ar/PublicacionesEstadisticas/Relevamiento_Expectativas_de_Mercado.asp | primaria | [L] | 3/2/1/3/3 |
| BCRA, Principales variables, https://www.bcra.gob.ar/PublicacionesEstadisticas/Principales_variables.asp | primaria | [M] (lista series sin valores) | 3/1/1/2/3 |
| Damodaran, https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html | secundaria académica reconocida | [L] | 2/2/1/3/2 |

Afirmaciones:
- **Tasas al 2026-11-26.** BADLAR de bancos privados, 23,00 % nominal anual y 25,57 % efectiva anual. TAMAR de bancos privados, 23,9375 % nominal anual y 26,73 % efectiva anual. Fuente: API del BCRA.
- **Inflación.** La inflación mensual de octubre de 2026 fue 2,20 % y la interanual 33,10 % (fecha 2026-10-31). La mediana del REM para la inflación de los próximos 12 meses es 21,80 % (fecha 2026-10-31). Fuente: API del BCRA, ids 27, 28 y 29.
- **REM de octubre de 2026.** Se publicó el 5 de noviembre de 2026, con relevamiento del 28 al 30 de octubre. Proyecta un tipo de cambio mayorista de $1.558 promedio en noviembre y $1.590 en diciembre. Proyecta una TAMAR de 23,90 % TNA para noviembre y 24,00 % para diciembre. El REM da inflación mensual de octubre de 1,8 %, que no coincide con el 2,20 % de la API. La diferencia es esperable: el REM es una expectativa y la API es el dato publicado. Fuente: página del REM.
- **Tipo de cambio.** El mayorista de referencia (id 5) fue 1600,8752 ARS/USD el 2026-11-27. Fuente: API del BCRA. No pude confirmar que sea la serie Com. A 3500. Es una sola fuente.
- **Riesgo país como prima (Damodaran).** Es una sola fuente, con fecha de actualización 5 de enero de 2026 y sin actualización posterior visible. Para Argentina, con rating Moody's Caa1: spread por rating 6,37 %, prima de riesgo país 9,71 % y prima total de capital 13,94 %. El dato tiene casi 11 meses a la fecha de consulta.
- **Tasa real (Fisher).** La relación se puede ilustrar con los datos de arriba: una TAMAR nominal de 23,9 % TNA frente a una inflación esperada a 12 meses de 21,8 % da una tasa real aproximada de (1,239/1,218) − 1 ≈ 1,7 %. Es cálculo mío sobre las dos cifras y no una afirmación de ninguna fuente. Falta una fuente que defina Fisher y la regla de consistencia nominal contra real.
- **UVA.** Aparece como serie 7913 en la página de Principales variables [M]. No obtuve su valor.

## Componente 2. Ajuste por inflación impositivo

| Fuente | Tipo | Marca | A/P/E/U/R |
|---|---|---|---|
| InfoLEG, Decreto 824/2019 (t.o. Ley de Impuesto a las Ganancias), https://servicios.infoleg.gob.ar/infolegInternet/anexos/330000-334999/332890/texact.htm | primaria | [L] por tramos (Título VI y arts. 56-96) | 3/3/1/3/3 |
| InfoLEG, Ley 27.802, https://servicios.infoleg.gob.ar/infolegInternet/anexos/420000-424999/423680/norma.htm | primaria | [L] (Títulos VII a XXV) | 3/3/1/3/3 |
| contadoresenred.com, índices octubre 2026 (https://contadoresenred.com/ajuste-por-inflacion-contable-e-impositivo-indices-octubre-2026/amp/) | secundaria | [S] | 1/1/1/1/3 |
| Cronista (columna sobre Ganancias, URL en el buscador) | secundaria | [S] | 1/1/1/1/3 |

Afirmaciones:
- **Estructura.** El Título VI se llama "AJUSTE POR INFLACIÓN" (arts. 105 a 108 del t.o. 2019). El art. 105 alcanza a los sujetos de los incisos a) a e) del art. 53. Fuente: InfoLEG, Decreto 824/2019.
- **Umbral.** El art. 106 aplica el ajuste cuando la variación del IPC "acumulado en los TREINTA Y SEIS (36) meses anteriores al cierre del ejercicio que se liquida" es "superior al CIEN POR CIENTO (100 %)". El art. 106 inc. c) actualiza por el "Índice de Precios al Consumidor Nivel General (IPC)". Fuente: InfoLEG, Decreto 824/2019.
- **Escalonamiento de los primeros ejercicios.** El mismo art. 106 trae los umbrales de 55 %, 30 % y 15 % para los tres primeros ejercicios. Esto ya no aplica hoy y no lo usaría en la nota.
- **Art. 108.** "No les serán de aplicación las exenciones establecidas en los incisos h) y t) del artículo 26". Fuente: InfoLEG, Decreto 824/2019.
- **Cómputo total desde 2021.** Una fuente secundaria dice que desde los ejercicios iniciados el 1/1/2021 el ajuste se computa al 100 %. La contraste solo con esa fuente secundaria, y el buscador indica que la Ley 27.701 agregó un art. 195 de diferimiento. No leí ese artículo: es una [S] sola. Fuente: contadoresenred.com.
- **Quebrantos.** El art. 190 de la Ley 27.802 sustituye el undécimo párrafo del art. 25: los quebrantos de ejercicios que inicien desde el 1° de enero de 2025 se actualizan por el IPC del INDEC, sin aplicar el primer párrafo del art. 93. Fuente: InfoLEG, Ley 27.802 (sancionada el 27 de febrero de 2026, publicada en el BO el 6 de marzo de 2026).
- **Estado al cierre de 2026.** Con una variación interanual de 33,10 % a octubre, es probable que el acumulado de 36 meses supere 100 %. No lo calculé con la serie del INDEC, así que queda como hueco.
- **Contable.** La RT 6 está dejada sin efecto por la RT 54 (T.O.), que rige para ejercicios iniciados desde el 1/7/2024. La RT 54 trae la sección sobre moneda de cierre en los párrafos 176 a 200. Fuente: https://normasweb.facpce.org.ar/biblioteca/KGVdKpkr/resolucion-tecnica-n-54 [L]. No verifiqué la Res. JG 539/18.
- **Actualización de amortizaciones.** El art. 88 punto 2 actualiza la cuota ordinaria con el índice del art. 93 según la fecha de adquisición o construcción, con la tabla de ARCA del mes de cierre. El art. 93 usa el IPC del INDEC para adquisiciones de ejercicios iniciados desde el 1/1/2018. Fuente: InfoLEG, Decreto 824/2019.
- **Corrección de numeración.** El texto ordenado trae el IPC en arts. 88 y 93. No verifiqué en esta ronda los artículos de la Ley 27.430 ni de la Ley 27.468 que pediste.

## Componente 3. Amortización impositiva de bienes de uso

Fuente única: InfoLEG, Decreto 824/2019 (t.o. 2019), misma URL que arriba [L] por tramos.

- **Art. 86 f)** lista como deducción "Las amortizaciones por desgaste, agotamiento u obsolescencia".
- **Inmuebles, art. 87.** Se deduce un "DOS POR CIENTO (2 %) anual sobre el costo del edificio o construcción". Los bienes de cambio quedan excluidos. ARCA puede admitir una tasa mayor si se prueba una vida útil menor a 50 años.
- **Desde cuándo en inmuebles.** El art. 87 dice que la deducción corre "desde el inicio del trimestre del ejercicio fiscal o calendario en el cual se hubiera producido la afectación".
- **Muebles, art. 88.** Se divide el costo "por un número igual a los años de vida útil probable". ARCA puede admitir otro método técnico, como unidades producidas u horas trabajadas. El texto leído no dice cuándo empieza la amortización de un mueble, así que no lo afirmo.
- **Art. 89** trata gastos de mantenimiento de inmuebles, no amortización. Tu mención de "art. 87/88/89" queda corregida: amortizan los arts. 87 y 88.
- **Diferencia con la contable.** La RT 54 trae el capítulo "BIENES DE USO Y DEPRECIACIONES" (índice, p. 96). No lo leí en profundidad, y esa comparación queda como hueco.

## Componente 4. Regímenes de promoción vigentes al 2026-11-27

| Fuente | Tipo | Marca | A/P/E/U/R |
|---|---|---|---|
| InfoLEG, Ley 27.742, https://servicios.infoleg.gob.ar/infolegInternet/anexos/400000-404999/401266/norma.htm | primaria | [L] por tramos | 3/3/1/3/2 |
| InfoLEG, Decreto 105/2026, https://servicios.infoleg.gob.ar/infolegInternet/verNorma.do?id=423212 | primaria | [L] parcial | 3/2/1/3/3 |
| InfoLEG, Ley 27.802 (Título XXIII), URL del componente 2 | primaria | [L] por tramos | 3/3/1/3/3 |
| argentina.gob.ar/normativa, Decreto 242/2026, https://www.argentina.gob.ar/normativa/nacional/decreto-242-2026-424730/texto | primaria | [L] | 3/3/1/3/3 |
| InfoLEG, Ley 27.264, https://servicios.infoleg.gob.ar/infolegInternet/anexos/260000-264999/263953/norma.htm | primaria | [L] | 3/3/1/3/1 |
| Infobae 2026-05-19 sobre la RGC 5849/2026, URL en el componente anterior | secundaria | [S] | 1/2/1/1/2 |
| Presidencia de la Nación, https://www.argentina.gob.ar/node/497777 | oficial divulgativa | [S] | 2/1/1/2/3 |
| Marval 2026-04-23, https://www.marval.com/Publicacion/rimi-se-reglamenta-el-regimen-17571 | secundaria | [S] | 1/1/1/1/3 |

### RIGI (Ley 27.742)
- **Sanción y publicación.** La ley fue sancionada el 27 de junio de 2024 y publicada el 8 de julio de 2024 ("e. 08/07/2024 Nº 44030/24"). El art. 228 dice que el régimen "entrará en vigencia el día de su publicación en el Boletín Oficial". El texto leído no trae la fecha de promulgación.
- **Plazo de adhesión.** El art. 168 fija "dos (2) años, contados a partir de la entrada en vigencia del presente régimen", con prórroga única de hasta un año. El Decreto 105/2026, firmado el 18 de febrero de 2026 y publicado en el BO el 19 de febrero de 2026 (n.° 35854), prorrogó "POR EL PERIODO DE UN (1) AÑO A CONTAR DESDE EL 8 DE JULIO DE 2026". El vencimiento en torno al 8 de julio de 2027 es inferencia mía de esa redacción. Con esto, el RIGI sigue abierto al 27/11/2026.
- **Mínimo.** El art. 173 pide "al menos doscientos millones de dólares estadounidenses". El Poder Ejecutivo puede fijar montos mayores por sector, hasta USD 900.000.000.
- **Sujetos.** El art. 169 habla de los Vehículos de Proyecto Único (VPU).
- **Ganancias.** El art. 183 a) fija la alícuota del art. 73 en "veinticinco por ciento (25%)".
- **Amortización acelerada.** El art. 183 b) (i) la fija para muebles amortizables en "como mínimo en dos (2) cuotas anuales, iguales y consecutivas". El art. 183 b) (ii) la fija para minas, canteras, bosques, obras de infraestructura y similares con "vida útil reducida al sesenta por ciento (60%) de la estimada".
- **IVA.** La devolución anticipada no figura literal. El art. 187 a) permite pagar el IVA de bienes de capital, obras e infraestructura "a través de la entrega de Certificados de Crédito Fiscal". Si ARCA no devuelve el saldo al proveedor en tres meses, el beneficiario puede transferirlo a terceros.
- **Derechos de exportación.** El art. 191 los exime "luego de transcurridos tres (3) años".
- **Estabilidad.** El art. 201 la fija en treinta años desde la adhesión del VPU.
- **Cuidado con la numeración.** El extracto leído mostró la parte del RIGI desde el art. 164. No leí el encabezado "Título VII" ni los arts. 162 y 163.

### RIMI (Ley 27.802, Título XXIII)
- **Norma de origen.** La Ley 27.802 se sancionó el 27 de febrero de 2026 y se publicó el 6 de marzo de 2026 (art. 217: vigencia desde la publicación). El RIMI está en el Título XXIII, arts. 177 a 184 [L].
- **Beneficiarios.** El art. 179 alcanza a sujetos del art. 53 de la Ley de Ganancias, micro, pequeñas o medianas hasta Mediana Tramo 2. Las inversiones valen en los "dos (2) primeros años" desde la entrada en vigencia del régimen.
- **Mínimos.** El art. 181 fija USD 150.000 para micro, USD 600.000 para pequeñas, USD 3.500.000 para Mediana Tramo 1 y USD 9.000.000 para Mediana Tramo 2.
- **Amortización acelerada.** El art. 182 la fija para muebles en "dos (2) cuotas anuales, iguales y consecutivas". Riego, eficiencia energética, semovientes y mallas antigranizo van en una sola cuota. Las obras se amortizan en el 60 % de su vida útil estimada.
- **IVA.** El art. 183 permite pedir la devolución "luego de transcurridos tres (3) períodos fiscales mensuales". El Decreto 242/2026 la limita a "no más del CINCUENTA POR CIENTO (50 %)" de la cuota anual del art. 24 de la Ley de IVA.
- **Exclusiones.** El art. 180 excluye "activos financieros, de portfolio y bienes de cambio". El art. 184 excluye, entre otros, a quienes tengan deudas fiscales firmes y exigibles o accedan al RIGI por las mismas inversiones.
- **Reglamentación.** El Decreto 242/2026 se firmó el 10 de abril de 2026 y se publicó en el BO n.° 35887 el 13 de abril de 2026. Rige desde su publicación (art. 12). Cubre bienes BK y BIT del Decreto 557/23, obras con menos de 30 % de avance a la entrada en vigencia, y bienes de alta eficiencia energética. ARCA, con las Secretarías de Agricultura y de Energía, debía dictar normas complementarias en 30 días (art. 11).
- **Resolución General Conjunta 5849/2026.** Se publicó el 19 de mayo de 2026. Según Infobae [S], los dos años corren desde esa fecha y exige Certificado MiPyME vigente. Según la misma fuente, la adhesión pasa por un Sistema de Gestión de Inversiones (SGI) que ARCA "aún no lanzó". No leí la resolución, así que no la afirmo como primaria.
- **Estado operativo.** No pude confirmarlo al 2026-11-27. Las fuentes más recientes que leí son de mayo de 2026. Es el hueco más importante.
- **Fuente única en los montos.** El texto de los mínimos y de la devolución está en la Ley 27.802, con coincidencia en Presidencia y Marval [S]. Es una sola fuente primaria.

### Ley 27.264 (pymes)
- **Vencida en inversiones.** El art. 15 limita las disposiciones del Título III a las inversiones productivas hechas "desde el 1° de julio de 2016 hasta el 31 de diciembre de 2018, inclusive". La ley se sancionó el 13 de julio de 2016. No encontré una prórroga. Es una sola fuente.
- **Beneficios.** El art. 24 daba un pago a cuenta de Ganancias del 10 % de la inversión productiva, con tope del 2 % de las ventas netas. El art. 27 daba un bono de crédito fiscal de IVA. No hay amortización acelerada en esa ley.
- **Lo que sigue vigente.** El art. 1 vuelve permanente el programa de Recuperación Productiva. El art. 6 sigue con el pago a cuenta con el impuesto a los créditos y débitos. No verifiqué el estado de este último.

### Economía del Conocimiento (Ley 27.506)
No la leí. Es un hueco, y solo importa si da beneficios sobre bienes de uso.

## Componente 5. Activación de intereses y diferencia de cambio

Fuente: FACPCE, RT 54 (T.O.), https://normasweb.facpce.org.ar/biblioteca/KGVdKpkr/resolucion-tecnica-n-54. Primaria, [L] (extraje el texto del PDF y leí los párrafos 125, 136 a 142). Puntaje 3/3/1/3/3. Es una sola fuente.

- **Vigencia y reemplazo de la RT 17.** La RT 54 (T.O.) rige para ejercicios iniciados desde el 1 de julio de 2024, con aplicación anticipada desde el 1 de enero de 2023. Deja sin efecto la RT 17 (y la RT 6). Fue modificada por las RT 56 y 59, la RT 62 y la Res. JG 656/25. La fecha de aprobación de la RT 54 original es el 1 de julio de 2022, con T.O. del 22 de mayo de 2024.
- **Opción.** El párrafo 136 permite contabilizar los costos financieros "como gastos del período" o "como parte del costo de un activo apto para activación de costos financieros generados por deudas computables".
- **Cuándo no se activa.** El párrafo 137 lo prohíbe si el proceso se prolonga más de lo técnicamente requerido, está interrumpido sin necesidad, o ya terminó y el activo está listo para usarse.
- **Cómo se aplica.** El párrafo 138 pide aplicar la política "de manera consistente" a todos los activos aptos del rubro, bienes de uso entre ellos. Primero se activan las deudas específicas y después las no específicas.
- **Deuda específica.** Del costo activable se resta el ingreso de las colocaciones transitorias (párrafo 139).
- **Deuda no específica.** Se aplica una tasa promedio mensual al promedio mensual de los activos aptos (párrafo 140).
- **Tope.** No se puede activar más que los costos financieros del ejercicio (párrafo 141).
- **Diferencias de cambio.** El párrafo 125 las contabiliza como ingresos financieros o costos financieros "de acuerdo con lo establecido por el párrafo 136". Es decir, las de deuda en moneda extranjera entran en la misma opción de activar o llevar a gastos.
- **Con ajuste por inflación.** Si se activa, el párrafo 142 pide hacerlo "netos del resultado por exposición al cambio en el poder adquisitivo de la moneda".

## Huecos y qué faltaría para cerrarlos

1. **Estado operativo del RIMI al 2026-11-27.** Falta el estado del SGI, la RGC 5849/2026 en texto y las resoluciones de Agricultura y Energía. Se cierra con la Biblioteca de ARCA o el Boletín Oficial de noviembre de 2026.
2. **Texto de la RGC 5849/2026.** Los mínimos y la ventana vienen de la ley y de un medio. Falta el texto oficial.
3. **Ley 27.742, Título VII.** No leí su encabezado ni los arts. 162 y 163. Las numeraciones citadas salen del texto de InfoLEG. Tampoco leí el Decreto 1092/2024 ni el reglamento del RIGI.
4. **Umbral del ajuste por inflación.** Falta calcular el IPC acumulado a 36 meses con el INDEC. Tampoco leí el art. 195 (Ley 27.701) sobre el diferimiento ni las Leyes 27.430 y 27.468.
5. **Cuándo se empieza a amortizar un mueble en Ganancias** y la interacción de la amortización con el ajuste por inflación (art. 106). El art. 88 no lo dice.
6. **Comparación con la amortización contable.** Falta leer el capítulo de bienes de uso de la RT 54.
7. **Evaluación nominal contra real y Fisher.** No encontré el texto de Sapag Chain ni de la FCE-UBA o de un consejo profesional. Se cierra con la cita directa de un texto de evaluación de proyectos.
8. **UVA y serie 3500.** Falta el valor de la UVA y la confirmación de que el tipo de cambio leído es el de la Com. A 3500.
9. **Riesgo país.** Solo hay Damodaran de enero de 2026. Falta una actualización posterior o una segunda fuente.
10. **Economía del Conocimiento (Ley 27.506).** No investigada.
11. **Segunda fuente independiente.** Salvo la coincidencia entre la ley, Presidencia y Marval sobre el RIMI, todo lo normativo es una sola fuente.

Sources:
- [Decreto 242/2026](https://www.argentina.gob.ar/normativa/nacional/decreto-242-2026-424730/texto)
- [Ley 27.742 en InfoLEG](https://servicios.infoleg.gob.ar/infolegInternet/anexos/400000-404999/401266/norma.htm)
- [Ley 27.802 en InfoLEG](https://servicios.infoleg.gob.ar/infolegInternet/anexos/420000-424999/423680/norma.htm)
- [Decreto 824/2019 en InfoLEG](https://servicios.infoleg.gob.ar/infolegInternet/anexos/330000-334999/332890/texact.htm)
- [Ley 27.264 en InfoLEG](https://servicios.infoleg.gob.ar/infolegInternet/anexos/260000-264999/263953/norma.htm)
- [Decreto 105/2026 en InfoLEG](https://servicios.infoleg.gob.ar/infolegInternet/verNorma.do?id=423212)
- [RT 54 en FACPCE](https://normasweb.facpce.org.ar/biblioteca/KGVdKpkr/resolucion-tecnica-n-54)
- [API de estadísticas del BCRA](https://api.bcra.gob.ar/estadisticas/v4.0/monetarias?limit=1000)
- [REM del BCRA](https://www.bcra.gob.ar/PublicacionesEstadisticas/Relevamiento_Expectativas_de_Mercado.asp)
- [Damodaran, prima de riesgo país](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html)
- [Infobae sobre la RGC 5849/2026](https://www.infobae.com/economia/2026/05/19/arca-reglamento-el-rimi-y-las-pymes-estan-a-paso-de-acceder-a-los-incentivos-para-inversiones-las-10-claves-del-regimen/)
- [Presidencia, RIMI](https://www.argentina.gob.ar/node/497777)
- [Marval, RIMI](https://www.marval.com/Publicacion/rimi-se-reglamenta-el-regimen-17571)
- [contadoresenred.com, índices de octubre de 2026](https://contadoresenred.com/ajuste-por-inflacion-contable-e-impositivo-indices-octubre-2026/amp/)