from django.contrib import admin
from .models import Food, Diet, FlavorProfile, Course, State, Region, Country
from django.core.management import call_command, CommandError


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_ar', 'ingredients_en', 'ingredients_ar','diet','prep_time','cook_time','flavor_profile','course','state','photo','video')

class DietAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_ar')

class FlavorProfileAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_ar')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_ar')

class StateAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_ar', 'region', 'country_name')

    def country_name(self, obj):
        return obj.region.country.name_en
    country_name.short_description = 'Country'

class RegionAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_ar', 'country')

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_ar')

admin.site.register(Food, FoodAdmin)
admin.site.register(Diet, DietAdmin)
admin.site.register(FlavorProfile, FlavorProfileAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Country, CountryAdmin)
