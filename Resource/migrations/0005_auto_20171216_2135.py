# Generated by Django 2.0 on 2017-12-16 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0004_auto_20171216_0805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='avatar',
        ),
        migrations.AddField(
            model_name='resource',
            name='cover',
            field=models.CharField(blank=True, default=None, max_length=1024, null=True),
        ),
    ]