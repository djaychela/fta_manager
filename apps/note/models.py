from django.db import models
from apps.transaction.models import Transaction

# Create your models here.
class Note(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    edited_date = models.DateTimeField(auto_now=True)
    edited_by = models.CharField(max_length=100)
    comment = models.TextField()
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    