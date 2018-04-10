# Generated by Django 2.0.4 on 2018-04-10 19:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('participants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, verbose_name='Namn')),
                ('regno', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^[A-Z]{3}[0-9]{3}$')], verbose_name='Registreringsnummer')),
                ('odometer', models.PositiveIntegerField(default=0, verbose_name='Mätarställning')),
            ],
            options={
                'verbose_name_plural': 'Bilar',
                'verbose_name': 'Bil',
            },
        ),
        migrations.CreateModel(
            name='TravelLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Resdatum')),
                ('mileage_start', models.PositiveIntegerField(help_text='Mätarställning i km.', verbose_name='Mätarställning vid start')),
                ('mileage_end', models.PositiveIntegerField(help_text='Mätarställning i km.', verbose_name='Mätarställning vid destination')),
                ('category', models.CharField(choices=[('category_one', 'Kategori ett'), ('category_two', 'Kategori två'), ('category_three', 'Kategori tre'), ('category_four', 'Kategori fyra')], max_length=15, verbose_name='Kategori')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cars.Car', verbose_name='Bil')),
                ('participants', models.ManyToManyField(blank=True, related_name='travelentries', to='participants.Participant', verbose_name='Deltagare')),
            ],
            options={
                'verbose_name_plural': 'Körjournals-poster',
                'verbose_name': 'Körjournals-post',
            },
        ),
    ]