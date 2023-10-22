from django.urls import path
from . import views

urlpatterns = [
    path('api/todo/', views.TodoList.as_view()),
]
