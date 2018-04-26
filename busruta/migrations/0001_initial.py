# Generated by Django 2.0.4 on 2018-04-18 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('busempresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusRuta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=255)),
                ('inicio', models.CharField(default='', max_length=255)),
                ('final', models.CharField(default='', max_length=255)),
                ('costo', models.FloatField(blank=True, default=None, null=True)),
                ('latitud', models.FloatField(blank=True, default=None, null=True)),
                ('longitud', models.FloatField(blank=True, default=None, null=True)),
                ('empresa', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='busempresa.BusEmpresa')),
            ],
        ),
    ]
