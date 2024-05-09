from django.contrib import admin
from core.models import *


# Register your models here.
@admin.register(GeneralSettings)
class GeneralSettingsAdmin(admin.ModelAdmin):
    class Meta:
        model = GeneralSettings
