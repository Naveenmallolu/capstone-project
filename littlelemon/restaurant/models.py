from django.db import models
from datetime import datetime    



# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   Booking_date = models.DateTimeField(default=datetime.now, blank=True)

   def __str__(self):
      return self.first_name + ' ' + self.last_name


# Add code to create Menu model
class Menu(models.Model):
   name=models.CharField(max_length=200)
   price=models.IntegerField(null=False)
   menu_item_description=models.TextField(max_length=1000,default='')

   def __str__(self):
       return self.name