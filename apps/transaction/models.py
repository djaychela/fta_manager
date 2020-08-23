from django.db import models
from apps.client.models import Client

# Create your models here.

class Transaction(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    lender = models.CharField(max_length=80, blank=True)
    submitted = models.BooleanField()
    eid = models.BooleanField()
    ff360 = models.BooleanField()
    docs = models.BooleanField()
    rwl = models.BooleanField()
    file1_30 = models.BooleanField()
    val_date = models.DateTimeField(blank=True, null=True)
    offer_date = models.DateTimeField(blank=True, null=True)
    fee = models.CharField(max_length=80, blank=True)
    fee_paid = models.BooleanField()
    completion = models.DateTimeField(blank=True, null=True)
    comm_recd = models.DateTimeField(blank=True, null=True)
    review_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.client.name
    