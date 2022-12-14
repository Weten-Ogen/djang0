from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price  = models.DecimalField(default=0,max_digits=10000, decimal_places=2)
    summary = models.TextField(blank=True, null=True)
    featured = models.BooleanField(null=True)
    structured = models.BooleanField()