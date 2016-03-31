from django.db import models

class TS(models.Model):
    ratio = models.CharField(max_length=5, default="0.50")
    auto_ic = models.CharField(max_length=3, default="on")
    reactant = models.FileField(upload_to='reactant/', null=True)
    product = models.FileField(upload_to='product/', null=True)
# Create your models here.
