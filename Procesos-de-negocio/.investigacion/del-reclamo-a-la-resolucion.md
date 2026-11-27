# Del reclamo a la resolución (issue-to-resolution): informe de investigación

Fecha: 2026-11-27. Sesión 13 de 16 (issue #120). Alcance: el recorrido que empieza cuando el cliente reclama (se abre un caso) y termina cuando el caso se cierra con la solución aplicada y registrada, con lo que vuelve a otros dominios: logística inversa, reingreso al stock, no conformidad, visita técnica, nota de crédito y reembolso (decisión de #99). La calidad es un paso, no un proceso propio.

Marcas: [L] texto completo leído (o la tabla/página entera), [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntaje 1-3 en autoridad / profundidad / ejemplos / unicidad (A/P/E/U).

## Fuentes

| Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|
| APQC, PCF Cross Industry 7.4 (agosto 2024), copia de la IFRC | https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf | primaria | 3/2/1/3 | [L] (grep por código) |
| APQC, Open Standards Benchmarking Measure List (2013) | https://www.apqc.org/sites/default/files/APQC%20Benchmarking%20Measures%20List.pdf | primaria | 3/1/1/3 | [L] de las filas citadas |
| APQC, «End-to-End Process Map and Measures: Issue-to-Resolution» | https://www.apqc.org/resource-library/resource-listing/end-end-process-map-and-measures-issue-resolution | primaria | 3/1/1/3 | [S] (solo socios; resumen del buscador) |
| APQC, medida «Warranty costs (repair and replacement) as a percentage of sales» | https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/warranty-costs-repair-and-replacement | primaria | 3/1/1/2 | [S] (403); nombre e ID [L] en la lista de 2013 |
| Romney y Steinbart (atribuido), *Accounting Information Systems*, cap. 12, diapositivas de Pearson (2012) | https://docs.google.com/presentation/d/1PJd1Bx3TA6fdXV6Rb7I1A62ffB9AT02d/htmlpresent | primaria (material del libro) | 3/2/1/2 | [L] de las diapositivas; autoría [S] |
| ISO 10002:2018 (vía la nota `../Servicio-al-cliente/Caso/reclamo.md`) | https://www.iso.org/standard/71580.html | primaria | 3/2/1/3 | no releída: se enlaza la nota, que leyó la definición y el índice |
| Notas de dominio (Servicio al cliente, Relación con clientes, Inventario, Cadena, Producción, Activos, Contabilidad, Impuestos, Tesorería, Comercio electrónico) | rutas abajo | secundaria interna | — | [L] |

## Afirmaciones

### Borde y piezas APQC

- APQC publica un mapa de punta a punta «Issue-to-Resolution»; según su resumen público, es un enfoque coordinado para encontrar, evaluar y llevar a las personas correctas a resolver un problema o consulta, y muchas versiones incluyen el análisis sistemático de los problemas para mejorar productos o procesos. [S] https://www.apqc.org/resource-library/resource-listing/end-end-process-map-and-measures-issue-resolution
- Piezas del PCF 7.4, literales [L]:
  - 6.2.3 «Manage customer complaints» (10389): 6.2.3.1 «Receive customer complaints», 6.2.3.2 «Route customer customer complaints» (sic), 6.2.3.3 «Resolve customer complaints», 6.2.3.4 «Respond to customer customer complaints» (sic), 6.2.3.5 «Analyze customer complaints and response/redressal».
  - 6.2.4 «Process returns» (20094): 6.2.4.1 «Authorize return», 6.2.4.2 «Process return and record reason».
  - 6.3.2 «Process warranty claims» (12669), diez pasos: 6.3.2.1 «Receive warranty claim», 6.3.2.2 «Validate warranty claim», 6.3.2.3 «Investigate warranty issues» (con 6.3.2.3.2 «Schedule field service», 6.3.2.3.3 «Request and receive defective part», 6.3.2.3.4 «Investigate issue/perform root cause analysis»), 6.3.2.4 «Determine responsible party», 6.3.2.6 «Approve or reject warranty claim», 6.3.2.7 «Notify originator of approve/reject decision», 6.3.2.8 «Authorize payment», 6.3.2.9 «Close claim», 6.3.2.10 «Reconcile warranty transaction disposition».
  - 6.3.3 «Manage supplier recovery» (20106).
  - 6.3.4 «Service products» (10218), con 6.3.4.1.3 «Generate service order» y 6.3.4.3.2 «Execute product repair».
  - 4.4.2.4 «Manage flow of returned products» (10352); 4.4.2.5 «Manage disposition of returned products» (20109), con 4.4.2.5.4 «Return to finished goods inventory».
  - 4.3.3.5 «Track and analyze non-conformance trends».
  - 9.2.2.5 «Resolve customer billing inquiries» (10798); 9.2.5 «Manage and process adjustments/deductions» (10746).
  - 6.5.2 «Measure customer satisfaction with customer-complaint handling and resolution» (10402); 6.5.4 «Evaluate and manage warranty performance» (12672).
- 6.1.6 en el PCF 7.4 se llama «Define warranty claims» (20089), no «Define warranty offering» como dice `../Servicio-al-cliente/Caso/garantia-y-reparacion.md`, que citó una copia sin versión. Para informar a la sesión principal.

### Controles del lado contable

- Amenaza «Inaccurate or invalid credit memos»; controles: «Segregation of duties of credit memo authorization from both sales order entry and customer account maintenance» y «Configuration of system to block credit memos unless there is either corresponding documentation of return of damaged goods or specific authorization by management». [L] diapositivas Pearson 2012 (ciclo de ingresos).
- La nota de crédito de una devolución revierte la venta y el costo (Devoluciones sobre ventas contra Cuentas a cobrar; Inventario contra Costo de lo vendido), ejemplo de OpenStax 6.4 ya en `../Contabilidad/Operaciones/ingresos-y-cuentas-a-cobrar.md#la-factura-la-nota-de-crédito-y-el-cobro`. [L de la nota]

### Medidas (APQC OSB, lista 2013) [L]

- 104217 «Warranty costs (repair and replacement) as a percentage of sales»; fórmula «[Warranty costs as a percentage of sales]». Según el resumen del buscador de la página de la medida, los costos incluyen mano de obra, materiales y diagnóstico de lo devuelto [S].
- 104208 «Value of returned products as a percentage of sales».
- 103155 «Return processing cycle time in days».
- 101913 «Percentage of corrective actions for customer complaints that are completed within 15 days».
- 100731 «First contact resolution rate for inquiries on existing orders and service-after-sales requests».
- 100628 «Cycle time in days to resolve adjustments» (lista de cuentas a cobrar 2012).
- Ninguna lista abierta trae una medida del tiempo de punta a punta del reclamo al cierre; el mapa Issue-to-Resolution de APQC es solo para socios. Hueco.
- Resolución al primer contacto (cuatro definiciones), reaperturas y su control, ya en `../Servicio-al-cliente/Calidad-del-servicio/metricas-de-atencion.md` [L]. Tiempo de resolución contra el acuerdo, con reloj que se pausa, en `../Servicio-al-cliente/Niveles-de-servicio/tiempos-de-respuesta-y-resolucion.md` [L de títulos y resumen]. Resolver en la primera visita, en `../Activos-y-mantenimiento/Servicio-de-campo/visita-tecnica.md#resolver-en-la-primera-visita` [L].

### Lo que ya está en los dominios (verificado leyendo las notas)

- Caso, estados (resuelto lo cree el equipo, cerrado lo confirma el cliente), cierre y reapertura: `../Servicio-al-cliente/Caso/caso.md` [L].
- Reclamo e ISO 10002 (nueve pasos, de la comunicación al cierre; cláusula 8 de análisis): `../Servicio-al-cliente/Caso/reclamo.md` [L].
- Garantía y reparación: autorización de devolución, cinco resoluciones disparadas desde el caso (reembolso con nota de crédito, cupón, devolución con movimiento inverso, reparación con orden, servicio de campo) y la tabla de dónde termina el caso: `../Servicio-al-cliente/Caso/garantia-y-reparacion.md` [L].
- Derivación al técnico; el caso sigue abierto mientras dura la visita: `../Servicio-al-cliente/Escalamiento/derivacion-al-tecnico.md` [L]. El cierre de la visita vuelve al caso: `../Activos-y-mantenimiento/Servicio-de-campo/visita-tecnica.md#el-cierre-vuelve-al-caso` [L].
- Logística inversa: autorización, disposición con las cuatro tareas de APQC 4.4.2.5, la plata no es de Cadena: `../Cadena-de-suministro-y-logistica/Despacho-y-entrega/logistica-inversa.md` [L].
- Recepción de devoluciones a un estado no disponible hasta decidir: `../Inventario-y-depositos/Operacion-del-deposito/recepcion.md` (línea 46) [L]; estados (cuarentena «Lo pone la recepción o un reclamo»): `../Inventario-y-depositos/Existencias/estados-del-stock.md` [L]. Término acordado en los alcances de Inventario y Cadena: «reingreso al stock».
- No conformidad: «El reclamo del cliente entra por Servicio al cliente; cuando se confirma un defecto del producto, se abre acá la no conformidad»; la acción correctiva se abre, entre otros casos, cuando la falla «llega del cliente»: `../Produccion/Calidad/no-conformidad.md` [L].
- Problema y causa raíz: `../Servicio-al-cliente/Escalamiento/problema-y-causa-raiz.md` [L de títulos].
- Devoluciones en una tienda: `../Comercio-electronico/Operaciones-del-comercio/devoluciones.md` [L].
- Disputas y deducciones en la cobranza: `../Tesoreria/Credito-y-cobranzas/gestion-de-la-cobranza.md#disputas-y-deducciones` [L].
- Nota de crédito como comprobante: `../Impuestos/Cumplimiento/comprobante-fiscal.md#la-factura-no-se-borra-nota-de-crédito-y-nota-de-débito` [L].

### Inferencias propias (marcadas así en la nota)

- El caso es el hilo del recorrido: cada resolución crea un documento en otro dominio, y el recorrido termina solo cuando todos volvieron. Sale de `garantia-y-reparacion.md` (lectura de esa base sobre dos sistemas) y se extiende acá al recorrido.
- El tiempo de punta a punta del reclamo se mide de la apertura del caso al último documento de la resolución (nota de crédito emitida, reembolso pagado, reemplazo entregado o equipo reparado), no a la respuesta al cliente. Definición propia; ninguna fuente abierta la da.
- La nota de crédito sin recepción es la falla que el control de Romney y Steinbart impide: se emite contra la devolución recibida o con autorización.
- Tasa de reclamos que terminan en no conformidad y reclamos de factura como señal del recorrido del pedido al cobro: lectura propia.

## Recursos canónicos

- APQC PCF 7.4, 6.2.3, 6.2.4 y 6.3.2: el reclamo, la devolución y la garantía como tres procesos del mismo recorrido.
- ISO 10002:2018 (paga): los nueve pasos y la cláusula 8.

## Huecos

1. El mapa y las medidas Issue-to-Resolution de APQC (solo socios).
2. Valores de referencia del costo de la garantía: el buscador menciona cifras de APQC (cerca de 4 % de las ventas en los peores y 0,8 % en los mejores) en un artículo de SDCExec que dio 403; no se usaron.
3. Ninguna fuente neutral sobre reglas de reapertura ni sobre el reclamo de factura como tipo de caso.
4. El texto de los pasos 7.2 a 7.9 de ISO 10002 (pago).

## Borrador para la nota de Argentina

### Del reclamo a la resolución

- **La ley fija parte del recorrido.** La Ley 24.240 da garantía legal de seis meses en cosas nuevas y tres en usadas desde la entrega, hace responsables solidarios a toda la cadena, pide constancia de cada reparación, estira la garantía por el tiempo en el taller y deja al consumidor elegir entre cambio, devolución del precio o quita si la reparación no satisface: [el producto falla y está en garantía](../Servicio-al-cliente/servicio-al-cliente-en-argentina.md#el-producto-falla-y-está-en-garantía) y [la reparación](../Servicio-al-cliente/servicio-al-cliente-en-argentina.md#la-reparación-constancia-plazo-que-se-estira-y-lo-que-pasa-si-falla). Para el recorrido, el caso no puede cerrarse mandando al cliente al fabricante.
- **Arrepentimiento y baja.** La compra a distancia se revoca en 10 días, con el envío de vuelta a cargo del vendedor, y el código de trámite se da en 24 horas: [quiere darse de baja o arrepentirse](../Servicio-al-cliente/servicio-al-cliente-en-argentina.md#quiere-darse-de-baja-o-arrepentirse-de-la-compra) y [devoluciones](../Comercio-electronico/Operaciones-del-comercio/devoluciones.md#lo-que-obliga-la-ley-en-argentina).
- **Plazos de respuesta por sector y adónde va el cliente.** No hay plazo general; bancos, telecomunicaciones y servicios públicos tienen los suyos, y si la empresa no responde el cliente va a la Ventanilla Federal Única (en la Ciudad de Buenos Aires, también el libro de quejas): [cuánto se tarda en contestar un reclamo](../Servicio-al-cliente/servicio-al-cliente-en-argentina.md#cuánto-se-tarda-en-contestar-un-reclamo) y [adónde va el cliente](../Servicio-al-cliente/servicio-al-cliente-en-argentina.md#adónde-va-el-cliente-si-la-empresa-no-responde).
- **La resolución económica es una nota de crédito electrónica.** Lleva CAE como la factura y solo la emite quien emitió la factura original ([factura electrónica de ARCA](../Comercio-electronico/Normativa/factura-electronica-de-arca.md)); el IVA de la devolución se ajusta a la alícuota original ([IVA en Argentina](../Impuestos/Impuestos-al-consumo/iva-en-argentina.md#débito-crédito-y-descuentos)).
- **El reingreso al stock lleva remito.** La mercadería que vuelve viaja con remito como cualquier traslado: [inventario y depósitos en la Argentina](../Inventario-y-depositos/inventario-y-depositos-en-argentina.md#todo-traslado-lleva-remito-aunque-no-haya-venta).
