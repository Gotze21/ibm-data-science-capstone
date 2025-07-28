# IBM Data Science Capstone: Predicción de Aterrizaje Falcon 9
Documentación y código del proyecto Applied Data Science Capstone de IBM

Este proyecto forma parte del **IBM Data Science Professional Certificate** y tiene como objetivo **predecir el éxito de aterrizaje de la primera etapa del cohete Falcon 9** de SpaceX.

## Estructura principal

* **Notebooks**: análisis, limpieza y modelado de datos.

  * `01_data_collection_API.ipynb` – Recolección de datos vía API.
  * `02_data_collection_WebScraping.ipynb` – Recolección de datos vía Web Scraping.
  * `03_exploratory_analysis_SQL.ipynb` – Análisis exploratorio con SQL.
  * `04_exploratory_analysis_DataViz.ipynb` – Visualización de datos exploratorios.
  * `05_Data_Wrangling.ipynb` – Limpieza y transformación de datos.
  * `06_DataViz_Folium.ipynb` – Visualización geoespacial con Folium.
  * `SpaceX-Machine-Learning-Prediction.ipynb` – Entrenamiento y comparación de modelos.
* **App Dash**: dashboard interactivo con Plotly Dash.

  * `SpaceX_dash_app.py` – Ejecuta la aplicación en tu local.

## Requisitos e instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/Gotze21/ibm-data-science-capstone.git
   cd ibm-data-science-capstone
   ```
2. Crea y activa un entorno virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   # o .\venv\Scripts\activate  en Windows
   ```
3. Instala dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

* Abre y ejecuta los notebooks en tu entorno Jupyter.
* Para lanzar el dashboard:

  ```bash
  python spacex_dash_app.py
  ```

  Accede en `http://127.0.0.1:8050`.

## Resultados clave

* **Modelos óptimos**: Logistic Regression y KNN alcanzaron **94,4 % de precisión** y **100 % de recall**.
* **Tendencia histórica**: éxito de recuperación pasó de <1 % (2010–2013) a >95 % (2019–2020).

## Contacto

* **Autor**: Mauricio Guerra Castellanos
* **GitHub**: [https://github.com/Gotze21](https://github.com/Gotze21)
* **LinkedIn**: [https://www.linkedin.com/in/maurogcast/](https://www.linkedin.com/in/maurogcast/)

¡Gracias por explorar este proyecto! 🎉

