# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-04 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20180604_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='pic',
            name='title',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
