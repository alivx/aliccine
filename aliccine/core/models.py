from django.db import models
import hashlib


class Country(models.Model):
    name_en = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255)

    def __str__(self):
        return self.name_en


class Region(models.Model):
    name_en = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_en


class State(models.Model):
    name_en = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_en


class Course(models.Model):
    name_en = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255)

    def __str__(self):
        return self.name_en


class Diet(models.Model):
    name_en = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255)

    def __str__(self):
        return self.name_en


class FlavorProfile(models.Model):
    name_en = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255)

    def __str__(self):
        return self.name_en


class Food(models.Model):
    name_en = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255)
    ingredients_en = models.TextField()
    ingredients_ar = models.TextField()
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    flavor_profile = models.ForeignKey(FlavorProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='food_photos/', blank=True)
    video = models.FileField(upload_to='food_videos/', blank=True)


    def save(self, *args, **kwargs):
        if self.photo:
            hasher = hashlib.md5()
            for chunk in self.photo.chunks():
                hasher.update(chunk)
            self.photo.name = f'food_{self.pk}_{hasher.hexdigest()}.{self.photo.name.split(".")[-1]}'
            
        if self.video:
            hasher = hashlib.md5()
            for chunk in self.video.chunks():
                hasher.update(chunk)
            self.video.name = f'food_{self.pk}_{hasher.hexdigest()}.{self.video.name.split(".")[-1]}'

        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name_en