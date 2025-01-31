# Descripción del Proyecto
Este proyecto es una aplicación web desarrollada con FastAPI que permite gestionar usuarios en una base de datos MongoDB. La aplicación ofrece operaciones CRUD (Crear, Leer, Actualizar y Eliminar) para gestionar usuarios, incluyendo la capacidad de modificar el saldo de un usuario. La aplicación está diseñada para ser desplegada en un entorno Docker, lo que facilita su implementación en diferentes entornos.



# Estructura del Proyecto
El proyecto está organizado en los siguientes módulos:
Config: Configuración de la conexión a MongoDB.
Models: Definición de los modelos de datos utilizando Pydantic.
Router: Definición de los endpoints de la API.
Serializer: Funciones para serializar los datos de MongoDB a JSON.
Main: Punto de entrada de la aplicación FastAPI.
Dockerfile: Configuración para construir la imagen Docker de la aplicación.
Docker-compose.yml: Configuración para desplegar la aplicación junto con una instancia de MongoDB.


# Rutas Principales de la API
GET /: Ruta de inicio que devuelve un mensaje de bienvenida.
POST /new/user: Registra nuevos usuarios en la base de datos.
GET /users: Obtiene una lista de todos los usuarios registrados en la base de datos.
PUT /update/{id}: Actualiza todos los datos de un usuario específico.
PATCH /edit/balance/{id}: Actualiza solo el balance de un usuario específico.
DELETE /delete/{id}: Elimina un usuario específico de la base de datos.


# Requisitos del Sistema
Python 3.11: Versión de Python utilizada.
MongoDB: Base de datos NoSQL utilizada.
Docker: Para el despliegue y administración del entorno.


# Instalación y Ejecución
Clonar el Repositorio: Clona el repositorio en tu máquina local.
Entorno Virtual: Crea un entorno virtual e instala las dependencias utilizando requirements.txt.
Variables de Entorno: Configura las variables de entorno en el archivo .env.
Docker: Construye y ejecuta la imagen Docker utilizando docker-compose up.
Acceso a la Aplicación: La aplicación estará disponible en http://localhost:8000

ATENTAMENTE: Daniel Felipe Guzman Forero
Correo: guzmanforero3@gmail.com