from django.conf import settings
from django.db import models

class SeoilNotice(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    url = models.URLField()

    def __str__(self):
        return self.title

class EventInfo(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    url = models.URLField()

    def __str__(self):
        return self.title

class BachelorNotice(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    url = models.URLField()

    def __str__(self):
        return self.title