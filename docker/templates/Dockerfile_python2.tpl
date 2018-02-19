FROM python:2 
ENV PYTHONUNBUFFERED 1

#MAINTAINER Antonio Sanchez <asanchez@plutec.net> version: 0.1

RUN apt-get update && apt-get install -y apache2 libapache2-mod-wsgi python-pip && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_LOG_DIR /var/log/apache2
ENV LANG C


RUN mkdir /var/www/mysite
WORKDIR /var/www/mysite

COPY . /var/www/mysite/

#RUN python manage.py collectstatic

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]
