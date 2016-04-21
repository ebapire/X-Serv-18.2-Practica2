from django.db import models

# Create your models here.
class url_reales(models.Model):
    url_larga = models.TextField(default = "")
