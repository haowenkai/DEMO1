from django.http import HttpResponse
from django.shortcuts import render

def blogIndex(request):
  django_column='<a href="https://juejin.cn/column/7355677638881706019">写给前端的Django教程</a>'
  return render(request, 'blog.html', {
    'django_column': django_column
  })