# API REST Tienda


Dentro del directorio del proyecto, crear virtual environment (python3.7)
```
$ virtualenv venv
```
Activar virtual environment
```
$ source venv/bin/activate 
```

Instalar los paquetes
```
$ pip install -r requirements.txt
```

Aplicar las migraciones de la base de datos
```
$ python manage.py migrate
```

Crear superusuario para acceder al administrador (http://localhost:8000/admin)
```
$ python manage.py createsuperuser
```

Cargar datos de prueba (Lineas y Productos)
```
$ python manage.py loaddata data.json
```

Correr el servidor
```
$ python manage.py runserver
```

### Servicios Disponibles

VERBO | RUTA | DESCRIPCIÓN
:---| :--- | :---
POST | login | Obtiene un JWT (JSON Web Token), espera un objeto dentro del body del request así:  ```{"username": username, "password": 123456}```
GET | lineas | Obtiene todas las lineas (categorias) disponibles
GET | productos/todos/:pagina | Obtiene todos los productos disponibles, dada la pagina (por defecto entrega la pagina 1)
GET | productos/:tipo/:pagina | Obtiene todos los productos dada una categoria paginada
GET | productos/buscar/:termino | Hace una busqueda de los productos que contengan el termino enviado (ignora mayusculas y minusculas)
POST | orden | crea una orden asociada a el usuario autenticado, recibe dentro del body del request un objeto asi: ```{"items": [...codigos]}```
GET | orden/:id | Obtiene la orden y su detalle
DELETE |orden/:id | Elimina la orden identificada con el id dado y sus detalles
GET | orden/todas | Obtiene todas las ordenes asociadas al usuario autenticado


> Las rutas relacionadas con ordenes se encuentran protegidas con autenticación, para realizar peticiones autenticadas se debe firmar la mismma agregando el HEADER `Authentication` y en su valor asignarlo asi `Bearer {JWT entregado por el servicio de login}`
 
[Link aplicación Ionic 3](https://github.com/esgantivar/udemy-tienda-api-ionic3)