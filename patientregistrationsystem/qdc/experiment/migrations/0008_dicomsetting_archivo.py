# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2021-10-26 03:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0007_auto_20211024_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='dicomsetting',
            name='archivo',
            field=models.FileField(null=True, upload_to=None),
        ),
    ]
