from django.db import models
from django.contrib.auth.models import User
from django. core. validators import MaxValueValidator, MinValueValidator
STATE_CHOICES = (
    ('koshi','koshi'),
    ('Madesh','Madesh'),
    ('Bagmati','Bagmati'),
    ('gandaki','gandaki'),
    ('lumbini','lumbini'),
    ('karnali','karnali'),
    ('sudurpashchim','sudurpashchim'),
)
class Customer (models.Model) :
 user = models.ForeignKey(User, on_delete=models .CASCADE)
 name = models.CharField(max_length=200)
 locality = models.CharField(max_length=200)
 city = models.CharField(max_length=50)
 zipcode = models.IntegerField ()
 state = models.CharField(choices=STATE_CHOICES, max_length=50)
def _str_(self):
 return str(self.id)


CATEGORY_CHOICES = (
    ('M','MOBILE'),
    ('L','LAPTOP'),
    ('TW','TOP WEAR'),
    ('BW','BOTTOM WEAR'),
    ('S','Shoes')
)
class Product (models .Model):
 title = models.CharField(max_length=100)
 selling_price = models.FloatField()
 discounted_price = models.FloatField()
 description = models.TextField()
 brand = models.CharField(max_length=100)
 category = models.CharField( choices=CATEGORY_CHOICES, max_length=2)
 product_image = models.ImageField(upload_to= 'productimg')

 def _str_(self):
  return str(self.id)


class Cart (models .Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 product = models.ForeignKey (Product, on_delete=models.CASCADE)
 quantity = models.PositiveIntegerField(default=1)

 def _str_(self):
  return str(self.id)


STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel')
)

class OrderPlaced (models .Model):
 user = models.ForeignKey (User, on_delete=models.CASCADE)
 customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
 product = models.ForeignKey (Product, on_delete=models.CASCADE)
 quantity = models.PositiveIntegerField(default=1)
 ordered_date = models.DateTimeField(auto_now_add=True)
 status = models.CharField(max_length=50,choices=STATUS_CHOICES, default= 'Pending')
