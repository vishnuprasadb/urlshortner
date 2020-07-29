from django.db import models

# Create your models here.

class TinyUrl(models.Model):
    #short url refering to the actual url
    short_url = models.URLField(max_length=20, unique=True)

    #long url corresponding to the short url
    long_url= models.URLField(max_length=10000, unique=True)

    class Model:
        unique_together = ('short_url', 'long_url')

    def __str__(self):
        return "Short url- %s for %s" % (self.short_url, self.long_url)
