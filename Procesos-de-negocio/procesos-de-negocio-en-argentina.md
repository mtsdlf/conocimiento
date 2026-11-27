---
resumen: >-
  Dónde la Argentina le agrega pasos o controles a cada recorrido de punta a punta: la factura electrónica con CAE, las percepciones al facturar y las retenciones al cobrar y al pagar, el cierre mensual que corre detrás de los vencimientos, el alta laboral antes del primer día y la garantía legal en los reclamos. El detalle de cada regla vive en los temas de dominio; acá va en qué paso cae.
estado: vigente
estabilidad: volatil
fuentes:
  - "Impuestos/Recaudacion-en-la-fuente/retenciones-y-percepciones-en-argentina.md"
  - "Impuestos/Impuestos-al-consumo/iva-en-argentina.md"
  - "Impuestos/impuestos-en-argentina.md"
  - "Comercio-electronico/Normativa/factura-electronica-de-arca.md"
  - "Comercio-electronico/Comercio-B2B/factura-entre-empresas.md"
  - "Compras-y-abastecimiento/compras-y-abastecimiento-en-argentina.md"
  - "Tesoreria/tesoreria-en-argentina.md"
  - "Administracion-de-personal-y-nomina/Liquidacion-de-sueldos/liquidacion-en-argentina.md"
  - "Servicio-al-cliente/servicio-al-cliente-en-argentina.md"
  - "Servicios-profesionales-y-proyectos/servicios-profesionales-en-argentina.md"
  - "Procesos-de-negocio/.investigacion/ (borradores de Argentina de cada informe, 2026-11-27)"
aliases: [procesos de negocio en Argentina, recorridos en Argentina, order-to-cash Argentina, procure-to-pay Argentina, factura electrónica en el recorrido, retenciones en el recorrido]
creado: 2026-11-27
revisado: 2026-11-27
---

# Procesos de negocio en la Argentina

Dónde la Argentina le agrega pasos o controles a cada recorrido de punta a punta: la factura electrónica con CAE, las percepciones al facturar y las retenciones al cobrar y al pagar, el cierre mensual que corre detrás de los vencimientos, el alta laboral antes del primer día y la garantía legal en los reclamos. El detalle de cada regla vive en los temas de dominio; acá va en qué paso cae.

Las reglas cambian seguido (la nota es `volatil`): lo que dice cada apartado vale a la fecha de las notas que enlaza, y esas notas tienen las normas con su número. Los recorridos son los del [tema](procesos-de-negocio.md); el orden de los pasos no cambia, cambia lo que se controla en algunos traspasos.

## Del pedido al cobro

- **El pedido no es factura.** La nota de pedido lleva la leyenda de documento no válido como factura ([la leyenda de lo que no es factura](../Relacion-con-clientes/relacion-con-clientes-en-argentina.md#la-leyenda-de-lo-que-no-es-factura)).
- **El despacho lleva remito.** Todo traslado de mercadería viaja con remito, que puede ser digital; en la provincia de Buenos Aires y las jurisdicciones adheridas, un traslado por tierra que supera cierto valor o peso pide además el COT ([el remito](../Cadena-de-suministro-y-logistica/Despacho-y-entrega/despacho.md#en-la-argentina-el-remito), [inventario y depósitos en la Argentina](../Inventario-y-depositos/inventario-y-depositos-en-argentina.md)).
- **La factura necesita CAE.** La factura electrónica se emite con el código de autorización que ARCA da por comprobante, y la letra depende de quién vende y quién compra ([factura electrónica de ARCA](../Comercio-electronico/Normativa/factura-electronica-de-arca.md)). La nota de crédito la emite quien emitió la factura y se relaciona con ella.
- **Al facturar se percibe; al cobrar se sufren retenciones.** Un vendedor que es agente de percepción suma IVA a la factura; las percepciones de Ingresos Brutos dependen de cada provincia y la base todavía no las tiene leídas ([percepciones](../Comercio-electronico/Comercio-B2B/factura-entre-empresas.md#percepciones-el-impuesto-que-el-mayorista-cobra-por-adelantado)). Un cliente que es agente de retención paga neto y entrega un certificado, que se aplica junto con la plata ([las retenciones sufridas](../Tesoreria/Credito-y-cobranzas/aplicacion-de-cobros.md#las-retenciones-sufridas)). Los regímenes, con el SIRCREB y el SIRTAC sobre las acreditaciones bancarias, están en [retenciones y percepciones en Argentina](../Impuestos/Recaudacion-en-la-fuente/retenciones-y-percepciones-en-argentina.md).
- **El cobro llega en cheque o ECHEQ.** Las reglas del ECHEQ (acreditación, aceptación, endosos) están en [lo que cambia con el ECHEQ](../Tesoreria/tesoreria-en-argentina.md#lo-que-cambia-con-el-echeq). Si el cheque a fecha cancela la factura al recibirse o al acreditarse es una decisión de diseño que la base todavía no tiene con fuente.
- **Entre una pyme y una empresa grande, la factura de crédito electrónica.** Por encima de un monto, el comprador la acepta o la rechaza en un plazo y la pyme la puede negociar ([la Factura de Crédito Electrónica MiPyME](../Comercio-electronico/Comercio-B2B/factura-entre-empresas.md#la-factura-de-crédito-electrónica-mipyme)).

## De la compra al pago

- **Al llegar la factura del proveedor** se constata el CAE antes del cruce de tres vías, y se miran la letra y la leyenda del comprobante ([qué se controla cuando llega la factura](../Compras-y-abastecimiento/compras-y-abastecimiento-en-argentina.md#qué-se-controla-cuando-llega-la-factura); la letra y la leyenda, en [qué factura tiene que mandar el proveedor](../Compras-y-abastecimiento/compras-y-abastecimiento-en-argentina.md#qué-factura-tiene-que-mandar-el-proveedor)). El crédito fiscal que deja la factura está en [IVA en Argentina](../Impuestos/Impuestos-al-consumo/iva-en-argentina.md).
- **Si la factura es de crédito electrónica**, el cruce tiene que terminar antes del plazo de aceptación, porque rechazarla por diferencias pide tener la recepción registrada; si no, queda aceptada sola ([la FCE MiPyME del lado del que compra](../Compras-y-abastecimiento/compras-y-abastecimiento-en-argentina.md#la-factura-de-crédito-electrónica-mipyme-del-lado-del-que-compra)).
- **Al pagar**, quien es agente retiene IVA, Ganancias e Ingresos Brutos y entrega el certificado; el proveedor con certificado de exclusión no sufre la retención ([retenciones y percepciones en Argentina](../Impuestos/Recaudacion-en-la-fuente/retenciones-y-percepciones-en-argentina.md), [agente de recaudación](../Impuestos/Recaudacion-en-la-fuente/agente-de-recaudacion.md)). En la [corrida de pagos](../Tesoreria/Pagos-a-proveedores/corrida-de-pagos.md), las retenciones que se descuentan del pago van en un campo aparte, cada una a su cuenta.
- **El medio de pago** puede estar condicionado por la factura: la leyenda «PAGO EN CBU INFORMADA» obliga a pagar a esa cuenta ([qué factura tiene que mandar el proveedor](../Compras-y-abastecimiento/compras-y-abastecimiento-en-argentina.md#qué-factura-tiene-que-mandar-el-proveedor)). Lo que se importa paga tributos y percepciones en la aduana ([comercio exterior en Argentina](../Impuestos/comercio-exterior-en-argentina.md)).

## Del registro al balance

- **El cierre mensual corre detrás de los vencimientos.** El responsable inscripto declara el IVA cada mes con IVA Simple, y el exento sigue presentando el Libro de IVA Digital ([IVA Simple y el Libro de IVA Digital](../Impuestos/Impuestos-al-consumo/iva-en-argentina.md#iva-simple-y-el-libro-de-iva-digital)); Ingresos Brutos tiene calendario provincial y, en Convenio Multilateral, se declara por SIFERE ([Ingresos Brutos](../Impuestos/Impuestos-al-consumo/ingresos-brutos.md#sifere-y-padrón-federal)); el F.931 de sueldos vence el mes siguiente ([la declaración mensual](../Administracion-de-personal-y-nomina/Cargas-y-declaraciones/cargas-sociales-en-argentina.md#la-declaración-mensual)). La agenda entera está en [el calendario de vencimientos](../Impuestos/impuestos-en-argentina.md#el-calendario-de-vencimientos).
- **El libro de IVA se concilia con el mayor antes de declarar**, para que el impuesto y el balance digan lo mismo ([registros fiscales](../Impuestos/Cumplimiento/registros-fiscales.md#cómo-se-relaciona-con-la-contabilidad)). Los libros que pide la ley están en [libros contables en Argentina](../Contabilidad/Registro/libros-contables-en-argentina.md).
- **Los estados anuales se reexpresan por inflación** y siguen las normas de la FACPCE, o las NIIF si la empresa cotiza ([el ajuste por inflación](../Contabilidad/Estados-contables/normas-contables-en-argentina.md#el-ajuste-por-inflación)). El cierre anual alimenta la [declaración jurada de Ganancias](../Impuestos/Impuestos-a-la-renta/ganancias-en-argentina.md#la-declaración-jurada-anual), con su propio [ajuste por inflación impositivo](../Impuestos/Impuestos-a-la-renta/ganancias-en-argentina.md#ajuste-por-inflación-impositivo).

## De la planificación a la producción

El recorrido no tiene un paso propio de la Argentina. Las habilitaciones sanitarias de la planta (alimentos, medicamentos, productos médicos y cosméticos), el registro por producto y la trazabilidad (alimentos, medicamentos y algunos productos médicos) son requisitos de la planta y del producto, y están en [Producción en la Argentina](../Produccion/produccion-en-argentina.md). La compra de materiales sigue el apartado de la compra al pago.

## De la contratación a la baja

- **El alta va antes del primer día.** La registración ante ARCA se comunica hasta el día anterior al inicio, o hasta el comienzo mismo en las actividades del Anexo I de la RG 2988 ([lo que deja hecho el alta](../Administracion-de-personal-y-nomina/Legajo/ingreso-y-egreso.md#lo-que-deja-hecho-el-alta), [la registración ante ARCA](../Administracion-de-personal-y-nomina/Legajo/relacion-laboral-en-argentina.md#la-registración-ante-arca)).
- **Cada liquidación termina en el F.931**, que ARCA recalcula y rechaza si no coincide ([la declaración mensual](../Administracion-de-personal-y-nomina/Cargas-y-declaraciones/cargas-sociales-en-argentina.md#la-declaración-mensual)). Lo que cambió con la Ley 27.802 en el libro de sueldos está en [libro de sueldos digital](../Administracion-de-personal-y-nomina/Cargas-y-declaraciones/libro-de-sueldos-digital.md#lo-que-cambió-con-la-ley-27802).
- **El empleador retiene Ganancias** con lo que el empleado informa, y hace la liquidación anual y la final ([Ganancias sobre sueldos en la Argentina](../Administracion-de-personal-y-nomina/Cargas-y-declaraciones/ganancias-sobre-sueldos-en-argentina.md)).
- **El sueldo se paga por acreditación en cuenta sueldo**, dentro del plazo legal ([cuenta sueldo y plazo de pago](../Administracion-de-personal-y-nomina/Liquidacion-de-sueldos/liquidacion-en-argentina.md#cuenta-sueldo-y-plazo-de-pago)).
- **La baja cierra con la liquidación final y el certificado de trabajo**, cada uno con sus rubros y plazos ([la liquidación final en la Argentina](../Administracion-de-personal-y-nomina/Liquidacion-de-sueldos/liquidacion-en-argentina.md#la-liquidación-final-en-la-argentina), [el certificado de trabajo del art. 80](../Administracion-de-personal-y-nomina/Legajo/relacion-laboral-en-argentina.md#el-certificado-de-trabajo-del-art-80)).

## Del reclamo a la resolución

- **La ley fija parte del recorrido.** La garantía legal hace responsable a toda la cadena, pide constancia de cada reparación y deja al consumidor elegir si la reparación no lo satisface; el caso no se cierra mandando al cliente al fabricante ([el producto falla y está en garantía](../Servicio-al-cliente/servicio-al-cliente-en-argentina.md#el-producto-falla-y-está-en-garantía), [la reparación](../Servicio-al-cliente/servicio-al-cliente-en-argentina.md#la-reparación-constancia-plazo-que-se-estira-y-lo-que-pasa-si-falla)).
- **El arrepentimiento y la baja** tienen plazo y código de trámite ([quiere darse de baja o arrepentirse](../Servicio-al-cliente/servicio-al-cliente-en-argentina.md#quiere-darse-de-baja-o-arrepentirse-de-la-compra), [devoluciones](../Comercio-electronico/Operaciones-del-comercio/devoluciones.md#lo-que-obliga-la-ley-en-argentina)).
- **No hay plazo general de respuesta**, pero bancos, telecomunicaciones y servicios públicos tienen los suyos, y el cliente sin respuesta va a la Ventanilla Federal Única ([cuánto se tarda en contestar un reclamo](../Servicio-al-cliente/servicio-al-cliente-en-argentina.md#cuánto-se-tarda-en-contestar-un-reclamo), [adónde va el cliente](../Servicio-al-cliente/servicio-al-cliente-en-argentina.md#adónde-va-el-cliente-si-la-empresa-no-responde)).
- **La resolución económica es una nota de crédito electrónica**, que emite quien emitió la factura; el IVA se ajusta a la alícuota original ([débito, crédito y descuentos](../Impuestos/Impuestos-al-consumo/iva-en-argentina.md#débito-crédito-y-descuentos)). La mercadería que vuelve viaja con remito ([todo traslado lleva remito](../Inventario-y-depositos/inventario-y-depositos-en-argentina.md#todo-traslado-lleva-remito-aunque-no-haya-venta)).

## Del proyecto al cobro

- **La factura del servicio lleva el período y el vencimiento**, así que el proyecto tiene que poder dar el período de cada factura ([la factura de un servicio](../Servicios-profesionales-y-proyectos/servicios-profesionales-en-argentina.md#la-factura-de-un-servicio-lleva-el-período-y-el-vencimiento)).
- **Cobrar un anticipo obliga a facturarlo**, aunque el ingreso se reconozca después ([cuándo nace la obligación de facturar](../Servicios-profesionales-y-proyectos/servicios-profesionales-en-argentina.md#cuándo-nace-la-obligación-de-facturar), [trabajo en curso](../Servicios-profesionales-y-proyectos/Facturacion-del-proyecto/trabajo-en-curso.md)).
- **El cobro llega neto de retenciones** de Ganancias e Ingresos Brutos, y la factura se cancela con la plata más el certificado ([las retenciones sufridas](../Tesoreria/Credito-y-cobranzas/aplicacion-de-cobros.md#las-retenciones-sufridas)).
- **El precio de un proyecto largo no se indexa en pesos**; los caminos que deja la ley están en [ajustar el precio en un proyecto largo](../Servicios-profesionales-y-proyectos/servicios-profesionales-en-argentina.md#ajustar-el-precio-en-un-proyecto-largo).

## De la compra a la baja del activo

- **Se llevan dos amortizaciones por bien.** La impositiva y la contable difieren, y la diferencia se revierte sola ([diferencias permanentes y temporarias](../Impuestos/Impuestos-a-la-renta/resultado-impositivo.md#diferencias-permanentes-y-temporarias)); el régimen de amortización acelerada para pymes está en [reformas recientes](../Impuestos/Impuestos-a-la-renta/ganancias-en-argentina.md#reformas-recientes).
- **Cada alta guarda su fecha de origen**, porque los bienes de uso se reexpresan por inflación desde ese mes (inferencia de la base sobre cómo funciona el índice; [el ajuste por inflación](../Contabilidad/Estados-contables/normas-contables-en-argentina.md#el-ajuste-por-inflación)).
- **La importación de bienes de uso** tiene su tratamiento en [percepciones al importar](../Impuestos/comercio-exterior-en-argentina.md#percepciones-al-importar), y las inspecciones que exige la norma, en [mantenimiento obligatorio en la Argentina](../Activos-y-mantenimiento/mantenimiento-obligatorio-en-argentina.md).

> [!NOTE] Sin fuente todavía: las vidas útiles impositivas de los bienes de uso, el tratamiento en Ganancias de la venta o el reemplazo de un bien de uso, y el IVA de esa venta. Ninguna nota de Impuestos los trata.
