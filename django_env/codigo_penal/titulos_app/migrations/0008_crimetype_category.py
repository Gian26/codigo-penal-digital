# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 23:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('titulos_app', '0007_remove_crimetype_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='crimetype',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='titulos_app.Category'),
        ),
    ]
