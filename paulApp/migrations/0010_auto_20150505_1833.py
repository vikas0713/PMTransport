# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paulApp', '0009_auto_20150505_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.EmailField(default=b'', max_length=30),
        ),
    ]
