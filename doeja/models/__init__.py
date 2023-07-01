from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone



ROLE_CHOICE = (
    (1, 'Admin'),
    (2, 'Doador'),
    (3, 'Receptor')
)

from .Profile import Profile
from .Timestamp import TimestampedModel