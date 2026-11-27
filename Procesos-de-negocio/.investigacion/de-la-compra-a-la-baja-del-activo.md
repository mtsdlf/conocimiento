# Informe crudo: de la compra a la baja del activo (acquire-to-retire)

Sesión 13 de 16 (issue #120), 2026-11-27. Ángulo: la vida del activo propio, de la decisión de invertir a la baja con su resultado, cruzando Activos y mantenimiento, Compras y Contabilidad (#99). La orden de trabajo es un paso; la amortización, de Contabilidad.

Marcas: [L] texto completo leído; [M] metadatos, resumen o parte; [S] resumen secundario o del buscador.

## 1. Lo que ya dicen los temas de dominio (leído entero, [L])

| Nota | Lo que aporta | Término que usa |
|---|---|---|
| `Contabilidad/Operaciones/activos-fijos-y-amortizacion.md` | NIC 16: capitalizar «si, y solo si»; costo; partes significativas; amortización desde que está disponible para usar; revisión de vida útil y residual como cambio de estimación; baja y resultado («Gains shall not be classified as revenue»); deterioro (NIC 36) y revaluación solo nombrados; la amortización no aparta plata | activo fijo; bien de uso; amortización; vida útil; valor residual; baja |
| `Activos-y-mantenimiento/activos-y-mantenimiento.md` | Dos registros del mismo equipo, el operativo y el contable; APQC 10.0 con 10.1 a 10.4; el tema toma 10.3 y la decisión de reemplazar de 10.4 | registro operativo / contable |
| `Activos-y-mantenimiento/Registro-de-activos/registro-de-activos.md` | El ciclo de vida según APQC; el registro nace en 10.2.4.3 y se actualiza en 10.3.2.4; «dar de baja un equipo en el registro físico no da de baja el bien de uso»; fallas del registro (duplicados, ubicación vieja, descripciones libres) | registro de activos; activo físico |
| `Activos-y-mantenimiento/Registro-de-activos/jerarquia-de-activos.md` | El traslado como movimiento fechado; un sistema abierto: el movimiento «records every transfer, issue, and receipt as a separate event» | traslado; ubicación técnica |
| `Activos-y-mantenimiento/Orden-de-trabajo/*.md` | Ciclo de la orden; el cierre pasa el costo a Contabilidad, que decide si se capitaliza («Capitalize Repair Cost», «Routine repair is normally an expense», en un ERP abierto) | orden de trabajo; cierre de la orden |
| `Activos-y-mantenimiento/Desempeno-de-los-activos/reparar-o-reemplazar.md` | Costo del ciclo de vida (NIST Handbook 135), costo anual equivalente, vida económica frente a vida útil; APQC 10.4.1.1 y 10.4.1.2; ejecución del reemplazo en 10.2.3.5; la baja deja dos registros que se cierran por separado | costo del ciclo de vida; costo anual equivalente; vida económica |
| `Activos-y-mantenimiento/Desempeno-de-los-activos/indicadores-de-mantenimiento.md` | MTBF, MTTR, disponibilidad, cumplimiento del preventivo, costo sobre valor de reposición | indicadores de mantenimiento |
| `Activos-y-mantenimiento/Servicio-de-campo/base-instalada.md` | El equipo del cliente: registro operativo «sin contraparte contable» | base instalada |
| `Compras-y-abastecimiento/Orden-de-compra/tipos-de-orden.md` | La compra de una máquina es una orden puntual (criterio de esa base) | orden puntual |
| `Compras-y-abastecimiento/Abastecimiento-estrategico/hacer-o-comprar.md` | APQC 10.1.1.3 «Determine build, buy, or lease decision» aparece en el PCF; la nota de Compras trata hacer o comprar para insumos | hacer o comprar |
| `Tesoreria/Financiamiento/prestamos.md#leasing` | Leasing financiero; la NIIF 16 solo por la página del IASB | leasing |
| `Impuestos/Impuestos-a-la-renta/resultado-impositivo.md` | La amortización como diferencia temporaria; Ley 27.802 (2026), amortización «en dos (2) cuotas anuales, iguales y consecutivas» (art. 182) para inversiones de MiPyMEs | diferencia temporaria |

## 2. Códigos APQC PCF 7.4 (leído en el texto bajado, [L])

URL: https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf

- 10.0 «Acquire, Construct, and Manage Assets»: 10.1 «Plan and acquire assets» (10.1.1.3 «Determine build, buy, or lease decision»); 10.2 «Design and construct assets» (10.2.1.1 «Define capital investment plan»; 10.2.3.3 «Construct new assets»; 10.2.3.4 «Augment existing assets»; 10.2.3.5 «Renew/Replace assets»; 10.2.4.3 «Create work and asset records»); 10.3 «Maintain assets»; 10.4 «Manage asset end-of-life» (10.4.1.1 «Monitor useful life of assets»; 10.4.1.2 «Perform cost vs. benefit analysis for replacement»; 10.4.2 «Decomission productive assets» [sic]; 10.4.3 «Perform sale or trade»; 10.4.5 «Dismantle assets»).
- 9.4 «Manage fixed-asset project accounting»: 9.4.1 «Perform capital planning and project approval» (9.4.1.3 «Review and approve capital projects and fixed-asset acquisitions»; 9.4.1.4 «Conduct financial justification for project approval»); 9.4.2 «Perform capital project accounting» (9.4.2.4 «Close/capitalize projects»; 9.4.2.5 «Measure financial returns on completed capital projects»).
- 9.3.3 «Perform fixed-asset accounting»: 9.3.3.3 «Process and record fixed-asset additions and retires»; 9.3.3.4 «Process and record fixed-asset adjustments, enhancements, revaluations, and transfers»; 9.3.3.5 «Process and record fixed-asset maintenance and repair expenses»; 9.3.3.6 «Calculate and record depreciation expense»; 9.3.3.7 «Reconcile fixed-asset ledger»; 9.3.3.8 «Track fixed-assets including physical inventory»; 9.3.3.9 «Provide fixed-asset data to support tax, statutory, and regulatory reporting».

El brief nombraba 9.4 y 10.0; la contabilidad del activo en uso está en 9.3.3, que hay que sumar.

## 3. Fuentes nuevas

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| IFRS Foundation, NIC 16, texto oficial (HTML 2026) | https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias16.html | primaria | 3/3/1/3 | [L] parcial (párrafos 7, 12, 20, 22, 55, 67, por búsqueda) |
| IAM, What is asset management (cita ISO 55000:2014) | https://theiam.org/what-is-asset-management/ | secundaria de un cuerpo profesional | 2/1/1/2 | [L] |
| APQC, Open Standards Benchmarking Measure List (16/11/2013) | https://www.apqc.org/sites/default/files/APQC%20Benchmarking%20Measures%20List.pdf | primaria | 3/2/1/3 | [L] (sección «Fixed Asset Accounting», 33 medidas) |
| Findlay y Martin, Asset registers: An overlooked foundation of financial integrity, RSM Australia, 4-ago-2026 | https://www.rsm.global/australia/insights/asset-registers-overlooked-foundation-financial-integrity | secundaria (firma de auditoría) | 2/1/1/2 | [L] |
| AnalystPrep y analystnotes, notas de estudio CFA sobre activos de larga vida | https://analystprep.com/cfa-level-1-exam/financial-reporting-and-analysis/financial-statement-disclosures-regarding-ppe-and-intangibles/ | secundaria | 1/1/2/1 | [S] |
| ISO 55000:2024, ficha (vocabulario: «asset life», «life cycle») | https://www.iso.org/standard/83053.html | primaria | 3/–/–/3 | [S] (la definición no se leyó) |

## 4. Afirmaciones

### Reconocimiento, puesta en marcha y costos posteriores (NIC 16, [L] parcial)
- Párr. 7: «The cost of an item of property, plant and equipment shall be recognised as an asset if, and only if:» es probable que fluyan beneficios futuros y el costo se mide con fiabilidad.
- Párr. 12: el servicio diario no se reconoce en el importe en libros («an entity does not recognise in the carrying amount of an item of property, plant and equipment» esos costos).
- Párr. 20: «costs incurred in using or redeploying an item are not included in the carrying amount of that item». Lectura de la base: el traslado de un equipo ya en uso va a resultados.
- Párr. 22: «The cost of a self-constructed asset is determined using the same principles as for an acquired asset».
- Párr. 55: «Depreciation of an asset begins when it is available for use, ie when it is in the location and condition necessary» para operar como pretende la gerencia. La puesta en marcha marca el inicio de la amortización, no la compra ni el primer uso.
- Párr. 67: se da de baja «(a) on disposal; or (b) when no future economic benefits» se esperan de su uso o disposición.
- Resultado de la baja (párr. 71, por Contabilidad): neto de la venta menos valor en libros; «Gains shall not be classified as revenue».
- Deterioro (NIC 36) y revaluación: la nota de Contabilidad solo los nombra; no hay detalle en la base.

### Ciclo de vida (ISO 55000, IAM)
- ISO 55000:2014, 3.2.1: «An asset is an item, thing or entity that has potential or actual value to an organisation»; 3.3.1: asset management es «the coordinated activity of an organisation to realize value from assets» (IAM [L]).
- El IAM describe el ciclo de vida como el que empieza cuando surge la necesidad del activo y llega hasta su disposición, incluidas las obligaciones que quedan después [L, parafraseado por el fetch; sin cita literal].
- La definición de «asset life» (ISO 55000, 3.2.2 en la edición 2014) no se leyó; la ISO 55001 tampoco.

### Activos fantasma y conciliación
- RSM (2026) [L]: en la verificación física aparecen «"Ghost assets" that no longer exist but continue to be depreciated»; recomienda «reconciliations between the fixed asset register, general ledger and operational asset systems». Sin cifras.
- Las cifras del 10 al 30 % de activos fantasma que circulan son de páginas de proveedores de software sin datos rastreables [S]: no entran.
- APQC 9.3.3.7 «Reconcile fixed-asset ledger» y 9.3.3.8 «Track fixed-assets including physical inventory» [L].

### Medidas (APQC Measure List 2013, [L], literal)
- 100733 «Fixed asset transactions resulting from physical inventories as a percentage of total fixed asset transactions» = «([Number of fixed asset transactions from physical inventories] / [Number of fixed asset transactions]) * 100.0». Lectura de la base: mide cuánto tuvo que corregir el inventario físico al registro contable.
- 103518 «Total cost of repair and maintenance per $1,000 gross value of fixed assets» = «[Cost to repair and maintain fixed assets] / ([Gross value of fixed assets] * 0.0010)». Distinto del «costo sobre valor de reposición» de Activos: divide por el valor bruto contable, no por lo que costaría reponer.
- 100008/100009 «Actual capital expenditure as a percentage of budgeted capital expenditures» (un año antes / año más reciente).
- 100586 «Cycle time in days to approve a capital project»; 100592 «Cycle time in days to close a capital project».
- 101903 «Percentage of capital projects completed on time».
- 100964 «Number of fixed assets managed per "perform fixed asset accounting" FTE».
- Edad promedio del parque ≈ amortización acumulada / amortización del período, y vida remanente ≈ valor neto / amortización del período, suponiendo línea recta (notas de estudio CFA [S]). Fuente secundaria única; entra en la nota con «según notas de estudio».
- Costo del ciclo de vida: en reparar-o-reemplazar.md (NIST Handbook 135, cap. 1).

## 5. Variantes

- Arrendamiento: NIIF 16 solo nombrada; la única nota es `Tesoreria/Financiamiento/prestamos.md#leasing`, que no leyó el texto de la norma.
- Activo construido por la propia empresa: APQC 10.2 y NIC 16 párr. 22. No hay nota de dominio que trate la obra en curso o la acumulación del costo de una construcción propia; hueco.
- Equipo en casa del cliente: `Activos-y-mantenimiento/Servicio-de-campo/base-instalada.md`, sin contraparte contable para quien lo mantiene.

## 6. Recurso canónico

NIC 16, párrafos 7, 12, 20, 22, 55 y 67 a 71 (el texto HTML oficial). Para la vida del activo como proceso, APQC 10.0 entero (una página del PCF).

## 7. Huecos

- La decisión de inversión (presupuesto de capital, VAN, aprobación) no tiene nota de dominio: ni Contabilidad de gestión (`presupuesto.md` trata el presupuesto maestro) ni Tesorería la desarrollan. Solo `reparar-o-reemplazar.md` usa el costo anual equivalente.
- Deterioro (NIC 36) y modelo de revaluación (NIC 16): sin nota.
- Activo construido: sin nota (obra en curso, costos que se activan).
- ISO 55000 «asset life» y «life cycle», e ISO 55001: no se leyeron.
- Ninguna cifra con fuente sobre cuántos activos fantasma tiene un registro típico.
- La transferencia entre centros o unidades (APQC 9.3.3.4 «transfers») vista desde Contabilidad: la nota contable no la trata.

## 8. Problemas encontrados en los temas de dominio

- `Contabilidad/Operaciones/activos-fijos-y-amortizacion.md:81`: Tesorería «todavía no escrito»; ya existe.
- `Contabilidad/Operaciones/activos-fijos-y-amortizacion.md`: no trata el traslado (NIC 16 párr. 20), el activo construido (párr. 22) ni cuándo empieza la amortización con la cita del párr. 55 (lo dice sin cita, línea 41). El deterioro queda «no cubierto» (línea 75).
- `Activos-y-mantenimiento/activos-y-mantenimiento.md:54-56`: Compras, Producción y Software de gestión «todavía no armado»; Compras y Producción ya existen.
- `Activos-y-mantenimiento/Orden-de-trabajo/cierre-de-la-orden.md:40`: Administración de personal y nómina «todavía no armado»; ya existe.
- `Activos-y-mantenimiento/Registro-de-activos/registro-de-activos.md:28`: cita la ISO 55000:2014 sin decir que está retirada (lo señaló su propia verificación, `.investigacion/verificacion-estrategia.md:36`).
- `Compras-y-abastecimiento/Orden-de-compra/tipos-de-orden.md:134`: «Activos y mantenimiento, todavía no armado».
- Choque de términos: `Activos-y-mantenimiento/Desempeno-de-los-activos/reparar-o-reemplazar.md:16` tiene como alias «costo total de propiedad, total cost of ownership, TCO», que también son alias de `Compras-y-abastecimiento/Abastecimiento-estrategico/costo-total-de-adquisicion.md` (glosario de Compras, línea 138). Dos notas responden al mismo alias con conceptos parecidos pero no iguales.
- Choque de medidas: «costo sobre valor de reposición» (Activos, `indicadores-de-mantenimiento.md:45`) y APQC 103518 (sobre valor bruto contable) son parecidos y no iguales; ninguna nota lo dice.

## Borrador para la nota de Argentina

Apartado «De la compra a la baja del activo». La base tiene poco de lo propio de la Argentina para este recorrido, y lo dice.

- **Amortización impositiva frente a contable**: la diferencia entre las dos es una diferencia temporaria que se revierte sola; el mecanismo, con un ejemplo, está en [resultado impositivo](../Impuestos/Impuestos-a-la-renta/resultado-impositivo.md#diferencias-permanentes-y-temporarias). La Ley 27.802 (2026) permite a las MiPyMEs amortizar en dos cuotas anuales los bienes muebles de una inversión productiva (arts. 181 y 182, citados allí; ver también [Ganancias en Argentina](../Impuestos/Impuestos-a-la-renta/ganancias-en-argentina.md#reformas-recientes)). Un sistema necesita llevar las dos amortizaciones por bien (inferencia de la base).
- **Ajuste por inflación**: los bienes de uso son partidas no monetarias que se reexpresan por el índice de su mes de origen, por eso cada alta guarda su fecha ([normas contables en Argentina](../Contabilidad/Estados-contables/normas-contables-en-argentina.md#el-ajuste-por-inflación)); el ajuste impositivo, en [Ganancias en Argentina](../Impuestos/Impuestos-a-la-renta/ganancias-en-argentina.md#ajuste-por-inflación-impositivo).
- **Importación de bienes de uso**: exceptuada de las percepciones de IVA y Ganancias al importar hasta el 31/12/2026, en [comercio exterior en Argentina](../Impuestos/comercio-exterior-en-argentina.md#percepciones-al-importar).
- **Mantenimiento obligatorio**: las inspecciones y servicios que exige la norma están en [mantenimiento obligatorio en la Argentina](../Activos-y-mantenimiento/mantenimiento-obligatorio-en-argentina.md).
- **Sin nota todavía**: las vidas útiles impositivas de los bienes de uso en Ganancias, el tratamiento de la venta o el reemplazo de un bien de uso en Ganancias y el IVA en la venta de un bien de uso. Ninguna nota de Impuestos los trata.
