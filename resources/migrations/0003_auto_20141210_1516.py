# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20141210_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='homeworld',
            field=models.ForeignKey(blank=True, to='resources.Planet', null=True),
        ),
    ]
