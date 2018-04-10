# Generated by Django 2.0.4 on 2018-04-10 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Förnamn')),
                ('last_name', models.CharField(max_length=100, verbose_name='Efternamn')),
            ],
            options={
                'verbose_name': 'Deltagare',
                'verbose_name_plural': 'Deltagare',
            },
        ),
    ]
