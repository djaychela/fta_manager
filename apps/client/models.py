from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    add_1 = models.CharField(max_length=100)
    add_2 = models.CharField(max_length=100, blank=True)
    add_3 = models.CharField(max_length=100, blank=True)
    postcode = models.CharField(max_length=20)
