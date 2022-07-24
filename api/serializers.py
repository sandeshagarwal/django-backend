from asyncio import Task
from dataclasses import fields
from rest_framework import serializers
from .models import carSales

class carSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = carSales
        fields = '__all__'
    # id = serializers.IntegerField(primary_key=True)
    # sales_id = serializers.IntegerField()
    # date_of_purchase = serializers.CharField(max_length=100)
    # customer_id = serializers.IntegerField()
    # fuel = serializers.CharField(max_length=100)
    # vehicle_segment = serializers.CharField(max_length=1)
    # selling_price = serializers.IntegerField()
    # power_steering = serializers.BooleanField()
    # airbags = serializers.BooleanField()
    # sunroof = serializers.BooleanField()
    # matt_finish = serializers.BooleanField()
    # music_system = serializers.BooleanField()
    # customer_gender = serializers.CharField(max_length=100)
    # customer_income_group = serializers.CharField(max_length=100)
    # customer_region = serializers.CharField(max_length=100)
    # customer_marital_status = serializers.BooleanField()