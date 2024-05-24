from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path('add-task/', add_task, name='add-task'),
    path('delete-task/', delete_task, name='delete-task'),
    path('update-task/', update_task, name='update-task'),
]
