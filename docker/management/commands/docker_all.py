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
        DF().handle(args, options)
        DB().handle(args, options)
        DR().handle(args, options)
        