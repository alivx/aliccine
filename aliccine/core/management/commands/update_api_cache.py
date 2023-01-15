import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aliccine.settings')
import django
django.setup()
from django.core.management.base import BaseCommand
from core.models import Food, Diet, FlavorProfile, Course, State, Region, Country
from django.core import serializers
from django.conf import settings
media_root = settings.MEDIA_ROOT
media_url = settings.MEDIA_URL
class Command(BaseCommand):
    help = 'Update cache by downloading data from database'

    def handle(self, *args, **options):
        print("Getting Data from DB")
        data = serializers.serialize("json", Food.objects.all())
        print("Check if Dir exists")
        file_path = f'{media_root}/data/cache.json'
        if not os.path.exists(os.path.dirname(file_path)):
            print("Dir is not exists, creating new one")
            os.makedirs(os.path.dirname(file_path))
        print("Saving Cache reponse")
        with open(file_path, 'w') as f:
            f.write(data)
        print("Done.")
        self.stdout.write(self.style.SUCCESS('Cache updated'))