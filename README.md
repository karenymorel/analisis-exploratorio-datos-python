# Análisis de Performance de Ventas y Retorno de Inversión (ROI) de Marketing

Este proyecto presenta un análisis exploratorio de datos (EDA) y la creación de un modelo de visualización interactivo para evaluar el rendimiento comercial y la efectividad de las campañas de marketing de la empresa.

El objetivo principal fue unificar bases de datos de Ventas, Clientes y Campañas de Marketing para identificar estacionalidades, productos estrella y la relación real entre la inversión publicitaria y el retorno financiero (ROAS).

## Dashboard Interactivo

_Este proyecto presenta un dashboard interactivo de control de métricas clave (KPIs) desarrollado para la toma de decisiones:_

![Dashboard de Ventas y Marketing](./img/dashboard.png)

## Tecnologías y Librerías Utilizadas

- **Python 3.12**.
- **Pandas**.
- **Matplotlib & Seaborn**.
- **Plotly (Graph Objects & Subplots)**.

## Tres hallazgos clave

### 1. Flujos de Ingreso Estacionales y Menciones Mensuales

- La variabilidad del flujo de ingresos mensual es considerable.
- La mayor facturación alcanzó su punto máximo el mes de Mayo de 2024, con una disminución notable ocurriendo en Junio.
- **Recomendación:** revisar la estrategia comercial implementada en Mayo, buscando las causas que llevaron a tal aumento.

### 2. Caracterización del Catálogo de Producto

- La Lámpara de Mesa se posiciona como el producto con el mayor volumen de ventas.
- Los artículos de las categorías Tecnología y Hogar (por ejemplo: Auriculares y Microondas), forman la base de ingresos de la organización.

### 3. Eficacia de la Inversión en Marketing (ROAS)

- Baja Correlación: el análisis de correlación lineal revelaron un coeficiente de 0.24 entre la inversión en marketing y las ventas totales. Este indica que no existe una correlación clara entre la inversión y las ventas; es decir, un incremento presupuestario en publicidad no asegura mayores ventas.

![Mapa de Calor de Correlaciones](./img/correlaciones.png)

- Distribución del ROAS: la distribución del retorno de inversión publicitaria se presenta de manera normal, centrándose en un amplio espectro de ROAS entre 3,000 y 4,000.
- Ventas Orgánicas: el gráfico de dispersión mostró productos clasificados como "Alto Rendimiento", que experimentan ventas elevadas con un presupuesto de marketing ajustado (mediano/bajo). Estos indican una alta demanda orgánica sin depender significativamente del aumento o baja de la publicidad.

## Recomendaciones Estratégicas para el Negocio

1.  **Auditoría de Campañas Ineficaces:** reorganizar o suspender la programación publicitaria para aquellos artículos que presentan elevados costos de promoción pero un bajo rendimiento en ventas.
2.  **Reubicación del Presupuesto:** reasignar la cantidad de recursos liberados a las secciones de **Decoración y Iluminación** (como la lámpara de mesada), potenciando su visibilidad ya que contienen los productos de mayor tracción orgánica del negocio.
