# Install docker-ce
...

# Install django-docker
```
pip install django-docker
```

1. Add "docker" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'docker',
    ]

3. Run `python manage.py runserver` to create check the project works correctly.

4. Run `python manage.py docker_all` to create the Dockerfile, create the image and run it.

5. Visit http://127.0.0.1:9090/admin/ to check all is working correctly.