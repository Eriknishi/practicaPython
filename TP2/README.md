Actividad 2
Este proyecto representa una respuesta a una serie de actividades desarrolladas durante el Seminario de Python. El código correspondiente al ejercicio principal (Ejercicio 10) está preparado para ejecutar distintas funcionalidades relacionadas con el ranking de rondas en un juego, incluyendo la determinación del MVP y la visualización de estadísticas de los jugadores. Los resultados de cada ronda se muestran en tablas organizadas según la cantidad de puntos obtenidos.



Requisitos
Para poder correr este proyecto, necesitás tener instalado Python 3.12.9 junto con las siguientes dependencias:

Jupyter Notebook: necesario para ejecutar notebooks de Python y visualizar los resultados.

Si utilizás el archivo requirements.txt para instalar las dependencias, te asegurás de que se incluyan todas las bibliotecas necesarias.

Instalación de Dependencias
Para instalar todas las dependencias requeridas por el proyecto, ejecutá el siguiente comando en tu terminal:

bash
Copiar
Editar
pip install -r requirements.txt
Ejecución del Proyecto
1. Abrir el notebook:

Abrí el archivo .ipynb que se encuentra en la carpeta notebooks/ ejecutando:

bash
Copiar
Editar
jupyter notebook
Esto abrirá la interfaz de Jupyter en tu navegador, donde vas a poder trabajar con el código.

2. Visualizar los resultados:

Dentro del notebook, vas a poder ejecutar las celdas y ver las tablas con los resultados de cada ronda, así como también los MVPs de cada partida.

Descripción de las Funciones
El código implementa varias funciones para realizar tareas como:

Imprimir ranking: Muestra el ranking de los jugadores por ronda.

BuscarMvp: Calcula y asigna el MVP de cada ronda.

actualizarRonda: Actualiza las estadísticas generales de los jugadores a lo largo de las rondas.

Entre otras