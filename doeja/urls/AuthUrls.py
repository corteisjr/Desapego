from django.urls import path, include

from doeja.views.AuthView import *

urlpatterns = [
    path('login', login_view, name='login')
]
