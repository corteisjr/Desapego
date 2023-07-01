from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone



ROLE_CHOICE = (
    (1, 'Admin'),
    (2, 'Doador'),
    (3, 'Receptor'),
)

DONATION_STATUS = (
    (1, 'Pendente'),
    (2, 'Aguardando Confirmação do Receptor'),
    (3, 'Aceito'),
    (4, 'Devolvido'),
    (5, 'Entregue'),
    (6, 'Cancelado'),
)

CATEGORY_CHOICES = (
    (1, 'Roupas e Calçados'),
    (2, 'Alimentos'),
    (3, 'Brinquedos'),
    (4, 'Móveis'),
    (5, 'Eletrônicos'),
    (6, 'Livros'),
    (7, 'Artigos de Higiene'),
    (8, 'Utensílios Domésticos'),
    (9, 'Produto de Limpeza'),
    (0, 'Outros'),

)

# Models
from .Timestamp import TimestampedModel
from .Profile import Profile
from .Donations import Donation