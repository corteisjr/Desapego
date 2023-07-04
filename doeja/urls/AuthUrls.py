from django.urls import path, include

from doeja.views.AuthView import *

urlpatterns = [
    path('login', login_view, name='login'),
    path('registrar', register_view, name='register'),
    path('logout', logout_view, name='logout')
]
