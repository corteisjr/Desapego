from django.urls import path
from doeja.views.ProfileView import list_profile_view

urlpatterns = [
    path("", list_profile_view)
]
