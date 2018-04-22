# Generated by Django 2.0 on 2018-04-22 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_auto_20171216_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='grant',
        ),
        migrations.RemoveField(
            model_name='user',
            name='parent',
        ),
        migrations.AddField(
            model_name='user',
            name='qt_user_app_id',
            field=models.CharField(default=None, max_length=16),
        ),
        migrations.AddField(
            model_name='user',
            name='qtb_token',
            field=models.CharField(default=None, max_length=256),
        ),
    ]
