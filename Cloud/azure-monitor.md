---
tipo: concepto
resumen: >-
  Azure Monitor junta las métricas, los logs (Log Analytics) y las trazas (Application Insights) de
  los recursos de Azure y dispara alertas; su costo depende de cuánto se ingiere y cuánto se
  retiene.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Microsoft Learn, Azure Monitor Logs overview: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-platform-logs"
  - "Microsoft Learn, Log Analytics agent overview (retirado): https://learn.microsoft.com/en-us/azure/azure-monitor/agents/log-analytics-agent"
  - "Archivo/Cloud/azure-referencia-framework.md (original, Observabilidad y logs costo-efectivos)"
aliases: [Azure Monitor, Log Analytics, Application Insights, App Insights, KQL]
parte_de: []
requiere: []
relacionado: []
---

# Azure Monitor

Azure Monitor junta las métricas, los logs (Log Analytics) y las trazas (Application Insights) de
los recursos de Azure y dispara alertas; su costo depende de cuánto se ingiere y cuánto se
retiene.

## Por qué importa

Sin configurarlo, Azure guarda pocas métricas de plataforma y casi ningún log. Lo que no se envía
a un workspace no se puede consultar después de un incidente. Y al revés: enviar todo sin pensar
hace que la factura de logs supere a la de cómputo.

## Cómo funciona

- **Métricas**: series numéricas que los recursos emiten solos; baratas y rápidas para alertas.
- **Logs**: se guardan en un workspace de Log Analytics y se consultan con KQL. Llegan por
  *diagnostic settings* de cada recurso y, desde las VMs, por el Azure Monitor Agent configurado
  con *data collection rules*. El agente anterior (Log Analytics agent) se retiró en agosto de 2024.
- **Application Insights**: APM de la aplicación: requests, dependencias, trazas distribuidas y
  errores. Guarda sus datos en un workspace de Log Analytics.
- **Alertas**: de métricas (rápidas) o de consultas de logs (flexibles), que avisan por *action
  groups* (correo, webhook, función).

**Controlar el costo**:

| Palanca | Qué hace |
|---|---|
| Plan de tabla | *Analytics* para consultar y alertar; *Basic* y *Auxiliary* cuestan menos por GB a cambio de consultas limitadas |
| Retención | 30 días incluidos en Analytics (90 para App Insights), ampliables; retención larga de hasta 12 años a menor precio |
| Sampling | App Insights guarda una muestra de las trazas, no todas |
| Data collection rules | Filtran qué se recoge antes de ingerirlo |

## Ejemplo

Un equipo manda los logs de acceso de un balanceador a una tabla Basic (mucho volumen, consultas
raras) y los errores de la aplicación a Analytics con una alerta de logs. La factura de ingesta
baja y los errores siguen avisando al instante.

## No confundir con

La [[observabilidad]] como propiedad de un sistema: Azure Monitor es la herramienta que recoge
los datos; que el sistema sea observable depende de qué emite la aplicación.

## Relaciones

- La usa: [[optimizacion-de-costos-en-azure]] — los logs son una palanca de costo.
- En otro Tema: [[observabilidad]] — el concepto detrás de métricas, logs y trazas.
