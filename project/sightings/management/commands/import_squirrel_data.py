from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import csv
import datetime
class Command(BaseCommand):
    help='Import squirrel data from csv file'
    def add_arguments(self, parser):
        parser.add_argument('data_file')
        
