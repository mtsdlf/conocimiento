---
tipo: recorrido
resumen: >-
  Recorrido para quien sabe redes en general y quiere diseñar la red de Azure: al terminar arma un
  hub-and-spoke con salida controlada, acceso privado a PaaS con su DNS y la landing zone que lo
  contiene, desplegada con Terraform.
estado: borrador
estabilidad: semi
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
parte_de: [cloud]
---

# Redes en Azure para quien ya sabe redes

Recorrido para quien sabe redes en general y quiere diseñar la red de Azure: al terminar arma un
hub-and-spoke con salida controlada, acceso privado a PaaS con su DNS y la landing zone que lo
contiene, desplegada con Terraform.

1. [[virtual-network-azure]] — la unidad de todo lo demás: espacio de direcciones, subredes y
   salida a internet. Va primero porque todas las notas siguientes la requieren.
2. [[network-security-group]] — el filtro dentro de la VNet; hace falta antes de conectar redes
   entre sí.
3. [[ruteo-en-azure]] — cómo decide Azure por dónde va un paquete; el peering y el hub dependen
   de esto.
4. [[vnet-peering]] — unir dos VNets, y por qué no es transitivo.
5. [[topologia-hub-and-spoke]] — usa el peering no transitivo para aislar proyectos y comparte
   lo común en el hub.
6. [[nat-gateway]] — la salida a internet de cada spoke, ahora que las subredes nuevas son
   privadas por defecto.
7. [[private-endpoint]] — el acceso privado a los PaaS desde los spokes.
8. [[dns-privado-para-private-link]] — sin esto el paso anterior no funciona; va justo después.
9. [[service-endpoint]] — la alternativa más simple, para reconocerla y saber por qué se prefiere
   el private endpoint.
10. [[azure-landing-zone]] — junta la red con las políticas, la identidad y la observabilidad.
11. [[landing-zone-con-terraform]] — cómo se despliega todo lo anterior como código, en stacks.

Para practicar: [[verificar-conectividad-privada-en-azure]].

Para consultar: [[tamanos-de-vm-azure]].

**Al terminar**: se puede diseñar y verificar la red de una landing zone. Lo siguiente es el resto
del Mapa [[cloud]] (cómputo, datos y diseño de soluciones) o [[conectividad-hibrida-azure]] si hay
que unir una red propia.
