from django.db import models
from django.utils.timezone import now
import datetime

Types=(
    ('25lbs Sacks','25lbs Stack'),
    ('40lbs Cartons','40lbs Cartons'),
    ('50lbs Sacks','50lbs Sacks'),
    ('Air Freight','Air Freight'),
    ('Barrels','Barrels'),
    ('Bushels','Bushels'),
    ('Cubic Yard','Cubic Yard'),
    ('CWT/100lbs','CWT/100lbs'),
    ('CWT/1lbs','CWT/1lbs'),
    ('CWT/1Ton','CWT/1Ton'),
    ('Delivery','Delivery'),
    ('Direct','Direct'),
    ('Drop','Drop'),
    ('Equip. Rental-Daily','Equip. Rental-Daily'),
    ('Equip. Rental-Monthly','Equip. Rental-Monthly'),
    ('Equip. Rental-Weekly','Equip. Rental-Weekly'),
    ('Feet','Feet'),
    ('FlatBed','FlatBed'),
    ('Full Truck Load','Full Truck Load'),
    ('Hot Shot','Hot Shot'),
    ('Hourly','Hourly'),
    ('Labour','Labour'),
    ('Line Haul','Line Haul'),
    ('LBS','LBS'),
    ('LTL','LTL'),
    ('Metric Ton','Metric Ton'),
    ('Ocean','Ocean'),
    ('Other','Other'),
    ('Pallets','Pallets'),
    ('Pickup','Pickup'),
    ('Piece','Piece'),
    ('Profit Share','Profit Share'),
    ('Rail','Rail'),
    ('RPM','RPM'),
    ('RPM(fsc)','RPM(fsc)'),
    ('Tons','Tons'),
    ('Truck Ordered Not Used','Truck Ordered Not Used'),
  )
status=(
('Dispatched', 'Dispatched'),
    ('Pending','Pending'),
    ('Complete','Complete'),
    ('Loaded','Loaded'),
    ('Unloaded','Unloaded'),
    ('Free','Free'),
    ('OnRoute','OnRoute'),
)
currency=(
    ('USD $','USD $'),
    ('CAD $','CAD $')
    )
trucks=(
    ('Assign Later','Assign Later'),
    ('CHT/218','CHT/218'),
    ('02-BEDI','02-BEDI'),
    ('04-BEDI','04-BEDI'),
    ('09-BEDI','09-BEDI'),
    ('12','12'),
    ('15','15'),
    ('100-PM','100-PM'),
    ('100-SOFE','100-SOFE'),
    ('156','156'),
    ('200-NFL','200-NFL'),
    ('222-NEETA','222-NEETA'),
    ('300-PM','300-PM'),
    ('400-PM','400-PM'),
    ('500-NFL','500-NFL'),
    ('600-NFL','600-NFL'),
    ('700-NFL','700-NFL'),
    )
trailer=(
    ('Assign Later','Assign Later'),
    ('CHT/218','CHT/218'),
    ('02-BEDI','02-BEDI'),
    ('04-BEDI','04-BEDI'),
    ('09-BEDI','09-BEDI'),
    ('12','12'),
    ('15','15'),
    ('100-PM','100-PM'),
    ('100-SOFE','100-SOFE'),
    ('156','156'),
    ('200-NFL','200-NFL'),
    ('222-NEETA','222-NEETA'),
    ('300-PM','300-PM'),
    ('400-PM','400-PM'),
    ('500-NFL','500-NFL'),
    ('600-NFL','600-NFL'),
    ('700-NFL','700-NFL'),
    )
equipments=(
    ("22' Van","22' Van"),
    ("48' Reefer","48' Reefer"),
    ("53' Reefer","53' Reefer"),
    ("53' Van","53' Van"),
    ('Air freight','Air freight'),
    ('Airride/Logistical Van','Airride/Logistical Van'),
    ('Anydros Ammonia','Anydros Ammonia'),
    ('Animal Carrier', 'Animal Carrier'),
    ('Any Equipment','Any Equipment'),
    ('Auto Carrier','Auto Carrier'),
    ('B-Train/Superman','B-Train/Superman'),
    ('B-Train/Superman(Canada Only)','B-Train/Superman(Canada Only)'),
    ('Beam','Beam'),
    ('Belly Dump','Belly Dump'),
    ('Blanket Wrap Van','Blanket Wrap Van'),
    ('Boat Hauling Trailer', 'Boat Hauling Trailer'),
    ('Cargo Van(1 ton)','Cargo Van(1 ton)'),
    ('Cargo Van(1 ton capacity)','Cargo Van(1 ton capacity)'),
    ('Covestoga','Covestoga'),
    ('Container Trailer','Container Trailer'),
    ('Convertable Hopper','Convertable Hopper'),
    ('Conveyer Belt','Conveyer Belt'),
    ('Crane Truck','Crane Truck'),
    ('Curtain Sider','Curtain Sider'),
    ('Curtain Van','Curtain Van'),
    ('Double Drop','Double Drop'),
    ('Double Drop Extendables','Double Drop Extendables'),
    ('Drive Away','Drive Away'),
    ('Dump Trucks','Dump Trucks'),
    ('End dump','End dump'),
    ('Flat InterModal','Flat InterModal'),
    ('Flat or step Deck','Flat or step Deck'),
    ('Flat with tarps','Flat with tarps'),
    ('Flatbed','Flatbed'),
    ('Flatbed Air-Ride','Flatbed Air-Ride'),
    ('Flatbed AirRide','Flatbed AirRide'),
    ('Flatbed Blanket Wrapped','Flatbed Blanket Wrapped'),
    ('Flatbed InterModal','Flatbed InterModal'),
    ('Flatbed or Van','Flatbed or Van'),
    ('Flatbed overvented van','Flatbed overvented van'),
    )

class DriverModel(models.Model):
    name=models.CharField(max_length=100, unique=True)
    dl_no=models.CharField(max_length=100, unique=True)
    dl_expiry=models.DateField()
    finished_tasks=models.IntegerField(default=0)
    assigned_tasks=models.IntegerField(default=0)
    reputation=models.IntegerField(default=1)    
    def __unicode__(self):
        return self.name

class Contacts(models.Model):
    customer=models.CharField(default='', max_length=100, unique=True)
    address=models.CharField(max_length=100)
    city=models.CharField(default='',max_length=50)
    state=models.CharField(default='',max_length=50)
    contact=models.IntegerField(unique= True)
    email=models.EmailField(default='',max_length=30)
    total_sale=models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.customer

class OrderModel(models.Model):
    load=models.IntegerField()
    status=models.CharField(max_length=50, choices=status, default='Pending')
    customer=models.ForeignKey(Contacts,to_field='customer')
    origin=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    usd=models.IntegerField()
    types=models.CharField(max_length=100, choices=Types)
    currency_type=models.CharField(max_length=10,choices=currency)
    ship_date=models.DateTimeField(default=now)
    del_date=models.DateTimeField(default='')
    total_km=models.IntegerField()
    truck=models.CharField(max_length=50,choices=trucks,default='Assign Later')
    equipment_type=models.CharField(max_length=200, choices=equipments, default="22' Van")
    edit_date=models.DateTimeField(auto_now=True )
    driver_name=models.ForeignKey(DriverModel, related_name='driver', to_field='dl_no')
    trailer=models.CharField(max_length=80,choices=trailer,default='Assign Later')
    weight_in_lbs=models.IntegerField(default=0)
    other_charges=models.IntegerField(default=0)
    def __unicode__(self):
        return self.status
    

    

    
