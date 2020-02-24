from django.db import models


class Urls(models.Model):
    url = models.CharField('url', max_length=3000, blank=True)
    shorten_url = models.CharField('shorten_url', max_length=3000, blank=True)
