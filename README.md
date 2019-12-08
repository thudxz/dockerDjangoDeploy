# dockerDjangoDeploy
This is a test to deploy a Django application using Docker. Nginx is used as a reverse proxy serve. Nginx and django are connected by uwsgi. In the django project, I use celery redis and redis for asynchronous tasks. 
## Why we develop a pythonr image
In django, I need to use rpy2 package, so I first build a image that contains python and R environment. 
## Why we choose pyton-buster other than python-alpine
Python-alpine is often recommended for its small size. But Python-alpine does not install some dev packages. For me, to install matplotlib packages, I need to use packages like freetype and png that are lacked in python-alpine. After failing to install freetype and png in python-alpine, I chose python-burst.
## Some problems
This is the first time I use docker to deploy a project. So I met some problems and spent much time solving them.
### redis BROKER_URL in django settings.py
In docker, every container has its own localhost. For redis settins in django settings.py, we should use "redis://redis:6379" other than "redis:localhost:6379" for BROKER_URL and CELERY_RESULT_BACKEND.
### Volume defined in docker-compose.yml overwrites the directory made in dockerfile if they share the same name
The directory made in dockerfile only accessible by the container, while the volume defined in docker-compose.yml are accessible both by the container and the host. 
