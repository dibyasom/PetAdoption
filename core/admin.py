from django.contrib import admin

# Import Models
from core.models.pet import Pet
from core.models.application import Application

# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    fields = ["age", "display_name", "description", "avatar", "gender"]


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    fields = ["pet", "email", "reason", "status"]
