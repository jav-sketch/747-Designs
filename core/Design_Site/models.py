from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Intro(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        self.title

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    # Category tuple
    CATEGORY =(
        ('BC', 'Business Card'),
        ('BR', 'Brochure'),
        ('FR', 'Flyer'),
        ('PR', 'Poster'),
        ('WI', 'Wedding Invitation'),
        
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

     
