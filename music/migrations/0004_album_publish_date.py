# Generated by Django 2.2.6 on 2020-01-30 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20200129_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='publish_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]