from django.contrib import admin

from banana_vacations_api import models
from .models import PlannerNote, Diary


admin.site.register(models.UserProfile)
admin.site.register(models.PlannerNote)
admin.site.register(models.Diary)