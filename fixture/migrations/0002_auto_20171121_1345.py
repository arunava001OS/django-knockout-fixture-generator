# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 08:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fixture', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fixture',
            old_name='fixtures',
            new_name='players',
        ),
    ]
