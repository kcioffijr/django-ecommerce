from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', height_field=300, width_field=300)


class Order(models.Model):
    product = models.ManyToManyField(Product)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    street = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)