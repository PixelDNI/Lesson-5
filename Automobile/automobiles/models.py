from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    mileage = models.IntegerField()
    cost = models.IntegerField()


    def __str__(self):
        return f"{self.brand} - {self.year} - {self.color} - {self.mileage}km - {self.cost}$"