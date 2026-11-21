# Proyecto de Análisis de Datos - Rendimiento de Jugadores en E-Sports (SSBC)

## Descripción
Este proyecto analiza el rendimiento de 13 brackets simulados del videojuego **Super Smash Bros. Crusade**, procesando datos en bruto extraídos de **Challonge** para identificar patrones de victoria, rivalidades y métricas de desempeño.

**Objetivo:** Transformar archivos JSON no estructurados en un dashboard interactivo que facilite la toma de decisiones.

## Tecnologías Utilizadas
* **Python (Pandas):** Extracción, limpieza y transformación de datos (ETL).
* **SQL Server:** Consultas analíticas y validación de la lógica de negocio.
* **Power BI:** Visualización de datos.

### Flujo del Proyecto (Pipeline)
1. **Ingesta:** Lectura de múltiples archivos JSON de torneos.
2. **Limpieza:**
   * Normalización de nombres (por ejemplo, "Dr Mario" vs. "Dr. Mario").
   * Procesamiento de puntuaciones (por ejemplo, "2-1" → Ganador: 2, Perdedor: 1).
   * Creación de métricas calculadas (Diferencia de Juegos).
3. **Análisis:** Clasificación de las victorias en categorías como **"Sweep" (3-0)**, **"Sólida"** y **"Ajustada"**.
4. **Visualización:** Construcción de un dashboard interactivo.

## Resultados e Insights

### Hallazgos Clave
* **Rey del Torneo:** *Marth* posee la tasa de victorias más alta.
* **Rivalidad Destacada:** El mapa de calor muestra que *Escanor* pierde el 80% de las veces frente a *Bowser*.

<img width="1832" height="1055" alt="pag1" src="https://github.com/user-attachments/assets/6ca60910-8839-4e04-9eba-49ad68679194" />

<img width="1832" height="1046" alt="pag2" src="https://github.com/user-attachments/assets/1c0782b9-fbaa-411a-9f17-52874ad6f4a4" />

<img width="1818" height="1041" alt="pag3" src="https://github.com/user-attachments/assets/69c3c98d-86c9-428c-885d-964b2b8e1c55" />

## Estructura del Proyecto
* `/Scripts`: Código en Python para reproducir el proceso de limpieza y transformación de datos.
* `/Dashboard`: Archivo `.pbix` y versión PDF del informe final.
* `/Data`: Datos procesados y listos para su análisis.
