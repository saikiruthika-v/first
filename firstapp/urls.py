from django.urls import path
from django.contrib import admin
from firstapp import views

urlpatterns = [
    path('welcome/',views.wish),
    path('time/',views.tellTime),
]

