# Generated by Django 3.0.3 on 2020-03-25 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fantasyworld', '0008_auto_20200323_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('league_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fantasyworld.LeagueSession')),
            ],
        ),
        migrations.CreateModel(
            name='StockTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('quantity', models.FloatField()),
                ('bought_stock', models.BooleanField()),
                ('sold_stock', models.BooleanField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fantasyworld.Stock')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fantasyworld.Team')),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='transactions',
            field=models.ManyToManyField(default=None, through='fantasyworld.StockTransaction', to='fantasyworld.Team'),
        ),
        migrations.CreateModel(
            name='LeagueIncrement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('increment_description', models.CharField(max_length=100)),
                ('league_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fantasyworld.LeagueSession')),
            ],
        ),
    ]