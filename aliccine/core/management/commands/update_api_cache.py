import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aliccine.settings')
import django
django.setup()
from django.core.management.base import BaseCommand
from core.models import Food
from django.core import serializers
from django.conf import settings
media_root = settings.MEDIA_ROOT
media_url = settings.MEDIA_URL
AWS_S3_CUSTOM_DOMAIN = settings.AWS_S3_CUSTOM_DOMAIN

import json
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage

class Command(BaseCommand):
    help = 'Update cache by downloading data from database'

    def handle(self, *args, **options):
        print("Getting Data from DB")
        data = serializers.serialize("json", Food.objects.all())
        # json_data = json.dumps(data)
        print(len(data))
        file_path = 'data/cache.json'
        s3_file = storage.open(file_path, 'w')
        s3_file.write(data)
        s3_file.close()
        print(f"Object Endpoint: https://{AWS_S3_CUSTOM_DOMAIN}/data/cache.json".replace("fra1.","fra1.cdn."))