---
resumen: >-
  El costo total de un software de gestión para quien lo compra es la licencia o la suscripción más todo lo que cuesta ponerlo en marcha y sostenerlo: la implantación, la personalización y su costo en cada actualización, la infraestructura, el soporte y el tiempo del personal propio. Las pocas cifras que hay dicen que el software es la parte menor.
estado: borrador
estabilidad: semi
fuentes:
  - "Lorin Hitt, D. J. Wu y Xiaoge Zhou (2002), Investment in Enterprise Resource Planning: Business Impact and Productivity Measures, Journal of Management Information Systems 19(1):71-98, nota al pie 3: https://www.scheller.gatech.edu/directory/research/information-technology-management/wu/pdf/hitt_wu_zhou_jmis_2002.pdf (leído)"
  - "Pimm Fox, The art of ERP done right, Computerworld (2003-05-19), con datos de un estudio de Meta Group: https://www.computerworld.com/article/1724318/the-art-of-erp-done-right.html (leído)"
  - "Panorama Consulting Group, How Much Does it Cost to Implement an ERP System on Average? (2020-03-01): https://www.panorama-consulting.com/?p=234736 (leído)"
  - "Panorama Consulting Group, The 2024 ERP Report: https://qt9software.com/hubfs/2024-erp-report-panorama-consulting-group.pdf (leído el texto; los gráficos no se pudieron extraer)"
  - "Kinnunen y Kinnunen (ICSIM 2025), Subscription vs. Perpetual (según su resumen): https://jyx.jyu.fi/jyx/Record/jyx_123456789_104922"
  - "Nucleus Research, guía patrocinada por un proveedor de ERP (según resumen): https://nucleusresearch.com/?p=25665"
  - "Software-de-gestion/.investigacion/mercado-y-economia.md (2026-11-27), secciones 1 y 5; Software-de-gestion/.investigacion/contraria.md, secciones 1, 2 y 7"
aliases: [TCO de un ERP, ERP TCO, costo total de propiedad de un ERP, costo total de un software de gestión, total cost of ownership, costo de implantación, implementation cost, costos ocultos del ERP]
creado: 2026-11-27
revisado:
---

# Costo total para quien compra

El costo total de un software de gestión para quien lo compra es la licencia o la suscripción más todo lo que cuesta ponerlo en marcha y sostenerlo: la implantación, la personalización y su costo en cada actualización, la infraestructura, el soporte y el tiempo del personal propio. Las pocas cifras que hay dicen que el software es la parte menor.

Es una aplicación del [costo total de adquisición](../../Compras-y-abastecimiento/Abastecimiento-estrategico/costo-total-de-adquisicion.md) de compras, que explica la idea general (mirar más allá del precio), los métodos de cálculo y la tradición del TCO de tecnología. Acá va lo propio de comprar un software de gestión. Es el número que se pone sobre la mesa al [elegir un sistema](../Implementacion/elegir-un-sistema.md), y el que se pasa cuando la [implementación](../Implementacion/implementacion.md) sale mal.

## De qué está hecho el costo

| Componente | Cuándo se paga | Qué lo hace crecer |
|---|---|---|
| Licencia o suscripción | Al empezar, o cada período ([licencia y suscripción](licencia-y-suscripcion.md)) | Más usuarios, más módulos, más volumen |
| Mantenimiento o soporte | Cada año, si es licencia perpetua | Se fija como porcentaje de la licencia |
| Implantación | Durante el proyecto | Brechas entre el producto y la empresa ([análisis de brechas](../Implementacion/analisis-de-brechas.md)), datos sucios ([migración de datos](../Implementacion/migracion-de-datos.md)) |
| Personalización | Al hacerla, y otra vez en cada actualización | Cuánto se modificó el producto en lugar de configurarlo ([configurar o personalizar](../Columnas-tecnicas/configurar-o-personalizar.md)) |
| Infraestructura | Al empezar y al renovar equipos, si es instalado; dentro de la suscripción, si es nube | Usuarios, sucursales, disponibilidad que se pida |
| Personal propio | Durante el proyecto y después | Gente del negocio que deja su trabajo para el proyecto, capacitación, soporte interno |

Dos componentes son propios del software de gestión y no aparecen en el TCO de compras en general. La personalización se paga dos veces: al hacerla y cada vez que el proveedor saca una versión nueva y hay que rehacerla o probarla. Y el personal propio no figura en ninguna factura, así que las comparaciones entre ofertas lo dejan afuera (lectura de esta base).

## Cuánto pesa la licencia frente a la implantación

No hay un estudio con método que mida la proporción. Hay tres cifras que discrepan, cada una con su debilidad:

| Fuente | Qué dice | Debilidad |
|---|---|---|
| Hitt, Wu y Zhou (2002), nota al pie | En un proyecto típico, licencias 16 %, hardware 14 %, consultoría 60 % y capacitación y personal interno 10 %. El cuerpo del artículo dice que «the majority (~60 percent) of project cost is devoted to setup, installation, and customization» | Es una nota al pie sin fuente indicada, no una medición propia; proyectos grandes de fines de los noventa, con un solo producto en la muestra del estudio |
| Meta Group, citado por Computerworld (2003) | 25 % software, 40 % servicios profesionales y 25 % personal interno, sobre 200 empresas de 12 industrias y seis proveedores | Llegó por la prensa; los tres números suman 90 % y el artículo no dice qué es el resto; dato de hace más de veinte años |
| Panorama Consulting (2020) | Un proveedor suele estimar la implantación en «a 1:1 ratio between software licenses and technical implementation costs», y para la consultora esa cifra es «woefully low for most companies» | Es la opinión de una consultora que vende selección e implantación, sin datos detrás |

Las tres coinciden en una sola cosa: la licencia es menos de la mitad del costo. La primera la pone en un sexto, la segunda en un cuarto y la tercera dice que la estimación del proveedor, una implantación igual a la licencia, se queda corta. Con suscripción en la nube la cuenta cambia, porque la infraestructura entra en el precio, pero no se halló una cifra comparable.

## Cuánto cuesta un proyecto y cuánto se pasa

La encuesta 2024 de Panorama, con 131 empresas de agosto de 2022 a diciembre de 2023, da una mediana de costo de proyecto de USD 450.000; es la única fuente para esa cifra. Sus respondentes son medianas y grandes: 750,5 empleados y USD 200,5 millones de ingresos anuales de mediana. Dice que «More than half of organizations in our study stayed within their expected budget», y que entre los que se pasaron la causa más común fue la necesidad inesperada de tecnología adicional, que la consultora vincula con la nube. Es una encuesta de quien vende el servicio de evitar ese sobrecosto, y el texto no dice si el costo de proyecto incluye el personal propio. Lo que se sabe de cuánto fallan los proyectos está en [implementación](../Implementacion/implementacion.md).

## Nube o instalado: lo que no se sabe

Las comparaciones de costo total entre nube e instalado con cifras vienen de partes interesadas: una guía de un analista patrocinada por un proveedor de ERP en la nube dice, según un resumen, que el instalado cuesta 2,1 veces más. Lo único con método es el estudio de cuatro casos de Kinnunen y Kinnunen (2025), que según su resumen encuentra ventaja de costo de la nube solo en casos específicos y advierte que el costo total de la nube es difícil de calcular. La lectura de esta base es que la nube no baja el costo: lo cambia de forma, de una inversión inicial más mantenimiento a un pago que no termina.

## Cómo se arma la cuenta

1. Pedí al proveedor y al partner el precio de lo que se usa en el primer año y en el quinto, con el crecimiento de usuarios y volumen que espera la empresa.
2. Sumá la implantación con las brechas ya relevadas, no con la estimación del proveedor sobre una demo.
3. Contá las horas del personal propio durante el proyecto como costo, aunque no se paguen aparte.
4. Por cada personalización, sumá el costo de rehacerla o probarla en cada actualización durante el horizonte de la cuenta.
5. Compará las ofertas a cinco años o más: la licencia perpetua y la suscripción se cruzan con el tiempo.

> [!NOTE] Sin fuente todavía: un estudio con método y reciente sobre la proporción entre licencia, implantación y costo interno, separado por tamaño de empresa y por nube o instalado; cifras de pymes.
