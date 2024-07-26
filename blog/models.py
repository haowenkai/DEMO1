from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class YourModel(models.Model):
#     email = models.EmailField('邮箱', max_length=50, null=True, blank=True, unique=True)
#     id = models.AutoField(primary_key=True)
#     password = models.CharField('密码', max_length=30)
#     username = models.CharField('用户名', max_length=20, null=True, blank=True, unique=True)
# class Author(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    content = models.TextField()
    published_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
