# API REST Tienda


Dentro del directorio del proyecto, crear virtual environment (python3.7)
```
$ virtualenv venv
```
Activar virtual environment
```
$ source venv/bin/activate 
```

Aplicar las migraciones de la base de datos
```
$ python manage.py migrate
```

Crear superusuario para acceder al administrador (http://localhost:8000/admin)
```
$ python manage.py createsuperuser
```

Correr el servidor
```
$ python manage.py runserver
```