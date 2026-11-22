---
resumen: >-
  Un punto de venta (POS) es el software del mostrador que registra cada venta, lleva la caja y descuenta el stock. No es el lector que cobra la tarjeta ni el sistema de gestión que lleva compras y contabilidad, aunque muchos productos juntan dos o tres de esas piezas.
estado: borrador
estabilidad: estable
fuentes:
  - "Tiendanube, ayuda Argentina, Qué es Punto de venta: https://ayuda.tiendanube.com/es_AR/pdv/que-es-punto-de-venta-de-tiendanube (consultada el 2026-11-22, por extracto)"
  - "Tiendanube, ayuda Argentina, Cómo comenzar a usar Punto de venta: https://ayuda.tiendanube.com/es_AR/pdv/como-comenzar-a-usar-punto-de-venta-en-mi-tiendanube (consultada el 2026-11-22, por extracto)"
  - "Mercado Pago, developers, Point, visión general: https://www.mercadopago.com.ar/developers/es/docs/mp-point/overview (consultada el 2026-11-22, por extracto)"
  - "Mercado Pago, developers, integración de Point con un punto de venta (API anterior): https://www.mercadopago.com.ar/developers/es/docs/mp-point-legacy/integration-configuration/integrate-with-pdv/introduction (consultada el 2026-11-22)"
  - "Fudo, sitio: https://fu.do (consultado el 2026-11-22, por extracto)"
  - "Comercio-electronico/.investigacion/local-fisico-con-caja.md"
  - "Comercio-electronico/.investigacion/contraria-gestion-y-local.md"
aliases: [POS, punto de venta, point of sale, PDV, caja registradora, software de caja, sistema de caja]
creado: 2026-11-22
revisado:
---

# Punto de venta

Un punto de venta (POS) es el software del mostrador que registra cada venta, lleva la caja y descuenta el stock. No es el lector que cobra la tarjeta ni el sistema de gestión que lleva compras y contabilidad, aunque muchos productos juntan dos o tres de esas piezas.

Es la pieza central del [local físico con caja](local-fisico-con-caja.md). Descuenta del mismo [stock](../../Operaciones-del-comercio/catalogo-y-stock.md) que la tienda online, y lo que la venta del mostrador necesita del cobro y del comprobante se lo pide a otras piezas.

## Lo que hace en el mostrador

Un POS de comercio chico cubre, en la descripción de la ayuda de una plataforma de tiendas argentina:

1. Buscar el producto en el catálogo y ver su stock.
2. Buscar o crear al cliente.
3. Aplicar descuentos, en monto fijo o en porcentaje.
4. Agregar envío y notas, si la venta sale del local.
5. Registrar el cobro y dejar la venta en la misma lista que las de la tienda online.

La versión más completa de ese producto suma la gestión de caja (apertura, cierre y arqueo), permisos por usuario, lector de códigos de barras e impresora de tiques. La misma ayuda lo presenta para vender también por WhatsApp, por teléfono o por redes.

## En qué se diferencia del lector de cobro

El lector cobra y el POS registra. El lector (una terminal de tarjetas o un QR) procesa el pago y liquida el dinero, con su comisión, como explica [Pagos](../../Pagos/pagos.md). El POS anota que la venta se cobró y con qué medio.

Las dos piezas pueden estar conectadas o no:

- **Sin conexión**: el empleado cobra en el lector y después carga en el POS el medio, y si quiere el número de comprobante, las cuotas y el banco. Es como funciona el POS de la plataforma de tiendas más usada en Argentina con una terminal externa, según su ayuda.
- **Con conexión**: el POS crea la orden de pago, el lector la muestra, el comprador paga y el POS recibe el aviso. Así describe Mercado Pago la integración de sus lectores con un punto de venta propio, por API, con los modelos Point Smart 1 y 2. La documentación avisa que una API nueva va a reemplazar a la anterior, sin fecha.

Con conexión desaparece la doble carga y el cierre de caja cuadra solo. Lo que ninguna de las dos fuentes resuelve es el comprobante fiscal: Mercado Pago no emite la factura de ARCA, y quien la emite es otro sistema (ver [factura electrónica de ARCA](../../Normativa/factura-electronica-de-arca.md)).

## En qué se diferencia del sistema de gestión

Un POS vende y cobra; un [sistema de gestión](../../Operaciones-del-comercio/Sistemas-de-gestion/sistemas-de-gestion.md) lleva además compras, proveedores, cuentas corrientes, varios depósitos y, en los más completos, la contabilidad. En la práctica las fronteras se cruzan. Los sistemas de gestión argentinos traen su propio POS, y hay POS de rubro (gastronomía, por ejemplo) que suman caja, terminal de pago integrada, factura y tienda online en un solo producto.

Por eso la pregunta útil al mirar un producto no es qué etiqueta tiene, sino cuál de estas cuatro cosas guarda como verdad: la venta, el cobro, el comprobante o el stock.

> [!NOTE] Sin fuente todavía: una definición de POS en un manual de retail (por ejemplo, el capítulo de sistemas de tienda de *Retailing Management*, de Levy y Weitz). Lo de arriba sale de la documentación de proveedores.

Los productos concretos, con sus precios al 2026-11-22, están en [puntos de venta en Argentina](puntos-de-venta-en-argentina.md).
