# Usa una imagen de Python ligera
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /code

# Instala las dependencias
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:usuario", "--host", "0.0.0.0", "--port", "8000"]
