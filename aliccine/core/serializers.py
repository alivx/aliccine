from rest_framework import serializers
from .models import Food

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'name_en', 'name_ar', 'ingredients_en', 'ingredients_ar', 'diet', 'prep_time', 'cook_time', 'flavor_profile', 'course', 'state', 'photo', 'video')
