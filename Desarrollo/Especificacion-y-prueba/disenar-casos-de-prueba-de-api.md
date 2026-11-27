---
resumen: >-
  Cómo armar la suite de casos de prueba de una API REST: el formato de cada caso y la lista de
  categorías que hay que cubrir, del camino feliz a la concurrencia.
estado: borrador
estabilidad: semi
revisado:
creado: 2026-10-03
fuentes:
  - "RFC 9110, HTTP Semantics, 15. Status Codes: https://www.rfc-editor.org/rfc/rfc9110.html#section-15"
  - "RFC 6585, Additional HTTP Status Codes, 4. 429 Too Many Requests: https://www.rfc-editor.org/rfc/rfc6585.html#section-4"
  - "Archivo/Desarrollo/casos-de-prueba-api.md (original; sus casos 012 y 023 dicen 400 Conflict, que es 409)"
aliases: [Casos de prueba de API, Test cases API REST, Suite de pruebas de API]
---

# Diseñar casos de prueba de una API

Cómo armar la suite de casos de prueba de una API REST: el formato de cada caso y la lista de
categorías que hay que cubrir, del camino feliz a la concurrencia.

## El contrato, las historias y las categorías propias

- Tener el contrato de la API (OpenAPI o equivalente) y los criterios de aceptación de cada
  [Historia de usuario](historia-de-usuario.md).
- Si la API es multi-tenant o acepta reintentos, entender [Multi-tenancy](../../Arquitectura/Sistemas-distribuidos/multi-tenancy.md) y
  [Clave de idempotencia](../../Arquitectura/Sistemas-distribuidos/clave-de-idempotencia.md): generan categorías propias.

## Formato, categorías, ambigüedades y efectos

1. **Escribí cada caso con el mismo formato**, en una tabla por endpoint:

   | Campo | Contenido |
   |---|---|
   | ID | `CAT-PROD-014`: prefijo de la API, recurso y número |
   | Título | qué se prueba, en una línea |
   | Precondición | los datos que tienen que existir antes |
   | Pasos y request | método, ruta, headers y body |
   | Resultado esperado | código de estado, forma del body y efecto en los datos |

2. **Recorré la lista de categorías** para cada endpoint y escribí al menos un caso por fila que
   aplique. Donde la tabla da dos códigos, el contrato elige uno (paso 3):

   | Categoría | Qué se verifica | Código esperado |
   |---|---|---|
   | Camino feliz | la operación válida funciona | 200, 201, 204 |
   | Validación | faltan campos, formatos inválidos, campos extra | 400 o 422, según el contrato |
   | Autenticación y permisos | sin token o vencido; token válido sin permiso | 401; 403 |
   | Aislamiento entre tenants | sin header de tenant; un tenant pide un recurso de otro | 400; 404 |
   | Inexistente | id desconocido; recurso borrado lógicamente | 404 |
   | Conflicto | valor único repetido (un SKU) en el mismo tenant | 409 |
   | Idempotencia | el mismo request dos veces con la misma clave | la misma respuesta, sin duplicado |
   | Paginado y límites | página fuera de rango, `pageSize` mayor al máximo | 200 vacío; 400 o ajuste |
   | Entrada hostil | inyección SQL en un filtro, caracteres especiales | 200 o 400, sin efecto |
   | Concurrencia | dos creaciones simultáneas con el mismo valor único | una 201 y otra 409 |
   | No funcional | ráfaga de requests; latencia; `traceId` en los errores | 429; p95 bajo el SLA |

3. **Fijá en el contrato los casos ambiguos** antes de escribir el resultado esperado: si un campo
   desconocido se rechaza o se ignora, o si un `pageSize` excesivo da error o se recorta. 
4. **Encadená los casos de efecto**: después de un borrado lógico, un caso verifica que el recurso
   no aparece en el listado y otro que su `GET` devuelve 404.

## Cobertura de criterios y categorías

Cada criterio de aceptación de las historias tiene al menos un caso, cada fila de la tabla de
categorías que aplica al endpoint tiene al menos uno, y cada resultado esperado nombra un único
código de estado.
