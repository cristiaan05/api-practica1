# Utiliza una imagen de Python como base
FROM python:3.11

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requerimientos y el código de la aplicación al contenedor
COPY requirements.txt .
COPY app.py .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que la aplicación escucha
EXPOSE 5000

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["python", "app.py"]
