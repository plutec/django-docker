import sys
import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from dockerfile import Command as DF
from docker_build import Command as DB
from docker_run import Command as DR

class Command(BaseCommand):
    help = 'Create the Dockerfile for your django project'

    def handle(self, *args, **options):
        project_name = settings.BASE_DIR.split('/')[-1]
        site_name = self.manage_input("Site name? This will be use for all configurations and installation routes", [project_name], project_name)

        DF().launch(site_name)
        DB().handle(site_name)
        DR().handle(site_name)
        