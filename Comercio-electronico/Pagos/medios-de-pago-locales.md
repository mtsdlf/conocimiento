---
resumen: >-
  Los medios de pago locales son los rieles que mueven el dinero sin pasar por las redes de tarjetas, como las transferencias instantáneas de un banco central, los pagos con QR y las billeteras con saldo propio. En América Latina compiten con la tarjeta en la venta online y cambian lo que cuesta cobrar, cuándo llega el dinero y si el pago se puede revertir.
estado: borrador
estabilidad: semi
fuentes:
  - "BCRA, Transferencias 3.0, sin fecha: https://www.bcra.gob.ar/sistemas-de-pago/transferencias-3-0/ (leído vía herramienta de resumen)"
  - "BCRA, Comunicación A 6885, 30/1/2020: https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A6885.pdf (leído: puntos 1.1.1 a 1.1.5)"
  - "MODO, página de inicio, sin fecha: https://www.modo.com.ar/ (leído vía herramienta de resumen)"
  - "Banco Central do Brasil, Relatório de Gestão do Pix 2023-2025: https://www.bcb.gov.br/content/estabilidadefinanceira/pix/relatorio_de_gestao_pix/relatorio_gestao_pix_2026.pdf (leído: índice, estadísticas, MED y Pix Automático)"
  - "Legisweb, Resolución BCB 402, julio de 2024: https://www.legisweb.com.br/legislacao/?id=462331 (según resumen del buscador)"
  - "EBANX, comunicado con datos de PCMI, 15/1/2026: https://business.ebanx.com/en/press-room/press-releases/digital-wallets-become-the-fastest-growing-payment-method-in-brazilian-e-commerce-in-2025-pcmi/ebanx-reports (leído vía herramienta de resumen; proveedor de pagos con interés comercial)"
  - "EBANX, Beyond Borders 2025: https://ebanx.com/en/beyond-borders-2025/ (leído vía herramienta de resumen; no da cifras de Argentina)"
  - "Comercio-electronico/.investigacion/pagos.md (secciones 1 y 4)"
  - "Comercio-electronico/.investigacion/huecos-pagos-y-operaciones.md (sección 3)"
aliases: [local payment methods, LPM, alternative payment methods, APM, transferencia instantánea, instant payment, Transferencias 3.0, pago con QR, billetera virtual, digital wallet, Pix, MED, Pix Automático]
creado: 2026-11-22
revisado:
---

# Medios de pago locales

Los medios de pago locales son los rieles que mueven el dinero sin pasar por las redes de tarjetas, como las transferencias instantáneas de un banco central, los pagos con QR y las billeteras con saldo propio. En América Latina compiten con la tarjeta en la venta online y cambian lo que cuesta cobrar, cuándo llega el dinero y si el pago se puede revertir.

> [!WARNING]
> Ley y dinero: las reglas que se cuentan acá (irrevocabilidad, tarifas, devoluciones) no reemplazan el consejo de un abogado o un contador; se leyeron en páginas sin fecha o por resúmenes.

Un medio de pago es el riel por donde corre el dinero; las [cuotas](cuotas.md) son financiación y se montan casi siempre sobre la tarjeta. Los rieles locales tienen otros actores que los de la tarjeta, descritos en [actores del pago](actores-del-pago.md), y otras reglas cuando algo sale mal.

## Transferencias 3.0 y el QR en Argentina

El BCRA presentó en 2020 un esquema de pagos con transferencia, Transferencias 3.0. Según su página, la acreditación es «en línea en un máximo de 15 segundos», las 24 horas, con cuatro tipos de operación: push, pull, pagos con transferencia y extracciones, estas últimas sin implementar todavía.

El QR es parte de los pagos con transferencia y es interoperable: «no importa la marca del código QR, podés pagar con cualquier billetera». Los pagos con transferencia son «irrevocables», el comprador no paga comisión y el comercio paga una tarifa propia, que está en [costos de cobro en Argentina](costos-de-cobro-en-argentina.md). La página no tiene fecha ni cita las comunicaciones que lo hicieron obligatorio.

## Billeteras e iniciadores de pago

Una billetera guarda medios de pago o saldo del cliente. Si guarda saldo, es un proveedor de servicios de pago con cuenta de pago en el marco de la A 6885 del BCRA, que se cuenta en [actores del pago](actores-del-pago.md). No se verificó en el registro del BCRA qué billeteras figuran.

Otro tipo de actor no guarda dinero: inicia el pago desde la cuenta bancaria del comprador. MODO se presenta como «un Proveedor de Servicio de Iniciación de Pagos», disponible en las apps de más de 30 bancos.

> [!NOTE]
> Sin fuente todavía: la participación de cada medio de pago en la venta online argentina (tarjeta, transferencia, QR, billetera), y cifras de uso de Transferencias 3.0, del QR o de MODO. La página regional de EBANX no da cifras de Argentina.

## Pix en Brasil

Pix es la transferencia instantánea del Banco Central do Brasil, y el caso con más datos públicos de un riel local. En 2025 llegó a casi 80 mil millones de transacciones (79,8), según el informe de gestión del propio Banco Central. En la venta online, un procesador de pagos lo ubica apenas por encima de la tarjeta de crédito en 2025. Esas cifras, con su fuente y sus discrepancias, están en [Pix en cifras](pix-en-cifras.md).

Dos productos de Pix importan al comercio. Pix Automático, para pagos recurrentes por débito autorizado, funciona desde el 16 de junio de 2025; lo creó la Resolución BCB 402 de julio de 2024, según un resumen del buscador. Le permite a un comercio cobrar pagos recurrentes sin tarjeta, y es un débito, no una cuota.

El MED (Mecanismo Especial de Devolução) funciona desde 2021. Permite bloquear fondos y pedir la devolución en casos comprobados de golpes, fraudes o crímenes, y desde octubre de 2025 tiene un autoservicio, el «botón de contestación». Es lo más parecido a un [contracargo](fraude-y-contracargos.md) que tiene Pix, pero lo inicia la víctima de un fraude. No se verificó qué pasa cuando el comprador reclama por un producto que no recibió.

## Qué cambia para el comercio frente a la tarjeta

| Rasgo | Tarjeta | Transferencia en Argentina | Pix |
|---|---|---|---|
| Quién paga la comisión | el comercio, con la tasa de descuento | el comercio; el comprador no paga | sin dato en las fuentes leídas |
| Cuándo llega el dinero | según el plazo que el comercio elija y pague | en un máximo de 15 segundos | sin dato en las fuentes leídas |
| Si se puede revertir | sí, por contracargo, durante meses | no: es irrevocable | solo por fraude comprobado, con el MED |
| Cuotas | sí, sobre la tarjeta de crédito | no | Pix Parcelado no está confirmado ([cuotas](cuotas.md)) |

La tabla junta datos de fuentes distintas; sus columnas no se compararon en una sola fuente. Que un medio irrevocable le saque al comercio el riesgo de contracargo es una inferencia de esas reglas: el riesgo de fraude pasa al comprador o al banco, y ninguna fuente leída lo mide.

## Cómo se usa al analizar una plataforma de tiendas

Frente a una plataforma de tiendas, se mira qué medios locales ofrece en su checkout además de la tarjeta, si los cobra por su propio agregador o por terceros, y a qué tarifa. En Brasil, una plataforma sin Pix deja afuera un medio que un procesador ubica en 42 % del valor de la venta online en 2025. En Argentina falta la cifra equivalente, así que el peso de la transferencia y el QR hay que medirlo en el análisis concreto.

El recurso para Pix es el [informe de gestión 2023-2025 del Banco Central do Brasil](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/relatorio_de_gestao_pix/relatorio_gestao_pix_2026.pdf): leer el infográfico de estadísticas de la sección 2, la 1.1.4 (Pix Automático) y la 1.2.1 (MED). Para Argentina, la [página de Transferencias 3.0 del BCRA](https://www.bcra.gob.ar/sistemas-de-pago/transferencias-3-0/) y los documentos técnicos que enlaza.
