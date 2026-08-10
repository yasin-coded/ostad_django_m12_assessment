from django.db import models
import datetime

# Create your models here.

class Book (models.Model):
    title = models.CharField (max_length=255)
    author= models.CharField (max_length=100)
    class Category (models.TextChoices):
        FICTION = 'Fiction'
        SCI_FI = 'Sci-Fi'
        BIOGRAPHY = 'Biography'
        FANTASY = 'Fantasy'
        MYSTERY = 'Mystery'
        HORROR = 'Horror'
    category = models.CharField (max_length=50, choices=Category.choices)
    price = models.DecimalField (max_digits=10, decimal_places=2)
    published_date = models.DateField (default=datetime.date.today)

    def __str__(self):
        return self.title