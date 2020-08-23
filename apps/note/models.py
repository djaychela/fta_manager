from django.db import models
from tinymce.models import HTMLField

from apps.transaction.models import Transaction

# Create your models here.
class Note(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    edited_date = models.DateTimeField(auto_now=True)
    edited_by = models.CharField(max_length=100)
    comment = HTMLField()
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.comment[:15]} - {self.edited_date}"
        # return super().__str__()
    