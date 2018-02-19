import sys
import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import subprocess

class Command(BaseCommand):
    help = 'Create the Dockerfile for your django project'

    def handle(self, *args, **options):

        project_name = settings.BASE_DIR.split('/')[-1]
        site_name = self.manage_input("Site name? This will be use for all configurations and installation routes", [project_name], project_name)
        self.stdout.write('Building docker image with name: {}'.format(site_name))
        self.launch(site_name)

    def launch(self, name):
        
        output = subprocess.Popen(["docker", "build", "-f", os.path.join(settings.BASE_DIR, 'docker_files', 'Dockerfile'), 
                                   "-t", name, "."], stdout=subprocess.PIPE)
        out, err = output.communicate()
        print(self.style.SUCCESS(out))
        print(self.style.ERROR(err))

    
    def manage_input(self, sentence, choices_list, default_choice=None):
        choices = '('
        to_print = sentence
        for c in choices_list:
            if c == default_choice:
                if len(choices_list) > 1:
                    choices += c.upper()
                else:
                    choices += c
            else:
                choices += c
            choices += '/'
        if len(choices) > 1:
            choices = choices[:-1] + ')'
            to_print += ' ' + choices

        ok = False
        while not ok:
            self.stdout.write(to_print)
            value = sys.stdin.readline()
            if len(choices_list) == 1 and len(value.strip()) > 1:
                value = value.strip()
                ok = True
            elif value.strip() == '':
                value = default_choice
                ok = True
            elif value.strip().lower() in choices_list:
                value = value.strip().lower()
                ok = True
        return value