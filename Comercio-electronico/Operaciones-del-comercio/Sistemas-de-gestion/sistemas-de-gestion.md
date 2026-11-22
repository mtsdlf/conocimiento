---
resumen: >-
  Un sistema de gestión (ERP, en su versión grande) es el software que lleva el negocio detrás de la tienda: factura, stock, compras, cobranzas, caja y, en los más completos, la contabilidad, todo sobre un mismo registro. En una pyme argentina conviven con la plataforma de tiendas y el marketplace, y la decisión de fondo es cuál de todos manda en cada dato.
estado: borrador
estabilidad: estable
fuentes:
  - "Alegra Argentina, preguntas frecuentes sobre ERP y software de gestión: https://www.alegra.com/argentina/ (leída el 2026-11-22; definición de parte, vende software de gestión)"
  - "Axoft, sitio: https://www.axoft.com/ (leído el 2026-11-22)"
  - "Contabilium, sitio Argentina: https://www.contabilium.com/ar (leído el 2026-11-22)"
  - "Dux Software, sitio y precios: https://www.duxsoftware.com.ar/ y https://www.duxsoftware.com.ar/precios (leídos el 2026-11-22)"
  - "Develop Argentina, sistemas de gestión comercial Argentina 2026, 25/06/2026: https://www.developargentina.com/blog/sistemas-gestion-comercial-argentina-2026 (por extracto; el autor vende desarrollo a medida)"
  - "Comercio-electronico/.investigacion/sistemas-de-gestion.md"
  - "Comercio-electronico/.investigacion/resenas-de-sistemas-de-gestion.md"
  - "Comercio-electronico/.investigacion/contraria-gestion-y-local.md"
aliases: [ERP, sistema de gestión, software de gestión, sistema de gestión comercial, software de facturación y stock, enterprise resource planning, back office]
creado: 2026-11-22
revisado:
---

# Sistemas de gestión

Un sistema de gestión (ERP, en su versión grande) es el software que lleva el negocio detrás de la tienda: factura, stock, compras, cobranzas, caja y, en los más completos, la contabilidad, todo sobre un mismo registro. En una pyme argentina conviven con la plataforma de tiendas y el marketplace, y la decisión de fondo es cuál de todos manda en cada dato.

Es la pieza de [Operaciones del comercio](../operaciones-del-comercio.md) que guarda el [catálogo y el stock](../catalogo-y-stock.md) cuando el comercio vende por más de un canal. Se conecta con la [plataforma de tiendas](../../Plataforma-de-tiendas/plataforma-de-tiendas.md) y con los marketplaces como explica [integración con tiendas y marketplaces](integracion-con-tiendas-y-marketplaces.md), y emite el comprobante que pide la [factura electrónica de ARCA](../../Normativa/factura-electronica-de-arca.md).

## De qué está hecho

Los sistemas que se venden a comercios argentinos declaran, con nombres distintos, los mismos módulos:

| Módulo | Qué lleva |
|---|---|
| Ventas y facturación | presupuestos, pedidos, facturas y notas de crédito, con el comprobante electrónico |
| Stock | productos, listas de precios, depósitos y movimientos |
| Compras | proveedores, órdenes y facturas de compra |
| Cuentas corrientes y cobranzas | lo que debe cada cliente y lo que se le debe a cada proveedor |
| Tesorería | cajas, bancos, cheques y arqueos |
| Contabilidad | asientos, balances y libros de IVA, en los planes altos o en sistemas que nacieron contables |
| Punto de venta | la venta del mostrador; ver [punto de venta](../../Venta-en-varios-canales/Local-fisico-con-caja/punto-de-venta.md) |
| Integraciones | tiendas online, marketplaces y cobros |

Lo que lo distingue de una plataforma de tiendas es que mira hacia adentro. La tienda vende al público; el sistema de gestión registra lo que se compró, lo que se debe y lo que se facturó, venga la venta de donde venga.

## Facturador, contable, gestión y ERP

El mercado usa cuatro etiquetas que se superponen:

1. **Facturador**: emite comprobantes electrónicos y, a lo sumo, lleva clientes y un stock simple.
2. **Sistema contable**: nace para el contador y el estudio; factura y lleva bancos y libros.
3. **Sistema de gestión comercial**: factura, stock, compras, cuentas corrientes y caja, con POS e integraciones.
4. **ERP**: todo lo anterior más producción, recursos humanos y varias empresas; se implementa con un consultor.

Un fabricante que vende la tercera define al ERP como lo que «abarca todos los aspectos operativos» y es más complejo y costoso, y al software de gestión como lo que «se centra en áreas específicas» y escala con más facilidad. Es una definición de parte. Los productos reales cruzan las etiquetas: hay contables que suman stock, facturadores que suman cobranzas y sistemas de gestión con POS y conector a tiendas incluidos.

En la lectura de la base, la etiqueta importa menos que la fuente de verdad de cada sistema: los comprobantes, el stock, la contabilidad o la cobranza. Dos sistemas que creen ser dueños del stock producen la sobreventa que describe [catálogo y stock](../catalogo-y-stock.md).

## Instalado o en la nube

Hay sistemas que se instalan en una computadora o un servidor del comercio y se venden por licencia, por módulo y por puesto, a través de una red de distribuidores; el caso argentino más conocido funciona así, según un resumen del buscador. Los que corren en la nube se pagan por mes. En los que se relevaron, el precio escala por comprobantes por mes y usuarios, y además por cuentas de canal conectadas (tiendas y marketplaces) en los que traen integraciones, o por depósitos en otros. Los precios de cada uno están en [sistemas de gestión en Argentina](sistemas-de-gestion-en-argentina.md).

## Cómo se elige y cómo falla

La única fuente leída sobre fallas de implementación es de un autor que vende desarrollo a medida: nombra como errores comunes elegir solo por precio, decidir solo con el criterio del contador y subestimar la migración de datos. Un fabricante reconoce el tercer riesgo en su página de precios: avisa que al migrar «no se pueden cargar datos históricos como ventas o cuentas corrientes», solo clientes, proveedores, productos, precios y stock.

Las reseñas de los usuarios agregan dónde duele después de elegir; están codificadas en [sistemas de gestión en Argentina](sistemas-de-gestion-en-argentina.md#lo-que-dicen-las-reseñas).

> [!NOTE] Sin fuente todavía: una definición canónica de ERP y estudios independientes sobre cómo fallan las implementaciones en pymes. El candidato es el capítulo de sistemas empresariales de Laudon y Laudon, *Management Information Systems*, que no se leyó: fijarse en el proceso de punta a punta y en los costos de cambio.

## Lo que hay adentro de Sistemas de gestión

- [Integración con tiendas y marketplaces](integracion-con-tiendas-y-marketplaces.md): cómo se conecta con la tienda y con el marketplace, quién manda en el stock y por qué se rompe.
- [Sistemas de gestión en Argentina](sistemas-de-gestion-en-argentina.md): los que operan en el país, con precios, integraciones, clientes declarados y reseñas, al 2026-11-22.
