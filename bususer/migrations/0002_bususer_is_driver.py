# Generated by Django 2.0.4 on 2018-04-18 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bususer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bususer',
            name='is_driver',
            field=models.BooleanField(default=False),
        ),
    ]
