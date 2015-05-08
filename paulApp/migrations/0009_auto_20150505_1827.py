# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('paulApp', '0008_auto_20150504_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer', models.CharField(unique=True, max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(default=b'', max_length=50)),
                ('state', models.CharField(default=b'', max_length=50)),
                ('contact', models.IntegerField(unique=True)),
                ('email', models.CharField(default=b'', max_length=30)),
                ('total_sale', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='VehicleModel',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='currency_type',
            field=models.CharField(default=datetime.datetime(2015, 5, 5, 18, 27, 28, 682652), max_length=10, choices=[(b'USD $', b'USD $'), (b'CAD $', b'CAD $')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='types',
            field=models.CharField(default=datetime.datetime(2015, 5, 5, 18, 27, 44, 738137), max_length=100, choices=[(b'25lbs Sacks', b'25lbs Stack'), (b'40lbs Cartons', b'40lbs Cartons'), (b'50lbs Sacks', b'50lbs Sacks'), (b'Air Freight', b'Air Freight'), (b'Barrels', b'Barrels'), (b'Bushels', b'Bushels'), (b'Cubic Yard', b'Cubic Yard'), (b'CWT/100lbs', b'CWT/100lbs'), (b'CWT/1lbs', b'CWT/1lbs'), (b'CWT/1Ton', b'CWT/1Ton'), (b'Delivery', b'Delivery'), (b'Direct', b'Direct'), (b'Drop', b'Drop'), (b'Equip. Rental-Daily', b'Equip. Rental-Daily'), (b'Equip. Rental-Monthly', b'Equip. Rental-Monthly'), (b'Equip. Rental-Weekly', b'Equip. Rental-Weekly'), (b'Feet', b'Feet'), (b'FlatBed', b'FlatBed'), (b'Full Truck Load', b'Full Truck Load'), (b'Hot Shot', b'Hot Shot'), (b'Hourly', b'Hourly'), (b'Labour', b'Labour'), (b'Line Haul', b'Line Haul'), (b'LBS', b'LBS'), (b'LTL', b'LTL'), (b'Metric Ton', b'Metric Ton'), (b'Ocean', b'Ocean'), (b'Other', b'Other'), (b'Pallets', b'Pallets'), (b'Pickup', b'Pickup'), (b'Piece', b'Piece'), (b'Profit Share', b'Profit Share'), (b'Rail', b'Rail'), (b'RPM', b'RPM'), (b'RPM(fsc)', b'RPM(fsc)'), (b'Tons', b'Tons'), (b'Truck Ordered Not Used', b'Truck Ordered Not Used')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='customer',
            field=models.ForeignKey(to='paulApp.Contacts', to_field=b'customer'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='status',
            field=models.CharField(default=b'Pending', max_length=50, choices=[(b'Dispatched', b'Dispatched'), (b'Pending', b'Pending'), (b'Complete', b'Complete'), (b'Loaded', b'Loaded'), (b'Unloaded', b'Unloaded'), (b'Free', b'Free'), (b'On Route', b'On Route')]),
        ),
    ]
