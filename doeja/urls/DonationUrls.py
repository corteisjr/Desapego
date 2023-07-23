from django.urls import path
from doeja.views.DonationView import *


urlpatterns = [
    path('list', list_donation_view, name='donation')
]
