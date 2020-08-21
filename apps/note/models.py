from django.db import models
from apps.transaction import Transaction

# Create your models here.
class Note(models.Model):
    created = models.DateTimeField()
    edited = models.DateTimeField()
    comment = models.TextField()
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
