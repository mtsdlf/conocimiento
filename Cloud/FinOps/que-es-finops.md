---
tipo: concepto
resumen: >-
  FinOps es, según la FinOps Foundation, un marco operativo y una práctica cultural que maximiza el
  valor de negocio de la tecnología y hace responsables del gasto, juntos, a ingeniería, finanzas
  y negocio.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "FinOps Foundation, What is FinOps?: https://www.finops.org/introduction/what-is-finops/"
  - "FinOps Foundation, FinOps Principles: https://www.finops.org/framework/principles/"
  - "FinOps Foundation, FinOps Personas: https://www.finops.org/framework/personas/"
  - "FinOps Foundation, FinOps Framework: https://www.finops.org/framework/"
  - "Archivo/Cloud/finops-referencia.md (original, texto generado con IA; reescrito desde las fuentes de arriba)"
aliases: [FinOps, Cloud FinOps, Cloud Financial Management]
parte_de: []
requiere: []
relacionado: []
---

# FinOps

FinOps es, según la FinOps Foundation, un marco operativo y una práctica cultural que maximiza el
valor de negocio de la tecnología y hace responsables del gasto, juntos, a ingeniería, finanzas
y negocio.

## Por qué importa

En la nube, cualquier ingeniero crea gasto con un `apply` y la factura llega un mes después a
finanzas, que no sabe qué la generó. FinOps junta a quien gasta con quien paga para que las
decisiones de tecnología se tomen mirando el costo a tiempo, no al cierre del mes.

## Cómo funciona

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

## Ejemplo

Un equipo de producto ve en su tablero que el costo de su servicio subió 30 % en un mes. Con
ingeniería encuentra un entorno de pruebas que quedó encendido; finanzas ajusta el pronóstico y el
equipo agrega el apagado nocturno a su pipeline.

## No confundir con

Recortar costos. FinOps busca el mayor valor por lo que se gasta: gastar más puede estar bien si
el ingreso crece más rápido, y eso lo mide el [Costo unitario](costo-unitario.md).

## Relaciones

- Detallada en: [Ciclo de vida de FinOps](ciclo-de-vida-finops.md) — las fases y la madurez de la práctica.
- Base de: [Showback y chargeback](showback-y-chargeback.md), [Costo unitario](costo-unitario.md) y [Optimización de costos en Azure](optimizacion-de-costos-en-azure.md).
- En otro Tema: [Plataforma como producto](../../Platform-Engineering/plataforma-como-producto.md) — el costo de cada capacidad de la
  plataforma es un dato más para su dueño; [Gobernanza de plataforma](../../Platform-Engineering/gobernanza-de-plataforma.md) — presupuestos y
  etiquetas obligatorias como límites del self-service.
