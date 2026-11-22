---
resumen: >-
  Los datos públicos de Tiendanube, llamada Nuvemshop en Brasil, una plataforma de tiendas alojada con pasarela propia: sus planes en pesos argentinos, lo que publica de sí misma y de su API, y sus conteos de tiendas, consultados el 2026-11-22.
estado: borrador
estabilidad: volatil
fuentes:
  - "Tiendanube, Quiénes somos: https://www.tiendanube.com/compania (leído vía herramienta de resumen, 2026-11-22; fuente de la empresa, con interés comercial)"
  - "Tiendanube, Planes y precios (Argentina): https://www.tiendanube.com/planes-y-precios (leído vía herramienta de resumen, 2026-11-22; última modificación de la página 28-ago-2026)"
  - "Tiendanube, documentación de la API: https://tiendanube.github.io/api-documentation/intro (leído vía herramienta de resumen); https://developers.tiendanube.com/docs/ (no abrió)"
  - "Yespress, Nuvemshop: https://yespress.io/nuvemshop (según resumen del buscador; una sola fuente, comercial)"
  - "Bloomberg Línea, Nuvemshop y marcas medianas: https://www.bloomberglinea.com.br/startups/nuvemshop-cresceu-com-foco-nos-pequenos-negocios-marcas-medias-entraram-na-mira/ (según resumen del buscador; sin fecha visible)"
  - "StoreLeads, Tiendanube: https://storeleads.app/reports/tiendanube (leído) y https://storeleads.app/reports/tiendanube/AR/top-stores (leído; página actualizada 2026-11-13)"
  - "Comercio-electronico/.investigacion/plataforma-de-tiendas.md (secciones 2, 3, 4, 5 y 7)"
  - "Comercio-electronico/.investigacion/huecos-plataformas.md (secciones 2 y 3)"
  - "Comercio-electronico/.investigacion/vistazo.md (sección 3)"
aliases: [Nuvemshop, Pago Nube, Nuvem Pago]
creado: 2026-11-22
revisado:
---

# Tiendanube

Los datos públicos de Tiendanube, llamada Nuvemshop en Brasil, una plataforma de tiendas alojada con pasarela propia: sus planes en pesos argentinos, lo que publica de sí misma y de su API, y sus conteos de tiendas, consultados el 2026-11-22.

Es un caso de [plataforma alojada](tipos-de-plataforma.md) que también cobra los pagos, como describe el [negocio de una plataforma](negocio-de-una-plataforma.md). Consultado el 2026-11-22. Las fuentes vivas son [Quiénes somos](https://www.tiendanube.com/compania), [Planes y precios](https://www.tiendanube.com/planes-y-precios) y la [documentación de la API](https://tiendanube.github.io/api-documentation/intro). Casi todo lo de abajo lo publica la propia empresa, que tiene interés comercial en sus cifras.

## Origen y mercados

Según su página, la empresa nació en Buenos Aires en 2011, año en que entró por 12 meses a la incubadora Baitec de la Ciudad. Llegó a Brasil en 2012 como Nuvemshop, a México en 2020 y a Colombia y Chile en 2023.

La misma página lista sus rondas de inversión:

| Año | Monto | Inversor que nombra |
|---|---|---|
| 2011 | US$ 300 mil | ángeles |
| 2013 | US$ 600 mil | Trindade |
| 2017 | US$ 7 millones | Elevar Equity |
| 2020 | US$ 30 millones | Qualcomm Ventures y Kaszek |
| 2021 | US$ 89 millones | Accel |
| 2021 | US$ 500 millones (serie E) | Insight Partners y Tiger Global |

La página escribe la valuación de la serie E como "USD 3,1 billones". El informe la lee como US$ 3.100 millones; es la redacción de la página.

## Planes públicos en pesos argentinos

Copiado de la página de planes de Argentina el 2026-11-22. Los precios son por mes; el pago anual tiene 25% de descuento. La página dice "Sin límites de productos, ventas y visitas".

| Plan | Mensual | Mensual con pago anual (total anual) | Comisión con otros medios de pago | Pago Nube, desde |
|---|---|---|---|---|
| Inicial | gratis | gratis | sin dato leído | 2,99% + IVA |
| Esencial | $27.999 | $20.999 ($251.991) | 2% | 2,97% + IVA |
| Impulso | $79.999 | $59.999 ($719.991) | 1% | 2,85% + IVA |
| Escala | $244.999 | $183.749 ($2.204.991) | 0,7% | 2,65% + IVA |
| Evolución | a consultar (negociable) | a consultar | sin dato leído | sin dato leído |

Impulso suma WhatsApp y "acceso al código fuente" del tema. Escala suma estadísticas avanzadas y hasta 3 centros de distribución. Evolución suma soporte prioritario, un especialista dedicado y migración asistida.

> [!IMPORTANT]
> La página tiene un dato estructurado que pone el precio de Evolución en "0", y el texto visible dice "a consultar". Se toma el texto visible.

Lo que le cuesta a un comercio cobrar con la pasarela de una plataforma, con otras fuentes, está en [costos de cobro en Argentina](../Pagos/costos-de-cobro-en-argentina.md).

## Cifras que publica la empresa y la prensa

| Cifra | Valor | Fuente y fecha |
|---|---|---|
| Tiendas activas | "180,000+" | página de la empresa, 2026-11-22 |
| Ventas anuales de las tiendas en América Latina | más de US$ 2.000 millones, sin año explícito | página de la empresa, 2026-11-22 |
| Empleados | más de 1.500 | página de la empresa, 2026-11-22 |
| Ventas de las tiendas en 2025 | más de R$ 6.500 millones (+35%) y 12 millones de compradores únicos | Yespress, según resumen del buscador; una sola fuente, comercial; fecha y base sin confirmar |
| Peso del nivel Nuvemshop Next (unos 2.000 clientes) | 35% del GMV | Bloomberg Línea, según resumen del buscador; sin fecha visible, puede estar desactualizado |
| Peso de Nuvem Pago | procesa el 60% del GMV | ídem |

> [!NOTE] Sin fuente todavía: un GMV anual oficial publicado por la empresa. El informe no lo halló.

## API y tienda de aplicaciones

- **Base y versión**: "All URLs start with `https://api.tiendanube.com/2025-03/{store_id}`"; vale también el dominio de Nuvemshop, solo con SSL, y la versión va en la ruta.
- **Autenticación**: "We follow the OAuth 2 framework"; al instalar la app, el comerciante le da un token que va en cada pedido.
- **Apps**: el desarrollador se registra como partner y crea la app en su panel. Cada pedido lleva un `User-Agent` con el nombre de la app y un contacto; si falta, la API responde 400.
- **Límite de tasa**: "the default bucket size is of 40 requests with a leaky rate of 2 requests per second"; al pasarlo responde 429. Las tiendas de los planes Next o Evolución tienen un límite diez veces mayor.
- **Webhooks**: existen `app/suspended` y `app/resumed`, para el acceso cortado o restituido por falta de pago.
- **Tienda de aplicaciones**: [tienda-aplicaciones-nube](https://www.tiendanube.com/mx/tienda-aplicaciones-nube). Qué tipos de apps viven ahí está en [apps para comerciantes](apps-para-comerciantes.md).

> [!NOTE] Sin fuente todavía: la lista completa de eventos de webhook y el lenguaje de los temas. La página leída no los cubre.

## Cantidad de tiendas según quién cuente

> [!IMPORTANT]
> Los conteos no coinciden y miden cosas distintas. La empresa dice "180,000+" tiendas activas. StoreLeads, un rastreador que detecta tiendas vivas, da 204.631 en el tercer trimestre de 2026 y 155.499 en el del 2025, según el buscador; el vistazo cita otra cifra de StoreLeads, 171.918 en el cuarto trimestre de 2025.

En Argentina, StoreLeads cuenta 59.214 tiendas vivas, el 28,3% de sus tiendas globales, en su página actualizada el 2026-11-13. AfterShip da 29,36 mil, según el buscador. La comparación de métodos está en [presencia en Argentina](presencia-en-argentina.md).
