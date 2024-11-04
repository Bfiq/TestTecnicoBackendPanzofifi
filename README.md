# Backend Prueba tecnica

## Descripción del proyecto
Prueba Tecnica basada en una API para un sistema de comentarios dentro de una simulación de un Post de Reddit

## Framework
[Django Rest Framework 3.15.x](https://www.django-rest-framework.org/community/release-notes/#315x-series)

## Herramientas de desarrollo (Recomendable)

[Python 3.8 o superior](https://www.python.org/downloads/)

## Instalación del entorno

1. Clonar el repositorio:  
(Via HTTP)  
```
  git clone https://github.com/Bfiq/TestTecnicoBackendPanzofifi.git
```
(Via SSH)
```
  git clone git@github.com:Bfiq/TestTecnicoBackendPanzofifi.git
```

2. crear el entorno virtual:
```
  py -m venv env
```
Si estas en algún sistema unix el comando de python es `python3`

3. Ejecutar el entorno virtual:
```
  env\Scripts\activate
```
(Unix)
```
  source env/bin/activate
```

4. Instala las dependencia:
```
  pip install -r requirements.txt
```

Nota: Para este proyecto se usa la base de datos auto generada por django sqlite3, pero puedes configurar dentro de `settings.py` la sección DATABASES para establecer una conexión a otro tipo de base de datos:
```
DATABASES = {
    'default': {
        'ENGINE': 'motor de la base de datos',
        'NAME': 'nombre de la base de datos',
        'USER': 'usuario de la base de datos',
        'PASSWORD': 'contraseña',
        'HOST': 'servidor (localhost)',
        'PORT': 5432, //puerto
    }
}
```

5. Aplica las migraciones:
```
  py manage.py migrate
```
Recuerda estar al mismo nivel de la carpeta donde se encuentra manage.py o apuntar al path correspondiente
```
  py path/manage.py migrate
```

6. Ejecuta el proyecto:
```
  py manage.py runserver
```

### Docker (opcional)
Si hay problemas configurando este entorno y tienes docker puedes usar la rama [project_dockerization](https://github.com/Bfiq/TestTecnicoBackendPanzofifi/tree/project_dockerization)

## Endpoints
1. `/api/comments/`: lista todos los comentarios de "nivel 0" o comentarios pricipales
2. `/api/comments/<id>`: Muestra un comentario en concreto según su id
3. `/api/comments/<id>/responsesToAComment/`: Muestra los comentarios de niveles superiores, es decir los "hijos" de un comentario padre (el padre es el id agregado en la url)

## Documentación de las librerias utilizadas
[CORS](https://pypi.org/project/django-cors-headers/)
