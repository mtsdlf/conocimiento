---
resumen: >-
  La estructura de cuentas bancarias es qué cuentas tiene la empresa, en qué bancos y monedas, para qué uso cada una y quién puede moverlas; junto con la relación con cada banco y lo que cobra, decide por dónde corre la plata y cuánto cuesta moverla.
estado: borrador
estabilidad: semi
fuentes:
  - "APQC, Process Classification Framework 7.4 (2024), 9.7.2.7, 9.7.2.8 y 9.7.3, pp. 24 y 25 (leído): https://solutions.ifrc.org/sites/default/files/2024-10/K014750_APQC%20Process%20Classification%20Framework%20(PCF)%20-%20Cross%20Industry%20-%20PDF%20Version%207.4.pdf"
  - "ACT, Competency Framework, competencia Cash Management (leído): https://www.treasurers.org/cpd-and-training/competency-framework/"
  - "AFP, especificaciones del examen CTP, subtema de estructura bancaria (leído): http://ctpcert.financialprofessionals.org/overview/ctp-test-specifications"
  - "OpenStax, Principles of Finance (2022), 19.3 Cash Management (leído): https://openstax.org/books/principles-finance/pages/19-3-cash-management"
  - "Wikipedia, Cash management (según su resumen; artículo con aviso de mantenimiento): https://en.wikipedia.org/wiki/Cash_management"
  - "Wikipedia, Treasury management (según su resumen): https://en.wikipedia.org/wiki/Treasury_management"
  - "Tesoreria/.investigacion/caja-y-liquidez.md, secciones 1, 2 y 6 (2026-11-27)"
  - "Tesoreria/.investigacion/caja-y-cobranzas-segunda-ronda.md, sección 3 (2026-11-27)"
aliases: [cuentas bancarias, estructura de cuentas, estructura bancaria, bank account structure, bank account management, relación con los bancos, bank relationship management, comisiones bancarias, bank fees, concentración de fondos, cash concentration, cash pooling, firmantes]
creado: 2026-11-27
revisado:
---

# Cuentas bancarias

La estructura de cuentas bancarias es qué cuentas tiene la empresa, en qué bancos y monedas, para qué uso cada una y quién puede moverlas; junto con la relación con cada banco y lo que cobra, decide por dónde corre la plata y cuánto cuesta moverla.

Es el mapa sobre el que se arma la [posición de caja](posicion-de-caja.md): cada cuenta es una fila con sus saldos. Los [medios de cobro y pago](medios-de-cobro-y-pago.md) son los caminos por los que la plata entra y sale de esas cuentas. Quién puede abrir una cuenta, en qué bancos y con qué firmas lo fija la [política de tesorería](../politica-de-tesoreria.md).

## Lo que dicen los marcos

El tema tiene marco pero casi no tiene desarrollo abierto. APQC le da dos subprocesos dentro de la gestión de caja: 9.7.2.7, «Manage and oversee banking relationships», y 9.7.2.8, «Analyze, negotiate, resolve, and confirm bank fees». La ACT incluye la administración de cuentas bancarias («bank account administration») dentro de la gestión de caja. El examen de la AFP pide «Manage optimal banking structure such as cash concentration/pooling etc.».

Ninguna de las tres fuentes dice cuántas cuentas conviene tener, en cuántos bancos ni con qué firmas. Lo que sigue en las secciones de estructura y firmantes es lectura de esta base y está marcado como tal.

## Para qué se abre cada cuenta

Por lectura de esta base, una pyme separa las cuentas por uso cuando el volumen lo justifica: una cuenta donde entran los cobros, una de la que salen los pagos a proveedores, una para sueldos, una en moneda extranjera si cobra o paga en otra moneda, y una o más donde se colocan los excedentes. Separar facilita conciliar, porque cada extracto trae un solo tipo de movimiento, y facilita controlar, porque cada cuenta tiene sus firmantes. El costo es más comisiones y más saldos que mirar.

> [!NOTE] Sin fuente todavía: una guía con autoridad sobre cómo se diseña la estructura de cuentas de una pyme (cuántas, de qué tipo, en cuántos bancos). La página de la ACT sobre estructuras de cuentas dio error al leerla.

## Firmantes y poderes

Cada cuenta tiene personas habilitadas para moverla, con un tope y a veces con firma conjunta. Ninguna fuente leída lo desarrolla. Las reglas generales de quién aprueba qué están en [autorizaciones](../../Contabilidad/Control-interno/autorizaciones.md), y por qué quien registra no tiene que ser quien firma, en [separación de funciones](../../Contabilidad/Control-interno/separacion-de-funciones.md).

Por lectura de esta base, la lista de firmantes de cada banco es un dato que envejece: una persona que deja la empresa sigue habilitada hasta que alguien avisa al banco. Por eso el registro de firmantes se revisa con la misma frecuencia que los accesos a los sistemas.

> [!NOTE] Sin fuente todavía: práctica documentada sobre firmantes, firmas conjuntas y poderes bancarios, y su revisión periódica.

## La relación con los bancos y lo que cobran

APQC trata la relación con los bancos como un proceso propio. El título de 9.7.2.8 nombra cuatro verbos sobre las comisiones: analizar, negociar, resolver y confirmar. Las comisiones aparecen como cargos en el extracto, y la [conciliación](../../Contabilidad/Control-interno/conciliaciones.md) las registra. Por lectura de esta base, el proceso incluye elegir con quién se opera, qué servicios se contratan y cómo se revisa lo que cobran, y compararlas con lo pactado es trabajo de la tesorería.

Un banco puede cobrar también en saldos. OpenStax describe el saldo compensatorio, un mínimo que la empresa mantiene en su cuenta corriente como condición de un préstamo; en su ejemplo, 50.000 dólares sobre un préstamo de 500.000. Esa plata no rinde y no se puede usar, así que encarece el préstamo (inferencia de esta base; el costo del préstamo se compara en [costo del financiamiento](../Financiamiento/costo-del-financiamiento.md)).

Por lectura de esta base, en cuántos bancos tener la plata es una decisión de riesgo: si un banco cae o congela fondos, la empresa pierde acceso a lo que tenía ahí. Esa decisión, con el límite por banco, está en [riesgos financieros](../Riesgos-financieros/riesgos-financieros.md).

## Concentrar los fondos

Cuando la plata entra por muchas cuentas (sucursales, bancos regionales, monedas), conviene juntarla. Según el resumen de un artículo de referencia, en la concentración de caja el banco principal junta en una cuenta que paga interés los saldos de las cuentas locales. Otro artículo, del que también se leyó solo el resumen, ubica el pooling, el netting y el banco interno entre las funciones de la tesorería, sin explicarlos.

APQC pone todo eso en 9.7.3, «Manage in-house bank accounts», con cuentas para las subsidiarias, préstamos entre empresas del grupo, pagos y cobros centralizados y «Manage internal payments and netting transactions». Es cosa de un grupo con varias sociedades. Una pyme de una sola sociedad lo resuelve, por lectura de esta base, con transferencias propias entre sus cuentas al armar la [posición de caja](posicion-de-caja.md).

> [!NOTE] Sin fuente todavía: la diferencia entre el pooling físico (se mueve la plata) y el nocional (el banco calcula intereses sobre la suma sin moverla), y cuándo conviene cada uno. La página de Wikipedia sobre cash pooling dio error al leerla.

## Cómo se modela en un sistema

Por lectura de esta base, la cuenta bancaria es una entidad con estos datos: banco, número e identificador para transferencias, moneda, uso, firmantes con su tope, cuenta contable que la refleja, estado (activa o cerrada) y fecha del último extracto importado. Con eso el sistema puede:

- armar la posición por cuenta y por moneda;
- elegir de qué cuenta sale cada pago según su uso y su saldo;
- avisar cuando una cuenta no recibe extracto hace días, que suele ser una cuenta olvidada;
- comparar las comisiones del extracto contra las pactadas con el banco.

El registro de movimientos y la integración con los bancos como diseño técnico van al tema Software de gestión, todavía no escrito.

## Cómo falla

Las fallas habituales, por lectura de esta base: cuentas abiertas para un uso que ya no existe, con saldo y comisiones que nadie mira; firmantes que dejaron la empresa y siguen habilitados; toda la plata en un solo banco; comisiones que suben sin que nadie las compare con lo pactado; y saldos atados a un préstamo que la posición muestra como libres. Los bancos, las cuentas en dólares y las comisiones de transferencia en la Argentina están en [tesorería en Argentina](../tesoreria-en-argentina.md).
