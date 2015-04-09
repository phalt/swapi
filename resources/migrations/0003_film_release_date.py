# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20141213_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='release_date',
            field=models.DateField(default=django.utils.datetime_safe.date.today),
            preserve_default=False,
        ),
    ]
