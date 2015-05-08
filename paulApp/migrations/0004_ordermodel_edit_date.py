# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('paulApp', '0003_vehiclemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='edit_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
