# Tercera ronda: búsquedas puntuales de quien escribe

Fecha: 2026-11-27. Búsquedas hechas por la sesión que arma el tema para tapar los huecos más grandes que dejaron las dos primeras rondas. Las marcas: [L] página leída con WebFetch (resumen de un modelo chico con cita pedida), [S] resultado del buscador. Todo lo que dice "según el buscador" es [S].

## Curva P-F

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Kevin Clark, CMRP, «Improving maintenance by adopting a P-F curve methodology», *InTech* (ISA), marzo/abril de 2019: https://www.isa.org/intech-home/2019/march-april/features/improving-maintenance-by-adopting-a-p-f-curve-meth | secundaria (practicante, revista de la ISA) | 2 | 2 | 1 | 2 | [L] |

- «Potential failure (PF) indicates a detectable state of failure, or the point at which degradation begins.»
- «Functional failure (FF) is when the asset or component has reached a failed state or no longer performs satisfactorily.»
- El intervalo P-F «represents the time between when potential failure is detected in an asset» y el estado de falla.
- «The method and frequency of detection essentially determine the length of the P-F interval.»
- Cita a John Bernet: «The P-F curve is a conceptual representation only and does not have any units or scale.»
- No nombra a Moubray ni a Nowlan y Heap.
- Según el buscador [S], varias fuentes secundarias atribuyen el término a John Moubray (Aladon); un glosario de un proveedor da como regla práctica inspeccionar a la mitad del intervalo P-F, que no es una regla de Moubray (https://tractian.com/en/glossary/p-f-curve-potential-failure-curve). Una crítica en Scribd sostiene que la curva no representa el preventivo por edad ni el dejar fallar.

## Nowlan y Heap (1978): los seis patrones

| Fuente | Tipo | A | P | E | U | Marca |
|---|---|---|---|---|---|---|
| Nowlan y Heap, *Reliability-Centered Maintenance*, United Airlines para el Departamento de Defensa, 29 de diciembre de 1978, DTIC ADA066579: https://apps.dtic.mil/sti/pdfs/ADA066579.pdf | primaria | 3 | 3 | 3 | 3 | no leído (DTIC devuelve HTML a curl y 403 al fetch) |
| Reliable Media, «The Six Failure Patterns: Nowlan and Heap Explained», 1 de septiembre de 2026 (actualizado el 13 de octubre de 2026): https://reliamag.com/topics/guides/six-failure-patterns-nowlan-heap/ | secundaria | 2 | 2 | 2 | 2 | [L] |

Según Reliable Media, que resume la Exhibit 2.13 del informe:
- A: bañera (mortalidad infantil, tramo plano, desgaste). 4 %.
- B: probabilidad constante o en leve aumento y desgaste marcado al final. A y B juntos: 6 % con desgaste marcado.
- C: aumento gradual sin edad de desgaste identificable. 5 %.
- D: baja de nuevo, sube rápido a un nivel constante. E: constante a toda edad. F: mortalidad infantil alta y después constante o casi.
- «Some 89 percent of the items analyzed had no wearout zone at all.»
- «The 4, 6, 5, and 89 percent figures are the percentage of United Airlines items in Exhibit 2.13»; «not a number you can drop into your own asset register without analysis».
- La NASA usa otro orden de letras: «in NASA's scheme the bathtub is Type E, while in Nowlan's it is Pattern A». El resumen de la NASA de tres estudios pone las fallas aleatorias entre 77 y 92 %.
- Discrepancias según el buscador [S]: una página de un proveedor reparte el 89 % entre D, E y F y da 2 % a A (https://oxmaint.com/industries/aviation-management/why-airport-asset-age-fails-reliability-predictor-best-cmms); AvWeb da 72 % de componentes no estructurales sin patrón de edad (https://avweb.com/features_old/the-savvy-aviator-47-reliability-centered-maintenance-part-1/).

## SAP PM: aviso, orden y estados

Según el buscador [S]:
- La documentación de SAP dice que una orden en TECO (técnicamente concluida) todavía admite la liquidación de costos, y que CLSD (cerrada) es final y bloquea la orden: https://help.sap.com/doc/saphelp_sfin100/1.9/en-US/88/16295411158c24e10000000a4450e5/content.htm
- La orden se libera (REL) cuando tiene la información necesaria; el aviso se crea con el estado «aviso pendiente» (Outstanding notification): https://help.sap.com/saphelp_46c/helpdata/en/de/957177415611d1893d0000e8323c4f/content.htm
- Los avisos asignados a una orden pueden seguir el estado de la orden: https://help.sap.com/doc/b183ce53118d4308e10000000a174cb4/700_SFIN3E%20006/en-US/238bb6535fe6b74ce10000000a174cb4.html
- CRTD (creada) no apareció en una fuente leída: es conocimiento general del buscador, no citado.

## Planificación y programación (Palmer)

Según el buscador [S]:
- El tiempo de herramienta (wrench time) típico de una planta, aun una buena, ronda el 35 %, y Palmer apunta a cerca de 55 % con planificación y programación (55/35 = 1,57, un aumento de 57 %). Fuentes: columna «Palmer's Planning Corner», Plant Services: https://www.plantservices.com/voices/palmers-planning-corner/article/55361071/do-you-know-the-purpose-and-principles-of-maintenance-planning-and-scheduling ; https://plantservices.com/planned-maintenance/planning-and-scheduling/article/11295301/understanding-the-math-of-maintenance-planning-and-scheduling
- Principios de planificación de Palmer, resumidos: planificadores en un departamento separado de las cuadrillas; los planificadores se ocupan del trabajo futuro; archivos simples y seguros a nivel de equipo; retroalimentación de los técnicos; evitar las trampas que impiden planificar todo; medir el desempeño, con el tiempo de herramienta como medida principal de eficiencia.
- Principios de programación, resumidos: trabajo planificado, un sistema de prioridades creíble, un horizonte de una semana, programas cargados al 100 % de las horas disponibles, programación diaria por el supervisor y cumplimiento del programa entre 40 y 90 %.
- El pendiente planificado es requisito para programar: https://reliableplant.com/Articles/Print/7051?id=7051
- No se encontró fuente para un rango de pendiente en semanas.

## Resolver en la primera visita (first-time fix)

Según el buscador [S]:
- Definición: proporción de trabajos terminados en la primera visita, sin visita de seguimiento, repuestos adicionales ni ayuda externa; trabajos resueltos en la primera visita sobre trabajos completados: https://ibm.com/think/topics/first-time-fix-rate
- Cifras atribuidas a Aberdeen Group por blogs de proveedores, que no coinciden entre sí: 88 % los mejores, 80 % el promedio y 63 % los rezagados (PTC: https://www.ptc.com/en/blogs/service/what-is-first-time-fix-rate); un promedio de cerca de 75 % (https://aexinc.com/blog/how-to-increase-first-time-fix-rates). El informe original de Aberdeen no se encontró.
- Un informe de un proveedor (Aquant, 2026, unos 30 millones de eventos de servicio) da 77 % según CustomerThink: https://customerthink.com/?p=1080461
