# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paulApp', '0007_auto_20150504_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='edit_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
