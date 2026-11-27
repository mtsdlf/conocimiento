---
resumen: >-
  En Argentina, evaluar una inversión pide resolver primero en qué moneda y en qué unidad se cuenta, porque la inflación hace que un flujo nominal descontado con una tasa real (o al revés) dé cualquier cosa; después pesan cómo se amortiza el bien para Ganancias, el ajuste por inflación impositivo y dos regímenes de promoción vigentes a fines de 2026, el RIGI para inversiones muy grandes y el RIMI para las de micro, pequeñas y medianas empresas.
estado: borrador
estabilidad: volatil
fuentes:
  - "Damodaran, Applied Corporate Finance, 4.ª ed., presentaciones del cap. 5, sobre la consistencia entre flujo y tasa (leído): https://pages.stern.nyu.edu/~adamodar/pdfiles/acf4E/presentations/invretA.pdf"
  - "Damodaran, Country Default Spreads and Risk Premiums, actualización del 5 de enero de 2026 (leído): https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html"
  - "Decreto 824/2019, texto ordenado de la Ley de Impuesto a las Ganancias, en InfoLEG, arts. 86 a 88, 93 y 105 a 108 (leído en esos artículos): https://servicios.infoleg.gob.ar/infolegInternet/anexos/330000-334999/332890/texact.htm"
  - "Ley 27.742, Título del Régimen de Incentivo para Grandes Inversiones, en InfoLEG, arts. 164 a 228 (leído por tramos): https://servicios.infoleg.gob.ar/infolegInternet/anexos/400000-404999/401266/norma.htm"
  - "Decreto 105/2026 (BO 19/02/2026), prórroga del plazo de adhesión al RIGI, en InfoLEG (leído en parte): https://servicios.infoleg.gob.ar/infolegInternet/verNorma.do?id=423212"
  - "Ley 27.802 (BO 06/03/2026), Título XXIII, arts. 177 a 188, en InfoLEG (leído en esos artículos): https://servicios.infoleg.gob.ar/infolegInternet/anexos/420000-424999/423680/norma.htm"
  - "Decreto 242/2026 (BO 13/04/2026), reglamentación del RIMI (leído): https://www.argentina.gob.ar/normativa/nacional/decreto-242-2026-424730/texto"
  - "Infobae, ARCA reglamentó el RIMI (19/05/2026), sobre la Resolución General Conjunta 5849/2026 (según su resumen): https://www.infobae.com/economia/2026/05/19/arca-reglamento-el-rimi-y-las-pymes-estan-a-paso-de-acceder-a-los-incentivos-para-inversiones-las-10-claves-del-regimen/"
  - "Ley 27.264, Título III, arts. 15, 24 y 27, en InfoLEG (leído): https://servicios.infoleg.gob.ar/infolegInternet/anexos/260000-264999/263953/norma.htm"
  - "FACPCE, Resolución Técnica 54 (texto ordenado), párrafos 125 y 136 a 142 (leído en esos párrafos): https://normasweb.facpce.org.ar/biblioteca/KGVdKpkr/resolucion-tecnica-n-54"
  - "Proyectos-de-inversion/.investigacion/argentina.md (2026-11-27)"
aliases: [proyectos de inversión en Argentina, evaluación de proyectos en Argentina, inflación en la evaluación de proyectos, RIGI, Régimen de Incentivo para Grandes Inversiones, RIMI, Régimen de Incentivo para Medianas Inversiones, amortización acelerada, amortización impositiva, bienes de uso en Ganancias, Ley 27.742, Ley 27.802, Decreto 242/2026, investment appraisal in Argentina]
creado: 2026-11-27
revisado:
---

# Proyectos de inversión en Argentina

En Argentina, evaluar una inversión pide resolver primero en qué moneda y en qué unidad se cuenta, porque la inflación hace que un flujo nominal descontado con una tasa real (o al revés) dé cualquier cosa; después pesan cómo se amortiza el bien para Ganancias, el ajuste por inflación impositivo y dos regímenes de promoción vigentes a fines de 2026, el RIGI para inversiones muy grandes y el RIMI para las de micro, pequeñas y medianas empresas.

Es la nota local de [Proyectos de inversión](proyectos-de-inversion.md). Toca sobre todo la [evaluación](Evaluacion/evaluacion-de-la-inversion.md) y el [cierre](Cierre/cierre-de-la-inversion.md). Las normas cambian seguido: lo que sigue es una copia de noviembre de 2026, y cada dato lleva su norma para volver a mirarla.

## Pesos de cada año, pesos de hoy o dólares

La regla general está en [flujo de fondos del proyecto](Evaluacion/flujo-de-fondos-del-proyecto.md#pesos-de-hoy-o-pesos-de-cada-año): flujo y tasa en la misma moneda y la misma unidad. Damodaran: «If the cash flows are nominal (real), the discount rate has to be nominal (real)». Con inflación alta hay tres maneras coherentes de hacerlo:

| Se cuenta en | Los flujos | La tasa | Cuidado con |
|---|---|---|---|
| Pesos de cada año (nominal) | Con la inflación esperada en cada precio y costo | Nominal en pesos | Que todos los precios suban con su propia inflación, no con una sola |
| Pesos de hoy (real) | Sin inflación, a precios de hoy | Real, sin inflación | Los impuestos y el capital de trabajo, que no siguen la inflación (abajo) |
| Dólares | Convertidos con el tipo de cambio esperado de cada año | En dólares | Que los costos en pesos y el tipo de cambio no se muevan igual |

Las tres dan el mismo resultado si los supuestos son coherentes entre sí. Para elegir, una lectura de esta base sin fuente con método: si la empresa compra y vende en pesos, pesos de cada año con la inflación esperada del REM deja modelar bien el impuesto y el capital de trabajo; si sus precios y su equipo siguen al dólar, conviene contar en dólares. Damodaran pasa de una tasa en dólares a una en otra moneda con la diferencia de inflaciones; la ecuación de Fisher, para pasar de nominal a real, está en [costo del financiamiento](../Tesoreria/Financiamiento/costo-del-financiamiento.md#la-tasa-real-con-inflación). Las tasas, la inflación pasada y esperada y el tipo de cambio de noviembre de 2026 están en [tasas de referencia en Argentina](../Tesoreria/tasas-de-referencia-en-argentina.md); esta nota no las repite.

Contar en pesos de hoy tiene una trampa, que esta base deduce de cómo funciona el impuesto. La amortización impositiva se calcula sobre el costo histórico y, si no se actualiza, su beneficio fiscal pierde valor con la inflación. Lo mismo pasa con el capital de trabajo: el stock y el crédito a clientes hay que reponerlos a precios nuevos. Un flujo en pesos de hoy que no lo corrige sale mejor de lo que es. La actualización que hoy prevé la ley está abajo.

Si la tasa se arma desde una tasa en dólares, se le suele sumar una prima por riesgo país. Damodaran publica una para cada país; en su actualización del 5 de enero de 2026, con calificación Caa1, da para Argentina una prima por riesgo país de 9,71 % y una prima total del capital propio de 13,94 %. Es una sola fuente y tiene casi once meses a la fecha de esta copia.

## Cuándo empieza a amortizarse para Ganancias

La amortización del bien es una deducción del impuesto a las ganancias (art. 86, inc. f del texto ordenado en 2019) y por eso entra en el [flujo de fondos](Evaluacion/flujo-de-fondos-del-proyecto.md#de-la-ganancia-al-flujo) como beneficio fiscal. Cuando la amortización impositiva y la contable difieren, la diferencia es temporaria, como explica [resultado impositivo](../Impuestos/Impuestos-a-la-renta/resultado-impositivo.md#diferencias-permanentes-y-temporarias).

- **Edificios y construcciones** (art. 87): «DOS POR CIENTO (2 %) anual sobre el costo del edificio o construcción», desde el inicio del trimestre en que el bien se afectó a la actividad. ARCA puede admitir una tasa mayor si se prueba una vida útil menor a 50 años.
- **Bienes muebles** (art. 88): el costo se divide «por un número igual a los años de vida útil probable», y ARCA puede admitir otro método técnico, como unidades producidas u horas trabajadas. La cuota se actualiza con el índice del art. 93 según la fecha de compra o construcción; para lo comprado en ejercicios iniciados desde 2018, ese índice es el IPC del INDEC.

La fecha que manda para Ganancias en los edificios es la de afectación a la actividad, que no tiene por qué coincidir con la contable de «disponible para usar» de [activación de la obra](Cierre/activacion-de-la-obra.md). Para un sistema, eso pide guardar las dos (inferencia de esta base).

> [!NOTE] Sin fuente todavía: desde cuándo se amortiza un bien mueble para Ganancias; el art. 88 leído no lo dice. Tampoco se comparó con la amortización contable del capítulo de bienes de uso de la RT 54.

## El ajuste por inflación

Para Ganancias, las sociedades ajustan su resultado por inflación cuando el IPC acumulado en los 36 meses anteriores al cierre supera el 100 % (arts. 105 a 108). Cómo funciona y si el umbral se cumple en los cierres de 2026 está en [Ganancias en Argentina](../Impuestos/Impuestos-a-la-renta/ganancias-en-argentina.md#ajuste-por-inflación-impositivo). Para evaluar una inversión importa por una razón: cambia el impuesto de los años del proyecto, y con eso el flujo. Si el ajuste rige o no en los años que se proyectan es un supuesto que conviene poner a la vista en el [análisis de sensibilidad](Evaluacion/analisis-de-sensibilidad.md).

Los estados contables, en cambio, se reexpresan por inflación desde 2018, con otro procedimiento; está en [normas contables en Argentina](../Contabilidad/Estados-contables/normas-contables-en-argentina.md#el-ajuste-por-inflación).

## Los intereses de la obra en la norma contable argentina

La RT 54 deja elegir: los costos financieros se pueden llevar «como gastos del período» o como parte del costo de un activo apto (párrafo 136), con la misma política para todos los activos aptos del rubro (párrafo 138). Las diferencias de cambio de una deuda en moneda extranjera entran en la misma opción (párrafo 125), y con ajuste por inflación lo que se activa va neto del resultado por exposición a la inflación (párrafo 142). Es una diferencia con la NIC 23, que obliga a activar. El detalle contable está en [activo construido en Argentina](../Contabilidad/Operaciones/activo-construido-en-argentina.md).

## RIGI: inversiones muy grandes

El Régimen de Incentivo para Grandes Inversiones está en la Ley 27.742, publicada el 8 de julio de 2024, que lo puso en vigencia ese día (art. 228). Lo que dice el texto leído:

- **Para quién.** Vehículos de proyecto único (art. 169), con una inversión de «al menos doscientos millones de dólares estadounidenses» (art. 173); el Poder Ejecutivo puede fijar montos mayores por sector.
- **Hasta cuándo.** La adhesión tenía un plazo de dos años con una prórroga posible de uno (art. 168). El Decreto 105/2026 la prorrogó «POR EL PERIODO DE UN (1) AÑO A CONTAR DESDE EL 8 DE JULIO DE 2026»; por lectura de esta base, vence hacia el 8 de julio de 2027.
- **Qué da.** Alícuota de Ganancias de «veinticinco por ciento (25%)» (art. 183 a); amortización acelerada de los bienes muebles en «como mínimo en dos (2) cuotas anuales, iguales y consecutivas» y de las obras de infraestructura con vida útil reducida al 60 % (art. 183 b); el IVA de bienes de capital y obras se puede pagar con certificados de crédito fiscal (art. 187); exención de derechos de exportación después de tres años (art. 191); y estabilidad por treinta años desde la adhesión (art. 201).

El umbral deja afuera a casi cualquier empresa en marcha mediana; el RIGI se nombra para saber que existe.

## RIMI: inversiones de micro, pequeñas y medianas empresas

El Régimen de Incentivo para Medianas Inversiones está en el Título XXIII de la Ley 27.802 (arts. 177 a 188), publicada el 6 de marzo de 2026, y lo reglamentó el Decreto 242/2026, publicado el 13 de abril de 2026.

| Punto | Qué dice | Norma |
|---|---|---|
| Quién | Sujetos del art. 53 de Ganancias que sean micro, pequeñas o medianas empresas hasta la mediana tramo 2 (las categorías del régimen MiPyME) | Ley 27.802, art. 179 |
| Cuándo | Las inversiones hechas en los «dos (2) primeros años» del régimen | Art. 179 |
| Mínimo | USD 150.000 (micro), USD 600.000 (pequeña), USD 3.500.000 (mediana tramo 1), USD 9.000.000 (mediana tramo 2) | Art. 181 |
| Amortización | Bienes muebles en dos cuotas anuales iguales y consecutivas; riego, eficiencia energética, semovientes y mallas antigranizo, en una; obras, en el 60 % de su vida útil | Art. 182 |
| IVA | Devolución del crédito fiscal «luego de transcurridos tres (3) períodos fiscales mensuales», hasta «no más del CINCUENTA POR CIENTO (50 %)» del cupo anual del régimen de devolución que sigue al art. 24 de la Ley de IVA, que fija cada Ley de Presupuesto | Art. 183 y Decreto 242/2026 |
| Cuándo cuenta y cuándo se pierde | La inversión se considera hecha en el ejercicio en que el bien se pone en marcha y se afecta a la actividad; el beneficio caduca si el bien sale del patrimonio antes de dos años fiscales, con excepciones, y hay multas de hasta dos veces el beneficio | Arts. 185 a 187 |
| Qué no | «activos financieros, de portfolio y bienes de cambio»; tampoco quien tenga deudas fiscales firmes o use el RIGI para la misma inversión | Arts. 180 y 184 |

El decreto alcanza a bienes de capital y de informática del Decreto 557/23, a obras con menos del 30 % de avance al entrar en vigencia y a bienes de alta eficiencia energética. Según un diario, la Resolución General Conjunta 5849/2026, de mayo, fija que los dos años corren desde su publicación, pide el certificado MiPyME vigente y hace la adhesión por un sistema de ARCA que en ese momento no estaba habilitado; la resolución no se leyó.

Para la evaluación, la amortización acelerada adelanta el beneficio fiscal de la amortización sin agrandarlo (el impuesto vuelve en los años siguientes, como advierte [resultado impositivo](../Impuestos/Impuestos-a-la-renta/resultado-impositivo.md#cómo-falla)), y la devolución del crédito de [IVA](../Impuestos/Impuestos-al-consumo/iva-en-argentina.md#liquidación-mensual-y-saldos) libera capital de trabajo antes. Las dos mejoran el VAN y acortan el repago; cuánto, depende de la tasa y del impuesto de cada caso (lectura de esta base).

> [!NOTE] Sin fuente todavía: si el RIMI estaba operativo al 27 de noviembre de 2026 (el sistema de adhesión de ARCA y las normas complementarias). Lo más reciente que se leyó es de mayo de 2026. Se cierra con la Biblioteca electrónica de ARCA o el Boletín Oficial.

## Lo que ya no rige

El régimen de fomento de inversiones pyme de la Ley 27.264 (2016) daba un pago a cuenta de Ganancias del 10 % de la inversión, con tope del 2 % del promedio de los ingresos netos del año y del anterior, 3 % para las industrias manufactureras micro, pequeñas y medianas tramo 1 (art. 24), y un bono de crédito fiscal por el IVA (art. 27), para inversiones hechas «entre el 1° de julio de 2016 y el 31 de diciembre de 2018, ambas fechas inclusive» (art. 15). No se encontró una prórroga. Se nombra porque todavía aparece en material de consulta.

> [!NOTE] Sin fuente todavía: una segunda fuente independiente para los datos normativos de esta nota (salvo el RIMI, que coincide con un resumen oficial y uno de un estudio jurídico); un texto de evaluación de proyectos usado en la Argentina sobre cómo tratar la inflación; y si la Ley 27.506 de economía del conocimiento da beneficios sobre bienes de uso.
