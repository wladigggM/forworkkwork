from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

#
class CustomerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=100)
    experience = models.TextField()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'
