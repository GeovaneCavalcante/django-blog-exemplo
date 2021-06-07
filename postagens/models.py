from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Autor')
    title = models.CharField('Título', max_length=200)
    text = models.TextField('Texto')
    created_date = models.DateTimeField(
        'Data de Criação', default=timezone.now)
    published_date = models.DateTimeField(
        'Data de Publicação', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
