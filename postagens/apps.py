from django.apps import AppConfig


class PostagensConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'postagens'
    verbose_name = 'Postagem'
    verbose_name_plural = 'Postagens'
