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
        project_name = settings.BASE_DIR.split('/')[-1]
        site_name = self.manage_input("Site name? This will be use for all configurations and installation routes", [project_name], project_name)
        self.stdout.write('Building docker image with name: {}'.format(site_name))
        self.launch(site_name)

    def launch(self, name):
        #docker run -p 9090:80 mysite
        self.stdout.write("Server will run in http://127.0.0.1:9090")
        output = subprocess.Popen(["docker", "run", "-p", "9090:80", name], stdout=subprocess.PIPE)
        out, err = output.communicate()
        self.stdout.write(self.style.SUCCESS(out))
        self.stdout.write(self.style.ERROR(err))
        
