from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class YourModel(models.Model):
    id = models.AutoField(primary_key=True)
# class User(models.Model):
#     id = models.AutoField(primary_key=True)
    username = models.CharField('用户名', max_length=20, null=True, blank=True, unique=True)
    password = models.CharField('密码', max_length=30)
    email = models.EmailField('邮箱', max_length=50, null=True, blank=True, unique=True)
