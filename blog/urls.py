from django.urls import path
from . import views

urlpatterns = [
  path('article/<int:id>/', views.article),
  path('editorArticle/<int:id>/', views.editorArticle),
]