from django.urls import path
from doeja.views.HomeView import list_donation_view

urlpatterns = [
    path("", list_donation_view, name='home')
]
