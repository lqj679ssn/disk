# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-29 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=512)),
                ('value', models.CharField(max_length=1024)),
            ],
        ),
    ]
