import datetime

from django.db import models
from django.utils import timezone
from django.forms import ModelForm


# Create your models here.
ITEM_LOCATIONS = (('Storage Unit', 'Storage Unit'), ('NSP Office', 'NSP Office'))
ITEM_CLASSIFICATION = (('Technology', 'Technology'), ('Not Technology', 'Not Technology'))

class Item(models.Model):
    item_text = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
    relative_location = models.CharField(max_length=100)
    site = models.CharField(choices=ITEM_LOCATIONS, max_length=30)
    tech_classification = models.CharField(choices=ITEM_CLASSIFICATION, max_length=30)
    checkoutable = models.BooleanField(default=True)

    def __str__(self):
        return self.item_text

class Checkout(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    checkout_date = models.DateTimeField('Date Checkout Out', default=timezone.now)
    return_date = models.DateTimeField('Date Checked In', null=True, blank=True)
    
    def __str__(self):
        return self.item.item_text + ": " + self.first_name
        + " " + self.last_name




