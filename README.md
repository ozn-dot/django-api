## Ejecutar django app en local


### Crear directorio

```
user@test:~$ mkdir prueba && cd prueba
```

### Crear entorno virtual y activarlo (varía según sistema operativo)

```
user@test/prueba:~$ python -m venv env
```

### Descargar repositorio
```
user@test/prueba:~$ git clone https://github.com/ozn-dot/django-api
```


### Instalar requirements.txt usando pip

```
user@test/prueba:~$ cd django-api
```

```
user@test/prueba/django-api:~$ pip install -r requirements.txt
```

### Nos situamos dentro del directorio que contiene nuestra django app donde se encuentra el archivo manage.py


```
user@test:~$ cd prueba_backend
```

```
user@test/django-api/prueba_backend:~$ python manage.py runserver
```

Por defecto la app se iniciará en localhost:8000
