---
tipo: concepto
resumen: >-
  Showback muestra a cada equipo el costo de lo que usa; chargeback además lo imputa al
  presupuesto contable de ese equipo. Los dos dependen de asignar el gasto con etiquetas y
  cuentas consistentes.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "FinOps Foundation, Invoicing & Chargeback: https://www.finops.org/framework/capabilities/invoicing-chargeback/"
  - "FinOps Foundation, Allocation: https://www.finops.org/framework/capabilities/allocation/"
  - "Microsoft Learn, Use tags to organize your Azure resources: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources"
aliases: [showback, chargeback, asignación de costos, cost allocation]
parte_de: [que-es-finops]
requiere: [que-es-finops]
relacionado: []
---

# Showback y chargeback

Showback muestra a cada equipo el costo de lo que usa; chargeback además lo imputa al
presupuesto contable de ese equipo. Los dos dependen de asignar el gasto con etiquetas y
cuentas consistentes.

## Por qué importa

Sin asignación, la factura de la nube es un solo número y nadie se siente dueño de él. Con
showback cada equipo ve su parte, que es la condición para el principio de FinOps "cada uno se
hace dueño de su uso".

## Cómo funciona

**La asignación** es la base: la FinOps Foundation la define como repartir el costo y el uso con
cuentas, etiquetas y otros metadatos para crear responsabilidad entre equipos y proyectos. En
Azure se hace con:

- **La jerarquía**: una suscripción o un grupo de recursos por equipo o proyecto.
- **Etiquetas** (`equipo`, `entorno`, `centro-de-costo`), obligadas al crear el recurso con
  [[azure-policy]].
- **Un criterio para lo compartido**: el hub de red o el clúster común se reparte por uso, en
  partes iguales o queda como costo de plataforma.

**La diferencia** entre los dos, según la Foundation, es la formalidad de mandar el gasto a
presupuestos contables oficiales. El showback siempre hace falta; el chargeback depende de las
políticas contables de la organización. Ninguno es "más maduro" que el otro.

## Ejemplo

Dos equipos comparten una suscripción. Con la etiqueta `equipo` obligatoria, el reporte mensual de
Cost Management agrupado por esa etiqueta muestra 4.000 USD para pagos y 1.500 USD para catálogo
(showback). Si finanzas además descuenta esos montos del presupuesto de cada área, es chargeback.

## No confundir con

Un presupuesto con alertas: avisa cuando un ámbito supera un monto, pero no reparte el gasto entre
equipos. Se usan juntos.

## Relaciones

- Parte de y requiere: [[que-es-finops]] — es una capacidad de la práctica.
- Usa: [[azure-policy]] — obliga las etiquetas de las que depende la asignación.
- Base de: [[costo-unitario]] — para dividir el costo de un servicio primero hay que saber cuál es.
