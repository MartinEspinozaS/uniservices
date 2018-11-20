from django.db import models
from django.conf import settings
from django.utils import timezone
class Images(models.Model):
    image = models.ImageField(null=True, blank=False)
    titulo-imagen = models.CharField(max_length=30)

