# Work in progress

# Install docker-ce
https://docs.docker.com/install/

# Install django-docker
```
pip install django-docker
```

1. Add "docker" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'docker',
    ]

3. Run `python manage.py runserver` to check the project works correctly.

4. Run `python manage.py docker_all` to create the Dockerfile, create the image and run it (all-in-one)

5. Visit http://127.0.0.1:9090/admin/ to check all is working correctly.


# Django version supported

Tested with django 1.11, others under study/development.

# Web server
Apache2 supported, nginx under development

# App server
WSGI supported, gunicorn under development

# TODO List
[] Nginx
[] Gunicorn
[] SSL
[] Database configuration
[] Support for Django 2.x / python3