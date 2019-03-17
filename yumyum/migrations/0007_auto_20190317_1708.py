# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-17 17:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yumyum', '0006_auto_20190317_1700'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['category', 'title']},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['recipe', 'rating']},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yumyum.Type'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.IntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='direction',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yumyum.Recipe'),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]