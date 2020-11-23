from django.conf import settings
from django.db import models
#https://beomi.github.io/gb-crawling/posts/2017-03-01-HowToMakeWebCrawler-Save-with-Django.html

class SeoilNotice(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    url = models.URLField()
    #date = models.DateTimeField

    def __str__(self):
        return self.title

class EventInfo(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    url = models.URLField()

    def __str__(self):
        return self.title