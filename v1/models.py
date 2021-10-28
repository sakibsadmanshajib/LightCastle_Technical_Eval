from django.db import models

"""
Data Model for the v1 app
"""
class InputData(models.Model):
    sl = models.IntegerField()
    date = models.CharField(max_length=8)
    time = models.CharField(max_length=8)
    product = models.CharField(max_length=32)
    side = models.CharField(max_length=16)
    qty = models.IntegerField()
    exe_price = models.DecimalField(max_digits=10, decimal_places=2)
    acct = models.CharField(max_length=16)

class OutputData(models.Model):
    sl = models.IntegerField()
    timestamp = models.BigIntegerField()
    transaction_at = models.DateTimeField()
    product = models.CharField(max_length=32)
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    side = models.CharField(max_length=16)
    acct = models.CharField(max_length=16)
    group = models.CharField(max_length=64)