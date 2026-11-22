---
resumen: >-
  FinOps es, según la FinOps Foundation, un marco operativo y una práctica cultural que hace
  responsables del gasto en tecnología, juntos, a ingeniería, finanzas y negocio; en Cloud es la
  parte que mira lo que cuestan todas las demás.
estado: borrador
estabilidad: estable
fuentes:
  - "FinOps Foundation, What is FinOps?: https://www.finops.org/introduction/what-is-finops/"
  - "FinOps Foundation, FinOps Principles: https://www.finops.org/framework/principles/"
  - "FinOps Foundation, FinOps Personas: https://www.finops.org/framework/personas/"
  - "FinOps Foundation, FinOps Framework: https://www.finops.org/framework/"
  - "Archivo/Cloud/finops-referencia.md (original, texto generado con IA; reescrito desde las fuentes de arriba)"
aliases: [Cloud FinOps, Cloud Financial Management]
creado: 2026-10-03
revisado:
---

# FinOps

FinOps es, según la FinOps Foundation, un marco operativo y una práctica cultural que hace
responsables del gasto en tecnología, juntos, a ingeniería, finanzas y negocio; en Cloud es la parte
que mira lo que cuestan todas las demás.

Dentro de [Cloud](../cloud.md), depende de
[Gobernanza e identidad](../Gobernanza-e-identidad/gobernanza-e-identidad.md), porque la
jerarquía de suscripciones y las etiquetas que obliga [Azure Policy](../Gobernanza-e-identidad/azure-policy.md)
son lo que permite repartir la factura. Sus palancas caen sobre el [cómputo](../Computo/computo.md)
(tamaño, reservas, Spot), los [datos operacionales](../Datos-operacionales/datos-operacionales.md)
(tiers de blob), las [redes](../Redes/redes.md) (egreso, private endpoints) y la
[operación](../Operacion/operacion.md) (retención de logs).

## Una práctica que se recorre en ciclos

En la nube, cualquier ingeniero crea gasto con un `apply` y la factura llega un mes después a
finanzas, que no sabe qué la generó. FinOps junta a quien gasta con quien paga para que las
decisiones de tecnología se tomen mirando el costo a tiempo, no al cierre del mes. El
trabajo avanza en tres fases que se repiten (Inform, Optimize, Operate), y cada capacidad madura por separado de Crawl a Walk y a Run.

## Principios, personas y dominios

**Los seis principios** oficiales de la FinOps Foundation:

1. Los equipos tienen que colaborar.
2. El valor de negocio guía las decisiones de tecnología.
3. Cada uno se hace dueño de su uso de tecnología.
4. Los datos de FinOps tienen que ser accesibles, oportunos y exactos.
5. FinOps se habilita de forma central.
6. Se aprovecha el modelo de costo variable de la nube.

**Las personas** son los roles que siempre participan: el FinOps Practitioner, Ingeniería,
Finanzas, Producto, Compras (Procurement) y la Dirección (Leadership). Otros roles, como Seguridad,
Sostenibilidad o la gestión de activos y servicios de TI, coordinan con la práctica sin ser parte
de ella.

El principio 5 explica el reparto: un equipo central negocia descuentos y publica los datos; cada
equipo decide sobre su propio uso (principio 3).

**El marco** agrupa el trabajo en cuatro dominios: entender el uso y el costo, cuantificar el
valor de negocio, optimizar el uso y el costo, y gestionar la práctica. Desde 2025 la Foundation
aplica FinOps a toda la tecnología (SaaS, data center, IA), no solo a la nube pública.

## Asignar, medir y recién después optimizar

No se optimiza lo que no se ve. Primero se asigna el gasto a cada equipo (showback, y chargeback
si las políticas contables lo piden); con eso se calcula el costo unitario, que dice si un servicio
se vuelve más eficiente aunque el total crezca. Recién después se optimiza, y en orden: primero el
uso, después la tarifa, porque comprometer una reserva antes de ajustar el tamaño congela por años
un gasto que sobraba. FinOps no es recortar: gastar más puede estar bien si el ingreso crece más
rápido.

## Un entorno de pruebas que quedó encendido

Un equipo de producto ve en su tablero que el costo de su servicio subió 30 % en un mes. Con
ingeniería encuentra un entorno de pruebas que quedó encendido; finanzas ajusta el pronóstico y el
equipo agrega el apagado nocturno a su pipeline.

## Qué hay adentro de FinOps

- [Ciclo de vida de FinOps](ciclo-de-vida-finops.md) — las fases Inform, Optimize y Operate, y la madurez Crawl, Walk, Run.
- [Showback y chargeback](showback-y-chargeback.md) — cómo se reparte la factura entre equipos y en qué se diferencian mostrar y cobrar.
- [Costo unitario](costo-unitario.md) — la métrica que relaciona el costo con lo que produce un servicio.
- [Optimización de costos en Azure](optimizacion-de-costos-en-azure.md) — rightsizing, reservas, savings plans, Spot, egreso y logs para bajar el costo sin romper los SLO.

## Ver también

- [Plataforma como producto](../../Platform-Engineering/Plataforma-interna/plataforma-como-producto.md) — el costo de cada capacidad de la
  plataforma es un dato más para su dueño.
- [Gobernanza de plataforma](../../Platform-Engineering/Plataforma-interna/gobernanza-de-plataforma.md) — presupuestos y
  etiquetas obligatorias como límites del self-service.
