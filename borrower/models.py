from django.db import models
from django.contrib.auth.models import User
from books.models import Book

# Create your models here.
class BorrowedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowed_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_copies = models.IntegerField(default=1)
    date_borrowed = models.DateTimeField(auto_now_add=True, null=False)
    status = models.CharField(max_length=30, default="N/A")

    def save(self, *args, **kwargs):
        if self.borrowed_copies == 0:
            self.status = "Returned"
        else:
            self.status = "In Use"

        super().save(*args, **kwargs)
