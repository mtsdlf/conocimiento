---
resumen: >-
  Los riesgos financieros son lo que puede salir mal con la plata de la empresa por causas de afuera: no tener caja cuando vence un pago (liquidez), que cambie la tasa de la deuda (tasa), que no pague quien debe (contraparte) o que se mueva el tipo de cambio; la tesorería decide cuáles acepta y cuáles cubre, según la política de tesorería.
estado: borrador
estabilidad: estable
fuentes:
  - "APQC, Process Classification Framework 7.4 (2024), categorías 9.7.3, 9.7.4 y 9.7.5 (leído): https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "Wikipedia, Liquidity risk, como fuente terciaria, orientada a bancos y aseguradoras (según su resumen): https://en.wikipedia.org/wiki/Liquidity_risk"
  - "Wikipedia, Interest rate risk, como fuente terciaria (según su resumen): https://en.wikipedia.org/wiki/Interest_rate_risk"
  - "Wikipedia, Forward contract, como fuente terciaria (según su resumen): https://en.wikipedia.org/wiki/Forward_contract"
  - "Wikipedia, Greensill Capital, como fuente terciaria (leído): https://en.wikipedia.org/wiki/Greensill_Capital"
  - "Jin y Jorion (2006), Firm Value and Hedging: Evidence from U.S. Oil and Gas Producers, Journal of Finance 61(2):893-919 (según su abstract): https://ideas.repec.org/a/bla/jfinan/v61y2006i2p893-919.html"
  - "Tesoreria/.investigacion/financiamiento-y-riesgos.md, secciones 0 y 2 (2026-11-27)"
  - "Tesoreria/.investigacion/financiamiento-y-pagos-segunda-ronda.md, sección 4 (2026-11-27)"
  - "Tesoreria/.investigacion/fundamentos-y-contraria.md, sección 4.5 (2026-11-27)"
aliases: [riesgos financieros, financial risk, financial risk management, gestión de riesgos financieros, riesgo de liquidez, liquidity risk, funding liquidity risk, riesgo de tasa, riesgo de tasa de interés, interest rate risk, riesgo de contraparte, counterparty risk, cobertura, hedging]
creado: 2026-11-27
revisado:
---

# Riesgos financieros

Los riesgos financieros son lo que puede salir mal con la plata de la empresa por causas de afuera: no tener caja cuando vence un pago (liquidez), que cambie la tasa de la deuda (tasa), que no pague quien debe (contraparte) o que se mueva el tipo de cambio; la tesorería decide cuáles acepta y cuáles cubre, según la política de tesorería.

La vertical recibe riesgos de las otras cuatro. [Caja y liquidez](../Caja-y-liquidez/caja-y-liquidez.md) dice cuánta plata hay y en qué bancos; [Crédito y cobranzas](../Credito-y-cobranzas/credito-y-cobranzas.md), cuánto deben los clientes; [Financiamiento](../Financiamiento/financiamiento.md), cuánta deuda hay, a qué tasa y en qué moneda. Riesgos financieros mira esos mismos números con otra pregunta: qué pasa si algo de afuera cambia. El fraude y el error interno no son de acá: son del [control interno](../../Contabilidad/Control-interno/control-interno.md) y de la [seguridad de los pagos](../Pagos-a-proveedores/seguridad-de-los-pagos.md).

## Cómo lo ordena APQC

APQC pone el riesgo en la categoría 9.7.5, «Monitor and execute risk and hedging transactions», con procesos para el riesgo de tasa (9.7.5.2), el de tipo de cambio (9.7.5.3), la exposición a clientes (9.7.5.4) y la ejecución de coberturas (9.7.5.5). No tiene un proceso de riesgo de liquidez: lo cubre 9.7.4.3 «Manage liquidity», dentro de deuda e inversión. Tampoco tiene uno de riesgo de contraparte: aparece repartido entre la exposición a emisores de inversiones (9.7.4.4), el seguimiento del crédito en las coberturas (9.7.5.5.5) y la exposición a clientes.

Dos cosas del marco importan para la pyme. La cobertura de tasa y la de cambio se definen «in accordance with risk policy» (9.7.5.2.3 y 9.7.5.3.3): primero se escribe qué se cubre, en la [política de tesorería](../politica-de-tesoreria.md), y después se cubre. Y el riesgo de contraparte no tiene un solo dueño, porque cada contraparte vive en otra parte del tema.

## Riesgo de liquidez: la plata que no llega a tiempo

El riesgo de liquidez es no poder pagar lo que vence. Wikipedia (fuente terciaria, escrita para bancos y aseguradoras) distingue dos formas. El riesgo de fondeo es que los pasivos no se puedan pagar a su vencimiento, o solo a un precio antieconómico. El riesgo de liquidez de mercado es que un activo no se pueda vender porque el mercado no lo compra.

Las mitigaciones que lista la misma fuente son líneas de crédito siempre disponibles, reservas explícitas de liquidez, un plan de contingencia de fondeo y probar el flujo de caja día a día con el escenario de que una contraparte clave no pague. En una empresa no financiera cada una tiene su lugar en el tema (lectura de esta base):

- La reserva y dónde se pone, en [colocación de excedentes](../Caja-y-liquidez/colocacion-de-excedentes.md). Una colocación que no se puede rescatar a tiempo es riesgo de liquidez de mercado.
- El escenario de prueba, en la [proyección de caja](../Caja-y-liquidez/proyeccion-de-caja.md).
- Las líneas, en el [financiamiento de corto plazo](../Financiamiento/financiamiento-de-corto-plazo.md). Una línea que el banco puede no desembolsar no protege en la semana en que hace falta.

## Riesgo de tasa: fija o variable

Wikipedia define el riesgo de tasa como la posibilidad de perder plata por los movimientos de las tasas de interés, pero trata bonos y bancos y no el caso de una empresa que debe.

> [!NOTE] Sin fuente todavía: el riesgo de tasa para quien toma deuda. La lectura de esta base, sin fuente leída: con deuda a tasa variable la empresa pierde si la tasa sube, porque suben las cuotas; con tasa fija pierde si la tasa baja, porque paga más que el mercado. En una pyme se resuelve sobre todo al elegir el préstamo: tasa fija o variable, y a qué plazo. La empresa grande además cubre con instrumentos (un canje de tasa, un tope), que APQC pone en 9.7.5.2. Falta una guía profesional de la ACT o de la AFP.

Para el sistema, el riesgo de tasa se ve si cada [préstamo](../Financiamiento/prestamos.md) guarda si su tasa es fija o variable y contra qué referencia se ajusta: así la proyección puede mostrar las cuotas con una tasa más alta.

## Riesgo de contraparte: quién puede no cumplir

El riesgo de contraparte es que quien le debe algo a la empresa no cumpla. En una pyme hay cuatro contrapartes, y cada una se trata en su lugar (lectura de esta base sobre el reparto de APQC):

- Los clientes, que pueden no pagar lo que compraron a plazo: es el [crédito a clientes](../Credito-y-cobranzas/credito-a-clientes.md).
- Los bancos y los emisores donde está la caja o la colocación: se acota repartiendo entre varios y fijando un límite por contraparte, en [cuentas bancarias](../Caja-y-liquidez/cuentas-bancarias.md) y [colocación de excedentes](../Caja-y-liquidez/colocacion-de-excedentes.md).
- El financiador del que depende un cobro anticipado: en Greensill, según Wikipedia (fuente terciaria), las aseguradoras dejaron la cobertura y el financiador cayó; está en [financiamiento de la cadena](../Financiamiento/financiamiento-de-la-cadena.md).
- La contraparte de una cobertura: según Wikipedia, los contratos forward tienen un riesgo de contraparte significativo (la fuente no da el motivo). Está en [riesgo de tipo de cambio](riesgo-de-tipo-de-cambio.md).

## Cómo se decide qué cubrir

Que cubrir compense no es obvio. Jin y Jorion (2006) estudiaron 119 productoras de petróleo y gas de Estados Unidos entre 1998 y 2001: según su abstract, la cobertura redujo la sensibilidad del precio de la acción al precio de la materia prima, pero no hallaron evidencia de que cambiara el valor de mercado de la empresa. No es un estudio de tipo de cambio ni de pymes; muestra que el valor de cubrir hay que justificarlo.

La decisión, en la lectura de esta base sobre APQC, tiene cuatro pasos:

1. Medir la exposición: cuánta deuda a tasa variable, cuánto se cobra y se paga en cada moneda y cuándo, cuánta plata hay en cada banco.
2. Decidir en la política qué parte se acepta y cuál se cubre, y con qué instrumentos.
3. Cubrir primero con decisiones del negocio: tasa fija, cobrar y pagar en la misma moneda, repartir los bancos.
4. Usar instrumentos financieros para lo que queda, si la política lo permite.

Qué hace la pyme con el tipo de cambio, con datos, está en [riesgo de tipo de cambio](riesgo-de-tipo-de-cambio.md).

## Lo que es de la empresa grande

Algunas herramientas solo tienen sentido en un grupo con varias empresas o países: el banco interno, que centraliza las cuentas de las filiales (APQC 9.7.3), la compensación de saldos entre empresas del grupo (*netting*) y la contabilidad de coberturas (9.7.5.6). Esta base las nombra como cosa de empresa grande y no las desarrolla, según el [alcance del tema](../ALCANCE.md).

## Cómo fallan

- Una sola línea, un solo banco. Si el único banco corta la línea o tiene problemas, la empresa pierde a la vez su caja y su financiamiento (lectura de esta base).
- Medir la liquidez solo con el saldo. La caja de hoy no dice si alcanza para los vencimientos de las próximas semanas; eso lo dice la proyección.
- Cubrir sin política. Una cobertura decidida caso por caso, sin saber qué se quería cubrir, puede terminar siendo una apuesta (lectura de esta base sobre la regla de APQC).
- Confiar en quien financia el cobro. El cobro anticipado depende del financiador, como mostró Greensill.

## Lo que hay adentro de Riesgos financieros

- [Riesgo de tipo de cambio](riesgo-de-tipo-de-cambio.md): las exposiciones de transacción, traslación y económica, la cobertura natural, el forward y los futuros, y qué hacen las pymes; leelo cuando la empresa cobra, paga o debe en otra moneda.

El riesgo de liquidez, el de tasa y el de contraparte no tienen nota propia: están en esta entrada y en las notas de otras verticales que se enlazan arriba.
