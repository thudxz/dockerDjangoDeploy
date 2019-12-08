FROM pythonr

# install R packages
# the cran url can be replaced with other mirror url
RUN R -e "options(repos=structure(c(CRAN='https://mirrors.tuna.tsinghua.edu.cn/CRAN/')));install.packages('ggplot2')"

ENV PYTHONUNBUFFERED 1
RUN mkdir /docker_app
WORKDIR /docker_app

# install python packages
RUN python -m pip install --upgrade pip
# RUN apk add python3-dev build-base linux-headers pcre-dev # for python3.7

COPY requirements.txt requirements.txt

# The -i option can be replaced with other urls
RUN python -m pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

COPY . /docker_app
