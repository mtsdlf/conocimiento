---
resumen: >-
  Las tasas de descubierto, plazo fijo, caución y descuento de cheques, y la inflación pasada y esperada en Argentina a fines de noviembre de 2026, cada una con su fecha y su fuente viva, y la tasa real que resulta de compararlas.
estado: vigente
estabilidad: volatil
fuentes:
  - "BCRA, API de Estadísticas Monetarias v4.0, valores al 25 y 26/11/2026, inflación a octubre de 2026 (leído): https://api.bcra.gob.ar/estadisticas/v4.0/monetarias"
  - "BCRA, Boletín Estadístico de octubre de 2026, índice de series, punto 1.1.3, para la definición de la serie de adelantos (leído en esa parte): https://www.bcra.gob.ar/archivos/Pdfs/PublicacionesEstadisticas/BoletinEstadistico/boldat202610.pdf"
  - "MAV, portada con Datos de Mercado, 26/11/2026 (las tablas leídas; el rótulo de cada pestaña y la unidad de la tasa, según su resumen): https://www.mav-sa.com.ar/"
  - "Banco Provincia, Tasas de uso judicial e históricas de consulta frecuente, actualizado al 2/11/2026, cuadro IV (leído): https://www.bancoprovincia.com.ar/CDN/Get/tasas_frecuentes"
  - "Tesoreria/.investigacion/argentina.md, secciones 3 y 4 (2026-11-27)"
  - "Tesoreria/.investigacion/argentina-y-fundamentos-verificacion.md (2026-11-27)"
aliases: [tasas de referencia, tasas en Argentina, tasa de descubierto, tasa de plazo fijo, BADLAR, TAMAR, tasa de caución, inflación interanual, REM, tasa real, Argentine reference rates]
creado: 2026-11-27
revisado: 2026-11-27
---

# Tasas de referencia en Argentina

Las tasas de descubierto, plazo fijo, caución y descuento de cheques, y la inflación pasada y esperada en Argentina a fines de noviembre de 2026, cada una con su fecha y su fuente viva, y la tasa real que resulta de compararlas.

Implementa [tesorería en Argentina](tesoreria-en-argentina.md), que explica cada instrumento. Los valores cambian por semana: copiados de la API de estadísticas del BCRA y de la portada del MAV el 2026-11-27. Para actualizarlos, la fuente viva de las tasas bancarias y la inflación es la [API de estadísticas monetarias del BCRA](https://api.bcra.gob.ar/estadisticas/v4.0/monetarias), y la del mercado de capitales, los Datos de Mercado de la [portada del MAV](https://www.mav-sa.com.ar/).

## Tasas para quien toma plata

| Tasa | Valor | Fecha | Fuente |
|---|---|---|---|
| Adelantos en cuenta corriente a empresas (el nombre bancario del descubierto), con acuerdo de 1 a 7 días, por $ 10 millones o más (serie 13) | 25,69 % TNA | 25/11/2026 | BCRA, API |
| Descubierto de empresas en la lista de un banco público provincial: con reciprocidad (la empresa le trae al banco sueldos, cobros u otros negocios) / resto / exceso sin acuerdo | 57,00 % / 65,00 % / 84,13 % TNA vencida | vigente desde 1/11/2026 | Banco Provincia, tabla actualizada al 2/11/2026 |
| Descuento de ECHEQ avalado a 15 días: mínima, máxima, promedio | 22,98 % / 28,00 % / 26,00 % | 26/11/2026 | MAV |
| Descuento de ECHEQ avalado a 60 días: mínima, máxima, promedio | 22,99 % / 28,00 % / 25,81 % | 26/11/2026 | MAV |
| Descuento de ECHEQ avalado a 90 días: mínima, máxima, promedio | 24,00 % / 31,00 % / 25,54 % | 26/11/2026 | MAV |
| Descuento de ECHEQ no garantizado a 13 días: mínima, máxima, promedio | 23,00 % / 40,00 % / 28,69 % | 26/11/2026 | MAV |

> [!IMPORTANT]
> El descubierto tiene dos cifras que no se contradicen pero no son la misma tasa. La serie del BCRA promedia adelantos de $ 10 millones o más, acordados a 1 a 7 días: es la tasa de una empresa grande. La lista de un banco público provincial, leída en su tabla de noviembre de 2026, da 57 % con reciprocidad y 65 % en el resto de los casos, y 84 % para el exceso sobre el acuerdo: se acerca más a lo que paga una pyme que gira sin negociar. La búsqueda había dado 62 % y 70 %, que eran los valores de febrero de 2026; la tabla es una serie histórica y los de noviembre son otros. Que para una pyme la referencia sea la lista de su banco es lectura de esta base.

Las tablas del MAV no rotulan la unidad de la tasa ni separan con claridad las pestañas (ECHEQ, pagarés, facturas); que la primera tabla sea la de ECHEQ y que las tasas sean nominales anuales se lee del orden de magnitud y de su resumen, no del texto. El segmento pesa: a 13 días, el no garantizado fue de 23 % a 40 %, y en el segmento de inversor calificado, con dos cheques, el promedio fue 46 %. Como contraste, un reporte del MAV citado en su portada daba en septiembre de 2025 una tasa promedio de 51,66 % para los cheques avalados (según su resumen). Entre las dos fechas la tasa del avalado bajó a cerca de la mitad, aunque las dos cifras no son series idénticas (un promedio mensual y una tabla de un día por plazo).

## Tasas para quien coloca plata

| Tasa | Valor | Fecha | Fuente |
|---|---|---|---|
| Depósitos a plazo fijo a 30 días | 20,56 % TNA | 25/11/2026 | BCRA, API |
| BADLAR de bancos privados (depósitos de $ 1 millón o más) | 21,9375 % TNA | 25/11/2026 | BCRA, API |
| TAMAR de bancos privados (depósitos de $ 1.000 millones o más) | 23,4375 % TNA / 26,11 % TEA | 25/11/2026 | BCRA, API |
| Pases entre terceros a 1 día (préstamos de un día con títulos como garantía) | 20,52 % TNA | 25/11/2026 | BCRA, API |
| Caución en pesos a 1 día: mínima, máxima, última | 15,00 % / 24,00 % / 16,01 % | 26/11/2026, vence 27/11 | MAV |
| Caución en pesos a 7 días, última | 20,00 % | 26/11/2026, vence 03/12 | MAV |
| Caución en dólares a 1 día / a 14 días, última | 1,10 % / 3,00 % | 26/11/2026 | MAV |

El plazo fijo de la tabla es un promedio del sistema: la tasa de una empresa depende del monto y del banco. Las cauciones del MAV tampoco rotulan la unidad. Los fondos comunes money market no tienen fila porque no se pudo leer su rendimiento.

## Inflación y otros valores de la misma fecha

| Dato | Valor | Fecha | Fuente |
|---|---|---|---|
| Inflación mensual | 2,2 % | octubre de 2026 | BCRA, API |
| Inflación interanual | 33,1 % | octubre de 2026 | BCRA, API |
| Inflación esperada a 12 meses, mediana del REM (Relevamiento de Expectativas de Mercado del BCRA) | 21,8 % | 31/10/2026 | BCRA, API |
| UVA (unidad de valor adquisitivo, ajustada por inflación) | $ 2.216,40 | 27/11/2026 | BCRA, API |
| Tipo de cambio mayorista de referencia | $ 1.600,6872 | 26/11/2026 | BCRA, API |
| Tipo de cambio minorista, vendedor | $ 1.628,75 | 26/11/2026 | BCRA, API |

## La tasa real del plazo fijo y del descubierto

La tasa real descuenta la inflación de una tasa efectiva; la fórmula está en [costo del financiamiento](Financiamiento/costo-del-financiamiento.md). La cuenta es de esta base, con capitalización cada 30 días para las dos tasas:

| Tasa | Tasa efectiva anual | Real con la inflación pasada (33,1 %) | Real con la esperada (21,8 %) |
|---|---|---|---|
| Plazo fijo a 30 días, 20,56 % TNA | 22,6 % | −7,9 % | +0,7 % |
| Adelanto a empresas, 25,69 % TNA | 28,9 % | −3,1 % | +5,9 % |

El signo depende de qué inflación se use. Mirando atrás, quien colocó a plazo fijo perdió y quien tomó un adelanto pagó menos que la inflación. Mirando adelante con la expectativa del REM, el plazo fijo apenas empata y el adelanto cuesta casi 6 % real. Las tasas del MAV no entran en la cuenta porque su unidad no está rotulada.
