from django.db import models

# Create your models here.
class Breed(models.Model):
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.url
