from django.urls import path
from doeja.views.DonationView import *


urlpatterns = [
    path('', list_donation_view)
]
