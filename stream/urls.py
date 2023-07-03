from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('stream/<str:room_name>/<str:created>', views.stream, name="stream"),
]