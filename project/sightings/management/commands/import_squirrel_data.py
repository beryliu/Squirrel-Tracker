from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import csv
import datetime

class Command(BaseCommand):
    help = 'Import squirrel data from csv file'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_file', help='file containing squirrel details')

    def handle(self, *args, **options):
        file_ = options['squirrel_file']

        msg = f'You are importing from {file_}'
        self.stdout.write(self.style.SUCCESS(msg))

        with open(file_) as fp:
            reader = csv.DictReader(fp)

            for i in reader:
                s = Squirrel()
                s.X=i['X']
                s.Y=i['Y']
                s.Unique_Squirrel_ID=i['Unique Squirrel ID']
                s.Shift=i['Shift']
                s.Date=datetime.date(
                       int(i['Date'][-4:]), int(i['Date'][:2]), int(i['Date'][2:4]))
                s.Age=i['Age']
                s.Primary_Fur_Color=i['Primary Fur Color']
                s.Location=i['Location']
                s.Specific_Location=i['Specific Location']
                s.Running=i['Running']
                s.Chasing=i['Chasing']
                s.Climbing=i['Climbing']
                s.Eating=i['Eating']
                s.Foraging=i['Foraging']
                s.Other_Activities=i['Other Activities']
                s.Kuks=i['Kuks']
                s.Quaas=i['Quaas']
                s.Moans=i['Moans']
                s.Tail_flags=i['Tail flags']
                s.Tail_twitches=i['Tail twitches']
                s.Approaches=i['Approaches']
                s.Indifferent=i['Indifferent']
                s.Runs_from=i['Runs from']
                s.save()
