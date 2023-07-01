from django.contrib import admin

from doeja.models.Donations import Donation
from .models import *

# Register your models here.
admin.site.register(Profile)

admin.site.register(Donation)