# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 13:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codemarker', '0004_auto_20171108_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='user_id',
            new_name='user',
        ),
    ]
