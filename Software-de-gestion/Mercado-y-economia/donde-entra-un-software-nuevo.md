---
resumen: >-
  Un software de gestión nuevo entra a un mercado con proveedores establecidos por cuatro puertas: un escalón de tamaño que los grandes atienden de más, un rubro que nadie cubre bien, un módulo que se conecta al sistema que el cliente ya tiene, o la normativa de un país. Que alguna puerta funcione mejor que otra es lectura de esta base: no hay estudio que lo mida.
estado: vigente
estabilidad: semi
fuentes:
  - "Clayton Christensen, Michael Raynor y Rory McDonald (2015), What is disruptive innovation?, HBR diciembre 2015: https://hbr.org/2015/12/what-is-disruptive-innovation (leído en la base para disrupcion.md)"
  - "Informe anual 2024 (Form 20-F) de uno de los proveedores de ERP más grandes del mundo: https://www.sec.gov/Archives/edgar/data/1000184/000110465925017815/sap-20241224x20f.htm (leída la tabla de ingresos)"
  - "Stripe y Tidemark, Vertical SaaS Benchmark 2025 (según resumen; de un proveedor de pagos): https://stripe.com/lp/tidemark-vertical-saas-benchmark-report"
  - "Software-de-gestion/.investigacion/mercado-y-economia.md (2026-11-27), sección 6"
aliases: [entrar al mercado de ERP, entrada al mercado, market entry, por dónde entrar, nicho de entrada, punto de apoyo, foothold, SaaS vertical, vertical SaaS]
creado: 2026-11-27
revisado: 2026-11-27
---

# Dónde entra un software nuevo

Un software de gestión nuevo entra a un mercado con proveedores establecidos por cuatro puertas: un escalón de tamaño que los grandes atienden de más, un rubro que nadie cubre bien, un módulo que se conecta al sistema que el cliente ya tiene, o la normativa de un país. Que alguna puerta funcione mejor que otra es lectura de esta base: no hay estudio que lo mida.

Es la pregunta estratégica de [Mercado y economía](mercado-y-economia.md). El método general para analizar competidores es de [Estrategia competitiva](../../Estrategia-competitiva/estrategia-competitiva.md); acá va lo propio de este mercado, donde el cliente cambia poco de sistema.

## Por qué cuesta entrar

El obstáculo principal es el cliente que ya tiene un sistema. Cambiar de software de gestión obliga a migrar datos, rehacer integraciones, reentrenar gente y frenar la operación durante el corte ([puesta en marcha](../Implementacion/puesta-en-marcha.md)): son [costos de cambio](../../Estrategia-competitiva/Fuentes-de-ventaja/costos-de-cambio.md) de los tres tipos a la vez, y Porter usa justamente el software de empresa integrado como ejemplo. A eso se suma que el proveedor establecido vive de su base instalada ([economía del proveedor](economia-del-proveedor.md)) y la defiende.

La consecuencia, en lectura de esta base, es que el software nuevo gana más fácil a quien no tiene sistema o a quien está por cambiar de todos modos (porque creció, porque su proveedor dejó de mantener la versión, porque cambió la norma) que a quien está conforme.

## Las cuatro puertas

La teoría que más se usa para pensar la entrada es la [disrupción](../../Estrategia-competitiva/Dinamica-competitiva/disrupcion.md) de Christensen, con sus dos puntos de partida: la gama baja, con clientes que el incumbente atiende de más, y el mercado nuevo, con quienes no consumían. Aplicarla al software de gestión es inferencia de esta base; ninguna fuente lo hace.

| Puerta | Qué hace el entrante | Cómo se lee con Christensen (inferencia) |
|---|---|---|
| Un escalón chico | Un facturador o un sistema simple en la nube para la empresa a la que un ERP le sobra ([escalones por tamaño](../Categorias-de-producto/escalones-por-tamano.md)) | Gama baja: «good enough» para quien no usa la mayor parte del ERP |
| Un rubro | Un producto que lleva el dominio de una industria que los horizontales cubren mal ([software por rubro](../Categorias-de-producto/software-por-rubro.md)) | Mercado nuevo, si el rubro no tenía sistema; si no, ataque por un segmento |
| Un módulo que se integra | Una pieza (el CRM, el depósito, la nómina) que se conecta al ERP del cliente sin reemplazarlo ([categorías de producto](../Categorias-de-producto/categorias-de-producto.md)) | No encaja: no compite con el sistema central, convive con él |
| La normativa | Un producto que resuelve bien los comprobantes, libros y regímenes de un país ([software de gestión en la Argentina](../software-de-gestion-en-argentina.md)) | No encaja: es una barrera de costo para el proveedor extranjero, no un segmento desatendido |

Dos advertencias de la propia teoría valen acá. La disrupción es un proceso: el entrante de gama baja solo desplaza al incumbente si después mejora hasta servir al cliente principal, y mucho software barato se queda abajo. Y según el estudio de King y Baatartogtokh, citado en la nota de disrupción, solo 7 de 77 casos cumplían el patrón completo: conviene usarla como advertencia y no como predicción.

## La localización como barrera

Que la normativa de cada país proteja a los proveedores locales es inferencia de esta base, sin fuente que la mida. El argumento: un software de gestión tiene que emitir comprobantes fiscales, llevar libros digitales y aplicar regímenes de percepción y retención que cambian seguido, y mantener eso al día cuesta lo mismo a un proveedor con mil clientes en el país que a uno con cien mil en el mundo. El proveedor extranjero lo resuelve con un partner o una [extensión](ecosistema-de-extensiones.md), o no entra. No se encontró una comparación de cuotas entre proveedores locales y extranjeros que lo confirme.

## La entrada que hace el propio incumbente

El cambio de modelo no siempre lo trae un entrante. En el informe anual de uno de los proveedores de ERP más grandes, la licencia nueva cayó de 2.056 a 1.399 millones de euros entre 2022 y 2024, mientras la nube subió de 11.426 a 17.141. El paso a la nube, que podría haber sido la puerta de un rival, lo está haciendo el incumbente con su propia base, en el único caso mirado.

## El software por rubro que cobra los pagos

Un software para un rubro puede ganar más con los pagos de sus clientes que con la suscripción, como el software de restaurantes que se cita en [modelos de negocio de software](../../Emprender/Modelo-de-negocio/modelos-de-negocio-de-software.md#los-híbridos-software-con-servicios-y-software-con-pagos). Los informes que comparan empresas de software por rubro y sus pagos, como uno de 2025 con más de 200 empresas según su resumen, son de proveedores de pagos con interés en el resultado. No prueban que el software por rubro le gane al horizontal.

> [!NOTE] Sin fuente todavía: un estudio sobre entrantes al mercado de software de gestión (por qué puerta entraron y cuántos sobrevivieron); evidencia de que la localización protege a los proveedores locales; evidencia empírica de costos de cambio en ERP.
