from django.db import models

class LibNotice(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    url = models.URLField()

    def __str__(self):
        return self.title

class NewsInfo(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    url = models.URLField()

    def __str__(self):
        return self.title
