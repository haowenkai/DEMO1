from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.YourModel)
class YourModelAdmin(admin.ModelAdmin):
    pass
# Register your models here.
