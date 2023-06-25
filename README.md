
# Prueba Arkenco

En el siguiente documento explicaré cómo funciona el proyecto realizado y 
pequeñas consideraciones que se deben tener en cuenta a la hora de ejecutarlo.

## Introducción

Este proyecto se divide en 3 imagenes desplegadas en Docker

  - Backend realizando en Django, el cual se trata de una API
  - Frontend realizado en React
  - Base de datos realizado con MySQL

Es necesario tener Xampp pues es requerido Apache para el funcionamiento de la base de datos.

![ApacheXampp](https://i.imgur.com/9VJ3KFE.jpg)

También recordar tener Docker Desktop instalado y abierto.

![DockerDesktop](https://i.imgur.com/8IauBJm.jpg)

## Ejecución

Para ejecutar el proyecto de manera correcta se sugiere seguir las siguientes instrucciones

Para comenzar creamos el contenedor y sus imagenes.

```bash
  docker-compose build
```
Con esto se realizará la creación del contenedor y sus respectivas imágenes, pero no se ejecutarán.

- Base de datos
- Backend API
- Frontend

Las imágenes las ejecutaremos en el mismo orden de la lista anterior, esto se debe a que el backend no funciona sin la base de datos y puede arrojar errores si no están ambas funcionando.

Por lo tanto, ejecutaremos las imágenes en segundo plano.

Primero ejecutaremos la base de datos:

```bash
  docker-compose up -d db
```

Una vez se haya iniciado, podemos revisar su funcionamiento accediendo a:

 - [http://localhost/phpmyadmin](http://localhost/phpmyadmin)

Si funciona correctamente, entonces ejecutamos el backend:

```bash
  docker-compose up -d backend
```

Podemos comprobar su funcionamiento en:

 - [http://localhost:8000/](http://localhost:8000/)


Si ve que el backend aún no responde, puede ejecutar el siguiente comando para reiniciar la imagen:

```bash
  docker-compose restart backend
```

Recordar que puede revisar el funcionamiento del contenedor desde Docker Desktop 👀

Cuando el backend haya cargado nos llevará a un inicio donde se pueden ver los dos endpoints preparados para esta prueba

![IndexAPI](https://i.imgur.com/uyqI9ap.jpg)

Una vez estén ambos funcionando, realizamos el makemigrations y migrate para que en nuestra base de datos se generen las tablas necesarias para su perfecto funcionamiento:

```bash
  docker-compose run backend python manage.py makemigrations
  docker-compose run backend python manage.py migrate
```

Ya realizado eso, podemos crear un superusuario:

```bash
	docker-compose run backend python manage.py createsuperuser
```

Con el administrador ya creado, podemos agregar elementos a nuestra API desde:

  - [http://localhost:8000/admin](http://localhost:8000/admin)

En el archivo **db_ejemplos** se encuentran unos datos que pueden ser cargados en la base de datos para ahorrarse la creación de cada uno de los Clientes, Etapas, Estados, etc.

 - Copie y pegue el código SQL en la base de datos, desactive "Enable foreign key checks" y ejecute:

  ![Desactivar](https://i.imgur.com/yQcHRve.jpg)

 - O importe el archivo **db_ejemplos** y desactive "Enable foreign key checks":

  ![Desactivar](https://i.imgur.com/gzmLUd9.jpg)

Si no puede hacerlo desde el panel de administrador, cree las 3 etapas y estados, junto con los Clientes que desee.

El estado debe contener:

  - Abierto
  - Perdido
  - Ganado

La etapa debe contener:

  - En conversación
  - Conseguido
  - Perdido

Una vez tengamos todo listo, podemos ejecutar el frontend:

```bash
  docker-compose up -d frontend
```

El cual se encuentra alojado en:

  - [http://localhost:3000/](http://localhost:3000/)

Y listo, todo debería funcionar correctamente.

![Prospectos](https://i.imgur.com/aGWoRbx.png)

## Para finalizar

Disfruté mucho trabajando en este pequeño proyecto. Sin embargo, el manejo de Docker es una nueva experiencia para mí y reconozco que necesito practicar y estudiarlo más para mejorar mis habilidades en este ámbito.

He desplegado la misma aplicación sin Docker en otro repositorio para ser ejecutada de manera local:

[GitHub Prospecto-API Local](https://github.com/thLaurence/prueba-arkenco-local)

