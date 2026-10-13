---
tipo: concepto
resumen: >-
  Las palancas para bajar el costo en Azure sin romper los SLO: ajustar el tamaño y apagar lo que
  no se usa, comprometer uso con reservas o savings plans, usar Spot y Hybrid Benefit, y controlar
  el egreso y los logs.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Microsoft Learn, Save costs with Azure Reservations: https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/save-compute-costs-reservations"
  - "Microsoft Learn, What are Azure savings plans?: https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/savings-plan-overview"
  - "Microsoft Learn, Azure Hybrid Benefit (SQL): https://learn.microsoft.com/en-us/azure/azure-sql/azure-hybrid-benefit"
  - "Microsoft Learn, Use Azure Spot Virtual Machines: https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms"
  - "Microsoft Learn, Create and manage budgets: https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets"
  - "Microsoft Learn, Advisor cost recommendations: https://learn.microsoft.com/en-us/azure/advisor/advisor-cost-recommendations"
  - "FinOps Foundation, FinOps Framework (Usage Optimization, Rate Optimization): https://www.finops.org/framework/"
  - "Archivo/Cloud/azure-referencia-framework.md (original, Costos y Logs)"
aliases: [optimización de costos en Azure, reducir costos Azure, rightsizing, reservas, savings plan, Spot VM]
parte_de: []
requiere: [que-es-finops]
relacionado: []
---

# Optimización de costos en Azure

Las palancas para bajar el costo en Azure sin romper los SLO: ajustar el tamaño y apagar lo que
no se usa, comprometer uso con reservas o savings plans, usar Spot y Hybrid Benefit, y controlar
el egreso y los logs.

## Por qué importa

Es la fase Optimize del ciclo de [[que-es-finops]] aplicada a Azure. El orden importa: comprometer
uso con una reserva antes de ajustar el tamaño congela por años un gasto que sobraba.

## Cómo funciona

La FinOps Foundation separa dos familias: optimizar el **uso** (consumir menos) y optimizar la
**tarifa** (pagar menos por lo mismo). Se hace primero la de uso.

**Uso**

- **Rightsizing**: Azure Advisor recomienda achicar o apagar VMs y scale sets con poco uso.
- **Apagar no-producción** fuera de horario y escalar a cero lo que lo permite (Functions, Container
  Apps, SQL serverless).
- **Autoescalado** en lugar de dimensionar para el pico.
- **Datos**: lifecycle policies que pasan blobs a Cool, Cold o Archive; autoscale de RU en Cosmos DB.
- **Red**: el egreso a internet y entre regiones se cobra por GB; la caché de Front Door lo baja,
  y los private endpoints cobran por hora y por GB procesado.
- **Logs**: retención corta, tablas Basic o Auxiliary para lo ruidoso, sampling (ver
  [[azure-monitor]]).

**Tarifa**

| Mecanismo | Compromiso | Cuándo conviene |
|---|---|---|
| **Reservas** | 1 o 3 años de un recurso concreto (serie de VM, región); hasta 72 % menos que el precio por uso; se pueden cambiar y reembolsar con tope | Carga estable que no va a cambiar de tipo |
| **Savings plan** | 1 o 3 años de un gasto por hora en cómputo; no se cancela ni se reembolsa | Carga estable que cambia de serie o de región |
| **Spot** | Ninguno; Azure desaloja la VM con 30 segundos de aviso | Batch, CI, cargas que toleran cortes |
| **Hybrid Benefit** | Licencias propias de Windows Server o SQL Server con Software Assurance | Quien ya pagó esas licencias |

**Avisar a tiempo**: los presupuestos de Cost Management alertan por gasto real o pronosticado,
pero no apagan nada.

## Ejemplo

Un equipo achica a la mitad las VMs que Advisor marca como subutilizadas, apaga dev de noche y
recién después compra un savings plan por el cómputo que quedó estable. Al revés, el plan habría
cubierto capacidad que sobraba.

## No confundir con

Recortar sin mirar el valor: bajar una base a un tamaño que rompe el SLO de latencia ahorra en la
factura y pierde en el negocio. El [[costo-unitario]] muestra si la optimización mejoró la
eficiencia.

## Relaciones

- Requiere: [[que-es-finops]] — es la fase Optimize de la práctica.
- Usa: [[azure-monitor]] — los logs son una de las palancas.
- Se mide con: [[costo-unitario]] — si el costo por unidad bajó.
