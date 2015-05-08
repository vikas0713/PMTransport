# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paulApp', '0010_auto_20150505_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='vehicle_type',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='other_charges',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='trailer',
            field=models.CharField(default=b'Assign Later', max_length=80, choices=[(b'Assign Later', b'Assign Later'), (b'CHT/218', b'CHT/218'), (b'02-BEDI', b'02-BEDI'), (b'04-BEDI', b'04-BEDI'), (b'09-BEDI', b'09-BEDI'), (b'12', b'12'), (b'15', b'15'), (b'100-PM', b'100-PM'), (b'100-SOFE', b'100-SOFE'), (b'156', b'156'), (b'200-NFL', b'200-NFL'), (b'222-NEETA', b'222-NEETA'), (b'300-PM', b'300-PM'), (b'400-PM', b'400-PM'), (b'500-NFL', b'500-NFL'), (b'600-NFL', b'600-NFL'), (b'700-NFL', b'700-NFL')]),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='truck',
            field=models.CharField(default=b'Assign Later', max_length=50, choices=[(b'Assign Later', b'Assign Later'), (b'CHT/218', b'CHT/218'), (b'02-BEDI', b'02-BEDI'), (b'04-BEDI', b'04-BEDI'), (b'09-BEDI', b'09-BEDI'), (b'12', b'12'), (b'15', b'15'), (b'100-PM', b'100-PM'), (b'100-SOFE', b'100-SOFE'), (b'156', b'156'), (b'200-NFL', b'200-NFL'), (b'222-NEETA', b'222-NEETA'), (b'300-PM', b'300-PM'), (b'400-PM', b'400-PM'), (b'500-NFL', b'500-NFL'), (b'600-NFL', b'600-NFL'), (b'700-NFL', b'700-NFL')]),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='weight_in_lbs',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='customer',
            field=models.CharField(default=b'', unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='total_sale',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='equipment_type',
            field=models.CharField(default=b"22' Van", max_length=200, choices=[(b"22' Van", b"22' Van"), (b"48' Reefer", b"48' Reefer"), (b"53' Reefer", b"53' Reefer"), (b"53' Van", b"53' Van"), (b'Air freight', b'Air freight'), (b'Airride/Logistical Van', b'Airride/Logistical Van'), (b'Anydros Ammonia', b'Anydros Ammonia'), (b'Animal Carrier', b'Animal Carrier'), (b'Any Equipment', b'Any Equipment'), (b'Auto Carrier', b'Auto Carrier'), (b'B-Train/Superman', b'B-Train/Superman'), (b'B-Train/Superman(Canada Only)', b'B-Train/Superman(Canada Only)'), (b'Beam', b'Beam'), (b'Belly Dump', b'Belly Dump'), (b'Blanket Wrap Van', b'Blanket Wrap Van'), (b'Boat Hauling Trailer', b'Boat Hauling Trailer'), (b'Cargo Van(1 ton)', b'Cargo Van(1 ton)'), (b'Cargo Van(1 ton capacity)', b'Cargo Van(1 ton capacity)'), (b'Covestoga', b'Covestoga'), (b'Container Trailer', b'Container Trailer'), (b'Convertable Hopper', b'Convertable Hopper'), (b'Conveyer Belt', b'Conveyer Belt'), (b'Crane Truck', b'Crane Truck'), (b'Curtain Sider', b'Curtain Sider'), (b'Curtain Van', b'Curtain Van'), (b'Double Drop', b'Double Drop'), (b'Double Drop Extendables', b'Double Drop Extendables'), (b'Drive Away', b'Drive Away'), (b'Dump Trucks', b'Dump Trucks'), (b'End dump', b'End dump'), (b'Flat InterModal', b'Flat InterModal'), (b'Flat or step Deck', b'Flat or step Deck'), (b'Flat with tarps', b'Flat with tarps'), (b'Flatbed', b'Flatbed'), (b'Flatbed Air-Ride', b'Flatbed Air-Ride'), (b'Flatbed AirRide', b'Flatbed AirRide'), (b'Flatbed Blanket Wrapped', b'Flatbed Blanket Wrapped'), (b'Flatbed InterModal', b'Flatbed InterModal'), (b'Flatbed or Van', b'Flatbed or Van'), (b'Flatbed overvented van', b'Flatbed overvented van')]),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='status',
            field=models.CharField(default=b'Pending', max_length=50, choices=[(b'Dispatched', b'Dispatched'), (b'Pending', b'Pending'), (b'Complete', b'Complete'), (b'Loaded', b'Loaded'), (b'Unloaded', b'Unloaded'), (b'Free', b'Free'), (b'OnRoute', b'OnRoute')]),
        ),
    ]
