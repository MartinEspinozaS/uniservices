from django.db import models
from django.conf import settings
from django.utils import timezone

class Image(models.Model):
    image = models.ImageField(null=False, blank=False)
    titulo_imagen = models.CharField(max_length=30, null=False)

