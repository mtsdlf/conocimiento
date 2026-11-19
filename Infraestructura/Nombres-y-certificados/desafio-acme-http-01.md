---
resumen: >-
  El desafío HTTP-01 de ACME prueba que se controla un dominio sirviendo un token en
  `/.well-known/acme-challenge/` por el puerto 80; en Kubernetes, cert-manager lo resuelve con un
  pod y un Service temporales.
estado: borrador
estabilidad: estable
fuentes:
  - "Let's Encrypt, Challenge types: https://letsencrypt.org/docs/challenge-types/"
  - "RFC 8555, §8.3 HTTP challenge: https://www.rfc-editor.org/rfc/rfc8555#section-8.3"
  - "cert-manager, HTTP01: https://cert-manager.io/docs/configuration/acme/http01/"
  - "cert-manager, ACME orders and challenges: https://cert-manager.io/docs/concepts/acme-orders-challenges/"
  - "cert-manager, DNS01: https://cert-manager.io/docs/configuration/acme/dns01/"
  - "Let's Encrypt, From 90 to 45 days: https://letsencrypt.org/2025/12/02/from-90-to-45"
  - "Archivo/Infraestructura/apisix-certmanager-letsencrypt.md"
aliases: [HTTP-01, http01, ACME HTTP challenge, desafío HTTP-01]
creado: 2026-10-03
revisado:
---

# Desafío ACME HTTP-01

El desafío HTTP-01 de ACME prueba que se controla un dominio sirviendo un token en
`/.well-known/acme-challenge/` por el puerto 80; en Kubernetes, cert-manager lo resuelve con un
pod y un Service temporales.

## Certificados que se renuevan solos

Una autoridad como Let's Encrypt solo firma un certificado para `ejemplo.com` si quien lo pide
demuestra que controla ese dominio. ACME (RFC 8555) automatiza esa prueba con desafíos, y así un
certificado se emite y se renueva sin intervención. Automatizar importa más cada año: Let's Encrypt
emite hoy certificados de 90 días y anunció que bajan a 45 días para 2028.

## Del token a la validación, y el solver de cert-manager

1. El cliente ACME pide un certificado y recibe un token.
2. El cliente publica el token en `http://<dominio>/.well-known/acme-challenge/<token>`.
3. Let's Encrypt consulta esa URL desde internet por el puerto 80. Sigue hasta 10 redirecciones,
   solo hacia los puertos 80 o 443.
4. Si la respuesta coincide, el dominio queda validado y se emite el certificado.

En Kubernetes, cert-manager crea por cada desafío un pod `acmesolver` y un Service. Con
`ingressClassName` crea además un Ingress que manda la ruta del desafío al pod; con
`gatewayHTTPRoute` crea un HTTPRoute de Gateway API. Antes de avisarle a Let's Encrypt, cert-manager
hace un self-check: pide la URL él mismo y espera a que responda. Si el Ingress controller o el gateway no sabe
enrutar hacia el Service del solver, el self-check falla y el certificado queda pendiente.

## Un `Certificate` con solver HTTP-01

Un clúster expone `app.ejemplo.com` con un Ingress controller en el puerto 80 de la IP pública.
Se crea un `Certificate` (el pedido de certificado de cert-manager) que usa un `ClusterIssuer` (la
configuración de la cuenta ACME) con solver HTTP-01. cert-manager crea el pod solver y un Ingress
temporal que manda `/.well-known/acme-challenge/*` a ese pod; Let's Encrypt valida y cert-manager
guarda el certificado en un Secret, que renueva antes del vencimiento.

Si el self-check corre desde dentro del clúster y el nombre resuelve a una IP que no se alcanza
desde adentro (la pública del router, sin hairpin NAT), el self-check falla aunque desde internet
funcione.

## Cuándo conviene DNS-01

El desafío **DNS-01** es la alternativa. DNS-01 publica el token en un registro TXT `_acme-challenge.<dominio>`: no
necesita el puerto 80 abierto y permite certificados wildcard, que HTTP-01 no permite. A cambio,
el cliente necesita credenciales de la API del DNS. Conviene DNS-01 cuando el servicio no es
alcanzable desde internet, por ejemplo en una LAN con [Split-horizon DNS](split-horizon-dns.md) o detrás de un túnel;
el homelab `home-k8` usa DNS-01 con Cloudflare por esa razón.
