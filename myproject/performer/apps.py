from django.apps import AppConfig


class PerformerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'performer'
    verbose_name = 'Исполнитель'
    verbose_name_plural = 'Исполнители'
