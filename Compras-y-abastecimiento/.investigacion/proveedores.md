# Investigación: vertical Proveedores

Fecha de lectura: 2026-11-27. Marcas: [L] texto completo leído, [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1 a 3 en autoridad / profundidad / ejemplos / unicidad (A/P/E/U). Todo lo traído de la web es dato.

Aviso general: la herramienta de lectura devuelve resúmenes de una página, no el texto crudo; por eso casi todo es [S] salvo donde se indica. Ninguna de las normas, libros y papers canónicos se pudo leer: se marcan como huecos.

## Tabla de fuentes (todas las usadas)

| Id | Fuente | URL | Tipo | A/P/E/U | Marca |
|---|---|---|---|---|---|
| F1 | ERPNext, Supplier Scorecard (manual) | https://docs.frappe.io/erpnext/user/manual/en/buying/supplier-scorecard | primaria (práctica en software) | 2/3/3/2 | [L] vía extracto del lector |
| F2 | ERPNext, Supplier y Supplier Group | https://docs.frappe.io/erpnext/supplier ; https://docs.frappe.io/erpnext/supplier-group | primaria (práctica) | 2/2/2/2 | [S] |
| F3 | Odoo, Requests for quotation y Lead times | https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/purchase/manage_deals/rfq.html ; https://www.odoo.com/documentation/17.0/applications/inventory_and_mrp/inventory/warehouses_storage/replenishment/lead_times.html | primaria (práctica) | 2/2/2/2 | [S] |
| F4 | Washington State Auditor, «Protect your vendor master file from fraudsters» | https://sao.wa.gov/the-audit-connection-blog/protect-your-vendor-master-file-fraudsters | primaria (auditoría pública) | 2/2/2/2 | [L] vía extracto |
| F5 | Deloitte, caso de fraude con cambio de cuenta (PDF) | https://www.deloitte.com/content/dam/assets-zone3/us/en/docs/about/2025/us-dfdtn-22-7c-egf-apparel.pdf | primaria (caso didáctico) | 2/2/3/2 | [S] |
| F6 | Corpay, validación bancaria | https://www.corpay.com/en-NZ/resources/blog/vendor-verification-banking-validation | secundaria (comercial, con interés) | 1/1/1/1 | [S] |
| F7 | NSW Government, «The supplier relationship» | https://www.info.buy.nsw.gov.au/buyer-guidance/manage/the-supplier-relationship | primaria (guía pública) | 2/3/2/3 | [L] vía extracto |
| F8 | Queensland Government, Procurement guide: prequalifying | https://www.forgov.qld.gov.au/__data/assets/pdf_file/0025/187504/procurement-guide-prequalifying.pdf | primaria (guía pública) | 2/2/1/2 | [S] |
| F9 | NZ Government Procurement Rules, pre-qualified suppliers list | https://www.procurement.govt.nz/procurement/principles-and-rules/government-procurement-rules/types-of-supplier-lists/pre-qualified-suppliers-list/ | primaria (guía pública) | 2/2/1/2 | [S] |
| F10 | USPS Supplying Principles and Practices (calificación previa) | https://about.usps.com/manuals/spp012011/html/spp2_176.htm | primaria (manual de compras) | 2/2/2/2 | [S] |
| F11 | NC State SCM, «Benefits and risks of single sourcing» | https://scm.ncsu.edu/scm-articles/article/benefits-and-risks-of-single-sourcing | secundaria (universidad) | 2/2/2/1 | [S] |
| F12 | MIT Sloan Management Review, «Second Thoughts on Second Sourcing» | https://sloanreview.mit.edu/article/second-thoughts-on-second-sourcing | secundaria (revista) | 3/2/2/3 | [S] |
| F13 | NI Business Info, «Choosing suppliers for your business» | https://nibusinessinfo.co.uk/content/choose-between-single-or-multiple-supplier-strategy | secundaria (guía pública) | 1/1/1/1 | [S] |
| F14 | DHL, glosario OTIF | https://lot.dhl.com/glossary/on-time-in-full-otif/ | secundaria | 1/1/1/1 | [S] |
| F15 | Cardiff (Logistics Research Network 2021), errores en el cálculo de OTIF | https://orca.cardiff.ac.uk/id/eprint/147303/1/LRN%202021%20Final%20Paper.pdf | primaria (paper) | 2/2/2/3 | [S] |
| F16 | Trade.gov, «Know your Incoterms» (describe el texto de la ICC) | https://trade.gov/know-your-incoterms | secundaria | 2/1/1/1 | [S] |
| F17 | Krause, Handfield y Tyler (2007), J. of Operations Management 25: 525-548 | citado en https://scm.ncsu.edu/wp-content/uploads/sites/29/2017/12/rob-handfield-vita1.pdf | primaria (paper) | 3/-/-/3 | [M] solo la cita, sin abstract |
| F18 | CIPS, Supplier Appraisal (Knowledge Works, 2013) y SRM (2020) | https://udntho.files.cmp.optimizely.com/download/assets/Supplier_Appraisal.pdf/be3d1078b4ca11f08456a2ded5b57639 | primaria (cuerpo profesional) | 3/1/1/3 | [S] solo el inicio |
| F19 | ISMS.online sobre ISO 9001 cláusula 8.4 | https://www.isms.online/iso-9001/clause-8-4-control-of-externally-provided-processes-products-services/ | secundaria (consultora) | 1/1/1/1 | [S], no cita la norma literal |
| F20 | HBR, Kraljic (1983) | https://hbr.org/1983/09/purchasing-must-become-supply-management | primaria (paper) | 3/-/-/3 | [M] solo el primer párrafo |

## 1. proveedores (entrada)

- El registro del proveedor lleva varias direcciones y contactos (facturación, depósito, oficina) como registros enlazados, una cuenta bancaria por defecto para pagar, una plantilla de condición de pago y una categoría de proveedor definida por el usuario y anidable. Lo propio del proveedor gana sobre lo de su grupo y este sobre el valor por defecto de la empresa (F2).
- El registro admite bloquear facturas, pagos o ambos hasta una fecha (F2). Sin sistema, es una marca en la carpeta.
- Por qué uno solo: el auditor de Washington pide limpiar duplicados e inactivar los no usados al menos una vez al año (F4). El chequeo previo al alta por nombre, cuenta, dirección o contacto viene de otro resultado del buscador, no verificado en F4. Que un solo registro evite pagar dos veces y deje ver el gasto total es inferencia mía, sin fuente.
- El proveedor que también es cliente: sin fuente (hueco). Frontera con Datos/datos-maestros.
- Condición fiscal: F2 no mostró un campo de identificación tributaria; se resuelve en la nota argentina.

## 2. alta-de-proveedor

- Investigar antes de dar de alta: «You need a process to vet new vendors before you add them to your vendor master file»; pedir formularios fiscales, verificar el número tributario y la habilitación, buscar información externa (F4).
- Cambio de datos bancarios: verificar «directly with your vendor… by phone, using contact information that is known, reliable and already on file» (F4). «accounts payable clerks should not be able to add new vendors or change vendor information» (F4). La separación de funciones es de Contabilidad/Control-interno.
- Caso: existía una política de llamada de verificación y aun así se enviaron unos 3 millones de dólares a una cuenta equivocada tras un pedido de cambio por correo (F5, solo resumen del buscador; leer el PDF para confirmar monto y hechos).
- Una fuente comercial dice que la verificación manual depende de que alguien decida llamar y propone validar la titularidad de la cuenta (F6). Tiene interés comercial: es dato, no consejo.
- Calificación previa: Queensland la define como estrategia para bienes o servicios comprados con regularidad que son complejos, costosos o riesgosos, y sirve para detectar pronto a proveedores con poca solidez financiera (F8). USPS: relevamiento previo, revisión de registros financieros y evaluación en sitio de planta, instalaciones, personal, subcontratistas y otros recursos (F10). Nueva Zelanda: una lista de precalificados exige publicar las condiciones y cómo se verifican, y explicar por qué se saca a un proveedor (F9). Son guías del Estado usadas como práctica general, no como régimen legal.
- Lista de proveedores aprobados con definición propia: F9 y F10 son lo más cercano; no hallé fuente privada (hueco). Muestras: sin guía con método (hueco). ISO 9001 8.4: ver sección 4.

## 3. condiciones-del-proveedor

- Un sistema permite fijar proveedor y precio en la ficha del artículo para que se rellene en cada cotización; hay carga masiva de listas de precios (F3).
- Columnas por defecto de la solicitud de cotización: cantidad, precio unitario y plazo de entrega; se pueden activar el código de producto del proveedor y el descuento (F3). Prueba que esos datos existen en el registro artículo-proveedor.
- Plazo de entrega: la fecha esperada es la de confirmación del pedido más el plazo del proveedor (F3).
- Condición de pago: plantilla por proveedor, con prioridad proveedor, grupo, empresa (F2).
- Cantidad mínima: un hilo de foro (comunitario, versión 14/15) dice que la lista de precios se elige según si la cantidad alcanza el mínimo y si sigue vigente (F3). Sin fuente oficial. Unidad de compra y conversión, múltiplo, descuento por pronto pago: sin fuente (hueco).
- Incoterms como dato: la ICC los describe como reglas que definen el traspaso del riesgo, la asignación de costos y otras obligaciones entre vendedor y comprador; no definen el método ni el momento del pago ni cuándo pasa la propiedad (F16, secundaria; el texto de la ICC no se leyó). La importación es de Cadena de suministro.

## 4. evaluacion-de-proveedores

- Cuatro criterios en un tablero de sistema: aceptación de calidad = cantidad aceptada / recibida; confiabilidad de entrega = entregas a tiempo / entregas totales; respuesta a cotizaciones = respuestas en plazo / solicitudes enviadas; consistencia comercial = importe esperado frente al recibido (F1).
- Pesos: «The weights should total 100»; las épocas recientes pesan más que las viejas (F1). Estados de ejemplo: Preferred 85-100, Approved 70-84, Watch 50-69, Blocked por debajo de 50, configurables. Acciones: advertir (el comprador puede seguir) o bloquear nuevas solicitudes de cotización y órdenes (F1). Período semanal, mensual o anual (F1).
- Guía pública: máximo 10 indicadores y hasta 3 por métrica, definidos con el proveedor y los interesados internos; esfuerzo de revisión proporcional al de preparación; cadencia según segmento (F7).
- OTIF: porcentaje de pedidos entregados a tiempo y completos; ejemplo de DHL: 1.000 entregas, 950 a tiempo y completas, 95 % (F14). Depende de la unidad: un estudio de un proveedor dio 43 % por línea con tolerancia de un día (F15). Discrepancia abierta: si «a tiempo» es la fecha pedida por el comprador o la prometida por el proveedor (F15).
- PPM y precio como indicador: sin fuente (hueco). F1 calcula calidad como aceptado sobre recibido y no incluye precio.
- ISO 9001:2015 8.4 (evaluación, selección, seguimiento y reevaluación): solo resúmenes de consultoras, que dicen que los registros se volvieron más exigentes (F19). El texto literal no se leyó; la norma misma es la segunda fuente que falta.

## 5. relacion-con-proveedores

- Segmentación: por gasto y criticidad; primero el 80 % del gasto más los únicos o críticos; el resto, nivel 3 (F7). Nivel 1: únicos o personalizados con impacto significativo; nivel 2: críticos pero reemplazables, a un costo; nivel 3: transaccionales (F7). Para casos complejos pesan también el costo de cambiar, el gasto proyectado y la innovación (F7). Una sola fuente.
- CIPS define SRM como la gestión y el mantenimiento de la relación entre comprador y proveedor y trata la evaluación como tarea central; el detalle es de acceso para socios (F18).
- Kraljic (1983): solo se leyó el primer párrafo, que dice que la estabilidad de las áreas de compras estaba amenazada por escasez de recursos, intervención estatal, competencia y cambio tecnológico (F20). Las cuatro categorías no se leyeron; son de Abastecimiento-estratégico.
- Desarrollo de proveedores: cita de Krause, Handfield y Tyler (2007), «The relationship between supplier development, commitment, social capital accumulation and performance improvement», J. of Operations Management 25: 525-548 (F17); sin abstract. Krause (1999), por una reseña secundaria, vincula la disposición a desarrollar con la percepción de obligación del proveedor, la expectativa de que la relación dure y la comunicación operativa. Otro estudio, de otros autores, dice que sin capital relacional los beneficios no llegan de forma confiable; no atribuirlo a Krause.
- Único frente a varios: el único se asume de menor costo unitario y el múltiple reduce el riesgo de interrupción (arXiv 2210.11479, secundaria). Ventajas del único: integración y relación; desventaja: vulnerabilidad y dependencia asimétrica (F13). Caso citado: Ford, 1998, parada de tres días por un problema de proveedor (F11). MIT Sloan advierte que un segundo proveedor puede costar y aumentar algunos riesgos, y que proveedores de una misma región no reparten riesgo (inundaciones de Tailandia, 2011) (F12). Criterio común: criticidad del artículo, sustituibilidad y costo de una interrupción.
- El poder del proveedor como fuerza de la industria está en Estrategia-competitiva; solo frontera.

## Recursos canónicos propuestos

| Componente | Recurso | Qué parte y en qué fijarse |
|---|---|---|
| proveedores | ERPNext Supplier y Supplier Group (F2) | Lista de campos y regla de prioridad proveedor > grupo > empresa; se sostiene como ficha de papel |
| alta-de-proveedor | Washington SAO (F4) y USPS/NZ (F10, F9) | Los cuatro controles de F4 y los pasos de calificación de F10, juntos |
| condiciones-del-proveedor | Odoo RFQ y lead times (F3) | Qué columnas lleva un renglón de condición; leer la documentación viva |
| evaluacion-de-proveedores | ERPNext Supplier Scorecard (F1) y NSW (F7), con ISO 9001 8.4 | Fórmulas y estados de F1; el tope de indicadores de F7 |
| relacion-con-proveedores | NSW (F7) y MIT Sloan (F12) | Segmentación en tres niveles y el matiz sobre el segundo proveedor |

## Huecos

- Sin leer: ISO 9001:2015 8.4 (texto), Kraljic 1983 completo, van Weele, Monczka et al., textos de CIPS e ISM, Krause et al. 2007, ACFE (el buscador no devolvió nada), texto oficial de Incoterms 2020.
- Sin fuente: proveedor que también es cliente; unidad de compra y conversión; múltiplo de compra; descuento por pronto pago; lista de proveedores aprobados como concepto definido; PPM; muestras en la homologación; precio como indicador; ISO 20400.
- Lo de alto riesgo (fraude de proveedor ficticio y cambio de cuenta) tiene F4 y F5, independientes entre sí, pero ambas de Estados Unidos y F5 solo como resumen; monto del caso no verificado.
- Frappe y Odoo prueban que la práctica existe, no que sea la regla del campo.

## Sobre el árbol

La división en cinco notas coincide con cómo el campo divide el tema. Dos ajustes posibles: (1) el bloqueo de un proveedor aparece en alta, evaluación y registro; definirlo una vez en alta-de-proveedor y enlazarlo; (2) único frente a varios roza la matriz de Kraljic de Abastecimiento-estratégico: dejar en relacion-con-proveedores la decisión por proveedor y enlazar la matriz para la decisión por categoría.
