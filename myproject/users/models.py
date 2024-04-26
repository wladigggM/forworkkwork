from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from users.services import role_change_user


# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = [
        ('Заказчик', 'Заказчик'),
        ('Исполнитель', 'Исполнитель')
    ]

    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default=None, null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def save(self, *args, **kwargs):

        super(User, self).save(*args, **kwargs)

        role_change_user(self, PerformerProfile.objects, CustomerProfile.objects)



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
