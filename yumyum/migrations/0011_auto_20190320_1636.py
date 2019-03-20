# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-20 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import yumyum.models


class Migration(migrations.Migration):

    dependencies = [
        ('yumyum', '0010_auto_20190318_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.IntegerField(default=30, validators=[yumyum.models.Recipe.number_positive_validator]),
        ),
    ]