# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-05 23:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yumyum', '0007_auto_20190305_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yumyum.Category'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')]),
        ),
    ]
