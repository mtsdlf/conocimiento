---
resumen: >-
  Operación es la parte de Cloud que mantiene un servicio a la vista y en pie: lo observa con
  métricas, logs y trazas, y lo protege de la caída de un datacenter o de una región según el RTO y
  el RPO.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Operación

Operación es la parte de Cloud que mantiene un servicio a la vista y en pie: lo observa con
métricas, logs y trazas, y lo protege de la caída de un datacenter o de una región según el RTO y
el RPO.

Dentro de [Cloud](../cloud.md), la operación mira lo que corre en el [cómputo](../Computo/computo.md)
y replica los [datos operacionales](../Datos-operacionales/datos-operacionales.md). Las dos mitades
cuestan: los logs pueden superar a la factura de cómputo y duplicar en otra región puede duplicar
la factura, así que las dos se deciden con [FinOps](../FinOps/finops.md) a la vista.

## Observar sin pagar de más

Sin configurarlo, Azure guarda pocas métricas de plataforma y casi ningún log, y lo que no se envía
a un workspace no se puede consultar después de un incidente. Al revés, enviar todo sin pensar
encarece la factura. El equilibrio sale del plan de cada tabla, la retención, el sampling y lo que
se filtra antes de ingerir.

## Resistir una caída

La alta disponibilidad reparte en zonas de una región; la recuperación ante desastres copia a otra
región; el backup recupera datos borrados o corruptos, pero no da continuidad. Cuánto se invierte
en cada una lo fijan el RTO y el RPO que pide el negocio, y un plan de DR que nunca se probó no
cuenta.

## Las dos notas de operación

- [Azure Monitor](azure-monitor.md) — métricas, logs, trazas, alertas y cómo se controla el costo de los logs.
- [Alta disponibilidad y DR en Azure](alta-disponibilidad-y-dr-en-azure.md) — zonas, regiones, backup y réplica de cada servicio según RTO y RPO.
