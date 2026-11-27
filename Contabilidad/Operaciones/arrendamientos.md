---
resumen: >-
  Un arrendamiento es un contrato que le da a una empresa el derecho a controlar el uso de un bien ajeno durante un plazo a cambio de pagos; con la NIIF 16, quien lo toma registra un activo por el derecho de uso y un pasivo por los pagos futuros, y el gasto se reparte entre amortización e interés.
estado: borrador
estabilidad: estable
fuentes:
  - "IFRS Foundation, NIIF 16 Arrendamientos, texto oficial (edición HTML 2026), párr. 5 a 50, 61 a 84, 100 a 103, B3 a B8, Apéndice A y C1: https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs16.html"
  - "IASB, IFRS 16 Effects Analysis (enero de 2016), secciones de presentación, ratios y covenants: https://www.ifrs.org/-/media/project/leases/ifrs/published-documents/ifrs16-effects-analysis.pdf"
  - "IASB, staff paper 7A, Post-implementation Review of IFRS 16, Overall assessment (julio de 2026), párr. 11 a 26 y 68 a 69: https://www.ifrs.org/content/dam/ifrs/meetings/2026/july/iasb/ap7a-pir-ifrs-16-overall-assessment.pdf"
  - "Contabilidad/.investigacion/arrendamientos.md (2026-11-27)"
aliases: [arrendamiento, arrendamientos, leasing, lease, leases, NIIF 16, IFRS 16, activo por derecho de uso, derecho de uso, right-of-use asset, pasivo por arrendamiento, lease liability, arrendatario, lessee, arrendador, lessor, arrendamiento financiero, finance lease, arrendamiento operativo, operating lease, alquiler, NIC 17]
creado: 2026-11-27
revisado:
---

# Arrendamientos

Un arrendamiento es un contrato que le da a una empresa el derecho a controlar el uso de un bien ajeno durante un plazo a cambio de pagos; con la NIIF 16, quien lo toma registra un activo por el derecho de uso y un pasivo por los pagos futuros, y el gasto se reparte entre amortización e interés.

La NIIF 16 rige para los ejercicios que empiezan desde el 1 de enero de 2019 (párr. C1) y reemplazó a la NIC 17 (párr. C21), que dejaba los arrendamientos operativos fuera del balance de quien los tomaba. El cambio importa porque el alquiler de un local, de una flota o de una máquina por cinco años compromete pagos futuros igual que un préstamo, y antes no se veía en el balance. El IASB contó casi 3 billones de dólares de compromisos por arrendamientos que las empresas cotizadas con NIIF o con normas de Estados Unidos solo revelaban en notas (Effects Analysis, 2016). En Argentina, las empresas que no aplican las NIIF (en general, las que no cotizan) siguen otra regla, que mantiene el modelo anterior: está en [arrendamientos en Argentina](arrendamientos-en-argentina.md).

Cómo financia la tesorería un bien con un leasing y cómo entra la cuota en la proyección de caja está en [préstamos](../../Tesoreria/Financiamiento/prestamos.md#leasing); acá queda cómo se registra. Decidir si conviene arrendar o comprar no tiene nota todavía.

## Cuándo un contrato es un arrendamiento

La NIIF 16 lo define por el control: «A contract is, or contains, a lease if the contract conveys the right to control the use of an identified asset for a period of time in exchange for consideration» (párr. 9). Hacen falta las dos cosas: un bien identificado (no «una camioneta cualquiera de la flota del proveedor») y el derecho a dirigir su uso y quedarse con sus beneficios. Se evalúa al firmar y solo se vuelve a evaluar si cambian los términos (párr. 11). Un contrato de servicio que no da ese control no es arrendamiento y va a gasto a medida que se recibe.

Muchos contratos mezclan el uso del bien con servicios, como un alquiler de equipos con mantenimiento incluido. La norma pide separar cada componente y repartir el precio según los precios independientes (párr. 12 a 14); como atajo, el arrendatario puede elegir no separarlos, por clase de bien, y tratar todo como arrendamiento (párr. 15).

El plazo es el período que no se puede cancelar más las prórrogas que el arrendatario está «reasonably certain» de usar y los períodos de una opción de terminación que está razonablemente seguro de no usar (párr. 18).

## El asiento del arrendatario

Quien toma el bien, el arrendatario, ya no clasifica: «At the commencement date, a lessee shall recognise a right-of-use asset and a lease liability» (párr. 22). Es un modelo único, el mismo para el local que para la máquina.

- **El pasivo** es el valor presente de los pagos que faltan, descontados con la tasa implícita del contrato o, si no se puede determinar, con la tasa incremental, la que el arrendatario pagaría por pedir prestado lo necesario para un bien parecido (párr. 26 y Apéndice A). Entran los pagos fijos, los variables que dependen de un índice o una tasa (con el valor del índice al inicio), las garantías de valor residual, la opción de compra si es razonablemente seguro que se ejerce y las multas por terminar si el plazo las supone (párr. 27). Los pagos variables que dependen de otra cosa, como un porcentaje de las ventas del local, quedan afuera y van a resultados cuando ocurren (párr. 38).
- **El activo por derecho de uso** se mide al costo: el pasivo inicial, más lo pagado antes del inicio, menos los incentivos recibidos, más los costos directos iniciales y la estimación del costo de desmantelar o restaurar (párr. 24).

Después, el activo se amortiza como cualquier [activo fijo](activos-fijos-y-amortizacion.md), en el menor entre su vida útil y el plazo del arrendamiento, salvo que la propiedad pase al arrendatario (párr. 31 y 32). El pasivo crece por el interés y baja por los pagos, con una tasa constante sobre el saldo (párr. 36 y 37).

### Una máquina a cinco años, con cifras supuestas

La norma remite a ejemplos ilustrativos que no estaban en el texto leído; las cifras son supuestas y el cálculo está verificado. Una empresa toma una máquina por 5 años y paga 10.000 al final de cada año. No hay pagos previos, costos iniciales ni opciones, y su tasa incremental es del 8% anual.

El pasivo inicial es 10.000 × (1 − 1,08⁻⁵) / 0,08 = 39.927,10, y el derecho de uso arranca con el mismo importe. Se amortiza en línea recta en los 5 años del plazo: 7.985,42 por año.

| Año | Pasivo al inicio | Interés (8%) | Pago | Pasivo al cierre | Amortización | Gasto del año |
|---|---|---|---|---|---|---|
| 1 | 39.927,10 | 3.194,17 | 10.000 | 33.121,27 | 7.985,42 | 11.179,59 |
| 2 | 33.121,27 | 2.649,70 | 10.000 | 25.770,97 | 7.985,42 | 10.635,12 |
| 3 | 25.770,97 | 2.061,68 | 10.000 | 17.832,65 | 7.985,42 | 10.047,10 |
| 4 | 17.832,65 | 1.426,61 | 10.000 | 9.259,26 | 7.985,42 | 9.412,03 |
| 5 | 9.259,26 | 740,74 | 10.000 | 0,00 | 7.985,42 | 8.726,16 |
| Total | | 10.072,90 | 50.000 | | 39.927,10 | 50.000,00 |

Al inicio:

| Cuenta | Debe | Haber |
|---|---|---|
| Activo por derecho de uso | 39.927,10 | |
| Pasivo por arrendamiento | | 39.927,10 |

Al cierre del año 1, el interés, el pago y la amortización:

| Cuenta | Debe | Haber |
|---|---|---|
| Intereses por arrendamiento | 3.194,17 | |
| Pasivo por arrendamiento | | 3.194,17 |
| Pasivo por arrendamiento | 10.000,00 | |
| Caja | | 10.000,00 |
| Amortización del derecho de uso | 7.985,42 | |
| Amortización acumulada del derecho de uso | | 7.985,42 |

En los cinco años el gasto suma 50.000, lo mismo que los pagos, pero se carga más al principio: 11.179,59 el primer año y 8.726,16 el último, porque el interés se calcula sobre un saldo que baja. Con la NIC 17, si el contrato era operativo, el registro era un gasto de alquiler de 10.000 por año, sin activo ni pasivo.

## Las dos exenciones

El arrendatario puede no aplicar el modelo a dos clases de contratos y registrar los pagos como gasto en línea recta (párr. 5 y 6):

- **Corto plazo**: «a lease term of 12 months or less» (Apéndice A). Un contrato con opción de compra no califica. La elección se hace por clase de bien (párr. 8).
- **Bajo valor**: se mira el bien nuevo y en términos absolutos, sin importar el tamaño de la empresa. La norma da como ejemplos tabletas, computadoras personales, muebles chicos y teléfonos, y dice que un auto no califica (B3 a B8). Esta elección se hace contrato por contrato.

Para quien construye un sistema, las exenciones son la frontera entre dos circuitos: el contrato que entra en una de ellas se registra como una factura de gasto común ([compras y cuentas a pagar](compras-y-cuentas-a-pagar.md)); el que no, necesita su propio registro con plazo, cuotas, tasa y una tabla como la de arriba.

## Cuando el contrato cambia

El pasivo no queda fijo. Se vuelve a medir si cambia el plazo (porque ahora es razonablemente seguro que se usa una prórroga), si cambia la evaluación de la opción de compra, si cambia lo esperado por una garantía de valor residual o si se ajusta el índice de las cuotas (párr. 39 a 43). La diferencia va contra el derecho de uso, y si este llega a cero, el resto va a resultados (párr. 39). Cuando cambia el plazo o la opción de compra se usa una tasa revisada; cuando cambia la garantía o un índice, la tasa original, salvo que el cambio venga de una tasa de interés variable (párr. 40 a 43).

Una modificación que suma el uso de otro bien a un precio proporcional es un contrato nuevo (párr. 44); cualquier otra se resuelve volviendo a medir el pasivo con una tasa revisada (párr. 45 y 46). En la práctica, cada actualización de un alquiler indexado obliga a recalcular la tabla desde esa fecha.

## Dónde aparece en los estados contables

- **[Balance](../Estados-contables/balance.md)**: el derecho de uso va en el mismo renglón que iría el bien si fuera propio, o se dice en cuál está; el pasivo, aparte o con su renglón informado (párr. 47).
- **[Estado de resultados](../Estados-contables/estado-de-resultados.md)**: la amortización y el interés, por separado (párr. 49). El alquiler deja de existir como gasto operativo.
- **[Estado de flujo de efectivo](../Estados-contables/estado-de-flujo-de-efectivo.md)**: la parte de capital de cada pago va en financiación, el interés donde la empresa ubique los intereses, y los pagos de las exenciones y los variables en operación (párr. 50). En el año 1 del ejemplo, 6.805,83 van a financiación y 3.194,17 son interés.

El activo y el pasivo tienen bases fiscales que suelen diferir de su valor contable, y por eso un arrendamiento genera [impuesto diferido](../Estados-contables/impuesto-diferido.md); la NIC 12 lo trata expresamente desde una enmienda de 2021.

## El arrendador sigue clasificando

Quien da el bien, el arrendador, mantiene la división de la norma anterior (párr. 61). El arrendamiento es financiero si «transfers substantially all the risks and rewards incidental to ownership of an underlying asset» (párr. 62); si no, es operativo. La norma da ejemplos que, solos o juntos, suelen llevar a financiero: la propiedad pasa al final, hay una opción de compra que es razonablemente seguro que se ejerce, el plazo cubre la mayor parte de la vida económica, el valor presente de los pagos equivale a casi todo el valor razonable del bien, o el bien es tan específico que solo el arrendatario lo puede usar (párr. 63).

- **Financiero**: el arrendador saca el bien de su balance y registra una cuenta a cobrar por la inversión neta, que devenga interés (párr. 67, 68 y 75). Es, en sustancia, una venta financiada.
- **Operativo**: el bien queda en su balance y se amortiza, y las cuotas son ingreso en línea recta (párr. 81, 82 y 84), como en [ingresos y cuentas a cobrar](ingresos-y-cuentas-a-cobrar.md).

Cuando una empresa vende un bien y lo vuelve a tomar en arrendamiento, la NIIF 16 le hace reconocer solo la ganancia de la parte de los derechos que de verdad transfirió (párr. 100); si la transferencia no es una venta, sigue con el bien y registra un pasivo financiero por lo cobrado (párr. 103).

## Lo que se le critica a la NIIF 16

> [!IMPORTANT]
> **Disputado: si un modelo único refleja bien todos los arrendamientos.**
> - **El IASB**, al emitir la norma, anticipó que «Applying IFRS 16, EBITDA will be notably higher» y que subiría el endeudamiento, y lo trató como un cambio contable y no económico; previó que los covenants se renegociarían o ya estaban protegidos por cláusulas que congelan las normas, y concluyó que «the benefits of IFRS 16 outweigh the costs» (Effects Analysis, 2016).
> - **Muchos preparadores y algunos usuarios**, en la revisión posterior a la implementación, dicen que un modelo único no refleja contratos que ven como operativos y no como deuda, se quejan de «distortions to EBITDA, leverage and other metrics» y del interés cargado al principio, y publican medidas que revierten la norma, incluso para los bancos que miden covenants sobre la base anterior (staff paper 7A, julio de 2026, párr. 13 y 20).
> - **El personal técnico del IASB** concluye que la norma está «overall working as intended» y propone estudiar cómo abaratar las tasas de descuento y las remediciones, que para muchos preparadores costaron más de lo esperado (párr. 22 a 25), aunque concluye que en conjunto los costos continuos «are not significantly higher than expected» (párr. 68 y 69). Es un papel del personal técnico; el informe final de la revisión no se encontró.

Sobre la magnitud: Lopes y Penela (2025), con datos de 2019 de empresas cotizadas, encuentran un EBITDA alrededor de 16,85% más alto, según el abstract; no se leyó el artículo.

> [!NOTE] Sin fuente todavía: los ejemplos ilustrativos de la NIIF 16 (los que traen cifras oficiales) y su fundamento de las conclusiones, que no venían en el texto leído.

## Qué leer de la norma

La NIIF 16 en la página de la IFRS Foundation. Para registrar contratos alcanzan los párrafos 9 a 16 (identificar y separar), 22 a 27 (reconocer y medir), 29 a 43 (después del inicio), 47 a 50 (presentación), B3 a B8 (bajo valor) y el Apéndice A (definiciones). Conviene fijarse en que el pasivo es un valor presente que se recalcula y que el derecho de uso lo sigue.
