from django.urls import path
from doeja.views.ProfileView import list_profile_view

urlpatterns = [
    path("profile", list_profile_view)
]
