from django.db import models
# from django.core.validators import MinLengthValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=25)
    description = models.CharField(max_length=150)
    book_image = models.ImageField(upload_to="images/")
    copies = models.IntegerField(default=1)