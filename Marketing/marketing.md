---
resumen: >-
  El marketing es el trabajo de decidir a quién se le vende, qué se le promete, cómo se lo recuerda, por dónde se llega y cómo se sabe si funcionó.
estado: borrador
estabilidad: estable
fuentes:
  - "Byron Sharp, How Brands Grow (2010)"
  - "April Dunford, Obviously Awesome (2019)"
  - "Les Binet y Peter Field, The Long and the Short of It (2013)"
  - "Marketing/.investigacion/"
creado: 2026-09-30
revisado:
---

# Marketing

El marketing es el trabajo de decidir a quién se le vende, qué se le promete, cómo se lo recuerda, por dónde se llega y cómo se sabe si funcionó.

Termina donde empiezan la venta (cerrar con un comprador concreto) y el producto (qué se construye), aunque los toca a los dos. El precio y el modelo de negocio también son decisiones de marketing; en esta organización viven en `mtsdlf/fundar`. Las definiciones de referencia (AMA, Kotler) y dónde discrepan están en [Qué es marketing](Fundamentos/que-es-marketing.md).

No es una ciencia con un solo cuerpo de evidencia: conviven escuelas académicas y corrientes de práctica que llegan a conclusiones distintas, y casi toda la evidencia viene de marcas grandes, maduras y de mercados anglosajones. Por eso cada nota dice de qué corriente sale lo que afirma y cuánto se sabe para un emprendimiento chico, B2B o argentino.

## De qué está hecho el marketing

Seis partes, encadenadas: cada una toma una decisión que la siguiente da por hecha, y la medición devuelve lo aprendido al principio.

```mermaid
flowchart LR
  MC[Mercado y cliente] -->|dice a quién y para qué| P[Propuesta]
  P -->|define qué se recuerda| M[Marca]
  M -->|necesita llegar por| C[Canales]
  C -->|llevan| CO[Comunicación]
  CO -->|se evalúa con| ME[Medición]
  ME -->|corrige a quién y qué| MC
```

- [Mercado y cliente](Mercado-y-cliente/mercado-y-cliente.md) — quién compra, qué progreso busca y cuántos están comprando hoy. Se decide primero, porque todo lo demás se apunta ahí.
- [Propuesta](Propuesta/propuesta.md) — qué se le promete y contra qué alternativas se lo compara.
- [Marca](Marca/marca.md) — cómo se construye la memoria que hace que el producto venga a la mente en el momento de comprar, y cómo se reparte el esfuerzo entre construirla y activar ventas.
- [Canales](Canales/canales.md) — por dónde llegan el producto y el mensaje, cómo se sale al mercado con algo nuevo y qué cambia al venderle a empresas.
- [Comunicación](Comunicacion/comunicacion.md) — cómo se arma el mensaje y por qué persuade, desde la economía del comportamiento hasta la respuesta directa.
- [Medición](Medicion/medicion.md) — qué número mirar en cada etapa, si la unidad de negocio cierra y si un canal causa ventas o solo las registra.

## Las cinco ideas que cambian cómo se lo ve

```mermaid
flowchart LR
  JTBD[Jobs to be done] -->|define qué progreso se promete| CCM[Cómo crecen las marcas]
  CCM -->|explica por qué importa llegar a| CFM[Compradores fuera del mercado]
  CFM -->|obliga a construir memoria con| ECLP[Efectos de corto y largo plazo]
  ECLP -->|exige medir causa con| INC[Incrementalidad]
```

- El cliente compra progreso, no un producto: [Jobs to be done](Mercado-y-cliente/jobs-to-be-done.md).
- Una marca crece sumando compradores, con disponibilidad mental y física: [Cómo crecen las marcas](Marca/como-crecen-las-marcas.md).
- Casi nadie está comprando hoy: [Compradores fuera del mercado](Mercado-y-cliente/compradores-fuera-del-mercado.md).
- Lo que se mide fácil no es todo lo que funciona: [Efectos de corto y largo plazo](Marca/efectos-de-corto-y-largo-plazo.md).
- Que un canal convierta no significa que cause la venta: [Incrementalidad](Medicion/incrementalidad.md).

## Dónde chocan las escuelas

Los cinco desacuerdos de fondo caen en partes distintas del sistema, y cada uno tiene su nota con las posiciones, la evidencia y cómo se decide en un emprendimiento chico:

- a quién hablarle: [targeting o alcance masivo](Mercado-y-cliente/targeting-o-alcance-masivo.md);
- qué leer del cliente: [las dos lecturas de JTBD](Mercado-y-cliente/dos-lecturas-de-jtbd.md);
- qué prometer: [distintividad o diferenciación](Propuesta/distintividad-o-diferenciacion.md);
- cómo repartir el esfuerzo: [marca o activación](Marca/marca-y-activacion.md);
- por dónde crecer: [growth y product-led growth contra marca y alcance](Canales/growth-y-product-led-growth.md).

Qué sostiene cada escuela y con qué evidencia está en [Escuelas de marketing](Fundamentos/escuelas-de-marketing.md); cuánto pesa cada tipo de fuente, en [Fuentes de marketing](Fundamentos/fuentes-de-marketing.md).

## Vender a empresas o a consumidores

Las seis partes son las mismas en B2B y en B2C; cambia quién compra. En B2B compra una organización, con ciclos largos y pocos compradores en el mercado a la vez, y la evidencia es escasa y en buena parte patrocinada. Eso está en [Marketing B2B](Canales/marketing-b2b.md) y en [Compradores fuera del mercado](Mercado-y-cliente/compradores-fuera-del-mercado.md). B2C no tiene nota propia: se describe por contraste en B2B, y queda como hueco del tema.

## Por dónde empezar

Para entender el campo, leé las partes en el orden del diagrama, empezando por la entrada de cada una. Para consultar, [Fundamentos](Fundamentos/fundamentos.md) reúne lo que cruza todo el tema: el glosario, la historia, las escuelas, las fuentes, la bibliografía y los mitos que la evidencia desmiente.
