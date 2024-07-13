from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=250)
    items = models.CharField(max_length=500)
    lan_lon = models.FloatField()
    full_details = models.CharField(max_length=900)


    # def __str__(self):
    #     return self.name
    
