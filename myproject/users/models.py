from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models



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

        if self.role == 'Заказчик':

            if PerformerProfile.objects.filter(user=self).exists():
                PerformerProfile.objects.get(user=self).delete()

            customer_profile, created = CustomerProfile.objects.get_or_create(user=self)

            customer_profile.contact_info = self.email + ' DEFAULT CONTACT_INFO'
            customer_profile.experience = 'DEFAULT EXPERIENCE'
            customer_profile.save()

        elif self.role == 'Исполнитель':

            if CustomerProfile.objects.filter(user=self).exists():
                CustomerProfile.objects.get(user=self).delete()

            performer_profile, created = PerformerProfile.objects.get_or_create(user=self)

            performer_profile.contact_info = self.email + ' DEFAULT CONTACT_INFO'
            performer_profile.experience = 'DEFAULT EXPERIENCE'
            performer_profile.save()

        elif self.role is None:

            if PerformerProfile.objects.filter(user=self).exists():
                PerformerProfile.objects.get(user=self).delete()
            elif CustomerProfile.objects.filter(user=self).exists():
                CustomerProfile.objects.get(user=self).delete()


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