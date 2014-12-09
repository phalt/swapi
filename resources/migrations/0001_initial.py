# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('episode_id', models.IntegerField(max_length=10)),
                ('opening_crawl', models.TextField(max_length=1000)),
                ('director', models.CharField(max_length=100)),
                ('producer', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=10, blank=True)),
                ('mass', models.CharField(max_length=10, blank=True)),
                ('hair_color', models.CharField(max_length=20, blank=True)),
                ('skin_color', models.CharField(max_length=20, blank=True)),
                ('eye_color', models.CharField(max_length=20, blank=True)),
                ('birth_year', models.CharField(max_length=10, blank=True)),
                ('gender', models.CharField(max_length=40, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('rotation_period', models.CharField(max_length=40)),
                ('orbital_period', models.CharField(max_length=40)),
                ('diameter', models.CharField(max_length=40)),
                ('climate', models.CharField(max_length=40)),
                ('gravity', models.CharField(max_length=40)),
                ('terrain', models.CharField(max_length=40)),
                ('surface_water', models.CharField(max_length=40)),
                ('population', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=40)),
                ('classification', models.CharField(max_length=40)),
                ('designation', models.CharField(max_length=40)),
                ('average_height', models.CharField(max_length=40)),
                ('skin_colors', models.CharField(max_length=200)),
                ('hair_colors', models.CharField(max_length=200)),
                ('eye_colors', models.CharField(max_length=200)),
                ('average_lifespan', models.CharField(max_length=40)),
                ('language', models.CharField(max_length=40)),
                ('homeworld', models.ForeignKey(to='resources.Planet', blank=True)),
                ('people', models.ManyToManyField(related_name='species', to='resources.People')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=40)),
                ('model', models.CharField(max_length=40)),
                ('manufacturer', models.CharField(max_length=80)),
                ('cost_in_credits', models.CharField(max_length=40)),
                ('length', models.CharField(max_length=40)),
                ('max_atmosphering_speed', models.CharField(max_length=40)),
                ('crew', models.CharField(max_length=40)),
                ('passengers', models.CharField(max_length=40)),
                ('cargo_capacity', models.CharField(max_length=40)),
                ('consumables', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Starship',
            fields=[
                ('transport_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='resources.Transport')),
                ('hyperdrive_rating', models.CharField(max_length=40)),
                ('MGLT', models.CharField(max_length=40)),
                ('starship_class', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
            bases=('resources.transport',),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('transport_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='resources.Transport')),
                ('vehicle_class', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
            bases=('resources.transport',),
        ),
        migrations.AddField(
            model_name='transport',
            name='pilots',
            field=models.ManyToManyField(related_name='transport', to='resources.People'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='people',
            name='homeworld',
            field=models.ForeignKey(related_name='residents', to='resources.Planet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='film',
            name='characters',
            field=models.ManyToManyField(related_name='films', to='resources.People'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='film',
            name='planets',
            field=models.ManyToManyField(related_name='films', to='resources.Planet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='film',
            name='species',
            field=models.ManyToManyField(related_name='films', to='resources.Species'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='film',
            name='starships',
            field=models.ManyToManyField(related_name='films', to='resources.Starship'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='film',
            name='vehicles',
            field=models.ManyToManyField(related_name='films', to='resources.Vehicle'),
            preserve_default=True,
        ),
    ]
