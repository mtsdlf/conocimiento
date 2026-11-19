---
resumen: >-
  Pasos para comprobar desde dentro de un spoke que un private endpoint resuelve a IP privada, que
  el egreso a internet sale por la NAT Gateway y que otro spoke no es alcanzable, y para aislar si
  una falla es de red o de la aplicación.
estado: borrador
estabilidad: semi
fuentes:
  - "Archivo/Cloud/azure-homelab-landing-zone.md (original, Apéndice C y §5)"
  - "Matias/Estudio/terraform-modulos-avanzados.md (sección AZURE NETWORKING, troubleshooting de red)"
  - "Microsoft Learn, Virtual network peering (troubleshoot): https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview"
  - "Microsoft Learn, Diagnose a virtual machine routing problem: https://learn.microsoft.com/en-us/azure/virtual-network/diagnose-network-routing-problem"
  - "Microsoft Learn, Troubleshoot connections with Azure Network Watcher: https://learn.microsoft.com/en-us/azure/network-watcher/connection-troubleshoot-portal"
aliases: [probar private endpoint, troubleshooting de red en Azure]
creado: 2026-10-03
revisado:
---

# Verificar la conectividad privada en Azure

Pasos para comprobar desde dentro de un spoke que un private endpoint resuelve a IP privada, que
el egreso a internet sale por la NAT Gateway y que otro spoke no es alcanzable, y para aislar si
una falla es de red o de la aplicación.

## Qué tener antes de probar

- Una máquina dentro del spoke para probar: una VM sin IP pública (entrando con Bastion o Run
  Command) o un contenedor de prueba en una subred del spoke.
- Saber cómo un [Private endpoint](Acceso-privado-a-PaaS/private-endpoint.md) depende del [DNS privado para Private Link](Acceso-privado-a-PaaS/dns-privado-para-private-link.md), y cómo una
  [Topología hub-and-spoke](topologia-hub-and-spoke.md) aísla los spokes.
- La IP pública de la [NAT Gateway](nat-gateway.md) del spoke, a mano.

## Los cuatro chequeos y cómo aislar una falla

1. Resolvé el nombre público del servicio desde el spoke, por ejemplo
   `nslookup <cuenta>.blob.core.windows.net`. Tiene que devolver una IP de la subred de endpoints
   (p. ej. `10.1.2.4`), no una pública. Si devuelve una pública, falta el vínculo de la zona
   `privatelink.*` con esta VNet.
2. Conectate al servicio por HTTPS:
   `curl -sS -o /dev/null -w "%{http_code} %{remote_ip}\n" https://<cuenta>.blob.core.windows.net/`.
   Un 403 o un 400 con la IP privada alcanza: el TLS llegó al servicio y lo que falta es
   autenticación.
3. Consultá la IP de salida: `curl -s https://ifconfig.me`. Tiene que coincidir con la IP de la
   NAT Gateway del spoke.
4. Intentá llegar a un endpoint de otro spoke con timeout corto (`curl --connect-timeout 3 …`).
   Tiene que fallar: los spokes no tienen ruta entre sí.
5. Si algo falla, aislá la capa en este orden:
   1. ¿La aplicación responde desde la misma máquina y el puerto escucha?
   2. **Effective security rules** de la NIC: ¿algún [NSG](network-security-group.md) la bloquea?
   3. **Effective routes** de la NIC: ¿hay rutas con next hop *VNet peering* hacia el hub? ¿Una
      [UDR](ruteo-en-azure.md) manda el tráfico a otro lado?
   4. **Connection troubleshoot** de Network Watcher, de la NIC origen al destino: muestra en qué
      salto se corta.
   5. Los flow logs en Log Analytics, para ver el tráfico real permitido o denegado.

## La combinación que prueba el aislamiento

El paso 1 devuelve una IP privada, el 2 muestra esa misma IP como `remote_ip`, el 3 devuelve la IP de la NAT y el 4 termina en timeout.
Esa combinación prueba acceso privado, egreso fijo y aislamiento entre proyectos.
