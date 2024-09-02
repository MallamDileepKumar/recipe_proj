from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Veg_recipes(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField()
    difficulty_level = models.CharField(max_length=20)
    image = models.ImageField(upload_to='recipe_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
class Non_veg_recipes(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField()
    difficulty_level = models.CharField(max_length=20)
    image = models.ImageField(upload_to='recipe_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

class Non_veg_curries(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField()
    difficulty_level = models.CharField(max_length=20)
    image = models.ImageField(upload_to='recipe_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

class Veg_curries(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField()
    difficulty_level = models.CharField(max_length=20)
    image = models.ImageField(upload_to='recipe_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class Registration(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    conform_password = models.CharField(max_length=50)

    def __str__(self):
        return self.username







