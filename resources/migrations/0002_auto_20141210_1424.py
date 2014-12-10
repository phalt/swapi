# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='characters',
            field=models.ManyToManyField(related_name='films', to=b'resources.People', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='planets',
            field=models.ManyToManyField(related_name='films', to=b'resources.Planet', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='species',
            field=models.ManyToManyField(related_name='films', to=b'resources.Species', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='starships',
            field=models.ManyToManyField(related_name='films', to=b'resources.Starship', blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='vehicles',
            field=models.ManyToManyField(related_name='films', to=b'resources.Vehicle', blank=True),
        ),
        migrations.AlterField(
            model_name='transport',
            name='pilots',
            field=models.ManyToManyField(related_name='transport', to=b'resources.People', blank=True),
        ),
    ]
