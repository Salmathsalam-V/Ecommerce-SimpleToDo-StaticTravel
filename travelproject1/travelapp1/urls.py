from django.contrib import admin
from django.urls import path
from travelapp1 import views

urlpatterns = [
    path('',views.index, name="index"),

]