# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-27 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_assessment_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='deadline',
            field=models.DateTimeField(),
        ),
    ]
