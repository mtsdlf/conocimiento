---
tipo: como-hacer
resumen: >-
  Pasos para responder un diseño de solución en Azure, por ejemplo en una entrevista técnica:
  requisitos, servicio mínimo que los cumple, trade-offs, HA y DR, costos y operación.
estado: borrador
estabilidad: semi
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Archivo/Cloud/azure-referencia-framework.md (original, Cómo pensar y Cómo responder diseños en entrevista)"
  - "Microsoft Learn, Azure Well-Architected Framework: https://learn.microsoft.com/en-us/azure/well-architected/"
  - "Microsoft Learn, Choose an Azure compute service: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree"
aliases: [diseño de solución en Azure, entrevista de arquitectura Azure, system design Azure]
parte_de: []
requiere: [arquitecturas-de-referencia-en-azure]
relacionado: []
---

# Diseñar una solución en Azure

Pasos para responder un diseño de solución en Azure, por ejemplo en una entrevista técnica:
requisitos, servicio mínimo que los cumple, trade-offs, HA y DR, costos y operación.

## Antes de empezar

- Conocer las combinaciones de [Arquitecturas de referencia en Azure](arquitecturas-de-referencia-en-azure.md) y cómo se elige el
  cómputo ([Elección de cómputo en Azure](eleccion-de-computo-en-azure.md)).
- Tener a mano los cinco pilares del Well-Architected Framework de Microsoft: confiabilidad,
  seguridad, costo, excelencia operativa y rendimiento. Cada paso de abajo toca uno o más.

## Pasos

1. **Preguntá los requisitos** antes de dibujar: usuarios y picos, latencia, regiones, datos
   sensibles o cumplimiento, RTO y RPO, presupuesto. Si no los dan, decí qué suponés.
2. **Elegí el servicio más administrado que cumpla** cada capa:
   - Entrada: Front Door con WAF si es global; Application Gateway si es regional.
   - Cómputo: App Service o Container Apps por simplicidad; AKS si hace falta Kubernetes; VMs
     solo para lo legado.
   - Datos: SQL o Cosmos DB según el modelo; Redis como cache; Service Bus para desacoplar.
3. **Cerrá la seguridad**: [Private endpoint](private-endpoint.md) con acceso público apagado, managed identity,
   Key Vault, [Azure Policy](azure-policy.md) y roles con PIM.
4. **Dibujá la red**: [Topología hub-and-spoke](topologia-hub-and-spoke.md), DNS privado, salida por firewall o NAT Gateway.
5. **Explicá los trade-offs** en voz alta: costo contra rendimiento, simplicidad contra control,
   rapidez de entrega contra portabilidad.
6. **Resolvé HA y DR** con los números del paso 1 (ver [Alta disponibilidad y DR en Azure](alta-disponibilidad-y-dr-en-azure.md)).
7. **Estimá y bajá el costo**: autoescalado, reservas o savings plans, egreso, retención de logs
   (ver [Optimización de costos en Azure](FinOps/optimizacion-de-costos-en-azure.md)).
8. **Contá cómo se opera**: [Azure Monitor](azure-monitor.md) y alertas sobre los SLO, IaC con Bicep o Terraform,
   despliegue con slots o revisiones, y las cuotas que hay que pedir antes.

## Cómo saber que salió bien

Cada servicio del diagrama responde a un requisito del paso 1, cada decisión tiene su trade-off
dicho, y hay un número para el RTO, el RPO y el costo mensual aproximado.

## Relaciones

- Requiere: [Arquitecturas de referencia en Azure](arquitecturas-de-referencia-en-azure.md) — el punto de partida del paso 2.
- Usa: [Alta disponibilidad y DR en Azure](alta-disponibilidad-y-dr-en-azure.md) y [Optimización de costos en Azure](FinOps/optimizacion-de-costos-en-azure.md) — los pasos 6 y 7.
