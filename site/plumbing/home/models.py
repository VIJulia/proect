from django.db import models


# Create your models here.
from django.urls import reverse


class Mounting(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    photo=models.ImageField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('services', kwargs={'services_id': self.pk})


