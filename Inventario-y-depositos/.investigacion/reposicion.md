# Reposición: investigación cruda

Fecha de lectura: 2026-11-27. Marcas: [L] texto completo leído, [M] metadatos o abstract, [S] resumen secundario o del buscador. Puntajes 1 a 3 en autoridad / profundidad / ejemplos / unicidad.

Aviso de método: el lector de páginas devolvió resúmenes, no el texto. Para las dos clases del MIT bajé el PDF y lo pasé por pdftotext, así que esas dos sí son [L]. Las fórmulas del MIT salen literales de ahí; donde el PDF perdió el signo de raíz cuadrada lo marco. El presupuesto de búsqueda se agotó en la tercera ronda: la crítica al EOQ y el texto de Harris quedaron sin leer.

## Fuentes

| # | Fuente | URL | Tipo | Aut/Prof/Ej/Uni | Marca |
|---|---|---|---|---|---|
| F1 | Caplice, C. (MIT CTL), *Inventory Management: Probabilistic Demand*, ESD.260 lección 11, oct. 2006 (diapositivas; remite a Silver, Pyke y Peterson, «SPP», como libro de texto) | https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/8b53c45fd26ffff706d815131e8d177e_lect11.pdf | primaria (material de curso basado en un libro de texto) | 3/2/3/2 | [L] |
| F2 | Caplice, C., *Inventory Management: More Probabilistic Demand*, ESD.260 lección 12, oct. 2006 | https://ocw.mit.edu/courses/esd-260j-logistics-systems-fall-2006/bc18dd1b2543535a61f826d00a8c6e42_lect12.pdf | primaria (ídem) | 3/2/3/2 | [L] |
| F3 | Wikipedia, *Economic order quantity* | https://en.wikipedia.org/wiki/Economic_order_quantity | secundaria | 1/2/3/1 | [S] |
| F4 | Erlenkotter, D. (2014), «Ford Whitman Harris's economical lot size model», *Int. J. Production Economics* 155: 12-15, DOI 10.1016/j.ijpe.2013.12.008 | https://ideas.repec.org/a/eee/proeco/v155y2014icp12-15.html | primaria (historia del campo) | 3/1/1/3 | [M] |
| F5 | Hammond y Western Technical College, *Operations Management*, §6.8 (CC BY 4.0) | https://biz.libretexts.org/Courses/Western_Technical_College/Operations_Management_(Hammond)/06%3A_Supply_Chain_and_Inventory_Management/6.08%3A_Measuring_Supply_Chain_Performance | secundaria (libro de texto abierto) | 2/2/3/1 | [S] |
| F6 | DeHoratius y Raman (2008), «Inventory Record Inaccuracy: An Empirical Analysis», *Management Science* 54(4): 627-641, DOI 10.1287/mnsc.1070.0789 | https://econpapers.repec.org/RePEc:inm:ormnsc:v:54:y:2008:i:4:p:627-641 | primaria (estudio empírico) | 3/1/2/3 | [M] |
| F7 | Wikipedia, *ABC analysis* | https://en.wikipedia.org/wiki/ABC_analysis | secundaria | 1/2/2/1 | [S] |
| F8 | Trusted Institute, «Inventory Planning Fundamentals and Functions» (preparación CPIM) | https://trustedinstitute.com/concept/cpim/inventory-management/inventory-planning-fundamentals/ | secundaria, comercial; no cita el Diccionario APICS | 1/1/1/1 | [S] |
| F9 | Mecalux Interlake, «ABC XYZ analysis» | https://www.interlakemecalux.com/blog/abc-xyz | secundaria, de un fabricante de estanterías | 1/1/1/1 | [S] (solo buscador) |
| F10 | SCM Dojo, guía ABC-XYZ | https://www.scmdojo.com/blog/abc-xyz-analysis-complete-guide/ | secundaria | 1/1/1/1 | [S] (solo buscador) |
| F11 | Material de curso IEOR sobre XYZ | https://neoprimate.github.io/IEOR/supply-chain/classification/xyz/index.html | secundaria | 1/1/1/1 | [S] (solo buscador) |
| F12 | ASCM, «The XYZs of inventory management» | https://www.ascm.org/ascm-insights/the-xyzs-of-inventory-management | primaria (organismo del campo) | 3/?/?/? | no leída: la página vino vacía |

Independencia: F9, F10 y F11 son fuentes distintas con umbrales distintos. F8 enumera las «funciones del inventario» pero no es el Diccionario APICS.

## 1. Funciones y costos del inventario

- Funciones según el material de preparación CPIM (F8, secundaria): anticipación, ciclo, seguridad, cobertura (hedge), transporte (pipeline), desacople y fluctuación. Literales: anticipación, «Inventory built up in advance to meet expected increases in demand»; ciclo, «The portion of inventory that results from ordering or producing in lots or batches»; transporte, «Inventory that is currently in transit between locations in the supply chain»; desacople, «Inventory held between stages of a production process or supply chain»; fluctuación, «Inventory carried to cover random, unpredictable variations in supply and demand». URL: F8.
- Divergencia: el árbol del brief lista cinco (ciclo, seguridad, anticipación, tránsito, desacople); F8 suma hedge y fluctuación (casi sinónimo de seguridad). Una búsqueda atribuyó al CPIM Learning System seis (anticipación, hedge, ciclo, fluctuación, transporte, repuestos de servicio), solo de forma secundaria. Falta el Diccionario APICS para fijar la lista.
- Costos: pedir o preparar, mantener y faltante (F8). Mantener se expresa como porcentaje anual del valor; F8 dice «often 20-35% annually» (un solo dato secundario). F8 lo desglosa en capital, almacenaje, riesgo (obsolescencia, rotura, hurto) y seguros e impuestos. El MIT usa r = 10 % en sus ejemplos (F1, diap. 18 y 29): es un dato de ejemplo, no del campo.
- Costos relevantes en el MIT: «TRC = OrderCosts + HoldingCosts + StockOutCosts», con TRC = A(D/Q) + (Q/2 + kσL)vr + B1(D/Q)p_u≥(k) (F1, diap. 25). Notación: A = costo por pedido, v = costo unitario, r = tasa de mantenimiento, D = demanda anual (F1, diap. 11 y 18).

Recurso canónico propuesto: Silver, Pyke y Thomas, cap. 1-2 (por qué hay inventario y estructura de costos); no leído. Mientras, F1 diap. 10-12.

## 2. Punto de pedido y sistemas de revisión

Literales de F1 (diap. 5-9):
- Notación: «s = Order Point, S = Order-up-to Level, L = Order Lead Time, Q = Order Quantity, R = Review Period, IOH = Inventory on Hand, IP = Inventory Position = (IOH) + (Inv On Order) – (Backorders) – (Committed)».
- Continua (R=0): «Order-Point, Order-Quantity (s, Q). Policy: Order Q if IP ≤ s. Two-bin system». «Order-Point, Order-Up-To-Level (s, S). Policy: Order (S-IP) if IP ≤ s. Min-Max system».
- Periódica (R>0): «Order-Up-To-Level (R, S). Policy: Order S-IP every R time periods. Replenishment cycle system». Híbrido «(R, s, S) System. Policy: Order S-IP if IP ≤ s every R time periods, if IP>s then do not order».
- Regla práctica (F1, diap. 8, «No hard and fast rules, but some rules of thumb»): artículos A: (s, S) continua o (R, s, S) periódica; B: (s, Q) o (R, S); C: manual ~ (R, S).
- Continua frente a periódica (F1, diap. 5): la continua es «Able to provide same level of service with less safety stock»; la periódica permite «Coordination of replenishments» y «Able to predict workload».
- Punto de pedido: «s = xL + kσL» (F1, diap. 9): demanda pronosticada durante el plazo más stock de seguridad; k es el factor de seguridad y σL el RMSE del pronóstico en el plazo.
- Frontera: el inventory position resta lo comprometido; el cálculo de lo disponible (ATP) es de este tema, ya citado en fecha-prometida.md.

Recurso canónico: F1 diap. 5-9 para el vocabulario y las cuatro políticas.

## 3. Lote económico (EOQ)

- Fórmula (F3, secundaria): Q* = √(2DK/h); costo total T = PD + KD/Q + hQ/2; D demanda anual, K costo fijo por pedido, h costo anual de mantener por unidad, P precio unitario. «Q* is independent of P; it is a function of only K, D, h» (la raíz se perdió en la extracción; la reconstruyo).
- Ejemplo de F3: D = 10.000; K = 40; P = 50; h = 4 + 50×2 % = 5; EOQ = √(2·10.000·40/5) = 400 unidades, 25 pedidos al año; costo total en el EOQ 502.000; a 500 unidades 502.050; a 300, 502.083,33. Muestra lo plano que es el costo cerca del óptimo.
- Ejemplo del MIT (F1, diap. 18): «EOQ = 228 units (A=50 $/order, r=10%, v=250 $/item)», con D = 13.000 al año. Verificado: √(2·50·13.000/(0,10·250)) = √52.000 ≈ 228. El MIT no escribe la fórmula en esas diapositivas; usa el resultado.
- Historia: Harris publicó el modelo en febrero de 1913 en la revista *Factory* (F4); el buscador dio el título «How many parts to make at once», 10(2): 135-136 (dato de segunda mano). F4: la fórmula es «one of the most cited and applied results in production and operations management» y el artículo quedó olvidado muchos años. Discrepancia: otros trabajos de Erlenkotter (1989, 1990) hablan del modelo «de 1915»; F3 atribuye la aplicación extensa a R. H. Wilson. Para zanjar fechas hay que leer a Harris o a Erlenkotter 1990.
- Supuestos y críticas (solo F3, secundaria): «EOQ applies only when demand for a product is constant over a period of time»; cada pedido llega completo cuando el stock llega a cero; costo fijo por pedido y un solo artículo por pedido; se lo criticó por «their restrictive set of assumptions»; Cargal sostiene que se armó para cálculo a mano y que las planillas permiten supuestos más realistas. La crítica lean/JIT (bajar el costo de preparación en vez de optimizar el lote) y la insensibilidad del óptimo no pude fuentearlas: hueco.
- Puente a periódica (F2, diap. 5): (s,Q) pasa a (R,S) con s → S, Q → D·R, L → R+L.

Recurso canónico: Harris 1913 (no leído) con Erlenkotter 2014 como guía; para el uso, F1 diap. 11 y 18.

## 4. Stock de seguridad

Literales de F1 y F2 (leídos):
- Nivel de servicio por ciclo (CSL, P1): «Probability of no stockouts per replenishment cycle. Equal to one minus the probability of stocking out. = 1 – P[Stockout] = 1- P[xL > s] = P[xL ≤ s]» (F1, diap. 13). Para una normal: «CSL=NORMSDIST(k)»; «CSL=NORMDIST(s, xL, σL, 1) where s=xL+kσL» (F1, diap. 16).
- Fill rate (P2): «Fraction of demand filled from IOH» (F1, diap. 20). «FillRate = (OrderQuantity − E[UnitsShort]) / OrderQuantity»; «IFR = (Q − E[US])/Q = 1 − E[US]/Q = 1 − σL G[k]/Q»; «G[k] = (Q/σL)(1 − IFR)» (F1, diap. 20 y 23).
- Faltante esperado: para normal «E[US] = σL G(k)», con G(k) la función de pérdida normal unitaria: «G(k) = Gu(k) = fx(xO)-k*Prob[xO≥k]»; en Excel «NORMDIST(k,0,1,0) – k(1 - NORMDIST(k,0,1,1))» (F1, diap. 22).
- «IFR usually much higher than CSL for same SS. IFR depends on both s and Q while CSL is independent of all product characteristics» (F1, diap. 24). Tabla de F1 (ejemplo de 13.000 al año), stock de seguridad según CSL y según IFR: 99 %: 601 y 513; 95 %: 423 y 348; 90 %: 330 y 252; 80 %: 217 y 148.
- Cambio de escala de tiempo (F1, diap. 19): «E[L] = nE[S]; VAR[L] = nVAR[S] so that σL = √n σS».
- Con costo de faltante (F1, diap. 25-28): por evento, regla «DB1/(√(2π) Q v σL r) < 1» entonces k mínimo; si no, «k = √(2 ln(DB1/(√(2π) Q v σL r)))». Por unidad faltante, «p_u≥(k) = Qr/(D B2)» (ec. 7.23). Los radicales se perdieron en la extracción y los reconstruí: verificar contra SPP, ecs. 7.19 y 7.20.
- Ejemplo numérico del MIT (F1 diap. 18; F2 diap. 3): demanda 13.000 por año ~ iid normal, plazo 2 semanas, RMSE del pronóstico 1.316 por año, EOQ 228; «σL=258 units and μL=500 units» (F2). Verificado: 13.000·2/52 = 500; 1.316/√26 = 258,1. Con CSL 95 %, k = 1,645 y SS ≈ 424 (F1 da 423).
- Ejemplo con revisión periódica (F2, diap. 6), R = 8 semanas, IFR = 0,95: «Q becomes D*R or (13000)(8/52) = 2000 units; xL becomes xR+L=(13000)/(52/10) = 2500 units; σL becomes σR+L = 1316/(√(52/10) = 577 units. So Gu[k] = (1-.95)(2000/577) = 0.1733 giving k=0.58. S = xR+L + kσR+L = 2500 + (.58)(577) = 2835 units. Policy becomes order up to 2835 units every 8 weeks.» Verificado: 0,05·2000/577 = 0,1733.
- Plazo variable: F1 y F2 suponen plazo fijo y trabajan con el RMSE del pronóstico en el plazo. Un resumen del lector dio σ = √(L σd² + d² σL²) como conocimiento general, pero no figura en F1 ni F2: no usar sin fuente. Hueco.
- Exactitud del registro: F6 informa que 65 % de casi 370.000 registros de 37 tiendas de un minorista estaban inexactos (abstract resumido por el lector); el modelo clásico lo ignora. Las fórmulas de arriba suponen un registro exacto.

Recurso canónico: Silver, Pyke y Thomas, capítulo de sistemas de punto de pedido (no leído); mientras, F1 diap. 9-24 y F2 diap. 3-6 con sus ejemplos.

## 5. Clasificación ABC y XYZ

- ABC: «The ABC concept is based on Pareto's law» (F7). Clases: A «very tight control and accurate records»; B «less tightly controlled and with moderate records»; C «the simplest controls possible and minimal records». «There are no fixed thresholds for each class.» Ejemplos de F7: 20 %/30 %/50 % de los artículos con ~70 %/25 %/5 % del valor anual de consumo; o 10 %/20 %/70 % con 66,6 %/23,3 %/10,1 %. Método de F7 en cinco pasos: valor anual de uso, ordenar, acumular, pasar a porcentajes, graficar.
- Uso en F1 (diap. 4): A «Require the most managerial attention and review»; C «Control systems should be as simple as possible»; y la advertencia «But – these are arbitrary classifications».
- XYZ por variabilidad de la demanda: coeficiente de variación, desvío sobre media (F9). Umbrales en discrepancia: F9, X ≤ 10 %, Y 10-25 %, Z > 25 %, adaptables a cada empresa; F11, X < 0,5, Y < 1,0, Z ≥ 1,0; F10, X < 0,5, Y 0,5-1,0. No son estándar. La fuente primaria (F12) no cargó. Hueco: XYZ es práctica de proveedores y blogs; no hallé texto de libro.

Recurso canónico: F7 para ABC; para XYZ, F12 cuando se pueda leer.

## 6. Indicadores

- Rotación: «Inventory turnover formula (cost of goods sold divided by average aggregate inventory value)». Ejemplo: 17.550.000 / 1.650.000 = 10,64 vueltas; 16.255.000 / 1.763.350 = 9,22 (F5).
- Días de inventario: «Days of supply formula (average aggregate inventory value divided by annual cost of goods sold, the sum of which is multiplied by 365)». Ejemplo: (3.025.600 / 45.000.000) × 365 = 24,54 días (F5).
- Nivel de servicio: dos definiciones literales en F1 (sección 4). F1 aclara que «Definitions in practice are fuzzy» (diap. 10).
- Exactitud: APQC PCF 4.4.3.5 «Track inventory accuracy» (apqc-4.txt, línea 121); F6 mide la inexactitud. Fórmula de exactitud de registros: sin fuente leída.
- SCOR: scor6.txt local solo trae procesos, no métricas de inventario. «Inventory days of supply» (AM.2.2 según un secundario) no la leí de SCOR. Los secundarios discrepan en qué mide (basada en COGS, o cobertura de la demanda futura); no leí ninguna de primera mano.
- Cobertura y obsolescencia: sin fuente.

## Recursos canónicos (resumen)

1. Caplice, ESD.260 lecciones 11 y 12 (F1, F2): vocabulario, políticas, fórmulas de s, S y fill rate, dos ejemplos con cuentas. Fijarse en que CSL y fill rate dan stocks distintos para el mismo porcentaje.
2. Silver, Pyke y Thomas, *Inventory and Production Management in Supply Chains*, libro base de F1; no pude leerlo y es la fuente a citar para las fórmulas.
3. Harris (1913) con Erlenkotter (2014) para el EOQ.
4. Libro abierto Hammond (F5) para los indicadores básicos.

## Si la división del árbol no coincide con el campo

El campo trata stock de seguridad y nivel de servicio como un solo problema con el punto de pedido (s = xL + kσL); conviene que las notas los enlacen estrechamente. El EOQ aparece como un paso de la política (s,Q), no como tema aparte. La lista de funciones del inventario depende del Diccionario APICS, sin verificar.

## Huecos

- Diccionario APICS: funciones, ABC, punto de pedido, stock de seguridad. No leído.
- Texto de Harris 1913 no leído; 1913 frente a 1915 pendiente (Erlenkotter 1990).
- Crítica al EOQ (lean/JIT, insensibilidad del óptimo, descuentos, demanda variable): solo la mención de F3.
- Stock de seguridad con plazo variable: sin fuente leída.
- Umbrales ABC y XYZ: solo secundarias.
- Exactitud de registros: fórmula e índices sin fuente; F6 solo por abstract.
- Rotación y días de inventario: solo un libro abierto; falta SCOR o APICS. Cobertura y obsolescencia: nada.
- Ecuaciones 7.19 y 7.20 con radicales reconstruidos.
- Software (ERPNext, Odoo, Dynamics, EWM): no consultado para este ángulo.
