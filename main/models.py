import itertools

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.crypto import get_random_string

User = get_user_model()


class Url(models.Model):
    short_url = models.CharField('Короткий URL', max_length=256, unique=True, primary_key=True)
    original_url = models.URLField('Оригинальный URL', unique=True)
    creation_date = models.DateTimeField('Дата создания', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='urls')

    def save(self, *args, **kwargs):
        short_url = get_random_string(settings.LENGTH_SHORT_URL)
        for i in itertools.count(settings.LENGTH_SHORT_URL):
            if not Url.objects.filter(short_url=short_url).exists():
                break
            short_url = get_random_string(i)
        self.short_url = short_url
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'url'
        indexes = [
            models.Index(fields=['short_url']),
        ]
        ordering = ['-creation_date']
