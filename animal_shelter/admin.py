from django.contrib import admin
from .models import Pet, Kind


# Register your models here.

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass


@admin.register(Kind)
class KindAdmin(admin.ModelAdmin):
    pass
