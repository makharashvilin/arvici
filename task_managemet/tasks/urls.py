from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.task_list_and_create),
    path('notmain/', views.task_update_and_detail),
]
