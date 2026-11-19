---
resumen: >-
  Recorrido para quien sabe redes en general y quiere diseñar la red de Azure: al terminar arma un
  hub-and-spoke con salida controlada, acceso privado a PaaS con su DNS y la landing zone que lo
  contiene, desplegada con Terraform.
estado: borrador
estabilidad: semi
creado: 2026-10-03
revisado:
---

# Redes en Azure para quien ya sabe redes

Recorrido para quien sabe redes en general y quiere diseñar la red de Azure: al terminar arma un
hub-and-spoke con salida controlada, acceso privado a PaaS con su DNS y la landing zone que lo
contiene, desplegada con Terraform.

1. [Virtual Network (Azure)](../Redes/virtual-network-azure.md) — la unidad de todo lo demás: espacio de direcciones, subredes y
   salida a internet. Va primero porque todas las notas siguientes la requieren.
2. [Network security group](../Redes/network-security-group.md) — el filtro dentro de la VNet; hace falta antes de conectar redes
   entre sí.
3. [Ruteo en Azure](../Redes/ruteo-en-azure.md) — cómo decide Azure por dónde va un paquete; el peering y el hub dependen
   de esto.
4. [VNet peering](../Redes/vnet-peering.md) — unir dos VNets, y por qué no es transitivo.
5. [Topología hub-and-spoke](../Redes/topologia-hub-and-spoke.md) — usa el peering no transitivo para aislar proyectos y comparte
   lo común en el hub.
6. [NAT Gateway](../Redes/nat-gateway.md) — la salida a internet de cada spoke, ahora que las subredes nuevas son
   privadas por defecto.
7. [Private endpoint](../Redes/Acceso-privado-a-PaaS/private-endpoint.md) — el acceso privado a los PaaS desde los spokes.
8. [DNS privado para Private Link](../Redes/Acceso-privado-a-PaaS/dns-privado-para-private-link.md) — sin esto el paso anterior no funciona; va justo después.
9. [Service endpoint](../Redes/Acceso-privado-a-PaaS/service-endpoint.md) — la alternativa más simple, para reconocerla y saber por qué se prefiere
   el private endpoint.
10. [Azure landing zone](../Gobernanza-e-identidad/azure-landing-zone.md) — junta la red con las políticas, la identidad y la observabilidad.
11. [Landing zone con Terraform](../Gobernanza-e-identidad/landing-zone-con-terraform.md) — cómo se despliega todo lo anterior como código, en stacks.

Para practicar: [Verificar la conectividad privada en Azure](../Redes/verificar-conectividad-privada-en-azure.md).

Para consultar: [Tamaños de VM en Azure](../Computo/tamanos-de-vm-azure.md).

**Al terminar**: se puede diseñar y verificar la red de una landing zone. Lo siguiente es el resto
del tema [Cloud](../cloud.md) (cómputo, datos y diseño de soluciones) o [Conectividad híbrida en Azure](../Redes/conectividad-hibrida-azure.md) si hay
que unir una red propia.
