# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-06 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20181103_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='uploadedBy',
            field=models.CharField(default='admin', max_length=254),
        ),
    ]
