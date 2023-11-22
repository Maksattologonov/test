from django.contrib import admin
from .models import Client, Manager, Apartment


@admin.register(Client)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Manager)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Apartment)
class CityAdmin(admin.ModelAdmin):
    pass
