from django.urls import path
from doeja.views.HomeView import home_view

urlpatterns = [
    path("", home_view)
]
