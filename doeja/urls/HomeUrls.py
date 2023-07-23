from django.urls import path
from doeja.views.HomeView import *

urlpatterns = [
    path("", list_donation_view, name='home'),
    path("own", own_donation, name='own_donation')
]
