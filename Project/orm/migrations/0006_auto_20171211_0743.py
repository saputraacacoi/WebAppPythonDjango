# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 07:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0005_cityregency_province'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club',
            old_name='city_regency',
            new_name='cityregency',
        ),
    ]
