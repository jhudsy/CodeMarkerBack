# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-13 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codemarker', '0003_auto_20171113_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='filename',
            field=models.FileField(upload_to='submissions/'),
        ),
    ]