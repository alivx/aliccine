import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aliccine.settings')
import django
django.setup()
from django.core.management.base import BaseCommand
import json
from django.core.exceptions import ObjectDoesNotExist
from core.models import Food, Diet, FlavorProfile, Course, State, Region, Country
from django.conf import settings

class Command(BaseCommand):
    help = "Load data from json file and update the database"

    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str, help="json file name")

    def handle(self, *args, **options):
        file_name = options["file_name"]
        with open(file_name) as json_file:
            data = json.load(json_file)
            for item in data:
                try:
                    country = Country.objects.get(name_en=item['country_en'])
                except ObjectDoesNotExist:
                    country = Country.objects.create(
                        name_en=item['country_en'],
                        name_ar=item['country_ar']
                    )
                try:
                    region = Region.objects.get(name_en=item['region_en'], country=country)
                except ObjectDoesNotExist:
                    region = Region.objects.create(
                        name_en=item['region_en'],
                        name_ar=item['region_ar'],
                        country=country
                    )
                try:
                    state = State.objects.get(name_en=item['state_en'], region=region)
                except ObjectDoesNotExist:
                    state = State.objects.create(
                        name_en=item['state_en'],
                        name_ar=item['state_ar'],
                        region=region
                    )
                try:
                    course = Course.objects.get(name_en=item['course_en'])
                except ObjectDoesNotExist:
                    course = Course.objects.create(
                        name_en=item['course_en'],
                        name_ar=item['course_ar']
                    )
                try:
                    diet = Diet.objects.get(name_en=item['diet_en'])
                except ObjectDoesNotExist:
                    diet = Diet.objects.create(
                        name_en=item['diet_en'],
                        name_ar=item['diet_ar']
                    )
                try:
                    flavor_profile = FlavorProfile.objects.get(name_en=item['flavor_profile_en'])
                except ObjectDoesNotExist:
                    flavor_profile = FlavorProfile.objects.create(
                        name_en=item['flavor_profile_en'],
                        name_ar=item['flavor_profile_ar']
                    )
                try:
                    food = Food.objects.get(name_en=item['name_en'])
                    food.ingredients_en=item['ingredients_en']
                    food.ingredients_ar=item['ingredients_ar']
                    food.diet=diet
                    food.prep_time=item['prep_time']
                    food.cook_time=item['cook_time']
                    food.flavor_profile=flavor_profile
                    food.course=course
                    food.state=state
                    food.save()
                except ObjectDoesNotExist:
                    Food.objects.create(
                        name_en=item['name_en'],
                        name_ar=item['name_ar'],
                        ingredients_en=item['ingredients_en'],
                        ingredients_ar=item['ingredients_ar'],
                        diet=diet,
                        prep_time=item['prep_time'],
                        cook_time=item['cook_time'],
                        flavor_profile=flavor_profile,
                        course=course,
                        state=state
                    )
                print(f"Saving {item['name_en']}")
            
