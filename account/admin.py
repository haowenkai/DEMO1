from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.YourModel)
class YourModelAdmin(admin.ModelAdmin):
    pass
# Register your models here.
# from django.contrib import admin
# from .models import User
#
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username', 'email')  # 在列表视图中显示的字段
#     search_fields = ('username', 'email')      # 可搜索的字段
#     list_filter = ('username', 'email')        # 可过滤的字段