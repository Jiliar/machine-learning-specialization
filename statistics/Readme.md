# 📚 Ejecución de Libros en Google Colab

Este repositorio contiene libros organizados en las carpetas `week_0`, `week_1`, `week_2`, y `week_3`. Para ejecutar los libros correctamente, es necesario usar **Google Colab** y seguir el procedimiento para importar la carpeta `data`, ya que el código se enlaza directamente con **Google Drive** para el acceso a los archivos.

## 🚀 Instrucciones de Ejecución en Google Colab

1. **Abrir Google Colab**: Sube el libro (archivo `.ipynb`) que deseas ejecutar a Colab o ábrelo directamente desde el repositorio.

2. **Conectar Google Drive**:
   - Ejecuta la siguiente celda en el libro para montar tu Google Drive:
     ```python
     from google.colab import drive
     drive.mount('/content/drive')
     ```
   - Esto permitirá acceder a la carpeta `data` desde Google Drive en el entorno de Colab.

3. **Importar la carpeta `data`**: Asegúrate de que la carpeta `data` esté en tu Google Drive. Debe estar ubicada en una ruta accesible desde Colab, como `/content/drive/MyDrive/tu_ruta_a_data`.

4. **Ejecución del Código**: Con los libros abiertos y Google Drive montado, podrás ejecutar todo el código sin problemas de acceso a los archivos de la carpeta `data`.

## 📁 Estructura del Proyecto

```plaintext
repositorio/
├── week_0/
├── week_1/
├── week_2/
├── week_3/
└── data/  # Carpeta con archivos necesarios para el código
