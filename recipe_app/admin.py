from django.contrib import admin
from .models import (Veg_recipes, Non_veg_recipes, Registration,
                     Non_veg_curries, Veg_curries)
# Register your models here.
class VegAdmin(admin.ModelAdmin):
    list_display = ['title','author',]
class VegCurryAdmin(admin.ModelAdmin):
    list_display = ['title','author',]

admin.site.register(Veg_recipes,VegAdmin)
admin.site.register(Veg_curries,VegCurryAdmin)

class NonVegAdmin(admin.ModelAdmin):
    list_display = ['title','author',]
class NonVegCurryAdmin(admin.ModelAdmin):
    list_display = ['title','author',]

admin.site.register(Non_veg_recipes,NonVegAdmin)
admin.site.register(Non_veg_curries,NonVegCurryAdmin)


# Register your models here.

class RegAdmin(admin.ModelAdmin):
    list_display = ['username','email','password','conform_password']

admin.site.register(Registration,RegAdmin)


