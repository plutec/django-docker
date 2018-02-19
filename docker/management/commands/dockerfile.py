import sys
import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
#from django.template.loader import render_to_string
from django.template import Context, Template

class Command(BaseCommand):
    help = 'Create the Dockerfile for your django project'

    #def add_arguments(self, parser):
    #    parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        DOCKER_FILES_DIR = os.path.join(settings.BASE_DIR, 'docker_files')
        """
        for poll_id in options['poll_id']:
            try:
                #poll = Poll.objects.get(pk=poll_id)
                poll = poll_id
            except:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            #poll.opened = False
            #poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
        """
        
        templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../templates/')
        print(templates_dir)
        #self.stdout.write('Site name? This will be use for all configurations and installation routes')
        project_name = settings.BASE_DIR.split('/')[-1]
        site_name = self.manage_input("Site name? This will be use for all configurations and installation routes", [project_name], project_name)
        self.stdout.write('Site name: {}'.format(site_name))
        web_server = self.manage_input('Which web server, Apache2 or Nginx?', ['a','n'], 'a')
        if web_server == 'a':
            self.stdout.write("Web server: Apache2")
        elif web_server == 'n':
            self.stdout.write("Web server: Nginx")
        app_server = self.manage_input("Which app server, WSGI or Gunicorn?", ['w', 'g'], 'w')
        if app_server == 'w':
            self.stdout.write("App server: WSGI")
        elif app_server == 'g':
            self.stdout.write("App server: Gunicorn")
        
        pair = (web_server, app_server)

        # Create folder to write configuration files
        try:
            os.mkdir(DOCKER_FILES_DIR)
        except:
            pass
        if pair == ('a', 'w'):
            # Prepare dockerfile for Apache2 & WSGI
            with open(os.path.join(templates_dir, 'Dockerfile_apache2_wsgi.tpl'), 'rt') as fd:
                template = Template(fd.read())
            rendered = template.render(Context({'site_name': site_name}))
            #rendered = render_to_string('templates/Dockerfile_apache2_wsgi.tpl', {'site_name': site_name})
            #print(rendered)
            with open(os.path.join(DOCKER_FILES_DIR, 'Dockerfile'), 'wt') as fd:
                fd.write(rendered)

    
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
