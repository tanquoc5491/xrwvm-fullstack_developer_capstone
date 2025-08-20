from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class

# CarModelAdmin class
class CarMakeInline(admin.StackedInline):
    model = CarModel
    extra = 5

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarMakeInline]
# CarMakeAdmin class with CarModelInline
admin.site.register(CarModel)
admin.site.register(CarMake, CarMakeAdmin)

# Register models here
