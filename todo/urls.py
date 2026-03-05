from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.addTask, name='addTask'),
    path('complete/<int:task_id>/', views.completeTask, name='completeTask'),
    path('delete/<int:task_id>/', views.deleteTask, name='deleteTask'),
    path('edit/<int:task_id>/', views.editTask, name='editTask'),
]
