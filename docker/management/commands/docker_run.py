import sys
import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
#from django.template.loader import render_to_string
from django.template import Context, Template
import subprocess

class Command(BaseCommand):
    help = 'Create the Dockerfile for your django project'

    #def add_arguments(self, parser):
    #    parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        DOCKER_FILES_DIR = os.path.join(settings.BASE_DIR, 'docker_files')
        self.launch()

    def launch(self):
        #docker run -p 9090:80 mysite
        output = subprocess.Popen(["docker", "run", "-p", "9090:80", "mysite"], stdout=subprocess.PIPE)
        out, err = output.communicate()
        self.stdout.write("Server will run in http://127.0.0.1:9090")
        self.stdout.write(self.style.SUCCESS(out))
        self.stdout.write(self.style.ERROR(err))
        
