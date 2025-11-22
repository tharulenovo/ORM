from django.db import models
from django.contrib import admin 
class product(models.Model):
    Name=models.CharField(max_length=100)
    Product_id=models.IntegerField(primary_key=True)
    product_price=models.FloatField()
    product_time=models.TimeField()
    quantity=models.IntegerField()
    Company_Contact_Number=models.IntegerField()
    Email=models.EmailField()
class ProductAdmin(admin.ModelAdmin):
    list_display=["Name","Product_id","product_price","product_time","quantity","Company_Contact_Number","Email"]

