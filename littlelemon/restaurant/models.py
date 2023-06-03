from django.db import models
from datetime import datetime   
from django.contrib.auth.models import User 



# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255,default="")
    No_of_guests = models.SmallIntegerField(default=1)
    Date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return f'{self.Name}--->Booking Date: {self.Date}---> Guests: {self.No_of_guests}'
   
   
class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self)->str:
        return self.title


# Add code to create Menu model
class Menu(models.Model):
   name=models.CharField(max_length=200)
   price=models.IntegerField(null=False)
   menu_item_description=models.TextField(max_length=1000,default='')
   
   def __str__(self):
       return f'{self.name} : {str(self.price)}'
    
class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self)->str:
        return self.title

    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu items'