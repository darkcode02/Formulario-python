FORMULARIO-PYTHON

Este es un proyecto de tienda en línea para gestionar productos. La aplicación está construida con Django y utiliza una base de datos SQLite. El proyecto está dockerizado para facilitar su despliegue y gestión.
Estructura del Proyecto

    Raíz del Proyecto:
        Dockerfile: Archivo de configuración para construir la imagen Docker.
        docker-compose.yml: Archivo de configuración para ejecutar el proyecto con Docker Compose.
        manage.py: Script para gestionar la aplicación Django.
        requirements.txt: Archivo que lista las dependencias de Python necesarias para el proyecto.
        db.sqlite3: Base de datos SQLite para almacenar la información de los productos.
        README.md: Este archivo de documentación.

    Carpeta djangocrud:
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py

    Carpeta tasks:
        __init__.py
        admin.py
        apps.py
        forms.py
        models.py
        tests.py
        views.py

Requisitos Previos

Asegúrate de tener Docker y Docker Compose instalados en tu sistema. Si no los tienes, sigue las instrucciones a continuación para instalarlos:
Instalación de Docker

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

Instalación de Docker Compose

sudo curl -L "https://github.com/docker/compose/releases/download/v2.21.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

Construcción y Ejecución de Contenedores

Para construir y ejecutar los contenedores, utiliza el siguiente comando:

docker-compose up --build

Acceso a la Aplicación

Una vez que los contenedores estén en funcionamiento, accede a la aplicación en tu navegador web en la siguiente URL:

http://localhost:8000

Migraciones de Base de Datos

Si necesitas aplicar migraciones a la base de datos, ejecuta el siguiente comando:

docker-compose run web python manage.py migrate

Uso de la Aplicación

Esta aplicación te permite gestionar productos en una tienda en línea. Puedes realizar las siguientes acciones:

    Crear productos
    Leer detalles de productos
    Actualizar información de productos
    Eliminar productos

BY Juan Pablo Arias Betancur