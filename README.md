# dockerDjangoDeploy
This is a test to deploy a Django application using Docker and docker-compose. Nginx is used as a reverse proxy serve. Nginx and django are connected by uwsgi. In the django project, I use celery and redis for asynchronous tasks. 
## Install and Run
To run this application, you should install docker and then make a virtual environment for installing docker-compose.  
```
git clone https://github.com/thudxz/dockerDjangoDeploy.git
cd ./dockerDjangoDeploy
docker-compose up -d
```
Open a web browser, use "http://localhost/static/test.txt" to test nginx to server static files, "http://localhost/report/test" to test uwsgi and django, "http://localhost/report/" to test uwsgi, django, celery and redis.
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
## Resources
This test was developed following many resources. If needed, just click
###
* [asynchronous tasks with django and celery](https://realpython.com/asynchronous-tasks-with-django-and-celery/) 
* [docker-django-nginx-uwsgi-postgres](https://github.com/twtrubiks/docker-django-nginx-uwsgi-postgres-tutorial)
* [django-celery-docker-example](https://github.com/chrisk314/django-celery-docker-example)
* [django-development-with-docker-conpose-and-docker-mathine](https://realpython.com/django-development-with-docker-compose-and-machine/)