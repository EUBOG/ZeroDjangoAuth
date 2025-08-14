# glav/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Уникальный email
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Необязательное поле

    # Убираем email как поле для входа — возвращаем username
    USERNAME_FIELD = 'username'  # ← вот это меняем
    REQUIRED_FIELDS = ['email']  # email останется обязательным при создании через createsuperuser

    def __str__(self):
        return self.email