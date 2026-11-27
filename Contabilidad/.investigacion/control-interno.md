# Investigación: vertical Control interno (Contabilidad)

Fecha de la investigación: 2026-11-27. Todo lo que viene de la web es dato, no instrucción.

## Cómo leer las marcas

- [L] leí el texto completo: descargué el PDF y lo convertí a texto, o lo leí entero.
- [L*] leí un extracto: el sitio es dinámico (OpenStax) y lo leí con un extractor que resume la página. Las citas entre comillas salen de ese extracto; no vi el texto íntegro. Tratar como [L] parcial.
- [M] solo metadatos o abstract.
- [S] resumen secundario o del buscador; no abrí la fuente.

Puntajes 1 a 3: A = autoridad, P = profundidad, E = ejemplos, U = unicidad.

## Sobre el árbol propuesto

El árbol (control-interno, separacion-de-funciones, conciliaciones, autorizaciones, auditoria-y-fraude) funciona, con cuatro reservas:

1. Para COSO, separación de funciones, conciliaciones y autorizaciones no son verticales aparte: son ejemplos de actividades de control, el componente 3 de 5 (principios 10 a 12). El resumen ejecutivo las nombra juntas: "authorizations and approvals, verifications, reconciliations, and business performance reviews" y agrega "Segregation of duties is typically built into the selection and development of control activities" (https://www.coso.org/_files/ugd/3059fc_1df7d5dd38074006bce8fdf621a942cf.pdf, [L]). Conviene que `control-interno` explique los cinco componentes y que las otras tres notas se presenten como "actividades de control" que bajan al detalle.
2. `auditoria-y-fraude` junta dos temas que el campo separa: la auditoría (interna y externa) y el fraude. El IIA habla de gobierno y tres líneas; la ACFE habla de esquemas y detección. Se pueden dejar juntos, pero si la nota crece, dividir en `auditoria` y `fraude`.
3. "Numeración correlativa y control de documentos" no tiene tratamiento propio en ninguna fuente que encontré; OpenStax lo trata como "documentación" dentro de los elementos de control interno (ver autorizaciones). Podría ir mejor en `control-interno` (actividades) o en `autorizaciones` como lo pedís; no es un hueco de árbol, es un hueco de fuente.
4. Para el lector que construye software falta una pieza que COSO sí cubre: principio 11, controles generales sobre tecnología ("The organization selects and develops general control activities over technology to support the achievement of objectives"). Es donde viven roles, permisos, bitácora y flujos de aprobación del sistema. Sugiero abrirla como sección de `separacion-de-funciones` y `autorizaciones` ("cómo se implementa en software"), o como nota propia.

---

## 1. control-interno (entrada)

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| COSO, Internal Control — Integrated Framework, Executive Summary (mayo 2013) | https://www.coso.org/_files/ugd/3059fc_1df7d5dd38074006bce8fdf621a942cf.pdf (enlazado desde https://www.coso.org/guidance-on-ic) | primaria | 3 | 2 | 1 | 3 | [L] |
| OpenStax, Principles of Financial Accounting, 8.2 "Define and Explain Internal Controls and Their Purpose within an Organization" | https://openstax.org/books/principles-financial-accounting/pages/8-2-define-and-explain-internal-controls-and-their-purpose-within-an-organization | secundaria didáctica | 2 | 2 | 3 | 2 | [L*] |
| OpenStax 8.3 "Describe Internal Controls within an Organization" | https://openstax.org/books/principles-financial-accounting/pages/8-3-describe-internal-controls-within-an-organization | secundaria didáctica | 2 | 2 | 3 | 1 | [L*] |
| ACFE, Occupational Fraud 2024 (fig. 37 y 30, sobre controles) | https://www.acfe.com/-/media/files/acfe/pdfs/rttn/2024/2024-report-to-the-nations.pdf | primaria (datos propios) | 3 | 3 | 2 | 3 | [L] |

Nota: no hay una fuente primaria gratuita con el marco completo (el libro completo de COSO se vende). El resumen ejecutivo basta para definición, componentes, principios y límites. El COSO Framework FAQ (https://www.coso.org/_files/ugd/3059fc_8fdac5b8011e4cd08d566bf40b1ac2a8.pdf) existe pero no lo leí: [M].

### Afirmaciones

- Definición literal: "Internal control is a process, effected by an entity's board of directors, management, and other personnel, designed to provide reasonable assurance regarding the achievement of objectives relating to operations, reporting, and compliance." (COSO, [L])
- Conceptos de la definición, literales: "A process consisting of ongoing tasks and activities—a means to an end, not an end in itself"; "Effected by people—not merely about policy and procedure manuals, systems, and forms, but about people and the actions they take at every level of an organization"; "Able to provide reasonable assurance—but not absolute assurance"; "Adaptable to the entity structure". (COSO, [L])
- Tres categorías de objetivos: operaciones ("effectiveness and efficiency of the entity's operations, including operational and financial performance goals, and safeguarding assets against loss"), reporte ("internal and external financial and non-financial reporting") y cumplimiento ("adherence to laws and regulations"). (COSO, [L])
- Los cinco componentes: Control Environment, Risk Assessment, Control Activities, Information and Communication, Monitoring Activities. (COSO, [L])
- Los 17 principios, literales (COSO, [L]):
  - Control Environment
    1. The organization demonstrates a commitment to integrity and ethical values.
    2. The board of directors demonstrates independence from management and exercises oversight of the development and performance of internal control.
    3. Management establishes, with board oversight, structures, reporting lines, and appropriate authorities and responsibilities in the pursuit of objectives.
    4. The organization demonstrates a commitment to attract, develop, and retain competent individuals in alignment with objectives.
    5. The organization holds individuals accountable for their internal control responsibilities in the pursuit of objectives.
  - Risk Assessment
    6. The organization specifies objectives with sufficient clarity to enable the identification and assessment of risks relating to objectives.
    7. The organization identifies risks to the achievement of its objectives across the entity and analyzes risks as a basis for determining how the risks should be managed.
    8. The organization considers the potential for fraud in assessing risks to the achievement of objectives.
    9. The organization identifies and assesses changes that could significantly impact the system of internal control.
  - Control Activities
    10. The organization selects and develops control activities that contribute to the mitigation of risks to the achievement of objectives to acceptable levels.
    11. The organization selects and develops general control activities over technology to support the achievement of objectives.
    12. The organization deploys control activities through policies that establish what is expected and procedures that put policies into action.
  - Information and Communication
    13. The organization obtains or generates and uses relevant, quality information to support the functioning of internal control.
    14. The organization internally communicates information, including objectives and responsibilities for internal control, necessary to support the functioning of internal control.
    15. The organization communicates with external parties regarding matters affecting the functioning of internal control.
  - Monitoring Activities
    16. The organization selects, develops, and performs ongoing and/or separate evaluations to ascertain whether the components of internal control are present and functioning.
    17. The organization evaluates and communicates internal control deficiencies in a timely manner to those parties responsible for taking corrective action, including senior management and the board of directors, as appropriate.
- Preventivos y detectivos, manuales y automáticos: los controles "may be preventive or detective in nature and may encompass a range of manual and automated activities such as authorizations and approvals, verifications, reconciliations, and business performance reviews." (COSO, [L]). OpenStax 8.2 no desarrolla la distinción preventivo/detectivo (el extracto lo dice explícitamente), así que COSO es la única fuente que la nombra en esta vertical; las definiciones de "preventivo" y "detectivo" (evitar antes vs. descubrir después) quedan sin fuente propia: ver huecos.
- Razonable y no absoluto: "even an effective system of internal control can experience a failure". Límites listados: suitability of objectives; "human judgment in decision making can be faulty and subject to bias"; "human failures such as simple errors"; "Ability of management to override internal control"; "Ability of management, other personnel, and/or third parties to circumvent controls through collusion"; "External events beyond the organization's control". Conclusión: "internal control provides reasonable but not absolute assurance". (COSO, [L])
- Desde OpenStax: "A properly designed and functioning internal control system will not eliminate the risk of loss." y los controles son "the systems used by an organization to manage risk and diminish the occurrence of fraud", con tres partes: "the control environment, the accounting system, and procedures called control activities". (OpenStax 8.2, [L*])
- Empresa chica, según COSO: el marco aplica a todas, y "a smaller entity's system of internal control may be less formal and less structured, yet still have effective internal control." Sobre segregación: "Where segregation of duties is not practical, management selects and develops alternative control activities." (COSO, [L])
- Empresa chica, según ACFE: las organizaciones con menos de 100 empleados "are much less likely to have various anti-fraud controls in place", y "the smaller staff size typically means there are fewer checks and balances and less segregation of duties in place". Controles con y sin tamaño (fig. 30): auditoría externa de estados 59% (<100) frente a 91% (grandes); revisión gerencial 39% frente a 79%; departamento de auditoría interna 40% frente a 90% (los pares de cada fila salen del texto extraído del PDF; el orden pequeña/grande lo deduje del propio texto del informe). (ACFE 2024 p. 48, [L])
- Debilidad de control como causa del fraude: "the most common contributor ... was a lack of internal controls (32%), followed by an override of existing internal controls (19%). Taken together, this means that more than half of the cases occurred due to an insufficient system of internal control." (ACFE 2024 p. 50, fig. 37, [L])

### Discrepancias

OpenStax usa un modelo de tres partes (entorno, sistema contable, actividades) que no es el de COSO (cinco componentes); es una simplificación didáctica. No se contradicen, pero conviene decirlo si se usan las dos.

### Ejemplo concreto

SCICAP Federal Credit Union (Iowa): una empleada con 37 años en la entidad fue condenada por robar "over $2.7 million in cash over a 37-year period". Llevaba dos juegos de registros, nunca tomó vacaciones y era la única con acceso por contraseña. (OpenStax 8.1, https://openstax.org/books/principles-financial-accounting/pages/8-1-analyze-fraud-in-the-accounting-workplace, [L*]). Una sola fuente para el caso. Sirve para mostrar entorno de control, separación y vacaciones obligatorias en un solo relato.

### Recurso canónico

COSO, Executive Summary, páginas 1 a 8: leer la definición (p. 2), las tres categorías de objetivos (p. 3), la lista de principios (p. 6 a 7) y "Limitations" (p. 8). En qué fijarse: que los 17 principios son requisitos para considerar efectivo el sistema (los cinco componentes y sus principios deben estar "present and functioning"), y que los límites incluyen la anulación por parte de la dirección y la colusión. Para lo didáctico: OpenStax 8.2 y 8.3.

---

## 2. separacion-de-funciones

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| OpenStax 8.3 | https://openstax.org/books/principles-financial-accounting/pages/8-3-describe-internal-controls-within-an-organization | secundaria didáctica | 2 | 2 | 3 | 2 | [L*] |
| OpenStax 8.2 (caso del banco de Enid) | https://openstax.org/books/principles-financial-accounting/pages/8-2-define-and-explain-internal-controls-and-their-purpose-within-an-organization | secundaria didáctica | 2 | 1 | 3 | 2 | [L*] |
| Universidad de Missouri, política de segregación de funciones | https://www.umsystem.edu/ums/policies/finance/segregation | primaria (política institucional, no norma general) | 1 | 2 | 2 | 2 | [L*] |
| COSO Executive Summary | https://www.coso.org/_files/ugd/3059fc_1df7d5dd38074006bce8fdf621a942cf.pdf | primaria | 3 | 1 | 1 | 3 | [L] |
| ACFE 2024 | https://www.acfe.com/-/media/files/acfe/pdfs/rttn/2024/2024-report-to-the-nations.pdf | primaria | 3 | 1 | 2 | 3 | [L] |

### Afirmaciones

- Funciones: OpenStax 8.3 separa "assets from custody" ("ensures that the person who controls an asset cannot also keep the accounting records") de "separation of duties" ("at least two (if not more) people are involved with most transactions"). Ejemplos literales: "the person who orders inventory should not also receive it" y "the person who writes a check should not also sign the check". Ejemplo de custodia: una persona cuenta el efectivo y otra prepara el depósito. (OpenStax 8.3, [L*])
- La política de Missouri lista cinco funciones: Authorization, Recording, Verification, Custody of Assets y Managerial Review. Regla: "No one person should have responsibility to complete two or more of these major functions." Piso mínimo: "At a minimum, no person should be able to perform more than two of the functions." Combinaciones prohibidas: "An individual should not be in a position to initiate, approve, and review the same action"; "Employees cannot authorize transactions for their own reimbursement"; "Authorization, Verification and Managerial Review should not be performed by the same person." (Missouri, [L*]). Ojo: la regla de "no más de dos" y la de "ninguna persona dos o más" parecen contradecirse en el extracto; la primera es el ideal y la segunda el mínimo cuando se permiten excepciones con controles compensatorios. No lo pude verificar contra el texto original.
- La conciliación aparece en Missouri solo como control mitigante, no como función aparte. El pedido incluía "(y conciliar)": no hay fuente que la ponga como cuarta función; sí lo hace la práctica común. Dejarlo como interpretación, no como cita.
- Controles compensatorios, según Missouri: "Mitigating or Compensating Controls must be established." Ejemplo: si quien lleva el registro también verifica, "a frequent detailed review could be performed and documented by a supervisor". Otros listados: audit trails, reconciliation of applications, supervisor-monitored exception reports, periodic managerial reviews. (Missouri, [L*])
- COSO: "Where segregation of duties is not practical, management selects and develops alternative control activities." (COSO, [L])
- Colusión: los esquemas con tres o más perpetradores causaron pérdidas "more than twice as high" que los de dos, y "The higher losses associated with collusive schemes could be related to easier circumvention of controls, such as separation of duties". Un perpetrador: mediana USD 75,000, 12 meses, USD 6,300 por mes; dos: USD 135,000, 12 meses, USD 11,300 por mes. (ACFE 2024, [L])
- Lista de prevención de la ACFE (p. 103): "Proper separation of duties", "Use of authorizations", "Physical safeguards", "Job rotations", "Mandatory vacations". (ACFE 2024, [L])

### Ejemplo concreto

Banco de Enid, Oklahoma: "There was no segregation of duties for opening loans"; una sola empleada abrió préstamos fraudulentos (OpenStax 8.2, [L*]; una sola fuente). Combinado con SCICAP (arriba): quien custodia y a la vez registra, sin vacaciones ni revisión, puede ocultar todo.

### Recurso canónico

OpenStax 8.3, elementos 4 y 5 (custodia y separación), por ser corto y con ejemplos. Complemento: la política de Missouri, para la lista de funciones y los controles mitigantes. En qué fijarse: que separar significa que ninguna persona controle una transacción de punta a punta, y que cuando no se puede (empresa chica) lo que se exige es revisión documentada de un tercero, no "confianza".

---

## 3. conciliaciones

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| OpenStax 8.6 (conciliación bancaria) | https://openstax.org/books/principles-financial-accounting/pages/8-6-define-the-purpose-of-a-bank-reconciliation-and-prepare-a-bank-reconciliation-and-its-associated-journal-entries | secundaria didáctica | 2 | 3 | 3 | 2 | [L*] |
| OpenStax 7.4 (libro auxiliar y cuenta de control) | https://openstax.org/books/principles-financial-accounting/pages/7-4-prepare-a-subsidiary-ledger | secundaria didáctica | 2 | 2 | 2 | 2 | [L*] |
| ACFE 2024 (conciliación como método de detección) | https://www.acfe.com/-/media/files/acfe/pdfs/rttn/2024/2024-report-to-the-nations.pdf | primaria | 3 | 1 | 1 | 3 | [L] |
| Entrada del buscador sobre conciliaciones entre empresas del grupo (varios sitios de proveedores de software, p. ej. https://www.numeric.io/blog/intercompany-reconciliation) | ver URL | secundaria comercial | 1 | 1 | 1 | 1 | [S] |
| IFRS 10, párrafo B86 (eliminación íntegra de saldos intragrupo), citado vía buscador | no abrí el texto de IFRS | primaria (norma), vía [S] | 3 | 1 | 1 | 3 | [S] |

### Afirmaciones

- Una conciliación bancaria es "an internal report that explains the differences between a checking account balance and the company's own records" (OpenStax, página de términos clave, vía buscador: [S]; https://openstax.org/books/principles-financial-accounting/pages/8-key-terms).
- Pasos (OpenStax 8.6, [L*]): (1) saldo según extracto del banco; (2) sumar depósitos en tránsito y errores del banco que redujeron el saldo, restar cheques pendientes; (3) saldo bancario ajustado; (4) saldo según libros; (5) sumar cobranzas hechas por el banco e intereses ganados, restar cheques rechazados (NSF), cargos del banco y errores de registro de la empresa; (6) saldo contable ajustado, que debe igualar al bancario; (7) asentar solo las partidas del lado de los libros. "Bank errors are corrected with the bank." (el extracto parafrasea; no es cita literal).
- Detección: la conciliación de cuentas detectó el 5% de los fraudes de la muestra ACFE (fig. 13); el examen de documentos, 6%; auditoría interna, 14%; revisión gerencial, 13%. (ACFE 2024 p. 24, [L])
- Auxiliar y cuenta de control: "the total of the accounts receivable subsidiary ledger must agree with the balance" de la cuenta de control, y "If the numbers did not match, we would have to find out where the error was" (OpenStax 7.4, [L*]; el extracto cortó la frase en el medio).
- Entre empresas del grupo: solo mención. Las guías de proveedores dicen que se concilia antes de consolidar y que después se eliminan los saldos intragrupo; la base normativa citada es IFRS 10 B86(c), "eliminated in full", que no verifiqué contra la norma. [S]

### Ejemplo concreto (con números)

Feeter Plumbing Company, 31 de julio (OpenStax 8.6, [L*]). Recalculé los totales y cierran.

| Lado banco | USD | Lado libros | USD |
|---|---|---|---|
| Saldo del extracto | 77,040 | Saldo en libros | 32,760 |
| + Depósito en tránsito (noche del 31) | 34,300 | + Pagaré cobrado por el banco | 60,000 |
| + Error del banco (cheque de 320 debitado por error) | 320 | + Intereses ganados | 1,800 |
| Subtotal | 111,660 | Subtotal | 94,560 |
| - Cheques pendientes (5523 por 9,620 y 6547 por 10,000) | (19,620) | - Cheque rechazado (Berson) | (2,200) |
| | | - Error de registro del cheque 5386 (registrado 1,760 en vez de 2,000) | (240) |
| | | - Cargos del banco | (80) |
| Saldo ajustado | 92,040 | Saldo ajustado | 92,040 |

Asientos (solo lado libros): debe Caja 61,800 / haber Pagarés a cobrar 60,000 e Ingresos por intereses 1,800; debe Cuentas a cobrar 2,200 / haber Caja 2,200; debe Gasto (Dues Expense) 240 / haber Caja 240; debe Gasto por cargos bancarios 80 / haber Caja 80. El extracto que leí marca que la fuente original trae un typo (Caja 61,000 en lugar de 61,800) y rótulos confusos del interés; los 61,800 son los que cuadran. No pude ver la página sin el extractor para confirmar el typo.

Ejemplo auxiliar/control (OpenStax 7.4, [L*]): clientes al 31 de enero, PB&J 0, Jones Co. 328, Black & White 0, Tiny Tim's 2,661, total 2,989 = saldo de la cuenta de control Cuentas a cobrar 2,989. Proveedores: 5,646 + 0 + 425 = 6,071 = cuenta de control.

### Recurso canónico

OpenStax 8.6, el ejemplo de Feeter completo (extracto, libros, asientos). En qué fijarse: qué partidas necesitan asiento (solo las del lado libros) y cuáles se resuelven con el banco (errores del banco y partidas en tránsito, que se acomodan solas). Para auxiliar/control: OpenStax 7.4. Falta un recurso canónico para el grupo (hueco).

---

## 4. autorizaciones

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| OpenStax 8.3 (documentación prenumerada, responsabilidades) | https://openstax.org/books/principles-financial-accounting/pages/8-3-describe-internal-controls-within-an-organization | secundaria didáctica | 2 | 2 | 2 | 1 | [L*] |
| OpenStax 8.5 (responsabilidad de la gerencia) | https://openstax.org/books/principles-financial-accounting/pages/8-5-discuss-management-responsibilities-for-maintaining-internal-controls-within-an-organization | secundaria didáctica | 2 | 1 | 1 | 1 | [L*] |
| Cornell, "Proper Authorization" | https://finance.cornell.edu/node/904269 | primaria (política de una universidad) | 1 | 1 | 1 | 1 | [L*] |
| Universidad de Missouri, segregación | https://www.umsystem.edu/ums/policies/finance/segregation | primaria (política institucional) | 1 | 2 | 2 | 2 | [L*] |
| Guías de proveedores de software sobre maestro de proveedores y SoD (p. ej. https://www.stampli.com/resources/vendor-master-governance-segregation-of-duties/) | ver URL | secundaria comercial | 1 | 2 | 1 | 1 | [S] |
| ACFE 2024 | https://www.acfe.com/-/media/files/acfe/pdfs/rttn/2024/2024-report-to-the-nations.pdf | primaria | 3 | 2 | 2 | 3 | [L] |

### Afirmaciones

- Autorización como actividad de control: COSO la nombra entre las actividades ("authorizations and approvals"), y la ACFE la incluye en su lista de controles antifraude ("Use of authorizations"). (COSO [L]; ACFE p. 103 [L])
- Documentación: OpenStax recomienda "prenumbered forms in pen to ensure that no forms can be altered" y copias de respaldo guardadas fuera del sitio. (OpenStax 8.3, [L*]). Esa es la única fuente que encontré sobre numeración correlativa.
- Responsabilidad: "A properly designed system of internal control clearly dictates responsibility for certain roles"; si una sola persona accede a la caja, cualquier sobrante o faltante se le atribuye. (OpenStax 8.3, [L*])
- Niveles de autorización: Cornell dice que "Proper authorization is determined by a unit's delegation plan, as required by University Policy 4.2" y depende de "transaction type and dollar amount"; no da montos. (Cornell, [L*]). No encontré en fuentes primarias generales (COSO, IIA, ACFE) una matriz de autorizaciones con montos: es un hueco.
- Ninguno puede aprobar lo propio: "Employees cannot authorize transactions for their own reimbursement" (Missouri, [L*]).
- Pagos y altas de proveedores: las guías de proveedores (sin autoridad) coinciden en que crear o mantener un proveedor debe estar separado de aprobar facturas y liberar pagos, y recomiendan registrar valor viejo, valor nuevo, usuario y hora de cada cambio. [S] Solo secundarias comerciales.
- Datos de riesgo para esta nota (ACFE 2024, [L]): los esquemas de facturación ficticia (billing) ocurrieron en 22% de los casos y su mediana de pérdida fue USD 100,000; la manipulación de cheques y pagos (check and payment tampering) tuvo la mayor mediana entre los esquemas de apropiación (USD 155,000). El glosario ACFE define billing scheme como "a fraudulent disbursement scheme in which a person causes their employer to issue a payment by submitting invoices for fictitious goods or services, inflated invoices, or invoices for personal purchases".

### Ejemplo concreto

No encontré en una fuente un ejemplo numérico de matriz de autorizaciones. El único ejemplo con estructura, de OpenStax 8.3, es la regla "quien escribe el cheque no lo firma" y las pruebas de caja con recuento independiente ("The two counts should be equal"; ejemplo de un turno con ventas de USD 800 que deben coincidir con efectivo, cheques y comprobantes de tarjeta). Cualquier matriz con montos que se ponga en la nota debe rotularse como ilustrativa y propia, no de una fuente.

### Recurso canónico

No hay uno bueno y gratuito en las fuentes primarias que revisé. Provisorio: OpenStax 8.3 (documentación y separación) más la política de Missouri (nadie autoriza lo propio). Hueco: buscar una guía de "delegation of authority" de una fuente neutral (IIA, un regulador o un manual del sector público).

---

## 5. auditoria-y-fraude

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| ACFE, Occupational Fraud 2024: A Report to the Nations | https://www.acfe.com/-/media/files/acfe/pdfs/rttn/2024/2024-report-to-the-nations.pdf (página de la edición: https://legacy.acfe.com/report-to-the-nations/2024/) | primaria | 3 | 3 | 3 | 3 | [L] (leí las secciones citadas: hallazgos clave, detección, tamaño, controles; no los 5600 renglones) |
| IIA, The IIA's Three Lines Model (2020) | https://www.theiia.org/globalassets/site/communication/2020/three-lines-model-updated.pdf | primaria | 3 | 2 | 1 | 3 | [L] (principios 3 a 5; no leí el resto) |
| IAASB, ISA 200 (handbook 2013, copia en IFAC) | https://www.ifac.org/system/files/publications/files/A008%202013%20IAASB%20Handbook%20ISA%20200.pdf | primaria | 3 | 2 | 1 | 3 | [L] (párrafos 5 y A1; la versión es de 2013, hay versiones posteriores) |
| OpenStax 8.1 (triángulo del fraude) | https://openstax.org/books/principles-financial-accounting/pages/8-1-analyze-fraud-in-the-accounting-workplace | secundaria didáctica | 2 | 2 | 3 | 1 | [L*] |
| OpenStax 8.5 y 8.7 (SOX, auditores) | https://openstax.org/books/principles-financial-accounting/pages/8-7-describe-fraud-in-financial-statements-and-sarbanes-oxley-act-requirements | secundaria didáctica | 2 | 1 | 2 | 1 | [L*] |
| PCAOB AS 2201 | https://pcaobus.org/oversight/standards/auditing-standards/details/AS2201 (la página dio 403) | primaria | 3 | - | - | 3 | [S] |
| ISA 315 (Revised 2019) | no conseguí el texto; solo resultados del buscador | primaria | 3 | - | - | 3 | [S] |

### Afirmaciones: auditoría interna y externa

- Tres líneas, literal: "Internal audit provides independent and objective assurance and advice on the adequacy and effectiveness of governance and risk management." Reporta "its findings to management and the governing body". (IIA Principle 4, [L])
- Independencia: "Internal audit's independence from the responsibilities of management is critical to its objectivity, authority, and credibility. It is established through: accountability to the governing body; unfettered access to people, resources, and data needed to complete its work; and freedom from bias or interference in the planning and delivery of audit services." (IIA Principle 5, [L])
- Primera y segunda línea: "Management's responsibility to achieve organizational objectives comprises both first and second line roles" y "responsibility for managing risk remains a part of first line roles and within the scope of management." Las funciones de segunda línea incluyen "internal control" entre otros objetivos específicos. (IIA Principle 3, [L])
- Auditor externo: el auditor busca "reasonable assurance about whether the financial statements as a whole are free from material misstatement, whether due to fraud or error", que "is a high level of assurance" pero "not an absolute level of assurance, because there are inherent limitations of an audit which result in most of the audit evidence ... being persuasive rather than conclusive." (ISA 200 párr. 5, [L])
- Qué no opina el auditor externo con ISA: "The auditor's opinion therefore does not assure, for example, the future viability of the entity nor the efficiency or effectiveness with which management has conducted the affairs of the entity." Y: "In some jurisdictions, however, applicable law or regulation may require auditors to provide opinions on other specific matters, such as the effectiveness of internal control". (ISA 200 A1, [L])
- Discrepancia a presentar (ISA vs. PCAOB): bajo ISA 200 la opinión es sobre los estados financieros y, salvo que la ley lo exija, no sobre la efectividad del control interno. Bajo PCAOB AS 2201 (empresas que cotizan en EE. UU.), el auditor expresa una opinión sobre el control interno sobre el reporte financiero junto con la de los estados; esto lo vi solo en resumen del buscador [S]. Ver la nota de OpenStax: SOX 302 exige que el CEO y el CFO certifiquen, y 404 trata reporte y pruebas de control interno ([L*]; el extracto de OpenStax 8.7 no cita las secciones por número, 8.5 sí).
- Nivel de divulgación: el pedido hablaba de "nivel de divulgación" del auditor externo; interpreté como nivel de seguridad que da la opinión y qué se informa. Lo que hay en fuente es "reasonable assurance" (arriba). No encontré una fuente sobre "divulgación" como tal: ver huecos.
- Qué detecta cada uno (ACFE 2024 fig. 13, [L]): auditoría interna 14% de los casos, revisión gerencial 13%, auditoría externa 3%. Texto: "Other common detection methods included internal audit (14%) and management review (13%). Collectively, these three detection methods accounted for 70% of the cases in our data." (los tres: tip, auditoría interna y revisión gerencial.) Ese 3% importa para el lector: la auditoría de estados no está diseñada para encontrar fraude de empleados.
- Controles con mayor efecto (ACFE 2024, [L]): "four controls—surprise audits, financial statement audits, hotlines, and proactive data analysis—were associated with at least a 50% reduction in both fraud loss and duration." Auditorías sorpresa: presentes en 42% de los casos, mediana USD 75,000 con el control contra USD 200,000 sin él (63% menos), y 9 meses contra 18 meses.

### Afirmaciones: triángulo del fraude

- Cressey, según OpenStax: los defraudadores de bancos eran "otherwise law-abiding citizens" con un problema financiero que sentían que no podían revelar. "The fraud triangle consists of three elements: incentive, opportunity, and rationalization." "Perceived opportunity is when a potential fraudster thinks that the internal controls are weak." (OpenStax 8.1, [L*]). Discrepancia terminológica: OpenStax dice "incentive (or pressure)"; la formulación habitual de Cressey es presión, oportunidad y racionalización. No leí a Cressey (*Other People's Money*, 1953); la fecha y el libro son de memoria y no los afirmo como dato verificado. Una sola fuente para el triángulo.
- Señales de alerta (ACFE 2024, [L]): "experiencing financial difficulties (27%)" y "living beyond means (39%)" aparecen entre las señales de conducta registradas (fig. 54).

### Afirmaciones: datos ACFE 2024 (literales)

Todas de https://www.acfe.com/-/media/files/acfe/pdfs/rttn/2024/2024-report-to-the-nations.pdf, [L]; es una sola fuente primaria (los artículos periodísticos que repiten estas cifras no cuentan como fuentes independientes).

- Muestra: "1,921 cases", "138 countries and territories", "more than $3.1 billion" de pérdidas totales. Es la 13.ª edición.
- Mediana de pérdida por caso: USD 145,000. Pérdida promedio: USD 1.7 millones. Estimación: "CFEs estimate that organizations LOSE 5% of revenue to FRAUD each year".
- Duración: "A typical fraud case lasts 12 MONTHS before detection". "The median duration of the occupational frauds in our study was 12 months". Cuanto más dura, más cuesta: menos de seis meses, mediana USD 30,000; entre dos y tres años, USD 250,000; cinco años o más, USD 875,000.
- Categorías: apropiación indebida de activos 89% de los casos, mediana USD 120,000; corrupción 48%, USD 200,000; fraude en estados financieros 5%, USD 766,000.
- Detección (fig. 13): "tips were the most common way frauds came to light, with 43% of cases"; auditoría interna 14%; revisión gerencial 13%; examen de documentos 6%; conciliación de cuentas 5%; por accidente 5%; auditoría externa 3%; monitoreo automático de datos 3%. "This is more than three times as many cases as any other detection mechanism."
- Denuncias: "over half of all tips ... (52%) came from employees"; clientes 21%, anónimos 15%, proveedores 11%. Canales: web 40%, email 37%, teléfono 30% (lectura de la figura, el orden de los porcentajes lo tomé del texto "Email and web-based reports BOTH surpassed telephone hotlines"). "organizations with hotlines were nearly twice as likely to detect fraud via tip as organizations without hotlines."
- Esquemas más comunes en general: facturación ficticia (billing) 22% y robo de activos que no son efectivo 22%. Más costoso entre los de apropiación: manipulación de cheques y pagos, mediana USD 155,000.
- Empresas chicas (menos de 100 empleados): mediana USD 141,000, "the second-largest loss among organizational size categories"; las de 10,000 o más, USD 200,000; 100 a 999, USD 130,000; 1,000 a 9,999, USD 102,000. Esquemas en chicas contra grandes (fig. 24): corrupción 44% contra 52%; facturación 31% contra 22%; manipulación de cheques y pagos 23% contra 9%; robo de no efectivo 20% contra 23%; reintegro de gastos 20% contra 12%; skimming 19% contra 9%; cash larceny 17% contra 9%; payroll 14% contra 9%. El texto confirma que corrupción y robo de no efectivo son más frecuentes en grandes, y que cheques/pagos y skimming muestran la mayor diferencia. El orden dentro de cada par lo deduje del texto extraído del PDF; verificar mirando la figura.
- Debilidades de control: falta de controles 32%, anulación de controles existentes 19% (ver control-interno).
- Edición más reciente: la ACFE ya publicó la edición 2026 (https://www.acfe.com/fraud-resources/report-to-the-nations, [M]). No usé sus cifras; el pedido era la edición 2024. Si la base se actualiza, conviene decirlo en la nota.

### Ejemplo concreto

SCICAP (ver control-interno): USD 2.7 millones en 37 años; no hubo vacaciones ni separación. Con los datos ACFE: el caso típico dura 12 meses, y este duró 37 años. (Comparación mía.)

### Recurso canónico

ACFE 2024, "Key Findings" (p. 3 y 4), "Initial Detection of Occupational Fraud" (p. 23 y 24), "Size of Organization" y "Anti-fraud controls in small businesses" (p. 32 y 48) y la "Fraud Prevention Checklist" (p. 102 y 103). En qué fijarse: son medianas, no promedios (la propia ACFE lo aclara); la muestra son casos investigados por CFEs, no una encuesta de todas las empresas. Para los roles: IIA Three Lines Model, principios 3 a 5. Para el triángulo: OpenStax 8.1. Para el auditor externo: ISA 200, párrafos 5 y A1.

---

## Huecos

1. Preventivo vs. detectivo: no hay una definición en las fuentes abiertas que leí. COSO solo dice que los controles "may be preventive or detective". Buscar una fuente (p. ej. ISACA, ISA 315 o un manual universitario).
2. Matriz de autorizaciones con montos (delegation of authority): solo políticas de universidades, ninguna con montos usables. Sin fuente primaria general.
3. Aprobación de pagos y altas de proveedores: solo guías de proveedores de software [S]. Sin fuente neutral. La ACFE da los esquemas de facturación ficticia (22%, USD 100,000 de mediana) pero no el control.
4. Numeración correlativa y control de documentos: una sola línea (OpenStax 8.3, prenumeradas y en tinta). Hay que tratarlo con cuidado.
5. Conciliación entre empresas del grupo: solo [S]; falta leer IFRS 10 B86 y alguna guía de una firma grande o un texto académico.
6. ISA 315 (Revised 2019) y PCAOB AS 2201: no pude leer los textos (resultados del buscador y un 403). Las afirmaciones sobre la opinión del auditor en el ICFR son [S].
7. Cressey: no leí la fuente original; el triángulo viene de OpenStax. Sin fecha ni cita primaria verificadas.
8. "Nivel de divulgación" del auditor externo: no encontré fuente que use ese término; lo reduje a nivel de seguridad (reasonable assurance) y alcance de la opinión.
9. OpenStax leído con extractor: las citas de OpenStax son [L*], no las vi en el texto completo. El extractor señaló un posible typo (61,000 por 61,800) en el asiento de la nota cobrada que no pude confirmar.
10. Regla de Missouri "ninguna persona dos funciones" frente a "no más de dos": parece contradicción por el extracto; no verificada.
11. ACFE: orden de los pares pequeña/grande en la fig. 24 deducido del texto del PDF, no de la imagen; la figura de canales de denuncia (40/37/30) también. Verificar mirando el PDF.
12. Falta una fuente sobre controles de TI (principio 11 de COSO; permisos, bitácoras) específica para software de gestión; no la busqué (fuera de las tres rondas por componente).
13. Rondas de búsqueda: usé como máximo tres por componente; autorizaciones y grupo quedaron con las rondas agotadas.

---

## Ampliación para controles sobre sistemas

Agregado el 2026-11-27 para la nota `controles-sobre-sistemas`, que el árbol sumó después de la investigación. Dos búsquedas web y tres lecturas.

### Fuentes

| Fuente | URL | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|---|
| COSO, Executive Summary (2013), párrafo de Control Activities y principio 11 | https://www.coso.org/_files/ugd/3059fc_1df7d5dd38074006bce8fdf621a942cf.pdf | primaria | 3 | 1 | 1 | 3 | [L] (pdftotext propio) |
| John White, «How to use COSO to assess IT controls», Journal of Accountancy, 1 de mayo de 2014 | https://www.journalofaccountancy.com/issues/2014/may/coso-it-controls-20138951 | secundaria profesional (AICPA) | 2 | 2 | 2 | 2 | [L*] (lector automático) |
| Indiana State Board of Accounts, manual de cuentas, cap. 14 «Information Technology Controls» (cita la Green Book de la GAO, COBIT 5 de ISACA y la GTAG 8 del IIA) | https://secure.in.gov/sboa/files/CH14-Information-Technology-Controls_9-25.pdf | primaria (manual de un organismo de control; cita textual de la Green Book) | 2 | 3 | 2 | 2 | [L] (pdftotext propio) |
| IIA, GTAG 8 «Auditing Application Controls» (2007), según resultado del buscador | https://www.scribd.com/document/712251125/GTAG8 | primaria, vía buscador | 3 | - | - | 3 | [S] |

### Afirmaciones

- COSO dice que las actividades de control se hacen "at all levels of the entity, at various stages within business processes, and over the technology environment" (Executive Summary, [L]).
- Puntos de foco del principio 11, literales según White (JoA 2014, [L*]; no los verifiqué contra el marco completo, que se vende): "Determines dependency between the use of technology in business processes and technology general controls"; "Establishes relevant technology infrastructure control activities"; "Establishes relevant security management process control activities"; "Establishes relevant technology acquisition, development, and maintenance process control activities." White describe los controles generales como los que "protect the application controls (picture an umbrella)".
- Green Book de la GAO, principio 11, citada textual por el manual de Indiana ([L]):
  - 11.06: "For information systems, there are two main types of control activities: general and application control activities."
  - 11.07: los controles generales "are the policies and procedures that apply to all or a large segment of an entity's information systems" y "include security management, logical and physical access, configuration management, segregation of duties, and contingency planning."
  - 11.08: los controles de aplicación "are incorporated directly into computer applications to achieve validity, completeness, accuracy, and confidentiality of transactions and data during application processing" e incluyen "input, processing, output, master file, interface, and data management system controls."
  - 11.05: objetivos de procesamiento: completeness ("Transactions that occur are recorded and not understated"), accuracy ("recorded at the correct amount in the right account (and on a timely basis)") y validity ("Recorded transactions represent economic events that actually occurred").
  - 11.10: mantener la infraestructura "often includes backup and recovery procedures, as well as continuity of operations plans".
  - 11.11: la integridad incluye "ensuring information's nonrepudiation and authenticity".
  - 11.12: la gestión de seguridad cubre "access rights ... including who has the ability to execute transactions" y estos controles "support appropriate segregation of duties".
  - 11.13: las amenazas internas "may come from former or disgruntled employees".
  - 11.14: "providing a unique user identification or token to authorized users"; "promptly update access rights when employees change job functions or leave the entity".
  - 11.15: el control de cambios "may involve requiring authorization of change requests; reviewing the changes, approvals, and testing results".
  - 11.16: "Control activities for the development, maintenance, and change of application software prevent unauthorized programs or modifications to existing programs."
- Manual de Indiana, texto propio ([L]): la separación de funciones en un sistema se logra "by appropriate assignment of security profiles that define the data the users can access and the functions that they can perform"; "Access must be restricted to the minimum required"; "Access rights must be periodically reviewed and approved by management". Controles de aplicación según la GTAG: entre sus objetivos, "A record is maintained to track the process of data from input to storage and to the eventual output"; dominios de procesamiento: "Audit trails and overrides", "Duplicate checks", "Interface balancing"; de datos maestros: "update authorization". Documentación de operaciones: que los procesos diarios, mensuales y de cierre "are performed correctly and completely" y que "Backups are completed successfully".
- GTAG 8 (vía buscador, [S]): los controles generales alcanzan a todos los componentes, procesos y datos de la organización; los de aplicación son propios de un programa que sostiene un proceso de negocio.

### Huecos

- El texto completo de los puntos de foco de COSO y de la GTAG 8 no lo leí; los puntos de foco vienen de White.
- La Green Book tiene una revisión de 2025; el manual de Indiana cita una versión anterior (no verifiqué cuál). Los párrafos citados son los de esa versión.
- Ninguna fuente da un ejemplo con números de un control sobre sistemas; el ejemplo de la nota reusa el error de registro de 240 de Feeter Plumbing (OpenStax 8.6).
