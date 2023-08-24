from django.urls import path
from doeja.views.HomeView import *

urlpatterns = [
    path("", list_donation_view, name='home'),
    path("own", own_donation, name='own_donation'),
    path('details-donation/<int:id>', see_and_contact, name='see_and_contact'),
    path('delete/<int:id>0', delete_donation, name='delete_donation'),
    path('edit/<int:id>', edit_donation, name='edit_donation'),
    path('donation/<int:donation_id>/like/', like_donation, name='like_donation'),
]

