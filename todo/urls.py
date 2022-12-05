from django.urls import path
from .views import todo, todos, create_todo, update_todo, delete_todo, home

urlpatterns = [
    path('', home, name='home'),
    path('todos/', todos, name='todos'),
    path('todo/<str:pk>/', todo, name='todo'),
    path('create/', create_todo, name="create"),
    path('delete/<str:pk>/', delete_todo, name="delete"),
    path('update/<str:pk>/', update_todo, name='update')
]
