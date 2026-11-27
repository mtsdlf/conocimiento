---
resumen: >-
  La migración de datos es la parte de la implementación que pasa al sistema nuevo lo que la empresa necesita para seguir operando: los datos maestros, los saldos de apertura, los documentos abiertos y, si se decide, la historia. Se limpia antes, se ensaya varias veces y se da por buena solo cuando los saldos del sistema nuevo concilian con los del viejo.
estado: vigente
estabilidad: semi
fuentes:
  - "Documentación de un ERP de código abierto, Opening balance (leída): https://docs.frappe.io/erpnext/user/manual/en/opening-balance"
  - "Guía de implementación de un proveedor grande, estrategia de corte, ms.date 2024-01-30 (leída): https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/prepare-go-live-cutover-strategy"
  - "Wipro, The ERP data migration conundrum (según resumen; consultora): https://www.wipro.com/analytics/latest-thinking/solving-the-erp-data-migration-puzzle/"
  - "Panorama Consulting Solutions, 2017 Report on ERP Systems & Enterprise Software (leído): https://www.panorama-consulting.com/wp-content/uploads/2017/07/2017-ERP-Report.pdf"
  - "Software-de-gestion/.investigacion/implementacion.md"
aliases: [migración de datos, data migration, conversión de datos, data conversion, carga inicial, saldos de apertura, opening balances, ensayo de migración, mock migration, datos históricos]
creado: 2026-11-27
revisado: 2026-11-27
---

# Migración de datos

La migración de datos es la parte de la implementación que pasa al sistema nuevo lo que la empresa necesita para seguir operando: los datos maestros, los saldos de apertura, los documentos abiertos y, si se decide, la historia. Se limpia antes, se ensaya varias veces y se da por buena solo cuando los saldos del sistema nuevo concilian con los del viejo.

Es una actividad del proyecto de [implementación](implementacion.md), con su plan, sus responsables y su fecha. El mecanismo de carga (formatos, importadores, el sistema que manda en cada dato, la diferencia con una integración que corre todos los días) es de [integración y migración](../Columnas-tecnicas/integracion-y-migracion.md), y la extracción y transformación en general, de [ETL y ELT](../../Datos/Ingesta-y-transformacion/etl-y-elt.md). La migración termina el día del corte, que se cuenta en [puesta en marcha](puesta-en-marcha.md).

En la encuesta de Panorama Consulting de 2017 (342 respuestas en su sitio, muestra autoseleccionada, consultora con interés comercial), los problemas de datos fueron la segunda causa de atraso, con 16 %, detrás del alcance ampliado.

> [!NOTE] Sin fuente todavía: un estudio con método sobre migración de datos en implantaciones de ERP. Lo que sigue sale de la documentación de productos y de consultoras.

## Qué se migra y qué se deja

No se migra todo. La decisión es qué necesita el sistema nuevo para operar desde el primer día y qué se puede consultar en el viejo. La documentación de un ERP de código abierto describe la carga de apertura, y la práctica de consultoras coincide, según un resumen, en que lo más común es cargar maestros con saldos abiertos.

| Qué | Cómo entra | Por qué así |
|---|---|---|
| Datos maestros | Clientes, proveedores, productos, cuentas, depurados y sin duplicados | Todo documento nuevo apunta a ellos ([datos maestros](../../Datos/Gobierno-y-calidad/datos-maestros.md)) |
| Saldos contables | Un balance de sumas y saldos aprobado a la fecha de corte, que tiene que balancear antes de cargarse | Es el punto de partida del mayor ([asiento y libros](../../Contabilidad/Registro/asiento-y-libros.md#el-balance-de-sumas-y-saldos)) |
| Saldos de clientes y proveedores | Como facturas abiertas, una por comprobante pendiente | Se van a cobrar o pagar de a una, y la [antigüedad de saldos](../../Contabilidad/Registro/cuentas-corrientes.md#la-antigüedad-de-saldos) se calcula por comprobante |
| Stock | Una conciliación de stock de tipo apertura, por producto y depósito | El costo de lo que se venda después sale de ahí |
| Documentos abiertos | Pedidos de venta y órdenes de compra sin cumplir | El trabajo en curso sigue al día siguiente del corte |
| Historia | Se deja en el sistema viejo o en un archivo de consulta, salvo decisión explícita | Cargarla cuesta más que consultarla |

De la tabla, la documentación de código abierto respalda los saldos contables, las facturas abiertas y el stock de apertura; el resto es lectura de esta base.

La documentación citada usa una cuenta transitoria de apertura: cada saldo entra contra ella, y al terminar la carga tiene que quedar en cero. Si no da cero, algo entró de más o de menos. Pide además los saldos de clientes y proveedores como facturas abiertas «where future settlement and ageing matter».

Dejar la historia afuera tiene un costo para quien consulta. En el comercio argentino, el fabricante de un sistema de gestión avisa que al migrar no se cargan datos históricos como ventas o cuentas corrientes, solo maestros y stock ([sistemas de gestión en el comercio](../../Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion/sistemas-de-gestion.md#cómo-se-elige-y-cómo-falla)). Un análisis de varios años que cruce el antes y el después del corte tiene que juntar dos fuentes, y eso es trabajo de [Visualización y BI](../../Datos/Visualizacion-y-BI/visualizacion-y-bi.md).

## Limpiar antes de cargar

El sistema nuevo hereda la [calidad de datos](../../Datos/Gobierno-y-calidad/calidad-de-datos.md) del viejo si nadie la mira. Según un resumen, las consultoras coinciden en perfilar el origen, deduplicar los maestros, mapear cada campo viejo a uno nuevo y conciliar con gente del negocio antes de la puesta en marcha. Son afirmaciones de práctica, sin método publicado.

En lectura de esta base, la migración es la ocasión de unir los registros duplicados en un registro de oro, porque después de la carga cada duplicado tiene documentos colgados y unirlo cuesta más. Cómo se encuentra a la misma persona en dos registros está en [datos maestros](../../Datos/Gobierno-y-calidad/datos-maestros.md#cómo-se-encuentra-a-la-misma-persona-en-dos-registros). La limpieza la hacen los usuarios clave que conocen el dato; el equipo técnico puede detectar el duplicado, pero no decidir cuál de los dos vale.

## Ensayar y conciliar

La migración se ensaya completa antes del corte real, con los mismos datos, herramientas y personas. La guía de implementación de un proveedor grande pide ensayos de corte («mock cutover») varias veces y pone entre las condiciones para el corte una estrategia de migración «ready and tested». Al final, se verifica que «your data is accurate and complete in production».

La comprobación es una [conciliación](../../Contabilidad/Control-interno/conciliaciones.md): dos registros del mismo saldo, el viejo y el nuevo, se comparan y cada diferencia se explica. En lectura de esta base, se concilian al menos estos totales:

1. Comprobá que el balance de sumas y saldos del sistema nuevo a la fecha de corte sea igual al aprobado en el viejo.
2. Comprobá que la suma de facturas abiertas de cada cliente y proveedor dé el saldo de su cuenta de control, como en [el auxiliar contra su cuenta de control](../../Contabilidad/Control-interno/conciliaciones.md#el-auxiliar-contra-su-cuenta-de-control).
3. Comprobá que el stock valorizado por depósito coincida con el del viejo y con la cuenta contable de mercaderías.
4. Comprobá que la cuenta transitoria de apertura quede en cero.
5. Contá los maestros por tipo en los dos sistemas y explicá cada diferencia (los que se unieron, los que se dieron de baja).

La conciliación la firma alguien del negocio, no quien hizo la carga. Es la misma lógica de [separación de funciones](../../Contabilidad/Control-interno/separacion-de-funciones.md) que hace valer cualquier conciliación.

## Cómo falla la migración

En lectura de esta base, la migración falla de cuatro maneras.

- Se deja para el final: la limpieza empieza tarde porque parece trabajo técnico.
- Se ensaya con una muestra: los errores aparecen con los datos raros, que una muestra no trae.
- Se carga la historia entera por las dudas: multiplica el trabajo de mapeo y trae al sistema nuevo los errores del viejo.
- Nadie del negocio firma: el equipo técnico da por buena una carga que cuadra en cantidad de filas y no en saldos.
