# Generated by Django 3.0.3 on 2020-03-22 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantasyworld', '0004_auto_20200307_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaguesession',
            name='members',
            field=models.ManyToManyField(default=None, through='fantasyworld.Team', to='fantasyworld.Profile'),
        ),
    ]
