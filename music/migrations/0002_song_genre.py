# Generated by Django 2.2.6 on 2020-01-28 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
