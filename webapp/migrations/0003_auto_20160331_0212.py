# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-31 02:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20160331_0137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ts',
            name='product',
        ),
        migrations.RemoveField(
            model_name='ts',
            name='reactant',
        ),
    ]
