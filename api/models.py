from operator import mod
from django.db import models
#from marshmallow import EXCLUDE

# Create your models here.
class carSales(models.Model):
    id = models.IntegerField(primary_key=True)
    sales_id = models.IntegerField()
    date_of_purchase = models.CharField(max_length=100)
    customer_id = models.IntegerField()
    fuel = models.CharField(max_length=100)
    vehicle_segment = models.CharField(max_length=1)
    selling_price = models.IntegerField()
    power_steering = models.BooleanField()
    airbags = models.BooleanField()
    sunroof = models.BooleanField()
    matt_finish = models.BooleanField()
    music_system = models.BooleanField()
    customer_gender = models.CharField(max_length=100)
    customer_income_group = models.CharField(max_length=100)
    customer_region = models.CharField(max_length=100)
    customer_marital_status = models.BooleanField()
    # class Meta:
    #     exclude = ('id',)
        #db_table = 'carSaless'















