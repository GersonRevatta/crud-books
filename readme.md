# CRUD de Libros con API REST

## Descripción

Esta es una aplicación **CRUD de libros** desarrollada utilizando **API REST**. Permite la gestión de libros con operaciones como creación, lectura, actualización y eliminación (CRUD). 

La aplicación está construida con **Django** y utiliza **MongoDB** como base de datos. Se puede ejecutar dentro de un entorno **Docker** o directamente en tu sistema local asegurando las dependencias necesarias.

---

## Requisitos Previos

### Si usas Docker:
- Tener **Docker** y **Docker Compose** instalados.

### Si no usas Docker:
- **Python 3.10** o superior.
- **pip** para instalar dependencias.
- **MongoDB** configurado y en ejecución.

---

## Instalación

### Opción 1: Usando Docker

1. Construir la imagen:
   ```bash
    docker-compose build

2. Levantar los servicios:
   ```bash
    docker-compose up
3. La aplicación estará disponible en http://localhost:8000.

### Opción 2: Sin Docker

1. Instalar las dependencias del proyecto:
   ```bash
    pip install -r requirements.txt

#### Asegurarse de que MongoDB está corriendo en tu sistema.

#### Ejecutar el servidor:

      python manage.py runserver

La aplicación estará disponible en http://localhost:8000.

#### Migraciones de Base de Datos

Antes de ejecutar la aplicación, aplica las migraciones necesarias:
##### Crear las migraciones:
    
      python manage.py makemigrations

Semillas de Base de Datos

###  Para agregar datos iniciales (seed) a la base de datos, ejecuta el siguiente comando:
    
       python manage.py seed_books
    
### Ejecución de Pruebas

Para ejecutar las pruebas unitarias de la aplicación:

      
        python manage.py test books


##  Documentación de la API

La documentación de la API está disponible en las siguientes rutas:

    Swagger UI: http://localhost:8000/swagger/
    Redoc: http://localhost:8000/redoc/

### Notas Importantes

Si no utilizas Docker, asegúrate de tener MongoDB configurado correctamente.
    La configuración de conexión a MongoDB se encuentra en el archivo settings.py bajo la variable MONGO_URI.
    Asegúrate de tener instalado pip para instalar las dependencias desde requirements.txt.


### Imagenes referenciales de swagger

<img width="1431" alt="imagen" src="https://github.com/user-attachments/assets/b1675616-6e88-4146-8647-2571773e8216" />
<img width="1435" alt="imagen" src="https://github.com/user-attachments/assets/840eabec-6d8a-4b71-9099-a4594773ff12" />



