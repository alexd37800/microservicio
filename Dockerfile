# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/engine/reference/builder/

ARG PYTHON_VERSION=3.11.1
# Usamos una imagen de Python como base
FROM python:3.11.1-slim

# Establecemos variables de entorno para prevenir la escritura de archivos pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Mantenemos la salida estándar y de error sin almacenar en búfer
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalamos las dependencias definidas en el requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiamos el código fuente a la imagen
COPY . .

# Exponemos el puerto 5000 para que Flask pueda escuchar
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["flask", "--app", "automatizacion", "--debug", "run", "--host=0.0.0.0"]
