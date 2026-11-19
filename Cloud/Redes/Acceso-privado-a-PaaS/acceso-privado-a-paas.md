---
resumen: >-
  El acceso privado a PaaS son los mecanismos para que una carga llegue a un servicio PaaS de Azure
  sin pasar por su IP pública y para cerrar ese acceso público: private endpoint con su DNS,
  service endpoint y network security perimeter.
estado: borrador
estabilidad: estable
fuentes: []
creado: 2026-11-19
revisado:
---

# Acceso privado a PaaS

El acceso privado a PaaS son los mecanismos para que una carga llegue a un servicio PaaS de Azure
sin pasar por su IP pública y para cerrar ese acceso público: private endpoint con su DNS,
service endpoint y network security perimeter.

Dentro de [Redes](../redes.md), es la pieza de un diseño privado por defecto. Un servicio PaaS
nace con IP pública; estas piezas dejan que los [datos operacionales](../../Datos-operacionales/datos-operacionales.md)
queden con el acceso público apagado y que [Azure Policy](../../Gobernanza-e-identidad/azure-policy.md)
niegue los que queden abiertos.

## Tres formas y cuál se recomienda

Desde una VNet se llega a un PaaS de tres formas: una instancia dedicada del servicio dentro de la
VNet, un private endpoint (una IP privada en la subred para una instancia del servicio) o un
service endpoint (la subred se identifica ante el servicio, que sigue con IP pública). Microsoft
recomienda el private endpoint; el service endpoint queda para casos simples o de bajo costo. El
network security perimeter no mete al recurso en ninguna red: pone una frontera de acceso público
alrededor de varios PaaS, y se puede usar junto con el private endpoint.

## Por qué casi todo falla en el DNS

El cliente sigue usando el nombre público del servicio. Si lo resuelve un DNS que no conoce la zona
`privatelink.*`, sale a la IP pública y, con el acceso público apagado, recibe un 403 o un timeout
que no parece un problema de DNS. Por eso el private endpoint no sirve sin su zona DNS privada
vinculada a cada VNet, y desde la red propia sin un resolver en el hub.

## Las cuatro notas de acceso privado

- [Private endpoint](private-endpoint.md) — una IP privada para una instancia de un PaaS; la forma recomendada. Leerla primero.
- [DNS privado para Private Link](dns-privado-para-private-link.md) — por qué el nombre tiene que resolver a la IP privada y cómo.
- [Service endpoint](service-endpoint.md) — la alternativa sin IP privada, más barata y más limitada.
- [Network security perimeter](network-security-perimeter.md) — una frontera de acceso público alrededor de varios PaaS.
