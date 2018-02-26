# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 06:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('titulos_app', '0009_auto_20171206_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=1000)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='titulos_app.Article')),
            ],
        ),
    ]