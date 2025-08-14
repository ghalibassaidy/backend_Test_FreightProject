from django.db import models

# Create your models here.

class Country(models.Model):
    country_name = models.CharField(max_length=100, unique=True)
    country_flag = models.URLField(max_length=250, blank=True, null=True)
    country_currency = models.CharField(max_length=10)

    def __str__(self):
        return self.country_name
    
class Category(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='categories')
    category_title = models.CharField(max_length=100)
    price_kg = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.category_title} ({self.country.country_name})"