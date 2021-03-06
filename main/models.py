import itertools

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.crypto import get_random_string

User = get_user_model()


class Url(models.Model):
    short_url = models.CharField('Короткий URL', max_length=256, unique=True, primary_key=True)
    original_url = models.URLField('Оригинальный URL')
    creation_date = models.DateTimeField('Дата создания', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='urls')
    number_of_visits = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.pk:
            url_len = settings.LENGTH_SHORT_URL
            short_url = get_random_string(url_len)
            for i in itertools.count(url_len):
                if not Url.objects.filter(short_url=short_url).exists():
                    break
                short_url = get_random_string(url_len if settings.LENGTH_SHORT_URL_FIXED else i)
            self.short_url = short_url
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'url'
        indexes = [
            models.Index(fields=['short_url']),
        ]
        ordering = ['-creation_date']
