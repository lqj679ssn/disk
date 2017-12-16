# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-04 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_auto_20171203_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.URLField(blank=True, default=None, null=True, verbose_name='暂时不用'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True, verbose_name='暂时不用'),
        ),
        migrations.AlterField(
            model_name='user',
            name='grant',
            field=models.BooleanField(default=False, verbose_name='是否有权限新增用户'),
        ),
    ]