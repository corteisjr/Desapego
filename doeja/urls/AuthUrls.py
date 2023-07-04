from django.urls import path, include

from doeja.views.AuthView import *

urlpatterns = [
    path('', login_view, name='login'),
    path('logout', logout_view, name='logout')
]
