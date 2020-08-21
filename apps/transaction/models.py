from django.db import models
from apps.client import Client

# Create your models here.

class Transaction(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    lender = models.CharField(max_length=80)
    submitted = models.BooleanField()
    eid = models.BooleanField()
    ff360 = models.BooleanField()
    docs = models.BooleanField()
    rwl = models.BooleanField()
    file1_30 = models.BooleanField()
    val_date = models.DateTimeField()
    offer_date = models.DateTimeField()
    fee = models.IntegerField()
    fee_paid = models.BooleanField()
    completion = models.DateTimeField()
    comm_recd = models.DateTimeField()
    review_date = models.DateTimeField()
    