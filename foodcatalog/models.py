from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.urls import reverse  # To generate URLS by reversing URL patterns
from django.db.models.signals import post_save
from django.dispatch import receiver 

class Food(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    foodname = models.CharField(max_length=200)
    quantity=models.IntegerField(help_text='Enter in cups or whole numbers')
    calories=models.IntegerField()
    fats=models.IntegerField(help_text='Enter in grams')
    carbs=models.IntegerField(help_text='Enter in grams')
    proteins=models.IntegerField(help_text='Enter in grams')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.foodname

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('food-detail', args=[str(self.id)])

class Meta:
    ordering = ['foodname']






 
