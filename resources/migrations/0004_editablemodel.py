# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_film_release_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditableModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('editable', models.NullBooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
