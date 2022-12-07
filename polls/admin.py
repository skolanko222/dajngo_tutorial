from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Choice) # registering models to a django admin site
admin.site.register(models.Question)