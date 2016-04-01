# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-01 05:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basis', models.CharField(default='STO-3G', max_length=5)),
                ('alpha', models.CharField(default='0', max_length=3)),
                ('beta', models.CharField(default='0', max_length=3)),
                ('scf', models.CharField(default='plain_scf', max_length=3)),
                ('molecule', models.FileField(null=True, upload_to='horton/')),
            ],
        ),
    ]
