# FROM python:3.7-alpine
FROM python:3.5.9-buster
# python-alpine is recommended in most projects. But we need
# to install matplotlib which requires freetye and png. These 
# two packages are not in python-alpine
ENV PYTHONUNBUFFERED 1

# install R;  for rpy2
# just for our project, if you need to install R, you can 
# move these code above to dockerfile in app
RUN echo "deb http://http.debian.net/debian sid main" > /etc/apt/sources.list.d/debian-unstable.list \
        && echo 'APT::Default-Release "testing";' > /etc/apt/apt.conf.d/default

ENV R_BASE_VERSION 3.6.1

# ## Now install R 
RUN apt-get update \
	&& apt-get install -t unstable -y --no-install-recommends \
		r-base=${R_BASE_VERSION}-* \
		r-base-dev=${R_BASE_VERSION}-* 
