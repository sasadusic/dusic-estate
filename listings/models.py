from django.db import models

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=200, default='House')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=40000.00, blank=True, null=True)  
    address = models.CharField(max_length=200, default='123 Main St', blank=True, null=True)
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1, default=2.0, blank=True, null=True)
    bedrooms = models.DecimalField(max_digits=3, decimal_places=1, default=2, blank=True, null=True)
    squares = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00, blank=True, null=True)
    # image = models.ImageField(upload_to='listings/%Y/%m/%d/', blank=True, null=True)
    description = models.TextField(default='This single-family home in Austin has been upgraded with stainless steel appliances and features an open-concept layout.', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f'{self.title} - ${self.price} - {self.address} - {self.squares} sqm'