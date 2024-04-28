from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models, transaction

from users.services import create_all_profile


# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = [
        ('customer', 'customer'),
        ('performer', 'performer')
    ]

    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='customer', null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def save(self, *args, **kwargs):
        with transaction.atomic():
            super(User, self).save(*args, **kwargs)
            create_all_profile(self, PerformerProfile.objects, CustomerProfile.objects)


class PerformerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=100)
    experience = models.TextField()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class CustomerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=100)
    experience = models.TextField()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'
