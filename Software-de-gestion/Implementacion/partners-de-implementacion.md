---
resumen: >-
  Un partner de implementación es la empresa que configura, migra y pone en marcha un software de gestión que no hizo; la implantación también la pueden hacer el proveedor del producto o la propia empresa. Quién implanta decide el contrato, quién carga el riesgo del desvío y cuánto conocimiento le queda a la empresa cuando el partner se va.
estado: borrador
estabilidad: semi
fuentes:
  - "Ko, Kirsch y King (2005), Antecedents of knowledge transfer from consultants to clients in enterprise system implementations, MIS Quarterly 29(1):59-86 (abstract): https://aisel.aisnet.org/misq/vol29/iss1/5"
  - "Guía de implementación de un proveedor grande, Success by Design (leída): https://learn.microsoft.com/en-us/dynamics365/guidance/implementation-guide/success-by-design"
  - "Panorama Consulting Solutions, 2017 Report on ERP Systems & Enterprise Software (leído): https://www.panorama-consulting.com/wp-content/uploads/2017/07/2017-ERP-Report.pdf"
  - "CACM, Managing risks in enterprise systems implementations, caso de una distribuidora de medicamentos (según resumen; la página dio 403): https://cacm.acm.org/research/managing-risks-in-enterprise-systems-implementations"
  - "GFOA, Which System is Truly Best? (según resumen): https://www.gfoa.org/materials/gfr-0826-erp"
  - "Software-de-gestion/.investigacion/implementacion.md"
aliases: [partner de implementación, implementation partner, integrador, system integrator, SI, consultora de implementación, implementador, socio de implementación, consultor funcional, transferencia de conocimiento, knowledge transfer]
creado: 2026-11-27
revisado:
---

# Partners de implementación

Un partner de implementación es la empresa que configura, migra y pone en marcha un software de gestión que no hizo; la implantación también la pueden hacer el proveedor del producto o la propia empresa. Quién implanta decide el contrato, quién carga el riesgo del desvío y cuánto conocimiento le queda a la empresa cuando el partner se va.

La decisión se toma junto con la elección del producto, en la primera fase de la [implementación](implementacion.md), y, en lectura de esta base, cuando el proveedor vende a través de partners, elegir el producto arrastra la elección de quien lo implanta. Por qué un proveedor vende por canal, qué margen deja y cómo se certifica a un partner es de [canal de partners](../Mercado-y-economia/canal-de-partners.md); esta nota mira la relación desde la empresa que compra.

## Quién puede implantar

| Quién | Qué sabe | Dónde flojea |
|---|---|---|
| El proveedor del producto | El producto por dentro y su hoja de ruta | Tiende a ver cada brecha como algo que su producto resuelve |
| Un partner o integrador | El producto en muchas empresas, a veces un rubro | Gana por hora o por proyecto, y conoce el negocio del cliente solo por lo que le cuentan |
| La propia empresa | Su negocio y sus procesos | Rara vez conoce el producto, y su gente sigue con el trabajo de todos los días |

La tabla es lectura de esta base. En la práctica se mezclan: el partner configura y migra, el proveedor resuelve lo que solo él puede tocar, y la empresa pone a los usuarios clave que deciden cada brecha y firman la migración. La guía de implementación de un proveedor grande se ofrece a «system integrators, independent software development companies, and customers» y reconoce un reparto de responsabilidades entre el proveedor, el partner y el cliente.

En la encuesta de Panorama Consulting de 2017, los motivos para contratar consultores fueron gestionar la implantación (27 %), la gestión del cambio (22 %) y una selección «sin sesgo» (19 %). La consultora vende esos tres servicios y la muestra es autoseleccionada: son visitantes de su sitio.

## El contrato de implantación

El contrato decide quién paga si la implantación lleva más de lo estimado. Los modelos son los de cualquier encargo de software, en [modelos de contrato y cobro](../../Desarrollo/Encargo/modelos-de-contrato-y-cobro.md): precio cerrado, tiempo y materiales, sus híbridos con tope y el abono para el soporte posterior.

En la encuesta de Panorama de 2017, las dos primeras causas de atraso fueron el alcance ampliado y los problemas de datos. En lectura de esta base, eso apunta a brechas que aparecen tarde y a datos peores de lo que se creía, y empuja a dos formas de contrato:

- Precio cerrado por fase: se cotiza primero un análisis de brechas y un relevamiento de datos, y recién con eso el resto. Así se cotiza [después de achicar la incertidumbre](../../Producto/Planificacion-y-entrega/proyecto-a-precio-cerrado.md#cotizar-después-de-achicar-la-incertidumbre).
- Tiempo y materiales con tope: la empresa carga el desvío hasta un límite y el partner por encima.

Un precio cerrado para toda la implantación, firmado antes del análisis de brechas, deja al partner dos salidas cuando el alcance crece: discutir cada brecha como cambio de alcance o recortar la calidad de lo que no se ve, como la limpieza de datos o la capacitación. El contrato tiene que decir además qué se entrega al final, con qué criterio se acepta y qué documentación queda ([traspaso](../../Desarrollo/Encargo/traspaso.md)).

> [!NOTE] Sin fuente todavía: estudios sobre contratos de implantación de ERP (precio cerrado frente a tiempo y materiales) y auditorías públicas de implantaciones que muestren cómo se repartió el riesgo. Lo de esta sección es lectura de esta base sobre las notas de encargo.

## El conocimiento que queda cuando el partner se va

La empresa contrata a un partner para implantar, pero necesita después operar y cambiar el sistema sin él. Ko, Kirsch y King (2005) estudiaron esa transferencia con pares de consultor y cliente de 96 proyectos de ERP. Según su abstract, los clientes esperan que los consultores les transfieran su conocimiento para mantener los sistemas «independent of the consultants», y la transferencia depende de factores de conocimiento, de motivación y de comunicación: 9 de sus 13 hipótesis se sostuvieron.

En lectura de esta base, el estudio muestra que la transferencia no ocurre sola, y se planifica con tres cosas: usuarios clave de la empresa que trabajan con el partner en la configuración y no solo la reciben, documentación de cada brecha y su resolución ([análisis de brechas](analisis-de-brechas.md)), y un criterio de aceptación que incluye que la empresa opere sin ayuda durante un período.

## Cómo sale mal la relación

En lectura de esta base, los intereses del partner y de la empresa no coinciden del todo: el partner gana más cuanto más trabajo hay, y la empresa no puede juzgar bien un trabajo que no sabe hacer.

- Un partner que no conoce el rubro configura el producto con los supuestos de su último cliente.
- Una empresa que delega todo se queda sin nadie que entienda el sistema cuando termina el contrato, y depende del partner para cada cambio.
- El litigio: según el resumen de un artículo de CACM, los síndicos de una distribuidora de medicamentos estadounidense que quebró en 1996 demandaron a la consultora y al proveedor de su ERP. Las cifras del caso discrepan entre fuentes y el artículo no se leyó.

En lectura de esta base, separar a quien elige el sistema de quien lo implanta reduce el conflicto en la elección, y licitar las dos cosas juntas, como recomienda la GFOA según un resumen, junta la responsabilidad. La elección entre las dos depende de cuánto sabe la empresa del producto ([elegir un sistema](elegir-un-sistema.md)).
