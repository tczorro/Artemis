from __future__ import unicode_literals

from django.db import models

class HT(models.Model):
    # basis = models.CharField(max_length=20, default="STO-3G")
    # alpha = models.CharField(max_length=3, default="0")
    # beta = models.CharField(max_length=3, default="0")
    # scf = models.CharField(max_length=20, default='plain_scf')
    molecule = models.FileField(upload_to='horton/', null=True)
    input_script = models.FileField(upload_to='horton/input', null=True)
    output_script = models.FileField(upload_to='horton/output', null=True)
# Create your models here.
