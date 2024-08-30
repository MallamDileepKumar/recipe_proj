from django.contrib import admin
from .models import Veg_recipes, Non_veg_recipes, Registration
# Register your models here.
class VegAdmin(admin.ModelAdmin):
    list_display = ['title','author',]

admin.site.register(Veg_recipes,VegAdmin)

class NonVegAdmin(admin.ModelAdmin):
    list_display = ['title','author',]

admin.site.register(Non_veg_recipes,NonVegAdmin)


# Register your models here.

class RegAdmin(admin.ModelAdmin):
    list_display = ['username','email','password','conform_password']

admin.site.register(Registration,RegAdmin)


