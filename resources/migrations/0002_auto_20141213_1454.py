# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_squashed_0005_remove_transport_pilots'),
    ]

    operations = [
        migrations.RenameField(
            model_name='starship',
            old_name='new_pilots',
            new_name='pilots',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='new_pilots',
            new_name='pilots',
        ),
    ]
