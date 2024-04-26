from django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length=225)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)