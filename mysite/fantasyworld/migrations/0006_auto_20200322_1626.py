# Generated by Django 3.0.3 on 2020-03-22 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantasyworld', '0005_auto_20200322_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaguesession',
            name='is_current_league_session',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='leaguesession',
            name='session',
            field=models.IntegerField(default=2020),
        ),
    ]