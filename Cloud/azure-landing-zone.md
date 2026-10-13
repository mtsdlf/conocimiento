---
tipo: concepto
resumen: >-
  Una landing zone de Azure es la base preconfigurada de un entorno con varias suscripciones
  (jerarquía, políticas, identidad, red, observabilidad y costos) sobre la que cada proyecto se
  despliega sin rehacer lo común.
estado: borrador
estabilidad: estable
dueno: matias
creado: 2026-10-03
autoria: ia
idioma: es
fuentes:
  - "Microsoft Learn, What is an Azure landing zone?: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/"
  - "Microsoft Learn, Azure landing zone design areas: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-areas"
  - "Microsoft Learn, Azure landing zone implementation options: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/implementation-options"
  - "Archivo/Cloud/azure-referencia-framework.md (original, gobernanza y estructura)"
  - "Archivo/Cloud/azure-landing-zone-case.md (original, roadmap de extensiones)"
aliases: [landing zone, ALZ, Azure landing zone, zona de aterrizaje]
parte_de: []
requiere: [topologia-hub-and-spoke, azure-policy]
relacionado: []
---

# Azure landing zone

Una landing zone de Azure es la base preconfigurada de un entorno con varias suscripciones
(jerarquía, políticas, identidad, red, observabilidad y costos) sobre la que cada proyecto se
despliega sin rehacer lo común.

## Por qué importa

Sin landing zone, cada equipo arma su red, sus permisos y sus logs a su manera, y la seguridad se
audita proyecto por proyecto. Con ella, un proyecto nuevo recibe una suscripción que ya cumple las
reglas y queda conectado a lo compartido.

## Cómo funciona

El Cloud Adoption Framework de Microsoft la divide en dos partes:

- **Landing zone de plataforma**: lo compartido. Suscripciones de identidad, de conectividad (el
  hub de la [[topologia-hub-and-spoke]], el DNS privado) y de administración (Log Analytics).
- **Landing zones de carga de trabajo** (antes "de aplicación"): una suscripción por proyecto o
  equipo, bajo un management group (Online, Corp) que le aplica políticas.

**La jerarquía** es management groups > suscripciones > grupos de recursos > recursos. Las
políticas y los roles asignados arriba se heredan hacia abajo.

**Las ocho áreas de diseño** que hay que decidir: facturación y tenant de Entra ID; identidad y
acceso; organización de recursos (nombres, etiquetas); topología de red y conectividad; seguridad;
administración (monitoreo, backup); gobernanza ([[azure-policy]], costos); y automatización de la
plataforma y DevOps.

**La implementación** se hace con el portal o como código. Para Terraform, el módulo
`caf-enterprise-scale` está deprecado y archivado desde septiembre de 2026; Microsoft lo reemplaza
por el acelerador basado en Azure Verified Modules. Un diseño propio en stacks se describe en
[[landing-zone-con-terraform]].

## Ejemplo

Una landing zone chica para un homelab: un hub con DNS Private Resolver y zonas `privatelink.*`
compartidas, dos spokes con NAT Gateway y private endpoints, una política que exige etiquetas,
presupuestos con alertas y un workspace de Log Analytics. Lo que queda para crecer: Azure Firewall
para centralizar el egreso, Bastion para administrar VMs y más políticas (TLS mínimo, acceso
público negado, diagnósticos obligatorios).

## No confundir con

Una suscripción: es un límite de facturación y de acceso. La landing zone es el conjunto de
suscripciones, políticas y red que las rodea.

## Relaciones

- Requiere: [[topologia-hub-and-spoke]] — la red de la plataforma.
- Requiere: [[azure-policy]] — las reglas que cada suscripción hereda.
- Usa: [[identidad-y-acceso-en-azure]] — el área de identidad y acceso.
- Detallada en: [[landing-zone-con-terraform]] — cómo se despliega como código.
- En otro Tema: [[gobernanza-de-plataforma]] — las políticas de la landing zone son gobernanza
  incorporada a la plataforma; [[golden-path]] y [[self-service]] — un spoke nuevo desde
  plantilla es un camino soportado para el equipo que lo pide.
