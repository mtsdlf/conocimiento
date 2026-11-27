---
resumen: >-
  El mercado argentino de software de gestión tiene tres rasgos propios: la localización fiscal es requisito para vender, los sistemas instalados se venden por licencia a través de distribuidores o centros de servicio y los de nube cobran por mes según comprobantes, usuarios y canales. No hay dato público del tamaño de este mercado; las cifras que circulan son de todo el sector de software.
estado: borrador
estabilidad: volatil
fuentes:
  - "Software-de-gestion/.investigacion/mercado-y-economia.md, sección 7 (2026-11-27; todo por resumen del buscador)"
  - "CESSI, Observatorio OPSSI, informe 2024 (por prensa; el PDF no se abrió): https://cessi.org.ar/ y Memoria 2025: https://cessi.org.ar/wp-content/uploads/2025/10/Memoria-2025.pdf"
  - "ITSitio, El software argentino bate récords (por resumen): https://www.itsitio.com/ar/software/software-argentino-bate-records/"
  - "Ámbito, 29/07/2026, exportaciones récord y caída del empleo (por resumen): https://www.ambito.com/tecnologia/la-industria-del-software-argentino-vuelve-tener-exportaciones-record-pero-el-empleo-cae-primera-vez-seis-anos-n6304732"
  - "UADE, exportaciones de software en la República Argentina (por resumen): https://www.uade.edu.ar/media/iy2ohbz0/exportaciones-de-software-en-la-repu-blica-argentina.pdf"
  - "Formulario de un proveedor local ante el Consejo Profesional de Ciencias Económicas (por resumen): https://www.consejo.org.ar/storage/attachments/FORMULARIO AXOFT.pdf-IjbL7u00lN.pdf"
  - "ITSitio, Un tango entre la tierra y la nube, fecha sin confirmar (por resumen): https://www.itsitio.com/?p=2899"
  - "Documentación de la localización argentina de un ERP de código abierto (por resumen): https://www.odoo.com/es/app/localization-argentina"
  - "FACPCE, guía de aplicación del ajuste por inflación (RT 6 y NIC 29), primera parte (por resumen): https://www.facpce.org.ar/web2014/pdf/Guia de aplicación de las normas contables sobre ajuste por inflación (RT 6 y NIC 29) - Primera parte.pdf"
aliases: [mercado argentino de software de gestión, mercado de ERP en Argentina, ERP argentino, localización argentina, centros de servicio, distribuidores de software de gestión]
creado: 2026-11-27
revisado:
---

# Mercado en la Argentina

El mercado argentino de software de gestión tiene tres rasgos propios: la localización fiscal es requisito para vender, los sistemas instalados se venden por licencia a través de distribuidores o centros de servicio y los de nube cobran por mes según comprobantes, usuarios y canales. No hay dato público del tamaño de este mercado; las cifras que circulan son de todo el sector de software.

Es el caso local de lo que cuenta [Mercado y economía](mercado-y-economia.md). Los sistemas concretos, con sus precios, sus límites por plan, cuántos clientes declaran y lo que dicen sus reseñas, están en la ficha de [sistemas de gestión en Argentina](../../Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion/sistemas-de-gestion-en-argentina.md), escrita desde el comercio.

> [!WARNING]
> Todo lo de esta nota se leyó por el resumen de un buscador o por la prensa; ninguna fuente se abrió entera. Las cifras son candidatas hasta que alguien lea el informe original.

## La localización fiscal como requisito

Un sistema que no emite el comprobante electrónico ante ARCA no se puede usar para facturar en la Argentina. Lo que la norma le exige (web services, CAE y CAEA, controlador fiscal, libros digitales, padrones) está en [software de gestión en la Argentina](../software-de-gestion-en-argentina.md), y las reglas impositivas, en [Impuestos](../../Impuestos/impuestos-en-argentina.md).

La documentación de la localización argentina de un ERP de código abierto muestra qué tiene que traer un producto, según su resumen: factura electrónica ante ARCA con certificado y firma, los tipos de comprobante (A, N y la factura de crédito electrónica MiPyME), un plan de cuentas según la responsabilidad fiscal y los libros de IVA de ventas y compras. A eso se suma el ajuste por inflación: la guía de la FACPCE describe un método de reexpresión secuencial y el consejo profesional publica índices periódicos, así que el sistema tiene que reexpresar y cargar coeficientes ([el ajuste por inflación](../../Contabilidad/Estados-contables/normas-contables-en-argentina.md#el-ajuste-por-inflación)).

En lectura de esta base, la localización es además una barrera de entrada para un proveedor de afuera: tiene que construirla o comprarla, y mantenerla al día con normas que cambian varias veces por año. Ninguna fuente encontrada la mide ni compara la participación de proveedores locales y extranjeros. Cómo pesa como vía de entrada para un producto nuevo está en [dónde entra un software nuevo](donde-entra-un-software-nuevo.md).

## Distribuidores y centros de servicio

Los sistemas instalados se venden muchas veces a través de una red de distribuidores, que en el mercado local se llaman centros de servicio o agentes. Es la forma local del [canal de partners](canal-de-partners.md): el distribuidor vende la licencia, la instala, capacita y da soporte.

La única cifra de escala es lo que declara un proveedor local de larga trayectoria sobre sí mismo: más de 200 distribuidores y agentes en el país y más de 200.000 pymes que usaron su sistema, según un formulario presentado ante el consejo profesional. Un artículo de prensa más viejo daba unos 70.000 clientes históricos y 13.000 que actualizaban cada año. Las dos cifras difieren en un orden de magnitud y ninguna dice qué cuenta: no sirven para medir el canal.

> [!NOTE] Sin fuente todavía: cuántos distribuidores hay en total, qué parte de la licencia y del servicio se queda el distribuidor y qué margen tiene.

## Instalado o en la nube

Conviven dos modelos de cobro. Los sistemas instalados en la computadora o el servidor del cliente se venden por licencia, por módulos y por puestos. Los de nube se pagan por mes y escalan el precio por tres cosas: comprobantes por mes, usuarios y cuentas de canal conectadas, como tiendas y marketplaces ([instalado o en la nube](../../Comercio-electronico/Operaciones-del-comercio/Sistemas-de-gestion/sistemas-de-gestion.md#instalado-o-en-la-nube)). La diferencia general entre los dos modelos está en [licencia y suscripción](licencia-y-suscripcion.md) y en [SaaS](../../Emprender/Modelo-de-negocio/saas.md).

El precio por comprobante es lo que distingue al mercado local, en lectura de esta base: ata lo que paga el cliente a cuánto factura, y el comprobante es la pieza que la norma obliga a emitir por sistema. Los planes de la ficha ponen el corte en cantidades como 250, 1.500 o 5.000 comprobantes por mes.

> [!NOTE] Sin fuente todavía: qué parte del mercado está en la nube y qué parte instalada, y cuántas empresas migraron de un modelo al otro.

## El tamaño del sector de software, que no es el de ERP

Las cifras públicas son de todo el sector de software y servicios informáticos, no del software de gestión. Según la prensa que cita el observatorio de la CESSI, el sector facturó USD 22.221 millones en 2024, un 13,1 % más, con 158.179 puestos de trabajo. Un informe universitario da exportaciones por USD 2.810 millones en 2024.

Las fuentes no coinciden en el empleo: una nota de julio de 2026 da 162.391 empleados y habla de la primera caída en seis años. No se resolvió qué período mide cada cifra.

> [!NOTE] Sin fuente todavía: el tamaño del mercado local de software de gestión o de ERP, su reparto entre proveedores y su reparto entre nube e instalado. No se encontró ningún dato público.
