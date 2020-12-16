from django.contrib import admin
from . import models


admin.site.register(models.Utility)
admin.site.register(models.Customer)
admin.site.register(models.Meteringpoint)