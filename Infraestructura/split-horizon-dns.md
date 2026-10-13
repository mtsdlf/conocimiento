---
tipo: concepto
resumen: >-
  Split-horizon DNS responde distinto el mismo nombre según quién pregunta: desde la LAN apunta a la
  IP interna y desde internet a la pública; el servidor interno pasa a ser un punto único de falla.
estado: borrador
estabilidad: estable
dueno: matias
revisado:
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "RFC 9499, DNS Terminology (Split DNS, View): https://www.rfc-editor.org/rfc/rfc9499"
  - "ISC, Understanding views in BIND 9: https://kb.isc.org/docs/aa-00851"
  - "AdGuard Home, Configuration (rewrites): https://github.com/AdguardTeam/AdGuardHome/wiki/Configuration"
  - "home-k8, lessons/adguard-vm-lan-dns-spof.md: https://github.com/mtsdlf/home-k8/blob/main/docs/lessons/adguard-vm-lan-dns-spof.md"
aliases: [split DNS, split-horizon, DNS de horizonte dividido]
parte_de: []
requiere: []
relacionado: [desafio-acme-http-01]
---

# Split-horizon DNS

Split-horizon DNS responde distinto el mismo nombre según quién pregunta: desde la LAN apunta a la
IP interna y desde internet a la pública; el servidor interno pasa a ser un punto único de falla.

## Por qué importa

Sin split-horizon, un equipo de la LAN que abre `app.ejemplo.com` resuelve la IP pública y sale a
internet para volver a entrar a la misma red, a veces por un túnel o un proxy externo. Con
split-horizon, el tráfico interno va directo a la IP de la LAN, y además se pueden tener nombres
que solo existen adentro.

## Cómo funciona

RFC 9499 describe split DNS como servidores autoritativos que dan respuestas parcial o totalmente
distintas para los mismos dominios según el origen de la consulta. El resultado es que un nombre
pensado como único globalmente significa cosas distintas para distintos usuarios.

La implementación suele ser una de dos:

- **Views**: un servidor como BIND elige el conjunto de respuestas según la IP de origen
  (`match-clients`), el destino o una clave TSIG.
- **Resolver interno con reescrituras**: un resolver de la LAN (AdGuard Home, Pi-hole, dnsmasq)
  contesta los nombres propios con la IP interna y reenvía el resto a un DNS público.

**El costo** es que todos los clientes de la LAN dependen del resolver interno. Si se cae y el
cliente cae a un DNS público, los nombres públicos resuelven a la IP de internet y los nombres
solo internos dejan de existir. Las defensas, de mejor a peor:

- **Un segundo resolver interno** con las mismas reescrituras: la LAN sigue igual.
- **El arranque automático** del servidor DNS, para que un reinicio no lo deje apagado.
- **Un DNS público como secundario** en los clientes: no salva los nombres internos, pero deja
  funcionando internet. Muchos clientes consultan el secundario aunque el primario esté arriba, así
  que a veces reciben la respuesta pública.

## Ejemplo

En el homelab `home-k8`, un AdGuard Home en una VM resuelve los nombres públicos de los servicios
propios hacia la IP interna del gateway de Kubernetes, agrega nombres que solo existen en la LAN y
reenvía el resto a resolvers públicos. Tras un reinicio del host, la
VM no arrancó sola y ninguna máquina de la LAN pudo llegar a los servicios internos; el arreglo
fue activar el arranque automático y sumar un DNS público como secundario en la laptop, que deja internet funcionando aunque no los
nombres internos.

## No confundir con

El DNS de Kubernetes (CoreDNS), que resuelve nombres de Services dentro del clúster. Split-horizon
se ocupa de qué IP ve cada red para el mismo nombre público.

## Relaciones

- Relacionado: [[desafio-acme-http-01]] — un nombre que solo existe en la LAN necesita DNS-01 para
  obtener un certificado.
